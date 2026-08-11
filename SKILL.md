---
name: research-slides
description: Create evidence-grounded, citation-aware HTML research presentations from papers, research notes, datasets, technical reports, or existing research decks. Use for paper presentations, lab meetings, conference talks, thesis defenses, research reports, technical tutorials, and research-slide redesigns where claims, figures, equations, and quantitative results must remain traceable to sources.
---

# Research Slides

Create research presentations that are visually strong **without weakening scientific traceability**.

The output is a fixed-stage 16:9 HTML deck. The skill should treat papers, figures, tables, equations, and datasets as evidence—not as decoration or generic text to summarize.

## Core Principles

1. **Evidence Before Polish** — A beautiful slide with an unsupported claim is a failed slide.
2. **Narrative, Not Transcription** — Do not convert paper sections into slides one-for-one. Build a research story around the scientific question and evidence.
3. **Show, Don't Tell** — Prefer visual previews, diagrams, figures, equations, and data displays over abstract style descriptions or walls of text.
4. **Claim Traceability** — Important claims, numbers, figures, and equations must have a source pointer or be explicitly labeled as interpretation.
5. **Progressive Disclosure** — Read the lightweight rules first. Load detailed style/template guidance only when needed.
6. **Fixed 16:9 Stage** — Every deck is authored at 1920×1080 and scaled as one stage. Never reflow slide content for phones.
7. **Verify the Render** — Source correctness and visual correctness are separate checks. Perform both.

## Evidence Model

Classify statements before they reach a slide:

| Type | Meaning | Slide treatment |
| --- | --- | --- |
| **Reported** | Directly stated or shown in the supplied source | Cite the exact section/page/table/figure when possible |
| **Derived** | Computed from supplied data or source values | Show the derivation or identify the calculation |
| **Interpretation** | Explanatory language added to improve understanding | Do not present as a source quote or reported finding |
| **Background** | Context from outside the primary material | Keep separate from primary-source findings and cite it when used |

Never silently convert an interpretation into a reported finding.

---

## Fixed Stage Rules

These rules apply to every generated deck:

- Use a `.deck-viewport` filling the browser window.
- Place all slides inside one `.deck-stage` authored at exactly **1920×1080**.
- Scale the whole stage uniformly to fit the viewport.
- Letterbox/pillarbox when needed. Do not rearrange slide content at mobile widths.
- Every `.slide` is 1920×1080 and uses `visibility`, `opacity`, and `pointer-events` for slide switching.
- Do not use responsive breakpoints to turn a research slide into a vertically stacked mobile webpage.
- Keep presentation controls outside the 1920×1080 design canvas.
- Include reduced-motion support.

**Before generating a deck, read `viewport-base.css` and include its full contents in the final HTML.**

## Density Modes

Research decks have two useful density modes. Ask once and design around the answer.

| Mode | Best for | Design behavior |
| --- | --- | --- |
| **Speaker-led** | lab meeting, conference talk, oral defense | one main idea per slide, larger type, fewer bullets, more visual explanation |
| **Reading-first** | async review, detailed report, handout | denser figures/tables/annotations, more self-contained explanation, still no overflow |

Do not create a vague middle setting. If the use case is live persuasion, default speaker-led. If the deck will be read without a presenter, default reading-first.

---

# Phase 0 — Detect the Task

Choose one mode:

- **Mode A: New Research Presentation** — source material → new deck.
- **Mode B: Research Deck Redesign** — existing PPT/HTML/slides → preserve the scientific content while redesigning the presentation.
- **Mode C: Existing HTML Enhancement** — improve an existing research HTML deck without breaking its evidence or layout.

If the user already supplied enough information to determine the mode, do not ask again.

### Mode C Modification Rules

Before changing an existing deck:

1. Count the current slide elements and inspect density.
2. Preserve source labels and citations unless the source itself changes.
3. If adding content causes crowding, split the slide rather than shrinking text.
4. If adding a figure, verify its caption, source, and intended scientific role.
5. After every substantial edit, render-check for overflow, clipping, overlap, and unreadable source text.

---

# Phase 1 — Research Intake

For a new deck, ask unresolved questions **together in one message** rather than one at a time.

