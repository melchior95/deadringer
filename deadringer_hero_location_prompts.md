# DEAD RINGER — Hero Location Image Prompts (Phase 1)

AI image generation prompts for the three Tier 1 hero locations. Auditions in three art styles across three platforms, matching the structure of `character_image_prompts.md`.

**Locations covered:** Kenji's Apartment (Ch 1 night state), Community Center Exchange Room (Ch 10 primary state), Endo's Garden (Ch 9 morning state).

**Total prompts:** 3 locations × 3 styles × 3 platforms = 27.

**Aspect ratio:** 16:9 widescreen (standard VN background). Characters will be composited on top; designs should leave compositional room (center-weighted or left/right of frame) for dialogue UI.

**Usage notes:**
- Gemini prompts: descriptive paragraph, one generation per prompt
- Stable Diffusion prompts: tag-based with negative prompt; use SDXL or Flux for quality
- Midjourney: concise natural language with MJ-specific flags (--ar 16:9 --v 6.1 --style raw)

---

# 1. KENJI'S APARTMENT

*A small one-room apartment on the Chuo line corridor. Night, 3:47 AM. A single desk lamp pools amber light over a case file, a pocket notebook, and two empty Boss coffee cans. The rest of the apartment is in shadow — a kitchen counter with a cookbook open facedown, a coat draped on a chair, the dark shapes of five old dead phones visible through a slightly ajar desk drawer. Off-white walls read gray in the lamplight. Blinds half-drawn over the window. A distant train rumbles past. The apartment is the home of a man whose life is the shape of procedure because procedure is the one thing that doesn't leave.*

---

## Style 1 — Steins;Gate / Vanillaware Painterly

### Gemini
A widescreen painterly visual novel background of a small one-room Japanese apartment at 3:47 AM, rendered in the warm melancholic style blending Steins;Gate's emotional linework with Vanillaware's luminous painterly depth. A wooden desk sits against the wall beneath a window with half-drawn blinds, and a single desk lamp pools warm amber light across a thin case file, a pocket notebook with a creased spine, and two empty Boss coffee cans — one used as a pencil holder, one still damp at the rim. The rest of the apartment dissolves into deep shadow with cool blue undertones from city light leaking between the blinds. A kitchen counter is partially visible with a battered cookbook open facedown, a coat draped over a chair, and a slightly ajar desk drawer revealing the dark silhouettes of five old dead phones. The wood-laminate flooring shows wear along the traffic path between door and desk. Off-white walls read gray in the lamplight. The atmosphere is the textured quiet of 3:47 AM in a man's apartment — melancholic, procedural, lived-in. Warm amber and deep cool gray-blue palette, painterly fabric and paper textures, 16:9 aspect ratio, visual novel widescreen background with center-weighted composition leaving room for dialogue.

### Stable Diffusion
```
japanese visual novel background, 16:9 widescreen aspect ratio, small one-room apartment at 3:47 AM night, wooden desk under window with half-drawn blinds, single desk lamp warm amber pool of light, thin case file on desk, pocket notebook with creased spine, two empty Boss coffee cans one as pencil holder, kitchen counter with cookbook open facedown, coat draped on chair, desk drawer slightly ajar showing five dead phones as dark silhouettes, wood-laminate flooring with traffic-path wear, off-white walls reading gray in lamplight, cool blue city light through blinds, deep shadow with blue undertones, painterly anime style, Vanillaware luminous depth, Steins;Gate emotional linework, warm amber and deep cool gray-blue palette, fabric and paper textures, melancholic procedural atmosphere, empty room composition, no characters, environmental background
```
Negative: `photorealistic, 3D render, photograph, people, characters, figures, western cartoon, chibi, harsh lighting, oversaturated, bright daylight, cluttered furniture, modern minimalism, sterile, lowres, blurry`

