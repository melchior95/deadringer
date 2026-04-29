# DEAD RINGER — Cutscene Structure & Production Specification

Master list of cutscenes across the full game. Per cutscene: trigger, runtime, format (still-with-camera / animated / mixed), production tier, location reference, key-frame description, motion spec where applicable, audio direction, transition spec.

**Companion docs:**
- `deadringer_asset_pipeline.md` §3.4, §5 — cutscene production phases
- `epilogue_production.md` — epilogue scenes already specified in detail; this doc references but does not duplicate
- `deadringer_memory_fragments_production.md` — Memory Fragments as interactive cutscenes, already specified; this doc references
- `deadringer_locations.md` — location art references
- `deadringer_audio_signatures.md` — audio direction sources
- `deadringer_hero_location_prompts.md` — Phase 1 hero location image prompts

**Total cutscenes:** 24 major cutscenes + 11 epilogue scenes (specced elsewhere) + transition / connector beats.

---

## 1. PRODUCTION FORMAT TAXONOMY

Every cutscene falls into one of four format categories:

**STILL + CAMERA** — a single or small series of static images with in-engine camera movement (pan, push-in, dissolve). ~70% of cutscenes. Cheapest, most AI-productive format.

**KEY-FRAMED STILLS** — 2–5 static images forming a short sequence. Still format, but multiple images. Used for scenes where location or composition shifts mid-scene (Yanagi arrival sequence, memory fragments, notebook scene).

**AI-ANIMATED** — generated video via Runway Gen-3 / Kling / Luma. Reserved for scenes where motion is load-bearing and still-with-camera fails. 6–10 scenes total.

**MIXED** — still-with-camera primary, with short animated interstitials for specific beats. Used for the most expensive scenes (exchange room discovery, final call to Sora, arrest, switchboard duel).

### 1.1 Production Tier System

**Tier 1 (hero cutscenes):** maximum budget, bespoke iteration, multiple passes.
- Cold open (Ch 1)
- Exchange Room entry (Ch 10)
- 3 AM scene (Ch 11)
- Final call to Sora (Ch 12)
- The Arrest (Ch 12)

**Tier 2 (set pieces):** high budget, single iteration pass, carefully reviewed.
- Yanagi arrival sequence (Ch 2)
- All three Memory Fragments (specced separately)
- Crying scene (Ch 4 or Ch 5)
- The Garden (Ch 9)
- Notebook scene (Ch 11)
- Mira amplified (Ch 10)
- Switchboard duel set dressing (Ch 12)

**Tier 3 (accent):** modest budget, AI-first production, light polish.
- The Bench (Ch 2)
- The Bridge (Ch 2)
- Haruki's break audio-visual cue (Ch 9)
- Doi's confession audio-visual cue (Ch 6)
- Transitions and connectors

---

## 2. SHARED CONVENTIONS

### 2.1 Entry Transitions

Every cutscene enters via one of five transition types:

- **Hard cut** — one frame to the next. Used between scenes within a chapter, and for the cold open.
- **Fade from black** — 1–2 second fade. Used at chapter openings.
- **Slow dissolve** — 3–5 second cross-fade from the preceding gameplay scene. Used when the cutscene is a deepening of the current moment, not a scene change.
- **Memory transition** — specific to Memory Fragments. 2-second dissolve + audio wire-sound rising + text-on-screen framing. See `deadringer_memory_fragments_production.md` §1.1.
- **Phone-ring cold start** — specific to the cold open Ch 1. A phone ring heard in black, visual resolves on the ring.

### 2.2 Exit Transitions

- **Fade to black** — 1–2 second fade. Used at chapter closes.
- **Hard cut** — cutscene to gameplay. Used for action/investigation transitions.
- **Slow dissolve back** — 3–5 second dissolve back to the continuing scene.
- **Memory exit** — specific to Memory Fragments, see fragment spec.
- **Hold-on-image** — cutscene ends with the final image held for 2–4 seconds before next scene. Used for emotionally weighty closes (Ch 4 crying scene close, Ch 11 3 AM scene close, Ch 12 final call).

### 2.3 Camera Language

The game's default camera is still or near-still. Cutscene camera language follows:

- **Fixed** — no camera movement. Image holds.
- **Slow push** — very slow push-in, ~5% zoom over 4+ seconds.
- **Slow pull** — slow zoom-out, same pace.
- **Lateral pan** — horizontal camera shift, authored. Used sparingly.
- **Handheld motion** — micro-shake, authored. Reserved for disorienting moments (Ch 12 switchboard duel, Ch 11 crash state).

Hand-held or dynamic camera is the exception, not the default. The game's visual register is observational.

### 2.4 Dialogue During Cutscenes

Most cutscenes include dialogue via voice-over + subtitles. Dialogue is overlaid on the cutscene image; the cutscene's visual does not animate to the dialogue. Exception: in-scene character speech (animated cutscenes where character lips should move). Where AI animation can't reliably produce natural lip-sync, accept misalignment — AI animation already subverts the convention of tight lip-sync, and the genre's heritage (VN character sprites that don't lip-sync) makes this acceptable.

### 2.5 Runtime Targets

| Format | Typical runtime |
|---|---|
| Still + camera | 10–30 seconds |
| Key-framed stills | 30–90 seconds |
| AI-animated | 8–20 seconds per shot; total cutscene 20–60 seconds |
| Mixed | 60–180 seconds |

