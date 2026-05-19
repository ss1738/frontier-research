# IDEA-001 — Genomic regulatory models that actually generalize to a fully held-out species

**Domain:** Genomics / regulatory deep learning
**Source of idea:** internet research, 2026-05-19
**Status:** CANDIDATE (needs feasibility verify before any run)

## The open problem (sourced, not asserted)

Current genomic deep-learning models predict regulatory signal
(enhancers, accessibility, expression) but **do not generalize
across cell types or across species** — and the field largely
*hides this* by testing on held-out **chromosomes within the same
species**, not a held-out species.

- "None of the existing predictive approaches allow generalization
  of the predictions across cell types." — review, NCBI PMC7678316.
- "Current genomic deep learning architectures generalize across
  grass species but **not alleles**." — bioRxiv 2024.04.11.589024.
- "It is common to test on held-out chromosomes *within the training
  species*, rather than a completely held-out species." — same.
- Active 2026 work (evolutionary transfer learning, bioRxiv
  2026.04.07.717039) confirms this is an *unsolved, live* gap, not
  a closed one.

So the gap is precise and current: **leak-free, fully-held-out-
species evaluation of regulatory prediction is rare, and models that
pass it do not exist in the open literature.**

## Why this fits (the unfair-advantage angle)

This is the exact failure mode this lab keeps catching elsewhere
(PhysioMind cohort artifact, CardioSafe ChEMBL→drug, GTEx PSI):
models that look strong under a soft split collapse under an honest
one. Here it is an *acknowledged, unsolved, publishable* problem with
fully public data — not a manufactured one.

## Frontier hypothesis (falsifiable)

A small from-scratch sequence model with an explicitly
**species-invariant** training objective (adversarial species-
confusion on the representation, like the RR-invariant idea, but for
genomic regulatory signal) generalizes to a **fully held-out
species** better than (a) the same model without the invariance
term and (b) standard within-species-chromosome-split models
evaluated cross-species.

## Cheapest kill-switch (hours, before any scale)

1. 2 species, 1 regulatory task (e.g., promoter / open-chromatin
   from raw sequence), public (Ensembl/UCSC; no registration).
2. Train on species A, **evaluate on species B (never seen)**,
   ortholog-aware so it is a true generalization test.
3. Baselines that MUST be beaten: k-mer/positional logistic; the
   non-invariant version of the same net; and a label-shuffle null.
4. Falsifier: if the invariant model does **not** beat the non-
   invariant one on the held-out species above the null, the
   invariance lever is dead here → log NEGATIVE, move on.

Honest prior (from this session's track record): invariance-style
levers have repeatedly NOT rescued cross-domain transfer. Expected
outcome is a negative; a *positive that survives a second species
pair* would be genuinely novel and worth escalating.

## Data (public, no gate)

Ensembl / UCSC genome FASTA + regulatory annotations for ≥2 species
with orthology maps (e.g., human↔mouse, or two grasses per the
cited paper). Few hundred MB. No dbGaP/registration.

## Next action

Feasibility-verify the exact public files + ortholog mapping on the
box BEFORE writing the experiment (verify-before-build). Then build
the kill-switch as FR-007 in the experiment loop.

## Sources
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7678316/
- https://www.biorxiv.org/content/10.1101/2024.04.11.589024.full.pdf
- https://www.biorxiv.org/content/10.64898/2026.04.07.717039v1
- https://www.biorxiv.org/content/10.1101/2021.12.31.474623.full.pdf
