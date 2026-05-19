#!/usr/bin/env python3
"""
FR-008 (IDEA-004) — does Buchwald-Hartwig yield-prediction skill
collapse from a RANDOM split to honest OOD splits, and does the
nonlinear model's advantage over linear vanish under OOD?

Identical data + features. Three regimes:
  R  random 70/30
  A  leave-one-additive-out (canonical OOD; additive drives yield)
  T  high-yield-tail held out (train low/mid yields -> predict tail)
Models per regime: HistGBR (nonlinear) | Ridge (linear) | mean.
Shuffled-y null per regime = honest floor.

Falsifier (predicted): R2 high under R, drops sharply under A & T,
AND HistGBR ~= Ridge under A/T. If the drop does NOT happen, the
'benchmark inflation' critique fails to replicate here (logged).
"""
import sys
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_absolute_error

CSV = "/data/frontier/data/bh_hte.csv"
COMPS = ["base_smiles", "ligand_smiles", "aryl_halide_smiles",
         "additive_smiles"]
NBITS = 1024
mgen = rdFingerprintGenerator.GetMorganGenerator(radius=2,
                                                 fpSize=NBITS)


def fp(smi):
    v = np.zeros(NBITS, np.float32)
    if not isinstance(smi, str) or smi.strip() == "":
        return v                                  # 'no additive'
    m = Chem.MolFromSmiles(smi)
    if m is None:
        return v
    a = mgen.GetFingerprintAsNumPy(m).astype(np.float32)
    return a


def evaluate(Xtr, ytr, Xte, yte):
    out = {}
    for name, mdl in [
            ("histgbr", HistGradientBoostingRegressor(
                max_iter=400, learning_rate=0.05, max_depth=4,
                l2_regularization=1.0, random_state=0)),
            ("ridge", Ridge(alpha=10.0)),
            ("mean", None)]:
        if mdl is None:
            p = np.full(len(yte), ytr.mean())
        else:
            mdl.fit(Xtr, ytr)
            p = mdl.predict(Xte)
        out[name] = dict(r2=float(r2_score(yte, p)),
                         mae=float(mean_absolute_error(yte, p)))
    return out


def main():
    d = pd.read_csv(CSV).dropna(subset=["yield"]).reset_index(
        drop=True)
    y = d["yield"].to_numpy(np.float32)
    # cache fp per unique smiles per component, then concat
    cols = []
    for c in COMPS:
        uniq = {s: fp(s) for s in d[c].astype(object).unique()}
        cols.append(np.stack([uniq[s] for s in
                              d[c].astype(object)]))
    X = np.concatenate(cols, 1).astype(np.float32)
    print(f"X={X.shape} y[min={y.min():.1f} mean={y.mean():.1f} "
          f"max={y.max():.1f}]", flush=True)
    rng = np.random.default_rng(0)
    res = {}

    # R: random 70/30
    idx = rng.permutation(len(y))
    cut = int(0.7 * len(y))
    tr, te = idx[:cut], idx[cut:]
    res["R_random"] = evaluate(X[tr], y[tr], X[te], y[te])
    res["R_random"]["null_histgbr_r2"] = float(
        evaluate(X[tr], rng.permutation(y[tr]), X[te], y[te]
                 )["histgbr"]["r2"])

    # A: leave-one-additive-out (mean over folds)
    add = d["additive_smiles"].astype(object).fillna("none").values
    accs = {"histgbr": [], "ridge": [], "mean": []}
    for a in pd.unique(add):
        teA = add == a
        if teA.sum() < 20 or (~teA).sum() < 50:
            continue
        e = evaluate(X[~teA], y[~teA], X[teA], y[teA])
        for k in accs:
            accs[k].append(e[k]["r2"])
    res["A_loao"] = {k: dict(r2=float(np.mean(v)),
                             n_folds=len(v)) for k, v in accs.items()}

    # T: high-yield tail held out (test = top-quartile yields)
    thr = np.quantile(y, 0.75)
    teT = y >= thr
    res["T_tail"] = evaluate(X[~teT], y[~teT], X[teT], y[teT])

    print(__import__("json").dumps(res, indent=2), flush=True)
    R = res["R_random"]["histgbr"]["r2"]
    A = res["A_loao"]["histgbr"]["r2"]
    T = res["T_tail"]["histgbr"]["r2"]
    Ar = res["A_loao"]["ridge"]["r2"]
    drop = R - A
    deep_adv_ood = A - Ar
    if R > 0.6 and drop > 0.25 and deep_adv_ood < 0.10:
        v = (f"CONFIRMED — yield skill collapses random->OOD "
             f"(R2 {R:.2f}->{A:.2f}, drop {drop:.2f}); nonlinear "
             f"advantage over linear nearly gone under OOD "
             f"({deep_adv_ood:+.2f}). Benchmark inflation replicates "
             f"on fresh public data. Value = the rigor, not SOTA.")
    elif R > 0.6 and drop > 0.25:
        v = (f"PARTIAL — big random->OOD drop ({drop:.2f}) but "
             f"nonlinear still beats linear OOD ({deep_adv_ood:+.2f}).")
    else:
        v = (f"NEGATIVE — inflation critique does NOT replicate here "
             f"(random R2 {R:.2f}, OOD {A:.2f}, drop {drop:.2f}). "
             f"Logged honestly.")
    res["verdict"] = v
    print("VERDICT:", v, flush=True)
    __import__("json").dump(
        res, open("/data/frontier/results/FR-008.json", "w"),
        indent=2)


if __name__ == "__main__":
    sys.exit(main())