The game's longest cutscene is Ch 12's convergence sequence (~180 seconds). Most cutscenes target under 60 seconds. VN conventions allow longer dialogue-heavy cutscenes; Dead Ringer prefers brevity.

---

## 3. CUTSCENE CATALOG

Ordered by chapter.

---

### 3.1 COLD OPEN (Ch 1)

**Trigger:** game start, new game.
**Runtime:** ~45 seconds total, multiple beats.
**Format:** Mixed — still + camera with short animated moment at phone ring.
**Tier:** 1 (hero cutscene).
**Location:** Kenji's Apartment, Ch 1 night state. See `deadringer_locations.md` §1 / `deadringer_hero_location_prompts.md` §1.

**Structure (four beats):**

1. **Black screen** (5s). The clock ticks, irregular. The refrigerator cycles on, runs for 6 seconds, clicks off. The apartment breathes in sound.
2. **Visual resolves** (10s). Light enters from the bottom of the frame — the desk lamp, warm and insufficient. Slowly, the desk comes into focus: case file, coffee cans, pocket notebook. Camera holds static.
3. **Wider reveal** (15s). Camera slowly pulls back to reveal more of the apartment — the kitchen counter, the cookbook, the coat, the drawer of dead phones slightly ajar. Kenji's silhouette enters frame at the bottom of the shot, seated at the desk.
4. **The ring** (15s). A phone rings. The ring cuts the apartment silence like a fissure. The screen cuts tight to the phone — **this is where animation applies**: a short animated beat of the phone's screen lighting up, the display resolving to "NO CALLER ID" as the ring continues. Kenji's hand enters frame, hovers, picks up.

**Key-frame images needed:**
- Beat 1: black screen (no image)
- Beat 2: the desk lit by the lamp, amber pool, surrounding shadow
- Beat 3: wider apartment view, Kenji's silhouette at the desk
- Beat 4: close on the phone face, "NO CALLER ID" visible (animation source)

**Animation source (Beat 4):** generate 8–15 second video clip of the phone on the desk. Screen lights up, display resolves, phone rings visibly (subtle vibration, light modulation). Kenji's hand enters at the end.

**Audio direction:**
- Beat 1: clock tick, fridge cycle, complete establishment of apartment ambience
- Beat 2–3: same ambience continuing, wire-sound enters faintly
- Beat 4: the ring — designed sound, not stock. "Not the standard tone — older, rawer, a sound with physical weight." Distinct from any other phone ring in the game.

**Transition in:** from main menu fade or new-game hard cut to black.
**Transition out:** beat 4 ends with Kenji's hand on the receiver. Cuts to dialogue scene (first Mira call).

**Notes:** This is the game's first impression. Everything else is calibrated against it. Budget as the most-iterated cutscene.

---

### 3.2 THE FIRST CALL (Ch 1)

**Trigger:** continues from cold open.
**Runtime:** ~3–5 minutes (dialogue-heavy).
**Format:** Still + slow camera. Not a cutscene per se — a dialogue scene with cutscene framing.
**Tier:** 2.
**Location:** Kenji's Apartment.

**Structure:**
- Camera stays on Kenji (medium close-up) for most of the scene. Rare cuts to: the desk, the dead phones drawer, Kenji's hand on the phone, the empty apartment around him.
- Dialogue delivered as voice-over from Mira (off-screen, phone audio) and Kenji (on-screen). Mira has no visual presence.

**Key-frame images needed:**
- Kenji medium close-up (Ch 1 state — cold-case fatigue, unlit cigarette)
- The desk with phone (tight composition)
- The dead phones drawer (low angle into the drawer)
- Kenji's hand on the receiver

**Audio direction:** per `deadringer_audio_signatures.md` §3.1 (Kenji), §4.1 (apartment), §5.1 (Mira Ch 1 clean voice).

**Transition in:** continues from cold open.
**Transition out:** Ch 1 close — hold on Kenji at the desk, fade to black, chapter title card.

---

### 3.3 YANAGI ARRIVAL SEQUENCE (Ch 2)

**Trigger:** Ch 2 opens.
**Runtime:** ~90 seconds.
**Format:** Key-framed stills — 5–6 images with camera transitions between.
**Tier:** 2.
**Location:** Yanagi-cho station exit → neighborhood.

**Structure (6 beats):**

1. **Elevated train** (10s) — distant shot of the train passing behind low-rise apartments.
2. **Station exit** (15s) — Kenji emerges from the station. Train departure audible behind him.
3. **Block 1 street** (15s) — the broken vending machine, grandmother watering plants.
4. **Block 2** (15s) — pharmacy, Mikan the cat in the window, bulletin board.
5. **Block 3** (15s) — school visible across the street.
6. **The school gate** (20s) — close on the school gate. The gate, the camera above, the path bending behind the building.

**Key-frame images needed:**
- Train passing behind apartment blocks (wide establishing shot)
- Station exit (Kenji emerging)
- Block 1 street with vending machine
- Block 2 pharmacy (Mikan visible in window)
- Block 3 approaching the school
- School gate close-up

**Audio direction:** per `deadringer_audio_signatures.md` §4.2. Mix shift at station exit (train departure → residential quiet). Wire-sound present throughout.

**Transition in:** chapter title card → fade up.
**Transition out:** hard cut to Kenji + Mira dialogue at the school gate.

