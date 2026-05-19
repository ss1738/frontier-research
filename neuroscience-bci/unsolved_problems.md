# Neuroscience & Brain-Computer Interface — Frontier Unsolved Problems

## TOP 3 GAPS

### 1. Chronic Implant Longevity — The Glial Scar Death Sentence
- Every intracortical implant fails in months to a few years: insertion → inflammation → glial scar → signal loss → neuronal death in 50-200µm radius
- Rigid silicon/metal electrodes: modulus ~1 GPa vs brain tissue ~1 kPa — 6 orders of magnitude mismatch
- No published device achieves 5-year stable primate recording
- Required: simultaneously (a) mechanically matched to brain tissue throughout lifetime, (b) biochemically active releasing anti-inflammatories, (c) electrically stable, (d) self-reporting its own degradation
- **Company unlock**: "The forever implant" — 10-year guaranteed BCI for ALS/locked-in + adaptive DBS for Parkinson's/depression that never degrades. The Intel of the brain.

### 2. Non-Invasive Semantic Decoding — The Bandwidth Wall
- EEG: 1-2 bits/second useful semantic content
- fMRI: 73%+ sentence decoding accuracy BUT requires 3-ton magnet
- Invasive BCIs: hundreds of bits/second, requires brain surgery
- White space: wearable neural interface capturing semantic content at >10 bits/second with mm spatial resolution
- **Specific approach**: OPM-MEG (optically-pumped quantum magnetometers as wearable helmet) + foundation model neural decoder trained on invasive+non-invasive paired data
- Nobody building this: Kernel shut down, Meta does wrist EMG only, OpenBCI = consumer EEG
- **Company unlock**: Thought-to-text without surgery for ALS/aphasia → consumer AR/VR neural control. $500B+ consumer market if bandwidth solved

### 3. Psychiatric Closed-Loop DBS — No Universal Biomarker
- Adaptive DBS for Parkinson's: FDA approved 2025 (beta-band LFP power = validated biomarker)
- For depression, OCD, PTSD: no equivalent biomarker exists
- UCSF N=1 closed-loop depression (Nature Medicine 2021) required weeks of invasive recording per patient — not generalizable
- **Wild hypothesis**: Cross-regional phase-amplitude coupling (subgenual ACC theta ↔ nucleus accumbens gamma) is a universal patient-independent biomarker for treatment-resistant depression. All current closed-loop DBS uses local single-region power spectra. Cross-regional phase coupling has NEVER been used as a real-time stimulation control signal.
- **Company unlock**: Psychiatric neuromodulation "AutoPilot" — hardware-agnostic software on any implantable neurostimulator, automatically identifies patient-specific biomarkers via RL. Platform model (like App Store for DBS). 84M treatment-resistant depression patients globally. $20-50B

---
Sources: Journal of Neurochemistry 2025, Columbia Engineering wireless BCI 2025, Nature Communications linguistic decoding 2025, PMC closed-loop DBS
