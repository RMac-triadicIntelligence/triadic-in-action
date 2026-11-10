# Round 3 scoring — 2026-11-09 (the conductor scores; Rusty reconciles)

Seal: conductor_sealed_findings_round3.md, sha256 1adae88b…279f. It stayed in the conductor
workspace.

## Exposure check
Both reports: 0 sealed-only phrases. Expert: 8 new findings, all DOC. Bot: 20 new findings,
18 DOC and 2 PRIOR (Byzantine quorum theory; the CBOR RFCs, both public standards).
Process note: the bot first received the Expert's handoff by misroute. It declined to grade
its own findings, then received its own handoff. Nothing sealed was exposed.

## Against the round 3 seal
| Item | Expert | Bot |
|---|---|---|
| S3-1 §5.6 contradicts itself on oscillation deposits | FOUND (F20, FATAL, fix-first) | FOUND (R3-F8) |
| S3-2 the deferred deposit vs the Permit's base-state binding | FOUND (F23, FATAL) | FOUND (R3-F2, FATAL) |
| S3-3 J_F has no organism or time index (snapshot vs live) | PARTIAL (F22: toy Φ never reads J) | FOUND (R3-F7, both failure scenarios; plus R3-F5) |
| S3-4 permanent deadlock if the human signers are gone | MISSED | MISSED |
| S3-5 golden trace overrides z₀ and tests only z relaxation | FOUND (F21) | FOUND (R3-F11, R3-F9) |
| S3-6 H1 target source unnamed | FOUND (F26) | FOUND (R3-F15) |
Expert: 4 FOUND / 1 PARTIAL / 1 MISSED. Bot: 5 FOUND / 1 MISSED.

## Correlated misses
S3-4 (signers gone → permanent deadlock) was missed by both seats. Across rounds 1–3 the
correlated misses are R1 S3, R2 S2-2, R2 S2-4 and R3 S3-4.

The argument-mismatch blind spot (rounds 1–2) did NOT recur: both seats found "J_F is in Φ
but the toy Φ never reads it". Caveat: v0.6 §5.8 itself flagged the class (the C3
"declared specialization"), and the bot cites it. The document primed the find, so this is
not evidence that the seats improved.

## The cross-check (first time)
- Bot checking A: 12 closed, 6 partly, 1 relabeled of 19. It caught two overstated
  dispositions (A-F18 "seed-matched"; A-F7 "full toy rules").
- Expert checking B: mostly agrees with the designer. It marked B's R2-F14 CLOSED, while the
  bot, re-examining its own finding, shows it is only RELABELED: nothing reads J_F (R3-F5).
- So in round 2 the self-check was too lenient (the bot passed its own B-F12), and here a
  cross-check was too lenient (the Expert passed B's R2-F14). Neither single check is enough.
  Rule from round 4: both the finder and a second seat sign off before a finding counts as
  CLOSED.

## Conductor's reproduction of the bot's toy
- The bot's toy_v06.py and experiments.py were run in a clean folder. Output reproduced
  exactly, and golden_A.txt matches the Appendix A rows.
- Confirmed: Appendix A reproduces; the default z₀ (−256,128) produces a CONFIRMED crossing at
  t=3 with no input; 0/1/15 holds are bit-identical; the rounding mode is the only thing the
  trace catches (half-away and trunc fail at row 2, floor at row 3).
- Nuance: of the four alternative readings that pass the trace, only "M uses T_next" diverged
  on the bot's realistic 10-encounter stream (at step 9). The other three (saturation order,
  M−z saturation, double rounding in outer) diverge only in constructed edge cases (EXP6, EXP9).
  They are real ambiguities, but the bot's "first real encounter stream" scenario is slightly
  overstated for them.
- Classifier gaps confirmed: through-zero is UNKNOWN twice; an oscillation's return leg
  becomes a CONFIRMED crossing.

## Conductor misses (not in the seal)
Bot:
- R3-F1: 2-of-3 doesn't tolerate a malicious member. Needs n≥3f+1. FATAL for the one-fault claim.
- R3-F3: holds push a pending deposit past Permit expiry, so support selects which crossings
  become lineage ground; W in the base hash gives support a veto.
- R3-F4: the bit-identity test can't fail by construction.
- R3-F5: J has no causal path in the toy, and δ_F has no schema. FATAL for H3.
- R3-F6: δ_F either carries parental T or carries nothing developmental.
- R3-F9: what a gate refusal blocks is undefined; the default z₀ crosses at t=3.
- R3-F10: crossings are set by start position relative to P₀, not by development.
- R3-F11 through R3-F20.
Expert:
- F24: J deposits used as a seed pattern.
- F25: no concrete CBOR field IDs.
- F27: no approval-graph cycle check.

## Fix-first picks
Expert: F20 (one deposit rule). Bot: R3-F5 (give J a causal path and a δ_F schema), then R3-F1,
then R3-F2.
