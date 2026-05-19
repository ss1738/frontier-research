# Nuclear Fusion — Frontier Unsolved Problems

## TOP 3 GAPS

### 1. Tritium Breeding at Scale — The Li-6 Supply Cliff and TBR Demonstration Gap
- Natural lithium is only 7.4% Li-6. Breeding blankets need 30–90% enrichment — historically required mercury amalgam columns (COLEX, now banned)
- Only two entities globally produce enriched Li-6 at scale: Russia and China. Neither supplies Western fusion programs on open-market terms
- Single ARC-class plant requires ~250,000 L of FLiBe molten salt. Startup inventory: 50–100 tonnes enriched lithium. At current global production: 10 plants would exhaust supply before 2040 (arXiv:2605.04707, Joule 2025)
- Target TBR >1.05–1.10 for self-sufficient commercial plant. NO experiment has demonstrated TBR > 1 at any scale relevant to a power plant
- ITER's Test Blanket Module = first time breeding concepts tested in real D-T plasma — but ITER will never breed tritium for its own consumption
- BABY experiment (Dec 2024, arXiv:2412.02721): first direct TBR measurement in molten FLiCl using high-energy neutrons. TBR = 3.57×10⁻⁴ (vs requirement ~1.1). Measured TBR was 2.3× LOWER than OpenMC simulations predicted. Tritium emerged as HT (insoluble gas) not predicted TF or HTO
- **Specific gap**: No closed-loop tritium breeding experiment at even 1% of reactor scale (>500 L salt). LIBRA targets ~500 L; ARC needs 250,000 L. Mass-transport coefficients in current models are off by factor ~2. Salt chemistry not understood well enough to model tritium extraction at scale
- **Company unlock**: Western Li-6 enrichment facility using electrochemical isotope separation (EIS — solid-state Li intercalation into V₂O₅, demonstrated at lab scale 2025, ScienceDirect). Most strategic fusion infrastructure asset in the West, pre-empting a monopoly bottleneck

### 2. Plasma-Facing Materials — Tungsten's Three Simultaneous Failure Modes
- Tungsten selected for ITER divertor and DEMO front-runner: high melting point (3422°C), low sputtering yield, low tritium retention vs carbon
- **Failure mode 1 — DBTT shift**: At 0.15 dpa / 400°C, DBTT shifts 200–250°C. At 1.67 dpa, shift reaches 500 K or more. DEMO divertor accumulates ~5–10 dpa per full-power year. Irradiated tungsten may be brittle at ALL operating temperatures below ~800°C
- **Failure mode 2 — He fuzz and bubble embrittlement**: 14 MeV DT neutrons transmute W into Re and Os + produce He via (n,α). He nucleates into nm-scale bubbles → micron-scale blisters → surface "fuzz" with ~50× lower thermal conductivity. Fuzz grows without saturation under continued He flux — no erosion-stable steady state observed
- **Failure mode 3 — Recrystallization**: Above ~1300–1500°C (exceeded transiently during ELMs), tungsten recrystallizes — grain boundaries weaken, creep strength collapses. Single large ELM deposits ~0.5 MJ/m² in microseconds
- All three mechanisms occur simultaneously and interact non-linearly. He-bubble-filled grain boundaries fracture differently under neutron-irradiation embrittlement. No facility can simultaneously irradiate with 14 MeV neutrons at fusion-relevant flux AND expose to fusion-relevant plasma
- PRX Energy 2024 (arXiv:2407.00858): cannot quantify neutron bombardment effects — computational and experimental burden exceeds current capability
- **Specific gap**: No validated lifetime model for tungsten under coupled plasma + neutron conditions. All neutron irradiation data comes from fission reactors (different spectrum, no He co-production). IFMIF-DONES (Spain, 14 MeV neutron test environment) = target operational ~2033
- **Company unlock**: Fusion-qualified W-alloy (ODS-W, W-Re, W-Cu laminates) divertor tile manufacturer with characterised post-irradiation ductility data. No commercial manufacturer produces fusion-qualified quantities. Owns supply chain for every tokamak following ITER

### 3. Grid Integration — The 1 GW Inflexible Baseload Problem
- Commercial fusion plant: ~1 GW continuous output. Rapid throttling risks plasma disruption — each startup/shutdown cycle is costly
- Germany H1 2025: 389 hours of negative day-ahead wholesale electricity prices. A fusion plant running full power during those hours loses money on every MWh
- Joule 2023: constraining fusion to baseload-only operation decreases breakeven cost by $50–340/kW depending on design — the plant destroys value every hour it cannot throttle
- ScienceDirect 2025 ("Baseload power plants are not essential for future power systems"): in deeply decarbonised grids, baseload plants without flexibility are actively economically penalised
- Thermal energy storage (TES) coupling raises modelled capacity factors to 94–98% — but plasma heat rejection varies on sub-second timescales (ELMs, sawteeth) while thermal storage operates on minute-to-hour timescales. No validated control architecture bridges these two timescales
- Frequency regulation requires <1 second response (primary). Fusion behind full AC converter = zero natural rotational inertia contribution to grid
- **Specific gap**: No integrated techno-economic study for fusion + short-duration storage + frequency regulation in a 2035-2040 grid (~60–80% renewable penetration) that closes the loop from plasma physics variability through heat exchanger dynamics to grid ancillary service revenue. Also: plasma wall interaction during intentional power ramp-down has never been studied
- **Company unlock**: Fusion-native grid services layer — thermal buffer + power electronics + market participation software designed specifically for plasma variability profile. ~$50M engineering problem, not a physics problem. Licenses to every fusion plant

## WILD HYPOTHESIS
**Magnetised Target Fusion with Liquid-Metal Wall for p-B11 Bremsstrahlung Recovery**: The canonical objection to p-B11 fusion is bremsstrahlung: at >150 keV ion temperature, radiation exits the plasma faster than fusion deposits it. Pfus/Pbrems peaks at only ~1.03–1.4 (Frontiers in Physics 2024). No experiment has compressed p-B11 fuel inside a liquid metal blanket. The hypothesis: a liquid lithium wall, optically thick at X-ray energies, could partially reabsorb bremsstrahlung photons — converting a pure loss into recoverable wall heating. Bremsstrahlung reabsorption threshold is achievable in the compressed plasma-metal boundary layer for 10–100 nanoseconds. TAE Technologies runs p-B11 in field-reversed configuration but at low density, without liquid-wall bremsstrahlung recovery. The first experiment: compress magnetised p-B11 plasma to ~10²⁶ cm⁻³ inside a liquid lithium liner. Measure bremsstrahlung reabsorption fraction vs open geometry as a function of liner thickness and density. p-B11 is nearly aneutronic (~0.1% energy in neutrons) so the liquid Li wall doubles as a calorimeter without activation concerns. If even 20–30% bremsstrahlung reabsorption is measured, the Pfus/Pbrems constraint relaxes enough to make a credible ignition roadmap at compression parameters 10× below what transparent-plasma analysis demands. This experiment has never been run.

---
Sources: arXiv:2605.04707 (Li-6 supply, Joule 2025), arXiv:2412.02721 (BABY experiment), ScienceDirect EIS enrichment 2025, arXiv:2407.00858 (plasma-facing materials screening PRX Energy 2024), ScienceDirect DBTT tungsten, Joule 2023 fusion grid value, ScienceDirect 2025 baseload power systems, arXiv:2511.10885 (bremsstrahlung constraints p-B11), Frontiers in Physics 2024 (Pfus/Pbrems), FIA Supply Chain 2024 Report
