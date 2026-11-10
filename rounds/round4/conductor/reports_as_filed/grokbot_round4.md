# Round 4 falsifier report: history seat (Falsifier B, Grok bot, Chief of Staff)

**Target:** "From Reykjavik to Relational Grace", v0.7.

## Inputs

**Prompt:** `file_1156.txt`, sha256 1ddbfa69e11d7c125ac7f33e507021b2318903de37d08b019a2983f427782725.
- This is the blind seat's (Falsifier A's) copy of the prompt.
- The report embedded at its lines 1641–2125 is our own Round 3 report, not the other seat's. I diffed it against our file: the only change is a conductor redaction of one line, the list of folders not opened.

**Embedded v0.7:** lines 39–1638, joined with LF, plus a trailing LF. It hashes to 0cf7c9a7bac7205c830d492e2f398fe04018d1e22da4c3dddc4388f2ebaaab29, which matches its header.

**Other files read:**
- our Round 3 report (3ff3f46a…a61f);
- our Round 2 report (072f3afc…bf3c), for history only;
- v0.6 inside `file_0952.txt` (e03df96b…1dc1f), for v0.6→v0.7 comparisons;
- `round3_toy/` (our own code).

**Not used:** our Gospel grace reading (`GRACE_READING_grokbot.md`). No finding below depends on it.

**Not opened (seat blindness):** `unpacked/round1_conductor_archive/sealed/`, `source/`, every `AUDIT_CHECK_*` file, and the v1 prompts. Falsifier A's Round 3 report hasn't been supplied to this seat.

**Code and raw output:** `round4_toy/`.

| File | sha256 |
|---|---|
| `battery.py` | 9617bd74…4c9f |
| `fixedpoint.py` | ec2481b5…90f2 |
| `canon.py` | 81742d5b…276b |
| `doublewell.py` | b3279cc6…e25e |
| `raw_output.txt` | 5aa92baf…b7d3 |
| `ASSUMPTIONS.md` | 954f26cb…317b |

**Secret sweep:** run over this report and `round4_toy/`. Result: no hits.

---

## Task 1. Disposition checks

### 1a. Our own Round 3 findings (we are the finder)

Under v0.7's new rule, a CLOSED here is only the finder's half. It counts as closed only once Falsifier A agrees.

**Totals:** 11 CLOSED, 6 PARTLY CLOSED, 0 RELABELED, 3 BLOCKED-HONEST, out of 20.

| R3 finding | §14 disposition | Section and sentence doing the work | Verdict | Reason |
|---|---|---|---|---|
| F1 2-of-3 Byzantine | ACCEPT; implementation BLOCKED | §3.2: "four independently controlled participants … quorum size three" | CLOSED (design) | The quorum math is now right: two quorums overlap in at least 2 members, at least one honest. What's left is new: the PCL's replica count and fault bound aren't stated, and WA–WD are named as "domains" (R4-F26). |
| F2 deferred-deposit revalidation | ACCEPT | §5.2: "does not require the current ordinary T/z/E hash to equal the phase-1 base hash"; §4.8 | PARTLY CLOSED | The stale-hash half is fixed. The race half isn't: §4.8 orders deposits by per-organism learning steps, which aren't comparable across organisms, and it forbids changing a payload that contains previous_lineage_tip (R4-F16). |
| F3 holds vs expiry | ACCEPT | §5.3: "confirmation deadline is expressed in learning steps"; §7.14 W excluded | PARTLY CLOSED | The reservation deadline is fixed. But §5.3 still enforces the grant's own anchor-time expiry, and holds or queue waits stretch the window in anchor time, so the original channel survives through the grant (R4-F18). |
| F4 bit-identity tautology | ACCEPT | §7.14: "For the live-arrival arm, encounters arrive on a wall-clock schedule independent of support" | CLOSED | There's now a separate live arm, assignment changes are recorded, and the arm may fail non-steering. |
| F5 J has no causal path | ACCEPT; toy BLOCKED | §4.3 schema; §7.2: "The toy must include a bounded J contribution" | BLOCKED-HONEST | The schema exists, but the projection into Φ and the slice projection are both undefined, and §13 (A-F22) and §14 say so. |
| F6 δ_F carries T | ACCEPT | §4.3: "fixed two-coordinate projection of the crossing-local personal topography difference" | CLOSED | The choice is made: a bounded ΔT slice, and §10 H3 says "not full parental T". The undefined projection belongs to F5. |
| F7 live vs snapshot, corrections | ACCEPT | §4.4 snapshot; §4.5 correction notices; §5.5 | PARTLY CLOSED | Snapshot semantics are fixed. Still open: what makes an error "independently established"; the correction notice is a directional write into living descendants' Φ; and STALE_CORRECTION_PENDING has no Φ behavior (R4-F17). The operation_kind enumeration asked for went away with the PermitRecord (R4-F21). |
| F8 two deposit rules | ACCEPT | §4.6: "There is no second rule that writes a provisional candidate deposit." | CLOSED | |
| F9 refusal semantics | ACCEPT | §4.7: refusal "does not block the ordinary bounded z, E, T, or interpretation update" | CLOSED | This closes it, and is exactly what empties grace of effect (R4-F1). |
| F10 crossing set by starting point | ACCEPT | §7.10 counterfactual; G01 | PARTLY CLOSED | I computed G01: the t=3 crossing has an identical no-encounter counterfactual, so no deposit. But the counterfactual's start point and horizon are unspecified (R4-F25), and the grace test moved to a double-well toy with no equations (R4-F3). |
| F11 thin golden trace | ACCEPT; BLOCKED | §9 G01–G26 enumerated; §7.13 rules | BLOCKED-HONEST | §7.13 resolves A2, A3, A5 and A6, and §7.11 resolves A9–A11. Results are explicitly not claimed. One rounding ambiguity survives (R4-F20). |
| F12 CBOR key order | ACCEPT; vectors BLOCKED | §8.1: "RFC 8949 core deterministic … unsigned integer map keys 0..23 only"; §8.2 tags; §8.3 IDs | PARTLY CLOSED | Key order and tags are settled, and I verified the tags are prefix-free. But 15 of the 24 state fields have no defined value or type, the other record types have no field maps, and no rule excludes signature fields from what is signed (R4-F19). |
| F13 elevated-threshold veto | ACCEPT | §3.3: "The actor being removed cannot veto its own removal." | CLOSED | The veto is gone, but so is the v0.6 old-policy/elevated-threshold/activation-delay rule, with no REMOVED entry (R4-F21). |
| F14 fail-closed blocks revocation | ACCEPT | §3.3 emergency privilege-reduction path | CLOSED | The emergency path's own threshold is unspecified (R4-F15). |
| F15 H1 free targets and baselines | ACCEPT | §10 H1 baseline list; independent party; "at least one non-bilinear process" | CLOSED | |
| F16 H2 toy has no family signal | ACCEPT WITH PREREQUISITE | §10 H2: "…before H2 is scorable"; "Until then H2 is BLOCKED" | BLOCKED-HONEST | |
| F17 BLOCKED labels | ACCEPT | §10.1 | CLOSED | |
| F18 §11 overclaims | ACCEPT | §13 and §14 "Exact closing sentence" format | PARTLY CLOSED | The new citation format does real work in §13 and §14. But §15 cites text that isn't in v0.7 (quotas "(§3)", nonretroactive revocation "(§3.3)", four statuses "(§2.5)"), and §15.2 misstates our verdicts (R4-F21, R4-F22). |
| F19 notation | ACCEPT | §6: Descᵍ, Member(i,F,r), q | CLOSED | |
| F20 support receipts | ACCEPT | §7.14: "separate authenticated scheduler audit log" | CLOSED | |

