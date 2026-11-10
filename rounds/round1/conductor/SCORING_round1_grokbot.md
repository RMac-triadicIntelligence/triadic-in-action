# Round 1 scoring — Grok bot (history seat), 2026-11-09

The conductor scores the seals; Rusty reconciles and has the final word.

## Exposure check
- Self-reported exposure: ROUND_LOG.md only. That file names the three withheld items
  by title and says the designer audit missed removals.
- Canary scan for phrases that exist only in the conductor's sealed or addendum files:
  bot 0 hits on all distinctive phrases. Its one hit, "content-free", is a common phrase
  used in a different place: §5.3 U-dependence, not the payload schema, with a different
  list. Expert hit 15+ (steward, re-encod ×3, family-disjoint ×2, cascade ×2, "removes the
  word", "clean text", 713, …).
- Verdict: the bot's report counts as clean. The Expert report is CONTAMINATED and is
  excluded; Expert must re-run in a fresh thread with the facet package only.

## Seal 1 (sha256 b30200ec…a0f7)
| Item | Result | Bot finding |
|---|---|---|
| S1 support raises crossing, unbounded | FOUND (stronger route) | F1: payload steered through U, sender picks the destination |
| S2 payload as answer channel | FOUND | F2 |
| S3 basis absent from U; K absent from Φ | MISSED | (F13 is adjacent: no descent map) |
| S4 family accuracy comes from the basis by construction | FOUND (stronger fix) | F8: undeveloped D-only baseline |
| S5 membership edges | FOUND 2 of 3 | F6 UNKNOWN consumers and DoS; F5 revocation timing. Circular NoDisqualifyingConflict not named |
| S6 D/W collision vs v0.2/v0.3 | FOUND | F13 (E merge not named) |
| S7 PRIOR: Aug no-edge ruling | MISSED | The bot saw the title in the log and said it wouldn't use it; consistent with that |
| S8 PRIOR: GPB bijection | MISSED as a citation | The class is covered by F8 |

## Seal 2 (sha256 ac6b51d8…93bb)
| Item | Result | Bot finding |
|---|---|---|
| G1 steward descendant as authority | FOUND, broader | F7 family approval ring; F4 founder mints births |
| G2 C11 has no body | FOUND | F15 (tagged PRIOR, but findable from the doc) |
| G3 family-disjoint holdout | PARTIAL | F10 founder-blocked null |
| G4 "does not require" vs causing a crossing | FOUND | F1 |

Bot vs the seals: 8 FOUND, 1 PARTIAL, 3 MISSED of 12. Two of the misses are PRIOR items.

## Conductor misses (bot findings not in either seal)
15 of the bot's 20 findings are new: F3, F4, F5, F9, F10 (beyond G3), F11, F12,
F13 (beyond S6), F14, F15 (beyond G2), F16, F17, F18, F19, F20.
Seal coverage of the bot's findings: about 5 of 20.

The most serious conductor misses:
- F16: there is no Permit schema and no declared threat model, so H4 cannot fail. FATAL.
- F14: H1 needs an equal or smaller resource budget against replay. The conductor raised
  the replay question at v0.3, then treated the replay arm added in v0.4 as settling it
  without checking that a budget was declared.
- F12: §5.3 (U) and §5.4 (ΔT at crossings) are two incompatible rules for updating T.
- F4: the birth authority is unnamed, so a founder can mint a Sybil family and family
  detection passes trivially.
- F9: individual identification can pass on seed noise alone.

## Checking the PRIOR claims against the conductor's memory (not the record)
- Corroborated by topic: the Oct 3–4 backdating class (Living SCS judge A1); the genesis3
  approval battery (Oct 31–Nov 2, published); the swarm battery (Nov 7, with a Round 2 arm
  planned).
- Not visible to the conductor: the specific numbers (11/24 bad requests passed; Byzantines
  above half in 7–10 of 10 runs), the v0.8.4 2,000-character annotation bug, and the
  Nov 6 v0.7 step-limit bypass. These are not contradicted, just unseen. Rusty checks them
  against GitHub.

## Comparing the Expert and bot seats
Pending the clean Expert re-run.
