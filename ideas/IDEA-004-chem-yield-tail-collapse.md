# IDEA-004 — Reaction-yield models collapse under high-yield-tail / OOD splits

**Domain:** Chemistry / reaction informatics
**Source:** session-2 internet research, cross-pass winner, 2026-05-19
**Status:** SELECTED → next experiment FR-008 (verify data first)

## The open problem (sourced, quantified)

Reaction-yield ML reports strong random-split R², but the
*useful* prediction (the optimal, high-yield reaction) is in the
rare tail and is OOD — under imbalanced-regression / tail splits
the apparent skill largely disappears.
- Liu et al., "Are We Making Much Progress? Revisiting Chemical
  Reaction Yield Prediction," arXiv:2402.05971, ACM Web Conf 2024.

## Why it fits (unfair-advantage angle)

This IS this lab's repeated, demonstrated competence: a metric that
looks real on a soft split and collapses on the honest one
(PhysioMind cohort, CardioSafe ChEMBL→drug, GTEx PSI, COSWARA batch
confound, SAE≤baselines). Here it is a *published, quantified,
open-data* instance — a clean falsification with predicted direction.

## Frontier hypothesis (falsifiable, sharp)

On identical HTE data, a small from-scratch model's yield-prediction
skill drops substantially from a random split to a high-yield-tail /
scaffold split, and a simple mean/linear baseline closes most of the
"deep model advantage" under the honest split.

## Cheapest kill-switch (decisive, hours)

1. Buchwald–Hartwig + Suzuki HTE sets (Doyle/Dreher; Open Reaction
   Database) — fully open, no registration.
2. Same small model, two splits: (a) random, (b) high-yield-tail /
   reactant-scaffold held-out.
3. Falsifier (predicted): random-split R² high; tail-split R² drops
   sharply AND deep model ≈ linear/mean baseline on the tail.
   - If the drop does NOT happen → the inflation critique fails to
     replicate here (still a logged result).
   - If it does → quantified confirmation on fresh data; the value
     is the rigor, not a new SOTA. Do NOT overclaim.

## Data / access
Open Reaction Database (open.reactiondatabase.org) + Doyle/Dreher
HTE CSVs (public, widely mirrored). VERIFY exact no-gate file on the
box before building.

## Novelty-risk (honest, from the comparison)
LOW novelty as an *idea* — the critique is published. The value is a
clean independent falsification under tail-split on public data with
a predicted direction (replication-with-teeth). Not a landmark; a
solid, defensible loop result that matches the lab's edge.

## Sources
- https://arxiv.org/html/2402.05971v2
