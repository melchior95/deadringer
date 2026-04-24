# DEAD RINGER — UI Art Prompts

AI image generation prompts for game UI elements. Structured in three art styles × three platforms to match `character_image_prompts.md` and `deadringer_hero_location_prompts.md`.

**Scope:** notebook UI (two layers), call screen, confrontation Board, Memory Fragment overlays, chapter title cards, menu/meta UI, miscellaneous gameplay overlays.

**Total prompts:** ~45 across six UI categories × 3 styles × 3 platforms. Not every element requires full 3×3 audition — the notebook, call screen, and confrontation Board get the full matrix; smaller elements get one canonical version per style.

**Companion docs:**
- `deadringer_notebook_system.md` — architectural spec for the notebook UI
- `deadringer_systems.md` §8 — Meta/UI specifications
- `deadringer_asset_pipeline.md` §3.3 — UI art production scope

**Core design principle:** the UI is diegetic wherever possible. Kenji's pocket notebook is a physical paper notebook, not a database grid. The call screen is a phone overlay, not an abstract menu. The confrontation Board is a desk of organized evidence, not a skill tree. This is the game's central UI commitment — audition against this principle ruthlessly.

**Aspect ratios:**
- Full-screen UI: 16:9
- Notebook open spread (two-page view): 16:9 or 3:2 depending on orientation
- Call screen overlay: 16:9 with UI framing
- Individual evidence item: 3:4 or 1:1 depending on type

---

# 1. THE NOTEBOOK — THE LOG (Layer 1)

*Kenji's pocket notebook, viewed open to a two-page spread. Left page shows recent entries (reverse-chronological); right page shows section shortcuts and active filters. Paper texture is a specific detail: slightly cream, faint blue rule lines, edges showing handling wear proportional to how far into the game the player is. Kenji's handwriting is precise but not neat — small Japanese half-print, annotations in black or navy pen, occasional underline or star for emphasis. Photographs and business cards are tucked into select pages, visible as rectangular corners protruding from page edges. The notebook sits on a surface — Kenji's desk by default, sometimes open on his lap. The player sees it from a slight angle, as though reading over Kenji's shoulder.*

---

## Style 1 — Steins;Gate / Vanillaware Painterly

### Gemini
A widescreen visual novel UI rendering of an open pocket notebook on a wooden desk, viewed slightly from above and at an angle. The notebook is Kenji Oda's personal pocket notebook, a paperbound book with a creased spine and edges showing the wear of daily use. Rendered in the painterly Steins;Gate–Vanillaware tradition — warm textural paintwork, fine material fidelity. Cream paper pages with faint blue rule lines. The left page shows four or five handwritten notebook entries in precise Japanese half-print, rendered with enough detail to read as handwriting but generalized enough to serve as UI. Entries vary in length; some have small asterisks or underlines. The right page shows section tabs or category labels — ALL / PEOPLE / EVIDENCE / READS / PINNED — arranged as hand-drawn bookmarks or header markers. A photograph corner is visible protruding from between pages further back in the book. A black ballpoint pen rests in the spine channel. Warm desk-lamp light falls across the pages from the left. The atmosphere is intimate, procedural, lived-in — a detective's working notebook, not a sterile database. Warm amber lamp light and cream paper against the surrounding desk's darker wood. 16:9 aspect ratio, composition with UI affordance space for filter tabs along the top or side.

### Stable Diffusion
```
japanese visual novel UI element, 16:9 widescreen aspect ratio, open pocket notebook on wooden desk, slight angle view over-shoulder, detective's personal working notebook, creased spine, cream paper with faint blue rule lines, Japanese half-print handwriting entries left page, section tabs right page (all people evidence reads pinned), photograph corner protruding from back pages, black ballpoint pen in spine channel, warm desk lamp light from left, painterly Steins;Gate Vanillaware style, fine material texture on paper and book cloth, warm amber lamp light and cream paper, intimate procedural atmosphere, UI affordance space for filters, no characters, environmental UI detail
```
Negative: `photorealistic, 3D render, photograph, modern tablet, digital UI, grid interface, sterile, characters, figures, bright daylight, pristine new notebook, lowres`

### Midjourney
```
An open pocket notebook on a wooden desk, viewed slightly from above and at an angle, rendered in Steins;Gate–Vanillaware painterly warmth. Kenji's working detective notebook — creased spine, paper showing handling wear, cream pages with faint blue rule lines. Left page: four or five handwritten entries in precise Japanese half-print. Right page: section tabs (ALL / PEOPLE / EVIDENCE / READS / PINNED) as hand-drawn headers. A photograph corner protruding from further back. A black pen in the spine. Warm desk-lamp light from the left. Intimate procedural UI — a detective's real notebook, not a database. Widescreen visual novel UI element --ar 16:9 --v 6.1 --style raw
```

---

## Style 2 — Capcom Kinu Nishimura / Akiman Clean Bold

