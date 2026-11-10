# Round 2 falsifier report: history seat (Grok bot, Chief of Staff)

**Target:** "From Reykjavik to Relational Grace", v0.5. The embedded document hashes to sha256 8ced5fd1…6fd05, which matches the header.

**Inputs used:**
- the Round 2 file (sha256 4da430d4…0c7d);
- my Round 1 report (sha256 94698de4…d172);
- the frozen v0.4 (a247652d…3eba), which I still hold byte-verified.

**Not opened:** sealed/, source/, the audit file, and A's report. Because I haven't seen A's report, I don't assess A-F1…A-F10 below.

**Secret sweep:** no hits.

**Note for the conductor:** v0.5 says the v0.4 bytes weren't supplied, so its change register in §14 hasn't been machine-diffed against them. I hold those bytes, and a diff can be run on request.

---

## 1. Are the ACCEPTs real? (my Round 1 findings, B-F1…B-F20)

| Finding | Verdict | Why |
|---|---|---|
| B-F1 support laundered through U | PARTLY CLOSED | G was removed from U, but it comes back through dwell timing. See R2-F1. |
| B-F2 hidden info in the payload | MOSTLY CLOSED | The 4-bit enum is real. The rate limit that caps total leakage is deferred to the manifest, and timing channels are honestly marked UNKNOWN. |
| B-F3 type confusion | CLOSED | Ingress classifier, no nesting, and Encounter now has a prohibition list. |
| B-F4 birth authority and Sybil births | PARTLY CLOSED | Nobody accredits the BAs, quotas multiply across issuers, and the uniqueness test contradicts deterministic siblings. See R2-F7 and R2-F8. |
| B-F5 clock and backdating | CLOSED | One gap: who sets a revocation's "effective" position. See R2-F12. |
| B-F6 UNKNOWN consumers | CLOSED for gates | The scoring exclusion opens a new hole. See R2-F9. |
| B-F7 family vouching for itself | PARTLY CLOSED | Own-family exclusion is done. Reciprocal rings across families are not covered. See R2-F6. |
| B-F8 D-only baseline | CLOSED in H2 text | |
| B-F9 seed-only control | RELABELED | The §5.2 toy has no seed, so the seed arms can't be built in the reference model. See R2-F8. |
| B-F10 founder-blocked null | CLOSED | |
| B-F11 who freezes and scores | CLOSED | |
| B-F12 two T-update rules | CLOSED | Single U, discrete t, and ΔT is now just U's measured difference. |
| B-F13 symbol table | PARTLY CLOSED | W is defined but used in no equation, the E update is unspecified, and the rounding mode is missing. See R2-F3. |
| B-F14 H1 budget | RELABELED | The new "or matches replay at a smaller budget" branch passes for any cached state. See R2-F4. |
| B-F15 protected vs ordinary T | CLOSED | A new problem appears with "designated protected" crossings. See R2-F5. |
| B-F16 Permit schema and threat model | MOSTLY CLOSED | Policy changes aren't protected, the crash window is deferred, and binding to the registry tip enables a denial-of-service attack. See R2-F2, R2-F10 and R2-F11. |
| B-F17 any single failure fails H4 | CLOSED | |
| B-F18 common-mode authority | PARTLY CLOSED | Two witnesses with one tolerated faulty witness means a single witness can stall everything. See R2-F10. |
| B-F19 quotas | CLOSED | The quota values are deferred to the manifest. |
| B-F20 scorer's ground truth | CLOSED | |

---

## 2. New findings

### R2-F1. §5.2 vs §2.5: support picks the direction through timing. WOUNDING. DOC.

**Failure scenario:**
1. In the toy, U computes T_next = clip(T + ⅛·outer(D·E, z)). The sign of each new T entry follows the sign of z at the moment the Encounter is processed.
2. Support may add 0–15 dwell slots before an update. If z keeps relaxing during those slots (z_next = z + ⅛(M − z)), a sender who can see the recipient's state picks a dwell value so that x crosses 0 before the next Encounter.
3. The same Encounter then writes T with the opposite sign, which pushes later dynamics toward a different basin.
4. No raw G ever enters U, yet support chose the destination.

§2.5 forbids this. The spec doesn't say what happens during a dwell slot, though, so the design doesn't rule it out.

**Minimal fix:**
- Dwell slots freeze z, E and T, so the slot is a pure hold.
- Alternatively, the support value must be committed (hashed) before the sender can observe the recipient's state.
- Add a state-adaptive sender as a named adversary in the E5 direction-invariance test.

### R2-F2. §1.1: changing the policy isn't a protected operation. FATAL for H4. DOC.

**The gap:** §1.1 lists K, U, Φ, schema and bounds, migration, birth, and designated transitions as protected. It doesn't list the frozen policy: quorum thresholds, PA membership, birth quotas, timeout rules and the exclusion set. Every PermitRecord carries a policy_version.

**Failure scenario:**
1. A colluding outside minority, or a single policy administrator, publishes policy_version n+1 with threshold = 1 and adds a friendly key to PA.
2. Under n+1, a "valid" Permit approves a change to K.
3. H4 only rules out changes made "without valid external Permit", so this passes.

