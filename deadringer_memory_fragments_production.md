# DEAD RINGER — Memory Fragment Scene Production Specification

Production specification for the three interactive Mira-POV scenes. This document is the build-time reference for each fragment — location, runtime, format, player agency, branching texture, return-to-present mechanics, camera/audio direction.

**Companion docs:**
- `deadringer_systems.md` §4 — Memory Fragment System overview
- `deadringer_locations.md` — locations referenced (Reiko's apartment kitchen state, Mira's classroom, school counselor's office)
- `deadringer_audio_signatures.md` §4 — environmental audio references
- Chapter files: `chapter_03.md` (Reiko Denial, lines 220–399), `chapter_04.md` (Rina Social Distortion, lines 607–706), `chapter_05.md` (Aizawa Procedure, lines 605–737)

**Scope of this document:**
- Production spec for three interactive scenes: Reiko Denial (Ch 3), Rina Social Distortion (Ch 4), Aizawa Procedure (Ch 5)
- Shared systems (entry transitions, interactive vocabulary, return-to-present)
- Per-fragment: location, runtime, agency scope, interactive element list, branching, voice/camera/audio direction, accessibility considerations

---

## 1. SHARED SYSTEMS

All three fragments share a consistent architecture. These systems are specified once and applied across all three scenes.

### 1.1 Entry Transition

When a trigger condition fires (see per-fragment sections), the current scene transitions out via:

1. **Visual dissolve** — the present-day scene blurs and fades over ~2 seconds. Color drains slightly; the apartment or call-screen becomes less saturated.
2. **Audio transition** — the wire-sound rises briefly, carrying a child's voice at the threshold of hearing. A single high-frequency tone swells and resolves into the memory's ambient bed.
3. **TEXT ON SCREEN:** the line *"This is a memory. You are Mira."* appears center-screen in the game's established text style. Holds for ~3 seconds. Fades.
4. **Perspective shift** — camera height drops to approximately 130 centimeters (Mira's height). The drop should be perceptible — the player feels they have become shorter. UI elements reposition accordingly.

Total entry transition: ~5–7 seconds.

### 1.2 Interactive Vocabulary

Each fragment offers a limited set of interactions:

- **Dialogue choice** — 2–4 authored options at each decision point. Mira's words only. (The other characters are NPC-driven.)
- **Environmental examine** — 3–6 objects per scene. Clicking/tapping an object produces a short Mira-POV observation (1–3 lines of internal narration or out-loud comment depending on context).
- **Advance** — at scene-beat breakpoints, the player taps to continue.

The player cannot:
- Move Mira's body freely (no walk-around). Camera is fixed-with-pan at authored positions.
- Choose actions outside the authored menu (no "flee," no "shout," no "hit").
- Replay or skip within the fragment (skip available on NG+ only — see `deadringer_systems.md` §8.2).

### 1.3 Camera Specification

Each fragment uses fixed camera positions with authored pans. Three position modes:

- **STANDING** — the default for Mira standing still. Camera at 130cm, facing the current conversational partner. Slight forward-lean (simulating a child's attentiveness).
- **EXAMINE** — when the player targets an examinable object, camera pans to it and zooms close. The zoom is handheld-ish but minimal; Mira is looking, not fidgeting.
- **WALK** — short authored camera movements when Mira moves within the scene (crossing a kitchen, walking to a doorway). Always short, always with a clear destination.

No head-bob. No free mouse-look. The constraint is authored and felt — Mira is precise, not fidgety; the camera should reflect that.

### 1.4 Return-to-Present Mechanic

All three fragments end the same way:

1. **Visual fade-out** — the scene thins. Warm colors dissolve. Sound attenuates.
2. **Audio transition** — the wire-sound rises again, this time carrying what feels like a message from inside the memory (a child's voice saying a fragment of something — "can't means won't" for Reiko, "I just wrote it down" for Rina, "personal effects" for Aizawa).
3. **TEXT ON SCREEN** — a single line surfaces as a notebook entry (deposited into the Log automatically). This line is the memory's "takeaway" — Mira's crystallized observation.
4. **Return to present** — Kenji's apartment. The call-aftermath state. Mira is quiet.

The return transition is slightly faster than the entry — ~4 seconds — because the player is returning to the familiar, not arriving somewhere new.

### 1.5 Agency Scope — Fixed Outcome Design

**Critical:** all three fragments arrive at a fixed outcome regardless of player choice. The thesis: Mira's dismissals were not preventable by a better version of her. Giving the player the illusion that a different choice could have saved her would betray the story's argument.

What branches:
- The *texture* of the dismissal (how it happens, what's said, what Mira observes about it)
- The *notebook entry* that results (each branch produces a slightly different crystallized observation)
- The *audio register* of the final beat (tone shifts based on approach)

What does not branch:
- Whether Mira is dismissed (she is)
- Whether the report produces action (it doesn't)
- The next-chapter consequence

This must be telegraphed to the player NOT through an on-screen explanation, but through the fragment's own internal logic. Players who try to "win" a fragment should feel the game's resistance — not as frustration, but as dawning understanding.

### 1.6 Accessibility

- Full subtitles for all NPC dialogue and Mira's internal monologue
- Audio description layer (optional) describes the environment and Mira's gestures
- Camera transitions should be cross-faded rather than hard-cut for players with motion sensitivity
- Text-on-screen moments hold long enough to read at a slow reading pace (6-second minimum for the entry text)
- Examinable objects have clear visual highlight on hover/focus

### 1.7 Save Behavior

- No saves inside fragments. Autosave triggers at fragment entry and at fragment exit.
- If the player quits mid-fragment: resume from fragment start on next launch. Memory Fragments cannot be partially saved.

### 1.8 Higashino Integration — Overall Design Note

**Higashino integration:** The three Memory Fragments were designed before the Higashino-lens pass but already contain the seeds of the hidden acts. Each fragment shows a character performing their failure in real time — Reiko dismissing, Rina repositioning, Aizawa filing. The Higashino-lens additions (hidden acts discoverable through investigation) recontextualize these performances retroactively. The fragments do not change. What the player brings to them changes. This is the Higashino principle: the truth was always visible. The reveal is learning to read it.

---

## 2. FRAGMENT 1 — REIKO DENIAL

**Chapter:** 3
**Trigger:** Fires automatically after the Reiko first-call Soul Read resolves (Ch 3, immediately after the read entry is deposited).
**Fragment duration (estimate):** 3–4 minutes with careful play; 2 minutes if the player rushes dialogue.
**Manuscript source:** `chapter_03.md` lines 220–399.

### 2.1 Location

**Formal location:** Reiko Kitahara's apartment — kitchen. Afternoon. Approximately 18 months before Mira's death.

**Visual direction:**
- A small apartment kitchen. Smaller than Kenji's. Afternoon light through a single window.
- A counter with a rice cooker, a step stool pushed against the wall, a collection of magnets on the fridge (a school calendar, a pharmacy shift schedule, three handwritten notes in Mira's careful script).
- A low table in the adjacent living space is partially visible.
- Mira's shoes at the entry. A school bag on the floor near the doorway.

**Lighting:** warm afternoon sun through white curtains. The apartment reads as loved and tired — a home maintained by a woman who is too busy to fully clean it.

**Camera:** Mira is standing just inside the kitchen doorway. Reiko is at the kitchen table. Camera default position: over Mira's shoulder, framing Reiko.

### 2.2 Runtime & Format

- **Runtime:** ~3:00–3:30 at expected pace.
- **Format:** Mixed — interactive dialogue + environmental examine + authored beats.
- **Structure:** entry transition → environment establish → examine opportunities (3) → dialogue decision point → fixed outcome → return transition.

### 2.3 Player Agency Scope

**Interactive dialogue — the primary choice:** `[PLAYER CHOICE — Mira's Approach]` (manuscript line 282)

Three options:
- **CAREFUL** — "Mom? Can I tell you something I noticed?"
- **DIRECT** — "There's a man who keeps watching the school when we get out."
- **URGENT** — "Mom, this is important. Please listen."

Each branches the dialogue sequence. All converge on Reiko's dismissal — the *texture* differs. CAREFUL gets a slower, more gentle dismissal. DIRECT gets a quicker "I don't know, honey, don't worry about it." URGENT gets a moment of genuine maternal attention that decays back to dismissal within a few exchanges.

**Secondary choice (mid-scene):** `[PLAYER CHOICE — Mira's Response]` at manuscript line 374.

This is the follow-up — does Mira ACCEPT Reiko's dismissal and leave, or PRESS further?

- **ACCEPT** → scene concludes via ACCEPT path
- **PRESS** → short additional exchange, then converges to ACCEPT sequence

Pressing produces the kitchen's most painful beat — Reiko's "I said I would" delivered too fast, a habit rather than a commitment — but does not change the outcome.

### 2.4 Environmental Examine Elements

Three elements are examinable. Each produces a Mira internal monologue beat.

| Element | Mira's observation (approximate) |
|---|---|
| **The magnets on the fridge** | Mira notices her own handwriting on three notes. They are reports — the watching man, the silver car, the bench at the park. She wrote them for Reiko to find. Reiko moved them to the fridge but has not acted on them. |
| **The step stool** | Mira uses it to reach the counter for the small pot. She is remembering that she made this coffee. Her hands are too small for the large pot. |
| **Reiko's mug** | Full. Steam gone. Reiko has not been drinking it. She made it for herself before Mira came in; she has been holding it as a prop. |

Examining all three is optional; the fragment plays fine without. Examining them deepens the player's understanding of Mira's observation style — these details echo what she documents in her notebook throughout the game.

### 2.5 Fixed Outcome

Regardless of path: Reiko dismisses. The dismissal is loving, tired, and structural. She says some variant of "I'm sure it's nothing, honey, but I'll mention it if I see him" and turns back to her coffee. She does not mention it.

Mira leaves the kitchen. The fragment's final beat is Mira in her bedroom doorway, looking back at her mother at the table. Reiko is not watching her.

### 2.6 Notebook-Deposit Entry

At scene end, a notebook entry is deposited into the Log:

> *"'Can't' and 'won't' are different."*

This is Mira's earliest documented observation of the distinction that recurs in Ch 5 (the Ogawa classroom entries) and Ch 11 (the notebook scene with Reiko).

### 2.7 Voice Direction

**Mira (young-alive, Ch 3 fragment):**
- Slightly younger register than her ghost-voice. She is eight in this memory, not nine.
- Emotional state: wanting to be heard. Aware her mother is tired. Trying to present information gently enough not to tip the balance.
- CAREFUL path: deliberate, sweet, over-rehearsed.
- DIRECT path: matter-of-fact, clinical.
- URGENT path: the armor slips — she sounds like a child, not an observer.

**Reiko (young-alive):**
- Early thirties. Not exhausted yet — tired but managing.
- Warmth is real. Dismissal is structural, not cruel.
- The "I'm sure it's nothing, honey" line should be delivered without condescension. Reiko genuinely thinks she is being reassuring. The horror is that she is; the reassurance is the dismissal.

### 2.8 Camera Direction (Shot List)

1. **Entry (after transition):** over-shoulder on Mira, framing Reiko at the table. Warm light. Hold 3 seconds.
2. **During Mira's opening line:** cut to medium on Mira (waist-up). Player reads her face.
3. **Reiko's reception:** cut back to Reiko. She sets the mug down, turns slightly. Camera attention on her expression as it processes Mira's words.
4. **During dismissal:** stay on Reiko. Slow push-in to close — the player watches the dismissal happen at close range.
5. **Mira's secondary choice:** medium on Mira. Shorter framing; tighter.
6. **Final beat (Mira in doorway looking back):** wide shot. Reiko at the table, Mira at the doorway. The distance is the scene's thesis.
7. **Exit transition:** hold the wide shot for 2 seconds. Then thin/fade.

### 2.9 Audio Direction

**Ambient bed:**
- Distant neighborhood sounds through the window (bicycles, occasional car)
- A wall clock (ticking, steady)
- The fridge cycling on during the scene (the same rhythm as Kenji's apartment — ~6 seconds on, ~97 off — a deliberate cross-chapter callback; this is the rhythm Mira cites in Ch 11 3 AM scene)
- No TV, no music

**Tics:**
- Reiko's ceramic mug being set on the table (once, after Mira's opening line)
- Mira's school bag adjusted on her shoulder (once, before she enters the kitchen)

**Transitions:**
- Entry: wire-sound rises, resolves into the kitchen ambient over ~2 seconds.
- Exit: kitchen ambient thins; wire-sound carries Mira's "can't means won't" line through the transition back to present.

### 2.10 Higashino-Lens Layer

**Higashino-lens layer:** The player who later discovers the missed phone call (Ch 8-9 evidence) and the fridge note ("Goodnight mom" + Lopsided drawing, Ch 11) will revisit this fragment mentally. Reiko's denial in the memory is the same mechanism that made her say "call back later." The warmth moment (centipede on the balcony — designed in Ch 11) shows what the relationship looked like when it worked. The fragment gains retroactive weight: the player is watching the exact moment the gap between Mira and her mother became load-bearing.

**Production note:** No changes to the fragment itself. The recontextualization happens in the player's understanding across the game, not in this scene. The fragment was already written correctly — the Higashino-lens pass just makes it heavier.

---

## 3. FRAGMENT 2 — RINA SOCIAL DISTORTION

**Chapter:** 4
**Trigger:** Fires automatically after the Rina call's Soul Read deposits (Ch 4).
**Fragment duration (estimate):** 2–3 minutes.
**Manuscript source:** `chapter_04.md` lines 607–706.

### 3.1 Location

**Formal location:** Mira's classroom, Yanagi Municipal Elementary, Class 3-1 (one year before her death, second grade). Midday free period.

**Visual direction:**
- A typical Japanese elementary school classroom. Desks arranged in clusters.
- Sunlight through tall windows. Colored paper, scissors, the remains of a craft project.
- Other children moving, talking. Approximately 20 students.
- Mira's cluster: three desks pushed together.
- Rina's cluster: two clusters away — four desks, a group of girls around Rina's desk.

**Visual tone:** brighter and more crowded than the Reiko fragment. The sensory density is part of the design — Mira is a quiet child in a loud room.

### 3.2 Runtime & Format

- **Runtime:** ~2:30 at expected pace.
- **Format:** Mixed — interactive + authored beats. Shorter than Reiko Denial.
- **Structure:** entry → establish → decision point → branch-specific exchange → all-paths aftermath → return.

### 3.3 Player Agency Scope

**Primary choice:** `[PLAYER CHOICE — Mira's Response]` (manuscript line 625)

Three options:
- **DIRECT** — Walk to Rina's desk. "That's my notebook."
- **CAREFUL** — Ask the teacher. "Ms. Tanaka, I think someone has my notebook."
- **OBSERVE** — Watch. Wait. See if Rina opens it.

Each branches the scene. All three converge on the notebook absorbed into Rina's bag and the teacher moving the class on.

### 3.4 Environmental Examine Elements

Three elements before the primary decision point:

| Element | Mira's observation |
|---|---|
| **Mira's bag** | Checked twice. The notebook is not in it. Mira knows she had it at recess. |
| **The craft scraps on Mira's cluster** | Blue paper. White paper. The colors of her notebook cover. The visual echo is Mira's own noticing. |
| **Rina's cluster (from across the room)** | The corner of the notebook is visible under Rina's textbook. Mira can see it; no other child is positioned to see it. She is the only witness. |

### 3.5 Fixed Outcome

Regardless of branch: the notebook ends up in Rina's bag, the teacher moves on, no one confirms Mira's claim. The social physics of the classroom decides.

- DIRECT: Rina denies; a classmate says "she's so dramatic" quietly; the teacher doesn't intervene.
- CAREFUL: teacher asks Rina; Rina denies; teacher decides to believe the one who generates less friction.
- OBSERVE: the notebook is slipped into Rina's bag between subjects. No one notices.

In all branches, the period ends. Mira is the last one at her desk. A girl passes and says, not unkindly: "Mira, it's probably at home. You lose things sometimes." (The line is preserved from manuscript.)

### 3.6 Notebook-Deposit Entry

Mira, at her desk, writes on a sheet of paper (the game displays this as a text-on-screen beat). The entry that deposits:

> *"Next time I won't tell the teacher. I'll just write it down."*

This is the origin of Mira's documentation instinct — the observation she learns from this moment that produces the blue notebook, the careful records, the observational style Kenji encounters two years later.

### 3.7 Voice Direction

**Mira (eight, Ch 4 fragment):**
- Slightly younger register than the Reiko fragment — she is one year younger here (second grade vs. third).
- Emotional state: calm but frustrated. She knows the notebook is hers. She is learning, in real time, that knowing is not enough.
- The final writing beat is delivered as internal monologue — a child talking to herself as she writes.

**Rina (ten, fragment):**
- Already socially fluent. Her denial is not defensive; it is confident.
- Reference: a child who has learned that being certain is more valuable than being right. Present the certainty cleanly; do not play it as malicious.

**Ms. Tanaka (teacher):**
- Friendly, busy, pragmatic. Her decision-making should feel efficient, not unfair. She is not the villain. She is the mechanism.

### 3.8 Camera Direction

1. **Entry:** wide shot of the classroom. Busy. Density of children. Mira's cluster visible in middle-distance.
2. **Close on Mira's bag:** over-shoulder as she checks. Empty. She checks again.
3. **Spotting the notebook:** cut to Mira's POV. Camera finds Rina's cluster across the room. Slight zoom on the corner of the notebook.
4. **Decision point:** medium on Mira.
5. **Branch-specific:**
   - DIRECT: tracking shot as Mira walks to Rina's desk. Camera follows her from behind.
   - CAREFUL: Mira walks to the teacher. Camera follows.
   - OBSERVE: Mira stays at her cluster. Camera holds on her face; occasional cuts to Rina's cluster showing the notebook absorbed.
6. **Aftermath:** Mira at her desk. Wide again — the classroom emptying, Mira alone at her cluster. The passer-by line is delivered from off-camera.
7. **Writing beat:** close on the paper. Mira's hand. The words appear as she writes them.
8. **Exit transition:** fade on the written paper.

### 3.9 Audio Direction

**Ambient bed:**
- Classroom crowd ambient. Overlapping voices. Not chaos — dense.
- A chair scraping in the distance.
- Ms. Tanaka's voice occasionally carrying from the front of the room ("Alright, let's finish up in five minutes").
- A school bell for period change.

**Tics:**
- Paper sounds (craft scraps).
- Scissors clipping (once, from an adjacent cluster).
- The specific sound of a textbook being closed when Rina packs her bag.

**The final beat (Mira writing):**
- The crowd ambient drops out almost entirely.
- Only the pen on paper, and Mira's breathing.
- This acoustic isolation is the audio telegraph that something important is happening.

**Transitions:**
- Entry: wire-sound resolves into classroom crowd. The crowd should feel disorienting briefly — denser than Reiko's apartment.
- Exit: the crowd is already absent by the writing beat. The transition is a visual fade on the paper; no additional audio event.

### 3.10 Higashino-Lens Layer

**Higashino-lens layer:** The notebook incident in this fragment is now confirmed as the origin point of Rina's social machinery (hidden act of selfishness — she chose not to return it). The lost-and-found log evidence (Ch 5-7) will prove this. The voicemail evidence (accessed repeatedly for years) proves Rina never forgot. The fragment's ambiguity ("Version A vs Version B") is now weighted toward Version A by the institutional evidence, but the fragment itself should preserve the ambiguity — the evidence arrives later, not here.

**Production note:** The fragment should be played straight. No hints about which version is true. The Higashino balance depends on the player discovering the evidence later and revisiting the ambiguity with new eyes.

---

## 4. FRAGMENT 3 — AIZAWA PROCEDURE

**Chapter:** 5
**Trigger:** Fires automatically after Aizawa's first-call Soul Read deposits (Ch 5).
**Fragment duration (estimate):** 3–4 minutes. The longest of the three fragments.
**Manuscript source:** `chapter_05.md` lines 605–737.

### 4.1 Location

**Formal location:** School counselor's office, Yanagi Municipal Elementary. Approximately six months before Mira's death. School hours.

**Visual direction:**
- A small office. A desk with neat stacks of paper. A wall calendar with dates circled in different colors. A hand sanitizer bottle (the one established in the present-day Aizawa calls).
- A small plant on the windowsill — green, needing water.
- Two visitor chairs. Mira is standing in front of the desk (she has not sat down).
- The door is closed.

**Visual tone:** contained, ordered, small. The office is the opposite of the classroom — small and orderly where the classroom was large and chaotic. The architecture of the environment is the architecture of the disappearance-of-reports: small rooms, contained, ordered.

### 4.2 Runtime & Format

- **Runtime:** ~3:00–3:30. Most interactive of the three fragments.
- **Format:** Mixed — interactive + authored beats. Includes the fragment's most painful mechanical moment (see §4.6).

### 4.3 Player Agency Scope

**Primary choice:** `[PLAYER CHOICE — Mira's Report]` (manuscript line 663)

Three options:
- **FORMAL** — "Ms. Aizawa, I need to file a report about Yui Sakamoto."
- **DIRECT** — "Yui's being hit. By her mom's boyfriend. She has bruises."
- **PLEADING** — "Please listen to me this time. This is important."

Each branches the exchange. The FORMAL path is the slowest and most complete. DIRECT is fastest. PLEADING is the most emotionally raw.

### 4.4 Environmental Examine Elements

Four elements (one more than other fragments — Aizawa's office is the richest environment):

| Element | Mira's observation |
|---|---|
| **The wall calendar** | Dates circled in different colors. Mira notices the system — Aizawa has a filing rhythm. Some dates are dated (past reports filed); some are future (scheduled follow-ups). |
| **The sanitizer bottle** | Mira notices it. This is pre-sanitizer-click-mechanism; Aizawa uses it normally in this memory. The sight of the normal-use bottle is the player's first encounter with it, and in the present-day timeline the click signature is already established. The difference is the tell. |
| **The plant** | Not watered. The plant is on the windowsill, but no water is near it. Mira notes: Aizawa remembers her filings, not her plant. |
| **The filing cabinet** | Closed. Mira can see it is the source of the forms on the desk. She does not open it. |

### 4.5 Branching Exchange

Each branch leads through a dialogue sequence (authored in the manuscript). All three converge on the same all-paths moment: Aizawa filing the report.

FORMAL: Aizawa responds procedurally. Asks dates, names, specific observations. Writes every word. "I'm going to document this and make sure it reaches the right people."

DIRECT: Aizawa responds to the data flow without interrupting. "You checked the schedule." Then: "Okay. I'm documenting this. I'll flag it for review."

PLEADING: Aizawa looks up. Fully. "This time" lands. "I always listen to you, Mira." Mira: "Listening isn't the part I'm worried about." Beat. Aizawa writes the date.

### 4.6 The All-Paths Filing Sequence

This is the fragment's mechanical core — and the single most painful beat in any fragment.

1. Aizawa finishes writing the form. Two pages, dense with Mira's report. Dated. Signed.
2. Aizawa opens a drawer. The drawer contains identical forms — stacked, organized by date.
3. **THE PLAYER, AS MIRA, CAN SEE THEM.** Previous reports. Previous filings. The same format, the same handwriting, the same drawer. These are the stack of Mira's own prior reports — and other children's prior reports, which Mira does not recognize but the player will recognize as the foundation of the dismissal pattern the game is investigating.
4. Aizawa places Mira's new form in a manila folder. Labels it. Puts it in the outgoing tray.
5. Aizawa: "I'm going to file this with the safety council. They review all reports about student welfare. Mr. Endo chairs the committee — he takes these things very seriously."
6. Mira (player-as-Mira, no branch choice): "What happens next?"
7. Aizawa: "The council reviews it. They'll follow up with the family if they determine it's warranted."
8. Mira: "When?"
9. Aizawa: "That depends on their review schedule. Usually within a few weeks."
10. The player, as Mira, processes "a few weeks." (The manuscript states: "a geological age. A few weeks is how many more Wednesday gym classes Yui will attend with bruises on her left arm.")
11. Mira: "...okay."
12. Mira turns to leave. Hand on the doorknob.
13. Aizawa: "Mira?"
14. Mira turns back.
15. Aizawa: "You did the right thing."
16. Hold on Mira in the doorway. The form in the tray. The system received the report.

### 4.7 Fixed Outcome

Mira walks out. The hallway is full of children. The bell is about to ring. Somewhere in the filing system, a folder with Yui's name is being routed to a committee chaired by a man who will read it, note it, and ensure it produces nothing.

### 4.8 Notebook-Deposit Entry

> *"I did the right thing. Nothing happened."*

This is Mira's observation of the pattern the entire game investigates.

### 4.9 Voice Direction

**Mira (nine, fragment):**
- The same age as her ghost-voice. This is the most recent of the three fragments (six months before her death).
- Emotional state: determined. She has learned from the Rina fragment to document. She has learned from the Reiko fragment to speak clearly. She is trying a new channel (the institutional one) with what she learned.
- FORMAL path: adult-mimicry. She is performing competence. The performance is precise but slightly off — a child imitating a register.
- DIRECT path: her native mode. Data flow. Precise. Fast.
- PLEADING path: "This time" — the weight in her voice is the weight of the prior Reiko and Rina fragments. A player who has done the previous two fragments hears the accumulation.

**Aizawa (fragment):**
- Younger than her present-day register. More hopeful. The sanitizer-click mechanism has not yet become her signature — she uses the sanitizer normally.
- Her listening is real. Her belief is real. The tragedy is that she is perfectly capable of acting and she chooses procedure instead.
- "You did the right thing, Mira" delivered warmly, without irony. Aizawa does not know what she is becoming.

### 4.10 Camera Direction

1. **Entry:** close on the office door from Mira's POV. Door opens. Aizawa at her desk.
2. **Mira's opening line:** medium on Mira. Aizawa's reaction in partial frame.
3. **Branch-specific exchange:** alternating mediums — Mira, Aizawa, Mira, Aizawa. Standard shot-reverse-shot.
4. **The filing beat:**
   - Close on Aizawa's pen. The writing happens in real time. The camera holds on the pen.
   - Cut to the drawer opening. CLOSE on the identical forms. The stack is the scene's emotional anchor. Hold ~4 seconds.
   - Cut back to Aizawa. She does not notice the player's attention.
5. **The "a few weeks" beat:** close on Mira's face. Her reaction to the timeline. The player watches the math happen in her expression.
6. **The doorway beat:** wide shot. Mira at the door. Aizawa at the desk. The form in the tray between them.
7. **Final beat:** Mira turns back after Aizawa calls her name. The two-shot. "You did the right thing." Mira does not respond — the silence is the answer. Mira walks out.
8. **Exit transition:** hold on the hallway beyond the door for ~2 seconds. Children crossing. The bell.

### 4.11 Audio Direction

**Ambient bed:**
- Muffled hallway sounds (children moving between classes; a bell, distant)
- Faint fluorescent hum
- The office is the quietest of the three fragment environments

**Tics:**
- Aizawa's pen (writing, deliberate)
- Paper being placed in the folder
- The drawer opening (a mechanical slide — the sound should be recognizable as the sound the filing cabinet makes in the present-day Aizawa office scenes)

**Critical audio beat:** the sanitizer bottle. Mira notices it on the desk. In this memory, it is not clicking. It is full, untouched, normal-use. The player who has heard the present-day Aizawa click hears the absence here and understands what the click became.

**Transitions:**
- Entry: wire-sound resolves into the office's quiet. The hallway sounds begin faintly. The player feels the closed-door isolation.
- Exit: hallway sounds crescendo as Mira opens the door. The bell rings just as the transition begins. The real-world bell is cut off by the fade.

### 4.12 Higashino-Lens Layer

**Higashino-lens layer:** The procedural wall the player watches in this fragment is the same professional skill Aizawa uses twice in the hidden acts design: once to protect Mira (the altered report — softening disciplinary language, Ch 5-7 evidence) and once to bury her (classifying the notebook as "personal effects, non-evidentiary," Ch 7-9 evidence). "Same handwriting. Both times." — this line from the Ch 8 confrontation extension connects directly to what the player witnessed in the fragment. The fragment shows the skill. The investigation shows the skill deployed in both directions.

**Production note:** The fragment should emphasize Aizawa's competence, not her failure. She files correctly, documents thoroughly, follows procedure. The horror is that the procedure is working exactly as designed — and that "working" means nothing happens. The hidden acts layer adds: this same competence was also, once, an act of love.

---

## 5. PRODUCTION DELIVERABLES

### 5.1 Art Assets (Per Fragment)

Each fragment requires:
- Location bed (kitchen / classroom / counselor's office) — see `deadringer_locations.md` for reference
- Character models: young-alive Mira (3 age variants — eight, nine, younger), young-alive Reiko, young-alive Aizawa, Rina, Ms. Tanaka, 20 classroom-ambient children
- Examinable object art (10 objects total across three fragments)
- UI for the TEXT ON SCREEN framing elements and the notebook-deposit entry

Reiko fragment and Aizawa fragment share some asset overlap with their present-day locations (Reiko's apartment, Aizawa's office). Rina fragment's classroom is unique to the fragment — unless the classroom is reused in a memory or flashback elsewhere, this is single-use.

### 5.2 Audio Assets (Per Fragment)

- Ambient beds (3 unique beds)
- Character vocal performances: young Mira (three variants), young Reiko, young Aizawa, Rina, Ms. Tanaka
- Foley: paper sounds, pen writing, drawer opening, door handle, classroom chair-scrape, fridge cycling
- Transition assets: entry transition (wire-sound rise + child's voice + fade), exit transition (wire-sound carrying the key line + fade)

### 5.3 Animation / Rigging

Fragments require limited animation:
- Standing / head-turning for Mira
- Seated animations for Reiko (at table), Aizawa (at desk), Rina (at cluster)
- Walking (short, authored) — Mira crosses kitchen in Reiko fragment, crosses classroom in Rina fragment (DIRECT path), turns at doorway in Aizawa fragment
- Face animation for emotional beats (Aizawa's full-attention pivot in PLEADING, Reiko's dismissal expression, Rina's certain denial)

### 5.4 Playtest Priorities

1. **The fixed-outcome design.** Do players feel the game's resistance, or do they feel railroaded? The distinction is emotional; playtest with careful qualitative observation.
2. **Examine rates.** How often do players examine environmental elements? If examination rates are low, consider adding visual affordances (subtle highlight, cursor change) without over-signposting.
3. **Runtime pacing.** Each fragment should feel contained but not rushed. If players report feeling "it was over too fast," extend the camera holds. If they report "it dragged," tighten the branch-specific exchanges.
4. **Emotional load.** The three fragments are Dead Ringer's most directly-painful scenes. Playtest for burnout — can a player reasonably complete Ch 5 (all three fragments experienced by now) in a single session without emotional exhaustion? If not, the game's natural pacing should encourage breaks.

### 5.5 Open Questions

1. **Young Mira voice actor.** Is it the same actor as ghost-Mira with pitch/filter variation, or a different actor for the younger register? Recommendation: same actor, different takes. The continuity of voice is load-bearing.
2. **Fragment skip on NG+.** Can the player skip fragments they've completed on NG+? Recommendation: yes, skip available. The fragments are designed as first-experience beats; replay value is not their purpose.
3. **Subtitle styling.** TEXT ON SCREEN framing beats ("This is a memory. You are Mira.") — styled differently from in-scene subtitles, or same style? Recommendation: same style, centered, slightly larger, no speaker attribution.
4. **Autosave timing.** Autosave at fragment entry AND exit, or only entry? If a player quits mid-fragment, do they resume at start (lose progress) or at mid-point? Recommendation: autosave at entry only. Fragments are indivisible by design; mid-fragment resume would dilute the scene's integrity.
5. **Camera motion sensitivity.** For players with motion sensitivity, provide an option to lock all camera movements to hard cuts rather than pans/dissolves. Confirm during accessibility review.

---

## 6. CROSS-REFERENCES

- `deadringer_systems.md` §4 — Memory Fragment System design
- `deadringer_notebook_system.md` §7.2 — how Memory Fragments deposit into the Log
- `deadringer_locations.md` — environmental references
- `deadringer_audio_signatures.md` §2, §5 — wire-sound transitions, voice direction
- Chapter files: `chapter_03.md`, `chapter_04.md`, `chapter_05.md` — manuscript source

---

**END MEMORY FRAGMENT PRODUCTION SPECIFICATION**
