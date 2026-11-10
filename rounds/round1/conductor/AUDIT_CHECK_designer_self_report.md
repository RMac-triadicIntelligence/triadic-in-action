# Conductor check: ChatGPT's change audit vs the machine diff — 2026-11-09

Inputs: chatgpt_change_audit.txt (designer self-report, 25 items), paste_vs_clean.diff.
ChatGPT stated its audit was a manual comparison, not byte-exhaustive. This check is
the byte-level comparison.

## Result
The self-report accurately describes what was ADDED. It reports no deletions at all:
the words removed, deleted and dropped never appear in it. The diff shows these removals
or narrowings, none of which the audit lists:

R1 (most consequential) Authority-manufacture rule narrowed.
  Paste §2.1: "A lineage's root of trust and authority succession must remain externally
  governed. The family cannot manufacture a new independent authority by creating
  descendants, aliases, or additional keys."
  Clean §2.2: "An organism cannot manufacture family membership merely by presenting a
  new key or alias."
  What was lost: the AUTHORITY clause (it became a membership clause), the descendants
  route, and the external governance of trust-root and authority succession.

R2 C11 left without a body.
  Paste §4.3: "an authorized developmental crossing must not be conflated with an
  exact-change approval of K." Removed. C11 still appears in the register, but no body
  text implements it now.

R3 Family-disjoint evaluation removed.
  Paste §3.1: "family-disjoint evaluation where the task calls for generalization to
  unseen founders." Clean keeps only "held-out generalization performance" (§3.3),
  which no longer says held-out families.

R4 The crossing prohibition was weakened.
  Paste: support "cannot ... force a separatrix crossing."
  Clean §1.1: support "does not require i to cross."
  "Does not require" bars mandating a crossing, not causing one.

R5 "Context" removed from the permitted support effects (§1.1). The audit's item 3
  mentions only the added accept/reject/unresolved choice. This is the edit that mooted
  sealed item S2.

R6 The specific capture attack was generalized.
  Paste E6: "redirect lineage-addressed grace or authorization to a newly registered
  identity."
  Clean E6: "lineage-addressed permission misdelivery." The new-enrollment route and the
  word grace are gone.

R7 Misstatement: audit item 12 says the clean version "retained the four possible
  outcomes." The paste predeclared three ("three competing outcomes") plus a separate
  fail sentence.

## Method note
A designer's self-report caught additions and missed every removal. Rule for later
rounds: no re-emitted artifact is accepted without a machine diff run by the conductor.

## Credit
ChatGPT disclosed unprompted that the re-emission was not notation-only, admitted it
should have flagged the changes, and named the limit of its own manual comparison. It
attributes no change to any source outside the conversation's prior critiques.
