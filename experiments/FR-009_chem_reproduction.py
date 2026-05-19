#!/usr/bin/env python3
"""
FR-009 — INDEPENDENT REPRODUCTION of FR-008 (IDEA-004).

System protocol: no idea graduates on one run. FR-008 found
random->OOD yield-skill collapse with HistGBR + leave-one-ADDITIVE-
out. This reproduces it with DELIBERATELY DIFFERENT choices:
  - different OOD split: leave-one-LIGAND-out (+ high-yield tail)
  - different models: RandomForest, small MLP (vs FR-008 HistGBR)
Same verified on-box data (bh_hte.csv). If the collapse + magnitude
reproduce under independent split & model -> IDEA-004 -> REPRODUCED.
If not -> FR-008 was split/model-specific (honest, important).
"""
import json
import sys
import numpy as np
import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

CSV = "/data/frontier/data/bh_hte.csv"
COMPS = ["base_smiles", "ligand_smiles", "aryl_halide_smiles",
         "additive_smiles"]
NB = 1024
mg = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=NB)


def fp(s):
    v = np.zeros(NB, np.float32)
    if not isinstance(s, str) or not s.strip():
        return v
    m = Chem.MolFromSmiles(s)
    return mg.GetFingerprintAsNumPy(m).astype(np.float32) if m is not None else v


def models():
    return {
        "rf": RandomForestRegressor(n_estimators=300, max_depth=14,
                                    n_jobs=8, random_state=0),
        "mlp": MLPRegressor(hidden_layer_sizes=(256, 64),
                            alpha=1e-3, max_iter=300,
                            early_stopping=True, random_state=0),
        "ridge": Ridge(alpha=10.0),
        "mean": None,
    }


def ev(Xtr, ytr, Xte, yte):
    o = {}
    for k, m in models().items():
        if m is None:
            p = np.full(len(yte), ytr.mean())
        else:
            m.fit(Xtr, ytr)
            p = m.predict(Xte)
        o[k] = float(r2_score(yte, p))
    return o


def main():
    d = pd.read_csv(CSV).dropna(subset=["yield"]).reset_index(drop=True)
    y = d["yield"].to_numpy(np.float32)
    cols = []
    for c in COMPS:
        u = {s: fp(s) for s in d[c].astype(object).unique()}
        cols.append(np.stack([u[s] for s in d[c].astype(object)]))
    X = np.concatenate(cols, 1).astype(np.float32)
    rng = np.random.default_rng(1)            # different seed vs FR-008
    res = {}

    idx = rng.permutation(len(y))
    cut = int(0.7 * len(y))
    res["R_random"] = ev(X[idx[:cut]], y[idx[:cut]],
                         X[idx[cut:]], y[idx[cut:]])

    lig = d["ligand_smiles"].astype(object).fillna("none").values
    acc = {k: [] for k in models()}
    for L in pd.unique(lig):
        te = lig == L
        if te.sum() < 30 or (~te).sum() < 100:
            continue
        e = ev(X[~te], y[~te], X[te], y[te])
        for k in acc:
            acc[k].append(e[k])
    res["L_loligo"] = {k: dict(r2=float(np.mean(v)), folds=len(v))
                       for k, v in acc.items()}

    thr = np.quantile(y, 0.75)
    te = y >= thr
    res["T_tail"] = ev(X[~te], y[~te], X[te], y[te])

    print(json.dumps(res, indent=2), flush=True)
    R = res["R_random"]["rf"]
    L = res["L_loligo"]["rf"]["r2"]
    T = res["T_tail"]["rf"]
    drop = R - L
    if R > 0.6 and drop > 0.25 and T < 0.0:
        v = (f"REPRODUCED — FR-008 collapse holds under DIFFERENT "
             f"split (ligand) & model (RF): random R2 {R:.2f} -> "
             f"leave-1-ligand-out {L:.2f} (drop {drop:.2f}); "
             f"high-yield tail R2 {T:.2f} (<0). IDEA-004 graduates "
             f"to REPRODUCED. Robust, not split/model-specific.")
    elif R > 0.6 and drop > 0.15:
        v = (f"PARTIAL REPRO — collapse present but weaker under "
             f"independent split/model (R {R:.2f}->{L:.2f}, "
             f"tail {T:.2f}). Effect real but magnitude varies.")
    else:
        v = (f"NOT REPRODUCED — under ligand split + RF the collapse "
             f"is much smaller (R {R:.2f}->{L:.2f}). FR-008 may be "
             f"additive-split / HistGBR-specific. Honest, important.")
    res["verdict"] = v
    print("VERDICT:", v, flush=True)
    json.dump(res, open("/data/frontier/results/FR-009.json", "w"),
              indent=2)


if __name__ == "__main__":
    sys.exit(main())