### Gemini
A widescreen visual novel UI rendering of an open pocket notebook, depicted in the clean bold Kinu Nishimura–Akiman style with precise linework and strong graphic composition. The notebook is rendered on a wooden desk at a slight over-shoulder angle. Clean graphic cream paper with crisp blue rule lines. Handwritten entries in stylized Japanese half-print — legible as handwriting but rendered with graphic clarity rather than textural naturalism. Section tabs along the right edge are rendered as clean bold rectangular markers in deep navy or maroon: ALL / PEOPLE / EVIDENCE / READS / PINNED. The notebook's creased spine and edge wear are rendered with confident linework rather than painterly texture — the character of age carried by line, not by paint. A photograph corner protrudes from between pages, its edge rendered as a precise graphic shape. The pen in the spine is a clean architectural object. Strong graphic contrast between cream paper and deeper-toned desk surface. Warm amber light source implied through value shifts rather than painterly rendering. 16:9 aspect ratio, widescreen UI composition with clean negative space for interactive overlays.

### Stable Diffusion
```
japanese visual novel UI element, 16:9 widescreen aspect ratio, open pocket notebook on wooden desk, Kinu Nishimura Akiman clean bold style, precise linework, strong graphic composition, cream paper crisp blue rule lines, stylized Japanese half-print handwritten entries, section tabs right edge rendered as clean bold rectangles (ALL PEOPLE EVIDENCE READS PINNED), deep navy and maroon tab accents, creased spine rendered in confident line, photograph corner protruding as precise graphic shape, black pen in spine channel, strong graphic contrast cream paper against wooden desk, amber light through value shifts, cel-shaded rendering, no characters, clean UI composition with negative space
```
Negative: `photorealistic, 3D render, photograph, tablet, digital UI, grid interface, painterly blurry, watercolor soft, characters, cluttered, lowres`

### Midjourney
```
An open pocket notebook on a wooden desk, slight over-shoulder angle, in bold Kinu Nishimura–Akiman linework — clean graphic composition, confident line, strong silhouette. Cream paper with crisp blue rule lines. Left page: handwritten entries in stylized Japanese half-print, legible but graphically rendered. Right page: section tabs in clean bold rectangles (ALL / PEOPLE / EVIDENCE / READS / PINNED) with deep navy and maroon accents. Creased spine rendered in line, not paint. A photograph corner protruding — precise graphic shape. A pen in the spine. Clean negative space for interactive overlays. Confident graphic UI design. Widescreen visual novel UI --ar 16:9 --v 6.1 --style raw
```

---

## Style 3 — Schrodinger's Call Gothic

### Gemini
A widescreen gothic illustration of an open pocket notebook, rendered in fine pen-and-ink with dense crosshatching on the notebook's paper texture and selective color on handwritten content. The notebook sits on a dark wooden surface with crosshatched shadow around its edges. The paper itself is cream-pale rendered primarily through hatching absence rather than paint, with inked rule lines across both pages. Handwritten entries on the left page are in deep monochrome ink — the player can read them as writing but the letterforms have the slightly-too-precise quality of a detective who never writes casually. On specific key entries, selective color accents: inky amber for PINNED entries, deep teal underline for case-critical contradictions. Section tabs along the right edge are rendered as ornate Victorian-style bookmark ribbons, the scrollwork on each tab carrying subtle motifs (telephone cable, clock, whale silhouette). A photograph corner protruding from back pages is rendered as a small rectangular void with faint static interference at its edge. The pen in the spine is rendered as a fine ink architectural element. An ornate Victorian frame borders the notebook itself — not the outer image, but the notebook as a preserved artifact. The atmosphere is gothic-procedural: a detective's working tool preserved like a relic. High contrast monochrome with selective amber, teal, and navy accents. 16:9 aspect ratio.

### Stable Diffusion
```
gothic pen and ink illustration, japanese visual novel UI element, 16:9 widescreen aspect ratio, open pocket notebook on dark wooden surface, fine crosshatching dense linework, monochrome ink base, cream-pale paper through hatching absence, inked rule lines across pages, handwritten Japanese half-print entries deep monochrome ink, selective color accents inky amber for PINNED entries deep teal underline for critical contradictions, section tabs as ornate Victorian bookmark ribbons right edge with scrollwork motifs (telephone cable clock whale), photograph corner protruding as small rectangular void with static interference, pen in spine as fine ink architectural element, ornate Victorian frame bordering the notebook as preserved artifact, crosshatched shadow around notebook edges on desk surface, gothic procedural atmosphere, Edward Gorey sensibility, high contrast monochrome with selective amber teal navy accents
```
Negative: `photorealistic, 3D render, color photograph, modern art style, bright colors, painterly soft, watercolor, digital UI, tablet, grid interface, lowres`

### Midjourney
```
An open pocket notebook on a dark wooden surface in gothic pen-and-ink — fine crosshatching, dense linework, monochrome base with selective amber on PINNED entries and deep teal underlines on critical contradictions. Cream-pale paper through hatching absence. Inked rule lines. Handwritten Japanese half-print entries in deep monochrome ink. Section tabs along the right as ornate Victorian bookmark ribbons with scrollwork hiding telephone cable, clock, and small whale motifs. A photograph corner protruding from back pages — rectangular void with static interference at its edge. A pen in the spine as fine ink architectural element. An ornate Victorian frame bordering the notebook as a preserved artifact. Edward Gorey gothic procedural UI. High contrast monochrome with selective amber, teal, and navy. Widescreen UI element --ar 16:9 --v 6.1 --style raw
```

