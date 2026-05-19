# Ideas Index — the main file

Every idea/novel gets its own file in `ideas/`. This index is the
map. Ideas come from internet research (sourced, falsifiable).
Promising ones become FR-NNN experiments in the run loop
(`../REGISTRY.md`). Negatives stay on record.

| ID | Domain | One-line gap (sourced) | Status | File |
|----|--------|------------------------|--------|------|
| IDEA-001 | Genomics | Regulatory models don't generalize to a *fully held-out species* | PARTIAL: invariance lever FALSIFIED on easy sub-case (FR-007 NEG); hard regulatory core UNTESTED | `IDEA-001-genomics-cross-species-generalization.md` |
| IDEA-002 | Fusion | Cross-tokamak disruption transfer | **DOWNGRADED** — 2 independent passes: heavily worked + data partly gated. Logged, not next. | `IDEA-002-fusion-cross-tokamak-disruption.md` |
| IDEA-003 | GW/space | Tabular LIGO glitch metadata vs trees | SUPERSEDED by IDEA-005 (open-set framing is the genuinely thin part) | `IDEA-003-ligo-glitch-tabular.md` |
| IDEA-004 | Chemistry | Yield models collapse under high-yield-tail/OOD splits | **REPRODUCED (FR-008 + FR-008R)** — graduated: collapse holds under independent split (additive→ligand) AND model (HistGBR→RF/MLP). Random R²~0.9→OOD ~0.32; high-yield-tail negative R² everywhere. First graduated finding. | `IDEA-004-chem-yield-tail-collapse.md` |
| IDEA-005 | GW/space | Open-set novelty detection for unseen glitch morphologies | CANDIDATE — strong 2nd; clean Zenodo data; genuinely thin | `IDEA-005-ligo-openset-novelty.md` |

| IDEA-006 | RF | RF fingerprinting collapses across receivers | DATA-VERIFY-BLOCKED — WiSig host unconfirmed. Not forced. | `IDEA-006-rf-cross-receiver.md` |
| IDEA-007 | Tabular | Do tabular robustness methods actually recover the shift gap? (TableShift) | DATA-VERIFY-PENDING — strong lab-edge fit, public-claimed; verify per-task no-gate before FR-010 | `IDEA-007-tableshift-robustness-overstated.md` |

### Sourced candidates queued (verify exact artifact from paper's data-availability, NOT host-guessing)
- **GW open-set (IDEA-005)** — Gravity Spy via Zenodo DOI. Highest no-gate confidence + genuinely under-explored. Next to verify.
- **Side-channel key/desync collapse** — ASCAD via ANSSI-FR GitHub (canonical, stable, public). Frontier cross-HARDWARE version is gated (field-acknowledged) → only the no-gate key-shift variant.

### Loop lesson (logged 2026-05-19)
Every NEW exotic domain (materials, fusion, RF) hit data-access friction; the only confirmed result (FR-008) came from a verified-accessible dataset. Bias the loop toward verified-no-gate data + the validated edge, not toward hunting new gated datasets.

### Two-session comparison verdict (2026-05-19)
Session-1 favored fusion; Session-2 independently rated fusion LOW-novelty/gated → fusion DOWNGRADED (honest, not defended). Non-overlapping cross-pass winner = IDEA-004 (chemistry tail-collapse): only candidate passing all of {published+quantified gap, zero-gate data, trivial compute, sharp falsifier, matches lab edge}. Weak/crowded fields dropped by Session-2: BCI, robotics(needs hardware), climate(gated CDS).

## Pipeline
internet research → sourced idea file (`IDEA-NNN-*.md`) →
feasibility verify → FR-NNN kill-switch experiment → honest log in
REGISTRY → independent reproduction before anything graduates.

## Discovery queue (fields to research next, one+/day)
materials small-data extrapolation · RF/comms · catalysis ·
fusion/plasma control · battery degradation · protein dynamics ·
climate downscaling · radio astronomy transients · cryptography ·
neuromorphic. Each becomes its own sourced IDEA-NNN file when
researched — not a vague list; only enters the index once it has
sources + a falsifier.
