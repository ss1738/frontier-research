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
| FR-012 | Genomics | 85M DNA-GPT on hg38 chr1 learns genomic structure; splice-site embeddings beat 6-mer baseline | hg38 chr1/chr2 | 85M | chr2 ppl < 4.0 AND splice AUC > 6-mer |
| FR-013 | AI/LLM | ICL collapses under sorted-label ordering (all class-0 first, then class-1) because transition statistics—not feature-label association—are the load-bearing mechanism | HuggingFace SST-2, AGNews, TREC, DBPedia, RTE | GPT-2 124M inference only | sorted-label accuracy drops ≥15pp vs random-ordered on 4/5 tasks |
| FR-014 | AI/Physics | PINN multi-scale failure (Helmholtz k=100, stiff Allen-Cahn, Burger's shock, 2D NS) is entirely FP32 precision stalls, not spectral bias or gradient conflict—FP64 alone closes it without architectural change | DeepXDE standard PDE benchmarks | ~500K MLP | FP64 reduces L2 error ≥50% on ≥3/5 canonical failure cases vs FP32-only baseline |
| FR-015 | AI/LLM | Grokking spectral gap (rolling Gram matrix SVD) predicts capability emergence jumps in LLMs ≥1000 steps before the accuracy spike—emergence is grokking at scale, not phase-transition-unpredictable | BabyLM 100M tokens or synthetic 3-hop arithmetic | 50–117M (GPT-2 small) | spectral gap precedes accuracy jump by ≥1000 steps in 5/5 runs |
| FR-016 | AI/CL | LayerNorm drift is the primary mechanism of catastrophic forgetting; freezing LayerNorm params alone (2-line fix) outperforms EWC on Split-CIFAR-100 without any weight regularization | Split-CIFAR-100 (10 tasks) | ViT-Small 22M | frozen-LN avg accuracy ≥ EWC avg accuracy across 10 tasks, 5 seeds |
| FR-017 | AI/Physics | FNO out-of-distribution frequency failure lives entirely in lifting/projection MLPs (not the Fourier spectral conv); swapping those two layers with sinusoidal-conditioned alternatives recovers ≥85% of in-distribution OOD gap | 1D variable-coeff wave equation (train 1–10 Hz, test 10–30 Hz) | 1–5M FNO | modified-FNO OOD error ≤15% relative to in-distribution error |
| FR-018 | BCI/Neuro | Subtracting the subject-specific aperiodic (1/f) EEG component in signal space before any learned encoder sees the data improves LOSO motor-imagery accuracy by ≥10pp over same encoder without this step | PhysioNet EEG MI 109 subjects (T1/T2 left/right fist) | EEGNet ~48K | LOSO accuracy ≥72% vs baseline ~62% (same model, no DA) |
| FR-019 | BCI/Neuro | Microstate transition grammar (treating EEG symbol sequences as a language) > first-order Markov baseline by ≥5pp on cross-subject emotion because transition syntax is more subject-invariant than topographic identity | SEED dataset 15 subjects or DEAP 32 subjects | LSTM/Transformer ~500K | LOSO emotion accuracy ≥ Markov baseline +5pp; trigram > bigram (nested falsifier) |
| FR-020 | BCI/Sleep | A 2-stage cascade where stage-2 uses stage-1 classifier uncertainty (entropy, P(Wake), P(N2)) as additional features raises N1 sleep-stage F1 from ~56% to ≥65% without any change to the core encoder | PhysioNet Sleep-EDF Expanded 153 subjects | Stage1: U-Time 5M; Stage2: MLP 50K | N1 F1 ≥65% on LOSO across 103 held-out subjects |
| FR-021 | Genomics | A codon-level transformer (64-token alphabet) beats ESM2 pseudo-likelihood on ProteinGym multi-mutant epistatic entries from E. coli expression contexts—because co-translational folding shapes epistatic landscapes—but not on yeast-display entries | ProteinGym multi-mutant DMS; UniProt bacterial seqs for pretraining | 15–20M | Spearman Δ≥0.05 vs ESM2 on ≥5/10 E. coli DMS entries; null on yeast-display entries |
| FR-022 | Genomics | A 5M model trained ONLY on inter-motif spatial distances (not TF identity) generalizes across cell types better than sequence models because regulatory spatial grammar is conserved but motif vocabulary is cell-type-specific | ENCODE MPRA (Sharpr-MPRA, lentiMPRA); JASPAR 2024; train K562+HepG2, test GM12878 | 5M transformer on spatial tokens | OOD cell-type correlation > ChromBPNet on held-out MPRA |
| FR-023 | Longevity | Protein evolutionary constraint (ESM2 embeddings of nearest gene) predicts whether a CpG site is in the Horvath aging clock (vs. matched age-correlated CpG)—coupling protein evolution to epigenetic drift | GSE40279 blood methylation; Horvath 353-CpG list; UniProt for evolutionary rates | 2–5M MLP on frozen ESM2 embeds | AUC >0.65 on held-out chromosomes (vs. genomic-features-only baseline) |
| FR-024 | Ocean | SSH anomaly field alone (no chlorophyll input) predicts North Atlantic phytoplankton bloom crash 10–14 days ahead because eddy-driven subduction appears in SSH curvature before the chlorophyll signal collapses | AVISO DUACS daily SSH; MODIS-Aqua chlorophyll-a; train 2003–2016, test 2019–2022 | 3–8M 2D CNN | HSS >0.1 on held-out 2019–2022 bloom seasons; zero-shot to Indian Ocean Arabian Sea as secondary test |
| FR-025 | Ocean | Atlantic-trained eddy mortality model (does this eddy die in 30 days?) generalizes zero-shot to Indian Ocean Agulhas ring shedding at >70% because approach-angle × vorticity geometry is basin-invariant | META3.2 global eddy dataset (AVISO); ERA5 wind; ETOPO1 bathymetry | 10M temporal GNN | Zero-shot Indian Ocean accuracy >70%; open-ocean eddies baseline < boundary-approaching eddy baseline (nested falsifier) |
| FR-026 | Climate | Temperature-conditioned CH4 plume detection (LST as input channel) generalizes zero-shot from summer training to winter test set—improving F1 by ≥5pp—because detection failure is surface-temperature-structured, not terrain-class-structured | EMIT L1B plumes + Carbon Mapper labels; MODIS LST; train Jun–Aug, test Dec–Feb | 5M U-Net | Winter F1 ≥ baseline+5pp; failure mode should correlate with LST not terrain class |

| FR-027 | Materials | A GNN classifying phonon stability from crystal graphs alone achieves ≥88% on random splits but collapses to <65% AUROC on triclinic/monoclinic hold-out—proving it learns symmetry shortcuts, not vibration physics | JARVIS phonon ~14k; Materials Project phonon ~5k | 2–5M CGCNN/ALIGNN | AUROC <65% on triclinic hold-out; coordination-number baseline beats GNN on this split |
| FR-028 | Materials | Superconductor Tc models (RF + GNN) are chemofamily interpolators—family-held-out MAE (cuprates removed) exceeds 20K for both models, exposing that all SOTA Tc prediction is taxonomic memorization, not physics | SuperCon 16k; ICSD Tc subset ~3k CIFs | 3M GNN + RF | Both models MAE >20K on family-held-out; gap ratio >3× vs random-split MAE |
| FR-029 | Materials | Band gap OOD failure on 5 TM elements (Fe/Mn/Co/Ni/Cu) is recoverable: adding explicit d-electron count + spin state as node features to ALIGNN recovers ≥0.10 eV of the OOD gap—proving current GNNs fail because they lack orbital inductive bias | Materials Project band gap 106k structures | 10M orbital-ALIGNN | Orbital-ALIGNN MAE improvement ≥0.10 eV over ALIGNN on TM-held-out split |

---

## Experiment priority queue (post-FR-012)

Ranked by: (speed to answer × novelty × field impact if true)

1. **FR-013** — ICL sorted-label: pure inference, <30min, reshapes ICL theory if true
2. **FR-014** — PINN FP64: ~500K model, 1-2h, falsifies 5 years of architecture work if true
3. **FR-019** — Microstate grammar: 45min, 500K params, genuinely untested cross-field synthesis
4. **FR-018** — EEG aperiodic stripping: 1.5h, crosses two totally isolated communities
5. **FR-024** — SSH bloom crash: 2-3h, proves/disproves eddy subduction as crash mechanism
6. **FR-016** — LayerNorm forgetting: 2h, 2-line fix vs. entire CL literature
7. **FR-017** — FNO lifting fix: 1-3h, localizes FNO's OOD failure to two layers
8. **FR-021** — Codon epistasis: 2-4h, wildest claim in the batch (translation kinetics → epistasis)
9. **FR-025** — Cross-basin eddy: 2-3h, first basin-invariant eddy mortality model
10. **FR-015** — Grokking→emergence: 2-4h, highest stakes if true

---

## Status legend
- DEFINING — hypothesis being written
- KILL-SWITCH — cheap falsification test running
- SCALING — survived kill-switch, larger run
- POSITIVE — survived honest eval + falsifier (candidate; needs independent repro)
- NEGATIVE — falsified honestly (kept on record — this is valuable)
- REPRODUCED — independent second run confirmed it
- RUNNING — training currently active on satyawan-1
- QUEUED — next in queue
- BLOCKED-ON-DATA — harness ready, waiting on data pipeline
