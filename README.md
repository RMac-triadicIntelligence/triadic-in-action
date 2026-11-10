# Triadic in action

The documentary record of a four-round, two-seat review of *From Reykjavik to Relational Grace* (v0.4 through v0.7). Rusty Williams McMurray closed rounds 1 through 4 on 2026-11-10 and asked that the previously sealed material be packaged, with salts revealed and labeled.

This is the public documentary record. The companion repository of papers, keel grace definitions, and executable toys is https://github.com/RMac-triadicIntelligence/triadic-in-action-builds.

## The method, in brief

Five seats, one version at a time:

1. The **keel** (Rusty) rules on grace, from the four Gospels only, and has the last word.
2. The **conductor** (Claude) writes down findings and hashes that file *before* anyone else sees the new version.
3. The **designer** (ChatGPT) revises the specification, starting each round in a fresh thread.
4. **Falsifier A** (Grok Expert, the blind seat) attacks the text in front of it, tagging findings DOC.
5. **Falsifier B** (Grok bot, the history seat) attacks the same text, and may tag PRIOR when a finding depends on earlier work.

A finding is **CLOSED** only when its finder and a second seat agree. Findings are tagged **DOC** or **PRIOR**. The sealed lists are now open; see `SALTS_REVEALED.md` and `METHOD.md`. The closure map is `CLOSURE_LEDGER.md`.

Rounds 1–4 are closed as rounds. Not every finding is CLOSED. Round 4's new findings still need a second-seat check, which was reserved for still-open Round 5 and is not in this repository.

## Layout

```
METHOD.md                    How the triad works
SALTS_REVEALED.md            What was committed before each round, now opened and verified
CLOSURE_LEDGER.md            Two-seat status, plus seal-vs-seat calibration
PROVENANCE.md                Every staged file → sha256 and when it was received
received/                    Original unique packets and archives (Round 5-free)
rounds/round1..round4/
  prompts/                   The packets each seat was sent
  designer/                  Designer-facing material (Round 1 also has the facet package)
  falsifier_a/               Grok Expert reports
  falsifier_b/               Grok bot reports (and the Round 4 Task 1b addendum)
  handoffs/                  Conductor-filed copies of the same packets
  conductor/                 Logs, scores, sealed findings (now open), source texts, manifests
grace_readings/              The shared prompt, plus the bot and Expert readings
conductor/                   Our digest of a later Claude share (raw chat text is not included)
```

Paper PDFs were not supplied for v0.5–v0.7. Authoritative plain-text versions are in the conductor `source/` folders here and, more accessibly, in https://github.com/RMac-triadicIntelligence/triadic-in-action-builds/tree/main/papers/.

## What is not here

- **Round 5 / v0.8.** Still open. Handoffs, the conductor handover (it briefs v0.8), and the original zips that mix Round 5 files with earlier material are staged separately under `hold-round5/` and are not for upload.
- **Name Badge Networking.** Out of scope.
- **The raw Claude share chat.** Excluded; `conductor/CLAUDE_SHARE_19fca05d_DIGEST.md` is the history-seat digest.
- **Already-public work**, linked rather than copied:
  - https://github.com/RMac-triadicIntelligence/commons-dwelling-grace
  - https://github.com/RMac-triadicIntelligence/relational-transitions-v0.1
  - https://github.com/RMac-triadicIntelligence/lab-notebook

## Missing

- ChatGPT's grace reading (the same prompt was sent to three readers; only the bot and Expert readings are on disk).
- No separate cryptographic salt strings. Commitments were SHA-256 of the sealed files. All six listed hashes verify. Details in `SALTS_REVEALED.md`.

## Dates

Work dates are 2026-11-09, America/Chicago, with a few packets re-sent on 2026-11-10 (2:07 PM and 2:16 PM CT) that match the 2026-11-09 8:01 PM CT archive by hash. Commit dates, if this is later published, will be the publish date. Nothing here is backdated.

## Related repositories

- This repo: https://github.com/RMac-triadicIntelligence/triadic-in-action
- Builds, papers, and toys: https://github.com/RMac-triadicIntelligence/triadic-in-action-builds
- Commons and dwelling grace (already public): https://github.com/RMac-triadicIntelligence/commons-dwelling-grace
- Relational Transitions v0.1 (already public): https://github.com/RMac-triadicIntelligence/relational-transitions-v0.1
- Lab notebook (already public): https://github.com/RMac-triadicIntelligence/lab-notebook

## License

Apache License 2.0. See `LICENSE` and `NOTICE`.