**Notes:** this is the game's tonal establishment for Yanagi. Each key-frame must land "well-maintained, ordinary, quiet" without sinister register.

---

### 3.4 THE BENCH (Ch 2)

**Trigger:** Kenji examines the bench near the school gate.
**Runtime:** ~15 seconds.
**Format:** Still + slow push-in.
**Tier:** 3.
**Location:** School Bench.

**Structure:** a single close-up on the bench slats showing the colored pencil marks. Slow push-in over 15 seconds. No narration; Mira's voice-over comments on the marks.

**Key-frame needed:** close-up of the wooden bench slats with faint colored pencil diagram visible — intersecting lines, small squares, transit route miniature.

**Audio direction:** street ambient, Mira's voice-over.

**Transition in:** cut from Kenji's investigation screen.
**Transition out:** cut back to investigation.

---

### 3.5 THE BRIDGE (Ch 2)

**Trigger:** Kenji examines the scratched number on the bridge south wall.
**Runtime:** ~20 seconds.
**Format:** Still + slow push-in.
**Tier:** 3.
**Location:** Bridge Underside.

**Structure:** wide shot of the bridge underside → slow push-in on the south wall → tight shot of the scratched phone number in concrete. Mira's voice-over acknowledgment.

**Key-frames needed:**
- Bridge underside wide shot (graffiti, water stains)
- Tight shot of the scratched number in concrete (deep grooves, weathering)

**Audio direction:** river echoing under the bridge, Mira's voice, faint wire-sound.

**Transition in/out:** cut.

---

### 3.6 REIKO DENIAL — MEMORY FRAGMENT (Ch 3)

**Trigger:** post-Reiko Soul Read.
**Runtime:** ~3:00–3:30.
**Format:** Interactive scene (first-person with dialogue choices).
**Tier:** 2.
**Location:** Reiko's Apartment kitchen, ~18 months pre-death.

**Full spec:** see `deadringer_memory_fragments_production.md` §2.

**Cutscene notes for this doc:** entry and exit transitions are shared Memory Fragment transitions; Kenji's apartment fades; kitchen resolves with text-on-screen framing. Exit with notebook-deposit text ("'Can't' and 'won't' are different.").

---

### 3.7 YUI'S CALL (Ch 4)

**Trigger:** player calls Yui for first time.
**Runtime:** ~3–5 minutes (dialogue).
**Format:** Audio-only — NO CUTSCENE KEY-FRAME NEEDED.
**Tier:** Not a cutscene; listed here for completeness.

**Notes:** Yui's apartment is never shown. The call runs as a call screen with Kenji's side visible (default call UI) and Yui represented only through audio signature. This is a deliberate design choice preserving Yui's protection from instrumentalization (per `deadringer_locations.md` §9).

---

### 3.8 CRYING SCENE (Ch 4 or Ch 5–6 deferred)

**Trigger:** Yui intervention success (primary) OR accumulated dismissed-reports weight (deferred).
**Runtime:** ~60 seconds.
**Format:** Abstract — no diegetic scene. Sound-forward with minimal visual.
**Tier:** 2 (emotionally central; requires careful handling).
**Location:** None specific. Abstract.

**Structure:**
- The call UI dims.
- The screen holds on black or on a very slow ambient shot (the wire-sound wavelength visualized faintly, or an abstract warm glow).
- Mira's voice does all the work. The crying is audible but private.
- The scene ends with Mira's register restabilizing.

**Key-frame image:** abstract visual only — possibly a faint waveform, a warm glow, or a simple cream field. Prompt:

```
Visual novel abstract cutscene frame — a warm cream field with faint copper-gold texture, like looking into a lamp at close range. A very subtle waveform pattern suggested at the edge, as if the sound itself is visualizing. No characters, no location, no narrative detail. Quiet, intimate, emotionally loaded. Widescreen 16:9 --ar 16:9 --v 6.1 --style raw
```

**Audio direction:** the scene's full weight. Mira's voice in UNARMORED register (see `deadringer_soul_read_voice_direction.md` §3.6). Wire-sound audible and slightly warmer than usual — the infrastructure carrying something it wasn't built for.

**Transition in:** the cutscene emerges from the Yui call/investigation. Slow dissolve, not hard cut.
**Transition out:** slow dissolve back to Kenji's apartment.

**Notes:** this is the game's most load-bearing audio moment. Do NOT generate complex visuals. The rule is: less visual = more audio weight. A player who looks at the screen during this scene should find nothing there; the scene happens in their ears.

---

### 3.9 RINA SOCIAL DISTORTION — MEMORY FRAGMENT (Ch 4)

**Trigger:** post-Rina Soul Read.
**Runtime:** ~2:30.
**Format:** Interactive scene.
**Tier:** 2.

**Full spec:** see `deadringer_memory_fragments_production.md` §3.

**Exit notebook-deposit text:** *"Next time I won't tell the teacher. I'll just write it down."*

---

### 3.10 AIZAWA PROCEDURE — MEMORY FRAGMENT (Ch 5)

**Trigger:** post-Aizawa Soul Read.
**Runtime:** ~3:00–3:30 (longest fragment).
**Format:** Interactive scene.
**Tier:** 2.

**Full spec:** see `deadringer_memory_fragments_production.md` §4.

**Exit notebook-deposit text:** *"I did the right thing. Nothing happened."*

---

### 3.11 DOI'S CONFESSION COLLAPSE (Ch 6)

