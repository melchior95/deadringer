# Higashino-Lens Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Implement all six Higashino-lens narrative enhancements across Dead Ringer's manuscript — emotional asymmetry, hidden acts of love/selfishness, cost of truth, Mira's Yui-sequence recontextualization, and Endo's selective truth sharpening.

**Architecture:** Two design documents feed into one manuscript pass. Changes layer onto existing scenes (break mechanics, call boards, notebook prompts, evidence chains) rather than creating new chapters. Character bible updated per character after manuscript changes land. Chapter structure updated last to reflect new information gates.

**Source designs:**
- `docs/plans/2026-04-28-higashino-lens-emotional-asymmetry-design.md` (Points 1, 2, 4)
- `docs/plans/2026-04-28-higashino-lens-selective-truth-mira-recontextualization-design.md` (Points 3, 5, 6)

---

## Implementation Order

The tasks are ordered by narrative chronology — earliest chapter changes first — so that later tasks can reference earlier planted evidence. Cross-cutting concerns (character bible, chapter structure) come last.

---

### Task 1: Mira Recontextualization — Yui-Sequence Foundation (deadringer_characters.md)

**Files:**
- Modify: `deadringer_characters.md` — Mira's character section

**Why first:** The Yui-report sequence is the deepest structural change. Establishing it in the character bible first creates the authoritative reference for all chapter-level changes.

**Step 1: Add Yui-sequence section to Mira's character entry**

After the existing "MIRA'S FALLIBILITY" section (~line 119), add a new section: **THE YUI SEQUENCE — WHAT THE PLAYER LEARNS LAST**

