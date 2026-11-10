# Round 4 — Conductor's sealed findings (v0.7 assembled, sha256 0cf7c9a7…ab29)
Sealed 2026-11-09 before either falsifier sees v0.7. Kept in the conductor workspace only.

S4-1 (DOC) The crossing mechanism under grace is undefined, so the barrier test passes by
construction or by fiat. Grace may not lower the barrier (§1.2), push (§1.4), write state or
destination (§2.5), or steer (§1.9), and the ordinary dynamics are gradient-driven on
V(x,h)=h(x²−1)² (§7.4). Nothing in the model can then carry a ready organism over a high
barrier, except the gate writing z across Σ, which is a privileged state write that §2.5
forbids. Either crossings never occur at high h, or the gate "permits" one by declaration and
§7.7's height-independence holds by definition. (The designer's own closing note half-flags
this.)

S4-2 (DOC) Selection steering through targeted grace. Grace may "seek the one" (§1.12), and
a deterministic observer can predict readiness and destination (C4 residual, §12). A grantor
can therefore choose WHOM and WHEN to grant so that only crossings toward a preferred basin
happen. Each grant is direction-free, yet the set of grants selects destinations. This
defeats §1.9 in effect. Possible fix: grant decisions committed blind to destination
prediction (B's "blind grace" blue-sky).

S4-3 (PRIOR — the keel's words) Readiness is fully independent of grace (§7.4: "The
readiness rule is independent of grace receipt"). The keel said that when the organism is not
ready, grace leaves it "just closer to crossing", through fullness. Under v0.7 the fullness
from grace can never contribute to readiness, so grace to the unready never brings it closer.
CONDUCTOR'S OWN ERROR: "closer to crossing" was dropped when item 4 of the grace definition
was recorded, so the designer could not have known. A keel decision for round 5.

S4-4 (DOC) Ambiguous key count. §1.3 and §7.6 say a crossing takes two keys (grace +
readiness). §5.1 has the gate verify grace, readiness, policy AND external authorization for
the phase-1 candidate. It's unclear whether a grace-enabled crossing also needs a Permit, which
would make three keys, or whether the Permit is needed only for the J deposit.

S4-5 (DOC) Grace under long silence. A GraceGrant has expiry and relay budget (§2.2, §2.4),
and no organism may originate grace (§1.1). In long silence every grant eventually exhausts,
so no grace-enabled crossing can ever happen again. §3.4 standing grants cover "ordinary
developmental operations" and protected operations, but do not say whether a standing general
grace grant (no expiry, "rain on the just and the unjust") is allowed. Development past any
barrier stops at exhaustion, which conflicts with the keel's long-absence horizon where
growth continues.

S4-6 (DOC, minor) Two quoted closing sentences in §12–§14 are truncations (KEEL 14, B-R3-F12).
Harmless, but the convention is exact sentences. The other 42 quotes are verbatim in the body.