---
---

# 2. THE CALL SCREEN

*The game's primary interactive surface. Full-screen overlay during calls. Top strip shows caller identity (name, small character portrait if known, "UNKNOWN" otherwise). Lower third houses dialogue text in a bordered panel. Intent selector — five options arranged as clean buttons at choice moments — appears above or beside the dialogue area. A small notebook icon sits in a corner for in-call compact notebook access. The ambient waveform indicator is a subtle thin line at the top edge, visualizing the wire-sound plus the NPC's audio signature. The investigation scene is dimmed and visible behind the call overlay, establishing that Kenji is somewhere while making the call. The call screen is the game's home for approximately 40% of total play time — it must be legible, non-distracting, and evocative.*

---

## Style 1 — Steins;Gate / Vanillaware Painterly

### Gemini
A widescreen visual novel call screen UI mockup, rendered in the Steins;Gate–Vanillaware painterly tradition. Full-screen composition with a soft painterly background depicting a dimmed-out view of Kenji's desk (amber lamp pool, case file, coffee can, blurred and desaturated to suggest the call overlay is the foreground layer). Over this dimmed scene, the call UI: a top strip with caller identity — a small painterly half-body portrait of an NPC (shown as placeholder: Reiko Kitahara, 35, her rehearsed register), a name label in Japanese and romanized script, a call-duration counter. Lower third: a dialogue panel with soft painterly borders, cream textual area with warm handwritten-feeling typography for the current line of dialogue. Right or upper-right area: five intent buttons arranged as soft painterly cards — REASSURE / PRESSURE / REDIRECT / REMAIN SILENT / BLUFF — each labeled in both script, with subtle icons suggesting approach (a cupped hand, a pointing finger, a curved arrow, an empty silence bubble, a mask). Bottom-right corner: a small pocket notebook icon for compact notebook access. Top edge: a very subtle thin waveform line, almost imperceptible, visualizing the wire-sound. Warm amber-gold ambient glow on the UI chrome. The entire composition reads as a phone overlay on a detective's evening desk. 16:9 aspect ratio, painterly visual novel UI mockup.

### Stable Diffusion
```
japanese visual novel call screen UI mockup, 16:9 widescreen aspect ratio, full-screen composition, dimmed painterly background Kenji desk scene (amber lamp case file coffee can desaturated blurred), call UI overlay: top strip caller identity with small painterly half-body portrait NPC placeholder Reiko 35-year-old, name label Japanese romanized, call duration counter, lower third dialogue panel soft painterly borders cream text area warm handwritten typography, right upper-right five intent buttons (REASSURE PRESSURE REDIRECT REMAIN SILENT BLUFF) as soft painterly cards with subtle icons, bottom-right small pocket notebook icon, top edge very subtle thin waveform line for wire-sound, warm amber-gold ambient glow on UI chrome, Steins;Gate Vanillaware painterly warm style, painterly visual novel UI mockup, no foreground characters
```
Negative: `photorealistic, 3D render, modern smartphone UI, iOS android style, flat material design, sterile clean UI, harsh edges, western game UI, chibi, bright saturated colors, lowres`

### Midjourney
```
A visual novel call screen UI mockup in Steins;Gate–Vanillaware painterly warmth — full-screen layout, dimmed painterly Kenji desk scene behind (amber lamp, case file, coffee can all desaturated and blurred). Call UI overlay: top strip with caller identity (small painterly half-body portrait placeholder, Japanese and romanized name label, call duration counter). Lower third: dialogue panel with soft painterly borders, cream text area, warm handwritten typography. Right side: five intent buttons arranged as soft painterly cards (REASSURE / PRESSURE / REDIRECT / REMAIN SILENT / BLUFF) with subtle approach icons. Bottom-right: small pocket notebook icon. Top edge: a very subtle waveform line visualizing the wire-sound. Warm amber-gold ambient on UI chrome. A phone overlay on a detective's evening desk. Widescreen VN UI mockup --ar 16:9 --v 6.1 --style raw
```

---

## Style 2 — Capcom Kinu Nishimura / Akiman Clean Bold

### Gemini
A widescreen visual novel call screen UI mockup rendered in clean bold Kinu Nishimura–Akiman style. Full-screen composition with a dimmed graphic-rendered view of Kenji's desk behind (bold cel-shaded, desaturated, clearly the background layer). Over this: the call UI — crisp architectural elements with confident linework. Top strip with caller identity: a bold cel-shaded NPC portrait (placeholder: Reiko), sharp typography for name label, architectural call-duration counter. Lower-third dialogue panel: clean rectangular frame with strong color-block navy border and cream text area. Intent selector: five buttons arranged in clean graphic grid — REASSURE / PRESSURE / REDIRECT / REMAIN SILENT / BLUFF — each as a bold rectangular button with graphic icons rendered in crisp linework. Compact notebook icon: architectural pocket notebook silhouette, bottom-right. Top edge waveform: a clean graphic line with stylized peaks suggesting audio signature. The UI chrome has strong graphic identity — navy, cream, deep maroon accents, clean metallic gold on hover states. Confident elegant UI design suitable for a detective-fiction VN. 16:9 aspect ratio, bold graphic UI mockup.

