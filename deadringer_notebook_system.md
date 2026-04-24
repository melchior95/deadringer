# DEAD RINGER — Notebook System Specification

Production specification for the game's central evidence-memory architecture. The notebook is Dead Ringer's replacement for the Phoenix Wright Court Record, Profile Tab, and Psyche-Lock system combined — and it carries more weight than any of those, because it is the only persistent interface the player has for twelve chapters of accumulated observation.

This document covers: the two-layer architecture, entry taxonomy, UI specifications, presentation mechanics, Ch 11 confrontation state, integration with adjacent systems, and open questions for implementation.

**Companion docs:**
- `deadringer_game_bible.md` — thesis, core mechanic loop, high-level notebook description
- `chapter_structure.md` — information economy, thread accumulation, NPC availability
- Chapter files (Ch 1–12, epilogue) — every `[NOTEBOOK PROMPT: ...]` is a generated entry

---

## 1. OVERVIEW

### What the Notebook Is

The player's in-game notebook is represented diegetically as **Kenji Oda's pocket notebook** — a physical paper notebook with a creased spine, established in the Chapter 1 cold open. Visual language: handwritten entries in Kenji's precise hand, tabs for sections, paper with wear across chapters. Not a database. Not a UI grid.

The notebook accumulates across the entire game. There is no "notebook reset" between chapters. Entries added in Ch 2 are still there in Ch 11.

### What It Replaces

The notebook consolidates four distinct Phoenix Wright UI elements into one artifact:

| Phoenix Wright | Dead Ringer equivalent |
|---|---|
| Court Record (evidence items) | Evidence entries in the Log |
| Profiles (character dossiers) | Character notes, auto-updating |
| Organizer (miscellaneous) | Observation entries |
| Psyche-Locks (hidden truths UI) | Soul Read entries + Break Mechanic per NPC |

**Critical difference:** PW never exceeds ~15 Court Record items per case. Dead Ringer generates roughly **40–60 notebook entries by Chapter 11**. The UI cannot treat every entry as equally prominent, equally presentable, or equally findable. That assumption is what breaks a naive port of the PW interface to this game.

### Design Principles

1. **Accumulation, not curation.** The player does not delete entries. Everything surfaced stays. The log is a record of what the investigation has seen.
2. **Density ≠ burden.** A player who explored deeply should not be punished with a harder-to-search notebook. The UI does the sorting; the player does the thinking.
3. **Pinned entries are rare and load-bearing.** When the game flags an entry with emphasis, that emphasis must be trustworthy. If everything is emphasized, nothing is.
4. **Ammunition is earned, not present.** The notebook stores observations. The confrontation uses assembled contradictions, which the Board builds from those observations. The player reads entries; the game packages them for use.
5. **Search beats memory.** A player who remembers "didn't Aizawa say something about the prior school?" in Ch 10 should be able to find it in one interaction. Full-text search is a feature, not a convenience.

---

## 2. TWO-LAYER ARCHITECTURE

The notebook has two distinct UI layers that serve different functions. The player sees Layer 1 in every chapter. Layer 2 appears only at specific moments.

### Layer 1: THE LOG (Persistent, Always Available)