**Trigger:** player uses SILENT on Doi's false confession.
**Runtime:** ~30 seconds.
**Format:** Still + slow push-in.
**Tier:** 3.
**Location:** Doi's store (exterior observation — we do not enter).

**Structure:** the exterior of Yanagi Mart, the door open as always. Camera slowly pushes in on the counter through the open door. The framed photograph behind the counter becomes visible as the camera arrives. Through the entire cutscene, Doi's voice continues from the phone call — we hear his register shift from performed guilt to real grief without seeing him. The photograph is Ren. This is the visual reveal of what he has been hiding.

**Key-frame image needed:** Yanagi Mart interior seen through the open door — the counter, the framed photograph of Ren in focus, Doi himself in partial silhouette.

**Audio direction:** store ambient (less than usual — the scene specifies the store has quieted), Doi's voice continuing, Mira silent.

**Transition in:** continues from phone call; slow dissolve into the exterior.
**Transition out:** hold on the photograph, fade to black.

---

### 3.12 THE GARDEN (Ch 9)

**Trigger:** Path B investigation; Kenji walks to Endo's home.
**Runtime:** ~40 seconds.
**Format:** Key-framed stills (3–4 frames) + slow camera.
**Tier:** 2.
**Location:** Endo's Home & Garden. See `deadringer_locations.md` §22 / `deadringer_hero_location_prompts.md` §3.

**Structure (4 beats):**

1. **Wide establishing shot** (10s) — Endo's house and garden seen from the sidewalk. Morning light, the garden in bloom. Beautiful at thumbnail.
2. **Medium on the garden** (10s) — closer, the spacing now visible. The measured intervals between plantings. Slow push-in.
3. **Close on the two newest plantings** (10s) — the shrub and the sapling at the eastern edge. Tight composition.
4. **Pull back to the wide shot** (10s) — returning to the establishing view. The garden now reads differently than it did at the start of the cutscene. Nothing visual has changed. The player's understanding has.

**Key-frame images needed:**
- Wide establishing shot of house + garden (primary composition, the style-audition prompt from `deadringer_hero_location_prompts.md` §3)
- Medium shot showing the architectural spacing
- Close-up on the two newest plantings
- Return to wide (can be the same image as beat 1)

**Audio direction:** residential morning — bird, distant car, a hose running somewhere. No interior sound. The house is silent. Wire-sound faintly present. Kenji's voice provides observational narration; Mira asks "What kind?" and accepts the sapling's species in quiet.

**Transition in:** cut from Kenji's investigation / street walk.
**Transition out:** cut to notebook-deposit prompt (the botanical timeline entry).

---

### 3.13 HARUKI'S BREAK (Ch 9)

**Trigger:** player calls Haruki during framing investigation; "disruptive honesty" phrase match.
**Runtime:** ~45 seconds.
**Format:** Still + subtle audio cue.
**Tier:** 3.
**Location:** Haruki's classroom (audio only, no visual).

**Structure:** the call UI holds on the default call screen state. Haruki's face/name in the caller strip. During the tell moment (the 2–3 second cessation of his pen-click and chair squeak), the visual presentation of the call UI itself subtly shifts — a quarter-second pause on the waveform indicator, a barely-perceptible desaturation in the dialogue panel border. The visual degradation is Haruki's state made environmental.

**Key-frame needed:** two variants of the call screen UI — default state and subtly-desaturated break state. Used in engine as state swap.

**Audio direction:** the cessation of tics IS the cutscene. All other audio holds (ambient, wire-sound). Haruki's voice continues flat post-break.

**Transition in/out:** holds within the call; no scene change.

---

### 3.14 EXCHANGE ROOM DISCOVERY (Ch 10)

**Trigger:** Kenji descends to the community center basement, opens the sealed door.
**Runtime:** ~90 seconds total.
**Format:** Mixed — still + camera primary, one animated beat.
**Tier:** 1 (hero cutscene).
**Location:** Community Center — Exchange Room. See `deadringer_hero_location_prompts.md` §2.

**Structure (6 beats):**

1. **The sealed door** (10s) — hallway. The door with its old weather stripping, the clean handle. Close on the handle.
2. **The door opens** (8s, animation) — the door slowly opens. **This is the animated beat.** Light from the hallway falls into the darker space beyond. Dust motes disturbed.
3. **First view of the room** (15s) — interior reveal. Camera holds on the room. The switchboard visible at the far wall. Slow, no movement.
4. **The chair** (15s) — camera pans slowly to the folding chair. The 15-degree angle becomes visible. The four worn depressions in concrete.
5. **The table** (15s) — camera pans to the small folding table beside the chair. Thermos. Notebook. Penlight. Personal items.
6. **Kenji crosses to the handset** (15s) — wide shot. Kenji walks into the room toward the handset on the shelf. The scene ends with his hand on the bakelite receiver.

**Key-frame images needed:**
- Exterior: the sealed door in the basement storage area, close on handle
- Interior wide: first view of the exchange room (the style-audition prompt from `deadringer_hero_location_prompts.md` §2)
- Close on the chair: showing the 15-degree angle and worn depressions
- Close on the table: thermos, notebook, penlight
- Wide: Kenji crossing to the handset

**Animation source:** Beat 2 (door opening) is the only animation. ~8 second clip. The door opens, dust disturbs, light shifts. Kenji's presence implied but not on-screen.

