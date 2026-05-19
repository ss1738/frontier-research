# Frontier Research — Sector Index & Top Opportunities

All 18 sectors researched. Each `unsolved_problems.md` has: current state (with numbers), top 3 precise technical gaps, one wild hypothesis nobody has run, and endpoint company description. Sources = real 2023-2025 papers.

## Sector Map

| Sector | File | Key Wild Hypothesis |
|---|---|---|
| Space | [space/](space/unsolved_problems.md) | Enceladus chiral amino acid flyby — $50M to answer "does life exist in the solar system?" |
| Nuclear Fusion | [nuclear-fusion/](nuclear-fusion/unsolved_problems.md) | MTF + liquid Li wall for p-B11 bremsstrahlung reabsorption — nobody has run this |
| Ocean Deep | [ocean-deep/](ocean-deep/unsolved_problems.md) | Abyssal trench isobaric thermal battery — uncalculated combined exergy |
| AI Models | [ai-models/](ai-models/unsolved_problems.md) | Chronological pretraining — strict temporal ordering of training corpus vs random shuffle |
| Quantum | [quantum/](quantum/unsolved_problems.md) | Device-personalized adaptive QEC decoder — treating syndrome history as real-time noise signal |
| Materials/Nano | [materials-nano/](materials-nano/unsolved_problems.md) | Charged domain wall drift memory — single wall position as analog state, no stochastic nucleation |
| Internet Protocols | [internet-protocols/](internet-protocols/unsolved_problems.md) | NDN-style content-addressed KV cache fabric for disaggregated LLM inference |
| Energy | [energy/](energy/unsolved_problems.md) | Grid-scale inertia synthetic via battery-inverter coordination |
| Transportation | [transportation/](transportation/unsolved_problems.md) | Sub-THz all-weather sensor for autonomous vehicles |
| Robotics | [robotics/](robotics/unsolved_problems.md) | Tactile sensing at skin-pore density (300 taxels/cm²) |
| Manufacturing | [manufacturing/](manufacturing/unsolved_problems.md) | Tooling Valley of Death — no SME-accessible process |
| Biotech/Gene | [biotech-gene/](biotech-gene/unsolved_problems.md) | Extra-hepatic LNP delivery; mitochondrial base editing; in-vivo logic circuits |
| Longevity/Health | [longevity-health/](longevity-health/unsolved_problems.md) | LINE-1 RT inhibitor as anti-aging target |
| Neuroscience/BCI | [neuroscience-bci/](neuroscience-bci/unsolved_problems.md) | OPM-MEG wearable semantic decoder at >10 bits/sec |
| Finance/Payments | [finance-payments/](finance-payments/unsolved_problems.md) | ZK-AML — encode AML rulesets as zero-knowledge circuits |
| Food/Agriculture | [food-agriculture/](food-agriculture/unsolved_problems.md) | Precision fermentation downstream processing (85% of cost) |
| Climate | [climate/](climate/unsolved_problems.md) | Atmospheric methane removal — <$5M/yr global research vs $20B+ for CO2 DAC |
| Consciousness | [consciousness/](consciousness/unsolved_problems.md) | PCI in slime molds via electrical micro-stimulation — first substrate-independent consciousness data |

---

## TOP 10 FRONTIER OPPORTUNITIES
Ranked by: (impact if solved) × (gap is real and specific) × (first-mover position possible)

### #1 — Atmospheric Methane Removal
**Sector**: Climate | **File**: climate/unsolved_problems.md
- Methane GWP = 86× CO2 over 20 years. Atmospheric CH4 at 1922 ppb (160% above pre-industrial)
- Global research funding: <$5M/year vs $20B+ committed to CO2 DAC
- Methane removal credits worth ~30× CO2 credits by GWP
- Three approaches (photocatalytic reactors, chlorine-enhanced OH, iron-salt aerosol) each with unresolved problems and zero coordinated research
- **First mover = standard setter** in a market that doesn't exist yet
- **Why now**: 2024–2025 photocatalysis papers have isolated the humidity-tolerance problem specifically — the gap is newly well-defined

