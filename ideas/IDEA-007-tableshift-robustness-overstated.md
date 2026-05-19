# IDEA-007 — Do tabular "robustness" methods actually recover the distribution-shift gap? (TableShift)

**Domain:** Tabular ML / distribution shift
**Source:** arXiv data-first search, 2026-05-19
**Status:** DATA-VERIFY-PENDING (do NOT claim no-gate until checked)

## The open problem (sourced)

TableShift (arXiv:2312.07577) is a curated, **publicly-accessible**
tabular benchmark where train/test differ by a real domain shift
(finance, health, public policy, civic). Reported in-distribution
accuracy substantially overstates shifted-test performance; whether
the proposed "robustness"/DA methods *actually* recover the gap is
contested — the recurring "looks-good-in-domain, collapses-under-
realistic-shift, and the fixes don't fix it" pattern.

## Why it fits (validated edge)

This is FR-008 / PhysioMind / CardioSafe / GTEx exactly: a metric
that evaporates under an honest split, and an invariance/robustness
"lever" that (per this lab's entire track record) does not move it.
TableShift was *built* to measure precisely this — public, tabular,
small-model, fast on one box.

## Frontier hypothesis (falsifiable)

On ≥3 TableShift tasks: (a) in-distribution → shifted-test accuracy
drops sharply for a from-scratch small model; (b) the standard
"robustness" interventions (reweighting / domain-adversarial / IRM-
style) do NOT close a meaningful fraction of that gap vs a plain
model. Predicted (consistent prior): big drop, fixes ≈ no help.

## Cheapest kill-switch
1. 3 TableShift tasks (verify no-gate access FIRST).
2. Plain GBM/MLP: in-dist split vs the benchmark's domain split.
3. Add one robustness method; measure gap recovered.
4. Falsifier: if the shift drop is small OR robustness recovers
   most of it → the "fixes don't fix" thesis fails here (logged).

## Data / access — GATING ACTION
TableShift is described as publicly accessible; some tasks may pull
from sources needing accounts (e.g., ICU/MIMIC-derived). MUST
verify per-task: pick only tasks with confirmed no-gate data before
building. Do not assume. (This is the loop lesson — every prior
unverified pick was gated.)

## Queued sharper sibling
arXiv:2605.13932 (2026) — scaffold splits on OGB/MoleculeNet still
overstate; time-splits worse. Fresher/sharper FR-008 continuation
but OGB/MoleculeNet access via pip-only packages = friction risk.
Promote only if a direct no-gate OGB zip is verified.

## Sources
- https://arxiv.org/pdf/2312.07577
- https://arxiv.org/html/2605.13932
- https://arxiv.org/pdf/2012.07421 (WILDS, related)
