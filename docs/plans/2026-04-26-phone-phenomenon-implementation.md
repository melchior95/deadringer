# Phone Phenomenon & Character Quirks — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Integrate the approved design (phone phenomenon, Yui folding quirk, Kaito coordinate quirk, micro-incidents, Ch 4-8 momentum) into the existing narrative documents.

**Architecture:** All changes are edits to two existing markdown documents: `deadringer_characters.md` (character bible entries for Yui and Kaito) and `chapter_structure.md` (chapter beats for Ch 4-9 plus a new phone phenomenon section). No new files created. No existing content deleted — only augmented.

**Tech Stack:** Markdown narrative documents. Git for version control.

---

### Task 1: Add Kaito's Coordinate Speech Signature

**Files:**
- Modify: `deadringer_characters.md` — Kaito's GAMEPLAY IDENTITY section (line ~1114)
- Modify: `deadringer_characters.md` — Kaito's THE BREAK section (line ~1179)

**Step 1: Augment Kaito's speech pattern and tell**

In the GAMEPLAY IDENTITY section, after the existing speech pattern and tell entries, add the spatial-temporal annotation signature. The existing delayed-processing mechanic stays — the coordinates are what fill the delay. Key additions:
- **Surface quirk** entry describing the annotation behavior with example dialogue
- **Feelings as locations** entry showing how he answers emotional questions with spatial data
- **Misdirection** entry explaining why coordinates sound like surveillance transcripts
- **Contrast pair** table (Kaito vs. Mira — emotional weather vs. physical positions)

**Step 2: Enhance the break scene**

Replace the existing break scene dialogue with the enhanced version that includes coordinate-filled testimony ("East entrance. Behind the post office. Eleven minutes the first time...") and the coordinate-drop moment ("I thought you knew you were alone").

**Step 3: Commit**

```
git add deadringer_characters.md
git commit -m "Add Kaito's spatial-coordinate speech signature to character bible"
```

---

### Task 2: Add Yui's Origami Folding Quirk

**Files:**
- Modify: `deadringer_characters.md` — Yui's GAMEPLAY IDENTITY section (line ~1722)
- Modify: `deadringer_characters.md` — Yui's YUI ON THE PHONE section (line ~1810)

**Step 1: Add folding-as-audible-tell to gameplay identity**

After the existing tell and break mechanic entries, add:
- **Audible signature** entry describing folding sounds on calls
- **Folding tell system** table (steady/speeds up/stops/tears)
- **Parallel with Aizawa** explaining institutional clicks vs. private folding
- **The physical object** — crane sent to Kenji as non-verbal trust signal
- **Epilogue echo** — folding absent in epilogue calls

**Step 2: Add "Did Anyone Come?" sound design**

In the YUI ON THE PHONE section, integrate the folding sound design into the existing "Did anyone come?" moment — steady folding during safe talk, speeding up as questions edge close, stopping during the twelve-second silence, paper tearing before "She said they would."

**Step 3: Commit**

```
git add deadringer_characters.md
git commit -m "Add Yui's origami folding quirk to character bible"
```

---

### Task 3: Add Town Phone Phenomenon Section to Chapter Structure

**Files:**
- Modify: `chapter_structure.md` — new section before Act II or after the Suspicion Arc section

**Step 1: Add THE YANAGI PHONE PHENOMENON section**

Insert a new top-level section containing:
- Overview: half-alive infrastructure, normalized by residents, Kenji notices
- Folklore layer table: who says what, when (Doi, school kids, Fumiko, local legend)
- Escalation curve table: local color → unsettling → pivot → active → revelatory
- Design principle: reactive escalation tied to investigation activity

**Step 2: Commit**

```
git add chapter_structure.md
git commit -m "Add town phone phenomenon section to chapter structure"
```

---

### Task 4: Update Chapter 4 — Yui (Phone Seeding + Folding Reference)

**Files:**
- Modify: `chapter_structure.md` — Chapter 4 section (line ~114)

**Step 1: Add phone folklore seeding and folding reference**

In the baseline investigation section of Ch 4, add:
- **Phone phenomenon seed:** A contact during the Yui/Rina investigation mentions Yanagi's phone weirdness offhand ("You calling from Yanagi? The reception out there..."). Player files as rural infrastructure.
- **Yui's folding audible:** Note that Yui's paper folding is audible from her first call — the player hears creasing sounds beneath her performed composure. Cross-reference character bible.

