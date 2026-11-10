# Round 4 scoring — 2026-11-09 (the conductor scores; Rusty reconciles)

Target: v0.7 assembled, sha256 0cf7c9a7…ab29.
Seal: r4sealed/conductor_sealed_findings_round4.md, sha256 1f518dd8…1a5c. It stayed in the
conductor workspace.

Reports (filed read-only):
- Grok Expert (Falsifier A, blind seat): r4reports/grok_expert_round4.txt, sha256 a3673ebb…e5b5
- Grok bot (Falsifier B, history seat): r4reports/grokbot_round4.md, sha256 22fb2834…8bfd
- Bot code: round4_toy.zip, sha256 ce958337…abdc (6 files; every file hash matches the
  report's table)

## Routing
The bot received the Expert's handoff again (as in round 3). Its file_1156.txt hash
1ddbfa69… equals FOR_GROK_EXPERT_Round4.txt with the final newline removed. The copy page's
buttons map correctly (exp4 → 319164ec, bot4 → c6d87a84), so the slip was at paste time.
Effects:
- no sealed material was exposed (both copies carry only v0.7 plus one prior report);
- the bot saw its own round 3 report and not A's, so its Task 1b (second seat on A-F20…A-F27)
  is a placeholder. A 1b-only handoff fixes it.
From round 5, each Grok handoff starts with a stop line naming its recipient.

## Exposure check
- Expert: 0 sealed phrases.
- Bot: 0 sealed-only phrases. "Selection steering" matches S4-2's title but is a generic
  two-word description; the bot coined "blind grace" in round 2 and the seal never left this
  workspace. "Lifted" is used in its ordinary sense, not the keel's (lift/nudge post-date the
  round 4 handoffs). Neither seat uses fill, nudge, or "closer to crossing".
- The bot again lists the round 1 conductor archive (unpacked/round1_conductor_archive/) as
  present on its machine and not opened. Round 1 is closed. That line is redacted in anything
  forwarded, as in round 3.
- Source tags: Expert 8 items, all DOC. Bot 26 findings, 24 DOC and 2 PRIOR (R4-F13 key aging
  and RFC 4998; R4-F14 fencing tokens). The bot flags both as from memory.

