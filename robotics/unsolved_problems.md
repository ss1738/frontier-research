# Robotics & Automation — Frontier Unsolved Problems

## TOP 3 GAPS

### 1. Tactile Sensing at Human Resolution — The Density Gap
- Human fingertip: ~0.5mm spatial resolution, 17,000 mechanoreceptors/hand, senses pressure + shear + vibration (1000Hz) + temperature + material
- Best commercial sensor (GelSight/DIGIT): ~1-2mm resolution, pressure only, 30Hz, fragile
- Gap: 4-6x worse resolution, missing modalities entirely, 30x slower
- Physics to make it are KNOWN — this is a manufacturing/cost problem, not a physics problem
- Without it: in-hand manipulation of soft fruit, wet dishes, tangled cables = impossible
- **Company unlock**: dense multi-modal tactile skin — the Intel of robot sensing, B2B component to every OEM

### 2. Out-of-Distribution Generalization Cliff
- Behavior cloning achieves high success in training environments, collapses with: different lighting, object moved >10cm, different background, unfamiliar object variant
- Learns correlations not task semantics — OOD inputs trigger no recovery behavior
- VLA models (RT-2, π0) show improvement but still require fine-tuning per deployment site
- Every physical environment is OOD by definition
- **Company unlock**: a robot that succeeds on "pick up the blue cup" in any room it has never seen, with any cup it has never touched

### 3. Whole-Body Loco-Manipulation Under Real Contact Forces
- Grasping heavy object instantly changes center of mass, destabilizes gait — arms and legs must be jointly controlled in single optimization
- Current stacks: separate locomotion + manipulation controllers
- Best published result (2025): 83% success on 2 contact-rich tasks — far below 99.9%+ needed commercially
- High-dimensional (50+ DoF) contact-rich control is computationally intractable with current MPC horizons
- **Company unlock**: unified whole-body controller that treats CoM dynamics and manipulation forces as a single optimization

## WILD HYPOTHESIS
**Wearable Soft-Robotic Glove as Training Data Generator**
Wearable that: (a) assists human worker with enhanced force, (b) records exact force/torque/tactile at 1000Hz from hand AND object, (c) feeds directly as robot training data — zero teleoperation required. Humans are the world's best robot policy generators. Turn all existing factory labor into robot training data perpetually. Meta is close with hand motion capture but hasn't closed the loop with contact forces and material properties.

## ENDPOINT COMPANY
**Dense multi-modal tactile skin** — manufacturing company producing tactile arrays at high density, low cost, high durability. B2B to every robotics OEM. First company at human-resolution (<$200/hand) gets designed into every humanoid robot on earth. The sensing component everyone needs and nobody makes.

---
Sources: a16z Physical AI Deployment Gap 2025, PMC 2025 loco-manipulation, arXiv dexterous manipulation 2025, TRI hard problems in manipulation