## Question 1 — Purpose

What is this presentation for?

- Lab / group meeting
- Conference talk
- Thesis / project defense
- Teaching / tutorial
- Research report / async review

## Question 2 — Length

Approximate length:

- Short: 5–10 slides
- Medium: 10–20 slides
- Long: 20+ slides

## Question 3 — Source Material

What is available?

- Paper / PDF
- Notes / Markdown / text
- Data / tables / notebook outputs
- Existing presentation
- Mixed materials

## Question 4 — Density

- Speaker-led
- Reading-first

If the user has already specified any of these, preserve that answer and ask only for missing information.

---

# Phase 2 — Evidence Extraction

Do this **before** designing slides.

## 2.1 Identify the Research Structure

Extract, when present:

- research problem
- motivation / gap
- hypotheses or research questions
- data / sample / experimental setting
- method / model / algorithm
- equations and variable definitions
- key figures and tables
- quantitative results
- ablations / sensitivity / robustness checks
- limitations
- conclusions

Do not assume every source has all of these.

## 2.2 Build a Claim Ledger

Maintain a working ledger for slide-worthy claims.

Recommended fields:

```text
claim_id
statement
claim_type: reported | derived | interpretation | background
source_pointer
figure_or_table
units / sample size if relevant
confidence / unresolved issue
```

The ledger may stay internal, but the final deck must preserve enough provenance that a reviewer can locate important evidence.

## 2.3 Figures and Tables

For each candidate figure/table:

1. Inspect what it actually shows.
2. Read the caption and surrounding explanation.
3. Record the source pointer.
4. Decide its scientific job in the story.
5. Decide whether to reuse it, crop it, redraw it, or replace it with a faithful explanatory diagram.

Never use a figure simply because it looks visually interesting.

## 2.4 Equations

For every important equation:

- preserve mathematical meaning
- define symbols needed by the audience
- distinguish the source equation from explanatory annotations
- do not alter constants, signs, subscripts, or conditions for visual convenience

## 2.5 Quantitative Results

For every number shown on a slide, preserve:

- value
- unit
- metric definition when ambiguous
- dataset / sample / condition
- comparison baseline when relevant
- source pointer

If any of these are unknown, do not invent them.

Read `RESEARCH_RULES.md` when the source contains empirical claims, statistics, citations, figures, or equations.

---

# Phase 3 — Narrative Design

Do not use the paper's section order automatically.

Design a presentation arc around the audience's question:

```text
Why does this matter?
        ↓
What was missing before?
        ↓
What did the authors / researchers do?
        ↓
How does it work?
        ↓
What evidence supports it?
        ↓
What should we conclude?
        ↓
What remains uncertain or limited?
```

## Slide Planning Rules

- Give each slide one clear scientific job.
- Use slide titles that state the point, not generic labels such as “Results” or “Method” when a more informative title is possible.
- Avoid repeating the same figure on multiple slides unless a later slide clearly uses a different crop or annotation for a different argument.
- Prefer one strong figure plus interpretation over six tiny screenshots.
- Move methodological detail to additional slides when it blocks the main narrative.
- Do not bury limitations only in the final slide if they materially affect interpretation of the results.

Before generating the full deck, create a concise slide outline with:

```text
slide number
message / scientific job
main evidence or visual
source pointer(s)
```

---

# Phase 4 — Visual Style Discovery

**Show options visually instead of asking the user to describe aesthetics in abstract language.**

## 4.1 Generate Three Real Title-Slide Previews

Create three distinct single-slide HTML previews using actual deck content.

Default mix:

- **A — restrained academic option** from `STYLE_PRESETS.md`
- **B — stronger editorial / technical option** from `STYLE_PRESETS.md`
- **C — context-specific wildcard** designed for the actual research topic

Do not render “Option A”, “preset”, “template”, internal filenames, workflow notes, or design-process language inside the slide itself.

Each preview must look like a genuine first slide from the final presentation.

## 4.2 Style Selection

Ask the user which preview they prefer, or whether to mix specific elements.

After selection, preserve the chosen visual thesis across the full deck:

- typography
- palette
- spacing rhythm
- figure treatment
- annotation style
- chart treatment
- decorative vocabulary
- motion behavior