### Midjourney
```
A small Japanese apartment at 3:47 AM — a wooden desk under half-drawn blinds, a single lamp pooling warm amber over a case file and a pocket notebook and two empty coffee cans, the rest of the room dissolving into deep cool-blue shadow. A kitchen counter in the background with a cookbook open facedown. A coat on a chair. A desk drawer slightly ajar showing the dark shapes of five dead phones. Wood-laminate floor with wear along the traffic path. The lived-in quiet of a room where nothing moves. Steins;Gate emotional precision meets Vanillaware painterly warmth, amber lamp against deep blue shadow, melancholic procedural register, empty environmental background, visual novel widescreen --ar 16:9 --v 6.1 --style raw
```

---

## Style 2 — Capcom Kinu Nishimura / Akiman Clean Bold

### Gemini
A widescreen visual novel background of a small Japanese apartment at 3:47 AM, rendered in the clean bold style of Kinu Nishimura and Akiman — precise linework, strong silhouette definition, confident graphic composition. The wooden desk sits against the wall beneath a window with half-drawn horizontal blinds casting clean striped shadow. A single desk lamp produces a controlled amber pool of warm light over a thin case file, a pocket notebook, and two empty Boss coffee cans. The shadow areas of the apartment are rendered in clean cel-shaded gradations with deep blue-gray tones — a kitchen counter with a cookbook face-down, a coat draped on a chair, and a desk drawer ajar revealing five dead phones in strong silhouette. The wood-laminate flooring shows worn traffic paths as clean graphic lines. Off-white walls rendered as flat value areas with crisp edge definition. The composition has bold silhouette readability and strong graphic contrast — warm amber pool against cool blue-gray negative space. 16:9 aspect ratio, widescreen VN background, center-weighted composition with clean negative space for dialogue UI.

### Stable Diffusion
```
japanese visual novel background, 16:9 widescreen aspect ratio, Kinu Nishimura style clean bold linework, Akiman character design sensibility applied to environment, small apartment at 3:47 AM, wooden desk under window with half-drawn horizontal blinds casting clean striped shadows, desk lamp with controlled amber pool of warm light, case file, pocket notebook, two Boss coffee cans, kitchen counter cookbook facedown, coat on chair, desk drawer ajar with five dead phones in strong silhouette, worn traffic paths on laminate flooring, cel-shaded clean gradations, deep blue-gray shadow areas, off-white walls as flat value areas, bold graphic silhouette, warm amber versus cool blue-gray contrast, strong negative space, confident elegant composition, empty environmental background, no characters
```
Negative: `photorealistic, 3D render, photograph, people, characters, figures, painterly blurry soft, watercolor, western cartoon, chibi, harsh noise, overcomplicated, lowres`

### Midjourney
```
A Japanese apartment at 3:47 AM in bold clean Kinu Nishimura linework — strong silhouette, confident graphic composition, crisp cel shading. A wooden desk under half-drawn blinds, striped shadow across the floor. A single lamp pooling warm amber over a case file, a pocket notebook, two coffee cans. The rest of the apartment rendered in clean cool blue-gray negative space — kitchen counter with a facedown cookbook, a coat on a chair, a drawer ajar showing five dead phones in strong silhouette. Worn paths on the laminate floor as graphic lines. Bold graphic contrast between warm amber pool and cool blue-gray shadow. Akiman elegance applied to architecture. Visual novel widescreen background with composition room for dialogue --ar 16:9 --v 6.1 --style raw
```

---

## Style 3 — Schrodinger's Call Gothic

### Gemini
A widescreen gothic illustration of a small Japanese apartment at 3:47 AM, rendered in fine pen-and-ink with dense crosshatching and selective color accents. The image is primarily monochrome ink with accents of inky amber where the desk lamp pools light, and deep teal glowing faintly from within the slightly ajar desk drawer where five dead phones rest in crosshatched silhouette. An ornate Victorian-style border frames the image, its corners worked with subtle telephone cable motifs and small clock shapes. The wooden desk sits beneath a window with half-drawn blinds rendered in precise ink lines. The case file and pocket notebook are defined in meticulous hatching. Static interference patterns disturb the edges of the composition, as though the scene itself is a degraded transmission. The atmosphere is gothic melancholy — Edward Gorey meets haunted visual novel, with the sensibility of an old photograph slowly dissolving. The air carries the weight of procedure performed without hope of resolution. 16:9 widescreen aspect ratio, gothic environmental background, ornate decorative frame, high contrast monochrome with selective amber and teal.

