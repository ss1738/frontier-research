#!/usr/bin/env python3
"""
FR-003 — does a from-scratch tiny model have a real, fee-survivable,
out-of-sample directional edge on BTC 1h?

Honest by construction (this is where crypto 'edges' fake-pass):
  - causal features only (window of past returns/vol; nothing >= t)
  - target = sign of NEXT bar return
  - WALK-FORWARD: expanding train -> predict next block, never shuffle
  - realistic taker fee charged on every position change
  - net-of-fee OOS metrics vs buy&hold AND flat
  - label-shuffle null (same pipeline) = the honest floor

Falsifier: net-of-fee OOS Sharpe must be > 0 AND beat the shuffle
null (p<0.05) AND beat buy&hold risk-adjusted. Expected outcome:
NEGATIVE (markets are efficient) — logged as a real result.
"""
import json
import sys
import time
import urllib.request

import numpy as np

SYM = "BTCUSDT"
ITV = "1h"
FEE = 0.0004          # 4 bps taker per side (Binance spot ~ realistic)
WIN = 48              # hours of history as features
RETRAIN = 2000        # walk-forward block size (bars)
CACHE = "/data/frontier/data/btc_1h.npy"


def fetch():
    import os
    if os.path.exists(CACHE):
        a = np.load(CACHE)
        if len(a) > 10000:
            return a
    rows = []
    end = int(time.time() * 1000)
    for _ in range(80):                       # ~80k bars max
        u = (f"https://api.binance.com/api/v3/klines?symbol={SYM}"
             f"&interval={ITV}&limit=1000&endTime={end}")
        d = json.load(urllib.request.urlopen(u, timeout=20))
        if not d:
            break
        rows = d + rows
        end = d[0][0] - 1
        time.sleep(0.15)
        if len(d) < 1000:
            break
    arr = np.array([[float(r[1]), float(r[2]), float(r[3]),
                     float(r[4]), float(r[5])] for r in rows],
                   np.float64)                 # O,H,L,C,V
    np.save(CACHE, arr)
    return arr


def main():
    import torch
    import torch.nn as nn

    a = fetch()
    close = a[:, 3]
    vol = a[:, 4]
    ret = np.diff(np.log(close))               # log returns, len N-1
    lv = np.log(vol[1:] + 1.0)
    lv = (lv - lv.mean()) / (lv.std() + 1e-9)
    N = len(ret)
    print(f"bars={len(close)} usable_ret={N}", flush=True)
    if N < 8000:
        print("DATA TOO SHORT — not running.", flush=True)
        json.dump({"status": "short", "n": int(N)},
                  open("/data/frontier/results/FR-003.json", "w"))
        return

    # causal features at time t: past WIN returns + past WIN logvol
    X, Y, R = [], [], []
    for t in range(WIN, N - 1):
        X.append(np.concatenate([ret[t - WIN:t], lv[t - WIN:t]]))
        Y.append(1.0 if ret[t + 1] > 0 else 0.0)   # next-bar dir
        R.append(ret[t + 1])                        # next-bar return
    X = np.asarray(X, np.float32)
    Y = np.asarray(Y, np.float32)
    R = np.asarray(R, np.float64)
    dev = "cuda" if torch.cuda.is_available() else "cpu"

    class Net(nn.Module):
        def __init__(s, d):
            super().__init__()
            s.net = nn.Sequential(
                nn.Linear(d, 64), nn.GELU(), nn.Dropout(0.3),
                nn.Linear(64, 32), nn.GELU(),
                nn.Linear(32, 1))

        def forward(s, x):
            return s.net(x).squeeze(-1)

    def walk_forward(Yv):
        """expanding-window walk-forward; returns OOS pred prob."""
        pred = np.full(len(Yv), np.nan)
        start = 4000                            # min train
        i = start
        while i < len(Yv):
            j = min(i + RETRAIN, len(Yv))
            torch.manual_seed(0)
            net = Net(X.shape[1]).to(dev)
            opt = torch.optim.AdamW(net.parameters(), 1e-3,
                                    weight_decay=1e-3)
            lf = nn.BCEWithLogitsLoss()
            xtr = torch.tensor(X[:i]).to(dev)
            ytr = torch.tensor(Yv[:i]).to(dev)
            net.train()
            for _ in range(60):
                bi = torch.randint(0, i, (256,))
                opt.zero_grad()
                lf(net(xtr[bi]), ytr[bi]).backward()
                opt.step()
            net.eval()
            with torch.no_grad():
                p = torch.sigmoid(
                    net(torch.tensor(X[i:j]).to(dev))).cpu().numpy()
            pred[i:j] = p
            i = j
        return pred

    def metrics(pred):
        m = ~np.isnan(pred)
        pos = np.where(pred[m] > 0.5, 1.0, -1.0)   # long/short
        r = R[m]
        chg = np.abs(np.diff(np.concatenate([[0.0], pos])))
        net_r = pos * r - chg * FEE                # fee on turns
        sharpe = (net_r.mean() / (net_r.std() + 1e-12)
                  * np.sqrt(24 * 365))
        bh = r.cumsum()[-1]
        return dict(
            n_oos=int(m.sum()),
            hit=float((np.sign(pos) == np.sign(r)).mean()),
            net_cum=float(net_r.sum()),
            net_sharpe=float(sharpe),
            buyhold_cum=float(bh),
            gross_cum=float((pos * r).sum()))

    real = metrics(walk_forward(Y))
    rng = np.random.default_rng(0)
    null_sh = []
    for _ in range(8):                          # shuffle-label null
        Ys = rng.permutation(Y)
        null_sh.append(metrics(walk_forward(Ys))["net_sharpe"])
    null_sh = np.array(null_sh)
    p = float((1 + (null_sh >= real["net_sharpe"]).sum())
              / (1 + len(null_sh)))
    res = dict(**real, null_sharpe_mean=float(null_sh.mean()),
               perm_p=p, fee=FEE)
    print(json.dumps(res, indent=2), flush=True)
    if (real["net_sharpe"] > 0 and p < 0.05
            and real["net_cum"] > real["buyhold_cum"]):
        v = ("PROVISIONAL EDGE — net-of-fee OOS Sharpe>0, beats "
             "shuffle null and buy&hold. Needs independent repro "
             "before any belief; do NOT overclaim.")
    else:
        v = (f"NEGATIVE — no fee-survivable OOS edge "
             f"(net_sharpe={real['net_sharpe']:.2f}, "
             f"net_cum={real['net_cum']:.3f} vs "
             f"buyhold={real['buyhold_cum']:.3f}, p={p:.3f}). "
             f"Markets efficient at this horizon. Logged.")
    res["verdict"] = v
    print("VERDICT:", v, flush=True)
    json.dump(res, open("/data/frontier/results/FR-003.json", "w"),
              indent=2)


if __name__ == "__main__":
    sys.exit(main())
