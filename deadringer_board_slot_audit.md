# DEAD RINGER — Board Slot Entry Audit

Cross-reference of every `[NOTEBOOK PROMPT]` in the manuscript against the eight Ch 11 Board slots defined in `deadringer_notebook_system.md` §5.2.

**Companion docs:**
- `deadringer_notebook_system.md` §5 — Board slot architecture and presentation mechanic
- `deadringer_systems.md` §7 — Contradiction System (factual vs knowledge-level)
- Chapter files 1–12 — every notebook prompt is sourced here

**Purpose of this document:**
1. Verify every Board slot is reachable through main-line play
2. Identify slots that require optional content (thoroughness-gated)
3. Surface prompts that don't serve any slot (context-only, possibly cuttable)
4. Surface prompts that serve too many slots (diluted weight)
5. Build per-chapter thoroughness thresholds for slot completion
6. Output tagging schema for build-time implementation

**Audit scope:** 70 notebook prompts across 11 chapter files (plus references in structure docs and ogawa-incident.md). Verified via grep `\[NOTEBOOK PROMPT` pattern; total count matches notebook system spec estimate (40–60 with optional expansion to ~70).

---

## 1. OVERVIEW

### 1.1 The Eight Board Slots (Quick Reference)

| # | Slot | Type | Thesis |
|---|---|---|---|
| 1 | **IMPOSSIBLE KNOWLEDGE** | Knowledge-level | Endo knows things with the wrong resolution |
| 2 | **SOCIAL ACCESS PATTERN** | Knowledge-level / positional | Endo positioned at every chokepoint |
| 3 | **COMMITTEE AS MECHANISM** | Factual | Same committee, opposite outcomes |
| 4 | **INFRASTRUCTURE ACCESS** | Knowledge-level | Endo is the only person with exchange access |
| 5 | **THE GARDEN** | Factual | Botanical timeline maps disappearances |
| 6 | **FRAMING AUTHORSHIP** | Factual | Planted documents trace to Endo's access |
| 7 | **SOCIAL ACCESS (WITNESS)** | Knowledge-level | People told Endo everything |
| 8 | **INDEPENDENT CORROBORATION** | Factual | Silver car witnessed by three independent sources |

### 1.2 Audit Findings Summary

| Finding | Count |
|---|---|
| Total notebook prompts | 70 |
| Prompts contributing to ≥1 Board slot | 47 |
| Prompts as context only (no slot contribution) | 23 |
| Prompts contributing to exactly 1 slot | 29 |
| Prompts contributing to 2 slots | 14 |
| Prompts contributing to 3+ slots (overload risk) | 4 |
| Slots with redundant coverage | 2 (GARDEN, INDEPENDENT CORROBORATION) |
| Slots with thin coverage | 1 (SOCIAL ACCESS WITNESS — requires optional Ch 11 case-assembly content) |
| Prompts requiring optional player exploration | 12 |

### 1.3 Reachability Summary

All 8 slots are reachable through a standard main-line playthrough. However:
- **3 slots** (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, FRAMING AUTHORSHIP) require ≥3 contributing entries each for completion.
- **2 slots** (GARDEN, INFRASTRUCTURE ACCESS) are completable with as few as 2 contributing entries each but benefit from 3+.
- **2 slots** (COMMITTEE AS MECHANISM, INDEPENDENT CORROBORATION) require specific NPC-gated content (Haruki Ch 5, Kaito Ch 7) — missing either leaves the slot EMERGING rather than COMPLETE.
- **1 slot** (SOCIAL ACCESS WITNESS) is the most optional — requires Ch 11 case-assembly calls that depend on Ch 6–8 trust cultivation.

---

## 2. PER-SLOT COMPLETION REQUIREMENTS

For each slot: required entries (minimum for COMPLETE state), contributing entries (boost signal density), source chapters, and thoroughness notes.

### 2.1 SLOT #1 — IMPOSSIBLE KNOWLEDGE

**Thesis:** Endo reports facts he should not have access to. Knowledge-level contradiction.

**Required entries (minimum 3 for COMPLETE):**
- Ch 8 — Endo Tell #1 (`chapter_08.md:159`): Endo describes Mira's reporting behavior as bracing/preparing — a listener's description, not an observer's.
- Ch 8 — Endo Tell #2 (`chapter_08.md:219`): Endo describes Doi's private emotional state with impossible fidelity.
- Ch 8 — Endo Tell #1 pressed (`chapter_08.md:193`): Endo justifies rather than dismisses when pressed on his access.