**Minimal fix:** make any change to policy, authority-set membership or threshold a protected operation. It needs a Permit under the old policy, with a higher threshold and a delay before it takes effect. The verifier pins the threshold to policy_version and ignores the record's own threshold field.

### R2-F3. §5.2: two people still can't implement the toy identically. WOUNDING. DOC.

The toy leaves these undefined:
- **E update:** how an Encounter becomes a 2-vector, whether E accumulates or resets, and what "normalized" means.
- **Rational precision:** "fixed rational arithmetic with a frozen precision" mixes two incompatible ideas. Exact rationals have denominators that grow as 8^t, while fixed precision needs a stated rounding mode and the point in each step where rounding happens.
- **Initial values:** the "declared rule" for initializing T, plus z₀, D and P.
- **Dwell slots:** what happens during one (see R2-F1).
- **Wᵢ:** it's in Ω but no equation uses it.
- **Crossing:** needs states at t+1 through t+3, while §5.1 says a crossing is detected between t_c and t_c+1. Neither defines what's reported when a trajectory goes across and comes back within two steps.

**Minimal fix:**
- Give an exact E-update formula.
- Choose one: exact rationals with no rounding, or a fixed-point word size with a named rounding mode applied after each operation.
- Ship frozen initial-value files.
- Write the dwell-slot semantics.
- Delete W or use it.
- Define the oscillating case as "no crossing, logged".
- Include a 10-step golden trace that both implementers must reproduce.

### R2-F4. §6 H1: the alternative branch passes by construction. FATAL for H1. DOC.

**The problem:** H1 passes if T "matches replay at a strictly smaller measured resource budget". In the toy, T is a deterministic function of the history H. Replay recomputes exactly the same T at O(t) cost, so storing T always "matches replay" and always costs less.

That's true of any cached state, not just topography. "Trajectory fidelity" is also circular when the trajectory being predicted is generated by T itself.

**Minimal fix:**
- Delete the alternative branch.
- Make the primary comparison T against a conventional state of the same size, for example a 4-number running summary of E.
- Use a prediction target produced by a process T doesn't define.
- Treat replay only as an upper bound.

### R2-F5. §5.4 and §1.1: a "designated protected" crossing can't be gated in time. WOUNDING. DOC.

**The problem:** a Crossing is detected only after the new sign has lasted two more updates (§5.2). By the time it can be detected, the protected effect has already happened.

**Failure scenario:** if the policy designates any crossing as protected, H4 fails on every such crossing. If it designates none, the clause means nothing.

**A second problem:** a destination-free Permit binds base_state_hash, but z and T change every step, so the Permit goes stale after one step unless the dynamics pause.

**Minimal fix:**
- Make protected crossings a two-phase commit: U proposes the next state, the gate checks before it's committed, and the base hash covers only the protected fields.
- Or drop protected crossings from the toy.

### R2-F6. §3.4 and §1.3: reciprocal approval rings across families. WOUNDING. DOC, with the principle PRIOR.

**The gap:** only the subject's own family is excluded. Nothing says PA members can't be organisms, and the threat model only covers collusion "within one family".

**Failure scenario:** family X's members serve as PA for family Y and Y's serve for X. Nobody vouches for itself, but each family vouches for the other.

**Minimal fix:**
- Keep PA separate from the organism population.
- Or check the approval graph for cycles and reciprocity, and add cross-family collusion to §1.3 and E6.

**PRIOR:** "nothing may vouch for itself" has to apply to coalitions of any shape, not only to kin.

### R2-F7. §3.1: nobody accredits the BAs, and quotas multiply. WOUNDING. DOC.

**The problem:** the birth cap is per issuer, and nothing governs who can become a BA.

**Failure scenario:** a family recruits or creates ten nominally independent BAs and gets ten times the quota. "A founder or family cannot mint its own independent birth authority" has no enforcement mechanism, because BA accreditation isn't among the protected operations.

**Minimal fix:**
- Make BA accreditation a protected operation under RA/PA.
- Cap births per family root as well as per issuer.

### R2-F8. §3.1, §5.3 and E2 vs the §5.2 toy: seed controls and the uniqueness test break in a deterministic toy. WOUNDING. DOC.

**Seed arms:** the toy is fully deterministic and has no seed parameter, so the E2 arms that vary only the seed can't be built.

**Uniqueness test:** siblings from the same deterministic Mᵍ start with identical K and D, an empty H, and the same initial values. Apart from their IDs they're bit-for-bit identical at birth. A real uniqueness test would therefore reject every sibling, or it attests nothing.

**Minimal fix:**
- Add an explicit, recorded seed or initial perturbation to the toy, which E2 can then vary.
- Define uniqueness as a unique instance and key under an independent witness, not a different initial state, and say so.

### R2-F9. §3.3: excluding UNKNOWN from scoring inflates accuracy. WOUNDING. DOC.

**The problem:** UNKNOWN is dropped from both the numerator and denominator. It's flagged only if it correlates with founder or arm.