**Audio direction:** per `deadringer_audio_signatures.md` §4.5. The door opening shifts the low-frequency soundscape — listener's ear adjusts. Inside the room, the structured static of the switchboard becomes audible. Dozens of layered frequencies.

**Transition in:** cut from hallway gameplay.
**Transition out:** hold on Kenji's hand on the handset, fade to the Mira amplified beat.

**Notes:** this is the game's second-most load-bearing cutscene after the cold open. The ~15-degree chair angle is the set piece's thesis; if the composition misses it, the scene fails.

---

### 3.15 MIRA AMPLIFIED (Ch 10)

**Trigger:** continues from Exchange Room entry.
**Runtime:** ~60 seconds.
**Format:** Mixed — still + subtle animation for atmospheric motion.
**Tier:** 2.
**Location:** Exchange Room (interior, same scene).

**Structure:** Kenji holds the handset. Camera holds on him in medium. The wire-sound clears. Mira's voice returns to Ch 1 quality — clean, present, room-close. The scene is not narratively eventful; it is emotional-mechanical. Visual holds; the content is audio.

**Atmospheric motion:** subtle dust particles in the fluorescent light, faint flicker of the overhead fixture, barely-perceptible shifts in the wire-sound's visualized waveform at the top of the screen. Handheld micro-motion on the camera, authored but minimal.

**Key-frame images needed:**
- Kenji in medium close, handset raised (the ear-listening posture)
- Tight on the handset in his grip
- Very slow atmospheric motion of dust / light flicker

**Animation source:** single 20-second ambient-motion clip of the room with the dust and light flicker.

**Audio direction:** see `deadringer_audio_signatures.md` §4.5. Mira's voice clears entirely. The residue voices faint underneath. The "other children" discovery happens audibly.

**Transition in:** continues from discovery.
**Transition out:** cut to Kenji's investigation of the room's physical evidence (the table, the notebook, the routing logs).

---

### 3.16 THE NOTEBOOK SCENE (Ch 11)

**Trigger:** Kenji gives Reiko Mira's blue notebook.
**Runtime:** ~2 minutes.
**Format:** Key-framed stills + slow camera.
**Tier:** 2.
**Location:** Reiko's Apartment (Ch 11 state).

**Structure (5 beats):**

1. **Entry to apartment** (15s) — Kenji at Reiko's door. Handoff of the notebook. Wide shot.
2. **Reiko at the low table** (20s) — she is seated at the low table. The notebook in front of her, unopened. She looks at it for several seconds. Camera on her face.
3. **She opens it** (30s) — close on her hands opening the notebook. The handwriting visible. She reads.
4. **Reading in silence** (60s) — the longest beat. Camera on Reiko, slow push-in across the beat. She reads for a minute. Occasionally a page turns. No dialogue. The player watches her face.
5. **The line** (15s) — Reiko: *"She was doing mine."* Close on her face. Fade.

**Key-frame images needed:**
- Wide of Reiko's apartment, Kenji at the door
- Reiko seated at the low table with the closed notebook
- Close on her hands opening the notebook (handwriting visible)
- Medium of Reiko reading, at different beats (multiple key-frames for the sustained reading scene)
- Close on her face at the line

**Audio direction:** apartment quiet (per Reiko signature §3.1). Clock. Refrigerator. No music. The scene's weight is in the silence; Reiko's voice delivers the one line clean.

**Transition in:** slow dissolve from Kenji walking to the apartment.
**Transition out:** hold on Reiko's face, fade to black.

**Notes:** this scene is emotionally the highest priority in Act IV. Budget for careful iteration. The "reading in silence" beat is the scene's engine — resist the temptation to fill it with action. Reiko reading, nothing else happening, is the design.

**Higashino-lens note:** The notebook's first visible entry should be the one about Yui — Mira's earliest observation, the one that reveals she was watching and protecting another child before anyone was watching her. Reiko's reaction in beat 4 (the sustained reading) carries different weight for the player who already knows the Yui-sequence: Reiko is discovering her daughter's hidden acts of care. The handwriting close-up in beat 3 should show enough of the first entry's content to register "Yui" for attentive players, without foregrounding it as exposition.

---

### 3.16b THE WARMTH MOMENT — CENTIPEDE ON THE BALCONY (Ch 11)

**Trigger:** during the 3 AM scene sequence; Mira describes Reiko's balcony ritual.
**Runtime:** ~20 seconds.
**Format:** Still + hold. No camera movement.
**Tier:** 3 (accent — emotional weight carried by audio, not visual complexity).
**Location:** Reiko's Apartment — balcony exterior, night.

**Structure:** a single held image of the balcony. The composition: a small balcony at night, a centipede on the railing, a cup of tea on the ledge. No person visible. The image holds while Mira's voice describes the moment — Reiko catching centipedes and releasing them over the railing rather than killing them, a small act of care nobody asked for or observed.

**Key-frame image needed:** the balcony at night — railing, a centipede (small, precise, naturalistic), a tea cup, the apartment interior light visible through the glass door behind. The image should read as "ordinary domestic moment" not "dramatic reveal."

**Audio direction:** apartment night ambient. Mira's voice in her observational register — describing what she saw, not interpreting it. The warmth is in the fact of the description, not in vocal performance.

**Transition in:** dissolve from the 3 AM scene's dialogue.
**Transition out:** dissolve back to the 3 AM scene.