### Stable Diffusion
```
japanese visual novel call screen UI mockup, 16:9 widescreen aspect ratio, Kinu Nishimura Akiman clean bold style, full-screen composition, dimmed graphic cel-shaded background Kenji desk scene desaturated, call UI overlay architectural crisp linework, top strip caller identity with bold cel-shaded NPC portrait placeholder, sharp typography name label Japanese romanized, call duration counter, lower-third dialogue panel clean rectangular frame strong color-block navy border cream text area, intent selector five buttons (REASSURE PRESSURE REDIRECT REMAIN SILENT BLUFF) as clean rectangular graphic buttons with crisp linework icons, compact pocket notebook architectural silhouette icon bottom-right, top edge clean graphic waveform line, UI chrome navy cream deep maroon accents metallic gold hover states, confident elegant detective VN UI design, bold graphic mockup
```
Negative: `photorealistic, 3D render, modern smartphone UI, material design flat, painterly blurry, watercolor soft, chibi, oversaturated, lowres`

### Midjourney
```
A visual novel call screen UI mockup in bold Kinu Nishimura–Akiman clean linework — full-screen layout, dimmed cel-shaded Kenji desk scene behind (desaturated, clearly background). Call UI: top strip caller identity with bold cel-shaded NPC portrait placeholder, sharp name typography, architectural call duration counter. Lower-third dialogue panel: clean rectangular frame, navy border, cream text area. Intent selector: five rectangular graphic buttons (REASSURE / PRESSURE / REDIRECT / REMAIN SILENT / BLUFF) with crisp linework icons. Compact pocket notebook icon bottom-right. Top edge: clean graphic waveform line. UI chrome in navy, cream, deep maroon with metallic gold hover states. Confident elegant detective VN UI. Widescreen UI mockup --ar 16:9 --v 6.1 --style raw
```

---

## Style 3 — Schrodinger's Call Gothic

### Gemini
A widescreen gothic illustration of a visual novel call screen UI, rendered in fine pen-and-ink with selective color accents. Full-screen composition with a crosshatched dimmed-down background of Kenji's desk. The UI overlay is rendered as though the call interface itself is a gothic artifact — a telephone receiver turned Victorian communication device. Top strip caller identity: a small ornate oval frame holding an inked NPC portrait, the portrait rendered in monochrome hatching with faint selective color suggesting character mood (teal for Reiko's controlled grief). Name label in elegant serif typography. Call-duration counter as an ornate clockface. Lower-third dialogue panel: a dense crosshatched frame with the text area rendered as cream paper inset, the current dialogue in inked handwriting-feeling typography. Intent selector: five ornate cartouches arranged right-side or bottom, each cartouche in its own Victorian frame with an inked symbolic icon — cupped hands (REASSURE), gripping fist (PRESSURE), curved arrow (REDIRECT), empty bell (REMAIN SILENT), theater mask (BLUFF). Compact notebook icon: an inked miniature notebook with crosshatched pages, bottom-right. Top edge waveform: a jagged inked line with static-interference patterns. The entire UI borders itself with an ornate Victorian frame, scrollwork hiding telephone cable motifs. High contrast monochrome with selective inky amber, teal, and deep red (danger states) accents. The atmosphere is gothic-procedural, as if the game's UI is a document preserved from an older time. 16:9 aspect ratio.

### Stable Diffusion
```
gothic pen and ink illustration, japanese visual novel call screen UI mockup, 16:9 widescreen aspect ratio, full-screen composition, crosshatched dimmed-down background Kenji desk, UI overlay rendered as gothic Victorian artifact, top strip caller identity with small ornate oval frame inked NPC portrait monochrome hatching faint selective color teal, name label elegant serif typography, call duration counter as ornate clockface, lower-third dialogue panel dense crosshatched frame cream paper inset text area inked handwriting typography, intent selector five ornate cartouches (REASSURE PRESSURE REDIRECT REMAIN SILENT BLUFF) each in Victorian frame with inked symbolic icons (cupped hands gripping fist curved arrow empty bell theater mask), compact notebook icon inked miniature crosshatched pages bottom-right, top edge jagged inked waveform with static interference patterns, ornate Victorian border scrollwork hiding telephone cable motifs, high contrast monochrome with inky amber teal deep red accents, Edward Gorey gothic procedural UI
```
Negative: `photorealistic, 3D render, color photograph, modern smartphone UI, material design, bright saturated, painterly soft, watercolor, simple flat UI, lowres`

### Midjourney
```
A visual novel call screen UI as gothic pen-and-ink illustration — full-screen layout, crosshatched dimmed Kenji desk behind, UI overlay as a Victorian communication artifact. Top strip: small ornate oval frame holding an inked NPC portrait (monochrome hatching with faint teal selective color), elegant serif name label, call duration as an ornate clockface. Lower-third dialogue panel: dense crosshatched frame, cream paper inset, inked handwriting-feeling typography. Intent selector: five ornate Victorian cartouches (REASSURE / PRESSURE / REDIRECT / REMAIN SILENT / BLUFF) with inked symbolic icons (cupped hands, gripping fist, curved arrow, empty bell, theater mask). Compact notebook icon as miniature inked notebook, bottom-right. Top edge waveform: jagged inked line with static interference. Ornate Victorian border with telephone cable scrollwork motifs. High contrast monochrome with inky amber, teal, and deep red accents. Edward Gorey gothic procedural UI. Widescreen --ar 16:9 --v 6.1 --style raw
```

