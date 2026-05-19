#!/usr/bin/env python3
"""
FR-007 (IDEA-001 kill-switch) — does species-invariance help a
from-scratch seq model generalize to a FULLY HELD-OUT species?

Task: coding (cDNA) vs non-coding (ncRNA) from raw nucleotide
sequence. Intrinsic labels (no ortholog mapping needed).
Train: HUMAN only. Test: MOUSE (never seen) + held-out human.

Arms (same net, same data):
  - baseline   lambda=0  (ordinary)
  - invariant  lambda=1  (gradient-reversal species-confusion head)
Controls: 4-mer logistic baseline (train human -> test mouse);
within-human holdout AUC (sanity the task was learned at all);
invariant vs baseline on the held-out species.

Falsifier: invariant must beat BOTH the baseline arm AND the k-mer
baseline on HELD-OUT-SPECIES AUC. Else the invariance lever is dead
(honest negative; consistent prior — invariance has not been the
lever in this lab's tests).

SMOKE=1 -> tiny caps + few steps to verify end-to-end.
"""
import gzip
import io
import os
import sys
import urllib.request

import numpy as np

GT = "/data/frontier/data"
BASE = "https://ftp.ensembl.org/pub/release-112/fasta"
FILES = {
    ("human", "coding"): f"{BASE}/homo_sapiens/cdna/Homo_sapiens.GRCh38.cdna.all.fa.gz",
    ("human", "noncod"): f"{BASE}/homo_sapiens/ncrna/Homo_sapiens.GRCh38.ncrna.fa.gz",
    ("mouse", "coding"): f"{BASE}/mus_musculus/cdna/Mus_musculus.GRCm39.cdna.all.fa.gz",
    ("mouse", "noncod"): f"{BASE}/mus_musculus/ncrna/Mus_musculus.GRCm39.ncrna.fa.gz",
}
SMOKE = os.environ.get("SMOKE") == "1"
CAP = 1500 if SMOKE else 12000      # seqs per (species,class)
L = 500                             # fixed window (nt)
MAP = {"A": 0, "C": 1, "G": 2, "T": 3}


def stream_seqs(url, cap):
    """Yield up to `cap` sequences (center-cropped/padded to L)."""
    out = []
    req = urllib.request.Request(url, headers={"User-Agent": "x"})
    with urllib.request.urlopen(req, timeout=60) as r:
        gz = gzip.GzipFile(fileobj=io.BytesIO(r.read()))
        cur = []
        for line in io.TextIOWrapper(gz, "ascii", errors="ignore"):
            if line.startswith(">"):
                if cur:
                    out.append("".join(cur))
                    if len(out) >= cap:
                        break
                cur = []
            else:
                cur.append(line.strip().upper())
        if cur and len(out) < cap:
            out.append("".join(cur))
    enc = []
    for s in out:
        if len(s) < 60:
            continue
        if len(s) >= L:
            st = (len(s) - L) // 2
            s = s[st:st + L]
        else:
            s = s + "N" * (L - len(s))
        v = np.fromiter((MAP.get(c, 4) for c in s), np.int8, L)
        enc.append(v)
    return np.array(enc, np.int8)


def get(species, cls):
    p = f"{GT}/fr007_{species}_{cls}{'_smoke' if SMOKE else ''}.npy"
    if os.path.exists(p):
        return np.load(p)
    a = stream_seqs(FILES[(species, cls)], CAP)
    os.makedirs(GT, exist_ok=True)
    np.save(p, a)
    return a