### Stable Diffusion
```
gothic pen and ink illustration, japanese visual novel background, 16:9 widescreen aspect ratio, small apartment at 3:47 AM, fine crosshatching dense linework, monochrome ink base with selective color accents, inky amber around desk lamp pool of light, deep teal glow from ajar desk drawer containing five dead phones, ornate Victorian decorative border with telephone cable and clock motifs in corners, wooden desk under window with half-drawn blinds precise ink lines, case file and pocket notebook meticulous hatching, coffee cans in crosshatched silhouette, kitchen counter with cookbook facedown, coat on chair, static interference patterns at image edges, Edward Gorey gothic sensibility, haunted visual novel atmosphere, degraded transmission aesthetic, high contrast monochrome with selective amber and teal, empty environmental gothic background, no characters
```
Negative: `photorealistic, 3D render, color photograph, modern art style, chibi, bright saturated colors, watercolor, painterly soft, western cartoon, simple flat illustration, lowres, blurry`

### Midjourney
```
A small Japanese apartment at 3:47 AM rendered as gothic pen-and-ink illustration — fine crosshatching, dense linework, monochrome base with selective inky amber glowing around the desk lamp and deep teal emanating from an ajar desk drawer full of dead phones. A wooden desk beneath a window with half-drawn blinds. A case file and pocket notebook in meticulous hatching. A kitchen counter with a cookbook facedown. Static interference patterns fragmenting the image edges. An ornate Victorian border with subtle telephone cable and clock motifs. Edward Gorey meets haunted visual novel — the aesthetic of procedure performed without hope of resolution, an old photograph dissolving. Widescreen gothic environmental background --ar 16:9 --v 6.1 --style raw
```

---
---

# 2. COMMUNITY CENTER EXCHANGE ROOM

*A small sealed concrete room in the basement of a municipal community center, approximately 4 meters by 6 meters. Low ceiling. A single overhead fluorescent fixture, recently replaced. The air has the faint ozone smell of decades of electrical charge sitting in copper wire. A floor-to-ceiling switchboard dominates the far wall — dozens of jacks labeled in faded ink with routing codes from the pre-1986 numbering system, patch cords hanging from hooks with cracked rubber insulation. A folding metal chair sits in front of the switchboard but is turned fifteen degrees away from it, facing instead the wall where cable runs exit through a conduit. The chair's legs have worn four small depressions into the concrete floor from years of weight applied regularly in the same position. A small modern folding table beside the chair holds a thermos, a closed notebook, and a penlight — the personal items of someone who comes here regularly and stays long enough to need tea. A bakelite telephone handset sits on a shelf beside the switchboard, its cord connecting to the board. The room's architecture is the architecture of listening. The horror is that nothing is obvious from the equipment alone — it is the worn chair angle, the personal items, the four depressions in concrete that tell the story.*

---

## Style 1 — Steins;Gate / Vanillaware Painterly

### Gemini
A widescreen painterly visual novel background of a small sealed concrete basement room lit by a single overhead fluorescent fixture, rendered in the Steins;Gate–Vanillaware painterly tradition with warm luminous depth and emotional environmental precision. The room is approximately 4 by 6 meters, low-ceilinged, concrete walls rendered with fine textural paintwork showing decades of dust and the faint ozone stain of sustained electrical charge. A floor-to-ceiling switchboard dominates the far wall — dozens of jacks labeled in faded ink with old pre-1986 routing codes, patch cords hanging from hooks with cracked rubber insulation painted with careful material fidelity. A folding metal chair sits in front of the switchboard but is turned fifteen degrees away from it, facing the wall where cable runs exit through a conduit. Four small worn depressions are visible in the concrete floor at the chair's legs — years of weight applied in the same position. A small modern folding table beside the chair holds a thermos, a closed notebook, and a penlight. A bakelite telephone handset sits on a shelf, its cord connecting back to the switchboard. The atmosphere is quiet and load-bearing — the specific hush of a room that has been used as a listening station for fifteen years. Cool fluorescent white balanced against warm copper tones from the exposed wire. 16:9 aspect ratio, widescreen VN background, composition centered on the chair-and-switchboard relationship with room for dialogue overlay.

