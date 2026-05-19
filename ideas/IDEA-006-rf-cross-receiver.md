# IDEA-006 — RF fingerprinting collapses across receivers (the shift is IN the public data)

**Domain:** RF / wireless signal ML
**Source:** session-2 + arXiv cross-check, 2026-05-19
**Status:** CANDIDATE → verify WiSig no-gate, then FR-009

## The open problem (sourced)

RF device fingerprinting (RFFI) reaches >99% in-domain but
**collapses across receivers/channels** — the transmitter signature
is entangled with receiver hardware artifacts; zero-shot cross-
receiver remains unsolved.
- CrossRF, arXiv:2505.18200 (2025).
- Cross-receiver disentanglement, arXiv:2510.09405 (2025).

## Why chosen over side-channel (honest)

Cross-device DL side-channel (ASCAD etc.) is *also* this pattern,
but arXiv (RAID'24 "A Second Look at Portability"; the field states
"no large-scale public datasets for cross-hardware EM shift") — its
frontier version is **data-gated**. Same trap that downgraded
IDEA-002 (fusion). RF/WiSig is preferred because the **cross-
receiver shift is present in openly-downloadable data** — testable
honestly, no gate. (Side-channel kept as a queued lower-priority
candidate, ASCAD key-shift only.)

## Why it fits (the validated edge)

Identical "looks-great-in-domain, collapses-under-realistic-shift"
as FR-008 chemistry / PhysioMind / CardioSafe / GTEx — the lab's
demonstrated, now repeatedly-confirmed competence.

## Frontier hypothesis (falsifiable)

A small from-scratch model with explicit receiver-disentanglement
generalizes to **held-out receivers, zero target labels** better
than a plain CNN — OR (the honest likely outcome, consistent with
prior): disentanglement does NOT beat the plain CNN cross-receiver,
and the in-domain 99% number is a ~large overstatement.

## Cheapest kill-switch
1. WiSig (multi-receiver, multi-day) — verify no-gate.
2. Train on subset of receivers; test on **held-out receivers**,
   zero target labels.
3. Falsifier: report in-domain acc, then held-out-receiver acc, for
   plain CNN vs disentangled. The finding is the in→OOD collapse
   (predicted, lab's edge); the sub-question is whether
   disentanglement is the lever (prior says no — invariance/
   disentangle has never been the lever in this lab).

## Sources
- https://arxiv.org/abs/2505.18200
- https://arxiv.org/abs/2510.09405
- https://homepages.uc.edu/~wang2ba/files/pub/raid24_mabon.pdf (why side-channel deprioritized)