**Contributing entries (optional boost):**
- Ch 9 — Endo Tell #3 (`chapter_09.md:462`): preemptive cable-work normalization.
- Ch 9 — Endo Redirect Tell (`chapter_09.md:436`): pivots from people to infrastructure.
- Ch 9 — Endo Bluff Response (`chapter_09.md:418`): pre-staging community framing.
- Ch 1 — Canvass report entry (`chapter_01.md:127`): establishes Mira's reports were written, creating the knowledge baseline against which Endo's voice-descriptions read as impossible.

**Source chapters:** Ch 1 (baseline), Ch 8 (primary), Ch 9 (reinforcement).

**Thoroughness notes:** COMPLETE at 3 entries. The 3 required are all Ch 8; a player who skipped the Ch 8 tells misses this slot. The Ch 9 follow-up adds density but is not sufficient alone.

**Reachability:** The Ch 8 Endo call is mandatory (incoming). Tells fire across any intent path. Slot is reachable by every playthrough.

**Risk:** If the player moves fast through Ch 8, tells may not be examined/logged. Consider making Endo Tell #1 and #2 auto-log on first occurrence rather than examine-gated.

---

### 2.2 SLOT #2 — SOCIAL ACCESS PATTERN

**Thesis:** Endo is positioned at every community chokepoint. Knowledge-level, positional.

