# DEAD RINGER — Manuscript Preface

## A Note to the Reader

This is a design document that contains a narrative. It is the master script for a phone-based mystery visual novel, written to be simultaneously readable as a story and actionable as a production specification. The two functions share a page.

Each chapter includes, in addition to scene writing:

- **Scene-level direction blocks** — `[VISUAL: ...]`, `[AUDIO: ...]`, `[DESIGN NOTE: ...]`, `[MECHANIC: ...]`
- **Player choice points** with branching responses
- **Notebook prompts** flagging evidence the player should log
- **End-of-chapter state summaries** — Player Knowledge, Notebook Contents, Phone Log, Mechanical State, Threads Open, Emotional Arc

A narrative-first reader can skim the bracketed direction and read the prose alone; the story remains coherent. A production reader can use the direction blocks as the working spec.

If a prose-only edition is ever needed for publication, the end-of-chapter state summaries would move to an appendix and the `[DESIGN NOTE]` blocks would be stripped. The core scene writing stands on its own.

---

## Structural Conventions

Most chapters follow a consistent structure: `## SCENE 1`, `## SCENE 2`, etc., with titled scene headers and player choice points inside each scene. Two chapters depart from this convention for specific design reasons.

### Chapter 1 — Thematic Headers

Chapter 1 uses all-caps thematic headers (THE PHONE, THE TEST, THE READ, THE CASE, THE DIRECTION, FIRST INTENT — THE CHOICE, ALL PATHS CONVERGE, CLOSE) rather than numbered scenes. This is intentional. Chapter 1 is the game's pilot — it teaches the player the core mechanics (phone interface, Soul Read, Notebook, Intent-based dialogue) through a compressed single-call encounter. Thematic headers mark the beats the player is being taught, not the scenes they are passing through. From Chapter 2 onward, the game's structure becomes multi-scene, and the conventional `## SCENE N` format is adopted.

### Chapter 9 — Path-Based Structure

Chapter 9 uses `## PATH A` through `## PATH F` rather than sequential scenes. This reflects the chapter's in-game structure: Chapter 9 is a free-investigation chapter in which the player chooses which leads to pursue from a menu. The paths are not sequential events the player experiences in order — they are parallel options from which the player selects three or four.

**In the game, a player never encounters all six paths in a single run.** The PATH structure reflects the architecture of choice, not the order of experience.

**For a linear read-through** (review, publisher, reference), a suggested canonical ordering:

1. **PATH A — Framing Deconstruction + Haruki's Break** (the chapter's most emotionally central beat)
2. **PATH B — The Garden** (physical proof of pattern)
3. **PATH C — Reiko's Static Call** (the call Reiko didn't take)
4. **PATH D — Sora's Map** (the drawing that maps the infrastructure)
5. **PATH E — Ogawa Thread (Deep)** (the prior suppression that worked)
6. **PATH F — Endo Follow-Up** (the third tell)

In this ordering, Haruki's break arrives first as the chapter's emotional anchor, the garden and the map prove the pattern through physical evidence, Reiko's static call lands the domestic cost, the Ogawa deep thread complicates the player's moral frame on Endo, and Endo's follow-up call closes on the antagonist's recalibration. Any internal cross-references (Haruki appearing in Path A as broken and in Path E as pre-break) are artifacts of the parallel-menu design and can be read past in a linear pass.

---

## A Note on Branching

The game branches on:
- **Trust** (the quality of each NPC relationship, shaped by player dialogue choices)
- **Timing** (Fumiko's publication countdown, Yui's intervention window)
- **Method** (which intent deployed against which NPC)
- **Allies in the final act** (who the player has cultivated by Chapter 12's switchboard duel)

It does **not** branch on culprit identity, on Mira's fate, or on the ending's emotional shape. This is a deliberate design choice that follows from the game's thesis: Dead Ringer is about reconstructing a truth that was always there. Allowing the player to rewrite the truth would undo the story's argument. There is one ending. What the player affects is the density of evidence, the safety of survivors, and the cost of the final confrontation.

---

## A Note on Reading Order

The chapters are written to be read sequentially. Each chapter's emotional and mechanical weight depends on what came before — and several of the manuscript's most important payoffs (the bridge number in Ch 10, Sora's bench artifact across Ch 2/3/5/10, Haruki's "disruptive honesty" in Ch 5 and Ch 9, Reiko's static call in Ch 9 and the notebook scene in Ch 11, Mira's humming in Ch 11 and her final signal in Ch 12) land on readers who have been paying attention to small details for hours.

The document rewards slow reading. The game does, too.

---

**Manuscript total:** 13 files (12 chapters + epilogue), approximately 8,600 lines.
**Companion documents:** `deadringer_game_bible.md` (design thesis and core mechanics), `deadringer_characters.md` (character bible), `chapter_structure.md` (information-economy map and NPC availability matrix), `deadringer_locations.md` (location production specs), `epilogue_production.md` (epilogue scene-by-scene production specification), `ogawa-incident.md` (Ogawa thread background and layered reveal design).

---
