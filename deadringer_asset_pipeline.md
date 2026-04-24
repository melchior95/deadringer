# DEAD RINGER — Generative Asset Production Pipeline

Plan of record for producing game assets using generative AI tooling. Orders deliverables by dependency and priority; flags what blocks what; maps each asset bucket to the right tool.

**Tools in use:**
- **Images:** Midjourney, Stable Diffusion (SDXL / Flux), Gemini (Imagen / 2.5 Pro image gen)
- **Animation:** Runway Gen-3, Kling, Luma (for cutscenes with motion)
- **Voices:** ElevenLabs (all character voice performances)
- **Audio / SFX / music beds:** ElevenLabs Sound Effects, Suno (music cues only — game is mostly ambient/diegetic)
- **Compositing / post:** conventional tools (Photoshop, After Effects, DaVinci)

**Companion docs:**
- `character_image_prompts.md` — 99 character audition prompts (11 × 3 styles × 3 platforms)
- `deadringer_locations.md` — location specs with tiers and time-of-day states
- `deadringer_audio_signatures.md` — per-NPC + per-location audio specs
- `deadringer_soul_read_voice_direction.md` — Mira voice coaching
- `deadringer_memory_fragments_production.md` — Memory Fragment scene specs
- `deadringer_notebook_system.md` — UI architecture for the notebook

---

## 1. PIPELINE OVERVIEW

The production is organized into five phases. Phases 1–2 are image/asset heavy; Phase 3 is voice-heavy; Phases 4–5 are integration and polish.

```
PHASE 1: Style Audition          ←  You are here
  ├── Character portraits (DONE — 99 prompts ready)
  └── Hero location backgrounds (IN PROGRESS — this doc initiates Tier 1)

PHASE 2: Full Asset Production   ←  Unblocked once style is locked
  ├── Remaining locations (Tier 2, Tier 3)
  ├── Character emotion/state variants
  ├── UI art
  └── Cutscene key-frames

PHASE 3: Voice Production        ←  Runs in parallel with Phase 2
  ├── Mira voice (all chapters, degradation-aware)
  ├── All 9 NPCs
  └── Ambient/residue voices (exchange room children)

PHASE 4: Animation / Motion      ←  Gated on Phase 2 key-frames
  ├── Cutscene animations (Runway/Kling)
  └── Environmental motion loops

PHASE 5: Audio & Integration     ←  Runs in parallel with Phase 4
  ├── SFX library (ElevenLabs)
  ├── Music cues (limited — Suno for Ch 12 + epilogue only)
  ├── Wire-sound custom (NOT AI — sound designer)
  └── Final integration (all assets → engine)
```

### 1.1 Why Hero Locations Now

Style audition with characters alone is insufficient. A style can work for portraits and fail on environments — the Steins;Gate painterly register that suits Mira's half-body may collapse on the Exchange Room's low-lit technical interior. Auditioning three hero locations alongside the character prompts gives a complete evaluation: does the style carry characters AND environments AND the game's most demanding set piece?

The three Tier 1 hero locations:
1. **Kenji's Apartment** — the game's home screen; recurs every chapter; must work across night / morning / afternoon states
2. **The Exchange Room** — the game's single most important set piece; Ch 10 pivot; must convey layered residue and physical menace
3. **Endo's Garden** — Ch 9 set piece; the game's most photogenic image; must land as beautiful-and-wrong

If the chosen style fails on any of these three, it is not the right style for Dead Ringer.

### 1.2 Style Audition Evaluation Criteria

When reviewing Phase 1 outputs, judge against:

| Criterion | Question |
|---|---|
| **Reads at thumbnail** | Can the character / location be identified at icon size? |
| **Reads at resolution** | Does the detail reward inspection? |
| **Tonal consistency** | Do character and location share visual language? |
| **Emotional register** | Does the style carry dread, warmth, dryness where needed? |
| **Asset productivity** | How many variations do we need? Does the style produce consistent sets? |
| **Cost at scale** | Can we produce 100+ images in this style without style drift? |

