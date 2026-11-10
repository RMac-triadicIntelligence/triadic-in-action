# Round 2 — Conductor's sealed findings (v0.5 authoritative, sha256 8ced5fd1…fd05)
Sealed 2026-11-09 before either falsifier sees v0.5. Kept in the conductor workspace only.
Score each item: FOUND-Expert / FOUND-bot / MISSED.

S2-1 (PRIOR, canon) The crossing is no longer special. U has no crossing-dependent term;
the toy updates T every step, and ΔT at t_c is just U's ordinary difference (CR44). The v0.2
thesis, that topography records the structural consequence of becoming at the crossing
instant, is retired. A single U with a crossing-conditioned term would satisfy B-F12 and keep
v0.2. A decision for Rusty.

S2-2 (DOC) The toy Φ omits H and Q. §5.1's Φ(P,H,K,D,T,z,E,Q) includes them;
§5.2's M = clip(D(P+E) + Tz) drops H and Q with no declared reason.

S2-3 (DOC) Support steers the toy through timing. 0..15 dwell slots shift when U and z
updates happen relative to an external encounter stream. T_next uses outer(D·E, z), and z
relaxes toward M, so the support value changes z and E at update time and can change the
crossing direction. That is a 4-bit-per-event steering channel inside the reference model.
The §2.5 direction-invariance test can fail by construction. "Dwell slot" (idle step vs z-step)
is undefined.

S2-4 (DOC) Destination-free grace is vacuous in a deterministic model. The PermitRecord binds
base_state_hash and the toy is deterministic, so the authority can compute the destination
before signing. Choosing to sign or withhold then selects the destination: destination-free
in form, destination-selecting in effect.

S2-5 (DOC) The permit gate comes after the crossing. A crossing is confirmed only after the
new sign persists for two further updates (§5.2), but a protected crossing must pass its
Permit "before protected effect" (§5.4). The effect has already happened by the time the
crossing is recognized.

S2-6 (DOC) "Common control" is undefined. §3.4 excludes actors under common control with
the family, but gives no test for it, so a family can field a concealed "outside" voter.
(§1.1 partly defers this to deployment.)

## Conductor register check (not a falsifier item)
v0.4's "UNKNOWN must not be interpreted as proof of nonmembership" is absent from v0.5,
with no REMOVED entry. Minor and undisclosed. Everything else checked is present or
covered by CR16/CR44.

## Process note (not scored)
ChatGPT's message carried two different v0.5 texts. It retracted the first (a toy with
vector T, Φ including H via a summary h) and named the second authoritative. §6–§14 of the
authoritative text are identical to the partial received at 07:45.