### Stable Diffusion
```
japanese visual novel background, 16:9 widescreen aspect ratio, small sealed concrete basement room, 4 by 6 meters low ceiling, single overhead fluorescent light, painterly anime style Steins;Gate Vanillaware warmth, floor-to-ceiling vintage telephone switchboard far wall, dozens of jacks labeled in faded ink old routing codes, patch cords on hooks cracked rubber insulation, folding metal chair turned fifteen degrees away from switchboard facing cable conduit, four worn depressions in concrete floor at chair legs, small folding table with thermos closed notebook penlight, bakelite telephone handset on shelf with cord to switchboard, concrete walls fine texture dust ozone stain, cool fluorescent white balanced with warm copper tones from exposed wire, quiet load-bearing atmosphere, empty environmental background, no characters, painterly fabric and metal textures
```
Negative: `photorealistic, 3D render, photograph, people, characters, figures, western cartoon, chibi, modern server room, computer equipment, bright lighting, clean sterile environment, lowres, blurry`

### Midjourney
```
A small sealed concrete basement exchange room, rendered in Steins;Gate and Vanillaware painterly warmth — 4 by 6 meters, low ceiling, a single overhead fluorescent fixture. A floor-to-ceiling vintage telephone switchboard on the far wall, dozens of jacks labeled in faded ink with pre-1986 routing codes, patch cords hanging from hooks with cracked rubber insulation. A folding metal chair in front of the switchboard but turned fifteen degrees away, facing the wall where cable runs exit through a conduit. Four small worn depressions in the concrete floor at the chair's legs. A small folding table with a thermos, a closed notebook, a penlight. A bakelite telephone handset on a shelf. Cool fluorescent white against warm copper tones from exposed wire. The specific quiet of a room used as a listening station for fifteen years. Widescreen environmental VN background --ar 16:9 --v 6.1 --style raw
```

---

## Style 2 — Capcom Kinu Nishimura / Akiman Clean Bold

### Gemini
A widescreen visual novel background of a small concrete basement room rendered in clean bold Kinu Nishimura linework — precise architectural definition, strong graphic silhouette, confident industrial elegance. The room is 4 by 6 meters, lit by a single overhead fluorescent casting sharp clean shadow patterns. A floor-to-ceiling vintage telephone switchboard dominates the far wall with crisp graphic rendering of each jack, each cord, each label. The patch cords' cracked insulation is rendered as detailed yet clean linework. A folding metal chair sits in bold silhouette, turned fifteen degrees toward the cable conduit wall. Four worn depressions in the concrete floor are rendered as clean graphic ovals. The folding table beside the chair holds a thermos, a closed notebook, and a penlight in strong silhouette. A bakelite telephone handset on a shelf, its cord defined with confident precision. The walls are flat cool-gray value areas with crisp edge definition. The room reads as both functional and sinister at graphic thumbnail size — a tight composition where every element earns its place. Cool industrial palette — pale fluorescent white, cool concrete gray, warm copper-brass on the switchboard jacks as the single color accent. 16:9 aspect ratio, widescreen VN background, bold graphic composition with clean negative space.

### Stable Diffusion
```
japanese visual novel background, 16:9 widescreen aspect ratio, Kinu Nishimura Akiman clean bold style, concrete basement room, single overhead fluorescent, vintage telephone switchboard far wall floor to ceiling, jacks and cords rendered with clean graphic precision, faded ink labels, folding metal chair in bold silhouette turned fifteen degrees toward cable conduit, four worn depressions in concrete floor as graphic ovals, folding table with thermos notebook penlight in silhouette, bakelite handset on shelf, cool concrete gray walls, pale fluorescent white light, warm copper-brass color accents on switchboard jacks, sharp clean shadow patterns, crisp edge definition, confident industrial elegance, strong graphic silhouette, empty environmental background, no characters, tight composition
```
Negative: `photorealistic, 3D render, photograph, people, characters, painterly blurry soft, watercolor, chibi, overcomplicated, cluttered, bright saturated colors, lowres`