**Higashino-lens note:** this is one of the hidden acts of love — Reiko's small, unwitnessed kindness that Mira recorded. The cutscene exists to give the moment visual weight. It should feel incidental, not climactic. The player who recognizes it as a hidden act does so because they have been trained by the Higashino-lens design to notice small care, not because the presentation signals importance.

---

### 3.17 THE 3 AM SCENE (Ch 11)

**Trigger:** after the Ch 11 confrontation close; the chapter's final scene.
**Runtime:** ~5–6 minutes (longest character-focused scene in the game).
**Format:** Still + slow camera.
**Tier:** 1 (hero cutscene).
**Location:** Kenji's Apartment (Ch 11 3 AM state).

**Structure:** the scene is dialogue-heavy and largely static. Camera holds on Kenji in various compositions as he moves through the scene.

**Key beats:**

1. Kenji lying on the bed with his shoes on, staring at the ceiling (~30s).
2. Kenji gets up, crosses the apartment, picks up the phone (~30s).
3. **Kenji on the floor against the desk** (~4 minutes). This is the scene's primary camera position. Unusual posture the player has never seen from Kenji before. The dialogue unfolds from this position.
4. Kenji sets the phone on the floor beside him (~15s).
5. Kenji lies back on the bed, shoes still on (~15s).
6. Hold on Kenji for an extended beat. Fade.

**Key-frame images needed:**
- Kenji on the bed staring at the ceiling (Ch 11 state)
- Kenji crossing the apartment (medium)
- Kenji on the floor against the desk (primary composition)
- Kenji's hand on the phone, phone on floor beside him
- Kenji back on bed, phone line still open

**Primary image challenge:** the "Kenji on the floor against the desk" composition. This has never been seen before in the game; Kenji does not sit on the floor. The image should convey: a man who has sat down somewhere unusual because he cannot bear the usual furniture tonight.

**Audio direction:** per `deadringer_audio_signatures.md` §4.1 (apartment), §5.2 (Mira 3 AM partial-unarmored), §5.4 (Kenji soft register). The refrigerator cycle's specific rhythm (6 on / 97 off) is audible and explicitly counted in dialogue. Wire-sound thin, carrying Mira.

**Transition in:** fade from black after chapter close.
**Transition out:** fade to black. Chapter title card for Ch 12.

**Notes:** this is one of the game's five most important scenes. Voice direction is extensive (see `deadringer_soul_read_voice_direction.md` §3.10). Camera holds are long by design — players will tolerate the duration because the dialogue is earning it.

---

### 3.18 SWITCHBOARD DUEL (Ch 12)

**Trigger:** Ch 12's mid-chapter through convergence.
**Runtime:** ~20 minutes (chapter's core, not a single cutscene but a chained sequence).
**Format:** Mixed — primarily call screens and cut-ins.
**Tier:** 1 collectively; individual beats Tier 2–3.
**Location:** Primarily Kenji's apartment; cut-ins to exchange room, utility substation, NPC locations.

**Structure:** the duel runs three interlocking systems (see `deadringer_systems.md` §5.5). Not presented as a single cutscene — individual beats within the duel warrant cutscene treatment:

- Endo placing calls (brief cut-ins to his meeting room / car / home)
- Mira intercepting (call screen with amplified state)
- Kenji's counter-calls (standard call screen)

**Specific cutscene treatments within the duel:**

**a) Fumiko publication decision** (~30s) — cut-in to Fumiko at her workspace, pen held over a draft. Her face in medium close as she makes the publication call.

**b) Mira's intercepts** (~15s each, ~8 total) — brief call-screen moments where the UI dissolves and Mira narrates what she hears. No full cutscene; presentation within call screen.

**Higashino-lens audio note:** Mira's intercept narration should use "forensic flatness" — the same clinical, affectless register she uses when reporting observations in the notebook. She is not emotional about what she overhears; she is precise. The flatness is itself the tell: Mira is performing the same observational discipline she used in life, and the absence of emotional inflection is what makes the content land harder. Audio direction should resist the temptation to add tremor, urgency, or horror to Mira's intercept voice. The facts are the horror. Her voice is the instrument that delivers them undistorted.

**c) Endo's mid-duel beats** (~15s each, ~4 total) — brief cut-ins to Endo during his own calls. Shot of him speaking into a phone. Helpful to establish his POV; also feeds into the arrest cutscene visual continuity.

**Key-frame images needed (for the above):**
- Fumiko at her workspace, pen held
- Endo on the phone (multiple variants — at home, in his meeting room)
- Kenji's apartment during the duel (state variant: more hectic desk, papers reorganized)

**Audio direction:** see audio spec §6.5 (Ch 12 wire-sound burning state). This is the chapter's audio showpiece; the wire-sound audibly degrades across the duel.

---

### 3.19 SORA'S SIGNAL (Ch 12)

**Trigger:** Mira catches Sora's fragment on the lines during the duel.
**Runtime:** ~60 seconds.
**Format:** Mixed — call screen + brief animation.
**Tier:** 2.
**Location:** Exchange Room audio space; no new visual.

**Structure:** the call screen UI dissolves. Mira's voice describes what she's hearing. A new voice enters the audio — Sora, fragmentary. The visual treatment: the wire-sound waveform at the top of the screen (normally subtle) gains a second thinner line — Sora's signal. The visualization is the cutscene's visual.

