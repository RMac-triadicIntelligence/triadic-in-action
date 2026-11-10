# Round 4 report — Task 1b addendum

History seat (Falsifier B); source `file_1249.txt` (sha256 542562f7…d165); v0.7 sha256 0cf7c9a7…ab29 (lines 39–1638 of `file_1156.txt`); not opened: `unpacked/round1_conductor_archive/sealed/`, `source/`, every `AUDIT_CHECK_*` file, and the v1 prompts. The Round 4 report is unchanged.

| Finding | Verdict | Exact v0.7 sentence | Reason |
|---|---|---|---|
| A-F20 | CLOSED | “There is no second rule that writes a provisional candidate deposit.” (§4.6) | The contradictory already-committed path is deleted; a candidate is a reservation, and an oscillation writes no deposit. |
| A-F21 | BLOCKED-HONEST | “No bit-exact results for G01–G26 are claimed in this document.” (§9) | G02, G08–G10, G13 and G15 name the traces A asked for, but their input bytes and expected states are not supplied. |
| A-F22 | BLOCKED-HONEST | “For a two-coordinate reference, define a projection of effective deposits into a two-coordinate vector, calculated deterministically from the ordered deposit records.” (§7.2) | The toy is now required to read J, but the exact formula A asked for is not given, so two implementers can still diverge (same residual as our R3-F5). |
| A-F23 | CLOSED | “It does not require the current ordinary T/z/E hash to equal the phase-1 base hash.” (§5.2) | Phase 2 binds the reserved intent, not the stale ordinary-state hash; the later CAS residual is our R4-F16, not this finding. |
| A-F24 | PARTLY CLOSED | “The J-shuffled arm preserves the same crossing points, counts, and marginal slice values while disrupting the alignment between deposit and crossing.” (§10 H3) | J-empty and J-shuffled arms on the same crossing points are now required, but because the shuffle keeps the slice values, a high-entropy pattern in those values still survives, and residual family signal after shuffling is not called contamination. |
| A-F25 | PARTLY CLOSED | “Until the exact bytes and digests are generated and checked, canonical-encoding conformance and H4 hash-binding tests remain BLOCKED.” (§8.4) | The STATE key map and RFC 8949 rule are now specified (§8.1, §8.3), but 15 field types and all non-STATE record maps are still missing (R4-F19), and the three vectors are honestly unproduced. |
| A-F26 | CLOSED | “The target-generating family is frozen by an independent party and must include at least one non-bilinear process.” (§10 H1) | An independent party now freezes the targets, and at least one process cannot be the same outer-product form as U. |
| A-F27 | PARTLY CLOSED | “Its family, descendants, ancestors, aliases, or controlled institutions cannot form an approval coalition for that operation.” (§3.1) | The exclusion now covers controlled institutions, and E6 names reciprocal-approval tests, but no operative section defines the cycle-check algorithm A asked for. |

The sha256 of this addendum is in `ROUND4_TASK1b_ADDENDUM_grokbot_history.md.sha256`.