---
---

# 3. THE CONFRONTATION BOARD (Chapter 11)

*The Ch 11 confrontation UI — Kenji's desk seen from above, evidence organized into eight thematic slots for presentation against Endo. Each slot holds a small cluster of evidence items: photographs, documents, handwritten index cards, small objects. Slot labels are visible as hand-drawn headers (IMPOSSIBLE KNOWLEDGE / SOCIAL ACCESS PATTERN / COMMITTEE AS MECHANISM / INFRASTRUCTURE ACCESS / THE GARDEN / FRAMING AUTHORSHIP / SOCIAL ACCESS WITNESS / INDEPENDENT CORROBORATION). Each slot has one of four visible states: DORMANT (slot not shown, space empty), EMERGING (greyed, with "X of Y pieces" indicator), COMPLETE (highlighted, presentable), PRESENTED (used, marked). The Board is a desk of organized investigation, not a skill tree. The player sees it from above and slightly rotated, as though standing over Kenji's working surface. When a slot is presentable during confrontation phases, a subtle visual cue highlights it. The desk's wood grain, the paper textures, the hand-drawn labels — everything diegetic.*

---

## Style 1 — Steins;Gate / Vanillaware Painterly

### Gemini
A top-down widescreen visual novel UI rendering of a detective's working desk organized as an eight-slot evidence board, rendered in Steins;Gate–Vanillaware painterly warmth. The camera is above and slightly rotated, showing the desk surface filled with evidence clusters. Eight regions are visible, each labeled by hand-drawn header on a small card (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION). Each slot contains a small painterly cluster of evidence — photographs, documents, index cards with handwriting, small objects like a silver car photograph or a botanical sketch. Slot states differentiated by paint: COMPLETE slots rendered with warm golden light pooling over them, EMERGING slots painted in muted grey-wash with a small "3 of 5" indicator on a scrap of paper, DORMANT slots simply not present in the composition. A cream-paper interface element along the top edge shows the current phase of confrontation (PHASE 2 displayed). The desk surface has painterly wood grain. Pinned above certain slots: handwritten notes with arrows connecting to related evidence in other slots. The composition reads as a detective's actual working evidence organization — not a UI grid. Warm desk lamp light spilling into the image from the right edge. 16:9 aspect ratio, top-down painterly UI mockup.

### Stable Diffusion
```
japanese visual novel UI element, 16:9 widescreen aspect ratio, top-down detective desk view eight-slot evidence board, Steins;Gate Vanillaware painterly style, desk surface filled with evidence clusters organized into eight labeled regions (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION), each slot with painterly cluster of evidence (photographs documents handwritten index cards botanical sketches silver car photo), COMPLETE slots warm golden light pooling, EMERGING slots muted grey wash with 3 of 5 indicator, cream-paper interface element top edge showing PHASE 2, painterly wood grain desk, pinned handwritten notes with arrows connecting slots, warm desk lamp light from right edge, top-down painterly UI mockup
```
Negative: `photorealistic, 3D render, modern software UI, grid interface, sterile clean, digital dashboard, characters, figures, flat graphic design, lowres`

### Midjourney
```
A top-down view of a detective's working desk organized as an eight-slot evidence board, Steins;Gate–Vanillaware painterly warmth. Camera above and slightly rotated. Eight labeled regions on the desk surface (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION) with hand-drawn header cards. Each slot with a painterly cluster of evidence — photographs, documents, handwritten index cards, a botanical sketch, a silver car photo. COMPLETE slots lit with warm golden pools. EMERGING slots in muted grey wash with small "3 of 5" paper indicators. Cream-paper header showing PHASE 2. Painterly wood grain. Pinned notes with arrows connecting slots. Warm desk lamp light from the right. A detective's actual evidence organization, not a UI grid. Widescreen top-down painterly mockup --ar 16:9 --v 6.1 --style raw
```

---

## Style 2 — Capcom Kinu Nishimura / Akiman Clean Bold

### Gemini
A widescreen top-down view of a detective's evidence board rendered in clean bold Kinu Nishimura–Akiman linework. The desk surface is rendered as flat deep-toned wood with confident graphic wood-grain. Eight clearly-defined regions organized across the surface, each labeled with a bold rectangular header card (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION) in crisp serif typography. Each slot contains clean graphic evidence items rendered with strong silhouette — photographs with crisp edges, documents as rectangular shapes with visible typography, index cards with graphic handwriting, stylized object icons. Slot states: COMPLETE slots rendered in bright cream and warm gold with confident color-blocking, EMERGING slots in cool desaturated grey-blue with clean "3 of 5" numerical indicators, DORMANT slots absent from composition. Top edge banner shows PHASE 2 in strong graphic typography. Connection lines between related evidence items rendered as bold graphic arrows in deep navy. The desk is organized with architectural precision — clean, readable, graphic. Confident detective-fiction UI design. 16:9 aspect ratio, top-down bold UI mockup.

