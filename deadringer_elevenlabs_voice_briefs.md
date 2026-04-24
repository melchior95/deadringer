# DEAD RINGER — ElevenLabs Voice Briefs

Production-ready voice direction for every speaking character in the game. Each brief specifies: voice selection strategy (library vs. clone), ElevenLabs parameter recommendations, sample lines for dial-in, state variations, post-generation processing, and known pitfalls.

**Companion docs:**
- `deadringer_soul_read_voice_direction.md` — full voice coaching for Mira across 12 chapters (primary reference for Mira)
- `deadringer_audio_signatures.md` §3 — per-NPC audio signatures, state variations, and environmental beds
- `deadringer_characters.md` — character bibles (register, emotional state, behavioral tics)
- `deadringer_asset_pipeline.md` §4 — voice production phase overview

**Scope:** 11 named speaking characters (Mira + 10 NPCs) + exchange-room residue voices. Approximately 2,500 unique line deliveries across the game.

---

## 0. ELEVENLABS PARAMETER PRIMER

Brief primer for anyone new to the platform. Skip if you've shipped ElevenLabs work before.

### 0.1 Three Core Sliders

**Stability (0–100):** how consistent the voice is across long generations.
- **Low (0–30):** highly variable, more emotional range, may sound uneven
- **Medium (30–60):** balanced — expressive but consistent
- **High (60–100):** near-monotone, stable across long passages, risks flatness

Dead Ringer default range: 40–55 for most characters. Higher for controlled NPCs (Endo, Aizawa), lower for emotional beats.

**Similarity Boost (0–100):** how closely the output matches the source voice.
- **Low (0–40):** model drifts; good for variety, bad for consistency
- **Medium (40–70):** recognizable as the source, flexible
- **High (70–100):** locked to source; consistent but may sound less natural

Dead Ringer default range: 70–85 — character consistency is a hard requirement.

**Style (0–100):** expressive intensity ("performance energy").
- **Low (0–20):** flat, deadpan, reportorial
- **Medium (20–50):** natural conversation
- **High (50–100):** performative, theatrical

Dead Ringer default range: 10–25 — the game's acting direction is "deliver flatly, let content do work." High Style values break the register for nearly every character.

### 0.2 Speaker Boost

Toggle. ON = amplifies speaker similarity at small coherence cost. Recommend ON for all Dead Ringer characters. The coherence cost is negligible in our tested settings; the consistency gain is worth it.

### 0.3 Models

- **Multilingual v2:** best quality, slowest, supports 29 languages
- **Turbo v2:** faster, English-only, slightly lower quality
- **Flash v2:** fastest, lowest quality, useful for prototyping only

Recommend **Multilingual v2** for final delivery — Dead Ringer's localization ambitions require it. Turbo v2 for iteration rounds.

### 0.4 Voice Selection Options

**Library voices:** instant, no training, limited range of real voice qualities. Good for ~60% of Dead Ringer's cast.

**Voice Cloning (Professional):** clone from a 30-minute audio sample of a real voice actor. Higher quality, requires source material. Recommended for Mira and the three child NPCs (Yui, Rina, Sora).

**Instant Voice Cloning:** clone from ~1 minute of audio. Faster, lower consistency. Adequate for Sora's brief exchange-room residue work but not for his named character lines in Ch 12 / Epilogue.

### 0.5 Session Practice

Lock Voice ID for each character at the start of production. Do NOT re-clone mid-project — the voice will drift. Record baseline takes for each character in session 1. Subsequent sessions use the same Voice ID + saved parameter profiles.

---

## 1. GLOBAL PRODUCTION PRINCIPLES

### 1.1 Flat Delivery as Default

The game's acting register is uniformly understated. Every character is directed away from theatrical performance. Consequences for ElevenLabs:
- Set **Style** low by default (10–25)
- Request "plain" deliveries in any prompt text
- Trim breaths and emotion markers from source text where possible
- Audition against the "flat delivery" test: does the line sound like news-reading or acting?

### 1.2 Consistency Across Sessions

- Record voice profile parameter sets per character, save as JSON
- Re-use same model version across all sessions (do not upgrade mid-production)
- Keep source clone audio archived — regenerating from fresh clones breaks continuity

### 1.3 Processing Chain (All Voices)

Every final voice asset passes through:

1. **Baseline normalization** — loudness-normalize to −18 LUFS for dialogue
2. **De-esser** — ElevenLabs tends to over-sibilant
3. **Mild compression** — 2:1 ratio, slow attack
4. **Phone filter** (for call scenes only) — band-limit to ~300 Hz – 3.4 kHz to simulate telephony
5. **Character-specific post** — Mira's degradation chain (see §2.6), Aizawa's breath emphasis, etc.

### 1.4 Do Not Use TTS "Emotion" Tags

ElevenLabs supports emotion hints in text (e.g., `[sad]`, `[angry]`). AVOID THEM for Dead Ringer. The game's tone requires delivery flatter than the emotion tags produce. Inline emotion markers break the register.

### 1.5 Line Punctuation for Pace Control

