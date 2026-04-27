# DEAD RINGER — Intent × NPC × Chapter Tuning Matrix

Build-time tuning document. For each player-choice point in the game, this doc specifies: intents available, expected outcome per intent, information yield, failure mode, trust delta, and diagnosability signals.

**Companion docs:**
- `deadringer_systems.md` §2 — Intent System overview and design principles
- `deadringer_notebook_system.md` §7.4 — intent lessons as Character Note updates
- Chapter files 1–12, epilogue — source material for every entry in this matrix

**Purpose of this document:**
1. Single-source reference for QA test cases (every intent × NPC × chapter combination has a specified outcome).
2. Tuning parameter table (trust deltas, information yields) for build-time balancing.
3. Diagnosability audit (every failure mode has an authored diagnostic signal).
4. Reachability verification (confirms every intent teaching moment is reachable through standard play).

---

## 1. GLOBAL INTENT MECHANICS

### 1.1 The Five Intents

| Intent | Short Description | Core Risk | Core Reward |
|---|---|---|---|
| **REASSURE** | Lower defenses, build trust, show patience | Appears soft; urgent NPCs respond poorly | Opens guarded NPCs who need safety |
| **PRESSURE** | Force information, name the evasion | Shutdown, hang-up, Dignity Filter activation | Accelerates NPCs who respond to directness |
| **REDIRECT** | Steer sideways, change topic, ask about context | Can feel unfocused; Endo fills redirect space | Reveals information guarded by performance |
| **REMAIN SILENT** | Say nothing; let NPC fill space | Surrender conversational control | Produces the game's richest information |
| **BLUFF** | Claim knowledge not possessed | Caught bluff recalibrates NPC faster | Accelerates NPCs who believe they're outmatched |

### 1.2 Availability Rules

- **Not every intent is available on every call.** Absence is authored. A call offering only REASSURE / REDIRECT / SILENT signals that PRESSURE and BLUFF would be tonally wrong.
- **Intents unlock progressively.** Ch 1's single choice point is forgiving and mechanical (all outcomes converge). Ch 3 introduces the full five. Ch 8+ may restrict intents (e.g., PRESSURE against Endo is almost always wrong; omitting it from a call is the design telling the player so).

### 1.3 Diagnosability Channels

Every intent choice must produce a retrospectively understandable outcome. Three channels carry the feedback:

1. **Mira's commentary** — real-time and post-call observations ("She's doing the voice" / "Stop, you're losing her" / "He doesn't know he just told you that").
2. **Audio signature shift** — the NPC's ambient audio changes observably (Aizawa's click rate, Doi's politeness, Haruki's overflow pausing).
3. **Character Note update** — post-call log entry in the notebook's Character section, phrased as observation not instruction.

No numeric meters, no explicit trust scores. The player reads state through tone.

### 1.4 Trust Delta Convention