### Stable Diffusion
```
japanese visual novel UI element, 16:9 widescreen aspect ratio, top-down detective evidence board, Kinu Nishimura Akiman clean bold style, flat deep-toned wood desk surface with confident graphic wood grain, eight defined regions each with bold rectangular header card (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION) crisp serif typography, clean graphic evidence items strong silhouette photographs documents index cards stylized objects, COMPLETE slots bright cream warm gold confident color blocking, EMERGING slots cool desaturated grey-blue with 3 of 5 indicators, top edge PHASE 2 strong graphic typography, connection lines as bold graphic arrows deep navy, architectural precision UI composition, top-down clean bold UI mockup
```
Negative: `photorealistic, 3D render, painterly blurry, watercolor, modern dashboard, flat material design, chibi, cluttered, lowres`

### Midjourney
```
A top-down detective's evidence board in bold Kinu Nishimura–Akiman linework — flat deep-toned wood desk with confident graphic wood grain. Eight defined regions each with bold rectangular header cards (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION) in crisp serif. Clean graphic evidence items with strong silhouette — photographs, documents, index cards, stylized object icons. COMPLETE slots in bright cream and warm gold with confident color-blocking. EMERGING slots in cool desaturated grey-blue with small "3 of 5" indicators. Top banner: PHASE 2 in strong graphic typography. Connection lines as bold navy graphic arrows. Architectural UI precision. Widescreen top-down mockup --ar 16:9 --v 6.1 --style raw
```

---

## Style 3 — Schrodinger's Call Gothic

### Gemini
A widescreen top-down view of a detective's evidence board rendered in fine pen-and-ink gothic style. The desk surface is crosshatched dark wood. Eight thematic regions organized across the surface, each marked by an ornate Victorian header with the slot name in elegant serif typography (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION). Each slot contains meticulously-hatched evidence items — photographs rendered as crosshatched rectangles with ink detail, documents as densely-inked paper, index cards with inked handwriting, small objects in precise silhouette. Slot states rendered through ink density and selective color: COMPLETE slots glow with inky amber pools that read as halo-light around the evidence cluster, EMERGING slots are cooler and sparser, with a small "3 of 5" indicator written as though in a detective's hand on a scrap of paper, DORMANT slots absent. Top edge banner: PHASE 2 in elegant serif with ornate flourishes. Connection lines as fine ink traces hiding small motifs (telephone cables, clock hands, whale silhouettes). The entire composition bordered by an ornate Victorian frame. Edward Gorey crossed with a detective's grimoire — the evidence organized as both archive and spell. High contrast monochrome with selective inky amber (COMPLETE states), deep teal (knowledge-level contradictions), and deep red (SOCIAL ACCESS WITNESS, the thinnest slot). 16:9 aspect ratio.

### Stable Diffusion
```
gothic pen and ink illustration, japanese visual novel UI element, 16:9 widescreen aspect ratio, top-down detective evidence board, crosshatched dark wood desk, eight thematic regions each with ornate Victorian header elegant serif typography (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION), meticulously hatched evidence items photographs as crosshatched rectangles documents densely inked paper index cards inked handwriting small objects precise silhouette, COMPLETE slots glow inky amber halo light, EMERGING slots cooler sparser 3 of 5 indicator as detective handwriting on paper scrap, top edge PHASE 2 elegant serif ornate flourishes, connection lines fine ink traces hiding telephone cable clock whale motifs, ornate Victorian frame border, Edward Gorey detective grimoire atmosphere, high contrast monochrome with selective inky amber teal deep red
```
Negative: `photorealistic, 3D render, color photograph, modern dashboard, bright saturated, painterly soft, material design, simple flat UI, lowres`

### Midjourney
```
A top-down detective's evidence board as gothic pen-and-ink — crosshatched dark wood desk surface. Eight thematic regions each with ornate Victorian header cards in elegant serif (IMPOSSIBLE KNOWLEDGE, SOCIAL ACCESS PATTERN, COMMITTEE AS MECHANISM, INFRASTRUCTURE ACCESS, THE GARDEN, FRAMING AUTHORSHIP, SOCIAL ACCESS WITNESS, INDEPENDENT CORROBORATION). Meticulously hatched evidence items — photographs as crosshatched rectangles, documents as densely inked paper, index cards with inked handwriting. COMPLETE slots glow with inky amber halo light. EMERGING slots cooler and sparser with small "3 of 5" indicators in detective handwriting. Top banner: PHASE 2 in elegant serif with ornate flourishes. Fine ink connection lines hiding telephone cable, clock, and whale motifs. Ornate Victorian border. Edward Gorey meets detective's grimoire. High contrast monochrome with selective amber, teal, and deep red. Widescreen top-down gothic UI --ar 16:9 --v 6.1 --style raw
```

---
---

# 4. MEMORY FRAGMENT OVERLAYS

*Text-on-screen elements for the three Memory Fragments. Two types: the framing text ("This is a memory. You are Mira.") that appears at fragment entry, and the notebook-deposit text that appears at fragment close (a single crystallized observation from Mira). Both are brief visual moments requiring careful typography and atmospheric treatment. The framing text should feel quiet and declarative. The deposit text should feel like something being written down.*

