# DEAD RINGER — Audio Signature Pre-Production Specification

Sound designer handoff document. Specifies: per-NPC audio signatures, environmental audio per location, the wire-sound evolution curve, Mira's voice degradation as an audio-direction spec, and the exchange room's layered static.

Audio is the game's primary storytelling channel. The game can be played with visuals minimized; it cannot be played without audio. Every system specified here has a load-bearing audio component.

**Companion docs:**
- `deadringer_systems.md` §1.3 (audio signature map), §3 (Soul Read degradation), §6 (partner degradation)
- `deadringer_locations.md` — per-location audio signature notes
- `deadringer_intent_matrix.md` §3 — per-call audio behavior under each intent
- Chapter files 1–12 — source material for every audio cue referenced here

**Terminology:**
- **Signature** — the core identifiable audio fingerprint of an NPC or location. Present in every scene featuring that NPC/location.
- **Bed** — the ambient layer underneath dialogue. Usually 3–6 elements.
- **Tic** — a specific recurring sound tied to an NPC's behavior (Aizawa's click, Haruki's pen).
- **State variation** — modulations of the signature under specific emotional conditions.
- **Wire-sound** — the game's central audio motif. The hum beneath every call, evolving across chapters.
- **Dropout** — a brief (quarter-second to one-second) failure of Mira's voice, used to signal degradation.

---

## 1. MASTER AUDIO PRINCIPLES

1. **Silence is a texture.** Scenes specified as "silent" are not audio-absent — they are audio-present in a specific way (apartment clock, refrigerator cycle, distant train). The sound designer should treat silence as a design element, not an omission.
2. **Diegesis over score.** The game has no traditional score across Acts I–III. What carries the emotional load is diegetic sound (ambience, character audio, the wire-sound). Music, if used at all, is reserved for the Ch 12 switchboard duel and Epilogue.
3. **Layered listening.** Every call has at least three audio layers: the NPC's voice + their environmental bed + the wire-sound. Players should be able to attend to any layer independently; each carries distinct information.
4. **Audio telegraphs state.** Every character state change (trust shift, approaching break, etc.) should have an audible correlate. The game teaches the player to listen by rewarding listening; audio must be the reward.
5. **Degradation is slow.** Mira's voice curve is designed to be missed on first listen. The sound designer should resist telegraphing the curve. The player should notice the absence, not the effect.

---

## 2. THE WIRE-SOUND (Central Motif)

The wire-sound is the audio thread that connects every scene, every call, and every chapter. It is the sound of the phone infrastructure carrying signals it was not designed to carry.

### 2.1 Core Character

A low-frequency hum with fine texture — not a clean sine, not pure noise. Think: 60 Hz power hum with a subtle harmonic stack on top, filtered through the specific resonance of old copper wire.

Reference registers (for pre-production):
- The background hum of an analog tube amplifier at idle
- The sound of an old intercom system left open on a dead line
- The tinnitus-like pressure of being near high-voltage power lines on a humid day

The wire-sound should *feel* like electricity remembering.

### 2.2 Evolution Across Chapters

The wire-sound changes across the game. The changes should be gradual enough that the player does not consciously register them but substantive enough to affect the scene's atmosphere.

| Chapter | Wire-sound state |
|---|---|
| Ch 1 | Clean. Present but unobtrusive. Mid-low frequency center. |
| Ch 2 | Identical to Ch 1. No change. |
| Ch 3 | Same core; slightly more present when Mira speaks. First hint that the sound is tied to her. |
| Ch 4 | Unchanged in most scenes; the Yui apartment's audio is notable for the wire-sound being *absent* — her apartment's curated silence doesn't carry the Yui call's wire-sound the way Reiko's or Doi's does. |
| Ch 5 | Same core. During Haruki's call, the wire-sound picks up slight modulation — the first very subtle change. |
| Ch 6 | A quarter-tone denser. A subliminal grain in the texture. Most players won't consciously notice. |
| Ch 7 | Noticeably thicker. The harmonics have compressed. A slight roughness. |
| Ch 8 | Crackling. Still mostly smooth but with intermittent clicks — ~1 every 10 seconds. |
| Ch 9 | Distinctly rougher. The harmonics are fighting. Crackles are regular, ~1 every 3–5 seconds. |
| Ch 10 | IN THE EXCHANGE ROOM: clear, structured, *resolved* — the wire-sound becomes something Mira can use. OUTSIDE the exchange room: the rough Ch 9 state. |
| Ch 11 | Distorted. The hum is not stable. Dropouts begin affecting the ambient, not just Mira's voice. |
| Ch 12 | The hum is burning — audible strain, spikes, degradation beyond Ch 11. By the chapter's end, it thins to a single frequency and vanishes. |
| Epilogue | No wire-sound. The absence is the mark. |

