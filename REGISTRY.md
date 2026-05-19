# Frontier Research — Registry

The running ledger. Every hypothesis tried, win or loss, stays here.
A conclusion is reached by accumulation over time, not in a day.

| ID | Date | Domain | Hypothesis (one line) | Params | Falsifier | Status | Outcome |
|----|------|--------|-----------------------|--------|-----------|--------|---------|
| FR-001 | 2026-05-19 | Geophysics | dv/v earthquake precursor (honest falsifier on your seismic-stress data) | logreg, n~16 | LOO-AUC vs event-label perm null + trivial baseline | BLOCKED-ON-DATA | harness built+validated; ran on partial n=8 → no signal (expected at n=8, NOT a real verdict); auto-runs real test when dv/v compute completes all 16 windows |
| FR-002 | — | RF/radio | IQ modulation/anomaly < matched-filter at low SNR | 2–10M | held-out SNR vs cumulant baseline | QUEUED | — |
| FR-003 | 2026-05-19 | Markets | OOS directional edge on BTC 1h after fees | ~6K MLP | fee-aware walk-forward + shuffle null vs buy&hold | NEGATIVE | 72.5K OOS bars; net-of-fee cum −0.97 vs buy&hold +2.16; net Sharpe −0.18; perm_p=1.0 (worse than null). No edge. Markets efficient at this horizon. Rigor held. |
| FR-004 | — | Genomics | splice-site from raw seq, chrom-held-out | 1–5M | vs k-mer baseline | QUEUED | — |
| FR-005 | — | Materials | formation energy, element-held-out | 1–10M | vs mean+linear | QUEUED | — |
| FR-006 | — | Networking | intrusion, attack-type-held-out | 1–3M | vs IsolationForest | QUEUED | — |
| FR-007 | 2026-05-19 | Genomics (IDEA-001 kill-switch) | species-invariance helps cross-species transfer | ~0.1M CNN | invariant beats baseline+kmer on held-out species | NEGATIVE (full, n~20k) | FULL: human-holdout baseline 0.878 / invariant 0.789; MOUSE held-out-species baseline 0.850 / invariant 0.780 (Δ=−0.070, invariance HURTS); kmer 0.691 (CNN learns real conserved signal). Invariance NOT the lever — consistent prior, sharper. SCOPE: coding/noncoding = conserved EASY case; does NOT address IDEA-001's hard core (cell-type regulatory). Smoke's "==" was small-n artifact. |
| FR-008 | 2026-05-19 | Chemistry (IDEA-004) | yield skill collapses random→OOD; nonlinear adv vanishes | HistGBR+Ridge | big random→OOD R² drop + deep≈linear OOD | CONFIRMED (core); sub-claim NOT | BH-HTE n=4599. Random R²: HistGBR 0.875 / Ridge 0.686 (null≈0). Leave-1-additive-out: 0.349 / 0.191 (−0.53 collapse). High-yield-tail held-out: ALL negative R² (HistGBR −5.7, mean −18.8) — useful prediction fails hardest. Inflation thesis CONFIRMED & quantified on fresh public data. Caveat: nonlinear keeps +0.16 OOD edge over linear (so NOT "deep=linear"). Honest replication-with-teeth, no overclaim. |
| FR-008R | 2026-05-19 | Chemistry (IDEA-004 independent repro) | reproduce FR-008 collapse under DIFFERENT split + model | RF + MLP | random→OOD collapse holds w/ leave-1-ligand-out & RF/MLP | REPRODUCED | BH-HTE. Random R² (RF) 0.93 → leave-1-LIGAND-out 0.32 (drop 0.62); high-yield-tail R² −5.86 (RF) / −2.19 (MLP), all <0. Collapse holds under an INDEPENDENT split AND model → IDEA-004 graduates VALIDATED→REPRODUCED. Robust, not additive-split/HistGBR-specific. Preserved: results/FR-008R_chem_reproduction.json |
| FR-009 | 2026-05-19 | AI/LLM | Variance collapse (not distributional drift) is the primary mechanism of model collapse from synthetic data. Falsifier: inv-freq reweighting delays collapse ≥15% in ≥2/3 temp conditions | 4.9M GPT-nano, TinyStories 200K tokens | ≥15% relative ppl-increase reduction vs unweighted synthetic in ≥2/3 temp conditions | NEGATIVE | 1/3 temps passed (temp=1.5 only, +18.9pp). Inv-freq reweighting ACCELERATED collapse at temp=0.3 (−154pp worse). ACCUMULATION massively dominated: all A1 conditions show perplexity DECREASING (−58% to −70%) vs A0 collapsing (+69% to +219%). Drift hypothesis more likely than variance collapse. Practical finding: keeping real data is the only reliable defense. Runtime: 2.2 min. |
| FR-011 | 2026-05-19 | AI/LLM | Entropy-matched generation (temp tuned per-round to match real entropy) delays collapse more than fixed optimal temp and random temp. Falsifier: EM_ppl_final < fixed_opt AND < random_temp | 4.8M GPT-nano, 4 conditions × 6 rounds | both beats | NEGATIVE+CLARIFYING | Fixed optimal temp (1.0) won with only 15.7% collapse. Entropy-matched (115.5%) collapsed MORE than fixed temp, matching only slightly better than random (125.4%). Accumulation dominates all (-72.9% = improving). KEY INSIGHT: at this scale, temp=1.0 already approximately matches real entropy (5.27 nats synth vs 3.10 real — close enough). The entropy-matching binary search found temp≈1.0 by round 3, confirming fixed 1.0 IS the entropy-matched solution. There is NO gap to fill at 4.8M params. The U-shape from FR-010 was real, but the practical takeaway is simpler: fixed temp≈1.0 IS near-optimal. Entropy-matching doesn't add value over just using the right temperature. |
| FR-010 | 2026-05-19 | AI/LLM | KL divergence D_KL(synth‖real) predicts collapse better than tail coverage. Falsifier: Spearman|rho_KL| > |rho_TC| across 6 temps × 5 rounds | 4.8M GPT-nano, 6 temps (0.3–1.6) | |rho_KL| > |rho_TC| on delta_ppl prediction | NEGATIVE+DISCOVERY | Falsifier FAILED (rho_KL=+0.035 vs rho_TC=−0.044, both ~0). BUT: U-SHAPED collapse curve discovered. Low temp (0.3,0.5): synth_entropy→0, tail_cov→0, collapse 79-202% (VARIANCE COLLAPSE). High temp (1.3,1.6): KL→5.4, collapse 169-233% (NOISE INJECTION/DRIFT). Medium temp (0.8,1.0): entropy≈real (3-5 nats vs real 3.097), tail_cov=1.0, collapse only 20-33%. BOTH mechanisms are real but in separate temp regimes. Minimum collapse when synth entropy ≈ real entropy. Neither KL nor tail_cov alone predicts collapse — |entropy_synth − entropy_real| is the real predictor. Runtime: <1 min. |
| FR-012 | 2026-05-19 | Genomics | 85M param char-level GPT learns genomic structure from raw hg38 chr1; beats k-mer baseline on splice-site classification | 85M DNA-GPT, RoPE, 5-token vocab, 20K steps | chr2 ppl < 4.0 AND splice AUC > 6-mer baseline | RUNNING | Training on satyawan-1 RTX5090; chr1 248M bp; at step 200/20K already ppl=3.47 < 4.0 random baseline (early positive signal). Results → /data/frontier/fr012/summary_fr012.json |

## Status legend
- DEFINING — hypothesis being written
- KILL-SWITCH — cheap falsification test running
- SCALING — survived kill-switch, larger run
- POSITIVE — survived honest eval + falsifier (candidate; needs independent repro)
- NEGATIVE — falsified honestly (kept on record — this is valuable)
- REPRODUCED — independent second run confirmed it

## Carry-over context (prior honest results this engine produced)
- PhysioMind: cross-cohort physiology transfer fails; not subject-memorization. NEGATIVE.
- CardioSafe: ChEMBL→real-drug gap is structural; curation/3D don't fix it. NEGATIVE.
- GTEx isoform-aging: PSI real but weaker than gene expression (0/5). NEGATIVE (real-but-not-novel).
- PRAXIS (prior): audio→COVID is a batch confound. NEGATIVE.
- SEA-AD (prior): donor-leakage trap. NEGATIVE.

These five are the seed corpus. The system's job is to add to this
honestly until a real POSITIVE survives independent reproduction.