---

## Canonical Style — Single Version Per Style

These are type-heavy UI elements; prompts focus on typography and atmospheric treatment rather than rich scene composition.

### Style 1 — Painterly (Midjourney canonical)
```
Typography overlay for visual novel memory-fragment entry — the single phrase "This is a memory. You are Mira." rendered in soft warm painterly serif, cream-white text against a black dissolving background with warm amber edge glow. The text sits center-screen and feels quiet, declarative, intimate. Behind the text, a very subtle blur of an indistinct kitchen window at dawn, almost abstracted to atmosphere. No other UI. Wide letter-spacing, gentle antialiased edges, the weight of a sentence spoken once. Widescreen 16:9, Steins;Gate–Vanillaware painterly typography treatment --ar 16:9 --v 6.1 --style raw
```

### Style 2 — Clean Bold (Midjourney canonical)
```
Typography overlay for visual novel memory-fragment entry — "This is a memory. You are Mira." in clean bold serif, cream text on deep navy background, confident letter-spacing, a single thin gold line underneath the text. Behind the text, a subtle abstracted dawn wash in cool blue-grey. No ornamentation. Confident graphic typography, Kinu Nishimura–Akiman UI sensibility. Widescreen 16:9 --ar 16:9 --v 6.1 --style raw
```

### Style 3 — Gothic (Midjourney canonical)
```
Typography overlay for visual novel memory-fragment entry — "This is a memory. You are Mira." in elegant serif with subtle ornamental flourishes at the phrase ends, inked monochrome on cream paper texture, small ornate Victorian filigree marking the start and end of the phrase. Behind the text, crosshatched dawn suggestion and static interference at the edges of the composition. Gothic typography plate, Edward Gorey sensibility. Widescreen 16:9 --ar 16:9 --v 6.1 --style raw
```

### Notebook-Deposit Variant

The post-fragment variant shows the crystallized observation appearing as though being written down. Key example: *"'Can't' and 'won't' are different."* (Reiko Denial fragment close).

```
Typography overlay — a single handwritten line materializing on a cream notebook page: "'Can't' and 'won't' are different." The text appears as though being written in real-time: the first word slightly faded-in, the last word still forming. Ink-pen handwriting, precise but child-sized. Cream paper texture. Soft warm lamp light. Visual novel UI overlay in [style variant per project]. Widescreen 16:9 --ar 16:9 --v 6.1 --style raw
```

---
---

# 5. CHAPTER TITLE CARDS

*Cards that appear at each chapter transition. Each card shows: the chapter number (e.g., "CHAPTER 3"), the chapter title ("First Calls"), and optionally a single orienting line. Brief hold (~3 seconds) before transitioning into the chapter's first scene. 12 chapters + epilogue = 13 title cards total.*

### Canonical Prompts

### Style 1 — Painterly
```
Visual novel chapter title card — a subtle painterly background (indistinct pre-dawn cityscape with one lit window, desaturated to near-monochrome), cream-white typography centered: "CHAPTER 3" in large elegant serif, "First Calls" below in smaller italic, a thin decorative line underneath. Warm amber edge glow on the typography. Soft, quiet, declarative — the feeling of a story continuing. Widescreen 16:9, painterly Steins;Gate–Vanillaware typography treatment --ar 16:9 --v 6.1 --style raw
```

### Style 2 — Clean Bold
```
Visual novel chapter title card — a clean cel-shaded background (abstracted pre-dawn cityscape, single lit window, strong graphic silhouette), cream typography centered: "CHAPTER 3" in bold serif, "FIRST CALLS" below in clean sans-serif capitals, a deep navy rule line between. Confident graphic title card design, Kinu Nishimura–Akiman UI sensibility. Widescreen 16:9 --ar 16:9 --v 6.1 --style raw
```

### Style 3 — Gothic
```
Visual novel chapter title card — gothic pen-and-ink border with Victorian filigree corners, cream paper center panel, elegant serif typography: "CHAPTER III" in decorative capitals, "First Calls" below in italic serif, small ornamental flourish between. Ornate frame with subtle telephone cable motifs worked into the scrollwork. Monochrome with selective inky amber on the chapter numeral. Widescreen 16:9, Edward Gorey gothic typography plate --ar 16:9 --v 6.1 --style raw
```

### Epilogue Title Card

The epilogue title card is distinct — it uses the word AFTER rather than CHAPTER NUMBER. Generate separately as a singular card with slightly longer hold and tonal weight.

---
---

# 6. MENU AND META UI

Main menu, pause menu, settings panels, save/load screen, credits. These are mandatory game-chrome elements but require minimal bespoke prompting — they follow the main UI style once locked.

### Main Menu — Canonical
```
Visual novel main menu mockup — center composition with game title "DEAD RINGER" rendered in elegant serif typography, subtitle "A Phone-Based Mystery" smaller below. Menu options arranged vertically: NEW GAME / CONTINUE / SETTINGS / CREDITS / QUIT. A single atmospheric background element: Kenji's desk seen at three-quarters, lamp on, phone face-down on the surface, dead phones drawer slightly ajar in the background. Widescreen 16:9, [style variant per project]. --ar 16:9 --v 6.1 --style raw
```