### Midjourney
```
A concrete basement exchange room in bold Kinu Nishimura–Akiman linework — 4 by 6 meters, low ceiling, single overhead fluorescent casting sharp clean shadow patterns. A floor-to-ceiling vintage telephone switchboard on the far wall with graphic precision, dozens of jacks and cords. A folding metal chair in strong silhouette, turned fifteen degrees toward the cable conduit wall. Four worn depressions in concrete at the chair's legs. A folding table with a thermos, a closed notebook, a penlight. A bakelite handset on a shelf. Cool concrete gray walls as flat value areas with crisp edge definition. Pale fluorescent white against warm copper-brass on the switchboard as the sole color accent. Confident industrial elegance. Bold graphic composition. Widescreen environmental VN background --ar 16:9 --v 6.1 --style raw
```

---

## Style 3 — Schrodinger's Call Gothic

### Gemini
A widescreen gothic illustration of a small concrete basement exchange room, rendered in fine pen-and-ink with dense crosshatching and static interference textures throughout. The image is monochrome ink with selective color accents — inky teal pulsing faintly from the vintage switchboard's jacks and patch cords, a warmer amber glow emanating from the overhead fluorescent fixture rendered as a pale ghost of light against the dense hatchwork. Floor-to-ceiling ink detail on the switchboard — every jack, every cord, every faded label rendered with obsessive precision, as though the room itself is a grimoire. A folding metal chair sits in stark graphic silhouette, turned fifteen degrees toward the cable conduit wall. The four worn depressions in the concrete floor are rendered as small shadow voids with teal glow reflected into them. The folding table holds a thermos, a closed notebook, and a penlight, each defined in meticulous hatching. A bakelite telephone handset on a shelf, its cord following crosshatched coils back to the switchboard. Static interference patterns disturb the edges and midfields of the image — the room itself is a degraded transmission. An ornate Victorian border frames the composition with telephone cable motifs worked into the scrollwork. Edward Gorey crossed with haunted industrial archaeology. 16:9 widescreen aspect ratio, gothic environmental background, high contrast monochrome with selective teal and amber accents.

### Stable Diffusion
```
gothic pen and ink illustration, japanese visual novel background, 16:9 widescreen aspect ratio, concrete basement exchange room, fine crosshatching dense linework, monochrome ink base with selective color accents, inky teal glow from vintage switchboard jacks and patch cords, amber ghost of fluorescent overhead light, obsessively precise floor-to-ceiling switchboard ink detail, every jack and cord rendered like a grimoire, folding metal chair stark graphic silhouette turned fifteen degrees toward cable conduit, four worn depressions in concrete floor as shadow voids with teal glow reflected, folding table thermos closed notebook penlight meticulous hatching, bakelite handset on shelf crosshatched cord coils, static interference patterns at image edges, ornate Victorian decorative border with telephone cable motifs, Edward Gorey haunted industrial archaeology, high contrast monochrome with selective teal and amber
```
Negative: `photorealistic, 3D render, color photograph, modern art style, chibi, bright saturated colors, watercolor, painterly soft, western cartoon, simple flat, sterile clean, lowres, blurry`

### Midjourney
```
A concrete basement exchange room rendered as gothic pen-and-ink — fine crosshatching, dense linework, monochrome ink with selective inky teal pulsing faintly from the vintage switchboard's jacks, amber ghost of fluorescent light overhead. Floor-to-ceiling obsessively precise switchboard ink detail — every jack, every cord, every faded label rendered like a grimoire. A folding metal chair in stark graphic silhouette, turned fifteen degrees toward the cable conduit. Four small shadow voids in the concrete floor where the chair's legs have worn depressions. A folding table with a thermos, a closed notebook, a penlight. A bakelite handset on a shelf. Static interference patterns at the image edges — the room as degraded transmission. An ornate Victorian border with telephone cable motifs. Edward Gorey meets haunted industrial archaeology. Widescreen gothic environmental background --ar 16:9 --v 6.1 --style raw
```

---
---

# 3. ENDO'S GARDEN