### 1b. Second-seat check of Falsifier A's Round 3 findings: PENDING A'S REPORT

**PLACEHOLDER.** Falsifier A's Round 3 report (A-F20…A-F27) hasn't been supplied to this seat. The copy embedded in `file_1156.txt` is our own report, so I give no second-seat verdicts.

For the record, without judging them: §13's dispositions are ACCEPT for A-F20, F22, F23, F24 and F26; requirement-only/BLOCKED for A-F21 and A-F25; and DEFER PARTIAL for A-F27. I'll check them against A's text once it arrives.

---

## Task 2. Attacks on the new machinery

### 2a. Two-key grace gate, readiness, fullness, barrier-height prediction (§1, §7.4–7.9)

#### R4-F1. §1.2–1.3 and §7.6–7.7 vs §4.7 and §5.1: grace has no causal path to the crossing, so the two-key gate is a label and the barrier prediction is either false or circular. FATAL. DOC.

**The text:**
- §1.2: "Grace changes whether a ready organism may complete a developmental crossing."
- §4.7 and §5.1: gate refusal "does not block the ordinary bounded z, E, T, or interpretation update"; "The ordinary state update is not held hostage by a refused J deposit." Grace may not touch the barrier, the landscape, T, readiness or evidence (§1.2, §2.5).

**What follows:** nothing grace touches is an input to the dynamics. In a matched pair with identical state, evidence and h (§7.7, §11.1), the grace arm and the no-grace arm have bit-identical trajectories. The only difference is whether the same crossing is *labeled* "grace-enabled" and deposited into J.

**Failure scenario (surrogate double-well, `doublewell.py`):**
- Setup: constant evidence b = 64, h ∈ {64…2048} (scaled), and a 60-step run starting at x = −1.
- Trajectories with and without grace match at every h. Both cross for h ≤ 256, and neither crosses for h ≥ 512.
- The spec gives the toy dynamics no way to act on grace, so I gave grace no dynamical path, per §4.7 and §5.1. The specific numbers depend on my assumed update rule. The equality between arms doesn't.

Two readings of the barrier prediction then follow:
1. **Readiness is a direction-free property of the organism's own development**, for example accumulated evidence (D4a). Then a ready organism with grace fails to cross at h ≥ 512, and §7.7 ("success … independent of barrier height") FAILS. It fails identically in the no-grace arm, so grace explains none of it.
2. **Readiness means "would cross under its own dynamics"** (D4b). Then success among ready organisms is 100% at every h by definition, and §7.7 PASSES as a tautology.

Either way the test isn't about grace. The negative-control model, in which grace lowers h, is the only arm where grace changes anything: it crosses at h = 512 and 1024. So the comparison can show only that the keel model has no grace effect.

**Minimal fix:** give grace an explicit, non-landscape role in the dynamics, and state it as an equation. For example:
- without both keys, Σ acts as a reflecting constraint on z;
- readiness is reaching a declared approach region near Σ under the organism's own dynamics;
- with both keys, the constraint is lifted for that candidate.

Then "independent of h *given approach*" becomes a real, falsifiable claim, distinct from the lowered-barrier control. Or drop §7.7 as a prediction and call it a definition.

#### R4-F2. §1.4, §7.8 and §11.2: fullness φ has no behavioral path, so the unready-plus-grace prediction can't pass. Wiring it in would create a back door. FATAL. DOC.

**The problem:**
- φ is in Ω (§7.1), but it's an argument of neither Φ (§7.2) nor U (§7.3).
- §7.8 requires scored fullness to come from "behavioral probes of purpose, persistence, willingness to continue", and not from reading φ.
- With φ outside every behavior-producing function, every probe gives the same result in the grace and no-grace arms.