### Settings Panel — Canonical
```
Visual novel settings panel UI mockup — clean layout with sections for AUDIO (separate sliders for dialogue, ambient, wire-sound, SFX, music), VIDEO (brightness, contrast, text size, color-blind mode), CONTROLS (keyboard, controller, touch input), ACCESSIBILITY (audio description toggle, camera motion sensitivity, high-contrast text mode), LANGUAGE. Consistent with the call-screen UI chrome. Widescreen 16:9, [style variant] --ar 16:9 --v 6.1 --style raw
```

### Save/Load Screen — Canonical
```
Visual novel save/load screen — three manual save slots plus an autosave slot, each slot shows a small thumbnail (scene, chapter, timestamp) with a short description. The slots are arranged as a horizontal strip of index cards on a desk surface, diegetic framing. Widescreen 16:9, [style variant] --ar 16:9 --v 6.1 --style raw
```

---
---

# 7. MISCELLANEOUS GAMEPLAY OVERLAYS

Smaller UI elements requiring one canonical version per style.

### Notebook Entry Popup
Short UI beat when a new notebook entry is added mid-scene. A small diegetic notification — a notebook page corner flipping up in the screen corner, a brief animated line appearing, a soft "plip" audio cue.

### Call-Incoming Overlay
When an NPC calls Kenji (Haruki Ch 5, Endo Ch 8, Fumiko Ch 9 static, Fumiko Ch 12 opening). A small phone-ring overlay in the screen corner, NPC name if known, accept/decline options.

### Intent Hover/Focus State
When the player hovers (mouse) or focuses (keyboard/controller) on an intent button, the button highlights with a subtle visual cue — a warm glow in the painterly style, a crisp border-thicken in the clean bold style, an inked halo in the gothic style. Each intent has a micro-icon that's more visible in hover state.

### Soul Read Transition
When Mira delivers a Soul Read, the call UI briefly dissolves/fades as her voice takes the center channel. The visual treatment: a soft warm desaturation in painterly, a strong graphic stripe overlay in clean bold, an ink-wash overlay with static interference in gothic.

### Degradation Visual Cues (Late Game)
From Ch 6 onward, the UI itself shows subtle degradation markers when Mira's signal is thinning — a faint static line across the top edge of the call screen, a quarter-second UI dropout coinciding with her voice dropouts, color desaturation in dialogue panel borders. These are not labeled as "Mira's health" — they are environmental.

**Canonical prompt structure (per style) for the degradation state:**
```
Visual novel call screen UI in [style] with subtle degradation state — [specific visual cue per style]. Used from Chapter 6+ to signal Mira's signal thinning without explicit UI labeling. Widescreen 16:9 --ar 16:9 --v 6.1 --style raw
```

---
---

## 8. USAGE & PRODUCTION NOTES

### 8.1 Hero Elements vs Chrome

**Hero UI** (full audition in 3×3 matrix): notebook (Log view), call screen, confrontation Board.

**Supporting UI** (one canonical version per style): Memory Fragment overlays, chapter title cards, main menu, settings, save/load.

**Chrome UI** (single prompt, implement in engine): notebook entry popups, hover states, transition effects, degradation cues.

### 8.2 Diegetic Commitment

Every UI element should read as something that could exist on a detective's desk or in their hand. The call screen is a phone overlay. The notebook is a paper notebook. The confrontation Board is an organized desk surface. The chapter title cards are pages turning. When in doubt, bias toward the diegetic metaphor.

Fail state to avoid: UI that reads as software dashboard. Material design, flat clean material-design, smartphone-iOS sensibility — all wrong for this game.

### 8.3 State Animations

Most UI element transitions are implemented in engine, not as static images. AI-generated images serve as reference for state endpoints; engine handles interpolation. Exception: Memory Fragment entry transitions, which benefit from bespoke animation (see cutscene structure doc).

### 8.4 Localization Considerations

All UI typography must support at minimum English, Japanese, Simplified Chinese, Korean. Verify that chosen typefaces have full character set coverage. Text expansion (English to Japanese: ~1.3×; English to German/French: ~1.2×) requires UI flex in panel widths. Design with expansion in mind.

### 8.5 Accessibility

- High-contrast mode overrides all style choices with WCAG AA-compliant color pairs
- Large-text mode supports up to 200% text scale without breaking layout
- Color-blind modes: protanopia, deuteranopia, tritanopia filters
- Screen-reader compatibility: all UI states have labeled text equivalents

### 8.6 Iteration Priority

1. Lock notebook Log view (most-seen UI, hero element)
2. Lock call screen (most-interacted UI)
3. Lock confrontation Board (Ch 11 set piece)
4. Derive remaining UI from locked hero elements (single-style production)

---

## 9. CROSS-REFERENCES

- `deadringer_notebook_system.md` — architectural spec for notebook UI
- `deadringer_systems.md` §2 — intent system
- `deadringer_systems.md` §5 — call slot economy (affects call screen state displays)
- `deadringer_systems.md` §8 — meta/UI
- `deadringer_asset_pipeline.md` §3.3 — UI art production scope
- `character_image_prompts.md`, `deadringer_hero_location_prompts.md` — style audition companions

---

**END UI ART PROMPTS**
