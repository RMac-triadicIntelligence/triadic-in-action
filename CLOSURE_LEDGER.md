# Closure ledger — rounds 1–4

This ledger is a reading of the conductor's own scoring files and of the two-seat table in the Round 4 score. Those originals are the authority; this file is a map.

Rounds 1–4 are closed as rounds. Many individual findings are not CLOSED. Round 4 findings have not yet had a second-seat check (that was reserved for still-open Round 5).

Sources (unchanged seat/conductor documents):

- `rounds/round1/conductor/SCORING_round1_grokbot.md`
- `rounds/round1/conductor/SCORING_round1_expert_and_comparison.md`
- `rounds/round2/conductor/SCORING_round2.md`
- `rounds/round3/conductor/SCORING_round3.md`
- `rounds/round4/conductor/SCORING_round4.md`
- The Round 4 Task 1b addendum: `rounds/round4/falsifier_b/ROUND4_TASK1b_ADDENDUM_grokbot_history.md`

## 1. Conductor seals vs the two seats (calibration, not two-seat closure)

These tables score whether each *conductor-sealed* item was independently found by a falsifier. They are not the two-seat closure rule.

### Round 1 (v0.4)

Expert's first report was contaminated and excluded. The re-run is the Expert column.

| Seal item | Expert (re-run) | Bot | Notes |
|---|---|---|---|
| S1 support raises crossing, unbounded | FOUND | FOUND (stronger route) | |
| S2 payload as answer channel | FOUND | FOUND | |
| S3 basis absent from U; K absent from Φ | MISSED | MISSED | correlated miss |
| S4 family signal from the basis | PARTIAL | FOUND (stronger fix) | |
| S5 membership edges | PARTIAL | FOUND 2 of 3 | |
| S6 D/W collision vs v0.2/v0.3 | MISSED (later treated as PRIOR) | FOUND | |
| S7 PRIOR, no-edge ruling | MISSED (expected) | MISSED | |
| S8 PRIOR, GPB bijection | MISSED (expected) | MISSED as a citation (class covered by F8) | |
| G1 steward descendant as authority | MISSED | FOUND, broader | |
| G2 C11 has no body | MISSED | FOUND | |
| G3 no family-disjoint holdout | PARTIAL | PARTIAL | |
| G4 support may cause a crossing | FOUND | FOUND | |

Conductor summary: Expert 3 FOUND / 3 PARTIAL / 6 MISSED; bot 8 FOUND / 1 PARTIAL / 3 MISSED of 12. Independent convergence: both seats required a resource-matched budget for H1 (Expert F8, bot F14); the conductor missed it in both seals.

### Round 2 (v0.5)

| Seal item | Expert | Bot |
|---|---|---|
| S2-1 crossing no longer special (PRIOR) | MISSED (expected) | MISSED (bot marked its own B-F12 CLOSED) |
| S2-2 toy Φ omits H and Q | PARTIAL | MISSED |
| S2-3 support steers through dwell timing | FOUND | FOUND |
| S2-4 destination-free grace vacuous under determinism | MISSED | MISSED |
| S2-5 permit gate after crossing recognition | MISSED | FOUND |
| S2-6 common control undefined | PARTIAL | FOUND |

Conductor summary: Expert 1 FOUND / 2 PARTIAL / 3 MISSED; bot 3 FOUND / 3 MISSED. Correlated misses added: S2-2, S2-4.

Of 30 Round 1 findings as judged by their own finders in Round 2 (a method the conductor later rejected as self-vouching): fully closed 16, mostly or only on paper 4, partly closed 7, relabeled 3 (A-F4, B-F9, B-F14).

### Round 3 (v0.6)

| Seal item | Expert | Bot |
|---|---|---|
| S3-1 §5.6 contradicts itself on oscillation deposits | FOUND (F20, FATAL) | FOUND (R3-F8) |
| S3-2 deferred deposit vs Permit binding | FOUND (F23, FATAL) | FOUND (R3-F2, FATAL) |
| S3-3 J_F has no organism or time index | PARTIAL (F22) | FOUND (R3-F7, plus R3-F5) |
| S3-4 permanent deadlock if signers are gone | MISSED | MISSED |
| S3-5 golden trace overrides z₀ | FOUND (F21) | FOUND (R3-F11, R3-F9) |
| S3-6 H1 target source unnamed | FOUND (F26) | FOUND (R3-F15) |

