#!/usr/bin/env python3
"""
FR-001 — honest falsifier for the dv/v earthquake-precursor claim.

Builds ON ~/seismic-stress (does NOT duplicate its ResNet). The
ResNet over hundreds of overlapping 21-day windows from 35-day
series has effective n ~= 16 (8 events + 8 negatives) and severe
within-event autocorrelation -> any AUC there is untrustworthy.

This collapses each window to ONE feature vector (no sliding leak),
runs leave-one-window-out, and asks the only honest question at this
n: is the real AUC above an EVENT-LABEL PERMUTATION NULL and above a
trivial dv/v-trend baseline?

Falsifier: real LOO-AUC must beat the permutation null (p<0.05) AND
the trivial baseline. With n~=16 even a 'pass' is provisional and
needs many more events before it means anything — stated, not hidden.
"""
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

sys.path.insert(0, str(Path.home() / "seismic-stress"))
from config import (EVENTS, NEGATIVE_WINDOWS, DATA_DVV,  # noqa
                     PRE_RUPTURE_DAYS, DAYS_BEFORE_EVENT)

SEQ = 21        # pre-rupture window length (days) used for features
NPERM = 2000


def load(wid):
    p = DATA_DVV / f"{wid}_dvv.npy"
    if not p.exists():
        return None
    d = np.load(str(p))                    # [n_pairs, n_days]
    if d.ndim != 2 or d.shape[1] < SEQ + 2:
        return None
    return np.nan_to_num(d, nan=0.0)


def feats(dvv):
    """One vector per window: no autocorrelated sliding windows.
    Use the last SEQ days; per-pair summarise then aggregate."""
    w = dvv[:, -SEQ:]                       # [n_pairs, SEQ]
    # per-pair: slope, mean, std, last-minus-first, min
    t = np.arange(SEQ)
    sl = np.array([np.polyfit(t, p, 1)[0] for p in w])
    mn = w.mean(1)
    sd = w.std(1)
    df = w[:, -1] - w[:, 0]
    mi = w.min(1)
    # aggregate across pairs (mean + most-negative) -> fixed length
    return np.array([
        sl.mean(), sl.min(), mn.mean(), sd.mean(),
        df.mean(), df.min(), mi.min(),
    ], np.float32)


def main():
    X, y, ids = [], [], []
    for ev in EVENTS:
        d = load(ev["id"])
        if d is not None:
            X.append(feats(d))
            y.append(1)
            ids.append(ev["id"])
    for ng in NEGATIVE_WINDOWS:
        d = load(ng["id"])
        if d is not None:
            X.append(feats(d))
            y.append(0)
            ids.append(ng["id"])
    X = np.array(X, np.float32)
    y = np.array(y)
    n = len(y)
    print(f"loaded windows: {n}  (pos={int(y.sum())} "
          f"neg={int((y==0).sum())})", flush=True)
    if n < 8 or y.sum() < 3 or (y == 0).sum() < 3:
        print("DATA NOT READY — dv/v compute incomplete. "
              "Not running on partial data (would be a fake result).",
              flush=True)
        json.dump({"status": "data_not_ready", "n": int(n)},
                  open("/data/frontier/results/FR-001.json", "w"))
        return

    def loo_auc(Xf, yy):
        oof = np.zeros(n)
        for i in range(n):
            tr = [j for j in range(n) if j != i]
            mu, sg = Xf[tr].mean(0), Xf[tr].std(0) + 1e-8
            c = LogisticRegression(max_iter=2000, C=0.5)
            c.fit((Xf[tr] - mu) / sg, yy[tr])
            oof[i] = c.predict_proba(((Xf[i] - mu) / sg)[None])[0, 1]
        return roc_auc_score(yy, oof), oof

    auc, _ = loo_auc(X, y)
    # trivial baseline: single feature = most-negative dv/v change
    base, _ = loo_auc(X[:, [5]], y)
    rng = np.random.default_rng(0)
    # event-label permutation null: fixed OOF predictions, shuffle
    # the true labels, recompute AUC NPERM times
    base_oof = loo_auc(X, y)[1]
    nd = []
    for _ in range(NPERM):
        yp = rng.permutation(y)
        nd.append(roc_auc_score(yp, base_oof))
    nd = np.array(nd)
    p = float((1 + (nd >= auc).sum()) / (1 + NPERM))
    n95 = float(np.percentile(nd, 95))

    res = dict(n=int(n), pos=int(y.sum()), loo_auc=float(auc),
               trivial_baseline_auc=float(base),
               perm_p=p, perm_null95=n95, n_perm=NPERM)
    print(f"LOO-AUC={auc:.3f}  trivial-baseline={base:.3f}  "
          f"perm_p={p:.3f}  null95={n95:.3f}", flush=True)
    if p < 0.05 and auc > base + 0.03:
        v = (f"PROVISIONAL SIGNAL — beats permutation null (p={p:.3f})"
             f" and trivial baseline. CAVEAT: n={n} (~8 events). Not "
             f"believable until many more events; needs independent "
             f"reproduction. Do NOT overclaim.")
    else:
        v = (f"NEGATIVE — dv/v precursor not above the event-label "
             f"permutation null / trivial baseline at honest n={n}. "
             f"The ResNet's high AUC (if any) is small-n autocorrelation"
             f", not signal. Logged.")
    res["verdict"] = v
    print("VERDICT:", v, flush=True)
    json.dump(res, open("/data/frontier/results/FR-001.json", "w"),
              indent=2)


if __name__ == "__main__":
    sys.exit(main())
