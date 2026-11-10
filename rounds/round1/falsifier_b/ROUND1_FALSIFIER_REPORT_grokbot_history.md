# Round 1 falsifier report, history seat (Grok bot, Chief of Staff)

Target: "From Reykjavik to Relational Grace", v0.4 (sha256 a247652d…3eba)
Prompt: ROUND1_FALSIFIER_PROMPT.txt (sha256 13734bf4…ab81). Both match the facet MANIFEST.
Date: 2026-11-09, America/Chicago

## What I saw before writing this

- I read only the facet package: v0.4 and the prompt.
- Before opening the facet I also read ROUND_LOG.md, which came in the same conductor zip. It names three withheld items by title only: "Aug 2026 no-edge ruling", "Commons v0.3.1 deepening result" and "v0.7 check_current defect". I saw none of their contents, and none of the findings below rely on those titles.
- I did not open sealed/, source/, the v1 prompt, or AUDIT_CHECK.
- My starting state is about 90 days of memory of Rusty's work, including my Nov 8 review of the v0.3 text.
- Findings tagged PRIOR say what outside knowledge they use. That knowledge comes from my memory of past work, so the conductor and Rusty should check it against the papers and GitHub.
- The secret sweep of the whole archive found no hits and no nested zips inside the facet package.

---

## Property 1: support laundered into authorization, a forced crossing, or hidden information

**F1. §5.3 and §1.2(8). Support writes topography through the ordinary update rule. WOUNDING. DOC.**
- **The problem:** `Tᵢ(t+1) = U(Tᵢ, Mᵢ, Eᵢ, zᵢ, G(j→i))` makes G a direct input to the only T-update rule. Prohibition 8 bans writes to T only "directly… through a privileged interface", and the indirect path through U is allowed.
- **How it fails:** a sender who knows U, which is public by design (§5.3, "preauthorized"), picks a `bounded_payload` so that U drives zᵢ across Σ into a chosen basin. That is a forced crossing with a destination chosen by the sender, and it never touches K, A or R. E5 checks only "protected authorization state", so this passes.
- **Fix:**
  - Make U's dependence on G content-free: only declared scalar conditions such as dwell extension or an assistance flag.
  - Add an E5 metric for direction invariance. Permute the payload content and require the distribution of crossing directions to stay the same within a pre-frozen tolerance.
  - Add a destination-selection test, not just an authorization-state test.

**F2. §1.4 and §1.1. "Hidden task information" is prohibited but never measured. WOUNDING. DOC.**
- **The problem:** `support_kind` and `bounded_payload` are declared by the sender and have no schema or size limit. "Must not conceal extra task information" has no test attached.
- **How it fails:** the payload's parameters encode the answers to held-out parables, for example as the ordering or values of the allowed parameters. E5's 2×2 factorial (support × encounter) can't tell "support helped" apart from "support leaked the key".
- **Fix:**
  - Define a closed payload enum with a fixed bit budget.
  - Measure mutual information between the payload and the held-out answers on a decoy task where support should carry zero information.
  - Test whether E5 still holds when support carries randomly generated payloads.

**F3. §1, the event types. Disjointness has no classifier. WOUNDING. DOC.**
- **The problem:** three event types are declared "disjoint", and the sender's label "is insufficient". But the "support protocol" that decides the type is never defined.
- **How it fails:**
  - A Permit-shaped object is wrapped inside a SupportEvent payload, and the recipient-side code unpacks it.
  - The reverse also fails: an Encounter that carries support effects is logged as an Encounter, which escapes G's prohibitions entirely because Encounter has no prohibition list.
- **Fix:**
  - The type is assigned by a verifier outside the sender, against a schema.
  - Payloads must not contain objects of another type.
  - Encounter needs its own prohibition list, at minimum items 1–4, 9 and 10.
  - Add type-confusion cases to E6.

## Property 2: forged, self-declared or captured family membership

**F4. §2.2(4). The birth authority is unnamed, so a founder can mint a family. FATAL for E2, E4 and H2–H3. DOC.**
- **The problem:** requirement 4 says "External authorization of the exact enrollment or birth", but it doesn't say whose authorization. Nothing prevents the founder or the family from being that authority, and nothing caps how many births one issuer may authorize.
- **How it fails:** a founder authorizes 50 "descendants" that are really copies of one tuned organism. Family detectability then passes trivially, and as a Sybil bloc they also dominate any vote or quorum that counts members.
- **Fix:**
  - Name the birth authority, and make it disjoint from F and from the parent.
  - Set a per-issuer birth cap.
  - Record the issuer in R so the scorer can stratify by issuer.