### #2 — Intraoperative Awareness Monitor (Next-Gen BIS)
**Sector**: Consciousness | **File**: consciousness/unsolved_problems.md
- 26,000 cases/year in the US of waking during anesthesia
- BIS (1990s EEG algorithm) = current standard; sometimes INCREASES awareness incidence because thresholds are unreliable
- PCI (TMS/EEG perturbational complexity) = most accurate in research, but requires TMS hardware + 30+ second windows — unusable in OR
- **Gap**: continuous real-time scalp-EEG complexity measure working through OR electrical interference, with <2% individual error rate (BIS: ~15%), invariant to anesthetic mechanism (propofol vs volatile vs ketamine)
- **Revenue model**: per-use device fees (BIS = $500M+/year for Medtronic). $5–10B market. FDA 510(k) pathway

### #3 — Tritium Breeding & Li-6 Supply (Western Fusion Infrastructure)
**Sector**: Nuclear Fusion | **File**: nuclear-fusion/unsolved_problems.md
- Only Russia and China produce enriched Li-6 at scale. Western fusion has NO secure supply
- 10 fusion plants would exhaust global Li-6 supply before 2040 at current production capacity
- TBR > 1 has NEVER been demonstrated at any scale relevant to a power plant
- **Electrochemical isotope separation (EIS) via V₂O₅** demonstrated at lab scale 2025 — the enabling technology exists, the scale-up company does not
- A Western Li-6 enrichment facility = the single most strategic fusion infrastructure asset; a national-security-grade business

### #4 — ZK-AML: Zero-Knowledge Anti-Money-Laundering
**Sector**: Finance | **File**: finance-payments/unsolved_problems.md
- 127 African banking institutions lost correspondent relationships in 2024–2025 alone
- Banks cannot legally share customer data across correspondent chains — the privacy-vs-compliance deadlock
- GENIUS Act (2026) mandates compliance but specifies no mechanism — first mover on ZK-travel-rule gets the standard
- **The gap**: nobody encoding FinCEN AML rulesets as ZK circuits — each bank proves "this transaction passes our AML ruleset" without sharing raw customer data
- Revenue: per-transaction fees ($0.001–0.01). Network-effect moat. TAM: $50–200B cross-border payments infrastructure. Comp: SWIFT ($3.5B revenue)

### #5 — DAC Sorbent Regeneration (Humidity-Swing / pH-Swing)
**Sector**: Climate | **File**: climate/unsolved_problems.md
- Current solid-sorbent DAC: 6–10 MJ/kg CO2 regeneration energy. Thermodynamic minimum: ~0.4 MJ/kg. Gap = 15–25×
- Humidity-swing or pH-swing (not thermal) could cut energy 60–70% and reach $100/tonne
- No sorbent simultaneously achieves: >90% CO2 purity + >10,000 cycles + hydrophobic water rejection + CO2 selectivity
- This is the enabling technology for the $490/tonne → $100/tonne DAC transition

### #6 — Precision Fermentation Downstream Processing
**Sector**: Food/Agriculture | **File**: food-agriculture/unsolved_problems.md
- Downstream processing = 85% of precision fermentation cost. Nobody solving this as a standalone
- Pichia pastoris secretes at 1–10 g/L for most heterologous proteins; cost-competitive process needs 50+ g/L
- No published complete techno-economic analysis of high-titer + single-step extraction at food-grade scale
- **Business**: B2B platform licensing high-titer strains + single-step extraction IP. TAM: $15–40B by 2035
- Vertically-integrated competitors have no incentive to build this as standalone → genuine gap