*A modest traditional Japanese house on a quiet residential street, morning light. A garden wraps around the south side of the house — not large, but immaculate. Flowering shrubs, ornamental grasses, several small trees at different stages of maturity. Every planting is equidistant from its neighbors — not the organic scatter of someone who gardens for pleasure, but the measured intervals of someone who assigns each addition its own territory. The two newest plantings sit near the garden's eastern edge, most visible from the sidewalk: a small ornamental shrub (three weeks older) and a sapling that will grow slowly and live for decades (planted the day after a child's body was found). The garden is in bloom despite late autumn — someone has been selecting plants that flower in shifted cycles to keep it visually consistent year-round. The house itself is unremarkable — tile roof, neatly swept entrance, the home of a man who takes care of things. No activity at the house. The view is from the sidewalk — public, visible, respectable. The garden's horror is not architectural; it is in the spacing.*

---

## Style 1 — Steins;Gate / Vanillaware Painterly

### Gemini
A widescreen painterly visual novel background of a modest traditional Japanese house seen from the sidewalk in gentle morning light, rendered in the warm luminous Steins;Gate–Vanillaware tradition. The house has a tile roof, neatly swept entrance, and the quiet unremarkable dignity of a home that is taken care of. A garden wraps around the south side, visible along its 15-meter frontage from the sidewalk — flowering shrubs in cool whites and pale pinks, ornamental grasses in muted gold, and several small trees at different stages of maturity, each planting rendered with loving botanical precision. The key visual detail: every planting is equidistant from its neighbors. The spacing reads as architectural, not organic — the measured intervals of a filing cabinet, not a gardener. Two small newest plantings are emphasized near the eastern edge: a small ornamental shrub and a delicate sapling, both just-established. The sapling is particularly young — its root system still adapting. Morning light is soft and forgiving, dew still present on the leaves. The house itself is in partial shadow, a still silent presence. The atmosphere is beautiful-and-wrong: at thumbnail, the composition reads as an idyllic garden. At full resolution, the unnatural precision of the spacing becomes visible. No human figures. Warm sunrise palette with cool pastel flowers, painterly luminous texture, 16:9 widescreen aspect ratio, composition with the garden as the visual primary and the house in supporting role.

### Stable Diffusion
```
japanese visual novel background, 16:9 widescreen aspect ratio, modest traditional Japanese house with tile roof, residential street morning light, south-side garden visible from sidewalk 15-meter frontage, flowering shrubs cool whites and pale pinks, ornamental grasses muted gold, small trees at different maturity stages, key detail: every planting equidistant with architectural spacing filing-cabinet logic, two newest plantings emphasized at eastern edge small ornamental shrub and delicate sapling, root system of sapling still adapting, morning dew on leaves, soft forgiving sunrise light, house in partial shadow still silent presence, painterly anime style Steins;Gate Vanillaware warmth, botanical precision, beautiful-and-wrong atmosphere, unnatural measured spacing, warm sunrise palette with cool pastel flowers, no human figures, environmental background
```
Negative: `photorealistic, 3D render, photograph, people, characters, figures, organic scattered garden, wild garden, cottage garden, western cartoon, chibi, night scene, harsh lighting, overgrown, lowres, blurry`

### Midjourney
```
A modest traditional Japanese house from the sidewalk in gentle morning light, rendered in Steins;Gate–Vanillaware painterly warmth — tile roof, neatly swept entrance, a garden wrapping the south side visible along 15 meters of frontage. Flowering shrubs in cool whites and pale pinks, ornamental grasses in muted gold, small trees at different maturity stages. The key detail: every planting is equidistant from its neighbors. The spacing reads as architectural, not organic — filing cabinet logic rendered in soil. Two small newest plantings emphasized at the eastern edge — a small shrub and a delicate just-planted sapling. Dew on leaves. Soft sunrise light. The house in partial shadow. Beautiful at thumbnail, wrong at full resolution. No human figures. Widescreen environmental VN background with garden as visual primary --ar 16:9 --v 6.1 --style raw
```

---

## Style 2 — Capcom Kinu Nishimura / Akiman Clean Bold