**Key-frame:** abstract waveform visualization. Two lines — the dominant (Mira/exchange) and the thin new signal (Sora).

**Animation source:** short loop of the dual-waveform animation, ~15 seconds, variable intensity.

**Audio direction:** the scene is the audio. Mira's voice processes what she hears into speech; Sora's voice as fragmentary residue. See `deadringer_audio_signatures.md` §4.5 for the exchange room layered design.

**Transition in/out:** dissolves in and out of the call screen UI without scene change.

---

### 3.20 MIRA'S FINAL CALL TO SORA (Ch 12)

**Trigger:** Mira tells Kenji she will reach Sora; she makes the call.
**Runtime:** ~45 seconds.
**Format:** Mixed — stills of Kenji + abstract visual for the call itself + still of Sora.
**Tier:** 1 (hero cutscene).
**Location:** abstract / the exchange / the substation where Sora is held.

**Structure (4 beats):**

1. **Kenji listening** (10s) — close on Kenji. He is hearing this happen but cannot speak. The processing lifts on Mira's voice; he hears her clear for the first time since Ch 10.
2. **Abstract signal** (15s) — the call itself. Visual: the waveform visualization from Sora's Signal cutscene, now dominated by Mira's signal pushing through. Subtle, not literal.
3. **Sora in the substation** (15s) — brief cut to Sora. He is holding an old phone / receiver in the utility substation. His face in medium close. He is listening. He is not yet rescued; he does not know Kenji is coming. Mira's voice reaches him.
4. **The line goes dead** (5s) — abstract visual returns. Mira's signal flatlines. Silence.

