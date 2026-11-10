# Round 2 scoring — 2026-11-09 (the conductor scores; Rusty reconciles)

Seal: conductor_sealed_findings_round2.md, sha256 497f6a04…e8f3. It stayed in the
conductor workspace; no copy left it.

## Exposure check
- Expert: 0 sealed-only phrases; 9 DOC, 0 PRIOR.
- Bot: 1 hit, "4-bit". That's natural: the 0..15 payload in the document is 4 bits. The bot
  used it about the payload enum, not the steering channel, and the seal never left the
  workspace. Clean.

## Against the round 2 seal
| Item | Expert | Bot |
|---|---|---|
| S2-1 crossing no longer special, v0.2 deposition retired (PRIOR) | MISSED (expected) | MISSED. The bot marked its own B-F12 CLOSED, endorsing the retirement. R2-F15 (grace has no hook) is adjacent |
| S2-2 toy Φ omits H and Q | PARTIAL (F12: unused fields) | MISSED |
| S2-3 support steers through dwell timing; dwell undefined | FOUND (A-F1 residual, F11, F13) | FOUND (R2-F1, plus a state-adaptive sender) |
| S2-4 destination-free grace vacuous in a deterministic model | MISSED | MISSED |
| S2-5 permit gate comes after crossing recognition | MISSED | FOUND (R2-F5) |
| S2-6 common control undefined | PARTIAL (F15) | FOUND (R2-F7 nominal BAs, R2-F6 rings) |
Expert: 1 FOUND / 2 PARTIAL / 3 MISSED. Bot: 3 FOUND / 3 MISSED.

## Correlated misses (both seats), rounds 1–2
- R1 S3: basis absent from U.
- R2 S2-2: toy Φ omits H and Q.
- R2 S2-4: destination-free grace is vacuous under determinism.
Two of the three are the same kind of defect: an argument missing between a general rule and
its instance. That is a recurring shared blind spot of the two Grok seats. n=3, so it's a
pattern to watch, not a result.

## Did the round 1 fixes hold? (each seat judged its own findings)
Of 30 findings: fully closed 16, mostly or only on paper 4, partly closed 7, relabeled 3
(A-F4, B-F9, B-F14). ChatGPT's 29 ACCEPTs out of 30 were real fixes for about half.

Method flaw: each falsifier judged the fixes to its OWN findings, which is self-vouching. The
bot's CLOSED verdict on B-F12 approved a fix that retired the v0.2 thesis without noticing the
cost. Rule for round 3: the seats cross-check each other's dispositions, or the conductor does.

## Conductor misses (not in the seal)
Expert: F14 canonical state-hash serialization (FATAL); F16 tolerance not principled; F17 cost
accounting; F18 high-entropy constant in K/D as a shared seed; F19 numeric collusion bound.
Bot: R2-F2 policy changes unprotected (FATAL for H4); R2-F4 H1's alternative branch passes by
construction (FATAL); R2-F14 nothing developed crosses generations (FATAL for H3); R2-F15
grace has no operational hook; R2-F7; R2-F8 deterministic toy has no seed; R2-F9; R2-F10;
R2-F11; R2-F12; R2-F13 family support privileges create a family signal; R2-F16.

## Fix-first picks
Expert: F11 (dwell and update semantics). Bot: R2-F4 (the H1 branch), then R2-F14 (H3), then
R2-F2 (policy).

## Canon link (for Rusty; PRIOR, withheld from all seats)
Three settled rules from the conductor's memory map onto four round 2 problems:
- Crossing-only gate deposit, or inherited ground written only at the gate (Sept 2026;
  Commons v0.10). This answers S2-1 and R2-F14 together: the crossing deposits into
  inherited ground, so something developed does cross generations, only through the gate.
- Grace is the signature required to cross a separatrix (Sept 2026). This answers R2-F15:
  grace becomes the admissibility gate on crossing Σ.
- Lineage-addressed broadcast grace with no per-organism edge (Aug 2026). This answers S2-4:
  a grant not conditioned on an individual's base state can't be used to pick that
  individual's destination.
Releasing these to the designer is Rusty's call.
