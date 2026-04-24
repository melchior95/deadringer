# DEAD RINGER — Systems & Gameplay Specification

Production specification for the systems and mechanics that together constitute Dead Ringer's gameplay. This document consolidates system-level design from the game bible, chapter files, character bible, and chapter structure into a single referenceable spec.

**Scope of this document:** Call System, Intent System, Soul Read System, Memory Fragment System, Call Slot Economy, Partner Degradation System, Contradiction System, Meta/UI.

**Scope excluded (covered elsewhere):**
- **Notebook system** → `deadringer_notebook_system.md` (separate spec, cross-referenced throughout)
- **Locations** → `deadringer_locations.md`
- **Characters** → `deadringer_characters.md`
- **Information economy and chapter-by-chapter progression** → `chapter_structure.md`
- **Thesis and high-level design philosophy** → `deadringer_game_bible.md`

**Design principles that cut across every system in this doc:**

1. **Listening is the core mechanic.** Every system is in service of the player learning to listen — to audio signatures, to what NPCs avoid saying, to the rhythm of silence, to Mira's thinning voice. Mechanics that reward listening over pushing are the design priority.
2. **Mira is a resource.** Every read, every intercept, every clear signal costs her. The game's most honest mechanical stake is the partner degrading as a consequence of use.
3. **The phone can be refused.** NPCs can hang up, shut down, or decline to call back. Every successful call is earned. No NPC is a compelled witness.
4. **Failure is rarely absolute.** A wrong intent produces worse information, not no information. A missed detail can be recovered later via a different path. The investigation converges; the player's path through it branches in texture, not in outcome.
5. **Diegesis over chrome.** Where possible, mechanics present as in-world elements (a pocket notebook, an audio hum, a call screen) rather than UI abstractions (health bars, meters, XP). The game's register is "a detective doing his job," not "a player optimizing a system."

---

## 1. THE CALL SYSTEM

The call is Dead Ringer's primary interaction verb. Every chapter except Ch 2 (pure exploration) is structured around calls. The call system must handle: dialing, waiting, picking up, carrying on, intercepting, and hanging up.

### 1.1 Call Screen Architecture

The call screen is an overlay UI that dims the investigation scene behind it and foregrounds the phone. Elements:

- **Caller identity strip** — name + small portrait if known; "UNKNOWN NUMBER" or "ID WITHHELD" if not
- **Dialogue text area** — lower third of screen, character dialogue
- **Intent selector** — five available intents (see §2), shown at decision points
- **Compact notebook icon** — opens the in-call compact notebook (see notebook spec §6)
- **Ambient audio layer indicator** — subtle waveform visualization at the top edge, showing the wire-sound and NPC audio signature (defaulting to "off" for sound-off players but critical when on)
- **Call timer** (optional, not always visible) — some calls have explicit durations; most do not show a timer

The background investigation scene remains partially visible behind the call. This is deliberate: the player is always somewhere while making a call, and that somewhere affects the call's weight. A call from Kenji's apartment carries different emotional charge than one made from outside the community center.

### 1.2 Call Lifecycle

```
  [Dial / Pick up]
          ↓
  [Connect — ring count, pause length, initial greeting]
          ↓
  [Opening exchange — NPC sets their register]
          ↓
  [Player choice: Intent]  ← multiple rounds
          ↓
  [NPC response — including audio signature changes]
          ↓
  [Soul Read (optional, post-call)]
          ↓
  [Notebook prompt(s) fired]
          ↓
  [Call ends — hang-up, shutdown, mutual disconnect]
```

Each phase has design considerations:

**Ring count / pause length** — how a call begins tells the player what kind of call it is. Reiko picks up on the second ring; she was waiting. Yui picks up on the fourth ring after a pause, checking caller ID first. Doi lets it ring six times. Kaito takes three seconds after picking up before saying "...yeah." These openings are character information delivered mechanically.

**Opening exchange** — the NPC's first sentence establishes their audio signature and their current register (rehearsed, guarded, curious, hostile, etc.). The player should have enough data by the first player-choice point to recognize the approach that will work.

**Intent rounds** — a call usually has 2–4 intent choice points. Each advances the conversation state. A call can end in the middle of an intent round if the player's choice triggers a shutdown (see §1.4).