ElevenLabs respects ellipses and em-dashes for pacing. Use deliberately:
- `...` = HOLD pause (1–2 seconds)
- `. . .` = LONG pause (3+ seconds)
- `—` = hard stop / interruption
- Single `.` at end of line = natural sentence end
- `.` mid-line = slight pause

For Mira's degradation states, use multi-period pauses liberally. For Endo's measured rests, use `.` with deliberate spacing.

---

## 2. MIRA KITAHARA (Primary)

**Line count estimate:** 1,500–2,000 unique lines across the full game.

**This is the game's most important voice.** Everything else is supporting cast.

### 2.1 Voice Selection Strategy

**Approach:** Professional Voice Clone.

**Source material requirement:** 30 minutes of clean audio from a voice-over artist delivering child-age performance. Preferred qualities in source actor:
- Age: 18–25 VO artist skilled at 8–10 child register (adult actors preferred for labor law and session availability)
- Native or near-native Japanese English accent (soft Tokyo dialect is fine; heavy regional accents distract)
- Capable of deadpan delivery (can "read a fact" without lifting pitch)
- Range includes warmth (Ch 11 3 AM scene) without descending into saccharine
- Unaffected (not trained-musical-theatre)

**Source script:** record the 30-minute clone sample using lines from chapter 3 (baseline armored register) + Ch 4 disclosure + 1–2 lines from Ch 10 amplification. This establishes full dynamic range in the clone source.

**Alternative (lower budget):** Library voice audition. As of the latest model versions, 2–3 library voices approximate the register but none of them will nail all three registers (armored / leaking / unarmored). If library is the choice, plan for manual post-processing to carry emotional range.

### 2.2 Parameter Profiles by Register

Mira operates in three registers. Each has a distinct ElevenLabs parameter profile.

