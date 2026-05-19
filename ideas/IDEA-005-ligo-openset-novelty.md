# IDEA-005 — Open-set novelty detection for unseen LIGO glitch morphologies

**Domain:** Space / gravitational-wave detector noise
**Source:** session-2 internet research (strong runner-up), 2026-05-19
**Status:** CANDIDATE (genuinely under-explored; clean data)

## The open problem (sourced)

Gravity Spy's classifier is *closed-set*: new glitch morphologies in
O4 (e.g., Low-frequency Blip, Fast Scattering) had to be discovered
by humans, not flagged by the model — an unknown glitch is silently
misassigned to a known class.
- Glanzer et al., arXiv:2208.12849 (O3 classifications).
- Wu et al. multi-view fusion O4, arXiv:2401.12913 (CQG 2025).

## Frontier hypothesis (falsifiable)

A small from-scratch model with an open-set / energy- or
reconstruction-based novelty score flags fully held-out glitch
classes as OOD with useful AUC — i.e., it would have surfaced the
new O4 classes automatically.

## Cheapest kill-switch
1. Gravity Spy spectrograms (Zenodo, no gate).
2. Train on N−2 classes; hold 2 classes out entirely.
3. Falsifier: OOD score must separate held-out classes from known
   ones above a useful AUC. If ≈ chance → open-set lever dead here.

## Novelty-risk (honest)
Open-set recognition is studied generally; applied open-set *on
Gravity Spy specifically* is genuinely thin (under-explored, not
just under-marketed). Medium-high novelty, clean data, clear
falsifier. Good 2nd after IDEA-004.

## Sources
- https://arxiv.org/pdf/2208.12849
- https://arxiv.org/html/2401.12913