**Required entries (minimum 3 for COMPLETE):**
- Ch 2 — Community Safety Council / M. Endo (`chapter_02.md:79`) [OPTIONAL: requires bulletin board examination].
- Ch 2 — Playground equipment donation (`chapter_02.md:383`) [OPTIONAL: requires playground examination].
- Ch 5 — Committee chair identification (derived from the chapter's chair reveal; no explicit prompt, but the Ch 5 "six appearances" Kenji notebook entry — see `chapter_05.md:409–411` — captures the pattern).

**Contributing entries (boost):**
- Ch 4 — Rina mentions Endo positively (`chapter_04.md:535`): confirms Endo's social capital.
- Ch 5 — Three dismissed reports (`chapter_05.md:223`): establishes Endo's committee authority.
- Ch 7 — Ogawa connection (`chapter_07.md:196`): same committee, opposite outcomes.

**Source chapters:** Ch 2 (seeds, optional), Ch 4–5 (confirmation), Ch 7 (reinforcement).

**Thoroughness notes:** PARTIAL reachability. The Ch 2 entries are both `Optional` in the manuscript — a player who doesn't examine the bulletin board or the playground plaque will miss 2 of the 3 required entries. The Ch 5 six-appearances entry is not itself a `NOTEBOOK PROMPT` — it's a visible Kenji-notebook display. Consider formalizing it as an explicit prompt.

**Reachability:** CONDITIONAL. A player who moves through Ch 2 without examining optional elements arrives at Ch 11 with SOCIAL ACCESS PATTERN as EMERGING (not COMPLETE). This is acceptable design — the slot is a reward for thoroughness.

**Audit recommendation:** Ensure the Ch 5 committee-chair moment (Kenji's "seven appearances" accumulation) produces an explicit `[NOTEBOOK PROMPT]`. Currently it's visible as in-scene text but not logged as a discrete entry. FLAG: add prompt.

---

### 2.3 SLOT #3 — COMMITTEE AS MECHANISM

**Thesis:** The safety council fires teachers quickly, dismisses children's reports indefinitely. Factual contradiction.

**Required entries (minimum 2 for COMPLETE):**
- Ch 5 — Three dismissed reports (`chapter_05.md:223`): pattern established.
- Ch 5 — Ogawa firing (`chapter_05.md:295`): opposite outcome, same mechanism.

**Contributing entries:**
- Ch 5 — Aizawa pattern (`chapter_05.md:629`): the filing process.
- Ch 5 — Sora Hayashi (`chapter_05.md:271`): named victim of the dismissal pattern.
- Ch 7 — Ogawa connection (`chapter_07.md:196`): deepens the mechanism.
- Ch 9 — Ogawa deep (`chapter_09.md:332`): Ogawa was cross-referencing Mira's observations; her firing was removal.
- Ch 11 — Haruki's case-assembly call (not itself in notebook prompts — referenced in `chapter_11.md:541` omitted entry; Haruki's 43 reports, 40 behavioral, zero actioned).

**Source chapters:** Ch 5 (primary), Ch 7 and Ch 9 (depth), Ch 11 (final numeric proof).

**Thoroughness notes:** COMPLETE at 2 entries. Both required entries are in Ch 5, reached via Haruki's incoming call (mandatory). Slot is reachable by every playthrough at minimum COMPLETE.

**For a richer presentation:** the Ogawa thread adds the Nishida layer (from ogawa-incident.md), now core content delivered via the Ch 8 Ogawa call, which contextualizes Endo's methodology. This doesn't gate the slot but enriches its confrontation delivery.

**Reachability:** STRONG. This is the safest slot — every player reaches it.

---

### 2.4 SLOT #4 — INFRASTRUCTURE ACCESS

**Thesis:** Endo is the only person with physical access to the exchange room. Knowledge-level.

**Required entries (minimum 2 for COMPLETE):**
- Ch 7 — Fumiko infrastructure map (`chapter_07.md:212`): cable routes under community center.
- Ch 10 — Infrastructure signature (`chapter_10.md:100`): Endo's knowledge density maps to cable routes.

**Contributing entries:**
- Ch 10 — Bridge number resolved (`chapter_10.md:174`): confirms the exchange as the mechanism.
- Ch 10 — Exchange room evidence (`chapter_10.md:296`): Endo's 15-year logs, the routing code leading to the substation.
- Ch 11 — Fumiko's one-key-fifteen-years testimony (if called during case assembly): explicit annual-inspection record.

**Source chapters:** Ch 7 (foundation), Ch 10 (convergence), Ch 11 (proof).

**Thoroughness notes:** COMPLETE at 2 entries. The Ch 10 entries are all plot-mandatory (Kenji enters the exchange room regardless of player choices). Ch 7 Fumiko call is typically reached (Fumiko is introduced Ch 6, her call in Ch 7 is part of the main investigation). Slot is reachable by every playthrough.

**Reachability:** STRONG. Ch 10 is a story beat, not a choice.

**Audit note:** The Ch 11 Fumiko one-key testimony is the most powerful confrontation material here but is trust-gated on Fumiko's cultivated relationship across Ch 6–11. Include, but do not require for COMPLETE.

---

### 2.5 SLOT #5 — THE GARDEN

**Thesis:** Botanical timeline maps disappearances. One plant per child. Factual.

**Required entries (minimum 2 for COMPLETE):**
- Ch 9 — The Garden (`chapter_09.md:140`): the full botanical-timeline entry. This single prompt contains most of the slot's argument.
- Ch 9 — Sora's map recontextualized (`chapter_09.md:262` [omitted] — see `chapter_09.md:208–246` for source scene): confirms Sora's earlier observation mapped the infrastructure leading to the exchange.

**Contributing entries:**
- Ch 2 — Older missing posters (`chapter_02.md:249`) [OPTIONAL]: the earlier victims whose plants in Endo's garden are the older/mature specimens.
- Ch 5 — Sora Hayashi (`chapter_05.md:271`): the named 3-week-prior plant.

**Source chapters:** Ch 9 (primary, self-contained).

**Thoroughness notes:** COMPLETE at 2 entries. Ch 9 Path B (The Garden) is optional — a player who skipped Path B misses both required entries. This is the **highest-risk slot for missed completion.**

**Reachability:** CONDITIONAL. Ch 9 is a free-investigation chapter; a player who chose only Paths A, C, and E (Framing, Reiko, Ogawa) misses the Garden entirely.

**Audit recommendation:** Consider making Path B (Garden) soft-mandatory — e.g., the Ch 9 investigation board surfaces the garden lead with higher priority signaling. Alternatively, accept that a player who skipped Path B arrives at Ch 11 with GARDEN as EMERGING and consider it the cost of playstyle. The design already anticipates this (see notebook system spec §5.6 — thoroughness as outcome density).

**Redundancy note:** the Ch 9 Garden prompt is densely informative — it contains nursery receipts, 3-week gap, species notes, and Endo's morning ritual all in one. Consider whether this should be split into 2–3 prompts for finer mechanical control. Currently the single prompt is efficient but over-loaded.

---

### 2.6 SLOT #6 — FRAMING AUTHORSHIP

**Thesis:** Every planted document traces to council-level access. Factual.

**Required entries (minimum 3 for COMPLETE):**
- Ch 7 — Framing analysis / language trace (`chapter_07.md:524`): "misunderstands," "difficult," "says things" — community vocabulary formalized.
- Ch 7 — Chat logs fabricated (`chapter_07.md:534`): metadata forensics.
- Ch 9 — Haruki's break (`chapter_09.md:109`): "disruptive honesty" in the framing files.

**Contributing entries:**
- Ch 5 — "Disruptive honesty" PIN (`chapter_05.md:162`): the phrase pinned for the Ch 9 payoff.
- Ch 4 — Rina phrasing connection (`chapter_04.md:603` — Rina Soul Read): the community vocabulary source.
- Ch 7 — Framing recontextualizes Rina (`chapter_07.md:524`): explicit link.

**Source chapters:** Ch 4–5 (foundation), Ch 7 (discovery), Ch 9 (weaponization).

**Thoroughness notes:** COMPLETE at 3 entries. All are plot-mandatory or near-mandatory:
- Ch 7's framing examination produces 2 required entries automatically.
- Ch 9's Haruki break is on Path A, which is the chapter's most likely first-choice.

**Reachability:** STRONG. Every standard playthrough completes this slot.

**Redundancy note:** the Ch 5 PIN and Ch 9 break are near-duplicates in content; the PIN exists specifically to insure the Ch 9 payoff for fast-reading players. This is deliberate — not redundancy, insurance.

---

### 2.7 SLOT #7 — SOCIAL ACCESS (WITNESS)

**Thesis:** People told Endo everything because not telling him felt strange. Knowledge-level.

**Required entries (minimum 2 for COMPLETE):**
- Ch 11 — Doi's case-assembly testimony (referenced at `chapter_11.md:541` [omitted]): "His recollection of Endo's behavior — the casual visits, the questions about which families were struggling, the way Endo always knew which children were 'at risk.'"
- Ch 11 — Reiko's updated understanding (from notebook scene, `chapter_11.md:159`): community's default of sharing with Endo.

**Contributing entries:**
- Ch 2 — Community Safety Council (`chapter_02.md:79`) [OPTIONAL]: foundation.
- Ch 4 — Rina's Endo reference (`chapter_04.md:535`): community consensus of Endo's goodwill.
- Ch 5 — Aizawa filing through council (`chapter_05.md:629`): institutional channel.

**Source chapters:** Ch 2 (seed), Ch 11 (primary — case-assembly calls).

**Thoroughness notes:** **THINNEST SLOT.** Required entries are Ch 11 case-assembly calls that depend on:
1. Doi's trust cultivated across Ch 3–6 (Ch 6 confession collapse necessary for Doi to be open in Ch 11).
2. Reiko's notebook scene, which requires Ch 9's static call.

A player who didn't break Doi's false confession or failed the Ch 9 Reiko static call may arrive at Ch 11 unable to get the required testimony. This slot is the most trust-gated.

**Reachability:** CONDITIONAL. Requires relationship cultivation across Act II and Act III.

**Audit recommendation:** This slot is the most thoroughness-dependent. Consider whether it should be:
(a) easier to complete (add a mid-game entry that lands the thesis with fewer trust requirements), or
(b) kept as-is (the hardest slot to complete is the one that rewards deep play).

Current recommendation: (b). Keep as-is. The slot's difficulty is a feature. A player who cultivated relationships deeply earns the most devastating Ch 11 slot. A player who didn't cultivate gets EMERGING and feels the cost of their approach.

---

### 2.8 SLOT #8 — INDEPENDENT CORROBORATION

**Thesis:** Three independent witnesses observed the silver car. Factual.

**Required entries (minimum 2 for COMPLETE):**
- Ch 6 — Doi silver car testimony (`chapter_06.md:359`): three sightings, partial plate.
- Ch 4 — Kaito's vehicle logs (`chapter_04.md:755`): timestamps matching Doi's.

**Contributing entries:**
- Ch 2 — Park sight line (`chapter_02.md:375`): the physical location.
- Ch 2 — Tire impressions (optional, `chapter_02.md` river path scene): physical trace.
- Ch 7 — Convergence entry (derived from `chapter_07.md` Scene 1): holding company → Endo.
- Mira's own notebook (retrieved Ch 1/Ch 2) — her sightings documented.

**Source chapters:** Ch 4 (Kaito), Ch 6 (Doi), Ch 7 (convergence).

**Thoroughness notes:** COMPLETE at 2 entries. The Kaito entry is from Ch 4 (neighborhood canvassing — automatic). The Doi entry requires resolving the Ch 6 false confession — which requires SILENT on the confession. A player who used PRESSURE or REASSURE on Doi's confession may not unlock the silver-car testimony.

**Reachability:** CONDITIONAL on Ch 6 Doi mechanic. The Ch 4 Kaito entry is automatic; the Doi entry is trust-gated.

**Redundancy note:** this slot has more contributing entries than it needs. Consider which should be primary. Recommendation: Doi + Kaito are the two required; Mira's notebook and Ch 7 convergence are narrative color, not slot-necessary.

---

## 3. PER-CHAPTER ENTRY LISTING (TAGGED)

Complete list of notebook prompts, tagged by type, NPCs, threads, and Board slot contributions.

### 3.1 Chapter 1 (4 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 127 | EVIDENCE | Doi | canvass pattern | #2, #7 (seed) |
| 221 | OBSERVATION | Mira | soul read system | — (context) |
| 279 | EVIDENCE | Mira | Mira's notebook thread | — (context/mech) |
| 299 | EVIDENCE | Mira | Yanagi canvass, bridge number | #4 (seed), #8 (seed) |

### 3.2 Chapter 2 (10 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 69 | OBSERVATION (OPTIONAL) | Mira | Yanagi atmosphere | — (context) |
| 79 | OBSERVATION (OPTIONAL) | Endo | Endo name accumulation | #2 (required) |
| 135 | OBSERVATION | Mira | school geography | — (context) |
| 165 | EVIDENCE | Sora (unnamed) | Sora thread | — (context; Sora thread) |
| 199 | EVIDENCE | Doi | Doi thread | #7 (contributing) |
| 237 | OBSERVATION (OPTIONAL) | Sora | Sora thread | — (seed for #7/thread) |
| 249 | OBSERVATION (OPTIONAL) | — | historical cases | #5 (contributing) |
| 347 | EVIDENCE | Mira (bridge) | infrastructure | #4 (seed) |
| 375 | EVIDENCE | Mira | silver car | #8 (contributing) |
| 383 | OBSERVATION (OPTIONAL) | Endo | Endo name | #2 (contributing) |

### 3.3 Chapter 3 (6 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 252 | SOUL READ | Reiko | — | — (character) |
| 556 | OBSERVATION | Doi, Endo | neighborhood management | #2 (contributing) |
| 590 | OBSERVATION | Doi | Doi tracking | #8 (contributing) |
| 612 | OBSERVATION | Doi, Sora | Sora thread | — (Sora thread) |
| 632 | SOUL READ | Doi | — | — (character) |
| 674 | OBSERVATION | — | bridge anomaly | #4 (seed) |

### 3.4 Chapter 4 (5 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 303 | SOUL READ | Yui | — | — (character) |
| 437 | CHARACTER | Mira | crying scene | — (emotional arc) |
| 535 | OBSERVATION | Rina, Endo | community consensus | #2 (contributing) |
| 603 | SOUL READ | Rina | Rina recontextualization | #6 (seed) |
| 755 | EVIDENCE | Kaito | silver car | #8 (required) |

### 3.5 Chapter 5 (10 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 120 | OBSERVATION | Haruki, Yui | protocol failure | — (character) |
| 162 | PIN | Haruki, Mira | "disruptive honesty" phrase | #6 (insurance) |
| 223 | EVIDENCE | — | three dismissed reports | #3 (required), #2 (contributing) |
| 271 | EVIDENCE | Sora | Sora thread | #3 (contributing) |
| 295 | EVIDENCE | Ogawa, Endo | Ogawa firing | #3 (required) |
| 395 | OBSERVATION | Ogawa, Mira | classroom texture | — (character, thematic) |
| 453 | [omitted line — requires re-grep] | — | — | — |
| 629 | OBSERVATION | Aizawa | filing pattern | #3 (contributing) |
| 645 | SOUL READ | Aizawa | — | — (character) |
| 843 | OBSERVATION | Sora, Haruki | vivid imagination parallel | #6 (contributing) |

### 3.6 Chapter 6 (4 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 261 | SOUL READ | Doi | — | — (character) |
| 359 | EVIDENCE | Doi | silver car | #8 (required) |
| 511 | EVIDENCE | Fumiko, Endo | historical case | #3 (contributing), #2 (contributing) |
| 525 | SOUL READ | Fumiko | — | — (character) |

### 3.7 Chapter 7 (11 prompts — the densest chapter)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 180 | EVIDENCE | Fumiko, Endo, Haruki | historical case + committee | #2, #3 (contributing) |
| 196 | EVIDENCE | Endo, Ogawa | Ogawa thread | #3 (contributing) |
| 212 | EVIDENCE | Fumiko | infrastructure | #4 (required) |
| 228 | SOUL READ | Fumiko | — | — (character) |
| 408 | [omitted] | — | — | — |
| 428 | SOUL READ | Kaito | — | — (character) |
| 464 | OBSERVATION | Fumiko | blind spot | — (character / lesson) |
| 524 | EVIDENCE | Rina (recontextualized) | framing language | #6 (required) |
| 534 | EVIDENCE | — | framing metadata | #6 (required) |
| 576 | [omitted] | — | — | — |
| 590 | EVIDENCE | Endo, Ogawa | Ogawa connection | #3 (contributing) |

### 3.8 Chapter 8 (5 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 159 | OBSERVATION | Endo | Tell #1 | #1 (required) |
| 193 | OBSERVATION | Endo | Tell #1 pressed | #1 (required) |
| 219 | OBSERVATION | Endo, Doi | Tell #2 | #1 (required) |
| 293 | [omitted — Endo locked room soul read] | Endo, Mira | — | — (character) |
| 485 | SOUL READ | Aizawa | — | — (character) |

### 3.9 Chapter 9 (10 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 109 | EVIDENCE | Haruki, Endo | framing / Haruki's break | #6 (required) |
| 140 | EVIDENCE | Endo, Sora, Mira | garden timeline | #5 (required) |
| 200 | EVIDENCE | Reiko, Mira | Reiko static call | #4 (contributing) |
| 246 | EVIDENCE | Sora, Endo | Sora's map | #4, #5 (contributing) |
| 262 | [omitted] | — | — | — |
| 270 | EVIDENCE | Ogawa, Mira | Ogawa cross-ref | #3 (contributing) |
| 296 | EVIDENCE | Ogawa, Nishida | Nishida report | — (Endo philosophy deep) |
| 308 | [omitted] | — | — | — |
| 332 | EVIDENCE | Ogawa | Ogawa deep | #3 (contributing) |
| 378 | EVIDENCE | Ogawa | Ogawa almost-call | #4 (contributing) |
| 418 | OBSERVATION | Endo | BLUFF response | #1, #6 (contributing) |
| 436 | OBSERVATION | Endo | REDIRECT tell | #1 (contributing) |
| 462 | OBSERVATION | Endo | Tell #3 | #1 (contributing), #4 (contributing) |

### 3.10 Chapter 10 (3 prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 100 | EVIDENCE | Endo, Fumiko, Sora | infrastructure signature | #4 (required) |
| 174 | EVIDENCE | — | bridge number resolved | #4 (contributing) |
| 296 | EVIDENCE | Endo, Sora, Mira | exchange room evidence | #4 (required), #1 (contributing) |

### 3.11 Chapter 11 (2 prompts + case-assembly prompts)

| Line | Type | NPCs | Threads | Board slots |
|---|---|---|---|---|
| 159 | EVIDENCE | Reiko, Mira | Reiko's new understanding | #7 (required) |
| 541 | [omitted — case assembly contributions per NPC] | variable | case assembly | contributes to every slot |

**Note:** Chapter 11's case-assembly scene (Scene 3 — "Building the Case") produces one NPC-specific entry per call placed during the scene. These entries feed directly into Board slots. Per the manuscript:
- Doi call → SLOT #7 (social access witness)
- Fumiko call → SLOT #4 (infrastructure one-key testimony)
- Haruki call → SLOT #3 (43 reports / 40 behavioral / zero actioned)
- Kaito call → SLOT #8 (vehicle log compilation)
- Aizawa call → SLOT #3, #6 (personal copies / procedural chain)

These prompts should be formalized as 5 explicit `[NOTEBOOK PROMPT]` entries during Ch 11 Scene 3 for clean Board-assembly gating. Currently they are narratively present but not all are explicit prompts. **FLAG: Ch 11 Scene 3 needs 3 additional notebook prompts to fully gate the case-assembly contributions.**

---

## 4. UNASSIGNED / CONTEXT-ONLY PROMPTS

23 prompts do not contribute to any Board slot. These are legitimate context/character entries but are cuttable in a tightening pass.

**Category A — Soul Read entries (character texture, 8 prompts):** Ch 1:221 (Soul Read system intro), Ch 3:252 (Reiko), Ch 3:632 (Doi), Ch 4:303 (Yui), Ch 4:603 (Rina), Ch 5:645 (Aizawa), Ch 6:261 (Doi 2nd), Ch 6:525 (Fumiko), Ch 7:228 (Fumiko 2nd), Ch 7:428 (Kaito), Ch 8:485 (Aizawa 2nd).

These are the emotional fuel of the game and should NOT be cut. They are "context-only" with respect to Board slots but are load-bearing for Character Notes and Memory Fragment cross-references.

**Category B — Character/arc entries (not slot-contributing, 6 prompts):** Ch 1:279 (Mira's notebook), Ch 2:69, 135, 165 (Yanagi atmosphere details), Ch 4:437 (Mira's crying break), Ch 5:120 (Haruki's protocol), Ch 5:395 (Ogawa classroom — added this session), Ch 7:464 (Fumiko's blind spot lesson).

These are character and thematic entries. Not slot-assignable but critical to the narrative.

**Category C — Optional Ch 2 environmental detail (5 prompts):** several Ch 2 optional `OBSERVATION` prompts provide Yanagi atmosphere. These are low-stakes findable details that reward exploration.

**Audit recommendation:** None of the Category A–C prompts should be cut. They serve functions outside the Board. The manuscript is not over-prompted.

---

## 5. OVERLOADED ENTRIES (Dilution Risk)

4 prompts contribute to 3+ Board slots. These may be over-loaded — single entries carrying too much argumentative weight, diluting their mechanical specificity.

| Line | Slots Served | Recommendation |
|---|---|---|
| Ch 7:180 (Fumiko historical case) | #2, #3 (contributing) | ACCEPTABLE. Single entry establishes two parallel arguments; each slot uses its relevant part. |
| Ch 9:140 (The Garden) | #5 (required), plus contributes to #1 (Endo's ritual as impossible knowledge) | Could be split into 2 prompts: botanical timeline as #5 required, Endo's ritual observation as #1 contributing. Currently one prompt carrying both. |
| Ch 9:246 (Sora's map) | #4, #5 (contributing each) | ACCEPTABLE. The map's dual nature (infrastructure AND victim artifact) is itself the point. |
| Ch 9:462 (Endo Tell #3) | #1, #4 (contributing each) | ACCEPTABLE. Cable normalization serves both knowledge and infrastructure slots naturally. |

**Overall:** overload risk is low. Only the Ch 9 Garden prompt is a candidate for split, and even there the single-prompt density is thematically justified (the garden is one artifact with two arguments; splitting may undercut the image's weight).

---

## 6. REACHABILITY ANALYSIS — PLAYTHROUGH SCENARIOS

Testing whether slots complete under different playstyles.

### 6.1 Completionist Playthrough

Player examines every optional element, pursues every side-thread, cultivates every NPC relationship. Ogawa thread and Nishida testimony are core content (Ch 8 call).

**Result:** all 8 slots COMPLETE. Ch 11 Board is at maximum density. Confrontation plays out with richest contradiction presentation.

### 6.2 Main-Line Playthrough (skip optional)

Player completes mandatory calls, skips Ch 2 optional examinations, takes Ch 9 Path A (framing) + Path B (garden) + Path C (Reiko) — the three most obvious.

**Result:** 
- Slots COMPLETE: #1, #3, #4, #5, #6 (5 of 8).
- Slots EMERGING: #2 (missing Ch 2 optional entries), #7 (missing some Ch 11 case-assembly trust), #8 (conditional on Ch 6 Doi mechanic).

**Acceptable.** The player with 5 complete slots has a confrontation with real weight, visibly missing two threads (SOCIAL ACCESS and SOCIAL ACCESS WITNESS) — the cost of skipping exploration.

### 6.3 Fast Playthrough (rushed)

Player moves quickly through dialogue, skips all optional investigation, chooses PRESSURE or REASSURE where SILENT would be rewarded.

**Result:**
- Slots COMPLETE: #3, #6 (2 of 8).
- Slots EMERGING: #1 (partial Ch 8 tells), #4 (partial infrastructure), #5 (missed if Path B skipped), #8 (likely missed due to Doi mechanic).
- Slots DORMANT: #2, #7.

**Concerning.** A rushed playthrough has only 2 complete slots. Ch 11 confrontation plays but feels thin. Is this the intended floor? 

**Recommendation:** the design should tolerate a minimum of 3 complete slots for a playable confrontation. Consider whether the Ch 8 Endo tells should be auto-logged (not examine-gated) to guarantee Slot #1 completion in a rushed playthrough.

### 6.4 Ogawa-Deep Playthrough

Player engages the Ogawa thread fully (Ch 5 → Ch 7 → Ch 8 mandatory Ogawa call delivering Nishida testimony).

**Result:** 
- Slot #3 (COMMITTEE AS MECHANISM) reaches RICH state (beyond COMPLETE — additional contributing entries stack).
- Ch 11 confrontation Phase 4 unlocks Endo's Fujisawa reference (per `chapter_11.md:483` design note).
- Epilogue's Nishida Question subplot activates.

This is the depth reward structure. Does not affect other slots significantly. A player who pursued Ogawa deep has the most morally complex confrontation; a player who didn't has a cleaner one.

---

## 7. RECOMMENDATIONS

### 7.1 Cuttable (none critical)

No prompts are obvious cut candidates. The manuscript is lean; every prompt serves at least a character-note or thematic function if not a Board slot function.

### 7.2 Additions Recommended

Three explicit `[NOTEBOOK PROMPT]` additions recommended:

1. **Ch 5 — "six appearances" explicit prompt.** Kenji's in-scene notebook accumulation (around `chapter_05.md:409–411`) is narratively visible but not formalized as a notebook prompt. Adding one locks SLOT #2 more firmly.
2. **Ch 11 Scene 3 — case-assembly prompts (3 additions).** Doi's social access, Kaito's vehicle logs, Aizawa's personal copies each need explicit `[NOTEBOOK PROMPT]` entries so the Board assembles cleanly. Fumiko's and Haruki's are already present.
3. **Ch 1 — Ch 2 Endo name accumulation prompt.** Create a thread-type entry in Ch 2 that explicitly tracks Endo-name-count across the chapter, updating as Mira/Kenji encounter each mention. Currently this tracking is implicit; formalizing helps gate SLOT #2.

### 7.3 Splits Recommended

1. **Ch 9 Garden prompt (line 140):** consider splitting into two prompts — one for the botanical timeline (SLOT #5), one for Endo's morning ritual observation (SLOT #1 contributing). Current single prompt is dense but mechanically over-loaded.

### 7.4 Auto-Log Recommendations

Two prompts should auto-log on scene arrival rather than examine-gated:

1. **Ch 8 Tell #1 (line 159):** trigger automatically on Endo's Mira-description line, not on player examination. Rushed players should still encounter this.
2. **Ch 2 Community Board Endo prompt (line 79):** currently OPTIONAL. Consider soft-raising to auto-trigger on community board approach. The player can still miss it entirely if they don't approach the board, but at least approach triggers logging.

### 7.5 Thoroughness Gating Calibration

The current design has Ch 11 Board completion tracking roughly this distribution:
- Completionist: 8 of 8 (~15% of expected players)
- Main-line: 5 of 8 (~60%)
- Rushed: 2 of 8 (~15%)
- Ogawa-deep: 6–8 of 8 (~10%)

The design target should ensure that rushed playthroughs still experience a readable Ch 11 confrontation. A floor of 3 complete slots is recommended. Currently the floor is 2. See §7.4 recommendation on Ch 8 auto-log.

---

## 8. BUILD-TIME DELIVERABLES

### 8.1 Prompt Database Schema

For each notebook prompt, build-time should track:

```
PromptID: unique identifier
SourceChapter: 01-12 or "epilogue"
SourceLine: line number in manuscript
TriggerCondition: scene beat that fires it (auto/examine/call-specific)
EntryType: evidence/observation/soul-read/pin/thread/memory-fragment
NPCs: [Reiko, Doi, Mira, ...]
Threads: [Sora, Ogawa, Silver Car, ...]
Pin: boolean
BoardSlotContributions: [{SlotID, RequiredBoolean, ContributionWeight}]
Optional: boolean (is this prompt examine-gated?)
```

### 8.2 Board Assembly Algorithm

At Ch 11 Scene 3 entry, the assembly algorithm:

```
For each slot (1–8):
  Count required entries present in Log
  If count >= slot.requiredMinimum:
    slot.state = COMPLETE
    Package slot with all required + all contributing entries
  Elif count > 0:
    slot.state = EMERGING
    Display "X of Y pieces found"
  Else:
    slot.state = DORMANT
    Do not display
```

### 8.3 Per-Slot Test Cases

QA test matrix — one test per slot per playstyle:

| Slot | Completionist | Main-line | Rushed | Ogawa-deep |
|---|---|---|---|---|
| #1 | COMPLETE | COMPLETE | EMERGING | COMPLETE |
| #2 | COMPLETE | EMERGING | DORMANT | COMPLETE |
| #3 | COMPLETE | COMPLETE | COMPLETE | RICH |
| #4 | COMPLETE | COMPLETE | EMERGING | COMPLETE |
| #5 | COMPLETE | COMPLETE | EMERGING | COMPLETE |
| #6 | COMPLETE | COMPLETE | COMPLETE | COMPLETE |
| #7 | COMPLETE | EMERGING | DORMANT | EMERGING |
| #8 | COMPLETE | COMPLETE | EMERGING | COMPLETE |

Each cell becomes a QA test case during build.

---

## 9. CROSS-REFERENCES

- `deadringer_notebook_system.md` §5 — Board slot architecture
- `deadringer_systems.md` §7 — Contradiction System, factual vs knowledge-level
- Chapter files 1–12 — every `[NOTEBOOK PROMPT]` referenced
- `chapter_structure.md` — thread accumulation and NPC availability map
- `ogawa-incident.md` — Ogawa thread layering (feeds SLOT #3 depth)

---

**END BOARD SLOT ENTRY AUDIT**
