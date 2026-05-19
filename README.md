# Frontier Research — operating system

Purpose: a daily practice of training small-parameter models
(1M → ~1B params) from scratch, across many domains and methods, to
find something genuinely new. Not a one-day thing. It accumulates.

Owner: Satyawan. Rig: satyawan-1 (RTX 5090, Tailscale 100.89.103.10),
env `/data/envs/scfm`. Box mirror: `/data/frontier/`.

## The loop (run every day, log every run)

1. **Pick** one hypothesis. Write it in `hypotheses/FR-NNN.md`:
   the claim, why it could be new (what is NOT already done),
   the data, the model (param count), and the **falsifier** —
   the cheapest result that would prove it wrong.
2. **Cheap kill-switch first.** Smallest experiment that could
   falsify it. Hours, not days. If it dies, log the negative.
3. **Scale only if it survives.** Bigger model / more data only
   after the kill-switch passes.
4. **Honest eval, always.** Leak-free splits, permutation/shuffle
   null, real baselines. A clean negative is a logged result, not
   a failure. No fabricated wins, ever. (This is the standard that
   makes the corpus trustworthy — it is the whole point.)
5. **Log it** in `REGISTRY.md` — every hypothesis, status, outcome.
   Negatives stay in the record; that is how a conclusion is
   reached over time.

## Why rigor is non-negotiable here

The value compounds only if every entry is true. One fabricated or
unchecked "win" poisons the whole corpus and the conclusion it is
building toward. Rigor is not caution — it is what makes this worth
doing at all.

## Layout

```
hypotheses/   FR-NNN.md   — one per idea (claim, falsifier, plan)
experiments/  FR-NNN_*.py — the code that ran
results/      FR-NNN_*.json/.log — outcomes
data/         shared datasets on the box
REGISTRY.md   — the running ledger (source of truth)
```

## Two-session compare (later)

When a hypothesis looks promising, a second independent run/agent
reproduces it from the registry entry alone. It only counts if it
survives the independent reproduction. No idea graduates on one run.