## Against the round 4 seal
| Item | Expert | Bot |
|---|---|---|
| S4-1 crossing mechanism under grace undefined; the barrier test passes by construction or fiat | FOUND (R4-F1, WOUNDING, fix-first: respecting V makes success h-dependent; forcing independence breaches §1.2/§1.9) | FOUND (R4-F1 FATAL, fix-first, with computed surrogate; R4-F3 no double-well update rule) |
| S4-2 selection steering through targeted grace | MISSED (treated C4 as "explicitly DEFERRED; not re-opened"; its ZK-readiness blue-sky is adjacent) | FOUND (R4-F6 grantor; extended by R4-F7 family relayers and R4-F23 H3 grant exposure) |
| S4-3 readiness fully independent of grace vs keel's "closer to crossing" (PRIOR, conductor's own error) | MISSED (its R4-F2 fix routes fullness into encounter choice, which feeds evidence and readiness, without flagging §2.5) | PARTIAL (R4-F2: wiring fullness to behavior would be the indirect readiness write §2.5 forbids. That is the structural conflict, though the keel's intent was not available to it) |
| S4-4 ambiguous key count (does a grace crossing also need a Permit?) | MISSED | MISSED (adjacent: R4-F21 notes "applicable external authorization" has no Permit schema) |
| S4-5 grace exhausts under long silence | MISSED (R4-F4: "liveness limit is deliberate") | MISSED (R4-F13 calls expiry-to-wait "the declared exhaustion behavior" and proposes mandatory horizons) |
| S4-6 two truncated closing-sentence quotes | MISSED | MISSED (adjacent: R4-F21 and R4-F22 catch other citation faults) |
Expert: 1 FOUND / 5 MISSED. Bot: 2 FOUND / 1 PARTIAL / 3 MISSED.

## Correlated misses
S4-4, S4-5 and S4-6 were missed by both seats. Running list: R1 S3, R2 S2-2, R2 S2-4, R3 S3-4,
R4 S4-4, S4-5, S4-6.

Pattern: long-silence liveness was missed by BOTH seats in BOTH rounds 3 (S3-4, signers gone →
deadlock) and 4 (S4-5, grace runs out). In round 4 both seats saw the exhaustion and accepted
it as a security property. The kin seats share a security-over-liveness bias. The keel's
horizon (growth continues while authority is silent) has to come from the conductor's items
until a seat shows it can see it unaided.

## Divergence between the seats (new this round)
The Expert reported "No defect found" in four areas where the bot found WOUNDING defects:
- GraceGrant/Relay (Expert R4-F3) vs bot R4-F5, F7, F8, F9, F10, F11, F24;
- standing grants and succession (Expert R4-F4) vs bot R4-F13, F14, F15;
- deposits and two-phase commit (Expert R4-F5) vs bot R4-F16, F17, F18, F25;
- encoding (Expert R4-F7) vs bot R4-F19, F20.
The conductor checked the anchors of R4-F4, F5, F9, F10, F13, F16, F17, F18, F20, F21, F22,
F24, F25 and F26 in the v0.7 text. Every quoted sentence is present and none of the attacks is
refuted. "No defect found" from a short report (55 lines vs about 600) is weak evidence, and
under the closure rule it cannot close anything by itself.

Where both seats found something, they converged on the same two items and the same fix-first:
R4-F1 (grace has no lawful causal path to the crossing) and R4-F2 (fullness has no behavioral
channel).

## The two-seat closure rule, first use
Round 3 findings from the bot (finder = bot, second seat = Expert):
| Finding | Finder (bot) | Second seat (Expert) | Status |
|---|---|---|---|
| R3-F1 | CLOSED (design) | CLOSED (design) / BLOCKED-HONEST (impl) | CLOSED (design) |
| R3-F4, F6, F8, F9, F13, F14, F15, F17, F19, F20 | CLOSED | CLOSED | CLOSED |
| R3-F2 | PARTLY | CLOSED | OPEN (race half: bot R4-F16) |
| R3-F3 | PARTLY | CLOSED | OPEN (grant-expiry channel: bot R4-F18) |
| R3-F7 | PARTLY | CLOSED | OPEN (correction semantics: bot R4-F17) |
| R3-F10 | PARTLY | CLOSED | OPEN (counterfactual start/horizon: bot R4-F25) |
| R3-F12 | PARTLY | CLOSED (design) | OPEN (field values/types: bot R4-F19) |
| R3-F18 | PARTLY | RELABELED | OPEN (§15 cites absent text: bot R4-F21) |
| R3-F5, F11, F16 | BLOCKED-HONEST | (PARTLY/) BLOCKED-HONEST | BLOCKED-HONEST |
Total: 11 CLOSED, 6 OPEN, 3 BLOCKED-HONEST of 20.

Round 3 findings from the Expert (finder = Expert, second seat = bot; bot 1b addendum
r4reports/grokbot_round4_task1b.md, sha256 975d4cbb…4e90; routed correctly; all 8 quotes are
verbatim in v0.7; 0 sealed phrases):
| Finding | Finder (Expert) | Second seat (bot) | Status |
|---|---|---|---|
| A-F20, A-F23, A-F26 | CLOSED | CLOSED | CLOSED |
| A-F24 | CLOSED | PARTLY (shuffle keeps slice values, so a planted pattern survives) | OPEN |
| A-F22 | PARTLY | BLOCKED-HONEST | OPEN |
| A-F25 | BLOCKED-HONEST | PARTLY | OPEN |
| A-F27 | PARTLY | PARTLY | OPEN |
| A-F21 | BLOCKED-HONEST | BLOCKED-HONEST | BLOCKED-HONEST |
Total: 3 CLOSED, 4 OPEN, 1 BLOCKED-HONEST of 8.

What the rule did: it stopped six premature closures. Five times the bot, as finder, was
stricter about its own findings than the Expert was as second seat, and each time it named a
concrete residual. Once (A-F24) the bot, as second seat, was stricter than the finder. So the
rule catches leniency in both directions. It earned its keep on first use.
Both seats: 14 of 28 round 3 findings CLOSED.

## Conductor's verification
- The bot's battery.py was re-run in a clean folder (python -I). Output matched raw_output.txt
  exactly except the cbor2 cross-check line (cbor2 isn't installed here, so it prints None,
  not True).
- Confirmed by reproduction: tags prefix-free; C1 candidate 237 bytes, hash c8c49049…e87f
  (non-normative); G01 trace equal to v0.6 with a confirmed crossing at t=3 and an identical
  no-encounter counterfactual; G05 to G15 values; holds 0/1/15 bit-identical; relay fan-out
  1,110 from one grant; per-product vs once-per-dot-product rounding differs ([0,0] vs [1,0]).
  Also G03: with the bot's inputs T contributes nothing to M ([676,−277] with and without T).
- The Expert's illustrative C1-like vector decodes as a 24-field map (60 bytes), and its claimed
  SHA-256(tag‖CBOR) = ccaef7ea…3640 is correct.
- The two seats' C1 candidates differ (60 bytes vs 237 bytes) and both are consistent with
  v0.7 §8. This is direct cross-seat evidence for bot R4-F19 and Expert A-F25.
- R4-F21 confirmed by text search: v0.6's PermitRecord schema (§2.2), PA accreditation (§2.5),
  quotas (§3.5), elevated threshold and activation delay (CR08), nonretroactive revocation
  (CR13) and BA quotas (CR16) have no counterpart in v0.7 and no REMOVED entry. §3.1 carries
  forward only the protected-operation list. §15.1 cites §3, §3.3 and §2.5 for rules those
  sections don't contain. The v0.6 linear-toy equations (E_next …) are also absent, yet G01
  depends on them.
- R4-F22 confirmed: §15.2's words for A-F3, A-F4, A-F13 and A-F19 are the designer's own
  dispositions, not the bot's round 3 verdicts.

## Conductor misses (not in the seal)
- Bot R4-F21 (governance dropped silently). The conductor's own rule is to diff every
  re-emitted version, and this should have been caught before sealing. A conductor miss.
- Both seats' R4-F2 (fullness has no behavioral path). The seal had only S4-3's half of this.
- Bot: R4-F4 (key 2 attested by one unnamed observer), F5 (general grants let the recipient
  pick when key 1 applies), F7, F8 (no origin accreditation), F9, F10, F11, F12, F13, F14,
  F15, F16, F17, F18, F19, F20, F22, F23, F24, F25, F26.

## Probable root cause of R4-F21 (added 12:55)
ChatGPT starts every designer round in a fresh thread (keel). No designer brief in rounds 2–5
carried the previous version's full text; each said "use … your own v0.x". So v0.7 was written
without v0.6 in front of it, and the governance v0.7 doesn't restate is most likely what the
designer never saw, not a deliberate removal. This was a conductor error. From round 5, every
designer brief carries the full current text (round 5: source supplement, sha256 ae6ce61e…).

## Conductor's own contribution to R4-F1
The prediction "with grace plus readiness, the crossing rate is independent of barrier height"
is the conductor's round 4 brief wording, built on grace v4. Grace v8 replaces it: filling
crosses at every height, taking longer as height grows; a nudge carries a ready organism over at
any fill level and height; the landscape never changes. The round 5 brief carries v8.

## Fix-first picks
Expert: R4-F1. Bot: R4-F1, then R4-F2, then R4-F21.

## Blue-sky (unscored)
- Expert: zero-knowledge readiness attestation (prove readiness on a committed snapshot without
  revealing it).
- Bot: a grace lottery arm. A declared share of grants goes to a public-beacon draw, which
  gives an unbiased grace effect and a baseline for detecting selection steering.
