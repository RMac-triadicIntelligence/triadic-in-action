# Round 3 — Conductor's sealed findings (v0.6 assembled, sha256 e03df96b…dc1f)
Sealed 2026-11-09 before either falsifier sees v0.6. Kept in the conductor workspace only.

S3-1 (DOC) §5.6 contradicts itself on oscillation. It says "a candidate that oscillates
produces no J_F deposit", and also says to "retain ... any already committed authorized
deposit as a separately identified candidate deposit requiring correction."

S3-2 (DOC) The deferred deposit can't be checked against its own binding. The Permit binds
base_state_hash, the pre-state (§2.2, §5.2). §5.6 appends δ_F two learning steps later
"under the same bound authorization ... subject to revalidation". By then the state has
changed: either the deposit is always refused, or the binding is quietly relaxed, which
weakens H4.

S3-3 (DOC) J_F has no organism or time index. §1.3 gives descendants an immutable snapshot
of J_F at birth, but Φ in §5.1 takes the bare J_F. It's unspecified whether a child's Φ reads
its birth snapshot or the live lineage sequence, including the parent's later deposits.
(This is the argument-mismatch class both seats missed in rounds 1 and 2.)

S3-4 (DOC) Permanent deadlock if the human signers are gone. §2.5 makes PA signers
"externally accredited humans or institutions"; §2.1 protects timeout rules, root succession
and PA membership. If the signer population disappears or goes silent, nothing can authorize
succession, and every protected operation stays PENDING forever. No standing grant and no
succession path exist without the signers.

S3-5 (DOC) The golden trace avoids the parts under test. Appendix A overrides z₀ to
(256,128), against the frozen (−256,128) in §5.3, to avoid a crossing. With E = 0 and no
encounters, T never moves, so the "normative" vector exercises only z relaxation: no U, no
J, no gate, no holds.

S3-6 (DOC, minor) H1's "held-out targets generated independently of the T reference model"
never names where the targets come from.