Do not switch to a different design system halfway through generation.

Read `STYLE_PRESETS.md` during this phase.

---

# Phase 5 — Generate the Presentation

Before generating, read:

- `viewport-base.css` — mandatory fixed-stage behavior
- `html-template.md` — HTML and controller architecture
- `STYLE_PRESETS.md` — chosen design system
- `animation-patterns.md` — motion guidance
- `RESEARCH_RULES.md` — evidence and attribution rules

## Required Output Shape

- Single HTML file for the deck
- CSS and JavaScript inline
- Local research assets may remain as relative files in an adjacent `assets/` directory
- 1920×1080 fixed slide stage
- keyboard navigation
- touch/swipe navigation when feasible
- page/progress indicator outside the slide canvas
- semantic `.slide` elements
- reduced-motion support

## Research-Specific Slide Components

Use components that communicate evidence clearly:

### Figure Slide

Include:

- the figure or faithful redraw
- a short claim-oriented title
- only the annotations needed to interpret it
- compact source/caption information

### Equation Slide

Include:

- the equation at readable scale
- variable definitions or a visual decomposition
- one explanation of what the equation means in the research story
- source pointer when the equation comes from the supplied material

### Result Slide

Include:

- the metric and experimental condition
- a comparison that preserves the original scale and meaning
- uncertainty/error bars when the source reports them
- the source pointer

### Method Diagram

Use an original explanatory diagram when it improves understanding, but never imply that a redraw is an original figure from the paper.

## Typography and Sources

Source labels are part of the scientific interface, not decoration.

- Keep source text visually subordinate but readable.
- Do not shrink citations until they become unusable.
- Use consistent source placement across slides.
- Distinguish source citations from interpretation notes.

---

# Phase 6 — Validation

A research deck passes only after **two different checks**.

## 6.1 Evidence Validation

Check:

- Every important quantitative claim is traceable.
- No citation was invented.
- Figure/table labels match the source.
- Units and sample sizes are preserved when relevant.
- Derived calculations are not presented as source-reported values.
- Interpretation is not disguised as a direct finding.
- Limitations are represented fairly.

## 6.2 Visual Validation

Render the deck and inspect it visually.

At minimum check:

- 1920×1080 authored stage remains 16:9
- no text overflow
- no card/panel overlap
- no cropped equations or figure captions
- no unreadably small citations
- no accidental page reflow
- navigation works
- screenshots look correct at a desktop viewport and at least one phone viewport where the stage should scale rather than reflow

Do not rely only on DOM `scrollHeight` checks. A layout can have no overflow and still contain overlapping panels.

If a slide fails, revise and render again.

---

# Phase 7 — Delivery

After validation:

1. Open the generated HTML in the browser when the environment allows it.
2. Report the file location and slide count.
3. State the chosen visual direction.
4. Explain navigation briefly.
5. Mention any unresolved evidence/source issue explicitly.
6. If a claim/source map was created, deliver it next to the deck.
7. Offer revisions based on scientific content, visual hierarchy, or density—not generic “make it prettier” changes.

---

# Supporting Files

| File | Purpose | When to read |
| --- | --- | --- |
| `RESEARCH_RULES.md` | claim types, citation rules, figure/table/equation integrity | evidence extraction + validation |
| `STYLE_PRESETS.md` | concrete academic visual systems | style discovery |
| `viewport-base.css` | mandatory fixed 1920×1080 stage CSS | generation |
| `html-template.md` | HTML structure and slide controller | generation |
| `animation-patterns.md` | motion patterns appropriate for research decks | generation |
| `SLIDE_SYSTEM.md` | research narrative and slide composition heuristics | narrative + generation |

## Non-Negotiable Failure Conditions

Do not deliver a deck if any of these remain unresolved:

- fabricated or guessed citation
- unsupported numerical result presented as fact
- equation altered in meaning
- figure source misrepresented
- text or chart clipped outside the slide
- overlapping slide panels
- mobile layout reflows the 16:9 research slide into a webpage

When evidence is incomplete, say so. When the layout is crowded, split the slide. When the visual idea is weak, generate a better preview before building the full deck.
