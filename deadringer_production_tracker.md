# DEAD RINGER — Production Tracker

Living master document for tracking outstanding work, blockers, and asset status across the project. Updated as work progresses. This doc answers one question: **what is still to do, and what is blocking it?**

**Companion to:** all 21 spec documents in the project root.
**Update cadence:** after every production session / milestone.

---

## STATUS LEGEND

- **[DONE]** — work complete, merged, verified
- **[IN PROGRESS]** — actively being worked; assignee if applicable
- **[READY]** — unblocked, spec complete, ready to start
- **[BLOCKED]** — spec complete but waiting on upstream dependency
- **[HUMAN]** — requires a human specialist (not AI-producible); role named
- **[DECIDE]** — awaiting a creative decision before it can proceed

---

## 1. IMMEDIATE ACTION ITEMS

Ranked by priority. The top of this list is what to do next.

| # | Action | Status | Blocker / Note |
|---|---|---|---|
| 1 | Generate 99 character portrait prompts across 3 platforms | [READY] | Prompts exist in `character_image_prompts.md`. Ready to run. |
| 2 | Generate 27 hero location prompts across 3 platforms | [READY] | Prompts exist in `deadringer_hero_location_prompts.md`. Ready to run. |
| 3 | Style lock decision (characters + hero locations reviewed together) | [DECIDE] | Requires creative director review of output from #1 and #2. Blocks ~80% of remaining art production. |
| 4 | Local TTS environment setup on RTX 5080 (F5-TTS + GPT-SoVITS) | [READY] | See `deadringer_elevenlabs_voice_briefs.md` §17. ~1 day install + test. Unlocks NPC voice production. |
| 5 | ElevenLabs Pro tier subscription for Mira A/B testing | [READY] | $99/month for 1 month. Scope: load-bearing Mira lines only. |
| 6 | Voice actor casting for Mira / Yui / Sora clone sources | [READY] | Same actors needed regardless of local vs cloud. Contract / recording sessions. |
| 7 | Commission sound designer for wire-sound | [HUMAN] | Sound Designer. Cannot start until role is filled. Blocks Phase 5. |
| 8 | Manuscript fix: split Ch 9 Garden prompt (audit flagged) | [DECIDE] | Audit flagged as ambiguous; deferred in current pass. Creative director call. |
| 9 | Full style audition of Ch 9 Path A/B/C/D/E/F prompt structure | [BLOCKED] | Blocked on style lock (#3). |
| 10 | Produce Phase 2 remaining 19 locations in locked style | [BLOCKED] | Blocked on style lock (#3). |
| 11 | Produce ~40 character state/emotion variants | [BLOCKED] | Blocked on style lock (#3) AND character reference lock. |
| 12 | Produce cutscene key-frames (20 scenes) | [BLOCKED] | Blocked on style lock (#3). |
| 13 | Produce Memory Fragment first-person art | [BLOCKED] | Blocked on style lock (#3). |
| 14 | Tooling development — manuscript parser + batch generation scripts for local TTS | [READY] | Python engineering, ~8–12 days. Prerequisite to batch voice production. |
| 15 | Non-voice audio production brief (SFX / ambient / music) | [READY] | Not yet specced. Fourth parallel track. |
| 16 | Build playable prototype from existing manuscript + assets | [BLOCKED] | Engine choice, team assembly — outside current scope. |

---

## 2. BLOCKED ITEMS (By Blocker)

### 2.1 Blocked on Style Lock (#3)

Once the art style is locked, the following become unblocked in sequence:

- Phase 2 locations (19 more)
- Phase 2 character state variants (~40)
- Phase 2 UI art in locked style (18 individual deliverables from UI prompt doc)
- Phase 2 cutscene key-frames (20 scenes)
- Memory Fragment art (3 scenes × multiple sub-shots)
- Phase 4 animation (gated further on key-frame completion)

**Estimated size of dependency:** ~80% of all remaining art production.

**Decision inputs needed for style lock:**
- 99 character portraits generated
- 27 hero location backgrounds generated
- Review against 6 evaluation criteria (`deadringer_asset_pipeline.md` §1.2)
- Cost-at-scale test with top 2 candidates

### 2.2 Blocked on Voice Actor Casting

- Mira clone source material (30 min audio)
- Yui clone source material (15–20 min audio)
- Sora clone source material (15 min audio)

These block Phase 3 voice production for the three child characters. NPC adult voices (F5-TTS with library reference audio) can proceed in parallel without this blocker — unblocked as soon as local TTS environment is set up.

### 2.3 Blocked on Local TTS Tooling

- Batch voice generation across 2,500 lines
- Take management and selection UI
- Consistency audit across generations
- Degradation chain preview integration

These block bulk voice production until the tooling scripts are built (~8–12 engineering days). Single-line generation via the gradio UI for testing can proceed immediately after install.

### 2.3 Blocked on Engine / Build Team

- Prototype implementation
- UI state-machine wiring (notebook Log ↔ Board transitions)
- Audio integration (degradation chain, environmental beds, voice mixing)
- Playtest feedback loop
- Localization pipeline

These require a game engine choice, programming team, and build infrastructure — all outside the current documentation scope.

---

## 3. HUMAN SPECIALISTS REQUIRED

Generative AI cannot produce these; human specialists required.

| Role | What they do | Priority | Notes |
|---|---|---|---|
| **Sound Designer** | The wire-sound (central audio motif, 12 chapter evolution states). Final audio mix. Non-voice SFX polish. | Critical — blocks the game's central audio identity | See `deadringer_audio_signatures.md` §2 for spec |
| **Creative Director** | Style lock decision. Voice casting approval. Emotional-judgment moments where AI output is ambiguous. | Required throughout | One person with authority; not consensus-based |
| **Voice Director** | ElevenLabs iteration guidance, take selection, consistency enforcement across 12 chapters | Required during Phase 3 voice production | Can be same person as Creative Director if scope allows |
| **Composer (optional)** | 4–6 music cues (Ch 12 + Epilogue). Game is mostly unscored; Suno can draft, human polishes. | Low — can be last-phase | Only if music is included at all |
| **Voice-over artists** | Mira, Yui, Sora clone sources (30 min / 15 min / 15 min samples) | Required for Phase 3 child voice production | Consider labor contracts that cover unlimited AI-generated derivatives |
| **Playtest Coordinator** | Run playtests on prototype, synthesize feedback | Required Phase 5 onward | Post-prototype role |
| **Localization Reviewers** | Per-target-language review of generated voice + text | Required if shipping localized versions | Languages: JP, CN-S, KR likely; EN-US source |
| **Accessibility Reviewer** | AD script, high-contrast mode validation, screen-reader testing | Required pre-launch | Critical for a game whose audio is load-bearing |
| **Legal (contract review)** | Voice cloning contracts, AI tool usage rights, localization rights | Required before voice clone sessions | Before Phase 3 begins |

---

## 4. RISK REGISTER

Issues that could derail the project. Ordered by severity.

### 4.1 Critical Risks

| Risk | Impact | Mitigation |
|---|---|---|
| **Mira's voice doesn't land** | Game-breaking. Mira is the emotional core; her voice is load-bearing for 85% of emotional weight. | Professional voice clone from an experienced VO artist. A/B test local GPT-SoVITS against ElevenLabs on 11 load-bearing scenes. Keep whichever wins per line. Reserve budget for 5+ audition candidates. |
| **Art style fails on the Exchange Room** | Ch 10 is the game's second-most important set piece. A style that can't render the room's layered complexity (concrete, low fluorescent, handset, worn chair, cable routes) fails the project. | Hero location audition includes Exchange Room in all 3 styles. If all 3 fail, the style pool expands before lock. |
| **AI animation character consistency fails** | Cutscenes like the arrest and Sora rescued depend on Endo's and Kenji's faces being the same across shots. Runway Gen-3 can fail on consistency. | Lock character reference with LoRA training or platform character-reference features. Fall back to stills with compositional motion for scenes where consistency fails. |
| **Sound designer can't deliver the wire-sound** | The wire-sound is the game's audio identity. Generic stock audio will not suffice. | Budget a dedicated sound designer for this one asset. Don't AI-generate the wire-sound. |
| **Local TTS quality gap on load-bearing Mira lines** | If local GPT-SoVITS can't match ElevenLabs on Mira's 11 key scenes, the game's emotional peaks underperform. | Maintain ElevenLabs Pro ($99/month) as A/B resource. Run blind-ranked quality gate (§17.10 of voice briefs) before committing all-local. |

### 4.2 High Risks

| Risk | Impact | Mitigation |
|---|---|---|
| **Endo's voice reads as villain early** | Ch 1–10 Endo must sound trustworthy. Miscast undermines the late-game reveal. | Extensive audition. Reject takes with any "off" quality. Consider professional clone over library voice if library fails. |
| **Memory Fragment interactivity frustrates players** | Fixed-outcome design risks reading as "game doesn't respond to my choices." | Playtest specifically for the Fragment registration as meaningful. Use the three branches to texture the dismissal, not change it. |
| **Notebook UI becomes a database** | Loss of diegetic commitment undermines the game's register. | Review every UI iteration against "detective's pocket notebook" rule. Reject material-design drift. |
| **Ch 11 Board doesn't feel like ammunition** | Confrontation reads as a gallery rather than an active mechanic. | Board slot completion signaling must be unambiguous. Thoroughness cost must be felt. |

### 4.3 Medium Risks

| Risk | Impact | Mitigation |
|---|---|---|
| **Rushed playthroughs lack Ch 11 slots** | Board audit projected minimum 2 complete slots for rushed players. After manuscript fixes (auto-log promotions), minimum is 3–4. | Playtest rushed playthrough; ensure confrontation is still readable at minimum density. |
| **Voice cloning contracts legally inadequate** | Downstream production blocked or redo-needed. | Engage legal before voice actor sessions. Contracts must cover both local and cloud inference use of clone source. |
| **Fish Speech commercial license not secured** | Kaito's voice (if assigned to Fish Speech) requires regeneration via F5-TTS before commercial ship. | Decide Kaito tool assignment before production starts. Default to F5-TTS if license status unclear. |
| **Localization breaks degradation chain** | Mira's processing chain is English-language-tuned. Different phoneme distributions may not degrade the same way. | Per-language audio engineering review. GPT-SoVITS handles multilingual cloning natively; the degradation chain needs per-language tuning. Budget for localization adjustments. |
| **Local TTS model deprecation during production** | If a model is updated mid-project, regenerated takes may not match earlier ones. | Pin model versions at project start. Do not auto-update. |
| **Music decision unresolved** | Some players will expect music; its absence is a design choice that requires defense. | Commit to position before launch. Draft 4–6 possible cues in Suno; creative director decides if any are included. |
| **5080 Blackwell driver / CUDA compatibility issues** | Local TTS setup fails on new hardware. | Verify CUDA 12.4+ on 5080 before voice production begins. Fallback: cloud ElevenLabs at higher cost. |

---

## 5. FULL ASSET INVENTORY

### 5.1 Documentation (21 files)

| File | Status | Purpose |
|---|---|---|
| `deadringer_game_bible.md` | [DONE] | Thesis, core mechanics, design philosophy |
| `chapter_structure.md` | [DONE] | Information economy, NPC availability, chapter map |
| `deadringer_characters.md` | [DONE] | Character bible — 11 NPCs |
| `ogawa-incident.md` | [DONE] | Ogawa thread layered reveal design |
| `preface.md` | [DONE] | Manuscript-level structural conventions |
| `deadringer_systems.md` | [DONE] | Call / intent / soul read / memory / slot / degradation / contradiction / meta systems |
| `deadringer_notebook_system.md` | [DONE] | Hero UI architecture — two-layer notebook + Board |
| `deadringer_intent_matrix.md` | [DONE] | Per-call tuning: intents × NPCs × chapters with outcomes |
| `deadringer_locations.md` | [DONE] | 22 locations with tiers, states, art direction |
| `deadringer_audio_signatures.md` | [DONE] | Audio design spec — per-NPC / per-location signatures + wire-sound + voice chain |
| `deadringer_soul_read_voice_direction.md` | [DONE] | Mira voice coaching — 12-chapter degradation curve + 11 load-bearing scenes |
| `deadringer_memory_fragments_production.md` | [DONE] | Production spec for 3 interactive scenes |
| `epilogue_production.md` | [DONE] | 11 resolution scenes + title screen, per-scene production spec |
| `deadringer_board_slot_audit.md` | [DONE] | All 70 notebook prompts tagged to 8 Board slots, reachability by playthrough |
| `deadringer_asset_pipeline.md` | [DONE] | 5-phase generative asset production plan |
| `character_image_prompts.md` | [DONE] | 99 character audition prompts (11 × 3 styles × 3 platforms) |
| `deadringer_hero_location_prompts.md` | [DONE] | 27 hero location audition prompts (3 × 3 styles × 3 platforms) |
| `deadringer_ui_art_prompts.md` | [DONE] | UI audition prompts — notebook / call screen / Board + supporting |
| `deadringer_elevenlabs_voice_briefs.md` | [DONE] | Per-character ElevenLabs production briefs |
| `deadringer_cutscene_structure.md` | [DONE] | 23 cutscenes with format / tier / specs |
| `deadringer_production_tracker.md` | [IN PROGRESS] | This document |

### 5.2 Manuscript

| File | Status | Lines | Notes |
|---|---|---|---|
| `chapter_01.md` through `chapter_12.md` | [DONE] | ~8,500 | 12 chapters, all editorial passes complete |
| `epilogue.md` | [DONE] | ~200 | Core text; production spec separate |
| `preface.md` | [DONE] | 70 | Structural note |
| `dead_ringer_complete.md` | [DONE] | ~8,680 | Compiled manuscript (preface + 12 + epilogue) |
| `compile_manuscript.py` | [DONE] | — | Compilation script |

### 5.3 Art Assets — Characters

| Asset class | Count | Status | Blocker |
|---|---|---|---|
| Character portraits (11 chars × 3 styles × 3 platforms = 99) | 99 prompts | [READY] | None |
| Character portrait generation | 0 of 99 | [READY] | Needs tool access |
| Style lock (character half) | — | [DECIDE] | Needs #3 |
| Character emotion/state variants (~40) | 0 prompts | [BLOCKED] | Style lock |
| Character LoRA training (Mira / Kenji / Endo) | 0 | [BLOCKED] | Style lock + reference sheets |

### 5.4 Art Assets — Locations

| Asset class | Count | Status | Blocker |
|---|---|---|---|
| Hero location prompts (3 × 3 × 3 = 27) | 27 prompts | [READY] | None |
| Hero location generation | 0 of 27 | [READY] | Needs tool access |
| Style lock (location half) | — | [DECIDE] | Needs #3 |
| Tier 2 location prompts (~11 locations in locked style) | 0 prompts | [BLOCKED] | Style lock |
| Tier 3 location prompts (~7 locations in locked style) | 0 prompts | [BLOCKED] | Style lock |
| Total location images (incl. state variants) | ~45 target | [BLOCKED] | Style lock |

### 5.5 Art Assets — UI

| Asset class | Count | Status | Blocker |
|---|---|---|---|
| Hero UI prompts (Log / Call / Board) × 3 styles × 3 platforms = 27 | 27 prompts | [READY] | None |
| Supporting UI (Memory Fragment overlays / title cards / menus / etc.) | 1 canonical per style | [READY] | None |
| UI generation (any) | 0 | [READY] | Tool access |
| UI in locked style (all 18 UI deliverables) | 0 | [BLOCKED] | Style lock |
| UI implementation in engine | — | [BLOCKED] | Engine / build team |

### 5.6 Art Assets — Cutscenes

| Asset class | Count | Status | Blocker |
|---|---|---|---|
| Cutscene structural spec (23 scenes) | [DONE] | [DONE] | — |
| Cutscene key-frame prompts (20 scenes to prompt) | 0 prompts | [BLOCKED] | Style lock |
| Cutscene key-frame generation | 0 | [BLOCKED] | Prompts then style |
| AI animation clips (8 identified scenes, ~160 total seconds) | 0 | [BLOCKED] | Key-frames + Runway credits |
| Cutscene editing / integration | 0 | [BLOCKED] | Engine / editor |

### 5.7 Audio Assets — Voices (Local-First Production Path)

| Asset class | Count | Status | Blocker |
|---|---|---|---|
| Voice briefs (ElevenLabs + local TTS) for all 11 characters | [DONE] | [DONE] | — |
| Local TTS environment setup (F5-TTS + GPT-SoVITS on RTX 5080) | [READY] | [READY] | 1 day install |
| Manuscript parser + batch generation tooling | [READY] | [READY] | ~8–12 engineering days |
| ElevenLabs Pro subscription (Mira A/B only) | [READY] | [READY] | $99/month for 1 month |
| Voice cloning — Mira (source recording → GPT-SoVITS clone) | 0 | [BLOCKED] | VO actor casting + contract |
| Voice cloning — Yui (→ GPT-SoVITS) | 0 | [BLOCKED] | VO actor casting + contract |
| Voice cloning — Sora (→ GPT-SoVITS) | 0 | [BLOCKED] | VO actor casting + contract |
| Voice reference selection — Kenji (F5-TTS) | 0 | [READY] | Library audio + local setup |
| Voice reference selection — Endo (F5-TTS) | 0 | [READY] | Library audio + local setup — critical casting |
| Voice reference selection — Reiko, Doi, Haruki, Aizawa, Fumiko, Rina (F5-TTS) | 0 | [READY] | Library audio + local setup |
| Voice reference selection — Kaito (Fish Speech or F5-TTS) | 0 | [DECIDE] | License decision on Fish Speech if commercial |
| Mira voice generation (~1,500–2,000 lines, GPT-SoVITS local + ElevenLabs A/B on 11 load-bearing) | 0 | [BLOCKED] | Clone complete + tooling |
| NPC voice generation (~500 lines per, × 10 NPCs, F5-TTS/Fish local) | 0 | [BLOCKED] | Tool setup + tooling |
| Exchange room residue voice generation (GPT-SoVITS or Fish Speech local) | 0 | [READY] | Local setup only |
| Localization voice generation (JP / CN / KR via GPT-SoVITS) | 0 | [BLOCKED] | English voices complete + localized scripts |

### 5.8 Audio Assets — Non-Voice

| Asset class | Count | Status | Blocker |
|---|---|---|---|
| Audio signature spec — per NPC / per location | [DONE] | [DONE] | — |
| Wire-sound custom design | 0 | [HUMAN] | Sound designer |
| Wire-sound chapter state transitions | 0 | [HUMAN] | Sound designer |
| NPC audio tic SFX (sanitizer click, pen click, pencil tap, etc.) | 0 | [READY] | ElevenLabs SFX or foley |
| Environmental ambient beds (~30 locations × 2–5 min each) | 0 | [READY] | ElevenLabs SFX or field recording |
| Music cues (4–6 total, if included) | 0 | [DECIDE] | Go/no-go on music |
| Final mix | 0 | [HUMAN] | Sound designer |

### 5.9 Build / Engine / Integration

| Asset class | Status | Blocker |
|---|---|---|
| Engine selection | [PENDING] | Project team / scope decision |
| UI state machine | [BLOCKED] | Engine |
| Audio integration pipeline | [BLOCKED] | Engine |
| Save system | [BLOCKED] | Engine |
| Localization infrastructure | [BLOCKED] | Engine |
| Accessibility layer | [BLOCKED] | Engine + AD script production |
| Playtest prototype | [BLOCKED] | All of the above |

---

## 6. PHASE PROGRESSION GATES

Go/no-go criteria between production phases.

### 6.1 Phase 1 → Phase 2 Gate (Style Lock)

**Required before moving to Phase 2:**
- [ ] 99 character portraits generated across all three styles and platforms
- [ ] 27 hero location backgrounds generated across all three styles and platforms
- [ ] Review layout (3×3×11 character grid + 3×3×3 location grid) assembled
- [ ] Evaluation against 6 criteria completed (`deadringer_asset_pipeline.md` §1.2)
- [ ] Top 2 style candidates re-generated with seed variations
- [ ] Style commitment signed off by Creative Director
- [ ] Winning platform (Gemini / SD / Midjourney) committed
- [ ] Character reference sheets prepared for locked style (for LoRA or reference use)

### 6.2 Phase 2 → Phase 4 Gate (Animation Start)

**Required before moving to Phase 4 animation:**
- [ ] All cutscene key-frames produced and approved
- [ ] Character consistency verified across scenes
- [ ] Runway / Kling tool access confirmed
- [ ] Runway credit budget allocated (~750 credits estimated)
- [ ] First 3 animation test clips produced and reviewed

### 6.3 Phase 3 → Phase 5 Gate (Audio Integration)

**Required before moving to final audio integration:**
- [ ] All character voices generated (Mira + 10 NPCs)
- [ ] Wire-sound custom-designed (human sound designer)
- [ ] Environmental beds produced for all locations
- [ ] NPC SFX library complete
- [ ] First chapter's full audio integrated as test

### 6.4 Phase 5 → Launch Gate

**Required before launch:**
- [ ] All content integrated
- [ ] Playtest feedback incorporated
- [ ] Accessibility layer complete (AD script, high-contrast, etc.)
- [ ] Localization pass complete (if shipping localized)
- [ ] Legal review of all contracts and licenses
- [ ] Final mix approved by sound designer + creative director

---

## 7. SCHEDULE ESTIMATE

Rough estimates for planning. Actual schedule depends on team size, tool access, and iteration count.

| Phase | Duration (est.) | Team requirement |
|---|---|---|
| Phase 1 — Style audition | 2–4 weeks | Creative director + 1 prompt operator |
| Phase 2 — Full art production | 8–12 weeks | 1–2 prompt operators, compositor |
| Phase 3 — Voice production (local-first + ElevenLabs A/B) | 6–10 weeks | Voice director + local TTS operator + voice actors (sessions) + Python engineer for tooling (~2 wks front-loaded) |
| Phase 4 — Animation | 4–6 weeks | Animation operator + compositor |
| Phase 5 — Audio integration | 4–8 weeks | Sound designer + mix engineer |
| Build integration | Parallel | Programming team |
| Playtest + polish | 6–8 weeks | Playtest coordinator + iteration |

**Total (rough):** 6–9 months from style lock to launch-candidate, assuming focused team and no major scope changes.

**Phase 3 note:** local TTS adds ~2 weeks of tooling development at the start of Phase 3 (manuscript parser, batch scripts, take management UI, consistency audit). After that initial investment, voice generation runs push-button with unlimited iteration — net neutral to slightly faster than pure-ElevenLabs at equivalent quality.

---

## 8. OPEN DECISIONS

Creative decisions awaiting commitment. Each blocks some downstream work.

| Decision | Impact if decided | Who decides |
|---|---|---|
| **Art style lock** | Unblocks ~80% of remaining art production | Creative Director |
| **Platform lock (Midjourney / SD / Gemini)** | Affects consistency tooling (LoRA vs reference) | Creative Director |
| **Mira voice: adult VO or child VO?** | Affects labor contracts, session duration, emotional range | Creative Director + Casting |
| **Voice production: local-first confirmed?** | Tentatively resolved (local-first + ElevenLabs A/B). Confirm or revise after local TTS setup + initial test generation on one test character. | Creative Director + Voice Director |
| **Kaito voice tool: Fish Speech or F5-TTS?** | Fish Speech has better teen-male register; F5-TTS is MIT-licensed for commercial use without additional negotiation. | Creative Director (license path decision) |
| **Music: include any at all?** | Affects Phase 5 scope | Creative Director |
| **Localization targets: JP, CN-S, KR, others?** | Affects voice, translation, review budget. GPT-SoVITS handles all three natively. | Publisher / Producer |
| **Ch 9 Garden prompt: split or keep unified?** | Minor mechanical question; audit flagged ambiguously | Creative Director |
| **Fragment skip on NG+ only or always?** | Affects replay experience | Creative Director |
| **Emerging Board slot visibility in Ch 11** | Spoiler trade-off vs thoroughness feedback | Creative Director |

---

## 9. DEPENDENCIES — VISUAL

Simplified dependency graph. `→` = blocks.

```
Phase 1 (Style Audition)
  → Style Lock
    → Phase 2 Art (locations, characters, UI, cutscene keyframes)
      → Phase 4 Animation (Runway/Kling)
    → LoRA training
      → Phase 2 character variants

Phase 3 (Voice)
  → Voice actor casting (child voices)
    → Clone sessions
      → Mira / Yui / Sora voice generation

Sound Designer commission
  → Wire-sound
    → Phase 5 audio integration

Engine decision
  → UI state machine
  → Audio integration pipeline
  → Save system
  → Playtest prototype
```

Critical path: Style Lock → Phase 2 Art → Phase 4 Animation. If any link in this chain stalls, art production stalls.

Parallel tracks (not on critical path): voice production, sound designer work, engine / build. These can proceed while art is in progress.

---

## 10. SPEC INDEX

Alphabetical index of every spec doc. One-line purpose per file.

- **`character_image_prompts.md`** — 99 AI prompts for character portrait style audition
- **`chapter_01.md` through `chapter_12.md`** — The 12 chapter scripts of the game
- **`chapter_structure.md`** — Information economy, NPC availability matrix, act structure
- **`compile_manuscript.py`** — Python script to compile chapters into `dead_ringer_complete.md`
- **`dead_ringer_complete.md`** — Compiled manuscript (preface + 12 chapters + epilogue)
- **`deadringer_asset_pipeline.md`** — 5-phase generative asset production plan
- **`deadringer_audio_signatures.md`** — Per-NPC/per-location audio design + wire-sound + Mira voice chain
- **`deadringer_board_slot_audit.md`** — Audit of 70 notebook prompts against 8 Board slots, reachability analysis
- **`deadringer_characters.md`** — Character bible for all 11 NPCs
- **`deadringer_cutscene_structure.md`** — 23 cutscenes with format / tier / production specs
- **`deadringer_elevenlabs_voice_briefs.md`** — Per-character voice production briefs (ElevenLabs §1–16 + local TTS workflow §17, F5-TTS / GPT-SoVITS / Fish Speech on RTX 5080)
- **`deadringer_game_bible.md`** — Thesis, core mechanics, design philosophy (top-level pitch doc)
- **`deadringer_hero_location_prompts.md`** — 27 hero location prompts for style audition
- **`deadringer_intent_matrix.md`** — Per-call tuning matrix: intents × NPCs × chapters
- **`deadringer_locations.md`** — 22 locations with tiers, states, art direction
- **`deadringer_memory_fragments_production.md`** — Production spec for 3 interactive Mira-POV scenes
- **`deadringer_notebook_system.md`** — Hero UI architecture — notebook + confrontation Board
- **`deadringer_production_tracker.md`** — This document
- **`deadringer_soul_read_voice_direction.md`** — Mira voice coaching — 12-chapter degradation curve
- **`deadringer_systems.md`** — Master systems spec (call / intent / soul read / memory / slots / degradation / contradictions / meta)
- **`deadringer_ui_art_prompts.md`** — UI prompts for notebook / call / Board + supporting elements
- **`epilogue.md`** — Epilogue script (11 character resolutions + title screen)
- **`epilogue_production.md`** — Per-scene production spec for the epilogue
- **`ogawa-incident.md`** — Ogawa thread — core Nishida testimony (Ch 8 call + Ch 11 confrontation)
- **`preface.md`** — Manuscript-level structural note (Ch 1 and Ch 9 header conventions)

---

## 11. UPDATE LOG

### 2026-04-23 — Tracker created
- All 21 spec documents complete
- Phase 1 prompts ready (characters + hero locations + UI)
- Phase 3 voice briefs ready
- Cutscene structure specified
- Outstanding: style audition → style lock → Phase 2 art production

### 2026-04-23 — Voice production pivot to local-first
- `deadringer_elevenlabs_voice_briefs.md` extended with §17 Local TTS Workflow
- Primary voice production path now: F5-TTS (adult NPCs) + GPT-SoVITS (child voices and Mira) on RTX 5080
- ElevenLabs retained as A/B testing resource for 11 load-bearing Mira lines only (Pro tier, ~$99/month for one month)
- Per-character tool assignments specified in voice briefs §17.4
- Tooling development added as action item (~8–12 engineering days for manuscript parser + batch scripts + take management UI + consistency audit)
- Child voice casting (Mira, Yui, Sora VO artists) remains the same blocker regardless of local vs cloud
- Revised voice production budget: $7K–$22K (down from $10K–$32K), with savings primarily in ElevenLabs subscription and audio engineering time
- Net iteration capacity: unlimited (vs character-count capped)
- New risks flagged: local TTS quality gap on Mira hero lines (mitigation: A/B reservation), Fish Speech commercial license for Kaito, Blackwell CUDA compatibility verification, model version pinning

### [future updates]
- Record date and summary of each production milestone as it lands here

---

## 12. QUICKSTART FOR NEW TEAM MEMBER

**If you just joined this project, read in this order:**

1. `deadringer_game_bible.md` — what the game is about
2. `deadringer_systems.md` — how the game works mechanically
3. `deadringer_asset_pipeline.md` — how production is organized
4. **This document** — what's outstanding and blocking
5. The spec relevant to your discipline (art / audio / engineering / writing)

**If you are the Creative Director:** your highest-priority actions are marked [DECIDE] in §1 and §8. Focus on style lock first (§1 #3) — it unblocks the most downstream work.

**If you are a prompt operator / AI artist:** your ready-to-start work is all [READY] rows in §1. Start with character portraits (#1) and hero locations (#2).

**If you are a sound designer:** see §3. You are the critical-path human specialist. Wire-sound spec is in `deadringer_audio_signatures.md` §2.

**If you are a voice director:** see §3 and `deadringer_elevenlabs_voice_briefs.md`. The voice briefs doc covers both ElevenLabs parameters (§1–16) and the local TTS production workflow (§17, primary path). The child voice casting problem (Mira, Yui, Sora) is your first priority — same blocker regardless of local vs cloud. After casting, set up local TTS environment (F5-TTS + GPT-SoVITS on the project's RTX 5080) before starting bulk generation.

**If you are a Python engineer supporting voice production:** you'll build the manuscript parser, batch generation driver, take management UI, and consistency audit tool per `deadringer_elevenlabs_voice_briefs.md` §17.11. Budget ~8–12 days for the tooling pass. This is a prerequisite to bulk voice production.

**If you are an engineer / programmer:** engine choice is still open. All implementation work is [BLOCKED] until that decides. In the meantime, review the systems spec and notebook system spec to scope the work.

---

**END PRODUCTION TRACKER**
