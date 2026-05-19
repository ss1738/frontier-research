# Hypothesis backlog — one experiment/day, rotate domains

Each is a from-scratch small model (1M–~1B params), public/owned
data, with a cheap falsifier. Negatives are logged, not discarded.

| ID | Domain | Hypothesis | Data | Params | Cheap falsifier |
|----|--------|------------|------|--------|-----------------|
| FR-001 | Geophysics | A tiny seq model predicts an imminent ambient-noise dv/v drop (stress precursor) earlier than a persistence/AR baseline | your own seismic-stress `compute_dvv.py` output (already running on the box) | ~1–5M | forward-chained time CV; must beat persistence + AR(p) out-of-sample or NEGATIVE |
| FR-002 | RF / radio | From-scratch tiny model classifies modulation / detects anomaly from raw IQ better than a matched-filter baseline at low SNR | RadioML 2018.01A (public) | ~2–10M | held-out SNR bins; must beat energy/cumulant baseline or NEGATIVE |
| FR-003 | Markets | Small seq model has out-of-sample directional edge on liquid crypto after realistic fees | public Binance 1m klines | ~1–5M | walk-forward, fee-aware; must beat zero-return + AR or NEGATIVE (expected) |
| FR-004 | Genomics | Tiny CNN predicts splice sites from raw sequence on a chromosome-held-out split as well as known baselines | GENCODE/Ensembl public | ~1–5M | chromosome-grouped split; must beat positional/k-mer baseline or NEGATIVE |
| FR-005 | Materials | From-scratch composition-only net predicts formation energy near Roost-class baselines | Materials Project (public API) | ~1–10M | element-held-out split; must beat mean+linear or NEGATIVE |
| FR-006 | Networking | Tiny model flags intrusions from flow features generalizing across attack types | CIC-IDS2017 (public) | ~1–3M | attack-type-held-out; must beat IsolationForest or NEGATIVE |

Rotation: FR-001 today. Each day pick the next undone row (or a new
one). Promising rows get an independent second-run before graduating.

## FR-001 — full spec (today)

**Claim:** ambient-noise seismic velocity change (dv/v) carries a
short-horizon precursor; a small causal sequence model on rolling
dv/v + its features predicts the *next-window drop* earlier/better
than persistence or AR.

**Why possibly new:** ML precursor work on dv/v exists but a clean,
falsifiable, leak-free small-model forward-chained test on your own
continuously-generated dv/v stream is not a standard published
result. Uses data you are *already producing on the box*.

**Falsifier (cheap, hours):** strictly forward-chained CV (train
past → predict future, no shuffling). The model must beat BOTH
(a) persistence (predict no change) and (b) AR(p) on out-of-sample
AUC/MAE for "drop in next window." If it does not, FR-001 = NEGATIVE,
logged, move to FR-002 tomorrow.

**Status:** kill-switch build is the next action.