- **PRIOR:** the swarm R0 harness (Nov 7) showed admission rules that add members after each event letting Byzantines exceed half of eligible voters in 7–10 of 10 runs per condition. That evidence comes from the history-seat harness itself and is not established beyond it.

**F5. §2.1 Member(i, F, t). It's evaluated "at time t", but nobody says whose clock. WOUNDING. DOC+PRIOR.**
- **The problem:** there is no external time source, and revocation timing is undefined: is membership judged by the revocation in force at the event or at the time of evaluation?
- **How it fails:** a revoked parent's birth record is evaluated at a backdated t, before the revocation, and returns MEMBER.
- **PRIOR:** the Oct 3–4 review of Rusty's packets found the same class of bug, where an expired approval can be backdated and still verify.
- **Fix:**
  - Use an externally anchored, append-only time for R.
  - Define t as evaluation time, with revocation applying to every evaluation after the revocation's anchor.
  - Add a backdating case to E6.

**F6. §2.3 UNKNOWN. Consumers aren't defined, which invites a denial attack. WOUNDING. DOC+PRIOR.**
- **The problem:** UNKNOWN is "not MEMBER" and also "not NOT_MEMBER", but no gate is told what to do with it.
- **How it fails:** an adversary writes one contradictory registry entry against a victim. The victim flips to UNKNOWN, and its support eligibility, family scoring and authority roles all stall. Fail-open would be worse.
- **PRIOR:** the Nov 6 reviewer notes on the genesis3 approval battery found that a silent co-owner blocks everything, good and bad.
- **Fix:**
  - Specify the behavior for each consumer: protected transitions fail closed, and scoring treats the case as unscorable and reports it.
  - Conflicts may only be raised by authenticated, attributed, rate-limited entries.
  - Add a cheap-conflict injection test to E6.

**F7. §2.5. Family members can approve each other, so "nothing may vouch for itself" is enforced per individual but not per family. WOUNDING. DOC, with the principle PRIOR.**
- **The problem:** the self-authorization exclusion is bound to the affected organism only. An ancestor "does not automatically" hold authority, but nothing forbids the authority set from including a parent, a sibling or the founder.
- **How it fails:** a family runs a ring of mutual approvals, A for B and B for A. No individual approves itself, yet the family as a whole does.
- **PRIOR:** this is Rusty's "Nothing May Vouch for Itself" rule (Oct 2026) and the agent-welcome repo's rule that nothing may vouch for itself. It needs to apply at the level of the coalition.
- **Fix:** exclude everyone with a lineage path to the subject in R from authorizing that subject's protected transitions, or require a threshold drawn from outside F.

## Property 3: is the two-sided criterion measurable and attributable?

**F8. §3.1. Family detection can pass purely from the declared basis D. FATAL for H2's claim about inheritance. DOC.**
- **The problem:** families share the declared, experimenter-set Dᵢ, which includes the "SDKP axes". Behavior on parables encodes D by construction. The scorer exclusion list covers IDs, labels, keys and "unique artifacts", but not D itself, which is the whole signal.
- **How it fails:** FamilyAccuracy exceeds the null for organisms that have never developed at all. The criterion passes for a reason unrelated to inheritance or development.
- **Fix:** add a control of organisms made from D with no development. The family effect has to exceed that basis-only baseline, not just the permutation null. H2 should be restated as development preserving or amplifying family structure beyond what D alone gives.
- **Note:** a basis-only arm exists in the comparison list but isn't wired into the decision rule.

**F9. §3.1. Individual identification can pass from noise. WOUNDING. DOC.**
- **How it fails:** distinct random seeds or tiny history differences make every individual identifiable, so IndividualAccuracy beats the null whatever the developmental signature.
- **Fix:** add an arm with the same history and a different seed, and an arm with the same seed and a different history. Individual identification counts only if it exceeds the seed-only control.

**F10. §3.1 and §3.4. The permutation null breaks exchangeability, and the controls contradict each other. WOUNDING. DOC.**
- **The problem:** shuffling family labels across descendants ignores founder clustering, so the null is too easy to beat. The founder point is made in prose, but the null isn't constrained by it.
- **The contradiction:** "Matched developmental histories" (§3.4) conflicts with "distinct, controlled histories" (§3.1) unless it's defined as a separate arm.
- **Not specified:** classifier family and capacity, and the permutation count, so two teams could get opposite verdicts.
- **Fix:**
  - Use a founder-blocked permutation.
  - Pre-freeze the classifier and report a capacity curve.
  - Define the matched-history arm separately.