**Soul Read** — post-call, Mira delivers a read (or doesn't — Reads are a consumable resource, see §4). The read is the player's second pass on what just happened.

**Notebook prompts** — fire during or after the call, adding Log entries (see notebook spec §3).

### 1.3 NPC Audio Signatures

Every significant NPC has a unique audio signature — the ambient sound of their environment + their personal vocal/behavioral tics. This is Dead Ringer's replacement for PW's character portraits. Signatures must be:

- **Immediately recognizable** (a player who has called an NPC once should recognize them in Ch 11 without seeing caller ID)
- **Consistent across chapters** (the core signature doesn't change; specific variations signal state)
- **Readable without sight** (the game can be played with visuals minimized; the signatures carry character information through audio)

Signature map (as established in the manuscript):

| NPC | Signature |
|---|---|
| **Reiko** | Apartment that's too quiet for one person. Clock tick. Kettle cooling. No TV. The specific quiet of a home where one person lives in the space two people made. |
| **Doi** | The store is always on — fluorescent buzz, register beeps, door chime, compressor hum. The man says as little as possible, but the store's noise never stops. |
| **Yui** | Curated absence. No TV, no music, no footsteps. The careful quiet of a room chosen because it's the room where sounds don't carry. Fabric shifts — she's on something soft, positioned for a fast exit. |
| **Rina** | Ambient social context — other voices in the distance, a playground, a school hallway. She is always in a populated space. |
| **Haruki** | Pen clicking. Chair squeaking. Papers shuffling. Overflow motion. The tell: once per call, everything stops for 2–3 seconds. |
| **Aizawa** | The sanitizer click. Mechanism only — the pump doesn't complete. Steady rhythm = composed. Rate increasing = pressure. Stopping = break. |
| **Fumiko** | The pen never stops scratching. Workspace after hours. Filing cabinet closing. The sound of someone always documenting. |
| **Kaito** | The unfiltered room — fan oscillating, clock with loud second hand, refrigerator cycling, pencil tapping arrhythmically. Every appliance audible. |
| **Endo** | Measured silence. Clean line. Little ambient. The absence of fidget. His breath is even enough to be audible between sentences. |

Signatures are set by the sound designer in pre-production. No signature should be reused between NPCs. If a new NPC is added in DLC or sequel content, their signature must be designed fresh.

### 1.4 Call Failure States

A call can end in several ways:

**MUTUAL DISCONNECT** (default) — the conversation reaches its designed endpoint, both parties acknowledge, the call ends. No penalty.

**HANG-UP** — the NPC ends the call prematurely because of a player action. Triggered by: sustained pressure on an unready NPC, a caught bluff, a question crossing a specific trust line. The call ends with fewer notebook prompts and no post-call Soul Read. Most NPCs can be re-called later, but the re-call opens with their audio signature shifted (Doi goes more polite; Yui goes quieter; Rina goes cheerier). The door isn't closed, but the register is recalibrated.

**SHUTDOWN** — the NPC stops engaging without hanging up. They continue to pick up but give minimal answers. Distinct from hang-up because the player can tell the NPC is still there; they're just not giving anything. Primary triggers: pushing Yui on dangerous topics, sustained bluff against Fumiko.

**OFF-SCREEN LOSS** — an NPC is made unreachable by a different NPC's action. Primary case: Endo's Ch 12 social-capital calls can turn certain NPCs against the investigation. The player calls them and gets voicemail or a cold "I don't think I should speak with you further."

**TIME WINDOW CLOSED** — Yui's 1–3 PM window specifically. Calling outside the window produces no pickup. This is the only time-gated call in the game's main line.

### 1.5 Incoming vs. Outgoing

Most calls are player-initiated. The exceptions matter.

**Haruki's first call (Ch 5)** — incoming. The phone rings; the player can answer or let it ring. Letting it ring defers the call one scene and starts the relationship slightly colder.

**Endo's first call (Ch 8)** — incoming. This one is mandatory — the player answers. The mandatoriness is the point: Endo is calling Kenji, not the other way around, and that inversion is the chapter's central unease.

**Reiko's static call (Ch 9)** — can be either direction depending on the player's path. If the player calls first, Reiko's disclosure arrives as confession. If Reiko calls first, it arrives as arrival — she has been waiting for permission to speak.

**Ch 12 — multiple incoming calls** — Fumiko opens the chapter; Endo's calls to other NPCs are "overheard" through Mira's intercept rather than answered. The call direction in Ch 12 is the chapter's chaos.

### 1.6 Payphone Logic (Minor)

Yanagi has exactly one remaining payphone, outside the community center. Mira avoided it while alive — her instinct, never explained, proved correct (the payphone is above the exchange). The player never uses this payphone. It's a visual detail.

Kenji uses an internal-department phone in certain scenes (retrieving Mira's evidence box from the precinct) and his personal work phone for everything else. Only one phone matters for gameplay: the work phone, plus the dead phone in the drawer that Mira called him on at 3:47 AM. The dead phone does not appear in the standard call UI. It is where Mira's voice comes from. Its use is strictly story-gated.

---

## 2. THE INTENT SYSTEM

Dead Ringer's replacement for Phoenix Wright's Press/Present binary. The player chooses an intent rather than specific words; the NPC responds based on the intent + their state + prior trust. Five intents are available from Ch 3 onward.

### 2.1 The Five Intents

1. **REASSURE** — build trust, open guarded NPCs, lower defenses. Risk: appears soft, NPCs who need urgency respond poorly.
2. **PRESSURE** — force information, name the evasion. Risk: shutdowns, hang-ups, and with the Dignity Filter (Doi), escalating politeness that closes the door with a thank-you.
3. **REDIRECT** — steer the conversation sideways, change topic, ask about context rather than content. Risk: can feel unfocused; late-game Endo fills the redirect space with preferred narratives.
4. **REMAIN SILENT** — say nothing, let the NPC fill the space with their own anxiety. The game's dominant mechanic; teaches the player that listening is a tool.
5. **BLUFF** — claim knowledge you don't have. High risk, high reward. NPCs who see through a bluff recalibrate faster; NPCs who don't become more forthcoming.

Not every intent is available on every call. The choice set is authored per scene. A call might show only REASSURE / REDIRECT / SILENT — because the scene's emotional logic rules out PRESSURE and BLUFF. The absence of intents is a design signal as strong as their presence. Example: Ch 9 Reiko static call offers REASSURE / REDIRECT / SILENT only. PRESSURE and BLUFF would be cruel in a confession scene.

### 2.2 Intent × NPC Matrix (Simplified)

A full matrix is a tuning document produced during build. High-level:

| NPC | Best | Worst | Notes |
|---|---|---|---|
| **Reiko** | SILENT / REDIRECT | PRESSURE | She's rehearsed. Silence lets the rehearsal collapse under its own weight. |
| **Doi** | SILENT | PRESSURE | The Dignity Filter. Pressure makes him more polite, not more honest. |
| **Yui** | SILENT | REASSURE | She's been reassured her whole life. Silence is the only approach she hasn't been trained against. |
| **Rina** | REDIRECT | PRESSURE | She fills silence with social performance. Redirect catches her when she's not prepared. |
| **Haruki** | Any (he overflows anyway) | — | Overflow means he tells you too much no matter what. The risk is managing what you share back. |
| **Aizawa** | REDIRECT | PRESSURE | Procedural walls can't be pushed. They must be circled. |
| **Fumiko** | BLUFF (risky) / TRADE-framed REASSURE | WITHHOLD | Transactional. Sharp. She detects bad-faith approaches. |
| **Kaito** | SILENT / PATIENCE | DIRECT | Delayed Signal. Silence gives him space to process. |
| **Endo** | REDIRECT | PRESSURE | Locked room. Silence doesn't break him; he fills it. Redirect maps his boundary. |

"Best" means "produces the most information and highest trust gain." "Worst" means "produces shutdown, hang-up, or maximum recalibration."

### 2.3 Progression Across Chapters

The player learns the intent system by watching which intents work against which NPCs. The progression is staged.

**Act I (Ch 1–3):** all intents experimentally offered; calls are forgiving; failure modes are visible but non-punitive.
- Ch 3 Doi call teaches PRESSURE's failure mode (the Dignity Filter).
- Ch 3 Reiko call teaches that REDIRECT unlocks information guarded by performance.

**Act II (Ch 4–7):** SILENCE emerges as the dominant mechanic.
- Ch 4 Yui call: silence produces the fragments reassurance cannot.
- Ch 6 Doi confession: silence lets the false confession collapse.
- The player internalizes that listening is a tool.

**Act III (Ch 8–10):** Endo breaks the pattern.
- SILENCE doesn't work on Endo (he fills it comfortably).
- REASSURE is irrelevant (he provides it).
- PRESSURE is ineffective (he recalibrates).
- The player must learn REDIRECT as the late-game dominant mechanic.

**Act IV (Ch 11–12):** all five intents deployed simultaneously across multiple NPCs.
- Ch 12 switchboard duel uses different intents for different NPCs in the call war.
- Mastery = using the full toolkit fluently.
- The player who relied on a single strategy is outmatched.

### 2.4 Sub-Mechanics: Per-NPC Filters

Some NPCs have named filters that modulate intent responses. These are authored per character.

**The Dignity Filter (Doi):** under any form of direct pressure, Doi becomes more polite rather than more honest. Escalating courtesy is his resistance. The player must bypass the filter (silence) or circle it (redirect). Established Ch 3, broken Ch 6 via silence during his false confession.

**The Rehearsal (Reiko):** Reiko has rehearsed answers to common questions. Direct questioning produces the rehearsed version. Silence or redirect causes her to depart from the script, which is where the truth lives. Established Ch 3, broken Ch 9 via static call and Ch 11 via the notebook scene.

**The Performance (Yui):** Yui has a performed voice for adults who might check on her. Direct questioning gets the performance. Silence lets the performance exhaust itself. Established Ch 4.

**The Overflow (Haruki):** Haruki can't not talk. The intent choice mostly shapes what direction he overflows in. The risk isn't getting too little; it's managing how much to feed him without triggering a Point of No Return (Ch 6).

**The Sanitizer Rate (Aizawa):** The click rate is the state indicator. Slowing = reassurance working. Speeding = pressure bearing down. Stopping entirely = break. The player listens for the rhythm.

**The Locked Room (Endo):** Endo cannot be read. Intents modulate how he redirects, not whether he breaks. See §4.5.

### 2.5 Diagnosability — How the Game Teaches Why an Intent Worked

A player-facing concern: when a call goes poorly, can the player retrospectively understand why? Without diagnosability, the intent system becomes guessing.

The game teaches through three channels:

1. **Mira's commentary.** After a call or mid-call during a visible error, Mira names what happened. "Stop. You're losing her." or "He's doing the voice." This is the most immediate feedback channel.
2. **Character Note updates.** After each call, the NPC's Character Note (notebook spec §3.1) updates with observations about the approach that was tried. "Pressure produced escalating politeness" phrased as observation, not instruction.
3. **Audio signature shifts.** The player hears the NPC's state change mechanically — Aizawa's clicks speeding up, Haruki's overflow going silent, Doi's courtesy hardening. The audio IS the feedback.

The game never shows a numeric "trust score" or a meter. Feedback is tonal and observational. This is a deliberate design choice — it preserves the register of "detective noticing things" over "player optimizing a stat."

### 2.6 Intent Lessons as Character Notes

Each NPC's Character Note accumulates a "What Has Worked / What Hasn't" section across the game. This section populates automatically from call outcomes. By Ch 7, the player has a reference for each major NPC that reads something like:

> **DOI**
> Best approach observed: Silence (Ch 3 redirect produced honest observation; Ch 6 silence produced confession collapse).
> Worst approach observed: Pressure (Ch 3 produced escalating politeness → courteous disconnection).
> Notes: Dignity Filter active. Wants to maintain composure. Will tell truth when given space to arrive at it rather than produce it on demand.

This is the notebook doing double duty as intent diagnostics. See notebook spec §7.4.

---

## 3. THE SOUL READ SYSTEM

Mira's reads are the game's signature mechanic. A read is a post-call (or post-scene) impression of a person or space, delivered in Mira's voice, filtered through her sensory vocabulary.

### 3.1 What a Soul Read Is

A Soul Read is **not mind-reading.** Mira does not access specific thoughts, hidden memories, or factual content. She reads *emotional weather* — pressure, fracture, warmth, distance, what a room or person is carrying. Her readings are metaphorical. They are accurate without being admissible.

Example: Doi's read in Ch 6 — "He's loud inside. Like a room where every radio is on a different station." This is a description of guilt-performance-under-pressure rendered as an acoustic metaphor. It is accurate. It is useless as evidence. It is critical as a decoding key.

### 3.2 Reads as Consumable Resource

**Every Soul Read costs Mira.** In the early game this is implicit — reads arrive instantly, richly, without visible exhaustion. Across the chapters, reads become slower, shorter, thinner. By Ch 9 the player has to decide which calls are worth spending a read on. By Ch 11 reads fail mid-delivery.

This is Dead Ringer's most uncompromising mechanical choice. The partner-as-resource framing makes every call feel like a withdrawal from a finite account. The account is Mira. See §6 for the full degradation curve.

### 3.3 Read Structure

Every read follows a loose template:

1. **Initial impression** — one or two sensory words (warmth, pressure, noise, cold, tangled)
2. **Metaphor** — the core reading, rendered as an analogy
3. **Personal note** — Mira's opinion, if she has one
4. **Practical note** — what this means for the investigation, if relevant

Not every read includes all four. Kaito's Ch 7 read has 1, 2, and a brief 3. Endo's Ch 8 read has 1 and an *incomplete* 2 — the locked room is exactly the absence of the rest of the template.

### 3.4 Read Failure Modes

Reads can fail in several ways, each mechanically distinct:

**DELAY** (Ch 4–7) — the read arrives, but later than usual. A beat between the call ending and the read beginning. Not a failure; an early warning.

**THINNING** (Ch 7–9) — the read arrives at normal time but shorter. Missing the practical note, sometimes missing the personal note. The player notices Mira skipping the parts she used to volunteer.

**MID-READ CUTOUT** (Ch 11) — the read begins and stops. Mira reaches for the next word and can't find it, or her voice drops to static mid-sentence. The player gets partial information.

**REFUSED READ** (Endo) — Mira attempts the read and hits the Locked Room. She reports back that she can't read him. Not exhaustion; incompatibility.

**AMPLIFIED READ** (Ch 10 only) — the read returns to Ch 1 richness because the exchange infrastructure carries her signal. Temporarily. This is a positive failure mode — the read is too rich, which tells the player something is structurally unusual about the environment.

### 3.5 The Locked Room (Endo-Specific)

Endo cannot be read. The game establishes this explicitly in Ch 8. Mira tries: "He's..." Long pause. "I can't get in. It's not like Reiko where there's a door and I can feel what's behind it. This is... there's no door. It's just wall. All the way around."

Mechanical consequence: the player cannot use reads to decode Endo. They must rely on other channels — informational tells, behavioral redirections, cross-reference with other NPCs' observations of him. This is the Contradiction System's moment (§7).

The Locked Room is also thematic: Endo's interiority is not available to the game's reading tool because he has spent fifteen years learning to not leak. He is the only NPC who mastered the listening infrastructure enough to stop producing signal himself.

### 3.6 Amplification (Ch 10)

In the exchange room, Mira's signal clears. Reads return to full richness for one chapter. The contrast with Ch 8–9's stripped reads is the chapter's emotional peak — the player remembers what they've been losing.

Mechanically:
- Ch 10 reads have no delay
- Full template (impression + metaphor + personal + practical)
- Readability of adjacent residues (the other children in the cables) — a new read capability, unique to the exchange room
- Proximity reading of Endo (not a full read, but the shape of his attention through residue — see Ch 10 Scene 7)

Amplification is a one-chapter state. It is structurally a gift and mechanically a signal that the exchange infrastructure is doing something no other environment can.

### 3.7 The Final Signal (Ch 12)

In Ch 12, Mira uses the last of her signal not to deliver a read but to make a single clear transmission: a phone-to-phone call to Sora. This is not a Soul Read. It is the mechanical consumption of everything Mira has left.

After the call to Sora, Mira is gone. The wire-sound persists (she is now part of the infrastructure, per her Ch 10 realization) but the voice does not return. The player has consumed the resource to its conclusion. The design commits to that consumption — there is no "she comes back for the epilogue" mechanic.

---

## 4. THE MEMORY FRAGMENT SYSTEM

Three interactive Mira-POV scenes punctuate Acts I and II. Each is a fixed-outcome sequence where the player controls Mira in a moment she experienced while alive.

### 4.1 Architecture

A Memory Fragment is triggered by a specific chapter beat (always post-call, always after an emotionally charged revelation). When triggered:

1. The current scene dissolves.
2. A TEXT ON SCREEN marker appears: *"This is a memory. You are Mira."*
3. The player's perspective shifts — first-person, from Mira's height (approximately 130 cm).
4. An interactive scene plays out with a limited, authored set of player choices.
5. The scene resolves at a fixed outcome.
6. The scene fades and the player returns to Kenji's apartment (or wherever the current scene was).

### 4.2 The Three Fragments

All three are fully written in the manuscript:

| Fragment | Chapter | Location | What Mira Reports | Outcome (fixed) |
|---|---|---|---|---|
| **Reiko Denial** | Ch 3 | Kitchen | "A man keeps watching the school when we get out." | Reiko dismisses. |
| **Rina Social Distortion** | Ch 4 | Classroom | Mira's notebook is missing; Rina has it. | Teacher sides with Rina (non-maliciously). |
| **Aizawa Procedure** | Ch 5 | Counselor's office | "Yui's mom's boyfriend hits her. She has bruises. No gym on Wednesdays." | Aizawa files the report. Nothing moves. |

Each fragment has three player-choice branches (CAREFUL / DIRECT / URGENT for Reiko; DIRECT / CAREFUL / OBSERVE for Rina; FORMAL / DIRECT / PLEADING for Aizawa). All paths converge on the same outcome. The branches affect the texture of the dismissal, not whether it happens.

### 4.3 Player Agency Scope

Inside a Memory Fragment, the player can:
- Choose between authored dialogue options (Mira's words, 2–4 choices per beat)
- Examine the environment (a small number of diegetic elements — the step stool, the fridge magnets, the counselor's desk drawer of filed reports)
- Advance the scene

The player cannot:
- Leave the scene early
- Pursue alternate actions outside the authored choices (no "run away," no "punch Reiko")
- Change the outcome

This is the deliberate design constraint. Memory Fragments are not puzzles. They are experiences of authored dismissal, delivered interactively so that the player feels agency that does not matter. The discovery that the outcome is fixed is the point.

### 4.4 Fixed Outcome — Design Rationale

Why not branch on outcome? Because branching would imply that Mira's failure was preventable by a better choice on her part. It wasn't. The thesis of Dead Ringer is that Mira delivered correct information and the adults around her did not act on it — the failure was not hers, and offering the player the illusion that it could have been would betray the story's argument.

The fixed outcome, arrived at through agency that doesn't alter it, is the mechanical rendering of that thesis.

### 4.5 Return-to-Present Mechanic

Each Fragment ends with a specific transition:
- The memory thins (visual — warm light dissolves)
- The wire-sound rises briefly, carrying a child's voice at the threshold of hearing
- What returns is Kenji's apartment, the case file, the phone
- Often: a TEXT ON SCREEN element that becomes a notebook entry (e.g., Reiko Denial ends with *"'Can't' and 'won't' are different."*)

The transition is consistent across all three fragments. Players learn the transition's shape; by Ch 5 it is recognizable.

### 4.6 Text-on-Screen Conventions

Fragments use text-on-screen in two ways:
1. **Framing text** — *"This is a memory. You are Mira."* at entry. One use per fragment, at start.
2. **Notebook-deposit text** — the line Mira wrote in her notebook as a result of this experience. Appears at fragment close. Deposits a notebook entry (a child's observation, written down, now permanent).

No other text-on-screen is used in fragments. The rest is dialogue and environmental description.

### 4.7 Integration with the Notebook

See notebook spec §7.2. Fragments produce MEMORY FRAGMENT-type entries that are not presentable as confrontation evidence (they're experiences, not facts) but are cross-referenced from NPC Character Notes. After the Aizawa Procedure fragment, Aizawa's Character Note shows "Mira reported Yui's abuse — documented, filed, no action" as a linked entry. This is how the Fragment's emotional weight persists into later gameplay.

---

## 5. CALL SLOT ECONOMY

The phone is a finite resource. The player cannot call every NPC in every chapter. Scarcity is the mechanism that forces prioritization.

### 5.1 Per-Chapter Slot Allocation

Based on the manuscript:

| Chapter | Available NPCs | Slots | Notes |
|---|---|---|---|
| Ch 1 | Mira (incoming) | 1 | The hook call; player cannot initiate |
| Ch 2 | None | 0 | Pure exploration chapter |
| Ch 3 | Reiko, Doi, Bridge | 3 | Generous — all three calls available, no competing demand |
| Ch 4 | +Yui, +Rina | 3 of 4–5 | First forced prioritization; Yui has a time window |
| Ch 5 | +Haruki, +Aizawa | 3 of 4 | Haruki's call is incoming (mandatory) |
| Ch 6 | +Fumiko, +Kaito | 3 of 5 | Doi's false confession may pre-empt a slot |
| Ch 7 | Full Act II roster | 4 of 8 | Peak scarcity of Act II; Fumiko blind spot can cost a slot |
| Ch 8 | +Endo (incoming) | 3 of 9 | Endo mandatory; Aizawa break available |
| Ch 9 | Full roster + paths | 3 "paths" + calls | Free-investigation structure; see Ch 9 |
| Ch 10 | Full roster | 2 of 8 | Investigation pivot; less information-gathering, more action |
| Ch 11 | Full roster + Endo confrontation | 3 case-assembly + 1 confrontation | Each call assembles a Board piece |
| Ch 12 | All, real-time | Variable | Switchboard duel (see §5.5) |

Slot counts are tuning parameters. The ranges above are targets; build-time tuning may adjust.

### 5.2 NPC Availability Windows

Most NPCs are reachable at any time within a chapter. The exceptions:

- **Yui (1–3 PM window)** — calling outside the window produces no pickup. In-chapter, the player has one 1–3 PM slot available per chapter.
- **Fumiko (48-hour publication timer)** — not a window, a clock. Once she introduces the timer (Ch 6), her cooperation has a decaying value. Calling too late produces premature publication.
- **Endo (incoming only, Ch 8)** — Endo calls Kenji in Ch 8. Kenji cannot initiate a call to Endo until Ch 9.
- **Sora (unreachable until Ch 12)** — no direct call is possible; Mira reaches him through the exchange.

### 5.3 Off-Screen NPC Communication

NPCs talk to each other between the player's calls. This is not random. Social logic authored per relationship.

| If the player calls... | These NPCs may learn about it... | Because... |
|---|---|---|
| Reiko | Haruki, school contacts | Reiko tells people the detective called |
| Rina | Community gossip network | Rina processes and redistributes |
| Haruki (with case details) | The family he visits (PoNR) | He acts on shared information |
| Fumiko (with too much) | Publication timeline accelerates | Her deadline is her own |
| Endo | Endo adjusts off-screen | He recalibrates after every call |
| Doi (during community pressure) | Community suspicion | Visible "suspect" contact |

This is the world reacting to the investigation's presence. The player's calls are not private.

### 5.4 Fumiko Publication Timer (Meta-System)

Fumiko has her own timeline. Introduced Ch 6: she's publishing in 48 hours regardless of the investigation. The timer is a soft real-time element — it progresses across chapters rather than in minutes.

- **Ch 6:** 48 hours on clock. Player can reduce by sharing information that slows her (she waits to verify).
- **Ch 7:** ~36 hours. Fumiko's blind spot can cost the player time inside the chapter.
- **Ch 8–9:** ~24–18 hours. The timer is tightening.
- **Ch 10:** ~12–10 hours.
- **Ch 11:** ~6 hours. Fumiko offers to publish early to frame Endo's obstruction as consciousness of guilt. Player choice.
- **Ch 12:** Resolves (she publishes). Her story becomes part of the Ch 12 call-war evidence chain.

The timer is Dead Ringer's equivalent of Ace Attorney's trial-day countdown, but negotiated rather than fixed. Players can extend or accelerate it through their interaction pattern. It is the game's primary global time pressure.

### 5.5 Ch 12 Switchboard Duel (Special Case)

Ch 12 breaks the per-chapter slot economy. The duel runs three interlocking systems:

1. **CALL WAR (SOCIAL)** — Endo burns social capital by calling Reiko / Haruki / Doi / district police / others. Player counters with their own calls, reinforcing trust and presenting evidence. Limited counter-calls per turn.
2. **INFRASTRUCTURE RACE (SURVEILLANCE VS. SIGNAL)** — Mira intercepts Endo's calls through the exchange. Player chooses which to monitor. Each intercept burns signal; the exchange degrades.
3. **EVIDENCE CHAIN (PHOENIX WRIGHT LAYER)** — Player presents contradictions during Endo's calls. Each redirection reveals more of what he's protecting.

All three systems run simultaneously. Slot management becomes a real-time strategy question — who can the player afford to lose? Slot count is not fixed; it is bounded by Mira's remaining signal and Endo's pace. The duel is designed to feel as though the phone itself is burning through.

---

## 6. PARTNER DEGRADATION SYSTEM

Mira's signal decays across the game. This is the game's most emotionally load-bearing mechanical choice. The system is primarily audio-visual (what Mira sounds like) rather than numeric (no meter).

### 6.1 The Curve

| Stage | Chapters | State |
|---|---|---|
| **Strong** | 1–3 | Full armor, unsolicited observations, full commentary between calls, sardonic. Reads are instant and detailed. |
| **First Waver** | 4–5 | Occasional pauses where there shouldn't be pauses. A word arriving slightly after the meaning. Easy to miss; easy to attribute to connection quality. |
| **Noticeable Decline** | 6–7 | Silences between calls. Loses words. Less unsolicited humor. The absence is what players notice. |
| **Degraded** | 8–9 | Speaks mainly during reads. Conserving. Reads take noticeably longer. Players adjust strategy around what Mira can still deliver. |
| **Temporarily Amplified** | 10 | Exchange room clears her signal. Ch 1 quality returns for one chapter. Devastating contrast. |
| **Post-Amplification Crash** | 11 | Worse than before. Reads cut out mid-delivery. Voice drops to near-static between calls. The exchange is degrading and so is she. |
| **Final Signal** | 12 | One last clear transmission — the call to Sora. Everything she has left goes into twenty words. Then static. Then the line goes dead. |

### 6.2 UI Manifestation

The degradation is never announced. No UI element tracks Mira's signal. The player notices because they've been listening to her voice for chapters and they know what she sounds like. The game teaches the player to listen — and then it takes away the thing they learned to listen to.

Specific audio-visual manifestations:

- **Wire-sound density** — the ambient hum that underlies every scene grows thicker, coarser, more crackling as chapters progress
- **Voice filter** — subtle high-frequency attenuation starting Ch 6, more aggressive Ch 8, near-radio-static Ch 11
- **Line drops** — quarter-second gaps in her speech, introduced Ch 7, increasing through Ch 11
- **Response latency** — from 0s (Ch 1) through 1s (Ch 5) through 3–5s (Ch 9) through mid-sentence failures (Ch 11)

### 6.3 Ch 10 Amplification (Special State)

In the exchange room:
- All degradation effects clear
- Voice is room-close, present, sharp
- Reads are full template, instant
- A secondary read capability appears (the other children's residue)

The amplification lasts from entry into the exchange room to the end of Ch 10. It ends hard, and Ch 11 opens on the crash.

### 6.4 Ch 11 Crash

The crash is mechanically worse than the Ch 9 degraded state. Every effect above is amplified:

- Wire-sound is now distorted, not just dense
- Line drops extend to full-second failures
- Response latency exceeds 5s on difficult questions
- Reads fail mid-delivery with observable frequency
- The Fumiko read attempt in Ch 11 Scene 3 is the mechanical demonstration of the failure state

### 6.5 Ch 12 Final Signal

Mira's Ch 12 behavior is partially restored (the exchange room still carries her, and the switchboard's active state gives her enough to work with) but the reserve is finite. Each intercept burns more. The final call to Sora is the mechanical end of the resource. After it, the voice does not return.

The design commits to permanence. Mira does not come back for the epilogue. The wire-sound in the Epilogue's Kenji scene is present but carries no voice.

### 6.6 Player Agency Around Degradation

The player has one meaningful decision around the degradation: which calls are worth spending Mira on. From Ch 8 onward, this means:

- Choosing to attempt a Soul Read vs. not requesting one
- Choosing which NPCs to call when multiple are available (some calls are harder on her than others)
- In Ch 12, choosing which of Endo's calls to intercept

The game does not quantify these costs. The player decides based on narrative priority and their sense of Mira's state. This is deliberately soft — the cost is emotional, not budgetary.

---

## 7. THE CONTRADICTION SYSTEM

Dead Ringer's replacement for Phoenix Wright's "present evidence against testimony" mechanic. Two types of contradiction exist; both are load-bearing.

### 7.1 Two Types of Contradiction

**Factual contradiction** — the familiar PW type. Statement A says X; Evidence B says not-X. Present B against A.

**Knowledge-level contradiction** — Dead Ringer's innovation. The question is not *what an NPC says* but *what they could possibly know.* An NPC reports a fact they shouldn't have access to. The contradiction is between the information and the NPC's access pattern.

Both types are detected and surfaced by the game; both contribute to the Ch 11 Board.

### 7.2 Entry-Level (Factual) Contradictions

Standard logic: when two notebook entries state incompatible facts, the game surfaces the contradiction. The player sees both entries linked with a visual indicator; a new CONTRADICTION entry is auto-created in the notebook.

Examples in the manuscript:
- Doi's canvass statement ("no relevant observations") vs. his Ch 6 testimony (three silver-car sightings with dates)
- Rina's Ch 4 description of Mira as "difficult and dramatic" vs. Mira's documented accurate reports
- The planted counselor notes vs. the counselor's retirement date

These work like PW contradictions. They are presentable in Ch 11 via the Board's FRAMING AUTHORSHIP slot.

### 7.3 Knowledge-Level Contradictions (The Endo Engine)

This is the game's most sophisticated contradiction logic. Rather than catching an NPC in a factual error, the game catches them possessing information they should not have.

Example (Ch 8): Endo describes Mira's "hesitation before delivering a report — the breath she took, like she was bracing for dismissal." Mira's reports were written. Filed through the school office. No recording of her voice during filings exists. Endo's description is accurate; Endo cannot legitimately possess the access required to have observed it.

The contradiction is between the *specificity of his knowledge* and the *plausible channels for that knowledge*. The player's job is to map the gap.

### 7.4 Detection & Surfacing

The game detects knowledge-level contradictions by comparing NPC statements against:
- Canonical facts (what's in evidence)
- Access inventories (what each NPC should be able to know given their documented role)
- Previously-established NPC knowledge (cross-reference with Character Notes)

When a mismatch is detected, the game surfaces a CONTRADICTION entry tagged as "KNOWLEDGE-LEVEL." Unlike factual contradictions, these are not immediately presentable — they require context and cross-reference to be made into ammunition.

The Ch 11 Board's IMPOSSIBLE KNOWLEDGE slot is the aggregator for knowledge-level contradictions against Endo. See notebook spec §5.2.

### 7.5 Design Rationale

Why knowledge-level contradictions? Because Endo does not lie. Endo tells truths with impossible access. A factual-contradiction engine cannot catch him — his facts are correct. Only a knowledge-level engine can.

This is the game's mechanical rendering of its thesis: the villain does not betray himself through false statements. He betrays himself through the *precision* of his true statements. The player must learn to listen for the wrong kind of accuracy.

### 7.6 Cross-reference with Board Slots

See notebook spec §5.2. The Board's eight slots divide between factual and knowledge-level contradictions:

- **IMPOSSIBLE KNOWLEDGE** — knowledge-level
- **SOCIAL ACCESS PATTERN** — knowledge-level (positional impossibility)
- **COMMITTEE AS MECHANISM** — factual (council records)
- **INFRASTRUCTURE ACCESS** — knowledge-level (one-key inspections)
- **THE GARDEN** — factual (botanical timeline)
- **FRAMING AUTHORSHIP** — factual (metadata forensics)
- **SOCIAL ACCESS (WITNESS)** — knowledge-level (the shape of community knowledge)
- **INDEPENDENT CORROBORATION** — factual (three witnesses, one car)

Roughly half the Board is factual, half knowledge-level. The confrontation exercises both types.

---

## 8. META / UI

### 8.1 Save System

**Autosave** — at every chapter transition, every call end, every Memory Fragment resolution. Silent, background.

**Manual save** — three slots plus an autosave slot. Manual save available at any non-modal scene. No save during calls (to prevent scumming intent choices).

**Continue** — resumes from the most recent autosave. Default boot state for returning players.

### 8.2 Text Speed / Skip / Autoplay

**Text speed** — three settings: slow / normal / fast. Player preference, fully adjustable at any time.

**Auto-advance** — advances text after a configurable delay per line. Off by default. Preserves audio timing even when text is past.

**Skip** — skips previously-read text. Does not skip unread text. Standard VN behavior. Disabled during Memory Fragments and Ch 11 confrontation (both are first-experience-only by design).

### 8.3 Thoroughness Tracking

The game tracks how many optional elements the player has examined per chapter. This is used for:
- Ch 11 Board slot completion
- Epilogue branching (per `epilogue_production.md`)
- Achievement/trophy conditions (if implemented)

The player does not see thoroughness numerically. They see its consequences (a complete Board, a richer epilogue, the Nishida Question surfacing). A post-game optional screen may show per-chapter completion rates for completionists.

### 8.4 Chapter Transitions

Transitions between chapters are hard cuts with a chapter title card. Standard VN convention. Each card includes:
- Chapter number
- Chapter title
- (Optional) a single line of orienting text

Transitions are designed to be the player's natural save-and-pause points. A three-hour chapter followed by an autosave and a title card is the expected rhythm.

### 8.5 Accessibility

Minimum requirements:
- **Full subtitles for all voiced content** (if voiced — the game can ship unvoiced, in which case this is moot)
- **Audio description for environmental details** (optional audio layer that describes what the player would see if they could see the screen; critical for blind players given the game's audio-heavy design)
- **High-contrast text mode** (for low-vision players)
- **Adjustable text size** (up to 200%)
- **Color-blind mode** (Protanopia, Deuteranopia, Tritanopia filters)
- **Keyboard / controller / touch input parity**

The audio-description layer is more important for this game than for most VNs, because the signal degradation is partially visual (animations of static, waveforms) and partially audio (the wire-sound filters). A blind player must be able to experience both layers.

---

## 9. OPEN QUESTIONS / DECISIONS DEFERRED

Questions that need build-time resolution.

1. **Intent button labeling.** Are the intents shown to the player as "REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF" (mechanical terms) or as in-character dialogue previews ("Let her know it's okay" / "Push her for specifics" / etc.)? Mechanical terms teach the system faster; dialogue previews preserve diegesis. Recommendation: mechanical terms in a tutorial mode, dialogue previews in normal play, player-selectable.

2. **Soul Read cost visibility.** Should the player see a visible indicator of Mira's signal state (a faint waveform, an audio meter, a subtle visual cue)? Or is the cost conveyed entirely through tonal/audio shifts? Pro-visible: easier for players who can't hear subtle audio. Pro-invisible: preserves the register. Recommendation: off by default, toggleable in accessibility settings.

3. **Ch 12 real-time tension.** The switchboard duel's time pressure is currently narrative (Endo is moving, Mira is burning). Should there be literal real-time elements — a timer ticking in the UI, calls expiring if not answered within N seconds? Pro: higher tension. Con: violates the anti-twitch design register. Recommendation: no real-timers; use NPC state shifts to convey urgency.

4. **Fumiko publication timer visibility.** Should the player see the timer as a number or only through Fumiko's own statements about it? Recommendation: Fumiko says it aloud ("twelve hours left"); no UI timer. Preserves diegesis.

5. **Mira's degradation progression — player-pausable?** If the player takes a long break between chapters, does Mira degrade further (mechanically penalizing slow play), or does she pause with the save? Recommendation: pause with the save. Degradation is story-time, not real-time.

6. **Memory Fragment skip.** Should returning players (NG+ or a skipped replay) be able to skip Memory Fragments? They are authored not as mini-games but as one-time experiences. Recommendation: skip available on replay only, disabled on first run.

7. **Endo's Ch 11 resolution.** The confrontation ends with Endo requesting counsel. Is this a hard end-of-scene, or can the player continue probing until they run out of Board slots to present? Recommendation: a hard end once he invokes counsel; presenting further contradictions is mechanically blocked. This reinforces that the confrontation is not a breakdown mechanic.

8. **Accessibility — audio description asset production.** Significant additional voice work for a secondary layer. Requires buy-in during localization and audio budgeting. Flag to production.

---

## 10. CROSS-REFERENCES

**This doc's sibling docs:**

- `deadringer_notebook_system.md` — notebook architecture, Board, in-call compact notebook
- `deadringer_locations.md` — per-location UI states, audio signatures
- `deadringer_characters.md` — NPC bibles (informs intent × NPC matrix and Character Notes)
- `chapter_structure.md` — chapter-by-chapter progression, information economy

**Manuscript sources for this doc's specifications:**

- Every chapter file (1–12, epilogue) — intent choice implementations, call scenes, audio signature evidence
- Game bible — thesis, high-level mechanics, emotional principle
- Ogawa incident doc — special-case thread integration

**Build-phase follow-ups required:**

- Intent × NPC matrix audit (full tuning document, one row per NPC × intent × chapter)
- Audio signature pre-production specification (collaboration with sound designer)
- Memory Fragment scene production specification (three scenes, interactive, first-person)
- Soul Read voice direction specification (the degradation curve as voice coaching document)
- Board slot entry audit (cross-reference every `[NOTEBOOK PROMPT]` with Board slot assignments)

---

## APPENDIX: QUICK REFERENCE

**The five intents:** Reassure, Pressure, Redirect, Silence, Bluff.

**The dominant intent per act:**
- Act I — experimentation
- Act II — Silence
- Act III — Redirect (Endo breaks Silence as a strategy)
- Act IV — all five simultaneously

**Soul Read as resource:** every read costs Mira. Degradation is the game's honest mechanical stake.

**Knowledge-level contradiction:** the villain does not lie. He tells truths with impossible access. The player's job is to map that impossibility.

**Memory Fragments:** fixed outcome. Branches exist in texture, not in whether Mira is dismissed. This is the thesis, mechanized.

**Fumiko timer:** the game's primary global clock. Negotiable, not fixed.

**Ch 12 switchboard duel:** three systems running simultaneously — call war, infrastructure race, evidence chain. Converges on Mira's final call to Sora.

**Core design principle across all systems:** listening is the mechanic. Every system rewards listening over pushing. A player who has learned to listen finishes the game. A player who has not is outmatched by Endo.

---

**END SYSTEMS & GAMEPLAY SPECIFICATION**