Every notebook prompt the game surfaces becomes a Log entry. The Log is:
- **Read-only** (the game creates entries; the player doesn't edit)
- **Searchable** (free-text across all entries)
- **Filterable** (by NPC, chapter, entry type, pinned state)
- **Organized** (into sections — see §4)
- **Persistent** (no entry is ever removed, even if superseded or recontextualized)

The Log is accessed via a pocket-notebook icon on the main UI, available in any non-modal scene (investigation, between calls, after a memory fragment resolves). During calls, a compact version is available — see §6.

### Layer 2: THE BOARD (Contextual, Chapter 11 Primary)

The Board is a curated confrontation interface that surfaces only in specific story states — primarily Chapter 11's confrontation with Endo, with preview states in Ch 10 and usage states in Ch 12.

The Board is:
- **Assembled** from Log entries the player has accumulated (not separately authored)
- **Slot-based** (6–8 slots, each representing an evidence chain)
- **Presentable** (individual slots can be "played" during confrontation phases)
- **Gated by thoroughness** (slots require specific entry combinations to be complete)
- **Ephemeral** (the Board exists during confrontation moments; when the scene ends, it dissolves back into the Log)

The Board is the game's replacement for the "Present Evidence" button in Phoenix Wright. But where PW presents a single evidence item against a single testimony statement, Dead Ringer presents a packaged evidence chain against a redirection. The unit of confrontation is different.

### How They Relate

```
    THE LOG (always)                 THE BOARD (Ch 11)
    ─────────────────                ──────────────────
    40-60 entries                    6-8 slots
    All chapters                     Assembled from Log
    Read-only                        Presentable
    Searchable                       Gated by completion
    Persistent                       Ephemeral
                    ↓ assembles →
```

A Board slot does not create new content. It *references and packages* Log entries into a contradiction that can be deployed against Endo. If the Log has the necessary entries, the slot is complete and presentable. If not, the slot is visible but incomplete — the player sees what they would have had, and why they don't have it.

---

## 3. ENTRY TAXONOMY

Every notebook entry has a type. The type determines visual treatment, filterability, and how the entry participates in Board assembly.

### 3.1 Entry Types

**EVIDENCE** — physical findings. Phone numbers, documents, receipts, physical artifacts. Visual: handwritten note with a small icon indicating physical source. Examples: the bridge number (Ch 2), nursery receipts (Ch 9), Endo's monitoring logs (Ch 10).

**OBSERVATION** — character-level or environmental patterns. Things Kenji notices, audio signatures, behavioral tells. Visual: prose note, no icon. Examples: Endo's measured three-second rests (Ch 8), Aizawa's sanitizer click rate (Ch 5), Haruki's pen-click tell (Ch 5).

**SOUL READ** — Mira's impressions of a person or space. Stored separately because they are subjective — not proof, but often the key to interpreting other entries. Visual: italicized quote from Mira, attribution line ("Mira's read — Ch X"). Examples: Reiko "pressure, fracture, love shaped wrong" (Ch 3), Doi's confession "like a room where every radio is on a different station" (Ch 6), Endo's locked room (Ch 8).

**CHARACTER NOTE** — accumulating dossier. Each NPC has one, auto-updating as entries referencing them arrive. Visual: a profile page, reachable from any entry tagged with the NPC's name. Summary of known traits + a list of linked entries.

**PIN** — flagged by the game as "remember this." Entries in this class have visual emphasis (boxed, marked with a small star, or distinct paper color). These are rare. The manuscript currently has roughly 3–4 entries per act flagged as PIN-worthy. Example: "disruptive honesty" (Ch 5).

**CONTRADICTION** — a tagged relationship between two or more entries that reveals a logical inconsistency. Contradictions are generated automatically when the entries are all present. Visual: a linking line between source entries on the Log view; its own compact summary card.

**MEMORY FRAGMENT** — a separate entry class for the three interactive Mira-POV scenes (Reiko Denial, Rina Social Distortion, Aizawa Procedure). Each fragment is logged with the entries it produced. Visual: distinct full-page entry with a "MEMORY" header.

**THREAD** — meta-entry representing a narrative line the player has been following (Sora's artifacts, the Ogawa incident, the silver car). Threads auto-assemble from tagged entries. Visual: a tab group or a filter, not a standalone entry.

### 3.2 Entry Lifecycle

```
  [Game scene surfaces prompt]
              ↓
     [Log entry created]
              ↓
     [Tagged: chapter, NPC(s), thread, type]
              ↓
     [Character notes updated if NPC tagged]
              ↓
     [Threads reassembled if thread tagged]
              ↓
     [Contradiction check: does this complete any?]
              ↓
     [Board assembly check: does this complete any slot?]
              ↓
         [Persistent]
```

An entry, once created, is never deleted. It may be:
- **Updated** (e.g., the bridge number entry in Ch 2 is "unknown format"; in Ch 10 it becomes "routing address, old exchange junction" — the entry gains an annotation, not a replacement)
- **Linked** (a Ch 2 entry about Sora's graph paper map fragment links to the Ch 5 entry naming Sora and the Ch 10 entry confirming the map's infrastructure match)
- **Recontextualized** (a Ch 4 entry about Kaito as a suspect gets a later note when Ch 7 recontextualizes his notebooks as observation)

### 3.3 Tagging Schema

Each entry carries:
- **Chapter** (auto, based on when surfaced)
- **NPC tags** (zero, one, or multiple — e.g., an entry about the Yui report might tag Yui, Haruki, and Mira)
- **Thread tags** (optional — Sora thread, Ogawa thread, Silver Car thread, etc.)
- **Type** (from §3.1)
- **Pin flag** (boolean)
- **Location tag** (optional — the bench, the bridge, the exchange room, etc. — for cross-reference with `deadringer_locations.md`)

Tags are the basis for filtering (§4.2) and Board assembly (§5.4).

---

## 4. LAYER 1 — THE LOG (UI Specification)

### 4.1 Default View

When the player opens the notebook, they see Kenji's pocket notebook open to a view of recent entries. The default view is:
- **Reverse chronological** (newest first)
- **Current chapter entries** highlighted; older entries more muted
- A small tab strip at the top with section shortcuts (ALL / PEOPLE / EVIDENCE / READS / PINNED / THREADS)

The page texture, the handwriting, the lamp-lit warmth of Kenji's desk — these are the visual register. The UI is a notebook, not a dashboard. Scrolling the page is a physical flip rather than a scroll bar.

### 4.2 Sections & Filters

Entries can be filtered by:

| Filter | Purpose |
|---|---|
| **ALL** | Default, reverse-chronological, every entry |
| **PEOPLE** | Entries grouped by NPC. Each NPC has their own page with a summary + linked entries |
| **EVIDENCE** | Only EVIDENCE-type entries, organized by chapter found |
| **READS** | Only Soul Read entries, chronological. Mira's voice is visually distinct |
| **PINNED** | Only entries flagged by the game. Usually 5–8 items by Ch 11 |
| **THREADS** | Sub-grouped: Sora, Ogawa, Silver Car, Exchange Infrastructure, Endo, etc. |

Filters compose: PEOPLE + a search for "car" shows every NPC's car-related entries.

### 4.3 Search

Full-text search across all entries. Search results highlight the matched phrase. Common failure modes to design around:
- Misspelled searches (fuzzy match within reason)
- Partial phrase matches (substring matching, not word-boundary only)
- Tag-based searches (searching "endo" returns every entry tagged with Endo, not just entries containing the literal string "endo")

### 4.4 Re-Read / Context Restoration

Every entry has a "GO TO SOURCE" affordance — clicking it rewinds to the scene beat where the prompt originally fired. Restricted: it doesn't allow gameplay replay, only text restoration. The player reads the original scene, reads the prompt in context, returns to the notebook.

This matters because Dead Ringer's prompts are often elliptical. The Ch 2 prompt "Bridge number — scratched in concrete, south wall, old format (pre-1986 prefix?)" means more if the player can re-read the scene where Kenji found it, Mira's commentary, and the specific atmosphere of the bridge underside. Re-read capability is what makes a dense notebook interpretable.

### 4.5 Evolution Across Chapters

The Log's visible state changes over the game's arc. Production should render this as a physical notebook filling up:

| Chapter | Log State (approximate entry count) |
|---|---|
| Ch 1 | 2–3 entries. The notebook is mostly empty. One PIN (the fact that Mira exists). |
| Ch 2 | 8–15 entries depending on player thoroughness. First sections emerge. |
| Ch 4 | 20–25 entries. Character notes populating. First threads (Sora, Silver Car) assembling. |
| Ch 7 | 30–40 entries. Threads visibly cross-referenced. First contradictions emerging. |
| Ch 9 | 45–55 entries. Evidence density peaks. The Ogawa thread may or may not be full depending on player depth. |
| Ch 11 | 50–60 entries. The Board assembly begins. |
| Ch 12 | 55–65 entries. Final entries from switchboard duel. |

Physical rendering: the notebook gets visibly fuller. Pages are tabbed. The cover shows handling wear. By Ch 11, it looks like a case file.

### 4.6 Mira's Blue Notebook (Distinct Artifact)

**Important distinction for the UI team.** The player's notebook = Kenji's pocket notebook. Separately, Mira's own observation notebook (the blue one with patterned cover, recovered from the evidence box in Ch 2) is a distinct artifact that lives *within* the Log as a special evidence item.

Mira's notebook has its own reading interface — when opened, it shows her handwriting, her entries (including the Ogawa classroom entries added in Ch 5, the back-of-notebook personal entries revealed in Ch 11, the case-relevant observations Reiko reads in Ch 11). It is referenced in confrontation as its own presentable item, not as part of Kenji's notebook proper.

This matters for the Ch 11 notebook scene with Reiko: Reiko reads *Mira's* notebook, not Kenji's. The UI should make this legible — a different artifact, a different handwriting, a different register.

---

## 5. LAYER 2 — THE BOARD (Confrontation Architecture)

### 5.1 What the Board Is

The Board is a confrontation-specific interface. Think of it as Kenji's desk during the Ch 9 free-investigation chapter — evidence spread out, threads pinned, connections drawn between items. When the player enters the confrontation state, the notebook opens to the Board view rather than the Log view.

The Board consists of 6–8 slots. Each slot represents a packaged evidence chain — a specific line of argument against Endo, assembled from multiple Log entries. A complete slot is a contradiction that can be presented. An incomplete slot is a visible reminder of what the investigation nearly had.

### 5.2 The Eight Slots (Provisional)

Based on the Ch 11 confrontation as written, the Board should have roughly these slots. Exact composition is a design decision that should be finalized alongside Ch 11 playtesting.

| # | Slot | What It Argues | Source Entries (approximate) |
|---|---|---|---|
| 1 | **IMPOSSIBLE KNOWLEDGE** | Endo knows things with the wrong resolution | Ch 8 Tell #1, Ch 9 Tell #3, Mira's notebook cross-ref, written-vs-heard distinction |
| 2 | **SOCIAL ACCESS PATTERN** | Endo positioned at every chokepoint | Community board (Ch 2), pharmacy notice (Ch 2), playground plaque (Ch 2), council chair role (Ch 5), committee dismissal pattern (Ch 5) |
| 3 | **COMMITTEE AS MECHANISM** | Same committee, opposite outcomes for teachers vs. reports | Three dismissed child reports (Ch 5), Ogawa firing (Ch 5), Haruki's committee records (Ch 11 assembly) |
| 4 | **INFRASTRUCTURE ACCESS** | Endo is the only person with exchange-room access | Fumiko's infrastructure map (Ch 7), cable route analysis (Ch 10), the one-key annual inspection (Ch 11 assembly via Fumiko) |
| 5 | **THE GARDEN** | Botanical timeline maps disappearances | Nursery receipts (Ch 9), three-week gap (Ch 9), Sora+Mira plantings (Ch 9) |
| 6 | **FRAMING AUTHORSHIP** | Every planted document traces to council-level access | Counselor notes fabrication (Ch 9), chat log metadata (Ch 9), behavioral report formatting (Ch 9), "disruptive honesty" phrase match (Ch 5+Ch 9) |
| 7 | **SOCIAL ACCESS (WITNESS)** | People told Endo everything because not telling felt strange | Doi's testimony (Ch 11 assembly), Reiko's community interactions (Ch 11) |
| 8 | **INDEPENDENT CORROBORATION** | Silver car sightings from three unconnected witnesses | Doi (Ch 6), Kaito's logs (Ch 7), Mira's notebook (retrospective via evidence box) |

Each slot requires a minimum number of source entries to become "complete." The exact thresholds are a design tuning parameter.

### 5.3 Slot States

Each slot has one of four states:

1. **DORMANT** — the player has none of the source entries. Slot not visible yet.
2. **EMERGING** — the player has some source entries. Slot visible, labeled, greyed out, with a count ("3 of 5 pieces found").
3. **COMPLETE** — all source entries present. Slot presentable. Highlighted.
4. **PRESENTED** — the slot has been deployed during confrontation. Visual state changes (played, checkmark, or burned-match icon — tonal choice).

The EMERGING state is important. It tells the player what they *could have had*. A player who skipped Ch 9's garden path sees Slot #5 grey out in the Ch 11 Board — "THE GARDEN: 2 of 3 pieces found (missing nursery receipts)." That's the cost of thoroughness, made visible.

### 5.4 Assembly Logic

The Board assembles automatically at the start of Ch 11. The game checks every slot against the Log's entries, resolves each slot's state, and renders the Board. The player enters the confrontation with the Board pre-assembled.

No player action is required for assembly. This is deliberate: the assembly represents Kenji organizing what the investigation found, which is his job as a detective. The player's job is to *present* the assembled contradictions, not to manually collate them. Manual collation would be tedious and would trivialize an entire chapter's worth of investigation into a mini-game.

### 5.5 Presentation Mechanic (Confrontation Phases)

The Ch 11 confrontation has five phases (as written in the manuscript). Each phase has a topic — what Endo is currently discussing — and only certain Board slots are presentable during that phase. The player's task is:

1. Read Endo's redirection.
2. Identify which Board slot contradicts the redirection.
3. Present that slot.
4. Watch Endo adjust.

Critical design point: **presenting a complete slot does not "win" the confrontation.** It advances the phase. Endo redirects in a different direction. The player maps his boundary by watching where he redirects *to*, not by cracking him.

Presenting an incomplete slot is a failure state — Endo redirects around the weakness and the slot is marked "BLUNTED" (not burned — it remains on the Board, but cannot be deployed again in this confrontation).

Failure to present anything during a phase (the player is stuck or loses the thread) produces a different failure mode: Endo takes the conversational initiative and the phase advances on his terms. This is not game-over. It shifts the post-confrontation state — the case against Endo is still built, but some avenues (certain NPC testimonies, certain legal cooperation) are weaker in Ch 12.

### 5.6 Thoroughness Gating (Outcome Density)

A player who completed every chapter's optional content and pursued the deep Ogawa thread enters Ch 11 with 7 or 8 complete slots. A player who moved through the main line has 4 or 5 complete. A player who missed key investigative beats has 3.

The confrontation plays through all five phases regardless. But the *density* of what the player can present affects:
- The specificity of Endo's final statement (more complete slots = more specific admissions of philosophy, not guilt)
- Post-confrontation NPC state in Ch 12 (some NPCs respond to the visible strength of the case when Endo calls them to pressure)
- The epilogue's outcomes (particularly the Nishida Question — gated on Ogawa deep thread)

The Board is the game's primary record of how seriously the player took the case. It is not a score. It is an index of attention.

---

## 6. IN-CALL COMPACT NOTEBOOK

During phone calls, the full Log is too large to display. A compact version of the notebook is available via a small icon on the call UI.

### 6.1 What the Compact View Shows

- **Current NPC's character note** (auto-pinned at top)
- **Recent entries** (last 5–10, reverse-chronological)
- **Pinned entries** (always available)
- **Search** (available but compressed)

The player can consult but cannot leave the call. Entering the compact notebook does not pause the call. If the NPC is actively speaking, the player hears it through the notebook view.

### 6.2 Intent Teaching Integration

The compact notebook displays, for the current NPC, any "intent lesson" the player has learned — for example, "Silence works on Yui" after the Ch 4 Yui call. These lessons are derived from Character Notes and help players self-correct within a call.

Intent lessons should be phrased as observations, not imperatives:
- Good: "Pressure produced defensiveness. Silence let her fill the space."
- Bad: "USE SILENCE."

The notebook is a reference, not a coach.

---

## 7. INTEGRATION WITH ADJACENT SYSTEMS

### 7.1 Soul Read → Notebook

When Mira completes a Soul Read, the game surfaces a SOUL READ-type entry. The entry captures:
- The NPC read
- Mira's impression (verbatim)
- Kenji's annotation if any
- The chapter and call context

Soul Read entries are visually distinct (italicized, attributed to Mira). They accumulate as a separate filter in the Log. In the late game (Ch 10+), the player can look back at early Soul Reads to notice the degradation curve in Mira's language.

### 7.2 Memory Fragments → Notebook

After each of the three Memory Fragments resolves, a MEMORY FRAGMENT entry is logged. The entry is:
- A page with its own full-page presentation (not a one-line prompt)
- Includes the key line from the fragment (Reiko's denial, Rina's claim, Aizawa's filing)
- References any Log entries the fragment confirms or complicates

Memory Fragment entries are not presentable against Endo. They are evidence of experience, not evidence of fact. The player cannot use "I was there when Reiko dismissed me" as a contradiction — it's not admissible by the game's own logic. But the Fragments inform the player's understanding of every Reiko/Rina/Aizawa entry that follows.

### 7.3 Call System → Notebook

Notebook entries are primarily created by `[NOTEBOOK PROMPT: ...]` directives in the manuscript. These fire:
- During calls (at moments of information exchange)
- After calls (Soul Read entries, summary observations)
- During physical investigation (Ch 2 exploration, Ch 9 garden visit, Ch 10 exchange room)
- After Memory Fragments

The call UI should surface a small "entry added" animation when a prompt fires during a call, without interrupting the call. The player sees that the notebook has grown, without having to stop listening.

### 7.4 Intent System → Notebook

Intent choices produce Character Note updates rather than new Log entries. When the player uses PRESSURE on Doi and it fails, Doi's Character Note accumulates: "Responds to pressure with escalating politeness. Dignity Filter active." This is the kernel of the intent diagnosability the PW-hybrid analysis called for.

The Character Note's "What works with X" section should populate organically across the game — not a list the player writes, a list the game observes.

---

## 8. PLAYER EXPERIENCE FLOW

A compressed walkthrough of how the notebook feels across the arc.

### Act I (Ch 1–3)

The notebook is a teaching tool. Ch 1 surfaces one or two entries and demonstrates the system. Ch 2 is the first high-density chapter — the player explores Yanagi and logs 8–15 entries depending on thoroughness. Ch 3 introduces Soul Reads as their own filter.

By the end of Act I, the notebook has roughly 15–20 entries. Sections have emerged. The player has made one or two "wait, I remember logging that" cross-references.

### Act II (Ch 4–7)

Density accelerates. Characters accumulate notes. Threads become visible. The first PIN entries arrive (the "disruptive honesty" entry in Ch 5 is the most explicit example). Cross-references become common.

Around Ch 6, the player should notice that the notebook is getting dense enough to warrant search. Around Ch 7, the first contradictions become visible in the Contradictions filter.

### Act III (Ch 8–10)

The investigation converges. Entries tagged with Endo multiply. Infrastructure tags begin connecting previously-unrelated entries (the bridge number from Ch 2 links to the cable map from Ch 7 links to the exchange room in Ch 10).

Mira's degradation becomes visible in the Log: the Soul Read filter shows entries getting shorter, more elliptical. The Ch 10 amplification produces an unusually rich read entry that contrasts with the surrounding thin ones. This is legible to the player who looks.

### Act IV (Ch 11–12)

The Board assembles at Ch 11's start. The player sees it for the first time. Complete slots are highlighted; emerging slots are visible and annotated. The confrontation deploys the Board.

In Ch 12, the Board state carries forward. Slots that were presented are "consumed"; slots that were blunted remain visible but unusable. The switchboard duel adds one final set of real-time entries (Mira's intercepts of Endo's calls — short fragments, high-impact, logged in real time as they happen).

### Epilogue

The notebook is visible in Kenji's apartment in the Epilogue — on the desk, closed, with a bookmark. It has weight. The game does not ask the player to open it again. Its job is done.

---

## 9. ACCESSIBILITY & QUALITY-OF-LIFE

### 9.1 Core Requirements

- **Full-text search** across all entries
- **Tag filtering** composable with search
- **Keyboard navigation** (arrow keys between entries, enter to open, escape to close)
- **Context restoration** ("go to source" from any entry)
- **Readable at arm's length on mobile** (if the game ships mobile)
- **Autosave** — the notebook state persists across save/load transparently

### 9.2 Optional/Deferred

- **Player annotations** (the player adds their own notes to entries) — interesting but risks breaking the "Kenji's notebook" diegetic frame. Defer.
- **Export to text** (copy the notebook as a plaintext file) — nice-to-have, relevant for fan communities. Defer.
- **Thoroughness indicator** (a progress bar showing how many optional items the player has found per chapter) — useful for completionists, potentially spoilery. Decide at playtest.
- **Re-read from notebook without leaving current scene** — technically possible, emotionally risky (re-reading Mira's Ch 3 dismissal scene during Ch 11's confrontation might be more than some players want). Decide at playtest.

### 9.3 Spoiler-Risk Decisions

Two design decisions have spoiler implications:

1. **Emerging slots in Ch 11 Board.** Should the player see slots they haven't completed (with "X of Y pieces found" annotations)? Pro: shows the cost of thoroughness; respects player intelligence. Con: reveals that Endo is the confrontation subject before the confrontation begins (the slots are labeled with their arguments). Mitigation: reveal the Board at the start of Ch 11 Scene 3 (the call board — "BUILDING THE CASE"), not earlier.

2. **Thread visibility.** When the player opens the THREADS filter in Ch 3, should they see "Sora Thread (3 entries logged)" even though Sora hasn't been named? Pro: teaches the player that there are threads. Con: tells the player Sora is important before the game intends them to know. Recommendation: name threads only after they're named in-game. Ch 3: thread is "Bench Artifact." Ch 5 after Sora is named: thread renames to "Sora Thread." The rename is the reveal.

---

## 10. OPEN QUESTIONS / DECISIONS DEFERRED

These are design questions that need build-time resolution. None block the systems spec; all will need tuning against actual playtest.

1. **Exact slot count and composition for the Board.** Proposed 8 above; playtest will show whether 6 is cleaner (less overwhelming) or 10 is richer (more differentiation per playthrough).
2. **Presentation failure penalty.** Blunting a slot is the current proposal. Alternative: no penalty, the phase just advances on Endo's terms. Playtest.
3. **Whether Ch 12 adds new slots or only burns existing ones.** Proposal: Ch 12 adds real-time intercept entries but no new Board slots. The case against Endo closed at Ch 11. Ch 12 is a different fight (the switchboard duel is for Sora and Mira, not Endo).
4. **How much the notebook "knows" about itself.** The compact notebook's intent lessons ("Pressure produces defensiveness on Doi") cross a design line — at what point does the notebook stop being Kenji's and start being the game's? Playtest whether those lessons feel like observations or coaching.
5. **Mira's notebook visibility.** Full access from Ch 2 (when recovered), or gated until Ch 11 (the notebook scene with Reiko)? Proposal: partial access Ch 2 onward — Kenji reads her case-relevant entries for investigation; the personal entries (back of notebook) revealed only when earned. Reiko reads the full notebook in Ch 11.

---

## 11. CROSS-REFERENCES

Every `[NOTEBOOK PROMPT: ...]` in the manuscript maps to a Log entry under this spec. A follow-up pass should:

1. Audit all `[NOTEBOOK PROMPT]` directives across Ch 1–12 and the epilogue.
2. Classify each by type (§3.1).
3. Tag with NPCs, threads, location.
4. Assign to one or more Board slots (§5.2).
5. Verify the Ch 11 Board is reachable by any reasonable playthrough (no slot requires content the player cannot earn through the main line).

That audit is the practical next step after this spec is approved. It will surface:
- Over-tagged entries (appearing in too many slots, diluting their weight)
- Under-tagged entries (not contributing to any slot, possibly cutable)
- Slot completion paths (which chapters must be played thoroughly to complete which slots)

---

## APPENDIX: QUICK REFERENCE

**Architecture:** Two layers — Log (persistent, 40–60 entries) and Board (confrontation-only, 6–8 slots).

**Diegetic frame:** Kenji's pocket notebook (the player's) + Mira's blue notebook (a special evidence artifact within).

**Entry types:** Evidence, Observation, Soul Read, Character Note, Pin, Contradiction, Memory Fragment, Thread.

**Confrontation unit:** The packaged evidence chain (a Board slot), not the single evidence item. Presenting a slot advances the phase and maps Endo's boundary; it does not crack him.

**Thoroughness is the stake:** the number of complete slots at Ch 11 is the game's record of how seriously the player investigated. Not a score. An index of attention.

**The notebook is Dead Ringer's single most load-bearing UI.** Specify it tightly. Playtest it ruthlessly. Everything else can be softer. Not this.

---

**END NOTEBOOK SYSTEM SPECIFICATION**