### #7 — Chronic BCI Implant Longevity (The Forever Implant)
**Sector**: Neuroscience/BCI | **File**: neuroscience-bci/unsolved_problems.md
- Every intracortical implant fails in months to years: insertion → glial scar → signal loss → neuronal death in 50–200µm radius
- Rigid silicon/metal electrodes: modulus ~1 GPa vs brain tissue ~1 kPa — 6 orders of magnitude mismatch
- No published device achieves 5-year stable primate recording
- Must simultaneously: (a) mechanically match brain tissue lifetime, (b) release anti-inflammatories biochemically, (c) maintain electrical stability, (d) self-report own degradation
- **Revenue**: "The forever implant" for ALS/locked-in + adaptive DBS for Parkinson's/depression that never degrades. This is the Intel of the brain

### #8 — RPKI BGP Stealthy Hijacking / Verified-Path Overlay
**Sector**: Internet Protocols | **File**: internet-protocols/unsolved_problems.md
- RPKI/ROV deployment reached 50% — but partial adoption CREATES new attack: stealthy BGP hijacking via non-ROV ASes. Targeted attacks: 99.5% success probability (NDSS 2026)
- ASPA (full AS_PATH verification): still IETF draft, zero production deployment
- **Commercial opportunity**: verified-path overlay for high-value traffic (financial, DNS root, CDN) without requiring universal SCION adoption
- The financial services sector will pay for verified BGP paths — regulatory pressure post any major routing incident

### #9 — Substrate-Independent Consciousness Measurement
**Sector**: Consciousness | **File**: consciousness/unsolved_problems.md
- 2024 NY Declaration: fish, cephalopods, crustaceans are sentient. Fungal networks show electrical oscillations analogous to neural spike trains
- IIT phi: computationally intractable for >20 binary elements. PCI: requires TMS + EEG — inapplicable to non-neural systems
- **Nobody has attempted perturbational complexity measurement in slime molds** using electrical micro-stimulation + multi-electrode recording
- **Market**: pharma (drug consciousness testing), animal welfare regulation, AI consciousness assessment (legally relevant in 2026+). $500M–2B research tools market that doesn't exist yet

### #10 — KV Cache Transport for Disaggregated LLM Inference
**Sector**: Internet Protocols | **File**: internet-protocols/unsolved_problems.md
- Disaggregated LLM inference (prefill-decode separation) is now production architecture at every major lab
- The network bottleneck: KV cache transfer. For 70B model with 32K context = 10–50 GB per request batch
- TCP/IP structurally wrong: no content-addressing, no multicast, no reuse-awareness. RDMA requires homogeneous fabric
- Shared prefix caching (system prompts reused across thousands of concurrent users) cannot be efficiently distributed
- NDN-style content-addressed KV cache fabric = a $100M engineering problem that unlocks 40–70% bandwidth reduction for high-reuse workloads at hyperscaler scale

---

## Wild Hypotheses That Could Be FR-NNN Experiments (trainable on satyawan-1)

| Hypothesis | Experiment | Model size | Data source |
|---|---|---|---|
| Chronological pretraining improves temporal reasoning | Pretrain two identical GPT-style models: one chronologically ordered, one shuffled. Evaluate on TimeQA, TRAM | 100M–500M | Common Crawl with publication dates |
| Device-personalized QEC decoder | Train LSTM/Transformer on (syndrome-history, noise-params) pairs; test vs static AlphaQubit baseline | 1M–10M | Simulated Sycamore noise model + IBM public syndrome data |
| Composition-aware training (binding loss) | Add explicit role-filler separation loss to transformer. Test on SCAN, COGS, ARC-AGI-2 | 10M–100M | SCAN, COGS, ARC-AGI-2 datasets |
| Model collapse mechanism (factorial design) | 3×3×3 factorial: distributional shift × tail frequency × verifier threshold. Measure collapse rate across 3 model scales | 1M–50M | Synthetic + real text mix |
| Hadal N₂O flux estimation (ML-based) | Train a biogeochemical model on all published hadal sediment profiles → estimate N₂O from environmental features | 1M | Open oceanographic databases |

Last updated: 2026-05-19. Research continues daily.
