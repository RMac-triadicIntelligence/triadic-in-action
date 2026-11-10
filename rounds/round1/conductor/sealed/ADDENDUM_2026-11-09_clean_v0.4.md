# Addendum to conductor_sealed_findings.md — 2026-11-09

The sealed file is unchanged (sha256 b30200ec…a0f7). It was written against the
pasted v0.4. This addendum records how each sealed item stands against the clean
v0.4 text ChatGPT returned. It is not part of the seal and is not scored.

Clean v0.4: v0.4_clean_from_chatgpt.txt, sha256 a247652d…3eba
Paste v0.4 (superseded): v0.4_paste_from_chat.txt, sha256 fa26c42a…f6f6

## Delivery against the conductor's request
Requested: one zip with Markdown, PDF, separate change register, MANIFEST.sha256, and
CHANGES_FROM_PASTE.md, with content identical except for restored symbols.
Received: a single plain-text file. No zip, manifest, PDF, separate register, or
CHANGES_FROM_PASTE. The content changed beyond symbol restoration (402 → 713 lines);
C16 and C17 record only the formatting changes. Substantive changes not in the register,
as seen by the conductor (full record in paste_vs_clean.diff):
- §1.1: "context" removed from permitted support effects; "accept, reject, or leave
  unresolved" added
- §1.2: prohibited effects expanded to 10 (adds "increase epistemic confidence" and
  "grant authority not independently established")
- §2.5 added: non-self-authorization across lineage, subject-bound exclusion
- E4: a fourth outcome ("neither detectable") made explicit
- §3.3 scoring outputs and §3.4 negative controls expanded
- §5.4 v0.2 deposition equation retained as historical source
- E6: attack list expanded, including lineage-addressed permission misdelivery and
  support laundering
- §12: a fifth review property added (topography vs full replay and conventional memory)

The conductor treats the clean text as canonical v0.4 for Round 1, identified by its hash.

## Sealed items against clean v0.4
- S0 RESOLVED: symbols present.
- S1 STANDS: §1.1 still permits extending dwelling; E5 still sets no bound on support's
  effect on crossing rates.
- S2 LARGELY MOOTED by an edit after the seal: "context" is gone from permitted effects,
  and content now routes through the separately typed Encounter. Residue: bounded_payload
  is still untyped ("allowed support parameters").
- S3 STANDS: U = U(Tᵢ, Mᵢ, Eᵢ, zᵢ, G) has no Dᵢ; Φ has no Kᵢ.
- S4 STANDS: Dᵢ enters Φ directly; there is no re-encoding control.
- S5 MOSTLY STANDS: NoDisqualifyingConflict is defined circularly ("excluding relevant
  lineage conflicts"); UNKNOWN handling covers the membership verdict but not
  SupportEvent or lineage-addressed grants; revocation is checked on the path, but
  whether it cascades to descendants is unspecified.
- S6 CONFIRMED: the table fixes D = basis and W = dwelling, against v0.2/v0.3 where
  D = dwelling and W = witness evidence. E still merges evidence and experience.
- S7, S8 (PRIOR): unchanged.

## Seal-integrity note
S2's mooting edit came after the seal. It counts as an independent designer fix only if
nothing from the sealed file reached ChatGPT. Rusty to confirm.
