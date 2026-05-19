# IDEA-002 — Cross-tokamak disruption prediction that survives a fully held-out machine

**Domain:** Fusion / plasma control
**Source:** internet research (session-1), 2026-05-19
**Status:** CANDIDATE — top pick this scan. Needs data-access verify.

## The open problem (sourced)

Tokamak disruption prediction works *per-device* but does **not**
transfer to a new machine — the central open barrier to a reactor-
ready predictor (ITER will have almost no its-own disruption data).

- "Most data-driven approaches were developed and optimized for one
  device and did not show promising cross-device predictive
  ability." — cross-tokamak disruption literature (arXiv 2309.05361;
  hybrid model arXiv 2007.01401).
- **DisruptionBench (2024)** — *first* benchmark explicitly built to
  test cross-tokamak generalizability: ~30k trials, DIII-D + Alcator
  C-Mod + EAST (MIT, dspace 1721.1/150682; arXiv 2410.11065). Its
  existence = the field admits this is unsolved and now measurable.

## Why it fits (unfair-advantage angle)

This is *exactly* the failure mode this lab keeps nailing
(PhysioMind cohort, CardioSafe ChEMBL→drug, GTEx, FR-007): strong
within-domain, collapses on a truly held-out domain. Here the
held-out structure is **pre-built and public** (DisruptionBench),
the stakes are frontier (fusion), and it's an acknowledged open
barrier — not a manufactured one.

## Frontier hypothesis (falsifiable)

A small from-scratch model with a **device-invariant** representation
(dimensionless physics-normalized inputs + adversarial machine-
confusion head) predicts disruptions on a **fully held-out tokamak**
(train DIII-D+C-Mod → test EAST, never seen) above (a) the same
model without invariance and (b) the DisruptionBench leaderboard
floor.

## Cheapest kill-switch (the honest gate)

1. Pull DisruptionBench (or its DIII-D/C-Mod/EAST signal subset).
2. Train on 2 machines, test on the 3rd (never seen) — the bench's
   own protocol.
3. Falsifier: device-invariant model must beat the non-invariant
   baseline AND a simple per-signal threshold on the held-out
   machine. If not → invariance dead here (consistent prior; honest
   negative, logged). NOTE: this lab's track record says invariance
   has NEVER been the lever — expected outcome is negative; a
   positive that survives a 2nd held-out machine would be genuinely
   new and high-value.

## Data / access

DisruptionBench / multi-tokamak datasets — **must verify access
before building** (some fusion datasets need a request; DIII-D/EAST
public subsets exist). VERIFY-BEFORE-BUILD: confirm a no-gate path
or scope to whatever public tokamak signal data is directly
downloadable. Do not assume.

## Novelty-risk (honest)

Cross-tokamak transfer is *actively worked* (hybrid models, viewmakers,
physics-guided). It is NOT virgin. The under-explored angle is a
*small from-scratch* model with explicit device-invariance evaluated
strictly on a fully held-out machine via the public benchmark — most
prior work uses larger/feature-engineered or partial-transfer setups.
Frame as "does the cheap invariance lever move the held-out-machine
number," not "we solved fusion."

## Next action
Verify DisruptionBench/tokamak data access on the box → if no-gate,
build as FR-008 kill-switch.

## Sources
- https://arxiv.org/pdf/2309.05361
- https://arxiv.org/pdf/2007.01401
- https://dspace.mit.edu/handle/1721.1/150682
- https://arxiv.org/pdf/2410.11065
