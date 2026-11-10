# Round 1 — Conductor's sealed findings (v0.4)

Sealed 2026-11-09 before either Grok facet has seen v0.4.
Purpose: reviewer calibration. After both Groks return, score each item below as
FOUND-Expert / FOUND-bot / MISSED, and log every Grok finding not on this list as a
conductor miss. The conductor does not score the round; Rusty reconciles.

Do not relay this file to any facet until both falsifier reports are in.

## S0 — Transport defect (excluded from scoring; fix before sending)
Math symbols were stripped in the paste: blank symbol column in the §4 table;
"For an organism , define"; "family root ."; "Here, is explicitly restored";
four non-equivalence relations in §1.2 run together on one line. Same loss as v0.3.

## Spec findings

S1 (DOC) Support can raise crossing probability via dwelling.
§1.1 lets support change the availability or duration of a dwelling opportunity.
Longer dwell near a separatrix changes crossing likelihood, so "Support ⇏ Crossing"
holds only as "no direct cause." Exp 5 holds authorization fixed but sets no bound on
how far support may shift crossing rates, so legitimate influence and laundering are
indistinguishable. Fix: predeclare a maximum support effect on crossing rate; above it
counts as laundering.

S2 (DOC) "Context" is an answer channel.
§1.1 lets support grant access to "context"; bounded_payload is untyped. §1.2 separates
an Encounter delivered alongside support, but not content carried inside the support
payload. Fix: support payload is content-free (scheduling / permission / duration
only), or any content makes it an Encounter.

S3 (DOC) Basis absent from the update rule.
The basis is defined as the axes memory forms along, but U in §4.3 does not take the
basis. Either the basis does not shape deposit (contradicting its definition) or U is
underspecified. K is also absent from Φ.

S4 (DOC) Family accuracy may measure Φ's invertibility in the basis.
The basis enters Φ directly. If Φ is near-injective in it, family detection passes by
construction; likewise individual identification via H_i. Needs a control where the
basis is re-encoded (same information, different representation), or Φ's sensitivity
to the basis is measured and capped.

S5 (DOC) Membership predicate undefined at the edges.
NoDisqualifyingConflict is undefined. Behavior of SupportEvent and lineage-addressed
grants when membership = UNKNOWN is unspecified (fail-closed?). Whether revoking an
ancestor cascades to descendants is unspecified.

S6 (DOC, probable — depends on S0) Symbol reassignment.
By tuple order, D now = basis and W = dwelling. In v0.2/v0.3, D = dwelling and
W = witness evidence. The B/E collision is fixed by creating a D/W collision against
the source papers. E merges evidence and experience into one symbol, which blurs the
distinction rather than resolving it.

## Canon-dependent (held back from facets this round)

S7 (PRIOR) The Aug 2026 lineage-addressed grace had no organism-to-organism edge.
Support_{j→i} and Blue-sky 3's support network reintroduce one as a non-authority
channel. A decision for Rusty, not a spec defect.

S8 (PRIOR) Genesis-Palette bridge v0.2.1 found the phenotype was a bijection of the
genome, so identity tests passed at ceiling on invertibility. S4 is the same class.