**Step 2: Commit**

```
git add chapter_structure.md
git commit -m "Add phone seeding and Yui folding reference to Ch 4"
```

---

### Task 5: Update Chapter 5 — The Teacher's Guilt (Micro-Incident 1 + Kaito Coordinates)

**Files:**
- Modify: `chapter_structure.md` — Chapter 5 section (line ~134)

**Step 1: Add Micro-Incident 1 (The Wrong Connection)**

After the Aizawa section, before the player knowledge summary, add the wrong connection event:
- Kenji dials, connects to wrong person — a woman mid-conversation about "the reports from that year"
- Line cuts, redial works normally
- Contact responds: "the phones in Yanagi have long memories"
- Mira: "The static on that call was different. It had layers."
- Late-game payoff note: the fragment was a real conversation routed through the exchange

**Step 2: Add Kaito's first call with coordinate signature**

Add a note that Kaito's first phone contact features his spatial-temporal annotations prominently — the player clocks his speech quirk within thirty seconds. His coordinates sound unsettling, reinforcing the red herring.

**Step 3: Update player knowledge**

Add to the chapter-end knowledge summary: the town's phones behave oddly, and a new suspect (Kaito) talks like a surveillance transcript.

**Step 4: Commit**

```
git add chapter_structure.md
git commit -m "Add wrong connection micro-incident and Kaito coordinates to Ch 5"
```

---

### Task 6: Update Chapter 6 — Doi's False Confession (Fumiko's Anomaly File)

**Files:**
- Modify: `chapter_structure.md` — Chapter 6 section (line ~152)

**Step 1: Add Fumiko's phone anomaly file**

In the Fumiko entry section, add that among her materials, she mentions a file of phone anomalies in the Yanagi district going back eight years. Telecom inspected twice — "normal, just old." She never published. The player now has the word "pattern" applied to both disappearances and phone behavior.

**Step 2: Commit**

```
git add chapter_structure.md
git commit -m "Add Fumiko's phone anomaly file to Ch 6"
```

---

### Task 7: Update Chapter 7 — The Silver Car (Haruki Setup + The Pivot)

**Files:**
- Modify: `chapter_structure.md` — Chapter 7 section (line ~174)

**Step 1: Add Haruki's breathing dismissal**

Early in Ch 7, during conversation, add Haruki mentioning the students' bridge number dare and dismissing a student's report of hearing breathing. This is the micro-setup for the macro-pivot — a child reported something true, an adult explained it away.

**Step 2: Add THE PIVOT — Micro-Incident 2 (The Breathing)**

After the existing player knowledge summary, add a new section: **The Pivot — "The Breathing"**. Contains:
- Placement: end of Ch 7, after Endo convergence
- The full scene: static changes, Mira says "wait" / "don't talk", breathing heard for four seconds, "That wasn't me. That was someone alive." / "Someone is in there."
- What the player knows vs. suspects (three people mentioned a child's absence)
- How this changes the game: past-tense mystery → present-tense rescue
- Updated player knowledge incorporating the pivot

**Step 3: Commit**

```
git add chapter_structure.md
git commit -m "Add Haruki breathing setup and the pivot to Ch 7"
```

---

### Task 8: Update Chapters 8-9 — Phone Escalation and Dual-Weight Calls

**Files:**
- Modify: `chapter_structure.md` — Chapter 8 section (line ~205) and Chapter 9 section (line ~223)

**Step 1: Add phone escalation to Ch 8**

Add to the Endo chapter:
- Every call now carries dual weight: case investigation + listening for the signal
- Phone bleed-through escalates — calls echo, fragments of other conversations intrude
- Endo calling on the same lines where a child was breathing changes the emotional register of his helpfulness
- The phone is now both tool and compromised environment

**Step 2: Add infrastructure tracking to Ch 9**

Add to the framing unravels chapter:
- While deconstructing evidence, the player is also tracking phone anomalies
- Which calls bleed, which locations produce static — maps to Endo's surveillance priorities
- Reiko's static phone call (already exists) now has additional resonance: the phone phenomenon the town normalized was the infrastructure that could have saved Mira

**Step 3: Commit**

```
git add chapter_structure.md
git commit -m "Add phone escalation and dual-weight calls to Ch 8-9"
```