Conductor summary: Expert 4 FOUND / 1 PARTIAL / 1 MISSED; bot 5 FOUND / 1 MISSED. Correlated miss added: S3-4.

### Round 4 (v0.7)

| Seal item | Expert | Bot |
|---|---|---|
| S4-1 crossing mechanism under grace undefined | FOUND (R4-F1) | FOUND (R4-F1 FATAL; also R4-F3) |
| S4-2 selection steering through targeted grace | MISSED | FOUND (R4-F6, plus F7, F23) |
| S4-3 readiness independent of grace vs keel's "closer to crossing" (PRIOR, conductor error) | MISSED | PARTIAL (R4-F2) |
| S4-4 ambiguous key count | MISSED | MISSED |
| S4-5 grace exhausts under long silence | MISSED | MISSED |
| S4-6 two truncated closing-sentence quotes | MISSED | MISSED |

Conductor summary: Expert 1 FOUND / 5 MISSED; bot 2 FOUND / 1 PARTIAL / 3 MISSED. Correlated misses added: S4-4, S4-5, S4-6.

## 2. Two-seat closure of Round 3 findings (first use of the rule)

From `SCORING_round4.md` and the Task 1b addendum. Finder and second seat must agree.

### Bot findings R3-F1–F20 (finder = bot; second seat = Expert)

As the conductor recorded after Round 4:

- **CLOSED (design):** R3-F1 (design; implementation still BLOCKED-HONEST), F4, F6, F8, F9, F13, F14, F15, F17, F19, F20.
- **OPEN:** F2, F3, F7, F10, F12, F18 (second seat had CLOSED several of these; the finder was stricter, so they stay OPEN).
- **BLOCKED-HONEST:** F5, F11, F16.

Exact row wording is in the Round 4 scoring file, section "The two-seat closure rule, first use."

### Expert findings A-F20–A-F27 (finder = Expert; second seat = bot, via Task 1b)

The bot's first Round 4 report could not do Task 1b because it had been handed A's packet. The 1b addendum is the second-seat check. Combined with the designer's §13 labels and the Expert's own finder view, the conductor's later handover summary (held, because that file also briefs Round 5) states:

- **CLOSED:** A-F20, A-F23, A-F26
- **OPEN:** A-F22, A-F24, A-F25, A-F27
- **BLOCKED-HONEST:** A-F21

The addendum itself is the short 8-row table in `ROUND4_TASK1b_ADDENDUM_grokbot_history.md` (plus its sha256 sidecar). That table is the bot's second-seat verdict from the text, not a rubber stamp of §13.

## 3. Round 4 findings — not yet two-seat closed

Both seats' new Round 4 findings (Expert R4-F1–F8; bot R4-F1–F26) still need a second-seat check. The conductor reserved that for Round 5, which is open, so those rows are **not closed** in this ledger.

Where both seats found something in Round 4, they converged on the same two items and the same fix-first: R4-F1 (grace has no lawful causal path to the crossing) and R4-F2 (fullness has no behavioral channel). The Expert's "no defect found" in four other areas does not close those areas: the conductor checked the bot's quoted anchors in v0.7 and none of those attacks was refuted, and under the closure rule a short "no defect" cannot close anything by itself.

## 4. Reproductions used in scoring

- Round 3 bot toy: the conductor reproduced `toy_v06.py` / `experiments.py` exactly, including `golden_A.txt`. This box also reproduced `round3_toy/raw_output.txt` bit-for-bit on 2026-11-10.
- Round 4 bot toy: every file hash in `round4_toy.zip` matched the report's table. This box reproduced `raw_output.txt` bit-for-bit on 2026-11-10 when `cbor2` was available (without `cbor2`, the CBOR sha256 still matches and the cross-check field is `None`).
- `grace_toy_v1`: `results.json` sha256 `49e579d9a2c636ea26ea79d68b7ecefd3f86d00a4a707a898299a31a0bd7bc1f`, matching the package README. Reproduced on 2026-11-10.