### Gemini
A widescreen visual novel background of a modest traditional Japanese house and its south-side garden, rendered in clean bold Kinu Nishimura linework with confident graphic precision. The house has a tile roof rendered with architectural clarity, the tiles defined in clean strokes. The sidewalk and garden frontage occupy the lower two-thirds of the composition. Flowering shrubs, ornamental grasses, and small trees are each rendered with strong silhouette definition — clean cel-shaded gradients, crisp edge work, and confident color blocking. The architectural spacing is the composition's thesis: every planting sits at precisely measured intervals, forming a grid that reads as deliberate at first glance. The two newest plantings at the eastern edge are rendered with slightly more visual weight — a small shrub and a young sapling, the sapling's proportions visibly new. Morning light is clean and graphic — pale warm wash with long clean shadows. The house itself reads as a bold silhouette against a cool morning sky. Cool pastel palette accented with graphic shadow. The beauty is confident and the spacing is wrong, and both qualities read at thumbnail. 16:9 aspect ratio, widescreen VN background, garden-primary composition.

### Stable Diffusion
```
japanese visual novel background, 16:9 widescreen aspect ratio, Kinu Nishimura Akiman clean bold style, modest traditional Japanese house tile roof architectural clarity, residential street, south-side garden 15-meter frontage from sidewalk, flowering shrubs ornamental grasses small trees rendered with strong silhouette definition, clean cel-shaded gradients, confident color blocking, crisp edge work, architectural measured spacing between plantings, filing-cabinet grid logic in soil, two newest plantings emphasized eastern edge small shrub and young sapling, sapling visibly new proportions, morning light clean graphic pale warm wash with long clean shadows, house bold silhouette against cool morning sky, cool pastel palette with graphic shadow accents, beautiful-and-wrong composition thumbnail-readable, no human figures, garden-primary environmental background
```
Negative: `photorealistic, 3D render, photograph, people, characters, organic scattered garden, wild garden, painterly blurry, watercolor soft, chibi, cluttered, overcomplicated, lowres`

### Midjourney
```
A modest traditional Japanese house and south-side garden in morning light, rendered in clean bold Kinu Nishimura–Akiman linework — tile roof in architectural clarity, the garden occupying the lower two-thirds of frame. Flowering shrubs, ornamental grasses, small trees with strong silhouette and confident cel shading. Every planting at precisely measured intervals — filing cabinet logic rendered in soil. Two newest plantings emphasized at the eastern edge, a small shrub and a young sapling (visibly just-planted). Clean graphic morning light with long clean shadows. The house as a bold silhouette against a cool morning sky. Cool pastel palette with graphic shadow accents. Beautiful at thumbnail, wrong at full resolution — both qualities readable. Widescreen environmental VN background --ar 16:9 --v 6.1 --style raw
```

---

## Style 3 — Schrodinger's Call Gothic

### Gemini
A widescreen gothic illustration of a modest traditional Japanese house and south-side garden, rendered in fine pen-and-ink with dense crosshatching and selective color. The image is monochrome base with unsettling selective accents: inky deep green where shadows pool in the garden, a pale cold pink in the flowering shrubs that reads as deathly rather than cheerful, and faint silver-gray on the sapling's young bark — the newest planting emphasized as the palest, youngest element in the composition. The house is rendered in meticulous ink detail — tile roof worked in crosshatched rows, entrance swept clean and rendered with almost funereal precision. The garden's measured spacing is the composition's thesis: each planting at precisely measured intervals, rendered as a grid of ink voids in the ground pattern. The two newest plantings at the eastern edge are emphasized with framing ink marks that resemble small headstones in their proportions — the sapling in particular stands out as thin and new and set apart. Morning light is rendered as a ghost of light on the left side of the composition, with crosshatching absence rather than paint. An ornate Victorian decorative border surrounds the image, its scrollwork hiding small leaf shapes and subtle telephone-cable motifs. Edward Gorey garden gothic — the quiet horror of a beautiful thing that is a graveyard. 16:9 widescreen aspect ratio, gothic environmental background, no human figures, the architectural spacing as the composition's sinister thesis.