Midjourney tends to win on the first four. Stable Diffusion wins on 5–6 (reproducibility via fixed seeds). Gemini wins on rapid iteration during audition. The final pipeline likely uses Midjourney for hero assets + SD/Flux with LoRAs for variations.

---

## 2. PHASE 1 — STYLE AUDITION

### 2.1 Character Portraits

**Status:** COMPLETE. See `character_image_prompts.md`.

**Coverage:** 11 characters × 3 styles × 3 platforms = 99 prompts.

**Characters covered:** Mira, Kenji, Endo, Reiko, Yui, Sora, Doi, Haruki, Aizawa, Fumiko, Rina, Kaito.

**Audition process (recommended):**
1. Generate all 99 prompts. ~30 minutes of tool time across three platforms.
2. Lay out as a 3×3×11 grid (style × platform × character).
3. Identify the style where the greatest number of characters read correctly.
4. Re-generate top candidates with seed variations in the winning style.
5. Lock style + platform.

### 2.2 Hero Location Backgrounds

**Status:** THIS DOCUMENT initiates. See `deadringer_hero_location_prompts.md` (forthcoming in this session).

**Coverage:** 3 locations × 3 styles × 3 platforms = 27 prompts.

**Locations covered:**
1. Kenji's Apartment (default night state — Ch 1 cold open lighting)
2. Community Center Exchange Room (Ch 10 primary state)
3. Endo's Garden (Ch 9 morning state)

**Audition process:** same as characters — lay out the 27 in a 3×3×3 grid, evaluate against the Character Portrait grid together, lock style + platform for everything.

---

## 3. PHASE 2 — FULL ASSET PRODUCTION (after style lock)

### 3.1 Remaining Location Backgrounds

Once style is locked, produce prompts for:
- 11 Tier 2 locations (recurring) — each with their state variations per `deadringer_locations.md`
- 7 Tier 3 locations (single-use) — one state each
- Total: ~45 unique location images (counting state variants)

### 3.2 Character Emotion / State Variants

Per-character state sheet needed for dialogue UI. Minimum states per NPC:

| NPC | Required States |
|---|---|
| Mira | baseline / armored / leaking / unarmored / amplified (Ch 10) / crashed (Ch 11) / humming (Ch 11) / final call (Ch 12) |
| Kenji | baseline / attentive / weary / surprised / angry / sitting-on-floor (Ch 11 3 AM) |
| Reiko | rehearsed / cracked (static call) / reading notebook (Ch 11) |
| Yui | performing / near-silent / reading in garden (Epilogue) |
| Doi | gruff / courteous-shutdown / collapsed (Ch 6) / at counter (Epilogue) |
| Haruki | overflow-active / overflow-stopped (the tell) / post-break focused |
| Aizawa | procedural / sanitizer-click-accelerated / post-break |
| Fumiko | transactional / sharp / pen-lifted (warmth) |
| Kaito | delayed-signal / teenager-revealing / post-rescue |
| Endo | helpful / paused (Ch 11 Phase 2) / arrest |
| Rina | social-center / epilogue (older, aware) |

**Estimate:** ~40 unique character state images across all 11 NPCs. Plus Sora in 3 states (unrecognized / held / post-rescue).

### 3.3 UI Art Prompts

Separate document after style lock. Covers:
- Notebook (pocket-notebook visual, blue notebook inside, paper texture evolution across chapters)
- Call screen (caller ID strip, intent selector, ambient waveform, compact notebook icon)
- Confrontation Board (Ch 11 eight-slot layout with emerging/complete/presented states)
- Memory Fragment text overlays ("This is a memory. You are Mira.")
- Chapter title cards

### 3.4 Cutscene Key-Frames

~15–20 critical cutscenes need key-frames (still imagery for pre-animation reference and non-animated cutscenes). Full list:

| Cutscene | Chapter | Key-frame description |
|---|---|---|
| Cold open | Ch 1 | Kenji's apartment desk, lamp, phone, dead phones drawer |
| First call | Ch 1 | The ringing phone at 3:47 |
| Yanagi arrival | Ch 2 | Station exit, train leaving |
| The Bench | Ch 2 | Colored pencil marks on slats |
| The Bridge | Ch 2 | Scratched number in concrete |
| Reiko Denial | Ch 3 | Mira-POV kitchen, Reiko at table |
| Yui's Apartment | Ch 4 | Audio-only, no key-frame needed |
| Crying Scene | Ch 4 or Ch 5 | The emotional center; abstract or character-focused |
| Rina Social Distortion | Ch 4 | Mira-POV classroom, notebook on Rina's desk |
| Aizawa Procedure | Ch 5 | Mira-POV counselor's office, drawer of identical forms |
| The Garden | Ch 9 | Wide shot, two newest plantings |
| Exchange Room entry | Ch 10 | First-view into the room |
| Mira amplified | Ch 10 | Handset raised, Mira's voice clearing |
| Notebook scene | Ch 11 | Reiko opens the blue notebook |
| 3 AM scene | Ch 11 | Kenji on the floor against the desk |
| The Arrest | Ch 12 | Handcuffs, car door, the garden in frame |
| Final call to Sora | Ch 12 | Split: Mira on the line / Sora receiving |
| Epilogue — Sora's classroom | Epi | The map on the wall, the essay on the desk |
| Epilogue — Yui's garden | Epi | Yui reading |
| Epilogue — Kenji's drawer | Epi | The six dead phones, Mira's now the sixth |

### 3.5 Memory Fragment First-Person Art

The three fragments are first-person POV. Requires:
- Kitchen scene from Mira's 130cm height (Reiko Denial)
- Classroom scene from Mira's 130cm height (Rina)
- Counselor's office from Mira's 130cm height (Aizawa)