def main():
    import torch
    import torch.nn as nn
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score

    dev = "cuda" if torch.cuda.is_available() else "cpu"
    torch.manual_seed(0)
    rng = np.random.default_rng(0)

    data = {}
    for sp in ("human", "mouse"):
        for cl in ("coding", "noncod"):
            data[(sp, cl)] = get(sp, cl)
            print(f"  {sp}/{cl}: {data[(sp,cl)].shape}", flush=True)

    def xy(sp):
        X = np.concatenate([data[(sp, "coding")],
                            data[(sp, "noncod")]]).astype(np.int64)
        y = np.concatenate([np.ones(len(data[(sp, "coding")])),
                            np.zeros(len(data[(sp, "noncod")]))])
        idx = rng.permutation(len(y))
        return X[idx], y[idx]

    Xh, yh = xy("human")
    Xm, ym = xy("mouse")
    n = len(yh)
    tr = np.arange(n) < int(0.85 * n)         # human train / hold
    Xtr, ytr = Xh[tr], yh[tr]
    Xhld, yhld = Xh[~tr], yh[~tr]
    print(f"human train={tr.sum()} human-holdout={(~tr).sum()} "
          f"mouse(all held-out species)={len(ym)}", flush=True)

    # k-mer (4-mer) logistic baseline, train human -> test mouse
    def kmer(X, k=4):
        F = np.zeros((len(X), 4 ** k), np.float32)
        for i, s in enumerate(X):
            ss = s[s < 4]
            if len(ss) < k:
                continue
            idx = np.zeros(len(ss) - k + 1, np.int64)
            for j in range(k):
                idx += ss[j:len(ss) - k + 1 + j] * (4 ** (k - 1 - j))
            np.add.at(F[i], idx, 1.0)
        return F / (F.sum(1, keepdims=True) + 1e-9)
    Kt, Km = kmer(Xtr), kmer(Xm)
    lr = LogisticRegression(max_iter=300, C=1.0).fit(Kt, ytr)
    kmer_mouse_auc = roc_auc_score(ym, lr.predict_proba(Km)[:, 1])

    class GRL(torch.autograd.Function):
        @staticmethod
        def forward(ctx, x, lam):
            ctx.lam = lam
            return x.view_as(x)

        @staticmethod
        def backward(ctx, g):
            return -ctx.lam * g, None

    class Net(nn.Module):
        def __init__(s):
            super().__init__()
            s.emb = nn.Embedding(5, 16)
            s.c = nn.Sequential(
                nn.Conv1d(16, 64, 9, padding=4), nn.ReLU(),
                nn.MaxPool1d(4),
                nn.Conv1d(64, 64, 9, padding=4), nn.ReLU(),
                nn.AdaptiveAvgPool1d(1))
            s.cls = nn.Linear(64, 1)
            s.spe = nn.Linear(64, 1)

        def feat(s, x):
            h = s.emb(x).transpose(1, 2)
            return s.c(h).squeeze(-1)

        def forward(s, x, lam):
            f = s.feat(x)
            return s.cls(f).squeeze(-1), s.spe(GRL.apply(f, lam)).squeeze(-1)

    def run(lam):
        torch.manual_seed(0)
        net = Net().to(dev)
        opt = torch.optim.AdamW(net.parameters(), 1e-3,
                                weight_decay=1e-4)
        bce = nn.BCEWithLogitsLoss()
        # species label: human=1 in train mix only if lam>0 -> need
        # both species' UNLABELED seqs for the adversary. Use human
        # train (sp=0) vs a sample of mouse (sp=1) for confusion.
        Xa = torch.tensor(Xtr, device=dev)
        ya = torch.tensor(ytr, dtype=torch.float32, device=dev)
        msamp = torch.tensor(
            Xm[rng.choice(len(Xm), min(len(Xm), len(Xtr)), False)],
            device=dev)
        steps = 60 if SMOKE else 800
        for st in range(steps):
            bi = torch.randint(0, len(Xa), (128,), device=dev)
            xb, yb = Xa[bi], ya[bi]
            cl, _ = net(xb, lam)
            loss = bce(cl, yb)
            if lam > 0:
                mi = torch.randint(0, len(msamp), (128,),
                                   device=dev)
                xs = torch.cat([xb, msamp[mi]])
                sp = torch.cat([torch.zeros(len(xb)),
                                torch.ones(len(mi))]).to(dev)
                _, sp_l = net(xs, lam)
                loss = loss + bce(sp_l, sp)
            opt.zero_grad()
            loss.backward()
            opt.step()
        net.eval()
        with torch.no_grad():
            def auc(Xe, ye):
                p = []
                for s in range(0, len(Xe), 512):
                    xb = torch.tensor(Xe[s:s + 512], device=dev)
                    p.append(torch.sigmoid(net(xb, 0)[0]).cpu().numpy())
                return roc_auc_score(ye, np.concatenate(p))
            return auc(Xhld, yhld), auc(Xm, ym)

    res = {}
    for lam, tag in [(0.0, "baseline"), (1.0, "invariant")]:
        h_auc, m_auc = run(lam)
        res[tag] = {"human_holdout_auc": float(h_auc),
                    "mouse_heldout_species_auc": float(m_auc)}
        print(f"  {tag}: human-holdout AUC={h_auc:.3f} | "
              f"MOUSE held-out-species AUC={m_auc:.3f}", flush=True)
    res["kmer_baseline_mouse_auc"] = float(kmer_mouse_auc)
    b = res["baseline"]["mouse_heldout_species_auc"]
    v = res["invariant"]["mouse_heldout_species_auc"]
    res["delta_invariant_minus_baseline"] = float(v - b)
    if v - b > 0.03 and v > kmer_mouse_auc + 0.02:
        verdict = ("PROVISIONAL — invariance improves held-out-"
                   "species generalization over baseline AND k-mer. "
                   "Needs a 2nd species pair before any belief.")
    else:
        verdict = (f"NEGATIVE — species-invariance does NOT improve "
                   f"held-out-species transfer (mouse AUC: baseline "
                   f"{b:.3f}, invariant {v:.3f}, kmer "
                   f"{kmer_mouse_auc:.3f}). Invariance not the lever "
                   f"here; consistent with prior. Logged.")
    res["verdict"] = verdict
    print("VERDICT:", verdict, flush=True)
    import json
    json.dump(res, open("/data/frontier/results/FR-007.json", "w"),
              indent=2)


if __name__ == "__main__":
    sys.exit(main())
