# IDEA-003 — Small model that generalizes LIGO glitch classes across observing runs

**Domain:** Space / gravitational-wave detector noise
**Source:** internet research (session-1), 2026-05-19
**Status:** CANDIDATE — frictionless public data; medium novelty.

## The open problem (sourced)

LIGO data has frequent non-Gaussian noise transients ("glitches")
that mimic/obscure real signals. Classification works on
time-frequency *images*; systematic evaluation of ML architectures
on *tabular glitch metadata* (cheaper, deployable) is under-done,
and a 2026 benchmark just opened this up.

- "Comparatively less attention has been given to systematic
  evaluations of ML architectures operating directly on tabular
  glitch metadata." — arXiv 2604.08796 (Apr 2026, Gravity Spy).
- Tree methods are strong on tabular; small DL models reach
  competitive accuracy with far fewer params — but cross-run /
  novel-glitch-class generalization is not characterized.

## Frontier hypothesis (falsifiable)

A small from-scratch model on tabular Gravity Spy metadata
generalizes to glitch classes / observing-run conditions it was not
trained on better than gradient-boosted trees — the honest test the
2026 benchmark sets up but does not push on out-of-distribution
glitch classes.

## Cheapest kill-switch

1. Gravity Spy dataset (public, Zenodo/Gravity-Spy — no gate).
2. Held-out *glitch class* split (train on subset of classes,
   test on classes/conditions unseen) — true OOD, not random split.
3. Falsifier: small DL must beat XGBoost/HistGBR on the held-out-
   class metric. If not, DL adds nothing here → NEGATIVE, logged.

## Data / access
Gravity Spy is openly hosted (Zenodo). Verify exact file on box
before building. No registration gate expected.

## Novelty-risk (honest)
Glitch classification is heavily worked (image-based). The genuinely
under-explored slice is *tabular-metadata + out-of-distribution
glitch-class generalization + small-model parameter efficiency*.
Medium novelty — a clean honest result is publishable as a methods
note, not a landmark. Good *fast* loop entry, lower ceiling than
IDEA-002.

## Sources
- https://arxiv.org/abs/2604.08796
- https://arxiv.org/pdf/1803.09933
