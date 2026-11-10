# Round 1 scoring — Grok Expert (blind, re-run) and comparison of the two seats — 2026-11-09

Treated as the Grok Expert re-run in a fresh thread with FOR_GROK_EXPERT_Round1.txt only.

## Exposure check
Canary scan: 0 hits on every sealed-only phrase. All 10 findings are tagged DOC and none
PRIOR, which is what a blind seat should produce. The report counts as clean.

## Expert vs the seals
| Item | Result | Expert finding |
|---|---|---|
| S1 support raises crossing, unbounded | FOUND | F1 (covert payload through Φ/U; or a provisional flag into A) |
| S2 payload as answer channel | FOUND | F1, F9 |
| S3 basis absent from U; K absent from Φ | MISSED | F7 is broader underdetermination and doesn't name it |
| S4 family signal from the basis by construction | PARTIAL | F5: undeclared shared seed or initialization, not the declared D |
| S5 membership edges | PARTIAL | F10: UNKNOWN missingness inflates accuracy |
| S6 D/W collision vs v0.2/v0.3 | MISSED | Conductor correction: S6 was mis-tagged DOC. It needs v0.2/v0.3 notation, so it is effectively PRIOR |
| S7 PRIOR: no-edge ruling | MISSED (expected) | — |
| S8 PRIOR: GPB bijection | MISSED (expected) | — |
| G1 steward descendant as authority | MISSED | F3/F4 cover forged membership, not authority assignment |
| G2 C11 has no body | MISSED | — |
| G3 no family-disjoint holdout | PARTIAL | F5: shared artifacts |
| G4 support may cause a crossing | FOUND | F1 |

Expert: 3 FOUND / 3 PARTIAL / 6 MISSED. Of the 9 items findable from the document
(excluding S6, S7, S8): 3 found, 3 partial, 3 missed (S3, G1, G2).
Bot, for reference: 8 FOUND / 1 PARTIAL / 3 MISSED.

## Conductor misses (Expert findings in neither seal)
F2 type label alone changing confidence; F3 registry security as an undischarged
assumption; F4 colluding birth forgery; F5 undeclared shared initialization; F6
threshold instability and pre-registration; F7 no reference implementation; F8
resource-matched baselines for H1. F9 and F10 partly overlap S2 and S5.

## Comparing the seats (same model family, different history)
- Volume: bot 20 findings, Expert 10.
- PRIOR use: bot about half carry PRIOR support; Expert zero.
- What history added: breadth, fixes backed by precedents from past batteries, cross-references
  to the canon (the S6 collisions; C11 cross-checked against the body), and the
  coalition-level reading of "nothing may vouch for itself" (bot F7).
- What the blind seat added: fixes at the mechanism level — an information-flow type system
  or taint barrier (F1), identical update paths for G and Encounter (F2), a reference
  implementation (F7), and enumerating shared initialization state (F5).
- Independent convergence: both seats require a resource-matched budget for H1 (Expert F8,
  bot F14). The conductor missed this in both seals. It is the round's strongest finding.
  Discount it somewhat: the seats are the same model family, and the prompt nominated the
  property.
- Disagreement on fix-first: Expert F1 (an information-flow barrier against support
  laundering); bot F16 (Permit schema and threat model). The two are complementary.
- Correlated miss (a test of the bot's blue-sky hypothesis on the Triad itself): both seats
  missed S3, that the basis is absent from the update rule U. One item is an anecdote, not
  a result, but it is the predicted pattern: kin share blind spots.