Internally tracked per NPC on a five-point scale: `-2 / -1 / 0 / +1 / +2` per intent outcome. The player never sees this number. It gates:
- Which information an NPC volunteers in later calls
- Whether the NPC accepts re-calls after a rough exchange
- Ch 12 switchboard-duel behavior (high-trust NPCs resist Endo's social pressure; low-trust NPCs can be turned)

Ch 12 outcomes are the only place the accumulated trust deltas produce visible consequences. For Acts I–III, trust shapes texture.

---

## 2. INTENT × NPC PROFILES (CONSOLIDATED)

Per-NPC summary of how each intent functions across all that NPC's calls. For per-call breakdowns, see §3.

### 2.1 REIKO KITAHARA (Mira's mother)

**Signature approach:** She is rehearsed. Silence or redirect departs from the script; direct questioning gets the performance.

| Intent | Outcome | Trust Δ |
|---|---|---|
| REASSURE | She deflects with practiced grace. Low yield. | 0 |
| PRESSURE | The rehearsal tightens. Protective register emerges. Nothing breaks. | –1 |
| REDIRECT | Pivot to specific logistics. Her guard relaxes on factual territory. | +1 |
| REMAIN SILENT | The performance decays under its own weight. Highest yield. | +2 |
| BLUFF | She doesn't engage with bluffs — not because she catches them, because she's too tired to play. No effect. | 0 |

**Key calls:** Ch 3 first call, Ch 9 static call (intent tree restricted: REASSURE refused, REDIRECT, SILENT), Ch 11 notebook scene (in-person, not intent-gated).

**Dignity Filter:** no. Her resistance is grief, not pride. Pressure produces protective distance, not escalating courtesy.

### 2.2 DOI (Yanagi Mart owner)

**Signature approach:** Dignity Filter active. Pressure makes him more polite, not more honest. Silence bypasses the filter.

| Intent | Outcome | Trust Δ |
|---|---|---|
| REASSURE | Relaxes slightly. Moderate yield on general topics; nothing on the silver car. | +1 |
| PRESSURE | The Dignity Filter activates. Courteous shutdown. | –2 |
| REDIRECT | Good approach. Neighborhood questions bypass the filter; yields ambient pattern observations. | +1 |
| REMAIN SILENT | Primary teaching mechanic. Bypasses the Dignity Filter entirely. | +2 |
| BLUFF | Potentially effective if the player bluffs knowledge of the photograph (Ren). Risky; if caught, closes the door permanently. | ±2 |

**Key calls:** Ch 3 first call (PRESSURE teaching moment), Ch 6 false confession (SILENT collapses it), Ch 11 case assembly (social access testimony, trust-gated).

**Dignity Filter:** yes, explicitly. Established Ch 3. Broken Ch 6 via silence.

### 2.3 YUI SAKAMOTO (11-year-old abuse victim)

**Signature approach:** The Performance. Adults who might check on her get a well-adjusted-child voice; silence forces the performance to exhaust itself.

| Intent | Outcome | Trust Δ |
|---|---|---|
| REASSURE | The performance receives reassurance and returns it. She has been reassured all her life. Zero actual information. | 0 |
| PRESSURE | Immediate shutdown. Gaps collapse to zero. The door closes. | –2 |
| REDIRECT | Safe territory (school) relaxes her fractionally. Gets surface-level observations. | +1 |
| REMAIN SILENT | PRIMARY MECHANIC. The performance runs out of material; fragments leak. | +2 |
| BLUFF | Not authored. Yui is the one NPC the game protects from player bluffs — implementing it would be narratively cruel. | — |

**Key calls:** Ch 4 only. After Ch 4's intervention (if triggered), Yui is unreachable for the remainder of the main line. She reappears in the Epilogue.

**Design note:** BLUFF is explicitly absent from Yui's intent menu. The omission is the design statement.

### 2.4 RINA NISHIZAWA (10, social center of Mira's class)

**Signature approach:** Fills silence with social performance. Silence doesn't work on her the way it works on Yui; Rina fills it cheerfully. Redirect catches her unprepared.

| Intent | Outcome | Trust Δ |
|---|---|---|
| REASSURE | Receives warmly. Continues to deliver the community consensus narrative. | 0 |
| PRESSURE | Produces defensive deflection. The social performance hardens. | –1 |
| REDIRECT | Best approach. Asking about specific students or events catches her before she's curated the answer. | +1 |
| REMAIN SILENT | She fills silence with chatter. Lower yield than Yui's silence. | 0 |
| BLUFF | She's not strategic enough to catch a bluff; low-risk. Moderate yield — she confirms details she assumes the player already has. | +1 |

**Key calls:** Ch 4 primary call, referenced Ch 7 (framing language echo), Ch 11 (absent — Rina is not called during case assembly; her role is background by that chapter).

**Dignity Filter:** no. She defends social position, not personal dignity.

### 2.5 HARUKI ISE (Mira's homeroom teacher, 29)

**Signature approach:** The Overflow. He cannot not talk. All intents produce information; the question is managing what Kenji shares in return.

| Intent | Outcome | Trust Δ |
|---|---|---|
| REASSURE | Over-performed gratitude; accelerated overflow. Player gets extra info but Haruki is more likely to act unilaterally. | +1 / risk |
| PRESSURE | Pressure doesn't land on Haruki the way it lands elsewhere. He absorbs it and keeps talking. | 0 |
| REDIRECT | Effective. Steers him toward specific institutional records rather than emotional confession. | +1 |
| REMAIN SILENT | Haruki fills silences aggressively. Extracts unfiltered material, some of which is unprocessed grief. | +1 / risk |
| BLUFF | He doesn't catch bluffs; he confirms details as if they were his own memories. Fast but risky. | +1 / risk |

**Key calls:** Ch 5 incoming, Ch 6 PoNR-leading interactions, Ch 9 break scene, Ch 11 case assembly.

**Key risk mechanic:** POINT OF NO RETURN (Ch 6). Information shared with Haruki in Ch 5–6 determines what he acts on unilaterally in Ch 6's PoNR. More info shared = bigger PoNR = more cascade damage. The calculated reassure/withhold pattern is the teaching.

### 2.6 AIZAWA EMI (vice principal / school counselor)

**Signature approach:** Procedural walls. Cannot be pushed through; must be navigated around. The Sanitizer Rate is her state indicator.

| Intent | Outcome | Trust Δ |
|---|---|---|
| REASSURE | Acknowledged procedurally. Low yield. | 0 |
| PRESSURE | The click rate speeds. She answers narrowly; the wall thickens. | –1 |
| REDIRECT | Primary mechanic. Asking about her previous school, her sleep habits, her filing system reveals the person behind the procedure. | +1 |
| REMAIN SILENT | Effective. The procedural register cracks under silence more than under challenge. Ch 8 break is silence-triggered. | +2 |
| BLUFF | "We've reviewed the council's disposition" — if the bluff is plausible she confirms details. If not, she deflects procedurally. | +1 / –1 |

**Key calls:** Ch 5 first call, Ch 8 break scene (the sanitizer stops), Ch 11 case assembly.

**State indicator:** Sanitizer click rate. Slow = composed. Speeding = pressure landing. Stopped = break.

### 2.7 FUMIKO ARAI (journalist)

**Signature approach:** Transactional. Bluffs can work; sustained withholding produces her publishing early. She has a clock of her own.

| Intent | Outcome | Trust Δ |
|---|---|---|
| REASSURE / TRADE-FRAMED | Accepted on trade terms. She goes first, but the clock starts. | +1 |
| WITHHOLD (proxy for PRESSURE) | She waits. Her pen doesn't stop. The clock accelerates. | –1 |
| REDIRECT (as "TEST") | Probing her prior knowledge. She respects this and matches it with disclosure. | +1 |
| REMAIN SILENT | She fills silence strategically, demonstrating value. Useful opener; diminishing returns. | 0 → +1 |
| BLUFF | Highest-risk NPC for bluffs. If plausible, accelerates her disclosure. If caught ("Don't insult me"), hard trust loss. | +2 / –2 |

**Key calls:** Ch 6 first call (sets the terms), Ch 7 blind spot, Ch 8 (Ogawa — core Nishida testimony), Ch 10, Ch 11 one-key testimony, Ch 12 publication decision.

**Meta-system:** The Fumiko Publication Timer. See `deadringer_systems.md` §5.4.

### 2.8 KAITO NISHIMURA (17, homeschooled, observer)

**Signature approach:** Delayed Signal. Silence is correct. Direct questioning accelerates him out of his native register. Patience produces the richest disclosures.

| Intent | Outcome | Trust Δ |
|---|---|---|
| PATIENCE (proxy for REASSURE) | Primary mechanic. He translates his notation system into language someone else can parse. Full data flow. | +1 |
| DIRECT (proxy for PRESSURE) | Accelerates him; he delivers faster but less contextualized. Adequate for spot confirmation. | 0 |
| REDIRECT | Produces adjacent observations (the volunteer man). Valuable for pattern recognition. | +1 |
| REMAIN SILENT | HIDDEN GATE. Unlocks the teenager reveal (detective show origin, unfinished novel). Highest personal disclosure. | +2 |
| BLUFF | Not authored in Kaito's call. His delayed processing makes bluffs ineffective; he asks for clarification rather than responding. | — |

**Key calls:** Ch 7 primary call, Ch 11 case assembly (vehicle logs trust-gated).

### 2.9 ENDO MASATO (the antagonist)

**Signature approach:** The Locked Room. No intent "works" in the Ch 8–9 sense. Intents produce different tell patterns, and the tells are the data. PRESSURE accelerates recalibration; REDIRECT maps his boundary.

| Intent | Outcome | Trust Δ |
|---|---|---|
| REASSURE | Irrelevant. He provides reassurance; he doesn't need it. No effect. | 0 |
| PRESSURE | He does not crack. He recalibrates faster. Each pressure moment costs the player a later opportunity. | –1 (tactical) |
| REDIRECT | PRIMARY MECHANIC. Each redirect forces him to choose avoidance direction. Shape of his redirections = boundary of his secret. | 0 (maps boundary) |
| REMAIN SILENT | He fills silence comfortably. In Ch 9 silence produces his "cables = renovation" tell (preemptive framing defaults). In Ch 11 silence is the first one he cannot fill (the "impossible knowledge" tell). | variable |
| BLUFF | Recognized and adjusted around. Never directly broken; risk-bearing. | –1 (tactical) |

**Key calls:** Ch 8 first call (incoming, mandatory), Ch 9 follow-up (three intent tree: BLUFF / REDIRECT / SILENT), Ch 10 referenced, Ch 11 confrontation (five-phase, different mechanics than standard calls).

**Soul Read:** Locked Room — Mira cannot read him. See `deadringer_systems.md` §3.5.

---

## 3. PER-CALL BREAKDOWN

Chronological index. For each player-choice point: chapter, NPC, intents available, expected outcomes, diagnostic signals.

### CH 1 — MIRA (First Call)

**Player choice:** Single, non-typical. Mira asks Kenji to commit to writing down a number. Choice is FORMAL / REFLEX / HUMAN (per Ch 1 manuscript).

**Intent system:** not yet deployed. All outcomes converge on Mira continuing the call. The choice teaches the player that Mira responds to tone; the specific tone matters less than the act of responding.

**Diagnosability:** Mira's one-line response to each choice reveals the approach's flavor — FORMAL gets procedural acknowledgment, REFLEX gets mild amusement, HUMAN gets the earliest seed of her partnership register.

**Purpose:** teach the player that dialogue has intent. Mechanics introduced in Ch 3.

---

### CH 2 — OBSERVATION (Environmental)

**Player choice:** `[PLAYER CHOICE — OBSERVATION]` at the river path blind stretch. Choose: EXAMINE THE EMBANKMENT / EXAMINE THE TREE LINE / CHECK THE PATH SURFACE.

**Not an intent choice.** This is exploration-depth. Each produces a different notebook entry; the PATH SURFACE option is the optional detail that rewards close looking (tire impressions in soft shoulder).

**Diagnosability:** no feedback needed — the player sees directly what they found.

---

### CH 3 — REIKO (First Call)

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | She says "how kind of you" and resumes her rehearsed account. Minimal yield beyond the script. |
| PRESSURE | Register tightens. She withdraws. First notebook prompt shortens. | 
| REDIRECT | Asks about Mira's daily schedule / logistics. Reiko relaxes; yields specific schedule details Mira uses later. |
| SILENT | Three-second gap. She fills it with information she didn't plan to share — the single-mother exhaustion, the guilt narrative she's built. Highest yield. |
| BLUFF | She does not engage with bluffs in grief mode. Response is a flat acknowledgment. |

**Soul Read post-call:** yes. "Pressure, fracture, love shaped wrong. Didn't believe me enough to be afraid." Rich early-game read.

**Diagnosability:** Mira's pre-call commentary (she'll be ready, she has a version, don't push her yet) sets player expectations. Post-call, Mira is quiet — the first time she goes quiet from emotional weight, which teaches the player that calls cost Mira.

**Teaching goal:** introduce the full intent system. SILENT is the highest-yield option; REDIRECT is second; PRESSURE produces withdrawal.

---

### CH 3 — DOI (First Call)

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | "You're not here to accuse. Fine." Moderate opening; he mentions "my own situation" (euphemism for custody). |
| PRESSURE | PRIMARY TEACHING MOMENT. The Dignity Filter activates. He becomes courteous, formal, distant. Ready to hang up. |
| REDIRECT | Neighborhood questions — bypasses the Dignity Filter. Yields his "somebody's project" observation (echoes Mira's Ch 2 line). |
| SILENT | The store sounds fill the space. "...I don't know what you want me to say." Honest register emerges without prompting. |
| BLUFF | "We have the officer's original notes." Risky. If plausible, he confirms having said more than the canvass recorded. |

**Additional content:** the streetlight curmudgeon beat (Ch 3 insertion) lands in REDIRECT and extends his non-defensive register.

**All-paths outcome:** he mentions the drawing boy (Sora artifact #2).

**Soul Read post-call:** yes. "Sadness so old it's turned into furniture. He's not hiding what you think he's hiding."

**Diagnosability:** Audio signature — his courtesy ESCALATES under PRESSURE. The player hears him become more polite, which is the opposite of what pressure is supposed to produce. This is the audible tell.

**Teaching goal:** introduce the Dignity Filter. The player learns that "pushing harder" has a failure mode that disguises itself as cooperation.

---

### CH 3 — BRIDGE NUMBER

**Intents available:** N/A (no one answers)

**Outcome:** structured static. Not a person, not a recording. The player logs it as anomaly. Mira notes "I know that sound" vaguely (foreshadowing Ch 10 resolution).

**Purpose:** establish that not every call connects to a person. The phone is infrastructure, not just a person-to-person tool.

---

### CH 3 — MIRA (Yui Disclosure Prep)

**Player choice:** `[PLAYER CHOICE — Responding to Mira]`

**Intents available:** reduced set — LISTEN / ACKNOWLEDGE / ASK.

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| LISTEN | She delivers the full disclosure about Yui at her own pace. |
| ACKNOWLEDGE | Faster delivery; she is relieved to be received. |
| ASK | She answers each question; more clinical, less emotional texture. |

**Diagnosability:** Mira's armor state in the scene — she's holding the name, releasing it one beat at a time. LISTEN lets her release at her own pace; ASK extracts faster at emotional cost.

**Not a trust-gating choice.** Mira is not gated by trust — she is a constant. The choice shapes texture, not outcome.

---

### CH 4 — YUI (Primary Call)

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF (per manuscript) — but BLUFF is narratively soft-locked; the game simply doesn't populate a usable bluff for this call.

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | The performance accepts reassurance. Zero actual information. Call stalls. |
| PRESSURE | Immediate shutdown. "We maybe talked a few times at school?" Mira: "Stop. You're losing her." |
| REDIRECT | "Tell me about the school." Safe territory; she relaxes fractionally. Yields Haruki reference. |
| SILENT | PRIMARY MECHANIC. Apartment's curated silence becomes audible; Yui fills with fragments. |
| BLUFF | "Mira's mother told us you were Mira's closest friend" — this is authored and present but produces complicated result: Yui flinches (recognizes the truth disguised as a bluff) but cannot confirm. |

**Soul Read post-call:** yes. "Small — packed herself into a box." Mira's first unguarded ask: "She was my friend and I didn't fix it. I need you to fix it."

**Diagnosability:** audio — the performance has zero gap on safe questions, measurable gaps on close-to-true questions. Longer gap = closer to something real.

**Teaching goal:** SILENT as the game's dominant mechanic. Yui is the first NPC where silence is the unambiguous correct choice.

---

### CH 4 — MORAL FORK (YUI INTERVENTION)

**Player choice:** `[PLAYER CHOICE — The Moral Fork]` — act now vs. defer.

**Not an intent choice.** A narrative branching decision affecting chapter trajectory and Mira's crying scene timing.

**Per-choice outcome:**

| Choice | Outcome |
|---|---|
| ACT NOW | Yui is removed from the house in Ch 4. Crying scene triggers Ch 4. Investigation time cost. |
| DEFER | Continue evidence-building; Yui remains in danger. Crying scene deferred to Ch 5–6 on a different catalyst. |

**Cross-reference:** `chapter_structure.md` — "Mira's Crying Scene — Placement" and "Yui Post-Rescue — Design Note."

---

### CH 4 — RINA

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | Warm reception; full community-consensus narrative delivered at length. The "Mira was intense" framing becomes visible. |
| PRESSURE | Defensive deflection. "I'm just trying to help, you don't have to be harsh." |
| REDIRECT | Best approach. Asking about specific events (playground renovation) catches her before curation; she mentions Endo positively without realizing the name matters. |
| SILENT | She fills silences with social chatter; moderate yield, lower than Yui's silence. |
| BLUFF | "Several classmates have said you had a complicated dynamic" — she confirms details, assuming the player has more than they do. |

**Soul Read post-call:** yes. "Remembers things wrong because it works better. Not lying — curating. Not cruel — normal."

**Memory Fragment trigger:** Rina Social Distortion (post-call).

**Diagnosability:** audio is subtle — Rina doesn't shift the way Doi shifts. The tell is verbal: the specific framing ("Mira just misunderstands things sometimes") that echoes later in the Ch 7 framing documents.

**Teaching goal:** the community's consensus narrative as mechanism. The player logs Rina's phrasing; it will return.

---

### CH 5 — HARUKI (First Incoming Call)

**Player choice:** `[PLAYER CHOICE — Receiving Haruki]` — how the player receives the guilt-driven helpfulness.

**Intents available:** all five, but modulated by Haruki's Overflow — see §2.5.

**Per-intent outcome:** per §2.5. All intents produce the school records offer; the choice shapes his self-assigned scope.

**Soul Read post-call:** yes (newly added in this session). "Cup overfilled. He was kind to me but kindness without stakes didn't cost him anything and therefore didn't help me. Use him. Don't trust him with information he doesn't need."

**Diagnosability:** Haruki's pen-click. Steady = he's in overflow (producing information). Stopping = the overflow has hit something it can't proceduralize (the tell that lands twice per call — once at "Sora Hayashi" moment, once at "Mr. Endo was... concerned").

**Teaching goal:** ally management as a mechanic. Haruki is useful and dangerous.

---

### CH 5 — AIZAWA (First Call)

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | Procedural acknowledgment. "I appreciate that, Detective." Sanitizer click steady. |
| PRESSURE | Click rate speeds. She narrows. "I filed through appropriate channels." |
| REDIRECT | Primary mechanic. Asking about her previous school surfaces the earlier reprimand context. |
| SILENT | Click rate slows. She fills with factual chronology. Highest yield. |
| BLUFF | "We've reviewed the council's disposition" — plausible. She confirms the disposition was "no action required" across all filings. |

**Memory Fragment trigger:** Aizawa Procedure (post-call, if procedural register is established).

**Soul Read post-call:** yes. "Holding something heavy, afraid to drop it. Believed Mira — genuinely. Chose documentation over action. Worse than not believing."

**Diagnosability:** sanitizer click rate. Primary audio indicator.

**Teaching goal:** procedural resistance as a distinct failure mode. Information is present but will not be actioned.

---

### CH 6 — DOI (False Confession)

**Player choice:** `[PLAYER CHOICE — Responding to the Confession]`

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF, but the scene's entire architecture is pushing SILENT.

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | Doi treats reassurance as permission to continue the confession. The false narrative accelerates. |
| PRESSURE | Confirms the false narrative. Doi is surrendering; pressure is what he's surrendering TO. Pressure deepens the lie. |
| REDIRECT | Questions about Ren (the grandson in the photograph) crack the surface. Effective but risky — if pursued hostilely, Doi re-entrenches. |
| SILENT | COLLAPSE. Doi stops performing guilt and starts leaking grief. The silence reveals the false confession is surrender, not truth. |
| BLUFF | If the player bluffs knowledge of Ren, Doi breaks differently — wounded rather than relieved. Produces information about the custody situation but damages trust. |

**Soul Read post-call:** "Loud inside — every radio on a different station." Confirms guilt is performance; the real hurt is elsewhere.

**Diagnosability:** audio — the store sounds behind him. Under REASSURE and PRESSURE the store stays loud (register protects him). Under SILENT the store quiets — a customer leaves — and his voice becomes audible alone for the first time.

**Teaching goal:** silence as the tool that reveals the false confession. Payoff of the Ch 3 PRESSURE lesson and the Ch 4 Yui SILENCE lesson combined.

---

### CH 6 — FUMIKO (First Call)

**Player choice:** `[PLAYER CHOICE — Fumiko's Terms]`

**Intents available:** TRADE / WITHHOLD / TEST / REMAIN SILENT (BLUFF is not offered on her first call; it becomes available Ch 7+).

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| TRADE | Her preferred mode. She opens with the 48-hour publication commitment. Full disclosure begins. |
| WITHHOLD | Her pen doesn't stop. She waits. Publication clock starts silently; she will publish in 48 hours with or without cooperation. |
| TEST | "What do you know about the safety council's dismissed reports?" She respects the specificity; matches disclosure. |
| SILENT | She fills silence strategically, demonstrating value. Useful opener; she delivers the eight-years-ago child case as a demonstration of her archive. |

**Additional content:** the melon-bun warmth-quota beat (Ch 6 insertion) lands in TRADE, flagging her personality without diluting her transactional register.

**Soul Read post-call:** "Angry-tired. Still believes change is possible. I like her."

**Diagnosability:** pen rhythm. Scratching during her questions = she's recording. Scratching during her answers = she's releasing. The rhythm shift is the trust-tell.

**Teaching goal:** an NPC who negotiates rather than resists. The trade-framed mechanic is Dead Ringer's replacement for PW's "present evidence to unlock dialogue" — here, information flows both directions.

---

### CH 7 — FUMIKO (Convergence Files)

**Player choice:** `[PLAYER CHOICE — Fumiko's Evidence]`

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF — full set for the first time with Fumiko.

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | She accepts; the trust established in Ch 6 carries through. Normal disclosure. |
| PRESSURE | She matches; the transaction accelerates but becomes colder. |
| REDIRECT | Asking about her archive methods yields the infrastructure map's provenance. |
| SILENT | She fills with more data than usual — her 14-year pattern summary. |
| BLUFF | HIGHEST-RISK MOMENT for Fumiko. If plausible, she raises her assessment of the investigation's depth and shares more. If caught ("Don't insult me"), hard trust loss affects Ch 7+ interactions. |

**Soul Read post-call:** "Same angry-tired but louder. New fear: being wrong when it matters."

**Teaching goal:** BLUFF as a late-game tool. Fumiko is the NPC who teaches the bluff mechanic's real risk profile.

---

### CH 7 — KAITO

**Player choice:** `[PLAYER CHOICE — Kaito's Notebooks]`

**Intents available:** PATIENCE / DIRECT / REDIRECT / SILENCE (BLUFF not authored; see §2.8).

**Per-intent outcome:** see §2.8. SILENCE is the hidden gate for the teenager reveal.

**Soul Read post-call:** "Doesn't know how to show it properly. Someone's listening. Like a window opened in a room that's been closed."

**Teaching goal:** the hidden gate. A player who has learned that SILENCE is valuable is rewarded with the richest character disclosure of the middle act. A player who hasn't learned it gets adequate information via PATIENCE but misses the teenager reveal entirely.

---

### CH 7 — FUMIKO'S BLIND SPOT

**Player choice:** `[PLAYER CHOICE — Fumiko's Lead]` — pursue the lead she recommends, or verify first.

**Not an intent choice.** A time-cost decision. Pursuing the lead loses a slot; ignoring it misses the lesson about verifying Fumiko's instincts.

**Design purpose:** teach the player that Fumiko is a trustworthy partner with blind spots. The lesson lands late-game.

---

### CH 7 — FRAMING EXAMINATION

**Player choice:** `[PLAYER CHOICE — Examining the Framing]`

**Not an intent choice.** Evidence examination pathing. Each branch reveals different framing-document details.

---

### CH 8 — ENDO (First Call)

**Player choice:** `[PLAYER CHOICE — First Response to Endo]`

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT / BLUFF — but all five produce variations on the same outcome: Endo remains helpful, provides real leads, and recalibrates based on what he learns from the player's response.

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | Endo accepts. Delivers three "helpful" leads, all pointing away from him. |
| PRESSURE | Endo adjusts, providing the same leads with preemptive framing. Does not crack. |
| REDIRECT | Endo steers the redirect — provides information on the topic the player pivoted to. Maps the boundary passively. |
| SILENT | Endo fills silence. The tell: his filler is the leads he'd deliver anyway. Silence does not surprise him. |
| BLUFF | Endo recognizes the bluff and adjusts around it. The recognition is the tell — he should not be able to recognize this level of detail, but he does. |

**Soul Read post-call:** the Locked Room. Mira cannot read him.

**Diagnosability:** the player's data is not which intent worked, but what each produced. The TELLS are the yield — his rhythm, his preemptive framing, his recognition of bluffs. Every intent produces a tell entry.

**Teaching goal:** intents map boundaries against Endo. The player must learn that "winning" looks different against a Locked Room NPC.

---

### CH 8 — CATCHING THE TELL

**Player choice:** `[PLAYER CHOICE — Catching the Tell]`

**Not an intent choice.** Evidence-interpretation choice. The player identifies WHICH specific thing Endo said constituted an impossibility. Three branches reveal different tell classifications (rhythmic / informational / empathic).

---

### CH 8 — AIZAWA'S BREAK

**Player choice:** `[PLAYER CHOICE — Approaching Aizawa's Break]`

**Intents available:** REASSURE / PRESSURE / REDIRECT / SILENT (BLUFF omitted — the scene would be cruel with it).

**Per-intent outcome:**

| Intent | Outcome |
|---|---|
| REASSURE | She appreciates it. The click rate slows. She discloses her previous-school reprimand in moderate detail. |
| PRESSURE | Click rate spikes. Then stops. The break happens via pressure, but the disclosure that follows is shaped by resentment. |
| REDIRECT | Asking about her previous school at the right angle produces the break gently — no click-spike, no defensiveness. Most coherent disclosure. |
| SILENT | The break happens through silence alone. Click rate slows, stops. "I chose the version of my job that let me sleep." Most emotionally devastating delivery. |

**Soul Read post-call:** "Cracked — cup that still holds water, can see the line. The closest one."

**Teaching goal:** the scene has multiple paths to the same disclosure; the paths shape the disclosure's emotional register. There is no "wrong" choice here, only tonal choices. A design statement: sometimes the player has agency over HOW something lands, not WHETHER.

---

### CH 9 — REIKO (Static Call)

**Player choice:** Intent tree added in this session — REASSURE / REDIRECT / SILENT (PRESSURE and BLUFF explicitly absent).

**Per-intent outcome:** see §3 call detail in `chapter_09.md`. REASSURE is refused by Reiko; REDIRECT gets the location; SILENT gets the kept log (the most detailed disclosure).

**Teaching goal:** a confession scene. Not every call is adversarial. The game restricts intents to what would be tonally appropriate.

---

### CH 9 — ENDO (Follow-up)

**Player choice:** Intent tree added in this session — BLUFF / REDIRECT / SILENT (REASSURE and PRESSURE absent).

**Per-intent outcome:** see Ch 9 detail. Each produces a different tell pattern, all contributing to Board slot IMPOSSIBLE KNOWLEDGE.

**Teaching goal:** Endo-specific mechanics. REDIRECT is no longer optional; it is the primary approach.

---

### CH 11 — ENDO CONFRONTATION (Five Phases)

**Player choice:** `[PLAYER CHOICE: How to press this]` (and equivalents across five phases).

**Not a standard intent choice.** The confrontation uses a different mechanic: Board slot presentation against phase topics. See `deadringer_notebook_system.md` §5.5.

Standard intents remain available as modulators, but they don't drive the confrontation's advancement — Board slot presentation does. A player may still REDIRECT or SILENT during a phase; the effect is secondary to which Board slot they present.

**Teaching goal:** the confrontation is not a normal call. It requires a different toolkit — the Board — assembled from eleven chapters of investigation.

---

### CH 12 — FUMIKO (Publication Decision)

**Player choice:** `[PLAYER CHOICE]` at line 266 — HOLD / PUBLISH.

**Not an intent choice.** A strategic decision about Fumiko's story timing. Shapes Ch 12 outcomes but not through the intent system.

---

## 4. TUNING NOTES / OPEN QUESTIONS

### 4.1 Trust Delta Calibration

The `±2` scale is schematic. Actual tuning may require finer resolution (±5 or ±10). Critical is that the scale is *consistent per NPC* — a –2 with Doi and a –2 with Fumiko should represent comparable damage relative to each NPC's baseline. Playtest will surface whether NPCs need per-NPC scaling.

### 4.2 Intent Availability Overrides

Some calls restrict the intent menu. Reasons:
- **Tonal** (Yui's PRESSURE shutdown is authored as narratively-inappropriate; the game prevents the worst version of a player moment)
- **Mechanical** (Ch 9 Reiko static call removes PRESSURE because it would not fit the confession scene)
- **State** (Ch 11 confrontation uses a different mechanic entirely)

Every override should be audited against the teaching curve. If a player never encounters an intent in a chapter where they'd expect it, the absence should be legible — preferably through Mira's commentary noting the approach is wrong.

### 4.3 Diagnosability Coverage

Every intent × NPC × outcome combination in §3 should have an authored diagnostic signal. Gaps identified during this audit:

- **Rina's audio signature** is less distinct than other NPCs'. Her diagnosability is verbal, not audio. Consider strengthening via ambient (children's voices in her background becoming more or less present based on the call's direction).
- **Haruki's Overflow** is well-established audibly; the tell (the stop) is load-bearing. Confirm in build that the silence is mechanically unambiguous — a 2-second hard stop, not a 0.5-second stumble.
- **Kaito's Delayed Signal** needs per-intent pacing specs. Each intent should produce a different delay profile in his response timing.

### 4.4 Balance Risks

- **SILENT is the strongest intent for most NPCs.** This is by design (the game's thesis is that listening is the mechanic). Risk: players who discover SILENT early may default to it excessively. Mitigation: Endo breaks SILENT's dominance in Act III; Rina and Haruki don't reward silence as strongly as Yui and Doi do.
- **BLUFF is high-variance.** Risk: players may avoid it entirely. Mitigation: Fumiko's Ch 7 call makes bluff a deliberate teaching moment; the reward is specifically tuned to encourage exploration.
- **PRESSURE is rarely optimal.** Risk: players feel the "hard" option is never correct. Mitigation: the intent is present to be a failure mode the player learns from; some calls have a moderate reward for measured pressure (Haruki's Overflow responds to pressure positively in limited doses). Ensure at least two calls in Act II have PRESSURE as a non-wrong option.

### 4.5 Build Deliverables

1. Full trust delta table (one row per NPC × intent × chapter combination). Roughly 180 rows when fully enumerated.
2. Per-call state machine diagrams (FSM per call, with intent edges and state nodes).
3. QA test case set (one per cell — "call Doi in Ch 3 with PRESSURE → expect courteous escalation → verify click stability and final state").

---

## 5. CROSS-REFERENCES

- `deadringer_systems.md` §2 — Intent System overview
- `deadringer_notebook_system.md` §7.4 — intent lessons as Character Note updates
- `deadringer_characters.md` — per-NPC character bibles (establishes base register and break mechanics)
- Chapter files 1–12 — source material; every `**[PLAYER CHOICE — ...]**` block is a row in this matrix

---

**END INTENT MATRIX**