**ARMORED (default, ~85% of Mira's lines):**
- Stability: 55
- Similarity Boost: 80
- Style: 15
- Speaker Boost: ON
- Model: Multilingual v2

Register description: clinical, precise, dry. Facts-first delivery. Use for all Ch 1–3 lines, most Ch 4–7 lines, all post-call observations.

**LEAKING (specific moments, ~10%):**
- Stability: 45
- Similarity Boost: 80
- Style: 25
- Speaker Boost: ON

Register description: armor showing a seam. Slightly more emotional access. Use for: post-Reiko-read quiet, Yui disclosure, the "Somebody had to be" beat, load-bearing Soul Reads.

**UNARMORED (three moments, ~5%):**
- Stability: 35
- Similarity Boost: 85
- Style: 30
- Speaker Boost: ON

Register description: the armor is off. Used only for the crying scene (Ch 4 or Ch 5–6 deferred), the Ch 11 3 AM disclosures (the dog name, "you didn't hang up"), and the Ch 12 final call to Sora. Do NOT use for any other line.

### 2.3 Sample Lines for Dial-In

Use these five lines to verify the clone is working before committing to a full session:

1. **Armored baseline:** `"You have three numbers."` (expected: flat, declarative, no lift)
2. **Armored with dry humor:** `"Also, she makes terrible coffee. That's not relevant. I just want it on record."` (expected: the second and third sentences delivered at the same flat pace as the first — the joke arrives as a fact)
3. **Leaking:** `"Stop. You're losing her."` (expected: brief, tight, concerned without being panicked)
4. **Unarmored partial (3 AM scene):** `"I don't know what I am. I've stopped trying to figure it out."` (expected: quieter, slower, the armor visibly thinning)
5. **Amplified (Ch 10):** `"Oh."` (expected: single word, present, wonder-quality — the contrast with the three preceding degraded chapters)

If the clone can land all five without manual intervention, proceed to full generation. If lines 1–3 work but 4–5 fall flat, plan for manual re-takes of the unarmored moments.

### 2.4 Degradation Processing Chain

Mira's voice is progressively processed across the 12 chapters. The ElevenLabs generation produces the performance; post-processing produces the decay. Reference `deadringer_audio_signatures.md` §5.2 for the technical spec.

Summary stages:

| Chapter | Post-processing |
|---|---|
| 1–3 | Phone filter only |
| 4–5 | + micro-dropouts (5–15ms random) |
| 6–7 | + HF attenuation, more frequent micro-dropouts |
| 8–9 | + macro-dropouts (100–400ms on emotional beats), bandwidth narrowing |
| 10 | Post-processing LIFTED for exchange room scenes |
| 11 | All Ch 8–9 processing returns + mid-word cutouts |
| 12 | Heaviest processing + a cleanup moment for the Sora call (20 words clean) |

**Do NOT use ElevenLabs' built-in "aged voice" effects or similar.** They produce gravel and age, not degradation. Dead Ringer's degradation is infrastructural, not biological.

### 2.5 Load-Bearing Lines (Voice-Direction-Critical)

From `deadringer_soul_read_voice_direction.md` §3, eleven moments where voice direction is especially precise. For each, additional ElevenLabs guidance beyond the parameter profile:

1. **Ch 1 "Please write down a number"** — use Armored profile. Generate 3 takes; select the one where "number" lands with the least pitch-rise.
2. **Ch 3 Reiko read — "love shaped wrong"** — use Leaking profile. Manually split the three words with individual takes and composite — ElevenLabs may rush the spacing.
3. **Ch 4 "She doesn't know I'm dead"** — Armored profile, but request the line with a beat before "dead." Stability at 45 for this line.
4. **Ch 4 crying scene** — Unarmored profile. Generate ~15 takes, select the ones where breath is audible but not performed. Manual compositing likely required.
5. **Ch 6 Doi confession read — "every radio on a different station"** — Leaking profile. Use the metaphor-construction ellipsis punctuation to produce the slight mid-line pause that makes the line sound invented on the spot.
6. **Ch 8 Endo locked room — "I can't get in"** — Leaking profile with Stability 35 (drop from 45 to get the uncertainty). Generate 10+ takes; the right one has a specific small confusion.
7. **Ch 10 amplified "There are others"** — Armored profile BUT with post-processing lifted. The clean voice plus the flat register is the chapter's emotional register.
8. **Ch 10 "He's doing what I did"** — same as #7. The repetition in "He's — he's" should be natural — use the em-dash to force the stutter.
9. **Ch 11 3 AM "I was supposed to have a dog"** — Unarmored profile. Record as a single take, do not split. The line's arc requires continuous delivery.
10. **Ch 11 "you didn't hang up"** — Unarmored profile, Similarity Boost raised to 90 for consistency with earlier Mira. The delivery must sound like the same Mira the player has heard for eleven chapters, just without armor. Critical: do NOT let the model add emotional coloring.
11. **Ch 12 final call to Sora — "My name is Mira. Please remember it."** — Unarmored profile, post-processing LIFTED for this call. Generate 5+ takes; select the one that sounds least like a goodbye. It should sound like filing.

### 2.6 Humming (Ch 11 3 AM Scene)

**Special case.** Mira hums half a tune in the 3 AM scene.

ElevenLabs does not produce reliable humming. Approach:
1. Have the voice actor record humming as raw source during the clone session (part of the 30-minute sample)
2. Process the humming through the Ch 11 degradation chain
3. Do NOT attempt to generate humming via ElevenLabs text-to-speech

If a live recording isn't available: use a placeholder and flag for re-recording in audio post.

### 2.7 Pitfalls to Avoid

- **Over-emoting:** ElevenLabs default settings lift too much. Start with Style 15, adjust UP only if the line is truly emotional.
- **Aging drift:** some library voices age the performance from line to line. If using a library voice, monitor across session for drift.
- **Breath synthesis:** ElevenLabs adds breath on its own. For Mira's baseline, this is usually fine. For degraded chapters, the synthesized breath is wrong (it sounds like a healthy breath, not a strained one). Manual breath insertion from voice actor's recorded breath library is recommended Ch 8+.
- **Sibilance:** child voice clones tend toward excess sibilance on "s" sounds. Apply de-esser aggressively in post.

---

## 3. KENJI ODA

**Line count estimate:** ~500 unique lines.

### 3.1 Voice Selection

**Approach:** Library voice.

**Reference:** 38-year-old male, tired-steady, dry. Archetype: world-weary detective voice without affected gravel. Think Gerald McRaney's quieter register, or Mitsuru Miyamoto in lower-key delivery.

**Library candidates to audition:** ElevenLabs Premium library voices tagged "middle-aged male," "calm," "narrator." Test 3–5; select the one that reads "tired without whiny."

### 3.2 Parameter Profile

- Stability: 60
- Similarity Boost: 75
- Style: 15
- Speaker Boost: ON

High Stability because Kenji's register is uniform across the game. He does not modulate. Low Style because his humor is always deadpan.

### 3.3 Sample Lines

1. **Baseline (Ch 1):** `"Oda. Can you give me a number I can call you back at?"` (expected: flat, procedural, polite-but-not-performed)
2. **Dry humor (Ch 3 coffee scene):** `"The kettle's broken. It's not broken enough to replace."` (expected: both sentences at the same pace, the second not lifted as punchline)
3. **Quiet gravity (Ch 11 3 AM):** `"I'm sorry I didn't find you sooner."` (expected: measured, no tremor, a fact being stated)
4. **The Reeves beat (Ch 11):** `"But I know one part of it. The people who love you are going to miss you."` (expected: slower than baseline, but not dramatically slower; the weight is in the words, not the delivery)

### 3.4 State Variations

Kenji's register doesn't change much. Two exceptions:

- **Ch 11 3 AM scene:** drop Stability to 50. The lines need to feel less rehearsed. Kenji is saying things he hasn't said aloud before.
- **Ch 12 switchboard duel:** raise Stability to 65. Kenji is running operations; crisp, decisive.

### 3.5 Pitfalls

- **Over-dramatization:** Kenji is the game's most restrained voice. If the library voice wants to lift or emphasize, switch voices. Do not compromise.
- **Age drift:** some library voices sound 45–50 rather than 38. Watch for it.

---

## 4. ENDO MASATO

**Line count estimate:** ~400 unique lines.

**This is the game's most difficult NPC voice to cast.** The voice must sound trustworthy to players who do not yet suspect Endo.

### 4.1 Voice Selection

**Approach:** Library voice OR clone from a specific reference actor.

**Reference:** 55-year-old male, warm-measured, conductor-like timing. The voice of a man who has been speaking to people in positions of authority for decades and calibrated himself to sound exactly like what they expect.

**Library candidates:** ElevenLabs voices tagged "senior male," "warm," "narrator," "authoritative but kind." Test aggressively — most library voices that advertise warmth lean toward grandfatherly or preacher, both of which break the character. Endo's warmth is specifically a competence voice, not a love voice.

**Clone option:** if library fails, clone from a reference actor who can land "the conductor." The voice actor should have experience with corporate narration or political speechwriting delivery — both traditions teach the relevant register.

### 4.2 Parameter Profile

- Stability: 70
- Similarity Boost: 85
- Style: 20
- Speaker Boost: ON

Very high Stability because Endo does not fluctuate. His control is the character. Similarity Boost high to prevent any drift that might leak vulnerability.

### 4.3 Sample Lines

1. **Warm-measured (Ch 8 opening):** `"Detective Tanaka? This is Masato Endo — I'm on the community safety council here in Yanagi. I hope I'm not interrupting."` (expected: warmth that sounds real, not performed; the pause before "here in Yanagi" measured to ~0.4 seconds)
2. **Institutional deflection:** `"The council takes every report seriously. We have a documented review process."` (expected: the plural "we" delivered as though it were natural; institutional framing as native speech)
3. **Pressed (Ch 8 tell):** `"I've spoken with Mira on several occasions. School events, community functions. I'm sure I'm recalling one of those interactions."` (expected: a half-beat delay before "I've spoken" — the retrieval tell — but otherwise smooth)
4. **Philosophical justification (Ch 11):** `"Do you know what the world does to children who keep speaking?"` (expected: genuinely troubled, not villainous; this is the line that must implicate the player in Endo's logic)

### 4.4 State Variations

- **Ch 8 first call:** full warmth. Stability 70.
- **Ch 9 follow-up:** subtle calibration shift. Stability 65. A trace of effort now visible to listeners paying attention.
- **Ch 11 confrontation Phase 2 (first unfilled silence):** Stability drops to 55 for the first paused line only. Elsewhere in Phase 2, back to 65.
- **Ch 11 Phase 5 (requesting counsel):** Stability 70 again. He has committed to a position.

### 4.5 The "Mira" Problem

Endo says Mira's name specifically. The manuscript notes that the pitch drops and the consonants soften — the intimacy of a man who has said this name in private, many times, to no one.

ElevenLabs may not produce this naturally. Approach:
1. Generate the line with standard parameters
2. If the name sounds flat or neutral, regenerate with a micro-lowered Stability (50) for that word specifically — split the take
3. Composite the softer "Mira" into the rest of the line

This detail lands Ch 8's unease. Do not skip it.

### 4.6 Pitfalls

- **Villain lean:** any hint of sinister register breaks the character. Ch 1–10 Endo must sound trustworthy. Reject takes that have any "off" quality.
- **Grandfatherly drift:** some library voices age the performance toward 65–70. Keep Endo at 55.
- **Measured rhythm:** the three-second rest is character. Use `. . .` punctuation in source text to enforce it. If the model compresses pauses, split takes and composite.

---

## 5. REIKO KITAHARA

**Line count estimate:** ~200 unique lines.

### 5.1 Voice Selection

**Approach:** Library voice.

**Reference:** 35-year-old female, shift-worker weariness, performing composure. The voice of a woman who has answered "how are you" for months without meaning it.

**Library candidates:** ElevenLabs tags "adult female," "calm," "warm-tired." Reiko's voice is controlled without being cold; she is performing composure for strangers.

### 5.2 Parameter Profile

- Stability: 55
- Similarity Boost: 75
- Style: 20
- Speaker Boost: ON

Medium Stability because Reiko modulates — her rehearsed register (Ch 3) is different from her cracked register (Ch 9) is different from the notebook scene (Ch 11).

### 5.3 Sample Lines

1. **Rehearsed (Ch 3):** `"Yes, of course. I've been expecting someone to follow up. How can I help?"` (expected: smooth, practiced, the right amount of polite distance)
2. **Cracked (Ch 9 static call):** `"I should have listened through the static."` (expected: not crying; just the arithmetic of a specific unbearable memory delivered as fact)
3. **Post-notebook scene (Ch 11):** `"She was doing mine."` (expected: three words, landed clean, the world's most devastating past tense)

### 5.4 State Variations

- **Ch 3:** Stability 60. The rehearsed register.
- **Ch 9 static call:** Stability 40. The control is slipping.
- **Ch 11 notebook scene:** Stability 45. She is saying things she has never said aloud.

### 5.5 Pitfalls

- **Melodrama:** Reiko does not cry in any call. Any take where she sounds weepy is wrong. Reject.
- **Motherly warmth:** she does not have warmth available for the detective. She performs politeness, not warmth. Watch for library voices that lean toward nurturing.

---

## 6. DOI

**Line count estimate:** ~200 unique lines.

### 6.1 Voice Selection

**Approach:** Library voice.

**Reference:** 65-year-old male, gruff baseline, capable of escalating courtesy under pressure. The voice of a lifelong shopkeeper.

**Library candidates:** ElevenLabs tags "senior male," "gruff," "weary." Doi's voice should carry physical age — not frail, but weathered.

### 6.2 Parameter Profile

- Stability: 55
- Similarity Boost: 75
- Style: 20
- Speaker Boost: ON

### 6.3 Sample Lines

1. **Gruff baseline (Ch 3):** `"Yanagi Mart."` (expected: two syllables, flat, the greeting of a man who has said this a thousand times)
2. **Courteous shutdown (Ch 3 PRESSURE response):** `"I appreciate you asking, Detective. What she observed was a man in his own store, near a window. I'm sorry I can't be more helpful than that."` (expected: the courtesy is polished; contrast with the baseline gruffness of Line 1)
3. **Collapse (Ch 6):** `"I didn't do it, Detective. I said I did because... I said I did because I couldn't keep being the man people thought I might be."` (expected: the em-dash pause is real; the second half quieter than the first)
4. **Streetlight curmudgeon (Ch 3):** `"You know what the old one was? A regular bulb. In a fixture."` (expected: dry, grumbling, mildly comedic without performing comedy)

### 6.4 State Variations

- **Ch 3 baseline:** gruff, Stability 55.
- **Ch 3 Dignity Filter activated (PRESSURE):** Stability 65 + Style 10. The courtesy is rigid.
- **Ch 6 confession collapse (SILENT):** Stability 40. The rigidity drops.
- **Epilogue:** baseline gruff, Stability 55. Unchanged.

### 6.5 Pitfalls

- **Excess gravel:** ElevenLabs senior-male voices often overproduce vocal fry. Doi is gruff but not damaged. Dial back if the voice sounds throat-cancer.
- **The shift to courtesy:** the PRESSURE-response politeness is the character's signature. It must sound REAL, not mocking. The voice must be able to deliver "I appreciate you asking" without irony.

---

## 7. HARUKI ISE

**Line count estimate:** ~400 unique lines.

### 7.1 Voice Selection

**Approach:** Library voice.

**Reference:** 29-year-old male, over-explainer, winded register. Think: a teacher who talks too fast because silence means he has to feel something.

**Library candidates:** ElevenLabs tags "young adult male," "energetic," "nervous." Haruki's voice carries rapid speech as default; his tell is when he STOPS.

### 7.2 Parameter Profile

- Stability: 40
- Similarity Boost: 75
- Style: 25
- Speaker Boost: ON

Lower Stability because Haruki's rhythm is variable by design.

### 7.3 Sample Lines

1. **Overflow (Ch 5):** `"My name is Haruki Ise. I'm — I was Mira's homeroom teacher. At Yanagi Elementary. Class 4-2."` (expected: fast, over-explaining, the em-dash pause brief)
2. **The tell (moment of stop):** ElevenLabs can't produce the tell natively. Generate the surrounding lines, leave a 2–3 second silence in the audio edit for the tell moment. The silence is the voice direction, not the voice.
3. **Post-break (Ch 9):** `"I named it. I gave it a name and they used the name."` (expected: slow, flat, anger under control; the opposite of the overflow register)
4. **Epilogue:** `"I file reports. I follow up."` (expected: calm, directed, the motion now purposeful)

### 7.4 State Variations

- **Ch 5–8 overflow:** Stability 40. Fast delivery.
- **Ch 9 break:** Stability 55. The rapid speech is gone; what replaces it is cold precision.
- **Ch 11+:** Stability 55 maintained. The post-break register holds.

### 7.5 The Tell

Haruki's signature audio tell — the 2–3 seconds where his pen clicking, chair squeaking, and papers shuffling all stop — is not produced by ElevenLabs. It's a foley/audio-editing beat. Generate Haruki's lines normally; insert the tell in post.

### 7.6 Pitfalls

- **Stuttering:** ElevenLabs sometimes generates unintended stutters on rapid dialogue. Check for unplanned repetition; re-generate if present.
- **Young-sounding drift:** some young-adult-male library voices skew toward 22. Keep Haruki at 29.

---

## 8. AIZAWA EMI

**Line count estimate:** ~150 unique lines.

### 8.1 Voice Selection

**Approach:** Library voice.

**Reference:** 40-year-old female, procedural, controlled. The voice of a vice principal who has been running school machinery for two decades.

**Library candidates:** ElevenLabs tags "adult female," "calm," "authoritative." Aizawa's voice is precise without being cold.

### 8.2 Parameter Profile

- Stability: 60
- Similarity Boost: 80
- Style: 10
- Speaker Boost: ON

High Stability because Aizawa's control is her character. Style very low — she does not perform.

### 8.3 Sample Lines

1. **Procedural (Ch 5):** `"Hello. This is Aizawa."` (expected: economical, no warmth, no coldness, pure function)
2. **Protective deflection:** `"I filed through the appropriate channels. The safety council reviewed each one."` (expected: smooth, bureaucratic; the deflection is procedural, not defensive)
3. **Break (Ch 8):** `"I chose the version of my job that let me sleep."` (expected: flat, confessional-but-controlled, no tears; delivered like a fact)

### 8.4 State Variations

- **Ch 5:** Stability 65. Full control.
- **Ch 8 break:** Stability 45. The control is cracking.
- **Ch 11:** Stability 60. She has accepted her role in the case.

### 8.5 The Sanitizer Click

Aizawa's audio signature (the click) is NOT produced by ElevenLabs. It is a foley element added in post — see `deadringer_audio_signatures.md` §3.6. Generate her voice independently; layer the click in audio production.

### 8.6 Pitfalls

- **Emotion emergence:** some library voices default to too much warmth. Aizawa's voice is specifically unwarm without being cold. Reject takes that sound caring.

---

## 9. FUMIKO ARAI

**Line count estimate:** ~250 unique lines.

### 9.1 Voice Selection

**Approach:** Library voice.

**Reference:** 45-year-old female, transactional-sharp, slight gravel (historical smoker). The voice of a journalist who has been right without being heard for fourteen years.

**Library candidates:** ElevenLabs tags "adult female," "confident," "mature." Look for voices with slight husk without overproduced vocal fry.

### 9.2 Parameter Profile

- Stability: 50
- Similarity Boost: 75
- Style: 25
- Speaker Boost: ON

Stability medium because Fumiko modulates more than most NPCs — her transactional default vs. her warmth-quota beat.

### 9.3 Sample Lines

1. **Transactional (Ch 6):** `"What do you know that I don't?"` (expected: flat, efficient, not hostile)
2. **Warmth-quota beat (Ch 6):** `"Okay. That's my warmth quota used. We can proceed to the part where I extract information from you."` (expected: dry humor, the punchline delivered as a fact)
3. **Philosophical (Ch 11):** `"He signed off on the room being sealed every year while using it three times a week."` (expected: cold precision, the twenty-word sentence landing as a closing statement)

### 9.4 State Variations

- **Ch 6 default:** transactional, Stability 55.
- **Ch 6 warmth-quota beat:** Stability 45, Style 30. The humor is direct and personal.
- **Ch 11–12:** Stability 55. She has earned the right to be certain.

### 9.5 Pitfalls

- **Affectation:** some library voices skew toward character-actress theatricality for "journalist." Fumiko is not theatrical. Reject.
- **Vocal fry:** moderate slight gravel is correct. Overproduced fry is wrong.

---

## 10. KAITO NISHIMURA

**Line count estimate:** ~100 unique lines.

### 10.1 Voice Selection

**Approach:** Library voice (upper age) OR professional clone.

**Reference:** 17-year-old male, delayed speech, autistic-coded. Delivered with cadence gaps — processing pauses built into the rhythm.

**Library candidates:** ElevenLabs tags "teen male" are often wrong (too performative-cartoon). Search "young adult male, monotone, thoughtful." If library fails, consider professional clone from a VO artist who can do the delayed-signal pattern.

### 10.2 Parameter Profile

- Stability: 65
- Similarity Boost: 80
- Style: 10
- Speaker Boost: ON

High Stability, very low Style. Kaito's delivery is uniform by design.

### 10.3 Sample Lines

1. **Baseline (Ch 7):** `"...yeah."` (expected: three-second ellipsis pause before the word; the delay is the character)
2. **Data delivery:** `"March 3rd. 2:45 PM. Silver sedan. Shinagawa plates. Parked on the east side of the school, near the gate. Engine running. Nobody got out. Departed 3:22 — seven minutes after dismissal."` (expected: even pace, information-dense, no emotional inflection)
3. **Teenager reveal (Ch 7 SILENCE hidden gate):** `"I am also writing a book. A novel. I have been writing it for three years. I have not finished a chapter."` (expected: each sentence complete, awkward-sincere, the admission delivered as data)

### 10.4 State Variations

Kaito does not modulate significantly. All lines use the baseline profile. The character's emotional range is in the LENGTH of his processing pauses, not vocal color.

### 10.5 Processing Pauses

Kaito's signature delayed-signal — the 3–9 second pauses before his responses — are not generated by ElevenLabs. They are editing-layer silences. Generate his lines normally. In audio production, insert the specified pause length before each line, based on the manuscript's guidance (e.g., "nine-second delay" before a heavy disclosure).

### 10.6 Pitfalls

- **Performative autism:** some voice actors and library voices over-code the delivery. Kaito is not a stereotype. Reject any take that feels like performance.
- **Youth drift:** some library voices skew toward 14–15. Keep Kaito at 17.

---

## 11. YUI SAKAMOTO

**Line count estimate:** ~80 unique lines.

### 11.1 Voice Selection

**Approach:** Professional Voice Clone.

**Source material requirement:** 15–20 minutes from a VO artist skilled at 10–12 child register with the specific "performed-normalcy" quality — the voice a child uses for adults who might check on her.

**Source actor qualities:**
- Able to deliver warmth that sounds real-but-constructed
- Able to deliver near-silence with fabric shifts (for the SILENCE path)
- Age 18–25 VO artist preferred; casting age 11 is difficult labor-law-wise and production-expensive

### 11.2 Parameter Profile

- Stability: 70 (Yui is performing — stable is correct)
- Similarity Boost: 85
- Style: 15
- Speaker Boost: ON

### 11.3 Sample Lines

1. **Performance (Ch 4 default):** `"Oh! Yes, that's me. How can I help you, sir?"` (expected: flawless, cheerful, calibrated to adult expectations)
2. **Gap before truth:** `"I usually go straight home."` (expected: the three-second gap before this line should be in the audio edit; the line itself is flat, rehearsed)
3. **Near-silent fragment (SILENCE path):** `"Um..."` (expected: small, uncertain, the performance cracking)

### 11.4 State Variations

- **Ch 4:** performed-normalcy, Stability 70.
- **Epilogue:** SHE DOES NOT SPEAK IN THE EPILOGUE. No voice required.

### 11.5 Pitfalls

- **Over-sweet:** library child voices are often saccharine. Yui is specifically NOT saccharine. She is competent at sounding fine. The difference is audible.
- **Abuse-drama voice:** do not direct the voice actor to sound traumatized. Yui's trauma is audible in the containment, not the performance.

---

## 12. RINA NISHIZAWA

**Line count estimate:** ~80 unique lines.

### 12.1 Voice Selection

**Approach:** Library voice OR professional clone.

**Reference:** 10-year-old female, cheerful social-center. The voice of a child who is popular because she is reliably pleasant.

### 12.2 Parameter Profile

- Stability: 55
- Similarity Boost: 75
- Style: 25
- Speaker Boost: ON

Higher Style because Rina's social fluency is performative — it should come across as an active performance.

### 12.3 Sample Lines

1. **Default (Ch 4):** `"Mira? Oh! Yes, I knew her. She was in the class above mine, actually — I mean, I'm a year older than she was — but we had the same homeroom because of the mixed-age classes."` (expected: bright, social, slight over-explanation of social position)
2. **The "intense" moment:** `"Mira just misunderstands things sometimes. She's really smart but she reads into things. Everyone who went to school with her kind of noticed that."` (expected: delivered warmly, casually; the player must understand that Rina is not being cruel — she is rehearsing community consensus)
3. **Epilogue:** `"We're having a bake sale on Saturday."` (expected: normal, unburdened; a child one year older who still does not fully understand her role)

### 12.4 Pitfalls

- **Villain voice:** Rina is never delivered as villain. Any take that sounds cruel is wrong. Her harm is the normality.
- **Age drift:** some library child voices skew younger (7–8) or older (13–14). Rina is specifically 10.

---

## 13. SORA HAYASHI

**Line count estimate:** ~30 unique lines (plus residue fragments in Ch 10).

### 13.1 Voice Selection

**Approach:** Professional Voice Clone OR Instant Voice Clone (budget-dependent).

**Reference:** 8-year-old male, quiet, observational. Speaks briefly and precisely.

**Source actor qualities:**
- Able to deliver matter-of-fact cataloging ("the pipe makes a sound when it gets cold")
- Able to deliver "brave for twenty more minutes" under Mira's instruction in Ch 12
- Small voice — Sora is young and physically small

### 13.2 Parameter Profile

- Stability: 70
- Similarity Boost: 80
- Style: 15
- Speaker Boost: ON

### 13.3 Sample Lines

1. **Exchange room residue (Ch 10):** `"small."` / `"the pipe makes a sound when it gets cold."` (expected: fragments, observational, matter-of-fact despite distress)
2. **Ch 12 recovery (very limited):** acknowledgment sounds, a quiet "okay" to Mira's instructions
3. **Epilogue essay (voiced-over?):** if voice is used for the essay, the delivery is careful, slightly formal, a child reading what he wrote

### 13.4 Special Case: Voiced Epilogue Essay

The Epilogue's key moment — Sora's essay mentioning Mira — may or may not be voiced. Per `deadringer_soul_read_voice_direction.md` §6.2 (Sora cast separately), if voiced, it should be Sora's voice, not Mira's. Whether to voice at all is a creative director decision.

Recommendation: generate a take of the essay in Sora's voice for evaluation. The final decision is creative, not technical.

### 13.5 Pitfalls

- **Crying child voice:** do not direct Sora as traumatized. He is observational. The horror is in his composure, same as Mira's.

---

## 14. EXCHANGE ROOM RESIDUE VOICES (Ch 10)

The "other children" in the exchange room — impressions of past voices absorbed into copper.

### 14.1 Voice Selection

**Approach:** 5–8 different library child voices.

**No clones required.** These are fragmentary voices with heavy post-processing.

### 14.2 Parameter Profile (shared)

- Stability: 50
- Similarity Boost: 60
- Style: 20
- Speaker Boost: OFF (allow some drift for variety)

Lower Similarity Boost because variety is the design — these should sound like different children.

### 14.3 Sample Content

Fragments only, no complete sentences. Approximately 20–30 fragments total, 2–5 seconds each:
- A girl asking for her mother (fragments: `"mom"` / `"please"` / `"I want..."`)
- Children reporting observations (fragments: `"they said..."` / `"I saw..."` / `"nobody believed..."`)
- Small affirmations (fragments: `"yes"` / `"no"` / `"okay"`)

All fragments go through heavy processing (see §14.4). Do not attempt to generate complete sentences for residue voices.

### 14.4 Post-Processing Chain

After ElevenLabs generation:
1. Low-pass filter at 2 kHz (remove high detail, simulate old wire)
2. Bit-crush to ~8-bit (add digital degradation)
3. Reverb with long decay (suggest a long-dead space)
4. Pitch variation per fragment (simulate different children)
5. Layer multiple fragments at varying amplitudes in the exchange room audio bed

The residue voices should be legible as voices but not as individuals. The sound designer owns the final mix; generation is the raw material.

---

## 15. PRODUCTION WORKFLOW

### 15.1 Session Structure

**Session 1 — Voice Selection (~4 hours):**
- Audition library voices for 7 library-voice characters (Kenji, Endo, Reiko, Doi, Haruki, Aizawa, Fumiko, Rina)
- Record clone source material for 3 clone characters (Mira, Yui, Sora) if using cloning
- Lock Voice IDs and save parameter profiles

**Session 2 — Mira Baseline (~6 hours):**
- Generate full Ch 1–3 Mira lines in Armored profile
- Verify degradation processing chain with engineer
- Produce Ch 10 amplified take library for comparison

**Sessions 3–5 — NPC Batch Generation (~4 hours each):**
- Per session: 2–3 characters full game text
- Review for consistency across chapters
- Mark lines for manual re-take or post-processing

**Session 6 — Mira Late-Game + Load-Bearing Lines (~8 hours):**
- Ch 8–12 Mira including degradation variants
- All 11 load-bearing lines with multiple takes
- Humming capture from source actor

**Session 7 — Residue Voices + Cleanup (~4 hours):**
- Exchange room residue voice fragments
- Re-takes from QA pass
- Final consistency verification

**Session 8 — Integration Review (~2 hours):**
- All generated audio in context with ambient beds
- Identify any remaining inconsistency issues

### 15.2 Take Selection Guidance

- **3 takes minimum per line** for dialogue-critical characters (Mira, Kenji, Endo, Reiko)
- **2 takes minimum** for other NPCs
- **5+ takes** for all 11 load-bearing Mira lines
- **Select for "least performed"** — the flat take is almost always correct for Dead Ringer

### 15.3 Iteration Budget

ElevenLabs generation is cheap per take (~cents per generation). Do not economize on takes.

Rough budget: 2,500 lines × 3 takes = 7,500 generations for final delivery. Plus iteration, QA, and re-takes: ~12,000 generations total across the full game's voice production.

### 15.4 Localization

ElevenLabs Multilingual v2 supports generating the same voice profile in 29 languages. For Dead Ringer's likely localization targets (Japanese, Simplified Chinese, Korean):

- Same voice clones, re-generated with translated scripts
- Verify per-language that the degradation processing still produces the intended effect (different languages have different phoneme distributions)
- Pay special attention to Mira's "can't vs won't" and Kenji's Reeves beat — these lines are English-specific in their phrasing; localization requires new voice direction, not just translation

### 15.5 Quality Control

Every generated voice asset must pass:
1. **Consistency check** — same character, same session, no drift
2. **Register check** — does the delivery match the specified profile?
3. **Emotion check** — is the take appropriately flat?
4. **Context check** — does the line work alongside the previous and next lines?
5. **Final mix check** — does the processed voice sit properly in the scene's audio bed?

Failed takes: regenerate immediately or flag for manual re-recording.

---

## 16. OPEN QUESTIONS

1. **Voice cloning contracts.** Voice-over artists providing clone source material should sign contracts specifying use scope, payment for unlimited generated lines, and moral rights. Get legal review before session 1.
2. **ElevenLabs subscription tier.** Production volume requires Enterprise or at minimum Scale tier. Budget accordingly.
3. **Mira's voice — real child vs. adult VO doing child?** Recommendation: adult VO with child-age capability. Child performers require strict labor-law compliance (California limits 4-hour sessions for minors, shorter for under-12); adult VOs can record the full degradation range in a single session. Verify with production that this trade-off is accepted.
4. **Accessibility layer voice.** Audio description requires its own narrator voice. Recommend: a neutral library voice, different from any character, stable parameters, low style. Separate voice ID, separate session.
5. **Director authority.** Who approves final takes? Recommend a single voice director with creative authority; otherwise the flat-delivery register will drift across sessions.

---

## 17. CROSS-REFERENCES

- `deadringer_soul_read_voice_direction.md` — detailed Mira voice coaching; this document's §2 is a condensed ElevenLabs-specific companion
- `deadringer_audio_signatures.md` §3 — per-NPC audio signatures, state variations, environmental beds
- `deadringer_characters.md` — character bibles
- `deadringer_asset_pipeline.md` §4 — production phase overview
- `deadringer_systems.md` §6 — Partner Degradation (spec Mira's processing chain)

---

**END ELEVENLABS VOICE BRIEFS**