Each needs several sub-shots for interactive-examine moments (the fridge magnets, Rina's desk, the drawer of forms).

---

## 4. PHASE 3 — VOICE PRODUCTION (ElevenLabs)

Runs in parallel with Phase 2. No dependencies on visual style lock.

### 4.1 Mira (Primary)

**Budget:** highest line count in the game. Roughly 1,500–2,000 lines.

**Voice model:** a child voice (age 9) with warmth, deadpan capability, and emotional range. ElevenLabs voices typically require fine-tuning for child registers — may need voice cloning from a young voice-over artist sample.

**Process:**
1. Select baseline voice (audition 3–5 candidates)
2. Establish Ch 1–3 baseline take
3. Apply degradation processing chain (see `deadringer_audio_signatures.md` §5.2) to baseline takes
4. Record/generate specific load-bearing lines separately (11 lines identified in `deadringer_soul_read_voice_direction.md` §3)

**ElevenLabs-specific considerations:**
- Use "Emotion" slider sparingly. Mira's deadpan requires low emotion; ElevenLabs defaults over-animate.
- Generate at 44.1kHz or higher for post-processing headroom.
- Save voice profile ID for consistency across chapters.
- For Ch 10 amplified vs Ch 11 crash: same voice profile, different post-processing. Do not use different voice profiles.

### 4.2 NPC Voices

One voice per character × ~100–500 lines each (depending on character).

| Character | Voice profile |
|---|---|
| Kenji | 38-year-old male, tired-steady, dry. Reference: world-weary detective archetype, minimal inflection |
| Endo | 55-year-old male, warm-measured, conductor-like timing. The voice must sound trustworthy. |
| Reiko | 35-year-old female, shift-worker weariness, performing composure |
| Doi | 65-year-old male, gruff baseline, capable of courteous shutdown (escalating politeness) |
| Haruki | 29-year-old male, over-explainer, winded/over-caffeinated register |
| Aizawa | 40-year-old female, procedural, controlled. Sanitizer click is separate SFX, not voice |
| Fumiko | 45-year-old female, transactional-sharp, post-smoking gravel |
| Kaito | 17-year-old male, delayed-signal, processing pauses built into cadence |
| Yui | 11-year-old female, performed-normalcy voice + contained breath |
| Rina | 10-year-old female, cheerful-social-center |
| Sora | 8-year-old male, quiet, observational, brief |

### 4.3 Voice Brief Document

Separate deliverable: `deadringer_elevenlabs_voice_briefs.md` — per-character ElevenLabs-ready directions including voice profile parameters, reference tones, sample line deliveries, degradation specs where applicable.

### 4.4 Exchange Room Residue Voices

Ch 10's "other children" residue — impressions of past voices absorbed into copper. Production approach:
- Use 5–8 different ElevenLabs child voices
- Heavy processing (low-pass filter, reverb, bit-crush)
- Fragments only, no complete sentences
- Layered in the exchange room audio bed

---

## 5. PHASE 4 — ANIMATION (Runway / Kling / Luma)

Gated on Phase 2 key-frames.

### 5.1 Cutscenes Requiring Animation

Not every cutscene needs motion. Many are stills with camera pan (static background + subtle zoom). Genuine animation is reserved for:

| Cutscene | Motion type |
|---|---|
| Ringing phone at 3:47 (Ch 1) | Static with camera push-in; phone ring animation minimal |
| Yanagi station arrival (Ch 2) | Train departure, Kenji emerging — short motion loop |
| Mira amplified — handset raised (Ch 10) | Static with atmospheric motion (dust particles, subtle lighting shift) |
| Final call to Sora (Ch 12) | Split-screen; minimal motion, emotional beat carried by audio |
| Sora recovered (Ch 12) | Cinematic; warrants full animation |
| Endo's arrest (Ch 12) | Cinematic; car door, garden pan |
| Epilogue character vignettes | Mostly stills; occasional subtle animation (Yui turning a page) |

**Estimate:** 6–10 shots requiring genuine animation. Remainder are stills with camera moves implemented in-engine or in compositing.

### 5.2 Animation Tool Choice

**Runway Gen-3 Alpha:** highest quality, best for painterly styles. Slower, more expensive.
**Kling:** faster, strong for cinematic realism. Less painterly.
**Luma:** good for dreamy/atmospheric; weaker on character consistency.

Recommendation: Runway for character animation, Kling for environmental / cinematic shots.

### 5.3 Consistency Problem

AI-generated video has historically struggled with character consistency across shots. Mitigation:
- Lock visual style in Phase 1 with exhaustive character references
- Use Runway's character-reference feature (if available) or similar for each shot
- Where consistency fails, fall back to stills with compositional motion rather than character animation

---

## 6. PHASE 5 — AUDIO PRODUCTION

Runs in parallel with Phase 4.

### 6.1 Ambient Beds per Location

Per `deadringer_audio_signatures.md` §4. ~30 location beds, each 2–5 minutes loopable. ElevenLabs Sound Effects can generate many; others may need field recording or royalty-free libraries curated by a sound designer.

### 6.2 Per-NPC Audio Tics

Sanitizer click (Aizawa), pen click (Haruki), pencil tap (Kaito), etc. ElevenLabs SFX or foley. Each needs rate variations (see audio signature spec §3).

### 6.3 The Wire-Sound

**CRITICAL: NOT GENERATIVE.** The wire-sound is the game's central audio motif and should be custom-designed by a human sound designer. Generative audio does not yet produce the precision this specific sound requires (the frequency coupling to Mira's voice, the 12-chapter evolution, the transition behaviors). 

Reserve budget for a dedicated sound designer on this one asset. Everything else can be AI-assisted.

### 6.4 Music Cues