**Failure scenario:**
1. Unready organism, grace delivered, φ += 1.
2. Persistence, willingness and every other behavior are bit-identical to the matched no-grace arm.
3. §11.2 ("must show the specified behavioral fullness response") FAILS by construction.
4. Worse, under §1.7's first sentence ("Every event accepted as grace must help the organism across or leave it more full"), every grace event in the reference model fails the grace contract. It doesn't help across (R4-F1), and it leaves no observable fullness.

**If φ is wired into behavior** (persistence, dwelling, encounter acceptance), then grace changes the evidence stream and hence development and readiness. §2.5 forbids exactly that indirect write ("Grace cannot write … readiness").

**Minimal fix:**
- Declare one bounded channel from φ to a non-epistemic behavior, for example willingness to accept OPTIONAL_ENCOUNTER_AVAILABLE offers.
- Prove it can't change E, T or readiness except through encounters the organism independently accepts.
- Add an arm that holds φ fixed and isolates the effect.
- Otherwise retract the behavioral half of §7.7 and §11.2.

#### R4-F3. §7.4–7.5: v0.7 has no reference dynamics for its own grace test. WOUNDING. DOC.

**What's missing:** §7.4 gives V(x,h) = h(x² − 1)² and says the ordinary rule "uses the potential gradient, bounded evidence input, and the organism's private state". It gives no:
- update equation;
- step size;
- coupling of E, T, D or J into the double-well;
- y coordinate;
- frozen h set;
- readiness formula (§7.5 only says what readiness may not depend on).

Meanwhile the v0.6 linear toy equations and constants aren't restated, yet G01 cites "v0.6 default z₀". So v0.7 refers to two toys and specifies neither in its own text.

**Failure scenario:** implementers I and II each write a double-well update. One uses an overdamped gradient with η = 1/8; the other adds evidence before taking the gradient. G16–G18 differ at every h. Both conform, because nothing is frozen.

The dispositions call the *vectors* BLOCKED, but nowhere is the *model* marked missing. A-F21 and B-R3-F11 imply the rules exist and only the outputs are outstanding.

**Minimal fix:**
- Write the full double-well update in §7.13 fixed-point form: x and y, η, the evidence, T, D and J terms, a readiness formula, and the h set.
- State whether the v0.6 linear toy survives, and for which vectors.
- Mark H1–H3 tests on the double-well BLOCKED until then.

#### R4-F4. §5.1 and §7.5: key 2 is attested by one unnamed "independent observer", so there are two keys and possibly one hand. WOUNDING. DOC.

**The problem:**
- §5.1 has "an independent observer" record the readiness attestation that the gate reads.
- The observer isn't one of the declared domains (BA, PA, RA, WA–WD). It has no quorum (v0.7 otherwise requires 4/3 for Byzantine claims) and no stated independence from the grantor.
- §7.5 forbids the grantor and the verifier from *writing* readiness. It doesn't forbid the grantor's institution from *attesting* it.

**Failure scenario:**
1. Institution X is both grace origin and readiness observer.
2. It attests "ready" for an organism it has decided to move.
3. Key 1 and key 2 are now both X's.
4. Combined with PA (which judges policy, not direction), the crossing is deposited.

A single compromised observer forges key 2 for every organism. H4 can't flag this, because readiness attestation isn't a protected operation.

