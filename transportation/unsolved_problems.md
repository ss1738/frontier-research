# Transportation & Mobility — Frontier Unsolved Problems

## TOP 3 GAPS

### 1. All-Weather Sensor Stack — Physics Problem Nobody Has Solved
- LiDAR fails in rain >30mm/h and fog <50m visibility (optical wavelengths scatter off water)
- Camera-only fails on low-contrast targets in rain/glare
- Radar: ~77GHz, works in rain BUT only ~30cm range resolution — can't distinguish child from traffic cone at 60mph
- Sub-THz imaging (300GHz–3THz) theoretically penetrates fog/rain with 1-2cm resolution — but no compact, cheap, fast sub-THz sensor exists
- Waymo/Aurora know this and work around it operationally (geofencing bad weather). Nobody solves the underlying sensor.
- **Company unlock**: sub-THz automotive imaging sensor — hardware physics problem, not software

### 2. Pedestrian/Cyclist Intent Prediction at Distribution Tails
- High accuracy on normal walking, collapses precisely where injury happens (person on phone stepping out, child chasing ball)
- Behavior cloning learns correlations not task semantics — breaks on distribution shift
- V2X (vehicle-to-infrastructure) supposed to solve this but DSRC vs C-V2X standards war unresolved globally
- **Company unlock**: calibrated uncertainty quantification tied to crash risk, + pedestrian-side V2X hardware that doesn't require standards resolution

### 3. Highway-to-Depot Last-Mile Transition for Heavy Freight
- Aurora/Kodiak explicitly DON'T solve this — they use "launch-and-landing zones" with human drivers at city limits
- 40-tonne semi navigating suburban industrial estate: tight radii, unmarked bays, dock-plate alignment to ±2cm
- Nobody is building robotics-grade last-mile docking for class-8 trucks
- **Company unlock**: precision low-speed positioning + dock plate actuation system for class-8 trucks

## WILD HYPOTHESIS
**Underground Urban Freight Tunnels**
Sub-5m diameter tunnels at 10-30m depth, autonomous electric freight vehicles at 60-80 km/h on fixed tracks. Zero weather, zero VRU interaction, no congestion, 24/7. Boring Company claims $10M/mile for 3.65m tunnels. No delivery company (Amazon, DHL, FedEx) or AV trucking firm is doing this. First pilot tunnel in Singapore/London/Tokyo = permanent physical moat.

## ENDPOINT COMPANY
**Sub-THz all-weather automotive sensor**: sells to Waymo, Aurora, Mobileye, every AV OEM as tier-1 supplier. No AV company achieves geofence-free commercial deployment without it. $50B+ market. Zero current competition — physics are known, packaging/cost/reliability engineering is unsolved.

---
Sources: MDPI Sensors, TechBrew 2026, EasyRain, MDPI 2025 pedestrian prediction review