The game is mostly unscored. Exceptions:
- Ch 12 switchboard duel — ambient tension, not a melodic theme
- Ch 12 final call to Sora — emotional underscore, subtle
- Epilogue — Kenji's scene may warrant the single melodic moment of the game
- Title screen / main menu — establishing theme

**Estimate:** 4–6 music cues total. Suno can draft; a human composer should polish the final versions.

---

## 7. BUDGET ESTIMATES

Rough tokens per phase for planning purposes. Not authoritative; depends on iteration count.

| Phase | Deliverable | Est. generations |
|---|---|---|
| 1 | Character portraits | 99 × 5 iterations = ~500 |
| 1 | Hero locations | 27 × 8 iterations = ~216 |
| 2 | Remaining locations | ~45 × 5 iterations = ~225 |
| 2 | Character state variants | ~40 × 3 iterations = ~120 |
| 2 | UI art | ~15 × 5 iterations = ~75 |
| 2 | Cutscene key-frames | ~20 × 5 iterations = ~100 |
| 3 | Voice generation | ~2,500 lines × 2 takes = ~5,000 |
| 4 | Animation | ~10 shots × 3 iterations = ~30 |
| 5 | SFX library | ~100 × 3 iterations = ~300 |

**Image generation total:** ~1,236 generations
**Voice generation total:** ~5,000 takes
**Video generation:** ~30 clips (expensive per-unit)

---

## 8. QUALITY CONTROL CHECKPOINTS

Before moving between phases, verify:

**Phase 1 → Phase 2 gate:**
- Style locked in. Document specifies which style / which platform / which specific model version.
- Character reference sheets prepared (for LoRA training or character-reference features).
- All hero locations pass the six evaluation criteria (§1.2).

**Phase 2 → Phase 3 gate (parallel track, not blocking):**
- No blocking dependency. Voice production can begin as soon as voice briefs are ready.

**Phase 2 → Phase 4 gate:**
- All key-frames approved.
- Character consistency verified across scenes (same character in two different scenes should look like the same character).

**Phase 4 → Phase 5 gate:**
- Animation-test sequences assembled.
- Audio placeholders in place for timing check.

---

## 9. OPEN QUESTIONS

1. **Style commitment.** Who decides which of the three styles is locked? Single creative director, or playtester consensus? Recommend: single decision-maker with authority to commit.
2. **Character consistency enforcement.** Will we train LoRAs on locked character designs, or rely on prompt discipline + reference images? Recommend: LoRA training for the top 3 most-appearing characters (Mira, Kenji, Endo); prompt discipline for others.
3. **Voice acting budget.** ElevenLabs subscription tier determines generation volume. Budget for a tier that supports 5,000+ takes without throttling.
4. **Animation budget.** Runway Gen-3 credits are significant. Recommend: budget ~500 credits for Dead Ringer; more if cutscene count expands in production.
5. **Human specialists.** Which roles are NOT generative-AI-replaceable?
   - Sound designer (for wire-sound + final mix)
   - Creative director (style lock, emotional judgment)
   - Playtest coordinator
   - Voice director (for ElevenLabs iteration guidance)
   - Possibly composer for final music polish
6. **Localization.** All generative work is English-first. Japanese, Chinese, Korean localizations require either: (a) localized voice generation (ElevenLabs supports multilingual), (b) localized text + subtitle production (conventional), (c) locale-specific imagery review (mostly unnecessary for a game set in Japan with international art style).

---

## 10. CROSS-REFERENCES

- `character_image_prompts.md` — Phase 1 character audition prompts
- `deadringer_hero_location_prompts.md` — Phase 1 hero location prompts (next deliverable)
- `deadringer_locations.md` — location specs
- `deadringer_audio_signatures.md` — audio production targets
- `deadringer_soul_read_voice_direction.md` — Mira voice direction
- `deadringer_memory_fragments_production.md` — Memory Fragment first-person art
- `deadringer_notebook_system.md` — UI art dependencies

---

**END ASSET PRODUCTION PIPELINE**
