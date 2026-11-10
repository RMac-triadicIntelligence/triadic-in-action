# The triad method (rounds 1–4)

This is a plain-language account of how "From Reykjavik to Relational Grace" was reviewed in four closed rounds, 2026-11-09, America/Chicago. It is assembled from the conductor logs, scoring notes, and handoffs in this repository. Seat documents themselves were not rewritten.

## Roles

| Role | Who | What they do |
|---|---|---|
| Keel | Rusty Williams McMurray | Human conductor. Relays every message. Rules on grace from the four Gospels only (Matthew, Mark, Luke, John). Final word on scoring. |
| Conductor | Claude | Seals findings *before* the falsifiers see a version, scores after both reports are in, verifies code, keeps the archive. Does not score as a falsifier. |
| Designer | ChatGPT | Revises the specification each round (v0.4 → v0.5 → v0.6 → v0.7). Starts every round in a fresh thread, so each brief has to carry the full current text. |
| Falsifier A (blind seat) | Grok Expert | Attacks the version in front of it. No memory between threads. Findings should be tagged DOC. |
| Falsifier B (history seat) | Grok bot (Chief of Staff) | Attacks the same version, with memory of earlier Rusty work. May tag PRIOR when a finding depends on knowledge outside the document, and must say what. Runs code. |

Handoffs are named `FOR_<RECIPIENT>_RoundN.txt`. The first line names the recipient and says that anyone else should stop and reply `WRONG COPY`. In rounds 3 and 4 the bot was nonetheless handed the Expert's copy first (paste-time misroute; the packets differ by a trailing newline). No sealed file was in those packets. The Task 1b addendum later finished the bot's second-seat check on A's Round 3 findings.

## Blindness

The conductor writes a sealed list of findings against the new version *before* either falsifier sees it. Rusty is given only the hash of that file. The falsifiers do not see the sealed list, each other's reports (except when a later brief includes a prior report for a cross-check), or the conductor's canon notes marked PRIOR and withheld.

After both reports are in, the conductor canary-scans them for phrases that exist only in the sealed files, then scores each sealed item as FOUND / PARTIAL / MISSED against each seat, and logs falsifier findings that were not on the sealed list as conductor misses.

Round 1's first Expert report was contaminated (canary hits on sealed-only phrases) and was excluded. The Expert re-ran in a fresh thread from the facet package only; that re-run was clean.

## DOC and PRIOR tags

Every falsifier finding is tagged:

- **DOC** — found from the document in front of the seat alone.
- **PRIOR** — depends on knowledge outside that document; the seat must say what.

PRIOR is allowed for the history seat. A clean blind-seat report should be all DOC. The conductor also tags some of *its own* sealed items PRIOR when they depend on earlier project canon that was withheld from the facets that round.

## Two-seat closure

A finding counts as **CLOSED** only when its finder and a second seat agree, judging from the text, not from a label in the designer's change register.

This rule was forced by earlier method flaws:

- Round 2: each falsifier judged the fixes to *its own* previous findings (self-vouching). The bot marked its B-F12 CLOSED and thereby endorsed retiring a crossing-specific deposit without noticing the cost.
- Round 3: the seats began to cross-check each other, but a single cross-check could still be too lenient (the Expert marked the bot's R2-F14 CLOSED; the bot, looking again, showed it was only relabeled).
- Round 4: the two-seat rule was used in earnest on the Round 3 findings. The conductor reports that it stopped six premature closures (five times the finder was stricter, once the second seat was).

Statuses used in the ledgers: CLOSED, PARTLY CLOSED / OPEN, RELABELED, BLOCKED-HONEST (honestly marked as not yet buildable). See `CLOSURE_LEDGER.md`.

Rounds 1–4 are **closed as rounds** (versions filed, reports in, scores written, archives kept). That is not the same as every finding being CLOSED. Several Round 3 items remain OPEN, and Round 4 findings still need a second-seat check (planned for Round 5, which is still open and is not in this repo).

## Keel authorization

Grace is not a designer or conductor invention. The keel reads the four Gospels only and settles the definition. While that work was in progress, Round 3 was told "GRACE IS PENDING" and was forbidden to treat its absence as a defect. Round 4 received a keel-approved definition (then v3 in the designer brief; later versions through v11 are in the companion builds repo) and was told not to argue the theology, only to attack how the spec uses it.

A later standing rule (keel, 2026-11-09 1:41 PM CT): build grace from the four Gospels first, and ask the keel whenever a conflict appears. The conductor is not to settle a grace conflict alone.

Items the conductor recorded under delegation (and which the keel may override) are marked as such in the grace-definition files.

## Version table (rounds 1–4 only)

| Round | Target | Authoritative SHA-256 | Status |
|---|---|---|---|
| 1 | v0.4 | `a247652dd5f98365be74245ce6195e06a94673eb4dce48ceb329ca3553903eba` | closed |
| 2 | v0.5 | `8ced5fd1833909c218880619daaeea2109fb484d1ea1e5ddb80f245d79f6fd05` | closed |
| 3 | v0.6 | `e03df96bc0175491c79645c94f0d4fc275d47c1b264d65ced059ccf41766dc1f` | closed |
| 4 | v0.7 | `0cf7c9a7bac7205c830d492e2f398fe04018d1e22da4c3dddc4388f2ebaaab29` | closed |

Round 5 / v0.8 is still open and is not published here.

The paper texts live in the companion repo `triadic-in-action-builds`, under `papers/`. The same bytes are also in this repo's conductor `source/` folders.

## Correlated misses (both seats), as scored

The conductor treats these as a pattern to watch, not as a finished result: R1 S3 (basis absent from U); R2 S2-2 (toy Φ omits H and Q); R2 S2-4 (destination-free grace vacuous under determinism); R3 S3-4 (permanent deadlock if the human signers are gone); R4 S4-4, S4-5, S4-6 (key count, grace exhaustion in long silence, two truncated quotes). Long-silence liveness was missed by both seats in both rounds 3 and 4.