Content should establish:
- Mira's first report to a teacher was about Yui — predates every other report in her file
- The "disruptive" classification originated from the Yui report fallout (teacher called Yui's mother, mother told the boyfriend, things got worse, Mira flagged for "causing disruption to a family situation")
- Every subsequent report entered the system already tagged by the first classification
- Mira didn't understand this connection — she thought the problem was herself
- The player discovers the institutional sequence through investigation (Ch 5-9) and the emotional truth through the notebook's first entry (Ch 11)

**Step 2: Update Mira's crying scene context**

In the existing crying scene section (~line 144), add a design note referencing the new layer: the player who has already discovered the Yui-report dates from school records hears "I thought there was something wrong with me" differently — Mira was wrong about the variable. It wasn't her intensity. It was her compassion.

**Step 3: Commit**

```
git add deadringer_characters.md
git commit -m "Add Yui-sequence recontextualization to Mira's character bible"
```

---

### Task 2: Haruki's Hidden Acts + Yui-Sequence Evidence Seeding (chapter_05.md)

**Files:**
- Modify: `chapter_05.md` — Haruki's call, school records investigation

**Context:** Ch 5 is where Haruki enters the game, provides school records, and the institutional investigation begins. This chapter needs:
1. Haruki's hidden act of selfishness (the "disruptive" phrase — already partially present at line 94/162)
2. Haruki's hidden act of love (the recommendation letter — same school file, discovered alongside the phrase)
3. Yui-sequence evidence seeding (dates showing Mira's earliest reports were about Yui, the behavioral classification origin)

**Step 1: Sharpen existing "disruptive honesty" content as hidden act of selfishness**

The phrase and its origin are already in the manuscript (lines 94, 162). Sharpen the notebook prompt at line 162 to make explicit that Haruki's language became the institutional category — not just a label but the vocabulary the school used to process every subsequent Mira report. Add a design note that this connects to the companion Higashino design: Haruki's hidden act of selfishness.

**Step 2: Add the recommendation letter discovery**

During the school records investigation section (after the behavioral file review), add a beat where Kenji finds a second document in Mira's file: Haruki's formal recommendation for an enrichment program. Written with specific examples of Mira's observational skills. Filed. Nothing happened. The player finds the "disruptive" framing and the advocacy back to back — same teacher, same file. The institution took the framing and ignored the support.

Add notebook prompt: "HARUKI — RECOMMENDATION: Formal recommendation for Mira for enrichment program. Specific praise for observational precision. Filed same term as 'disruptive honesty' classification. Institution used the label, ignored the support. Same teacher wrote both."

**Step 3: Seed the Yui-sequence dates**

In the school records section, add evidence that surfaces the chronology:
- A behavioral report date showing Mira's earliest flagged report predates the silver car/Endo observations
- The earliest report's subject line or summary references "disruption to a family situation" (not Endo, not the silver car — a domestic concern)
- Haruki's testimony should include an offhand mention: something like "Her first report was before my time — I inherited the file. The initial flag was... not about what you'd expect. Not about any of the things she's known for reporting."

The player who tracks dates notices the sequence but doesn't yet have Mira's voice for it. That comes in Ch 11.

Add notebook prompt: "MIRA — REPORT CHRONOLOGY: Earliest behavioral flag in Mira's school file predates silver car reports by 8+ months. Initial classification: 'disruption to a family situation.' Not Endo. Not surveillance. A domestic concern. Every subsequent report — silver car, man near school, behavioral patterns — entered the system tagged by this original classification. The 'disruptive' label was built BEFORE Mira started reporting what killed her."

**Step 4: Integrate with Haruki's confrontation/break**

Update the confrontation integration to reflect the design: when the player presents the school file, Haruki recognizes his own language. The cost arrives quietly — his most careful, most professionally responsible contribution taught the institution how to dismiss Mira. If Haruki's break scene is in Ch 9 (per chapter_structure.md), add a forward reference design note here.

**Step 5: Commit**

```
git add chapter_05.md
git commit -m "Ch 5: Add Haruki hidden acts + Yui-sequence evidence seeding"
```

---

### Task 3: Rina's Hidden Acts + Emotional Asymmetry (chapter_04.md)

**Files:**
- Modify: `chapter_04.md` — Rina's call, Memory Fragment #2

**Context:** Ch 4 has Rina's main call and the notebook incident memory fragment. This chapter needs:
1. Rina's emotional asymmetry (she spent Mira's credibility for social definition)
2. Rina's hidden act of selfishness (the notebook — chose not to correct the record; already partially present as Memory Fragment #2)
3. Rina's hidden act of love (the voicemail she kept)
4. Partial evidence for the notebook act (teacher note or lost-and-found log)

**Step 1: Sharpen Memory Fragment #2 as hidden act of selfishness**

The notebook incident already exists as Memory Fragment #2 (~line 13, 820). Update the memory fragment to include the specific Higashino detail: Rina found the notebook, could have returned it, and chose not to. She recognized the opportunity — if Mira accuses and is wrong, "Mira accuses people" becomes social fact. She let the absence do the work.

**Step 2: Add partial evidence — the discoverable record**

During the school records investigation accessible from this chapter (or cross-referenced from Ch 5 records), add a discoverable item: a teacher note or lost-and-found log that places the notebook in a location Rina had access to, with a timestamp contradicting her version. This should be available in the Ch 5-7 investigation window. Add a notebook prompt when discovered.

**Step 3: Add the voicemail discovery**

Add a discoverable phone record detail: during school communication records investigation, the player finds phone data showing a voicemail from Mira's number to Rina's, accessed repeatedly over years. The voicemail's content isn't heard — just the access pattern. The love (keeping it, replaying it) and the selfishness (never acting) sit in the same person, on the same phone.

Add notebook prompt: "RINA — VOICEMAIL: Mira left Rina a voicemail [date]. Phone records show the voicemail has been accessed [X] times over [Y] years. Rina never deleted it. She never acted on it. She replayed it."

**Step 4: Weave emotional asymmetry into Rina's call**

Add texture to Rina's existing dialogue that surfaces the asymmetry: her social vocabulary depends on Mira's outsider status. She was "reasonable" because Mira was "intense." Thread this through her responses — not as explicit statement but as audible pattern the player can track.

**Step 5: Update confrontation integration**

Add a beat to the break sequence: the player presents the notebook evidence (teacher note), and Rina's defense shifts from "I didn't start it" to the realization that she did. The cost: she can't maintain the frame that she was passive.

**Step 6: Commit**

```
git add chapter_04.md
git commit -m "Ch 4: Add Rina hidden acts, emotional asymmetry, voicemail evidence"
```

---

### Task 4: Kaito's Hidden Acts (chapter_04.md or chapter_07.md)

**Files:**
- Modify: `chapter_04.md` or `chapter_07.md` — depending on where Kaito's main call/break lands
- Reference: `chapter_01.md` — for "no relevant observations" language parallel

**Context:** Kaito needs:
1. Hidden act of selfishness (the witness form — "no relevant observations")
2. Hidden act of love (the late-night calls he answered)
3. Emotional asymmetry (Mira's courage was his exemption)

**Step 1: Check Ch 1 for the "no relevant observations" canvass language**

Verify the canvass report language in Ch 1 that Kaito's witness form should echo. If it doesn't exist yet, add a brief reference to canvass reports using institutional language during the case file review.

**Step 2: Add the witness form as discoverable evidence**

In the school records investigation window (Ch 5-7), add a school incident form with Kaito's name, dated during the period of Mira's reports, reading "no relevant observations." The player who remembers the canvass report from Ch 1 recognizes the institutional language.

Add notebook prompt: "KAITO — WITNESS FORM: School incident form, dated [X]. Kaito asked directly if he'd seen anything unusual near school. Response: 'no relevant observations.' SAME LANGUAGE as Doi's suppressed canvass testimony (Ch 1). He had the silver car, the timing patterns, everything in his notebooks. He said no."

**Step 3: Add the phone records — late-night calls**

During infrastructure investigation (Ch 7-9), add discoverable phone records showing a pattern: calls from Mira's home to Kaito's phone, late evening, consistent over months. He answered every time. Add notebook prompt connecting this to his selfishness: he knew more about Mira than anyone because she told him things at 9 PM that she told no one else, and he still said "no relevant observations."

**Step 4: Update confrontation integration**

Kaito's existing emotional climax ("I thought you didn't need help" / "I didn't tell anyone") gets reshaped: he wasn't just silent. He was asked directly and said no. The concrete lie sits underneath the emotional reveal.

**Step 5: Commit**

```
git add chapter_04.md chapter_07.md
git commit -m "Ch 4/7: Add Kaito hidden acts — witness form, late-night calls"
```

---

### Task 5: Doi's Hidden Acts (chapter_06.md)

**Files:**
- Modify: `chapter_06.md` — Doi's false confession arc

**Context:** Doi needs:
1. Hidden act of selfishness (reported observations to Endo directly — co-opted contribution)
2. Hidden act of love (gave Mira the blue notebook)
3. Emotional asymmetry (took relief from responsibility by passing concerns up the chain)

**Step 1: Add the council intake form as discoverable evidence**

In the community council records investigation window (Ch 7-9), add a discoverable council intake form or logged call record with Doi's name, describing concerns about activity near the school. Dated before Mira's death. This can be seeded in Ch 6 as a forward reference or planted in Ch 7-9 investigation content.

Add notebook prompt: "DOI — COUNCIL REPORT: Intake form dated [X]. Doi reported concerns about activity near school to community safety council. Filed by council chair — Endo. Doi did the responsible thing. The responsible thing traveled to the worst possible person."

**Step 2: Add the blue notebook origin**

In Mira's eraser catalogue (already referenced in the manuscript), add a first entry: "Notebook from Mr. Doi. He said I should write things down so I don't forget. Blue cover." This connects the game's most important artifact to Doi's small kindness. Can surface through the notebook scene in Ch 11 or through evidence examination in earlier chapters.

**Step 3: Update the false confession arc**

Reshape the false confession resolution: when the player breaks through and surfaces the council record, Doi's real guilt arrives. He didn't just fail to act — he acted, and the action traveled to Endo. His guilt isn't about inaction. He did the right thing in the wrong direction.

**Step 4: Commit**

```
git add chapter_06.md
git commit -m "Ch 6: Add Doi hidden acts — council report, blue notebook origin"
```

---

### Task 6: Aizawa's Hidden Acts (chapter_05.md, chapter_08.md)

**Files:**
- Modify: `chapter_05.md` — Aizawa's first call
- Modify: `chapter_08.md` — Aizawa's break scene (if present)
- Modify: `chapter_07.md` or `chapter_09.md` — evidence chain investigation window

**Context:** Aizawa needs:
1. Hidden act of selfishness (classified notebook as "personal effects, non-evidentiary")
2. Hidden act of love (altered a disciplinary report to protect Mira)
3. Emotional asymmetry (Mira's persistence was her institutional absolution)

**Step 1: Add the property intake form as discoverable evidence**

In the evidence chain investigation window (Ch 7-9), add a discoverable property intake form with Aizawa's signature, classifying Mira's observation notebook as "personal effects, non-evidentiary." She opened it, saw the eraser reviews on the first pages, did not read further.

Add notebook prompt: "AIZAWA — NOTEBOOK CLASSIFICATION: Property intake form signed by Aizawa. Mira's observation notebook classified as 'personal effects, non-evidentiary.' Aizawa opened it. Saw eraser reviews. Did not read further. 14 months of dated, accurate observation — buried by the one person whose professional identity was built on documentation."

**Step 2: Add the altered report as discoverable evidence**

In the school records investigation (Ch 5-7), add two versions of the same disciplinary report — or a handwritten correction visible in the file. Aizawa softened language that would have escalated Mira's classification. The complication: the altered report became part of the trail Endo later cited. Kindness became complicity through procedure.

Add notebook prompt: "AIZAWA — ALTERED REPORT: Two versions of same disciplinary report. Original: language that would have escalated Mira's 'behavior problem' classification. Revised (Aizawa's hand): softened. She protected Mira from the system. The softened report is now part of the trail Endo cited to categorize Mira as 'managed.' The kindness and the burial are the same skill."

**Step 3: Update confrontation integration**

Extend Aizawa's existing break ("I chose the version of my job that let me sleep") with a second layer: she didn't just fail to act while Mira was alive. After Mira died, she held the proof and chose not to look.

**Step 4: Commit**

```
git add chapter_05.md chapter_07.md chapter_08.md
git commit -m "Ch 5/7/8: Add Aizawa hidden acts — notebook classification, altered report"
```

---

### Task 7: Yui's Hidden Act (chapter_04.md or post-intervention chapter)

**Files:**
- Modify: Chapter where Yui's post-intervention content lives (likely `chapter_04.md` or later)

**Context:** Yui needs:
1. Hidden act of selfishness (the lily that never arrived — post-death, during volunteer search)
2. Hidden act of love (crane on windowsill — already in manuscript, no changes needed)
3. Emotional asymmetry (took refuge in Mira's friendship while hiding it entirely)

**Step 1: Add the lily as discoverable physical evidence**

In the shoebox contents (discovered during or after the Yui intervention), add the lily: forty-three folds, Mira's name written on it, dated to the week of the volunteer search. One piece different from the others — more deliberate.

Add notebook prompt: "YUI — THE LILY: Found in shoebox. 43 folds — her most patient work. Mira's name. Dated to the week of the volunteer search. She brought it to the search perimeter. Saw the volunteers. Saw Endo organizing. Went home. Even after Mira was gone, the architecture of avoidance still controlled her."

**Step 2: Add the post-intervention reveal**

Different from other characters: the lily surfaces through trust during a post-intervention call when Yui is safe and beginning to speak freely. She explains the lily without being confronted. The player had it in the notebook; Yui tells them what it was.

**Step 3: Commit**

```
git add [relevant chapter file]
git commit -m "Add Yui hidden act — the lily that never arrived"
```

---

### Task 8: Endo's Selective Truth Sharpening (chapter_08.md)

**Files:**
- Modify: `chapter_08.md` — Endo's first call, the three leads, the informational tell

**Context:** Sharpen Endo's Ch 8 leads to make the partition pattern visible:
- Each lead contains a true thing that would point toward him if combined with information he gave someone else
- The Ogawa staffing change example: told to Kenji as context, told to Haruki as administrative, withheld from Reiko

**Step 1: Sharpen the three leads**

Revise Endo's three helpful leads so each one contains a subtle partition marker — a detail that the player will recognize in Ch 12 intercepts as having been presented differently to a different audience. The leads should remain genuinely helpful (they must still function as real investigative leads), but each should contain a seam the attentive player can spot on replay.

For the Ogawa staffing change lead specifically: Endo frames it to Kenji as "a staffing change, I believe" — vague, contextual. The player who later hears (via Ch 12 intercept) how Endo described the same event to Haruki will notice the difference.

**Step 2: Add design notes for partition tracking**

Add design notes to each lead explaining which version was given to which audience and what truth was withheld from whom. These notes serve as implementation reference for the Ch 12 intercept pass.

**Step 3: Commit**

```
git add chapter_08.md
git commit -m "Ch 8: Sharpen Endo's three leads — partition pattern seeded"
```

---

### Task 9: Mira Names the Routing (chapter_10.md)

**Files:**
- Modify: `chapter_10.md` — Scene 7 (Mira Hears Endo)

**Context:** Add Mira's one-line observation about Endo's routing, placed after "That's not care. That's collecting."

**Step 1: Add the routing line**

After Mira's existing "That's not care. That's collecting." line (~line 317), add her second observation about routing. Something in the register of: "He doesn't hide things. He sorts them. Everyone gets a piece. Nobody gets the picture."

This gives the player vocabulary for what they've been sensing. One line. Mira's voice.

**Step 2: Commit**

```
git add chapter_10.md
git commit -m "Ch 10: Add Mira's routing observation — selective truth vocabulary"
```

---

### Task 10: Reiko Three-Layer Design (chapter_09.md, chapter_11.md)

**Files:**
- Modify: `chapter_09.md` — Reiko's static call (Layer 2 already partially present)
- Modify: `chapter_11.md` — The notebook scene (Layer 3, plus Yui-sequence first entry)

**Context:** Reiko's three-layer design:
- Layer 1 (ongoing asymmetry): Texture across existing Reiko calls — no new scenes needed, just sharpening of rehearsed phrases. Can be addressed in character bible update.
- Layer 2 (the missed call): Already present in Ch 9 Path C. Needs sharpening as the Higashino "hidden act" and connection to the phone record as discoverable evidence (not just Reiko's confession).
- Layer 3 (the notebook scene): Already the strongest scene in the game. Enhancement is what the player brings to it.

**Step 1: Add phone record evidence for Layer 2**

Currently, Reiko's missed call is revealed through her confession (Ch 9 Path C). The Higashino design requires partial evidence discoverable through investigation BEFORE Reiko confesses. Add a phone record — a logged call from the school to Reiko's number, short duration, dated before Mira's disappearance, originated from a location near an active cable run — discoverable during infrastructure investigation (Ch 8-9 window). The player finds the record, notes the date and duration, and arrives at Reiko's confession already suspicious.

Add notebook prompt when phone record is discovered: "PHONE LOG — SCHOOL → REIKO: Call logged [date], duration 43 seconds. Originated from school office. Location near active cable run — exchange bleed-through likely. Short call, urgent timing (after program ended early). What was this call?"

**Step 2: Add Reiko's fridge note (hidden act of love)**

In Ch 11, when the apartment opens to investigation, add the fridge note discovery: among the refrigerator notes in Reiko's kitchen drawer, one note that isn't a report. A drawing of Lopsided the whale eraser. "Nikujaga was really good. You make the best one. Goodnight mom." Discoverable as a physical object during the scene.

Add notebook prompt: "REIKO — FRIDGE NOTE: Not a report. Drawing of Lopsided. 'Nikujaga was really good. You make the best one. Goodnight mom.' Even after Mira stopped reporting to Reiko, she never stopped loving her."

**Step 3: Add Reiko warmth moment**

The design doc flags a gap: the manuscript characterizes Reiko's love primarily through objects and routines. Add at least one recovered detail or memory fragment showing Mira and Reiko in a moment of genuine warmth. Design during implementation — something specific, not sentimental. Mira showing Reiko a bug. Watching something together in the narrow window between waking and school. A moment where the subject wasn't dangerous and it worked.

**Step 4: Add the notebook's first entry (Yui-sequence completion)**

In Ch 11's notebook scene, ensure the first entry Reiko reads is about Yui — the entry that starts the fourteen-month log. Not by name (Mira protects her), but unmistakable. This is the completion of the Yui-sequence: the player who tracked the institutional dates in Ch 5-9 now hears Mira's voice for the first time, and the pattern locks in.

The first entry should read something like: "I told Mr. Ise about [her]. He called her mom. Her mom called [him]. Now it's worse. I made it worse. I don't know what to do. I'm going to try again but different this time."

**Step 5: Commit**

```
git add chapter_09.md chapter_11.md
git commit -m "Ch 9/11: Reiko three-layer design — phone record, fridge note, notebook first entry"
```

---

### Task 11: Ch 12 Intercepts — Selective Truth Reveal (chapter_12.md)

**Files:**
- Modify: `chapter_12.md` — The call war intercepts

**Context:** The Ch 12 intercepts already exist. The sharpening: each intercept should contain one detail that connects to something Endo told Kenji in Ch 8, reframed for the new audience. The player who remembers Ch 8 hears the echo.

**Step 1: Cross-reference Ch 8 leads with Ch 12 intercepts**

For each intercept (Endo → Reiko, Endo → Haruki, Endo → District Police, Endo → Doi), identify which Ch 8 lead it echoes and how the same event is reframed. Ensure at least one specific detail per intercept that the attentive player can connect to Ch 8.

Specific targets:
- **Endo → Reiko intercept:** Endo does NOT mention the staffing change (Ogawa). He mentioned it to Kenji. The omission is the tell — Reiko might connect it to Mira's reports.
- **Endo → Haruki intercept:** Endo references the staffing change differently — as administrative, not investigative context. Different framing, same event.
- **Endo → District Police intercept:** The institutional register is new — the player has never heard Endo in full bureaucratic mode. "No warmth. No pauses. Just procedure weaponized."
- **Endo → Doi intercept:** Endo quotes Doi's own words back to him. The fidelity tell — knowing things with the wrong resolution — deployed as a weapon.

**Step 2: Add design notes connecting partitions**

Add design notes to each intercept documenting which truth was partitioned where, referencing the Ch 8 seeding from Task 8.

**Step 3: Commit**

```
git add chapter_12.md
git commit -m "Ch 12: Sharpen intercepts — selective truth partition pattern revealed"
```

---

### Task 12: Character Bible — All Hidden Acts and Asymmetry (deadringer_characters.md)

**Files:**
- Modify: `deadringer_characters.md` — All character sections

**Context:** After the chapter-level changes land, update each character's bible entry to document:
- Emotional asymmetry (what they took from Mira)
- Hidden act of selfishness (specific, irreversible, discoverable)
- Hidden act of love (specific, discoverable, with complication)
- Cost of truth (what solving the mystery means for them)
- Discovery method and chapter window
- Confrontation integration notes

**Step 1: Update Rina's section**

Add: emotional asymmetry (spent Mira's credibility), notebook selfishness act, voicemail love act, cost, discovery windows.

**Step 2: Update Kaito's section**

Add: emotional asymmetry (Mira's courage was his exemption), witness form selfishness act, late-night calls love act, cost, discovery windows.

**Step 3: Update Aizawa's section**

Add: emotional asymmetry (Mira's persistence was her institutional absolution), notebook classification selfishness act, altered report love act, cost, discovery windows.

**Step 4: Update Yui's section**

Add: emotional asymmetry (took refuge while hiding friendship), lily selfishness act, crane love act (already present — add design note), cost, discovery windows.

**Step 5: Update Doi's section**

Add: emotional asymmetry (took relief by passing concerns up), council report selfishness act, blue notebook love act, cost, discovery windows.

**Step 6: Update Haruki's section**

Add: emotional asymmetry (proxy courage), weaponized language selfishness act, recommendation love act, cost, discovery windows.

**Step 7: Update Reiko's section**

Add: three-layer design documentation, ongoing asymmetry notes, missed call hidden act, fridge note love act, warmth gap resolution, cost (notebook scene).

**Step 8: Update Endo's section**

Add: selective truth principle documentation — never lies, partitions truth, switchboard as philosophy made literal. Reference Ch 8 partition seeding and Ch 12 reveal.

**Step 9: Commit**

```
git add deadringer_characters.md
git commit -m "Character bible: Add all Higashino-lens through-lines per character"
```

---

### Task 13: Chapter Structure — Information Gates Update (chapter_structure.md)

**Files:**
- Modify: `chapter_structure.md` — Information gates, suspicion arc

**Context:** New evidence items need to be registered in the information gates:
- Yui-sequence dates (Ch 5-7 investigation window)
- Haruki's recommendation letter (Ch 5)
- Rina's notebook evidence + voicemail (Ch 5-7)
- Kaito's witness form + phone records (Ch 5-9)
- Aizawa's property intake form + altered report (Ch 5-9)
- Doi's council intake form (Ch 7-9)
- Reiko's phone record (Ch 8-9)
- Reiko's fridge note (Ch 11)
- Notebook first entry — Yui sequence completion (Ch 11)

**Step 1: Add new information gates**

Add gates for each new evidence item, specifying what the player must know before the evidence becomes available and what it unlocks.

**Step 2: Update the NPC availability map if needed**

Check whether any hidden act discoveries change when an NPC becomes callable or change the call dynamics.

**Step 3: Add Higashino-lens evidence tracking section**

Add a new section documenting the hidden acts evidence chain — which evidence is discoverable when, and which confrontations it feeds into.

**Step 4: Commit**

```
git add chapter_structure.md
git commit -m "Chapter structure: Add Higashino-lens evidence gates and discovery windows"
```

---

### Task 14: Sync dead_ringer_complete.md

**Files:**
- Modify: `dead_ringer_complete.md` — Master manuscript

**Context:** After all chapter-level and character bible changes are complete, sync `dead_ringer_complete.md` to reflect the updated content. This file is the combined manuscript — all chapters and character entries in one document.

**Step 1: Identify sections in dead_ringer_complete.md that correspond to modified chapters**

Cross-reference the chapter files with their locations in the master manuscript.

**Step 2: Apply all changes from individual chapter files to the master**

Ensure every modification made in Tasks 1-13 is reflected in the master manuscript.

**Step 3: Commit**

```
git add dead_ringer_complete.md
git commit -m "Sync master manuscript with all Higashino-lens changes"
```

---

## Implementation Notes

**Writing quality bar:** These are narrative manuscript files, not code. Every addition must match the existing voice — Mira's sardonic precision, Kenji's clinical restraint, Reiko's rehearsed composure, Endo's measured warmth. Do not add design language to dialogue or narrative prose. Design notes use [DESIGN NOTE:] brackets. Notebook prompts use [NOTEBOOK PROMPT:] format.

**Evidence placement principle:** Partial evidence is discovered through investigation. The character fills in the rest during confrontation. Evidence changes the question; the break changes the answer. Never put the full hidden act in the evidence — the evidence is a seam, not a confession.

**Non-repetition check:** After implementation, verify that no two characters' hidden acts of selfishness use the same shape (social commission, self-suppression, administrative burial, ongoing suppression, co-opted contribution, weaponized language). If any feel similar, revise.

**Yui-sequence integrity check:** After all chapter changes, read the Yui-sequence evidence in chronological order (Ch 5 dates → Ch 7 records → Ch 9 cross-references → Ch 11 first entry) and verify the split delivery works — institutional data first, Mira's voice last.

**Selective truth integrity check:** After Ch 8 and Ch 12 changes, verify that Endo's partition pattern is traceable — the player who compares Ch 8 leads to Ch 12 intercepts should be able to map which truth went where and what was withheld from whom.