### 2.3 Relation to Mira's Voice

The wire-sound is Mira's substrate. Her voice rides on it. Technical implementation: Mira's voice should be filtered such that her fundamental frequency is coupled to the wire-sound — when the hum is clean, her voice is clean. When the hum degrades, her voice degrades with it. This is not metaphor; it should be a literal audio-processing chain.

### 2.4 Spatial Behavior

The wire-sound is center-of-field, low spatial width. It does not move. It is not directional. It feels equally close in headphones and speakers. The sound designer should resist the temptation to add movement — the hum's stillness is part of its character.

### 2.5 The Bridge Scene (Ch 10)

When Kenji re-dials the bridge number in Ch 10, the wire-sound thickens into the structured static of the exchange room. This is the payoff of the Ch 3 setup. The same sound; now comprehensible. Sound designer should treat this as a single waveform evolution across the two chapters — the Ch 3 version is the same signal, less processed.

---

## 3. PER-NPC AUDIO SIGNATURES

For each significant NPC: signature, bed, tics, state variations.

### 3.1 REIKO KITAHARA

**Signature:** the apartment that's too quiet for one person.

**Bed:**
- Wall clock (analog, steady tick — ~60 BPM)
- Kettle cooling on the counter (metal contracting, irregular tiny ticks, audible for ~20 seconds after a boil)
- Space heater hum (low, constant, subtly audible)
- Refrigerator compressor (cycles on ~every 2 minutes, runs for ~30 seconds)

**Tics:**
- Her breath — controlled, deliberate. Measured inhales between sentences. The breath is so controlled it sounds like a conscious performance.
- A small fabric shift when she adjusts on a chair. Infrequent.

**State variations:**
- **Ch 3 (rehearsed):** bed steady, breath controlled, response timing fluent.
- **Ch 9 (static call):** the bed has a secondary hiss layer — the exchange bleeding through. Her breath is less controlled. Small catches between sentences.
- **Ch 11 (in-person, notebook scene):** she is seen, not just heard. The bed is the apartment at midday — different light, different ambient. Less heater, more outside sound.

**Reference:** Yasujirō Ozu's domestic interiors — the measured quiet that is also a held silence.

---

### 3.2 DOI (Yanagi Mart)

**Signature:** the store is always on.