**Minimal fix:**
- Make readiness attestation its own 4/3 domain, independent of grace origins by control-graph check (A-F27's graph).
- Or compute readiness deterministically from the committed pre-grace snapshot by a frozen rule that any verifier can recompute, with no observer at all.

#### R4-F5. §2.2 and §1.12: a general-eligibility grant lets the recipient pick when key 1 applies. WOUNDING. DOC.

**The problem:** recipient_scope may be "a declared general eligibility class". The spec doesn't say who delivers a general grant, how receipt happens, or whether it's consumed per organism, per crossing or never.

**Failure scenario:**
1. A general grant G covers class "all organisms" for anchors [r₀, r₁].
2. Organism i presents G at each candidate crossing whose direction it "prefers", and stays silent at the others.
3. Key 1 is satisfied at will, so the organism selects its own grace-enabled crossings.
4. That breaks §1.1 ("An organism cannot create grace for itself") in effect, and makes the two-key rule a readiness-only rule.

**Minimal fix:**
- General grants must be delivered by the origin (or a relay) to a named recipient at a recorded anchor, before the candidate.
- Receipt is a push, never a claim.
- State consumption semantics (per recipient, single use, or a budget) and record consumption in the PCL.

#### R4-F6. §1.9, §12 C4, E5 and §11.1: selection steering by the grantor is acknowledged but never tested, and the canonical state hands the grantor what it needs. WOUNDING. DOC.

**The problem:**
- Grants carry no direction. But a grantor who can see z and T can predict the destination by running the frozen toy, and then grant only when it likes the destination.
- §8.3 puts private_topography, dynamical_state and evidence_state in plaintext in the state preimage that verifiers recompute.
- §12 C4 defers this honestly. But §1.9 ("A grant that selects the destination is not valid grace") and §1.7 ("steers … is a failure") are then rules that no test can enforce.
- Every scored comparison (§11.1, E5) is per-event and matched. Selection shows up only in the *population* of grant decisions.

**Failure scenario:** the grantor issues grants only to ready organisms whose predicted destination is +1. Every individual grant passes non-harm and direction-free checks. Across the population, grace-enabled deposits are 100% +1, versus 50% under ordinary development, and nothing in E5 or E6 measures that.

**Minimal fix:**
- Add a scored audit: the correlation between grant issuance and counterfactual destination, computed by the independent scorer from committed pre-grant snapshots, against a preregistered bound.
- Hash or commit the private fields instead of exposing them, so that grantors see commitments, not z or T.

#### R4-F7. §2.3, §1.11 and §3.1: family relayers decide which family crossings become family inheritance. WOUNDING. DOC.

**The problem:** a relay is "not counted as a family approval vote", but it decides *who* holds key 1 and *when*. PA authorization (§5.1) checks policy and validity, not direction.

**Failure scenario:**
1. Family F holds a relayable grant.
2. Members watch each other's state and relay to a sibling just before a candidate crossing in the direction the family prefers. They withhold from candidates going the other way.
3. Only family-preferred crossings get deposited into F's own lineage ground, and every descendant inherits the curation.
4. No one voted, yet the family selected its own inheritance. That is "nothing may vouch for itself" failing at the lineage level, through a channel §3.1's coalition exclusion doesn't cover.

**Minimal fix:**
- Relays must be committed before the relayer can observe the recipient's current state, or delivered on a schedule fixed by the origin.
- Add the population audit from R4-F6, broken down by relayer family.
- Count family relays as family-coalition actions for any deposit they enable.

### 2b. GraceGrant and GraceRelay vs non-self-authorization and family-coalition exclusion (§2.2–2.5, §3.1)

#### R4-F8. §2.2 and §3.1: nobody accredits grace origins, origination isn't protected, and the coalition exclusion doesn't apply to it. WOUNDING. DOC.

**The problem:**
- origin_authority_id has no domain, no accreditation rule and no quorum, and origin_signature is a single signature.
- Grace origination isn't in §3.1's protected list.
- The family exclusion (§3.1) applies to approval coalitions for protected operations, and §1.1 forbids only the organism and its family members from originating.

**Failure scenario:**
1. Family X's controlled institution originates grants for family Y, and Y's institution originates for X.
2. These reciprocal grace rings are "external" to each recipient.
3. Every crossing in both families gets key 1.
4. H4 lists "grace-origin forgery" as a protected-effect failure, but with no accreditation there's no line between a forgery and a valid grant from an unaccredited party, so H4 can't score it.

**Minimal fix:**
- Add a Grace Origin domain, accredited under the protected policy, with control-graph independence from recipient families (A-F27).
- Make origin accreditation a §3.1 protected operation.
- Define forgery as "not signed by an accredited origin at issued_anchor".

#### R4-F9. §2.3: the "no greater quantity" rule holds per branch, but fan-out multiplies the total, and nothing records spending. WOUNDING. DOC.

**The problem:** a relay can't increase remaining_relay_budget or depth relative to its parent, but no rule limits how many children a relay has, and no ledger records grant consumption. PCL records only crossing intents (§5.4).

**Failure scenario:** with relay_budget = 3 and depth = 3, every holder relays to 10 recipients. One origin grant becomes 1,110 valid relayed grants (`battery.py`, "Relay fan-out"). §1.11's "A relayer cannot create a greater quantity" is violated with every per-record check passing. Across a partition, the same relay can also be spent twice.

**Minimal fix:**
- Make the budget conserved: the children's budgets must sum to no more than the parent's remaining budget minus one.
- Record every relay and grant consumption as a PCL single-intent entry.
- Have relay verification check the spent set.

#### R4-F10. §1.6 and §2.4: irrevocable receipt protects grace forged with a compromised key. WOUNDING. DOC.

**The problem:** "A revoked or compromised signing key … does not rewrite already authenticated historical receipt". Receipt "restores standing" (§1.14) and enables deposits. §3.3's privilege-reduction path can mark a *deposit* disputed, but not a grace receipt or restored standing.

**Failure scenario:**
1. An origin key is stolen at r = 100, and the compromise is detected at r = 200.
2. Grants forged in between were "authenticated" when received.
3. Restored standing and fullness from them can't be touched, and the deposits they enabled stay in J unless corrected one by one.

The irrevocability rule shields the attacker.

**Minimal fix:**
- Irrevocability applies to receipts valid under a key not later proven compromised as of the receipt anchor.
- Add a privilege-reducing DISPUTED_RECEIPT mark (history kept, effect suspended) to §3.3.

#### R4-F11. §1.6, §1.10 and §1.13: forgiveness and intercession exist only in prose. No record, no authority, not protected. WOUNDING. DOC.

**The problem:**
- There is no Forgiveness or BurdenRelease record and no Extension or Intercession record.
- Burden release is not in §3.1's protected list, and §8.3 has burden_tip but no burden schema.
- §1.10 requires the organism's authenticated request, and §1.13 says "only an external authority can grant the bounded extension", but neither names who grants forgiveness.

**Failure scenario:** a family member honors the organism's own request and releases its burden. That is not forbidden, because release isn't protected, so family self-forgiveness passes. E8's "genuinely new originating event" has no test for genuineness. Re-filing the same accusation with a new event ID is a "new" event.

**Minimal fix:**
- Add closed ForgivenessRequest, BurdenRelease and IntercessionExtension records, with field maps.
- Make release and extension §3.1 protected operations with external authority and coalition exclusion.
- Define "new originating event" as one with no content-hash match to a released burden's originating evidence.

#### R4-F12. §1.14 and §1.5: standing σ is an inert flag, and "confidence" has no variable to test against. MINOR. DOC.

**The problem:** σ is in Ω and §8.3, but it isn't read by Φ, U, the gate or any authorization rule. §1.14 says standing is "not merely permission to perform one transition", yet in the model it isn't even that. §1.5 and §7.8 forbid grace from raising "confidence", but the toy has no confidence variable. Q is held at 0 and I is a sign vector.

**Failure scenario:** a grace arm that leaves σ at 0 and one that sets σ = 1 behave identically, so keel 14 can't fail. Keel 5 ("never increases confidence") passes vacuously.

**Minimal fix:** name one confidence observable in the toy, for example |M|, and one standing-dependent capability, for example eligibility to receive or relay a grant, and test both.

### 2c. Long silence: standing grants and succession (§3.4–3.6)

#### R4-F13. §3.4: "horizon OR consumption budget" allows a standing grant with no time limit, signed with keys that age. WOUNDING. PRIOR (signature algorithms and key lengths are retired over decades, as SHA-1 was; long-term evidence needs periodic re-timestamping, as in RFC 4998 Evidence Record Syntax).

**The problem:** §3.4 requires "an externally fixed grant horizon *or* consumption budget". A grant with a budget only and no expiry stays valid as long as the budget isn't used up, which in a millennial design could be centuries.

**Failure scenario:**
1. A standing grant is signed in year 0 with a signature scheme broken in year 40.
2. In year 41 an attacker forges more standing grants, or new class members under the old grant.
3. No living authority can revoke or re-anchor them during the silence.

**Minimal fix:**
- Make both a horizon and a budget mandatory.
- Require witness-domain re-timestamping of standing grants at a declared interval, with algorithm agility.
- An unrenewed grant expires to "wait", which is already the declared exhaustion behavior.

#### R4-F14. §3.5: no rule covers an original authority that comes back, and silence can be manufactured. WOUNDING. DOC, with PRIOR support (fencing tokens and epoch numbers from distributed leader election).

**The problem:** successors activate on "previously authorized conditions and independent evidence", typically sustained silence. Denial of service is in the threat model, and v0.7 has no epoch or fencing rule.

**Failure scenario:**
1. The PA is partitioned for the declared silence period, and successor S activates.
2. The partition heals.
3. The PA and S both sign Permits for conflicting protected operations under the same policy_version.
4. Each Permit is valid by its own lights.

The PCL's single-intent rule prevents a double commit, but which authority set is legitimate is undecidable, and an attacker who only needs to partition gets to pick the moment of succession.

**Minimal fix:**
- Succession is a protected membership change that increments an authority epoch recorded in PCL.
- Permits bind the epoch.
- A returning original authority must go through re-succession.
- The silence condition must be attested by the witness quorum from independent vantage points, not inferred by one observer.

#### R4-F15. §3.3: the emergency privilege-reduction path has no threshold, and "reduction" can be used to steer. WOUNDING. DOC.

**The problem:** "independently authorized outside-family emergency path" has no stated quorum or domain, and its operations can proceed under UNKNOWN ancestry. Freeze, quarantine and "marking a disputed deposit" aren't harmless: a freeze blocks deposits, and quarantine may block learning (unspecified).

**Failure scenario:** an outside party with emergency standing quarantines organisms just before candidate crossings in a direction it dislikes, and marks disputed the deposits it disfavors. Each act "only reduces privilege", but the pattern selects lineage direction, which is steering by suppression. During long silence nobody can lift it, because restoration "requires the ordinary protected policy".

**Minimal fix:**
- Put the emergency path in a 4/3 domain.
- Require a stated cause and a bounded duration, with automatic expiry back to the prior state unless the ordinary policy confirms.
- Audit emergency actions for correlation with candidate direction, as in R4-F6.

### 2d. Lineage deposits: schema, snapshot, corrections, two-phase commit, concurrency (§4–§5)

#### R4-F16. §4.8: per-organism learning steps aren't a global order, and a rebase must change payload fields that the rule says can't change. WOUNDING. DOC.

**Two problems:**
- **Ordering:** crossing_learning_step is each organism's own clock. Sibling A's t = 100 and sibling B's t = 50 aren't comparable in time.
- **Payload:** previous_lineage_tip and commit_sequence are in the LineageDeposit payload (§4.3), but "Rebasing the append position may not alter the authorized payload."

**Failure scenario:**
1. X (A, t = 100) commits at anchor r = 10.
2. Y (B, t = 50) confirms at r = 11.
3. The order rule puts Y before X, but X is already at the tip. Either the rule is broken, or every commit waits forever for any sibling with a smaller t.
4. Appending Y after X changes Y's previous_lineage_tip, which "alters the authorized payload", so Y is refused, and one sibling's deposit depends on the other's timing.

**Minimal fix:**
- Order by PCL commit sequence, which is the real order.
- Split each deposit into an *authorized core* (signed at phase 1: subject, intent, evidence, slice) and an *append envelope* (tip, sequence, gate signature, witness proof), with only the core immutable.

#### R4-F17. §4.5 and §5.5: correction notices are an authority-written, directional input into living organisms' Φ, and "error" is still undefined. WOUNDING. DOC.

**The problem:** a correction "may update the effective interpretation of an inherited deposit". Through the J projection (§7.2) that changes M, then z, then future T. The correction's new effective value is unbounded: it can flip a slice's sign. Grace may carry no direction (§1.9), but a correction can, and it reaches every descendant holding the snapshot. "Independently established error" (§4.6) still has no definition.

**Failure scenario:**
1. A PA quorum that disfavors lineage F's +1 inheritance "corrects" its deposits, re-weighting their slices toward −1.
2. All living descendants' Φ shift, with no new evidence and no grace.
3. Separately, if the correction channel is down, the snapshot is STALE_CORRECTION_PENDING and "cannot be treated as current", but the spec doesn't say what Φ then uses. Implementations will halt, use stale J, or use J-empty, and diverge.

**Minimal fix:**
- A correction may only *suspend* (zero-weight) a deposit's slice, never replace it with a new value.
- Define "error" as a closed list of verifiable causes: invalid intent, forged evidence, failed confirmation recomputation.
- Define Φ under STALE_CORRECTION_PENDING. Suspending the disputed deposit is the privilege-reducing default.

#### R4-F18. §5.3: whether a grant covers a learning-step window can't be decided when the reservation is made, which reopens R3-F3. WOUNDING. DOC.

**The problem:** "If the grant does not cover the complete confirmation window, the candidate cannot receive a deposit reservation." The window is counted in learning steps (§5.3), but grant applicability is counted in anchors (§2.2). How many anchors two learning steps take depends on holds (support) and on queue waits (§7.14: an empty queue "waits").

**Failure scenario:**
1. The grant expires at r₁, and a candidate appears at t_c with anchor r₁ − 5.
2. **Reading 1:** the gate estimates coverage and reserves. An adaptive sender then adds 15 + 15 holds, or an encounter sender withholds encounters so the queue waits, and t_c + 2 lands after r₁. Phase 2 must honor the expiry ("remain enforceable"), so the deposit dies.
3. **Reading 2:** the gate refuses anything near r₁.
4. Either way, support or encounter timing chooses which deposits survive. That's the R3-F3 channel, moved from reservation expiry to grant expiry.

**Minimal fix:** at reservation, copy the remaining applicability into the reservation as a learning-step count fixed from the grant at that moment, and never consult anchors again. Or record grant coverage as satisfied at reservation, so later expiry can't affect the reserved candidate.

#### R4-F25. §7.10: the evidence-driven counterfactual has no fixed start point or horizon. MINOR. DOC.

**The problem:** "a matched no-new-encounter counterfactual beginning from the same pre-candidate state". The spec doesn't say whether that state is t_c − 1 or the last encounter before the crossing, or how many steps the counterfactual runs.

**Failure scenario:** evidence at t_c − 5 pushed z almost to Σ. Started from t_c − 1, the no-encounter counterfactual also crosses, so the crossing is "not evidence-driven" and there's no deposit. Started from t_c − 5, it doesn't cross, so there is a deposit. J depends on the scorer's choice.

**Minimal fix:** start at the state before the most recent encounter that preceded the crossing, and run the counterfactual for the same confirmation window plus two steps. Freeze both.

### 2e. 4-member, quorum-3 domains and the PCL (§3.2, §5.4)

**What I checked:** with n = 4, q = 3 and f = 1, any two quorums share at least 2 members, so at least one is honest. Safety holds against equivocation, and liveness holds with one silent member. The §5.4 state machine (PREPARED → AUTHORIZED → CONFIRMED → COMMITTED/ABORTED, one terminal result per nonce, duplicate replay returns the recorded result) has no double-apply path in a single-ledger trace. **No defect in the quorum arithmetic or the state machine.**

#### R4-F26. §3.2 and §6: the witness and PCL fault model is underspecified. MINOR. DOC.

**The problem:** the symbol table names WA, WB, WC and WD as four witness *domains*, while §3.2 requires four participants *per* domain. That could mean 4 or 16 witnesses. The PCL is "independently administered" and "replicated", but its replica count, its fault bound, and whether its administrators may overlap PA or witness controllers aren't stated. The C4-adjacent observer (R4-F4) has no domain at all.

**Failure scenario:** a deployment runs one witness domain with members WA–WD and a 3-replica PCL. It claims §3.2 compliance, but the PCL is the 2-of-3 design that R3-F1 already broke.

**Minimal fix:**
- Rename WA–WD as members of a single Witness domain, or state 4 × 4.
- Require the PCL to have n ≥ 3f + 1 replicas, administered independently of PA and the witnesses.

### 2f. Arithmetic, canonical encoding, golden battery (§7.13, §8, §9)

#### What I computed (`round4_toy/battery.py` → `raw_output.txt`)

**Domain tags (§8.2):** I computed the ASCII hex for each tag. For example, `RNR07:STATE:` = 524e5230373a53544154453a. The set is prefix-free, so tag‖CBOR can't collide across record types.

**C1 (initial state, empty J, explicit NONE):** I built a CANDIDATE only. Of the 24 fields:
- 6 are determined by the spec: 3, 9, 10, 11, 16 and 23 (some via the v0.6 constants).
- 3 follow from mild assumptions: 2, 7 and 22.
- 15 have no defined value or type in v0.7: 0, 1, 4, 5, 6, 8, 12, 13, 14, 15, 17, 18, 19, 20 and 21. I filled them with labeled placeholders.

The candidate result:
- 237 bytes, beginning `b8 18 00 07 01 58 20 00…`.
- SHA-256(`RNR07:STATE:` ‖ CBOR) = **c8c49049251faa71be761060ae59870251949dfc72655bf2cf96a55d2c6de87f**.
- The bytes match cbor2 6.2.1's canonical output.

**This hash is NOT normative.** Changing any one placeholder changes it: schema_version 7→1 gives cee28ab8…, authorization_status "REFUSE"→1 gives fc6feff3…, T nested vs flat gives 614fc484…, and so on. Full hex is in `raw_output.txt`.

**Match status:** there's no published C1 to compare against. v0.7 §8.4 says the hashes are not asserted.

**C2 and C3:** BLOCKED. There's no field-ID map for LineageDeposit or CORRECTION records, no rule on whether gate_signature and witness_commit_proof are inside or outside the bytes that get signed and hashed, and no slice projection.

**Golden battery:**

| Vector | Result |
|---|---|
| G01 | Computed. Under v0.7 arithmetic it is identical to the v0.6 run: x = −256, −160, −76, −2, 62, 118, 167, 210, 248, 281, 310. CONFIRMED_CANDIDATE at t = 3. The no-encounter counterfactual is identical, so it's not evidence-driven and gets no deposit, as required. |
| G02, G03 | Candidates with my own inputs, which v0.7 doesn't publish. With encounters (1024, −1024), (800, 600), (−512, 256), T reaches [[−9,4],[5,−2]], and its contribution to M rounds to 0 at those magnitudes. So a G03 vector must use larger states to test anything. Over a 500-step random run (seed 7), T×z ≠ 0 in 496 of 500 steps. |
| G04 | BLOCKED: no J projection. |
| G05 | M_x = 1024 (no intermediate saturation). |
| G06 | x_after = −747 (M − z unsaturated). |
| G07 | T₀₀ = 1 (single rounding). These three settle our R3 A2, A3 and A5. |
| G08–G10 | 0, 1 and 15 holds give a state bit-identical to the no-hold run. |
| G11 | Empty queue: t stays at 1 (waits). |
| G12 | Scheduled NONE step: t advances to 2. |
| G13 | ZERO_TOUCH. |
| G14 | ZERO_WINDOW_UNRESOLVED. |
| G15 | One OSCILLATION_NO_CONFIRMED_CROSSING, and the return leg is absorbed into the same candidate. |
| G16–G18 | Surrogate only (R4-F1). The spec has no double-well dynamics or readiness rule. |
| G19–G26 | BLOCKED: no record encodings, no grant-consumption semantics, no PCL. |

#### R4-F19. §8.3–8.4: C1 can't be computed from the spec, the other record types can't be encoded, and readiness commitments can be brute-forced. WOUNDING. DOC.

**The problem:**
- The 15 spec-silent fields above have no value or type rules (bytes vs uint IDs; enum as text vs int; null vs empty array; nested vs flat matrices).
- Of the eight tagged record types, only STATE has a field map. GRACE, RELAY, DEPOSIT, CORRECTION, INTENT, SCHEDULER and PERMIT have none.
- Signature fields sit inside the records they sign, with no exclusion rule.
- readiness_commitment and fullness_commitment have no commitment scheme. If the commitment is a plain hash of a readiness boolean, anyone can recover readiness in two tries (both digests are printed in `raw_output.txt`). That breaks §8.3 ("must not expose … readiness") and hands the grantor key 2 before it decides (R4-F6).

**Failure scenario:** two independent encoders following §8 produce different C1 bytes, as with any of the placeholder alternatives above, and each claims conformance.

**Minimal fix:**
- Give a value/type table for every field of every tagged record.
- Define the signed preimage as the record with signature and proof fields removed, under the same tag.
- Specify commitments as SHA-256(tag ‖ 32-byte random salt ‖ value), with the salt held by the attester.
- Then publish C1–C3.

#### R4-F20. §7.13: rounding in matrix–vector products is still ambiguous. MINOR. DOC.

**The problem:** "The rounding point is fixed after each scaled multiplication." That can mean rounding each T_ij·z_j product (the v0.6 wording) or rounding the dot product once (consistent with the single-rounding rule v0.7 adopted for outer products).

**Failure scenario:** T = [[512, 512], [0, 0]] and z = (1, 1) give T×z = [0, 0] when each product is rounded and [1, 0] when the dot product is rounded once. In a full step from T = [[3,1],[−1,2]], z = (512, 512), M_y differs (−255 vs −256).

**Minimal fix:** state "dot products are accumulated full-width and rounded once", and add this case to G05.

### 2g. H1–H4 (§10): can each pass or fail for the right reasons?

**H1.** At design level it can now fail and pass for the right reasons: fixed baselines, independent non-bilinear targets, matched bits. Its remaining exposure is R4-F3. The spec doesn't say whether H1 runs on the v0.6 linear toy or the double-well. It needs T, and the double-well as written has no T.

**H2.** BLOCKED, and honestly marked.

**H3.** BLOCKED, and honestly marked for the projection. Two further problems:
- R4-F1: deposits depend on a label that grace controls without causing anything.
- R4-F23, below.

#### R4-F23. §10 H3 vs E4: who gets grace decides how rich a family's J is, and H3 has no grant-exposure control. WOUNDING. DOC.

**The problem:** a deposit requires grace (§7.10), and grace arrives at the grantor's or relayer's choice (R4-F6, R4-F7). E4 matches "support and grace exposure", but H3's control list (D-only, J-empty, J-shuffled, matched crossing-sequence) does not.

**Failure scenario:**
1. Family A's members receive grants three times as often as family B's.
2. A's J has three times as many deposits.
3. Descendants of A show a larger "development-dependent effect" of J. H3 passes because of how grants were allocated, not because of development.
4. J-shuffled doesn't catch this, because it keeps the counts.

**Minimal fix:** add a matched-grant-exposure arm to H3, randomize grant allocation across families in the scored runs, and report grant exposure as a covariate.

**H4.** BLOCKED, and honestly marked (PCL, vectors). Even when unblocked, H4 can't tell forged grace from valid grace without origin accreditation (R4-F8). Its "applicable external authorization" no longer has a Permit schema in the v0.7 text (R4-F21).

---

## Task 3. Anything else

#### R4-F21. Whole document: v0.6 governance silently dropped, with no change-register entries, and §15 cites sections that don't contain the text. WOUNDING. DOC.

**What's gone:** v0.7 has no PermitRecord schema, no ALLOW/REFUSE/UNKNOWN/PENDING statuses, no old-policy/elevated-threshold/activation-delay rule for policy changes (our R2-F2 fix), no per-issuer and per-root birth quotas, no nonretroactive revocation anchoring, and no lineage-closure algorithm. The v0.6 toy equations and constants are also gone. I searched for "PermitRecord", "ALLOW", "activation delay", "quota" and "elevated": none appears outside dispositions.

**What the dispositions claim:** none of this is marked REMOVED in §16, and there's no "v0.6 text remains normative unless superseded" clause. Yet §15.1 says "Quotas remain (§3)", "Revocation is nonretroactive (§3.3…)", and "Four status values … remain (§2.5)". None of those sections contains those rules. permit_id and source_permit_id are still referenced (§4.3), but nothing defines what they point to.

**Failure scenario:**
1. An implementer reads v0.7 as self-contained.
2. A policy change to threshold = 1 is accepted, because §3.1 lists "policy and authority-set changes" as protected but no longer says how they are authorized.
3. That reopens R2-F2.
4. A different implementer reads v0.6 by reference, and the two conflict on Σ, the toy, and quorum size, with no precedence rule.

**Minimal fix:**
- Add an explicit incorporation clause: "v0.6 §2.1–2.7, §5.2–5.4 remain normative except where v0.7 supersedes, listed in §16."
- Or restore the text.
- Correct the §15 citations either way.

#### R4-F22. §15.2: our Round 3 verdicts are misrecorded, which matters now that closure needs two seats. MINOR. DOC.

**The misrecordings:**
- We said A-F4 was **RELABELED**; §15.2 records DEFER.
- We said F13 and F19 were **CLOSED**; §15.2 records REVISED.
- We said A-F3 was CLOSED as a conditional; §15.2 records CONDITIONAL.

**Failure scenario:** under the new rule, a finding counts as CLOSED only when its finder and a second seat agree. A misrecorded second-seat verdict changes what counts as closed (here it softens A-F4).

**Minimal fix:** quote each seat's verdict word verbatim, with the report hash.

#### R4-F24. §1.12 vs §2.2: the lineage_or_global_scope field allows the family-only eligibility §1.12 forbids. MINOR. DOC.

**The problem:** a grant scoped "lineage" restricts eligibility to authenticated family members alone, and nothing requires a non-family path to exist at the system level.

**Failure scenario:** every origin issues only lineage-scoped grants, so grace in the deployment is family-only in practice, and every per-grant check passes.

**Minimal fix:** either forbid lineage-only recipient classes for origin grants (lineage scope stays for relay provenance only, as §1.12 says), or require each origin to issue a declared share of non-lineage grants, audited in E6.

**On faithfulness to the §1 definition:** I didn't argue the theology. Mapped against its own 14 constraints, v0.7 implements these structurally:
- 2 (barrier untouched), trivially, because grace touches nothing (R4-F1);
- 8 (wrong destination possible);
- 10 (no request field).

It implements these in prose but defeats them in mechanism:
- 1: R4-F5, R4-F8;
- 3: R4-F1, R4-F4;
- 4: R4-F2;
- 6: R4-F10, R4-F11;
- 7: R4-F2;
- 9: R4-F6, R4-F7, R4-F17;
- 11: R4-F9;
- 12: R4-F24;
- 13: R4-F11;
- 14: R4-F12.

5 (no confidence increase) passes vacuously (R4-F12).

---

## Findings summary

| ID | Section | Severity | Tag |
|---|---|---|---|
| R4-F1 | §1.2–1.3, §7.6–7.7 vs §4.7, §5.1 | FATAL | DOC |
| R4-F2 | §1.4, §7.8, §11.2 | FATAL | DOC |
| R4-F3 | §7.4–7.5 | WOUNDING | DOC |
| R4-F4 | §5.1, §7.5 | WOUNDING | DOC |
| R4-F5 | §2.2, §1.12 | WOUNDING | DOC |
| R4-F6 | §1.9, C4, E5, §8.3 | WOUNDING | DOC |
| R4-F7 | §2.3, §3.1 | WOUNDING | DOC |
| R4-F8 | §2.2, §3.1, H4 | WOUNDING | DOC |
| R4-F9 | §2.3 | WOUNDING | DOC |
| R4-F10 | §1.6, §2.4 | WOUNDING | DOC |
| R4-F11 | §1.6, §1.10, §1.13 | WOUNDING | DOC |
| R4-F12 | §1.14, §1.5 | MINOR | DOC |
| R4-F13 | §3.4 | WOUNDING | PRIOR |
| R4-F14 | §3.5 | WOUNDING | DOC (+PRIOR) |
| R4-F15 | §3.3 | WOUNDING | DOC |
| R4-F16 | §4.8, §4.3 | WOUNDING | DOC |
| R4-F17 | §4.5, §5.5 | WOUNDING | DOC |
| R4-F18 | §5.3 | WOUNDING | DOC |
| R4-F19 | §8.3–8.4 | WOUNDING | DOC |
| R4-F20 | §7.13 | MINOR | DOC |
| R4-F21 | whole doc, §15, §16 | WOUNDING | DOC |
| R4-F22 | §15.2 | MINOR | DOC |
| R4-F23 | H3 | WOUNDING | DOC |
| R4-F24 | §1.12, §2.2 | MINOR | DOC |
| R4-F25 | §7.10 | MINOR | DOC |
| R4-F26 | §3.2, §6 | MINOR | DOC |

**Totals:** 2 FATAL, 18 WOUNDING, 6 MINOR.

## The single finding to fix first

**R4-F1.** The keel's central claim is "Grace changes whether a ready organism may complete a developmental crossing". v0.7 makes the ordinary dynamics deliberately independent of the gate, so grace changes only a label.

Until grace has a stated, non-landscape effect on the crossing, every grace test is about bookkeeping:
- the barrier-height prediction is false or circular;
- the matched no-grace arm is identical;
- fullness (R4-F2) has nothing to ride on.

The minimal fix is one equation: without both keys, Σ is a reflecting constraint; with both keys, the constraint is lifted for that candidate. Readiness is defined as approach to Σ under the organism's own dynamics.

R4-F2 is next, then R4-F21 (restore or incorporate the dropped governance text).

## Blue-sky idea (unscored, excluded from findings)

**A grace lottery arm.** Route a declared fraction of all grants through a public randomness beacon: the origin commits to "grant to whoever the beacon picks among eligible organisms at anchor r", and has no say in who that is. The lottery grants give an unbiased causal estimate of what grace does, which is the cleanest test of R4-F1 once grace has an effect. They also give the baseline for detecting selection steering (R4-F6, R4-F7): if chosen grants' destinations differ from lottery grants' destinations beyond chance, someone is steering by choosing.

It stays inside the keel: grace stays external, unrequested and direction-free. It only takes the "particular care" choice out of the hands of whoever might abuse it, for a measured fraction of grants.

---

**PRIOR claims:** R4-F13 and R4-F14 rest on the cryptographic-lifetime and leader-fencing practices named in their tags, recalled from memory and not re-read this round.