**Key-frame images needed:**
- Kenji listening (Ch 12 state of his face — the hours-long duel visible)
- Abstract waveform (Mira's signal pushing through, visualized)
- Sora in the substation (small room, old phone, listening) — **NEW CHARACTER KEY-FRAME: requires character design for Sora in post-capture state**
- Abstract waveform flatlining

**Animation source:** Beat 2 and Beat 4 share a single abstract waveform animation (~20 seconds, tracked from active to flatline).

**Audio direction:** see `deadringer_soul_read_voice_direction.md` §3.11. Mira's processing LIFTS for this call — clean voice for ~20 seconds. The signal then flatlines: static, then nothing. Sora's brief acknowledgment sounds (no words, just quiet assent).

**Transition in:** slow dissolve from Kenji's apartment during the duel.
**Transition out:** hold on the flatlined waveform. Silence. Cut to Kenji's apartment.

**Notes:** this is the emotional climax. The processing lift on Mira's voice is the scene's most important audio beat — the player has lost her voice clarity for chapters; it returns once, briefly, for this.

---

### 3.21 SORA RESCUED (Ch 12)

**Trigger:** Kenji arrives at the utility substation.
**Runtime:** ~45 seconds.
**Format:** AI-animated (one of the few genuine animation cases).
**Tier:** 1 (hero cutscene).
**Location:** Utility Substation exterior + brief interior.

**Structure:**

1. **Kenji at the fence** (10s animation) — Kenji approaches the padlocked fence of the decommissioned substation. Cuts the lock.
2. **Entry** (15s animation) — interior of the substation. Small, dusty. Sora sitting on the concrete floor with a blanket that smells like dust.
3. **Kenji kneels** (10s still + slow push) — close on Sora's face as Kenji enters his field of view. Sora does not recognize Kenji, but recognizes what is happening.
4. **Kenji speaks** (10s still) — Kenji says the thing Mira told Sora he would say. Sora's recognition.

**Animation source:** Beats 1 and 2 as AI-animated clips. Runway Gen-3 quality required — the character animation for Kenji and Sora needs consistency.

**Key-frame images needed:**
- Kenji at the padlocked fence (exterior of substation)
- Interior of the substation (small, dusty, a blanket, Sora seated)
- Close on Sora's face (recognition beat)

**Audio direction:** minimal dialogue. Environmental sound (the substation's specific acoustic — concrete, dust, a pipe in the distance making a sound when it gets cold). Sora's small acknowledgment.

**Transition in:** cut from Kenji leaving the apartment mid-duel.
**Transition out:** fade to the arrest scene.

---

### 3.22 THE ARREST (Ch 12)

**Trigger:** Kenji has Sora; warrant processes; Endo is arrested.
**Runtime:** ~60 seconds.
**Format:** Mixed — animated + stills.
**Tier:** 1 (hero cutscene).
**Location:** Endo's Home & Garden (exterior, arrest at the home).

**Structure:**

1. **Police arriving** (15s animation) — a police car arrives at Endo's house. Neighbors notice. Morning light.
2. **Endo at the door** (15s animation) — Endo comes to the door. He is calm. The officer reads the arrest particulars.
3. **The handcuffs** (10s still + zoom) — close on Endo's wrists being cuffed. Clean, procedural.
4. **The car door** (10s animation) — Endo is placed in the back of the police car. The door closes. The camera holds on the closed car door.
5. **The garden** (10s still) — wide shot of the garden. Unchanged. Beautiful. The sapling at the eastern edge visible. Hold.

**Animation source:** Beats 1, 2, 4 need animated clips. Runway Gen-3 quality. Character consistency on Endo is critical; use locked reference.

**Key-frame images needed:**
- Police car arriving at the residential street
- Endo at his door (calm, no struggle)
- Close on the handcuffs
- The car door closing on Endo inside
- The garden in morning light — same composition as Ch 9 Garden but now in post-arrest context

**Audio direction:** no dialogue from Endo. Officer voice, procedural. No music. Ambient morning. The sound of the car door closing should have weight. Final frame on the garden: wire-sound very faint, possibly silent.

**Transition in:** cut from Sora rescued.
**Transition out:** fade to black. End of main story. Epilogue begins after.

**Notes:** the final image (the garden, unchanged) is the cutscene's thesis. Endo is gone; his garden remains. The beauty remains. This is the final image of the main story.

---

### 3.23 EPILOGUE CUTSCENES (Epilogue)

**Trigger:** main story closes; epilogue begins.
**Runtime:** ~9–11 minutes total.
**Format:** Primarily stills with careful camera; one or two subtle animations.
**Tier:** 1 collectively (the entire epilogue is a hero sequence).

**Full spec:** see `epilogue_production.md` — all 11 character resolution scenes plus the title screen return are fully specified in the epilogue production document.

**Summary for this doc:** Sora's classroom (Ch 12 epilogue scene), Yui's garden, Reiko's apartment, Doi's shop, Haruki's classroom, Fumiko's published story, the Nishida Question, Aizawa's desk, Kaito's route, Rina's schoolyard, Kenji's drawer, title screen return.

Each scene has its own key-frame requirements and audio direction per the epilogue production spec. For integration with this cutscene master list: all epilogue scenes are **STILL + CAMERA** format with **HOLD-ON-IMAGE** exits between them. The epilogue's structure is: fade up, hold, fade out, brief black, fade up on next scene. This rhythm is the epilogue's quiet design.

**Cross-reference:** `epilogue_production.md` owns the epilogue's production details.

---

## 4. PRODUCTION PRIORITY LIST

Ordered for production scheduling.

### Tier 1 — Hero Cutscenes (produce first, iterate heavily)

1. **Cold open** (Ch 1) — establishes everything
2. **Exchange Room discovery** (Ch 10) — the game's second-biggest visual moment
3. **The 3 AM scene** (Ch 11) — the game's emotional anchor
4. **Mira's final call to Sora** (Ch 12) — the game's climax
5. **The arrest** (Ch 12) — the final image
6. **Epilogue hero scenes** (see epilogue production doc)

### Tier 2 — Set Pieces (produce after hero cutscenes lock)

7. Yanagi arrival sequence (Ch 2)
8. Memory Fragments — three scenes (specced elsewhere)
9. Crying scene (Ch 4 / 5)
10. The Garden (Ch 9)
11. Notebook scene (Ch 11)
12. Mira amplified (Ch 10)
13. Sora rescued (Ch 12)
14. Remaining epilogue scenes

### Tier 3 — Accent (produce with spare capacity)

15. The Bench (Ch 2)
16. The Bridge (Ch 2)
17. Doi's confession collapse (Ch 6)
18. Haruki's break audio-visual cue (Ch 9)
19. Switchboard duel cut-ins (Ch 12)
20. Sora's Signal (Ch 12)

---

## 5. ANIMATION BUDGET

Only cutscenes needing genuine AI video generation:

| Cutscene | Animation length (total) | Tool recommendation |
|---|---|---|
| Cold open — phone ring | ~10 seconds | Runway Gen-3 |
| Mira amplified — atmospheric motion | ~20 seconds | Runway Gen-3 or Kling |
| Exchange Room — door opening | ~8 seconds | Runway Gen-3 |
| Sora rescued — arrival + entry | ~25 seconds | Runway Gen-3 (character consistency) |
| Arrest — police + handcuffs + car | ~30 seconds | Runway Gen-3 (character consistency) |
| Sora's Signal — waveform animation | ~15 seconds | Kling or Luma (abstract motion easier) |
| Final call to Sora — waveform | ~20 seconds | Kling or Luma |
| Switchboard duel cut-ins | ~30 seconds total | Runway Gen-3 |

**Total animation runtime:** ~160 seconds across the game. Modest by feature-film standards; significant for AI generation.

**Estimated Runway credit budget:** ~500 credits for first-pass production, ~250 for iteration. Total ~750 credits.

---

## 6. ACCESSIBILITY

Every cutscene must support:
- Full subtitles for all dialogue
- Audio description layer (described scene for blind players — separate voice-over track)
- Camera-motion-sensitivity mode: replaces pans and dissolves with hard cuts
- Runtime indicator (not visible by default; optional setting for players who need to know how long a cutscene runs)
- Skip (available on replay only, disabled on first run)

The audio description layer is more important for this game than most VNs because several cutscenes rely heavily on visual composition reveals (the garden's spacing, the exchange room chair angle, the 3 AM scene's Kenji posture). A blind player must be able to experience these details through description.

---

## 7. CROSS-REFERENCES

- `deadringer_asset_pipeline.md` §3.4, §5 — cutscene production phases
- `epilogue_production.md` — epilogue scenes detail
- `deadringer_memory_fragments_production.md` — Memory Fragment scenes
- `deadringer_locations.md` — location art references
- `deadringer_audio_signatures.md` — audio direction sources
- `deadringer_hero_location_prompts.md` — Phase 1 hero location prompts
- `deadringer_soul_read_voice_direction.md` — Mira performance direction for voiced beats
- `deadringer_ui_art_prompts.md` — UI element art for call screens and overlays

---

**END CUTSCENE STRUCTURE SPECIFICATION**