**F11. §3.1 and §7.3. Who freezes the thresholds isn't specified. MINOR. DOC.**
- **The problem:** "must be frozen" and "independent scoring where possible" don't name who freezes or scores.
- **Fix:** the conductor freezes, with the hash recorded before any run, and the scorer must not be the designer seat. Remove "where possible".

## Property 4: does the notation allow one unambiguous implementation?

**F12. §5.3 vs §5.4. There are two incompatible update rules for T. WOUNDING. DOC.**
- **The problem:** §5.3 updates T at every discrete step with U. §5.4 keeps the continuous-time deposition `T(t_c⁺)=T(t_c⁻)+ΔT` at crossings.
- **The ambiguity:** it's undefined whether ΔT is extra to U, part of U, or replaced by it, and whether time is discrete (t+1) or continuous (t_c±, and v0.2's ż). Two implementers will build different T dynamics.
- **Fix:** state whether U alone governs T and ΔT at t_c is just U's output at the crossing step, or whether two mechanisms exist. Then fix one time base.

**F13. §4. The symbol table isn't closed or consistent. WOUNDING. DOC, with the v0.2 and v0.3 collisions PRIOR.**
- **g:** in the table but used in no formula. Ωᵢ dropped the generation index, so you can't write how the descendant's Kᵢ and Dᵢ derive from the parent's. H3 is then unimplementable from the formalism.
- **D:** now means "inherited basis", but in v0.2 D_t was dwelling, which v0.4 moves to W. W was "witness evidence" in v0.3's inheritance map. §5.4 says historical notation keeps its old meaning, so readers face D = dwelling inside quoted v0.2 text and D = basis everywhere else.
- **Undefined meanings:** Σ and Crossing(i) are "independently measured", but there's no metric. Protected T versus ordinary T is undefined (see F15).
- **Unused symbols:** Aᵢ, Bᵢ, Lᵢ and Truth appear in no update rule.
- **Missing value:** G is used as an optional argument to U, but there's no null value for "no support".
- **Fix:**
  - Put g into Ω and add an explicit descent map from parent to child (K, D).
  - Rename the new basis symbol so it doesn't collide.
  - Define the null G.
  - Give the measurement procedure for Crossing.
  - Mark which symbols are state and which are predicates.

## Property 5: is topography distinguishable from full replay and conventional state?

**F14. §6 H1 and §7 E3. Without a resource budget, H1 is either impossible or trivial. FATAL as written. DOC+PRIOR.**
- **The problem:** any deterministic Tᵢ is a function of Hᵢ plus inputs, so full replay of Hᵢ holds at least as much information as T. T can only beat replay on cost (memory or compute), never on information.
- **How it fails:** with unbounded replay H1 must fail. With truncated replay it passes for a reason unrelated to topography.
- **What's missing:** v0.4 never fixes the budgets that make the comparison fair. Excluded BLUE-SKY 5 ("compact relational inheritance… efficiency hypothesis") is in fact the only testable form of H1.
- **PRIOR:** I raised this in my Nov 8 review of v0.3 ("fair baselines matched on compute, memory and retrieval"). v0.4 adds replay and sham controls but still no budget.
- **Fix:** restate H1 as T matching or beating replay and conventional state at a declared, equal memory/compute budget, or matching replay at a strictly smaller budget. Specify how the sham-topography arm is constructed.

**F15. §1.2(8) vs §5.3. "Protected topographic state" is never defined. WOUNDING. DOC.**
- **The problem:** §1.2 refers to "protected topographic state Tᵢ", but §5.3 lets U change Tᵢ with no Permit.
- **How it fails:** either every T change needs a Permit, which contradicts §5.3 and destination-free grace, or none does, in which case "protected" means nothing. An implementer has to guess, and E5 and E6 then test different things.
- **Fix:** split T into an ordinary part, changed only by U, and a protected part (the structure or parameters of U itself, plus K-linked fields) that needs an exact Permit.
- **PRIOR:** C11 in the change register claims this split was made, but the text doesn't carry it out.