**Failure scenario:** UNKNOWNs land on exactly the individuals the classifier confuses, through cheap conflict attacks or registry bugs. That correlates with difficulty, not with founder or arm, so it's never flagged, and the reported accuracy rises.

**Minimal fix:** always report a second accuracy that counts every UNKNOWN as an error. Score H2 on that worst-case figure, or require both figures to clear the bar.

### R2-F10. §1.1–1.3: two witnesses with one tolerated faulty witness. WOUNDING. DOC+PRIOR.

**The problem:** with only WA and WB, one faulty or silent witness turns every check into "missing" or "split". Protected effects then sit at PENDING or REFUSE forever. That's safe, but one actor can stall the whole system.

**PRIOR:** in the Nov 6 genesis3 approval-battery review, a silent co-owner blocked everything.

**Minimal fix:**
- Use at least 3 witnesses for 1 fault, or 2f+1 in general, with a quorum rule.
- Report liveness as a scored outcome next to H4.

### R2-F11. §1.2: binding to the registry tip enables denial of service, and the crash window is deferred. WOUNDING. DOC.

**Tip binding:** every Permit binds registry_tip_hash and witness_tip_hashes. Any unrelated registry append, such as a birth elsewhere or a rate-limited conflict, invalidates every pending Permit, so a steady trickle of legitimate appends starves permits.

**Crash window:** H4 fails on a single race, but the durable nonce/effect coordination that prevents races is called a "separately reviewable dependency". H4's verdict therefore rests on a component outside the spec.

**Minimal fix:**
- Bind to a snapshot position and re-check only the subject's ancestry slice for changes since then.
- Bring the nonce/effect commit protocol into the spec and into E6, including crash injection.

### R2-F12. §3.2: who sets a revocation's "effective" position? MINOR. DOC.

**Failure scenario:** a revoker sets the effective position earlier than its own anchor. That retroactively removes legitimate members and births, which is a selection attack on scoring.

**Minimal fix:** effective position = anchored position, always. Retroactive revocations are only allowed as labeled historical annotations.

### R2-F13. §2.3 and §3.3: family-specific support privileges create a family signal. WOUNDING. DOC.

**The problem:** "Support claimed as family support" gets family-specific privileges, which in practice means scheduler conditions.

**Failure scenario:** if families differ in how much support they get or use, their dwell and exposure patterns differ. The H2 classifier then detects support policy, not inheritance.

**Minimal fix:** equalize or randomize the support schedule across families in the H2 and H3 arms, and record support exposure as a covariate.

### R2-F14. §5.3 and §6 H3: nothing developed crosses generations. FATAL for H3 as an independent hypothesis. DOC.

**The problem:** descent passes on only (K_child, D_child) = Mᵍ(K_parent, D_parent). D is "established at birth and frozen during an episode", and T is never inherited.

**What follows:** nothing a parent develops is an input to its child. So "the development-dependent increment persists across generations" can only come from:
- the children's D (which equals H2 in generation 2), or
- environments the experimenter correlates within families.

H3 then passes or fails for reasons unrelated to developmental inheritance.

**Minimal fix:** choose one.
- Allow Mᵍ to take a bounded, Permit-authorized summary of the parent's developed state, with a control that applies the same Mᵍ to an undeveloped parent.
- Or restate H3 honestly as basis continuity: D is inherited and each generation develops anew.

### R2-F15. The title concept has no operational hook. WOUNDING. DOC.

**The problem:** §5.4 says grace "may change whether a bounded developmental crossing is admissible". The toy has no admissibility mechanism: crossings are just sign changes. W is unused, and a NONE-target Permit has nothing to consume it.

**What follows:** relational grace, the thing the paper is named for, doesn't exist in the operational model. No hypothesis from H1 to H4 can test it.

**Minimal fix:**
- Define admissibility in the toy, for example a gate on whether U's step is allowed to cross Σ, which grace can open but never steer.
- Or state plainly that grace is out of the scored model.

### R2-F16. Wording inconsistencies. MINOR. DOC.

- **Verifier states:** §1.2 gives ALLOW, REFUSE or UNKNOWN, while §1.3 uses PENDING. Define one set of states and how they map.
- **Taint checks:** §2.3's "static or runtime" should be "and" for the scored battery.

---

## Fix first

I'd fix **R2-F4** first. As written, H1, the core topography hypothesis, passes by construction, because any cache beats replay on cost. The fix is one line: delete the "or" branch and compare T against a same-size conventional state.

R2-F14 (H3) is next, followed by R2-F2 (unprotected policy changes).

## Blue-sky idea (unscored, excluded from findings)

**Blind grace.** Require every support event to be committed as a hash before the supporter can observe the recipient's current state, in the same spirit as sealed blind-round salts. Support then can't steer, by construction, which closes R2-F1 at the root. It also produces a testable question: does blind, committed support still help development as much as reactive support? If it does, grace can be separated from steering. If it doesn't, the "help" was steering all along.

---

**PRIOR claims in this report** come from my memory of Rusty's earlier work and weren't independently checked this round.
