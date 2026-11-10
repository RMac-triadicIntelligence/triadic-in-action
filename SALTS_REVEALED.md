# Salts revealed — rounds 1–4

Rusty lifted the seal on rounds 1–4 at 2:16 PM CT, 2026-11-10, and asked that salts be revealed and labeled.

## What was actually used

No separate cryptographic salt strings were found in the rounds 1–4 materials. The conductor's standing rule, recorded in `CONDUCTOR_HANDOVER.md` (that file is held with Round 5, because it also briefs v0.8), was:

> Seal conductor findings before the falsifiers see a version. Seal stays in the workspace; Rusty gets only the hash.

The commitment, in every round, is the SHA-256 of the sealed findings file itself (`SHA-256(file bytes)`), not `SHA-256(salt ‖ payload)`. There is therefore no salt to concatenate and no salt+payload hash to recompute.

What is revealed here is the sealed payload of each round, together with the hash that was the commitment. Verification is: hash the revealed file and compare it to the hash recorded in that round's scoring note, manifest, or `SEAL_SHA256SUMS_original`.

Mentions of "salt" in the round documents are prose, not openings:

- Falsifier B's "blind grace" blue-sky (Round 2 and later): "in the same spirit as sealed blind-round salts."
- Falsifier B's Round 4 fix for readiness/fullness commitments: "Specify commitments as SHA-256(tag ‖ 32-byte random salt ‖ value), with the salt held by the attester." That is a proposed scheme for the spec, not a sealed-round opening.

Round 5 salts, if any, stay withheld.

## The commitments, now open

All five sealed findings files are in this repo under `rounds/roundN/conductor/sealed/`. Each hash below was recomputed from those bytes on 2026-11-10 and matches the hash the conductor recorded at sealing time.

| Round | Seal | File | Commitment (SHA-256 of the file) | Recorded in | Verified |
|---|---|---|---|---|---|
| 1 | Seal 1 (against the pasted v0.4; also used for the clean text via an addendum) | `rounds/round1/conductor/sealed/conductor_sealed_findings.md` | `b30200eca8475ab039ea8ff8b36c2d7d0053ad670fbe9141d7ec159b6ea5f0a7` | `SEAL_SHA256SUMS_original`; scoring "Seal 1 (sha256 b30200ec…a0f7)" | **verified** |
| 1 | Seal 2 (clean v0.4, G1–G4) | `rounds/round1/conductor/sealed/conductor_sealed_findings_2.md` | `ac6b51d8482f0a7f32a132dfac6b55c1cea052c7239edce1221b1f0ed62093bb` | scoring "Seal 2 (sha256 ac6b51d8…93bb)" | **verified** |
| 1 | Prompt frozen with seal 1 | `rounds/round1/prompts/round1_falsifier_prompt_v1_SUPERSEDED.txt` (original name in the seal list: `round1_falsifier_prompt.txt`) | `1876e4c51662780c342352306c2cdaf332287813ef0c2e1adfd07932d4d77129` | `SEAL_SHA256SUMS_original` | **verified** |
| 2 | v0.5 authoritative (`8ced5fd1…fd05`) | `rounds/round2/conductor/sealed/conductor_sealed_findings_round2.md` | `497f6a04acc3e80519894d748d94ad421d97c20a5e32649c639ed265bf7fe8f3` | scoring "sha256 497f6a04…e8f3" | **verified** |
| 3 | v0.6 assembled (`e03df96b…dc1f`) | `rounds/round3/conductor/sealed/conductor_sealed_findings_round3.md` | `1adae88b202c08b23273451c454efe5b88d12514a99d46b6a5c73c16a67b279f` | scoring "sha256 1adae88b…279f" | **verified** |
| 4 | v0.7 assembled (`0cf7c9a7…ab29`) | `rounds/round4/conductor/sealed/conductor_sealed_findings_round4.md` | `1f518dd8fb8382662673b9e9e014b9b6c48689f01445e24976d965b1bfac1a5c` | scoring "sha256 1f518dd8…1a5c" | **verified** |

Related, not a salt: the superseded v1 falsifier prompt was later replaced by `round1_falsifier_prompt_v2.txt` (sha256 `13734bf4725d099d2bb73e1bb76ac3b97646834bd10f76000a2d65845eb4ab81`). The seal list records the v1 bytes.

Round 1 also has `ADDENDUM_2026-11-09_clean_v0.4.md`, which the conductor explicitly says is **not part of the seal** and is not scored. It is filed next to the seals for context.

## Counts

- Sealed findings files revealed: 5 (plus the Round 1 v1 prompt that was hashed with seal 1).
- Cryptographic salt strings found for rounds 1–4: 0.
- Commitments verified: 6 of 6 listed hashes.
- Other secrets (passwords, private keys, API tokens, usernames/credentials): none withheld. A full recursive scan of the work tree, including nested zips, found no high-confidence credential patterns. Keyword hits for "salt", "secret", and "token" were ordinary prose (secret-scan notes, "support token" in a finding, "blind-round salts" as a metaphor).

## If a later salt surfaces

If Rusty or the conductor still holds a salt string that is not in these files, it can be added here and checked as `SHA-256(salt ‖ payload)` against a committed hash. Nothing in the received archives supplied such a string.