**Bed:**
- Fluorescent buzz (steady ~100 Hz ballast hum)
- Refrigerator compressor (cycles, different pitch from Reiko's — this is a commercial unit)
- Register beeps (scanning a barcode produces 3 quick beeps; drawer opening = 1 deep chunk + mechanical slide)
- Door chime (customer entering = 2 descending tones; leaving = nothing, just the door)
- Radio (volume low, news or easy-listening, never identifiable)

**Tics:**
- His breath — tired, deliberate. He pauses before answering more than he needs to.
- Paper rustling (receipts, bags).

**State variations:**
- **Ch 3 (gruff):** bed busy, his voice compete with it. He doesn't apologize for serving customers mid-call.
- **Ch 3 REDIRECT (streetlight beat):** the store goes briefly quieter — a lull in customer traffic — and his voice emerges more distinctly.
- **Ch 3 PRESSURE (Dignity Filter):** register shift is audible in his voice specifically; the bed doesn't change. He becomes more formal; the store continues as normal. The disjunction is the tell.
- **Ch 6 (false confession):** the bed is audibly reduced — he has turned the radio off. He has cleared the counter of customers. The store is quieter than the player has ever heard it. The reduction is diegetic (he is committing to the confession) and mechanical (his voice must be unobstructed for SILENT to work).
- **Epilogue:** the store is unchanged. The bed is identical to Ch 3. The audio signature is the evidence that the world moved on without him.

**Reference:** the specific acoustic of a Japanese corner shop in the 15-minute lull between the lunch rush and the afterschool wave.

---

### 3.3 YUI SAKAMOTO

**Signature:** curated absence.

**Bed:**
- A clock tick. Steady.
- Fabric shifts (she is sitting on something soft).
- *Nothing else.* No TV, no music, no footsteps, no refrigerator. The absence is the point.

**Tics:**
- Her breath is contained. Measured. Too controlled for an eleven-year-old.
- A small throat-clearing sound before difficult words.
- **Paper folding (primary tell):** Soft, precise creasing sounds beneath her voice. Yui folds origami while she talks — the sound is her self-regulation mechanism and the player's audible health bar.
  - *Steady creasing (~2-3 second intervals):* Composed. Architecture holding. The folds are deliberate, each crease clean.
  - *Accelerating (~1 second intervals, tighter):* Anxiety rising. The paper sounds sharper — smaller folds, less precision, more urgency.
  - *Stops:* The real answer is imminent. Absolute silence — no paper, no breath, no performance. Equivalent of Aizawa's sanitizer click stopping.
  - *Paper tearing (once only):* The break. Slow, deliberate. Not angry — careful destruction. The sound of the fold she was making being unmade. Occurs during "Did anyone come?" — twelve seconds of silence, then the tear, then "She said they would."

**State variations:**
- **Ch 4 (default):** the bed is the absence. The clock is the loudest element. Paper folding is the secondary rhythm — steady, regular, almost soothing against the quiet.
- **Ch 4 PRESSURE (shutdown):** even the clock seems to quieten. The bed collapses to her breath and the folding alone. Folding accelerates — tighter, faster, the paper sounds sharper. This is the audio of a child making herself as small as possible in an apartment where sounds don't carry.
- **Ch 4 SILENT (the fragments work):** the bed remains curated-absence, but Yui's voice gains texture — fabric shifts more, small sounds emerge from a girl who is momentarily less controlled. The folding slows but does not stop. She is not safe enough to put the paper down.
- **Ch 4 BREAK ("Did anyone come?"):** folding stops. Twelve seconds of absolute silence. Then the slow tear — paper being deliberately destroyed. The loudest thing in the scene is the absence of the sound the player has come to expect.
- **Epilogue:** a garden. Birds. Wind. The grandmother's kitchen radio in the distance. No folding. This is the first time Yui is heard in a space with ambient life and without paper in her hands. The contrast is the scene's entire emotional weight.

**CRITICAL DESIGN NOTE:** Yui's apartment has the least ambient sound of any scene in the game. The sound designer must resist filling the space. Every instinct to add texture should be audited — is this sound serving the scene, or am I uncomfortable with silence? The discomfort is the design.

---

### 3.4 RINA NISHIZAWA

**Signature:** ambient social context — she is always in a populated place.

**Bed:**
- Other children's voices in the distance (non-distinct, treated as crowd ambience)
- Playground or classroom sounds depending on when the call is placed
- Occasional footsteps passing her
- A school bell at scheduled intervals

**Tics:**
- None personal. Her voice itself is the tic — cheerful, well-calibrated, performatively warm.

**State variations:**
- **Ch 4 (default):** the bed is school context. She modulates her voice for the adults around her — subtle, but audible; she is never purely alone on the line.
- **Ch 4 REDIRECT (off-guard):** the bed is briefly less present — she has stepped aside for a more private exchange — and her voice modulates less. Information leaks.
- **Ch 4 PRESSURE:** the bed stays; her voice goes cheerier. Defensive deflection is delivered at higher pitch.

**Design note:** Rina's audio signature is less distinctive than other NPCs'. Consider strengthening via a specific, identifiable ambient element — e.g., a recognizable schoolyard bell pattern that becomes her recurring audio signature across scenes.

---

### 3.5 HARUKI ISE

**Signature:** overflow motion.

**Bed:**
- Empty classroom after hours
- Distant hallway sounds (janitor's cart, a door closing somewhere, HVAC)

**Tics (primary audio character):**
- **Pen clicking** — not rhythmic; irregular, nervous. Approximately 1 click every 1–3 seconds. Variable.
- **Chair squeaking** — he shifts every 10–15 seconds.
- **Papers shuffling** — whenever he talks about evidence or records.

**THE TELL:** once per call, all three tics STOP. 2–3 seconds of complete stillness from him. This is the load-bearing audio beat.

**State variations:**
- **Ch 5 (incoming, default):** tics active, overflow running.
- **Ch 5 tell moments:** one during "Sora Hayashi" reveal, one during Endo committee reference. The cessation is the scene's anchor.
- **Ch 6 (post-PoNR):** tics intensify. Faster clicking, more chair movement. He is more agitated, not less.
- **Ch 9 (break scene):** tics stop, then resume differently. When he resumes, the clicking has a different rhythm — slower, deliberate, directed. "Anger that has found its target" delivered audibly.
- **Ch 11 (case assembly):** tics are minimal. He has transformed. The quiet is the evidence of the transformation.
- **Epilogue:** no tics. His restless energy has re-directed. He is still moving, but the motion has purpose; the motion is no longer audible as fidget.

**CRITICAL:** the sound designer must ensure the tell (complete cessation) is mechanically unambiguous. A 0.5-second pause reads as a stumble; a 2-second pause reads as the tell. Calibrate.

---

### 3.6 AIZAWA EMI

**Signature:** THE SANITIZER CLICK.

**Bed:**
- Fluorescent hum (school office, slightly brighter than Doi's store)
- Hallway sounds during school hours (children, distant)
- Complete quiet after hours (Ch 8 break scene is after-hours — nothing in the bed but the hum and the click)

**Tics (singular):**
- **Sanitizer bottle pump clicking.** Mechanism only — the pump does not complete. Just the click of the mechanism being engaged and released. Single-handed, absent-minded.

**State variations (read through click rate):**
- **Ch 5 (default):** ~1 click every 4–5 seconds. Steady.
- **Under REASSURE:** rate slows to ~1 every 6–7 seconds.
- **Under PRESSURE:** rate speeds to ~1 every 2 seconds.
- **Ch 8 break (approaching):** rate accelerates to ~1 per second.
- **Ch 8 break (moment):** THE CLICK STOPS. Complete cessation for 4–6 seconds before she speaks. This is the singular load-bearing audio moment of her arc.
- **Ch 8 post-break:** no more click. The bottle has been set down.
- **Ch 11 case assembly:** no click. It is established.
- **Epilogue:** the bottle is gone. The audio signature is the absence.

**PRODUCTION:** a library of click-rate variations recorded from a single sanitizer bottle should be the source. The click should be the same click at all rates — it is the frequency that changes, not the sound. This makes the rate legible as character state.

---

### 3.7 FUMIKO ARAI

**Signature:** the pen that never stops.

**Bed:**
- Workspace after hours (keyboard clacks occasionally, small fan, distant city)
- Filing cabinet drawer closing (once per call, usually mid-conversation)

**Tics:**
- **Pen scratching on paper.** Continuous. Different character from Haruki's clicking — this is deliberate, directed note-taking. Long strokes, pauses between words.

**State variations:**
- **Ch 6 (default):** scratching continuous. Transactional register.
- **Ch 6 melon-bun beat:** the pen LIFTS for the duration of the anecdote. Clean silence from her side for ~8–12 seconds. This is the first time the pen stops. The signature of her warmth is its absence.
- **Ch 7 (bluff moment):** pen scratches faster — she is recording the bluff for post-call analysis.
- **Ch 9 (Ogawa deep):** the scratching changes rhythm — she is writing, not note-taking. Denser.
- **Ch 11:** pen is more measured. She is finishing the story, not starting it.
- **Ch 12 (publication decision):** pen is loud and present. She is actively drafting the headline.

**Reference:** the specific sound of a fine-point ballpoint on quality paper, not notebook paper. Fumiko uses a good pen.

---

### 3.8 KAITO NISHIMURA

**Signature:** the unfiltered room.

**Bed (everything audible at all times):**
- Fan oscillating (the oscillation arc is audible; end-of-sweep pauses are perceptible)
- Clock with loud second hand (distinct tick, quartz, slightly off-beat with a real clock's physics)
- Refrigerator cycling (different pitch again — home refrigerator)
- Occasional distant bird
- A neighbor's TV just barely audible through the wall

**Tics:**
- **Pencil tapping** — arrhythmic, idle. Different from Haruki's clicking (pencil on hard surface, softer attack) and Fumiko's scratching (writing, not tapping).

**State variations:**
- **Ch 7 (default):** full bed, pencil tapping. His native register.
- **Ch 7 PATIENCE path:** pencil STOPS as he begins reading from notebook. A notebook spine cracks audibly. He is organized; the bed continues.
- **Ch 7 SILENCE path (hidden gate):** the bed changes. He has turned the fan off partway through the call without explaining why. The room is momentarily less busy. He is paying more attention to the conversation than he has before. The reduction is the audible tell of the personal disclosure to come.
- **Epilogue:** Kaito is walking his route. Outdoor ambient. The unfiltered room is not where he is. The pencil is not audible because it isn't there anymore (he has stopped carrying the notebooks).

**CRITICAL:** Kaito's audio must feel inclusive, not cluttered. A player should feel they could pay attention to any element of his bed and learn something. The design is not "busy room" but "room where nothing is being filtered out."

---

### 3.9 ENDO MASATO

**Signature:** measured silence.

**Bed:**
- A clean line. Minimal ambient.
- A faint clock (antique, wooden, more refined than other NPCs' clocks).
- Occasionally, a page turning (slow, deliberate).
- Nothing else.

**Tics (the absence of tics):**
- **He does not fidget.** No pen, no fabric shift, no throat-clearing.
- **His breath is even** enough to be audible between sentences.
- **His pauses are measured.** Consistently 3 seconds for emphasis, rarely more.

**State variations:**
- **Ch 8 (first call):** measured warmth. The breath and the pauses are the entire audio of him.
- **Ch 9 BLUFF response:** a shorter pause before his answer. 1 second instead of 3. This is the only calibration-signal he produces unprompted.
- **Ch 9 REDIRECT response:** his longest pauses — up to 5 seconds — as he selects which way to redirect.
- **Ch 9 SILENT response:** he does not fill the silence for 5 seconds, then he speaks. The length before his speech is the tell.
- **Ch 11 confrontation Phase 2:** the first silence he cannot fill. 3 seconds extends to 5, to 7. The breath audibly changes — shallower, a subtle swallow. The first audio sign of strain.
- **Ch 11 Phase 5 (counsel):** his pauses shorten. He has committed to a position; he is no longer calibrating. The audio becomes crisper.
- **Ch 12 arrest:** no dialogue. Handcuffs and a car door. No audio of Endo speaking.

**DESIGN PRINCIPLE:** Endo is the only NPC whose signature is what he *doesn't* do. The sound designer must resist adding character sounds to him. Every addition erodes his function.

---

### 3.10 MIRA (Special Case — Voice Direction in §5)

Mira is not a standard NPC. Her audio is treated in §5 as a voice-direction concern rather than a signature-and-bed concern. Her "bed" is the wire-sound (§2); her "signature" is her voice's evolution across chapters.

---

## 4. ENVIRONMENTAL AUDIO PER LOCATION

Cross-reference with `deadringer_locations.md`. Per-location audio specs:

### 4.1 Kenji's Apartment

**Bed:**
- Refrigerator compressor (6 seconds on, 97 seconds off — rhythmic and recurring across the game; see Ch 11 3 AM scene where the rhythm is explicitly noted)
- Analog clock on the kitchen wall (slightly irregular tick — NOT rhythmic, which is the signature)
- Distant train on the Chuo line (variable intensity, ~every 4–8 minutes)
- Occasional bicycle bell or passing voice outside

**State variations (evolves across chapters):**
- **Ch 1 (cold open):** wire-sound is faint. Clock and fridge dominate.
- **Ch 3–7:** unchanged. The apartment is stable.
- **Ch 8–10:** wire-sound thicker.
- **Ch 11 3 AM scene:** refrigerator cycle is explicitly counted ("six seconds on, ninety-seven seconds off"). The rhythm should be recognizable to the player by this point. Wire-sound is thin, present but conserved.
- **Ch 12:** wire-sound degrades through the day.
- **Epilogue:** no wire-sound. Fridge, clock, train as they were in Ch 1.

### 4.2 Yanagi District Exterior (Ch 2)

**Station exit:** train departure behind Kenji, residential quiet ahead. Transitional audio moment — treat as a foley moment.

**Block 1 (residential):** weekday residential ambient — distant bicycles, a sprinkler, a grandmother's radio barely audible.

**Block 2 (pharmacy):** commercial block — awnings rolling out, low-volume conversations inside shops.

**Block 3 (school approach):** muted children's voices from upper windows, a distant school chime.

**The Bench:** ambient street.

**Community board intersection:** commercial-residential transition; quieter than Block 2.

**River path:** the audio transition at the descent is the chapter's most important ambient moment. Neighborhood sounds fall away; water / birds / wind emerges. Design this as a hard-but-not-abrupt mix shift over ~8 seconds as Kenji descends.

**The Bridge:** water accelerates through the channel; echo in the underside space. The scratched phone number, when dialed in Ch 3, produces structured static. In Ch 10, Kenji dials again and the structured static is recognizable as the wire-sound's core — the same signal, now understood.

**The Park:** bird calls, wind through bare branches, empty playground swing chains clattering. The silver-car sight line audio: residential street audible on the east side.

### 4.3 Community Center Exterior

Residential-adjacent. Quieter than the commercial strip. The payphone does not ring. Epilogue: a chain on the side entrance (audible when Kenji passes).

### 4.4 Community Center Main Hall

Empty-building reverb. Fluorescent hum. Footsteps carry. As Kenji moves toward the basement stairs, a faint subsonic hum from below. The exchange's residual charge, audible-but-below-consciousness. The player may not register it.

### 4.5 The Exchange Room (Ch 10 Set Piece)

**PRIMARY AUDIO SET PIECE OF THE GAME.**

**Layered design:**
- Base layer: the wire-sound, now structured and present — the same frequency as the bridge number from Ch 3, scaled up in presence
- Secondary layer: dozens of frequencies overlapping. Each frequency represents a residual charge from a past conversation. Not words — impressions.
- Tertiary layer: the boy's voice (Sora) barely audible, cataloging his surroundings. "...small..." "...the pipe makes a sound when it gets cold..." "...there's a blanket but it smells like dust..."
- Quaternary layer: the girl asking for her mother. Even fainter. Thin high frequency.
- Mira's voice, amplified: room-close, present, Ch 1 quality.

**Design:** the listener should be able to attend to any single layer and hear it clearly. All layers must coexist without masking. The secondary layer (the dozens) is the hardest to design — it needs to feel like residue, not like a chorus.

**Reference:** for the secondary layer, consider the sound of a shortwave radio tuning across multiple stations in a dead hour — fragmentary, overlapping, each station distinct but none complete.

**State evolution within the chapter:**
- On first entry: ambient dominates, Mira is a voice among many
- As the scene progresses and Mira amplifies: her voice clears and centers
- At scene close: structured but still carrying the other layers underneath

**Ch 12 state:** the exchange is being used harder than it was built for. The structured static gets denser, begins to distort. By the chapter's end: the signal collapses. Silence.

### 4.6 Community Center Meeting Room (Ch 11 Confrontation)

Windowless, soundproofed, fluorescent hum. No ambient from outside — this is the most isolated audio space in the game. Endo's measured breath becomes audible between sentences. The cork board notices and the whiteboard are visual; the audio is the hum plus the two men.

During the confrontation's phase transitions: no music, no audio shift. The silence between phases is the tell. Phase 2's silence (the first Endo cannot fill) should be MECHANICALLY LONGER than any other silence in the game up to this point.

### 4.7 Yui's Grandmother's Home (Epilogue)

Real birds. Wind through ornamental grasses. A neighbor's distant television. The grandmother's small domestic sounds inside the house (pot, radio, water). Everything Yui's apartment did not have.

### 4.8 Sora's Classroom (Epilogue)

Ambient classroom after-hours. Distant corridor voices. Old wall clock. A fan somewhere. The specific quiet of a space that was loud and will be loud again.

---

## 4B. THE YANAGI PHONE PHENOMENON — AUDIO DESIGN

The town's phone infrastructure is half-alive. These sounds escalate across the game as the exchange bleeds into daily calls. The escalation is reactive — it intensifies as Kenji investigates and Endo monitors harder.

### Layered Static

The baseline phone phenomenon. Yanagi calls have a subtle secondary texture beneath normal static — structured, almost rhythmic, like two signals running on the same wire. This is the exchange's ambient bleed-through.

- **Ch 1-3 (ambient):** Barely perceptible. A slight texture to the bridge number's static — patterned, not random. Most players will not consciously register it. The static has periodicity, as if something is cycling in the infrastructure.
- **Ch 4-5 (noticeable):** The layering becomes audible during calls to Yanagi numbers. A second frequency beneath the primary signal. Mira describes it as "layers — like two things playing at once."
- **Ch 8-9 (active):** The layering is pronounced. Calls develop faint echoes — a doubling in the audio, as if the line is being mirrored. Fragments of other conversations intrude at the edges of calls. Brief, half-audible, never fully intelligible.
- **Ch 10-12 (the exchange):** Full infrastructure sound. The static resolves into the exchange's operational frequency — the sound of decades-old telephone infrastructure that never fully shut down.

### The Wrong Connection (Ch 5 — Micro-Incident 1)

A call routing error. The audio signature: normal dial tone, normal ring, then a *click* that sounds slightly different from a standard connection — a half-second of dead air followed by a voice already mid-sentence. The voice is not addressing Kenji. It is a conversation already in progress, bleeding through. When the line cuts, there is a distinct pop — not a hang-up, a disconnect. The infrastructure releasing.

### The Breathing (Ch 7 — Micro-Incident 2 / THE PIVOT)

The most important single audio event in the game. The scene's audio must be designed with extreme precision:

- **Setup:** The static on the line changes texture — the layered quality from earlier chapters becomes more prominent, more structured. The two-signal effect is no longer subtle.
- **Mira's "wait":** Her voice drops to near-whisper. The Soul Read processing tone (if one exists) stops.
- **The breathing itself:** Shallow. Small. Rhythmic. A child's breathing — not distressed, not panicked, but measured the way a frightened child measures breath to stay quiet. Audible for exactly four seconds. It is present in the infrastructure layer, not the call layer — as if it is coming from inside the wire, not from a phone.
- **Disappearance:** The breathing fades rather than cuts. The static returns to its previous texture. The infrastructure settles.
- **Critical:** The breathing must be unmistakable once the player hears it but not startling. It is not a jump scare. It is the quiet horror of realizing something alive is inside a system designed for signals.

### Call Bleed-Through (Ch 8-9)

Post-pivot, calls carry echo artifacts:
- **Faint doubling:** A 50-100ms delay on certain words, as if the line is being monitored and the monitoring creates a reflection.
- **Fragment intrusion:** Brief (1-3 second) bleeds of other audio — a voice, ambient sound from a different location, a phone ringing somewhere else in the network. These are real conversations being routed through the exchange. Never fully intelligible. Always at the edge of perception.
- **Selective intensity:** The bleed-through is stronger on calls to certain NPCs — mapping to which conversations Endo is monitoring most closely. This is a subtle clue layer the player may or may not track consciously.

---

## 5. MIRA'S VOICE DEGRADATION — AUDIO DIRECTION SPEC

Mira's voice curve is the game's most load-bearing audio design. See `deadringer_systems.md` §6 for the curve; this section specifies the audio processing chain.

### 5.1 Base Voice

Mira's voice is nine years old. The actor must land:
- Precise diction (she is a child who finishes sentences)
- Deadpan delivery (comedy without inflection)
- Measured pauses (she thinks before she speaks)
- Warmth underneath the armor (the warmth should not be performed — it should leak)

**Processing at baseline (Ch 1–3):** minimal. A slight phone-filter (telephony band-limiting, ~300 Hz – 3.4 kHz). The wire-sound is present but does not color her voice. Her voice sits on top of the wire-sound cleanly.

### 5.2 Degradation Processing Chain

Across the game, Mira's voice is progressively processed. Each stage adds one or more treatments:

| Stage | Chapters | Processing Additions |
|---|---|---|
| Clean | 1–3 | Baseline phone-filter only. |
| First Waver | 4–5 | Micro-dropouts (5–15ms gaps) at irregular intervals. Subtle; listener notices subconsciously. |
| Noticeable Decline | 6–7 | Micro-dropouts more frequent. Slight high-frequency attenuation. Voice less crisp. |
| Degraded | 8–9 | Macro-dropouts (100–400ms) at emotional beats. Bandwidth further compressed (~500 Hz – 2.8 kHz). Occasional brief noise bursts layered with her words. |
| AMPLIFIED (Ch 10) | 10 | All processing REMOVED. Full clean voice, room-close miking. The contrast is the design. |
| Post-Amplification Crash | 11 | All Ch 8–9 processing returns, heavier. New: mid-word cutouts (voice begins a word and fails partway, hard cut to noise). |
| Final Signal | 12 | Heaviest processing. During the call to Sora, briefly the processing LIFTS — clean voice for ~20 words — then the line goes fully dead. |

### 5.3 Breath, Pace, Filter Coupling

Mira's breath, pace, and the wire-sound are mechanically coupled:

- **Breath:** at clean baseline, her breath is nearly inaudible. As she degrades, breath becomes audible — short catches, shallow inhales between sentences. In Ch 11, the breath between words is longer than the words themselves.
- **Pace:** degradation slows her pace. Ch 1 Mira delivers at normal conversational speed. Ch 11 Mira delivers at roughly 60–70% of Ch 1 speed. The slowness is not pausing for effect — it is the cost of speaking.
- **Filter coupling:** Mira's voice filter is keyed off the wire-sound. When the wire is clean, she is clean. When the wire is crackling (Ch 8–9), her voice carries the crackle. This coupling is mechanically implemented, not performed.

### 5.4 Load-Bearing Delivery Specifications

Specific moments where the voice direction matters critically:

**Ch 3 Reiko read — "love shaped wrong":** delivered slowly, deliberately, with full presence. This is the game's first demonstration of how precise Mira can be when a read lands. The three words should feel deliberate — she is choosing them, not reporting them.

**Ch 6 Doi confession read — "like a room where every radio is on a different station":** delivered with distaste. Mira does not like the sensation she is describing. The metaphor should sound specifically constructed — she built it because she needed it.

**Ch 8 Endo read — the locked room:** delivered with confusion bleeding into fear. "I can't get in" is the first time Mira admits a limit. The admission should land as a seam in her armor, not a fact.

**Ch 10 amplification — "there are others":** the voice that has been thinning for three chapters returns to full presence. The shift should be emotionally seismic. The performer should find early-game Mira again; the processing lift supports her.

**Ch 11 "you didn't hang up":** the voice is thin, conserving, but the emotional load of this line is the chapter's weight. The line should be delivered clean of irony — Mira is being sincere, and the sincerity should be startling to a player who has learned her sarcasm.

**Ch 11 humming:** Mira hums half a tune she hasn't finished in four years. She has never been heard singing. The hum should be thin, private, slightly off-key — a child's voice in recall, not performance.

**Ch 12 call to Sora — "Someone is coming. His name is Kenji. He's grumpy but he listens":** the processing LIFTS briefly. Mira is spending the last of her signal on clarity for a frightened child. The actor's delivery should be warm but urgent. Twenty words. No self-awareness. She is doing a job.

**Ch 12 final line — "My name is Mira. Please remember it":** the last clean delivery. After it: static, then nothing. The line should not sound like a goodbye. It should sound like a file being closed.

### 5.5 Voice Actor Briefing Points

1. **Mira is funny because she is protecting herself.** Do not perform the humor as delivery. Deliver flatly; let the words do the work.
2. **Mira is a child.** Not a precocious adult in a child's body. Her sentences are child-length. Her vocabulary is child-level. Her observational precision is unusual for her age, but her register is age-appropriate.
3. **The degradation is involuntary.** Mira does not notice she is thinning. She does not announce her own decline. The actor should not telegraph fatigue — that is the processing chain's job.
4. **Armor is the default.** Mira's armor drops three times across the game: Ch 4 crying scene, Ch 11 3 AM scene (partial), Ch 12 final call (full). Every other moment, she is armored.
5. **Do not play death.** Mira does not know she is fading. She is aware of the limit but she is curious about it, not afraid. Play curiosity.

---

## 6. SOUND DESIGN DELIVERABLES

### 6.1 Master Asset Lists

1. **Wire-sound library** — 12 chapter-state variations + amplified state + Ch 12 collapse. Total: ~14 unique wire-sound assets with specified transition logic between them.
2. **NPC audio signature library** — 9 NPCs × (base + ~4 state variations each) = ~45 signature assets. Plus bed elements (each NPC's 3–6 bed layers) = ~40 additional assets.
3. **Location audio beds** — per `deadringer_locations.md`, one bed per location × time-of-day states = ~30 location bed assets.
4. **Mira voice processing chain** — implementable as a VST/plugin chain, not discrete assets. State transitions keyed off chapter progression.
5. **Exchange room special** — ~8 specialized layer assets (wire structured, residual voices, Sora voice, girl voice, Mira amplified, etc.).

### 6.2 Mixing Targets

- **Dialogue clarity** — NPC voice must always be legible, even when the bed is busy. Reference mix target: dialogue at –14 LUFS, bed at –24 LUFS, wire-sound at –28 LUFS baseline.
- **Dynamic range** — preserve a wide dynamic range. The Ch 11 confrontation's phase-2 silence should feel genuinely quiet. Do not compress the game into uniform loudness.
- **Accessibility:** full captions, with audio-description layer as optional secondary audio (see `deadringer_systems.md` §8.5).

### 6.3 Open Questions for Sound Designer

1. **Wire-sound motif music.** Should the wire-sound motif appear in an orchestral arrangement during the Ch 12 climax, or is the game strict about never scoring? Recommendation: strict. Confirm with director.
2. **Mira's voice — live actor or procedural?** Live actor. The degradation is processing on top of the live take. Do not substitute procedural voice synthesis for late-game Mira; the performance must be human throughout.
3. **Audio-description script.** Who writes it? Recommend: the game's dialogue writer drafts the AD script, sound designer reviews for audio-layer clarity.
4. **Localization.** How does the NPC audio signature library adapt to dubbed languages? The beds are language-independent; the voices are not. The degradation chain is voice-independent and can apply uniformly to any language. Confirm with localization team.

---

## 7. CROSS-REFERENCES

- `deadringer_systems.md` §1.3 (audio signature map), §3 (Soul Read degradation), §6 (partner degradation)
- `deadringer_locations.md` — per-location audio notes
- `deadringer_intent_matrix.md` §3 — per-call audio behavior under each intent
- Chapter files 1–12, epilogue — source material

---

**END AUDIO SIGNATURE SPECIFICATION**