### Stable Diffusion
```
gothic pen and ink illustration, japanese visual novel background, 16:9 widescreen aspect ratio, modest traditional Japanese house and south-side garden morning light, fine crosshatching dense linework, monochrome ink base with selective color, inky deep green shadow pools in garden, pale cold deathly pink flowering shrubs, silver-gray young bark on sapling, house meticulous ink detail tile roof crosshatched rows, architectural measured spacing between plantings as grid of ink voids in ground pattern, two newest plantings emphasized eastern edge with framing marks resembling small headstones, sapling thin and new and set apart, morning light as ghost of light crosshatching absence, ornate Victorian decorative border with leaf and subtle telephone-cable motifs, Edward Gorey garden gothic, quiet horror of beautiful graveyard, no human figures, environmental gothic background, high contrast monochrome with selective accents
```
Negative: `photorealistic, 3D render, color photograph, bright vibrant colors, cheerful garden, cottage garden, painterly soft, watercolor, chibi, simple flat illustration, lowres, blurry`

### Midjourney
```
A modest traditional Japanese house and south-side garden in gothic pen-and-ink — fine crosshatching, dense linework, monochrome base with unsettling selective accents: inky deep green shadows in the garden, pale cold deathly pink in the flowering shrubs, silver-gray on the sapling's young bark (the palest element in the composition). The house rendered in meticulous ink detail — tile roof in crosshatched rows, almost funereal precision. Every planting at precisely measured intervals, a grid of ink voids in the ground pattern. Two newest plantings at the eastern edge framed like small headstones — the sapling thin and new and set apart. Morning light as a ghost of absence on the left. An ornate Victorian decorative border with leaf and subtle telephone-cable motifs. Edward Gorey garden gothic — the quiet horror of a beautiful thing that is a graveyard. Widescreen environmental background --ar 16:9 --v 6.1 --style raw
```

---
---

## USAGE & EVALUATION NOTES

### Testing Protocol

1. Generate all 27 prompts. Note which platform produces the fastest and which produces the most consistent results.
2. Arrange into a 3×3×3 grid (style × platform × location) in a reference document.
3. Pair with the character portrait grid from `character_image_prompts.md`.
4. Evaluate against the six criteria from `deadringer_asset_pipeline.md` §1.2:
   - Reads at thumbnail
   - Reads at resolution
   - Tonal consistency (with characters)
   - Emotional register
   - Asset productivity (consistency across generations)
   - Cost at scale
5. Top-two styles should be re-generated with 3–5 seed variations each to evaluate consistency.
6. Final style lock decision incorporates both character and location performance.

### Per-Location Quality Bars

**Kenji's Apartment** must land:
- The amber-warm lamp against cool-blue shadow is the shot's emotional geometry — fails if lighting contrast is flat
- The dead phones in the ajar drawer must be visible AND unremarkable — the viewer should be able to count them on close inspection but not notice them on first glance
- The cookbook facedown on the counter is optional prominent, but should exist

**Exchange Room** must land:
- The chair's 15-degree angle (turned away from the switchboard) is the set piece's thesis — if missing, the composition fails
- The four worn depressions in concrete at the chair's legs
- The switchboard must read as archaic-but-maintained, not broken

**Endo's Garden** must land:
- Architectural spacing — not organic scatter. If it looks like a normal garden, the image failed.
- Two newest plantings visible at the eastern edge (shrub + sapling)
- Beauty-with-wrongness on a single frame. The image should be shareable as pretty; the wrongness should arrive on a second look.

### Recurring Failure Modes to Watch

- **Over-cluttered interiors** — AI tends to fill space. Kenji's apartment and the Exchange Room are designed to be *sparse.* Reject outputs that add decor the prompt didn't specify.
- **Organic garden** — AI's garden default is cottage-garden charming. Reject outputs where the architectural spacing isn't visibly legible.
- **Wrong era** — AI sometimes modernizes. The Exchange Room must read as pre-1986 telephony; the switchboard should not look like a modern patch bay.
- **Human figures** — all prompts specify no characters. Reject any output with incidental people.
- **Harsh lighting** — all three locations need atmospheric lighting. Reject sterile/even illumination.

---

**END HERO LOCATION PROMPTS (PHASE 1)**