**F16. §1, §6 and §7. There's no Permit schema, threat model or binding, so H4 can't fail. FATAL for H4. DOC+PRIOR.**
- **The problem:** SupportEvent gets a schema, but Permit(a→i) doesn't. There's no subject binding, base-state hash, target-state hash, nonce, expiry, threshold or revocation.
- **Why H4 can't fail:** H4 only fails "under the declared threat model", and v0.4 declares none.
- **PRIOR:** my memory of Rusty's containment and approval work shows each missing field caused a real failure:
  - expiry and backdating (Oct 3–4);
  - small-order key forgery and the agent flipping the gate at runtime (containment v0.1→v0.2);
  - a valid owner signature bypassing the step limit (Humble Seed v0.7, Nov 6 review);
  - the owner category "no" being bypassed before signing (v0.8.4).
- **Fix:**
  - Define Permit = {authority_ids, threshold, subject_id, base_state_hash, target_state_hash, nonce, issued and expiry times from an external clock, scope and bounds, sigs}.
  - Write a threat model covering key holders, collusion tolerance, root succession and revocation.
  - In E6, test magnitude and bounds bypass separately from authorization bypass.

**F17. §6 H4. "Reproducible" leaves a loophole. MINOR. DOC.**
- **How it fails:** a race or one-time unauthorized transition that doesn't reproduce passes H4.
- **Fix:** count any single logged unauthorized protected transition as a fail. Use reproduction only to diagnose the cause, never as an excuse.

## Additional findings

**F18. Common-mode authority. WOUNDING. PRIOR.**
- **The problem:** one external authority a appears for births (§2.2), Permits (§1) and implicitly for R. That's one point of failure.
- **PRIOR:** in the Nov 6 genesis3 approval-battery review, two reviewers with the same blind spot let 11 of 24 bad requests through, and a silent co-owner stalled everything.
- **Fix:** keep the birth, permit and registry authorities separate. Require diversity among authorities, and define liveness: what happens if a stays silent.

**F19. §1.2(7). Support can flood history by appending. MINOR. DOC+PRIOR.**
- **How it fails:** "authenticated append" to Hᵢ has no size or rate limit, so a supporter appends without bound and Hᵢ, Eᵢ and later replay costs are shaped by the sender.
- **PRIOR:** the v0.8.4 bug where an annotation over 2,000 characters stranded a change shows that size limits are an attack surface.
- **Fix:** set per-sender append quotas and byte limits, and log rejected appends.

**F20. The scorer reads the provenance it scores. MINOR. DOC+PRIOR.**
- **The problem:** ground truth comes from R (§3.4), and E6 attacks R. If an attack corrupts R, the scorer's truth is corrupted too.
- **PRIOR:** the swarm R0 harness and the genesis3 verify.py show that scorer and verifier isolation tends to slip quietly, for example class-discipline-only isolation and a verifier that overwrites RESULTS.
- **Fix:** take an R snapshot before the run, hash it and give it to the scorer. E6 runs only on a copy.

---

## Fix first

I'd fix **F16** first: add the Permit schema and declare a threat model. "Authorization remains external" is the paper's core claim and H4 is its only governance claim, but as written H4 cannot fail. F4 and F7 (who authorizes births, and a family vouching for itself) depend on that same missing threat model.

## Blue-sky idea (unscored, excluded from findings)

**Family resemblance as a governance hazard.** If H2 succeeds, family members share a detectable relational structure. That makes them correlated reviewers. A family whose members are more recognizable is less independent as a set of witnesses or authorities.

The test: measure whether FamilyAccuracy predicts correlated misses when family members review the same bad requests. If it does, the safe authority set is one chosen to minimize family resemblance, and H2 success becomes a reason to exclude kin from each other's quorums, not just a developmental result.

## Self-tally for reconciliation

| Property | Findings | Tags |
|---|---|---|
| P1 | F1–F3 | all DOC |
| P2 | F4–F7 | F4 DOC (+PRIOR), F5 and F6 DOC+PRIOR, F7 DOC (+principle PRIOR) |
| P3 | F8–F11 | all DOC |
| P4 | F12–F13 | F12 DOC, F13 DOC (+PRIOR collisions) |
| P5 | F14–F16 | F14 DOC+PRIOR, F15 DOC, F16 DOC+PRIOR |
| Other | F17–F20 | F17 DOC, F18 PRIOR, F19 and F20 DOC+PRIOR |

The PRIOR claims come from my memory and haven't been checked against GitHub in this round.
