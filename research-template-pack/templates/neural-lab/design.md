# Neural Lab — Full Design System

Use this file only after `neural-lab` has been selected during Phase 4 of `SKILL.md`.

Neural Lab is a dark computational research system for AI, machine learning, algorithms, and systems presentations. It should feel like a serious model-analysis environment: precise, controlled, technical, and evidence-led.

It must **not** look like a gaming UI, crypto dashboard, cyberpunk poster, or generic dark SaaS landing page.

---

# 1. Visual Thesis

The visual thesis is:

> **Scientific signals moving through a precise dark research field.**

The slide should feel as if the audience is inspecting a model, an experiment, or an argument—not operating an app.

The system is built from five ideas:

1. a deep navy research field;
2. strong typographic hierarchy;
3. thin structural lines;
4. cyan for model/logic flow;
5. amber for evidence/comparison emphasis.

Everything else stays quiet.

---

# 2. Fixed-Stage Contract

Every slide is authored at exactly:

```text
1920 × 1080
```

Use the repository fixed-stage architecture:

```html
<div class="deck-viewport">
  <main class="deck-stage">
    <section class="slide active visible">...</section>
  </main>
</div>
```

Do not convert this design to responsive page reflow.

The full stage scales uniformly to the browser viewport.

Use `viewport-base.css` as the canonical stage behavior.

---

# 3. Design Tokens

Use these values as the default design system.

```css
:root {
  /* canvas */
  --nl-bg: #08111C;
  --nl-bg-deep: #050B12;
  --nl-surface: #101B2A;
  --nl-surface-2: #152235;

  /* text */
  --nl-text: #F4F7FA;
  --nl-text-soft: #CAD5DF;
  --nl-muted: #91A1B2;
  --nl-muted-2: #657789;

  /* structure */
  --nl-line: #26384A;
  --nl-line-soft: rgba(145, 161, 178, 0.18);

  /* semantic accents */
  --nl-cyan: #53D6C5;
  --nl-cyan-soft: rgba(83, 214, 197, 0.14);
  --nl-amber: #F2B84B;
  --nl-amber-soft: rgba(242, 184, 75, 0.14);

  /* caution / negative only when scientifically meaningful */
  --nl-red: #E87979;

  /* typography */
  --nl-display: "Space Grotesk", "Aptos Display", "Segoe UI", sans-serif;
  --nl-body: "IBM Plex Sans", "Aptos", "Segoe UI", sans-serif;
  --nl-mono: "IBM Plex Mono", "Cascadia Mono", "Consolas", monospace;
}
```

## Accent semantics

Do not choose accent colors arbitrarily.

- **cyan** = architecture, dependency, method flow, active concept, selected model path;
- **amber** = result emphasis, baseline difference, evidence that supports the main claim;
- **red** = only for genuinely adverse/failing/negative scientific states;
- **white** = primary argument;
- **muted gray-blue** = context, metadata, secondary explanation.

Never use more than two active accent colors on the same slide unless the underlying data itself requires more categories.

---

# 4. Typography System

Typography should provide most of the visual hierarchy.

## 4.1 Latin typography

### Hero title

```css
font-family: var(--nl-display);
font-size: 104px;
font-weight: 650;
line-height: 0.98;
letter-spacing: -0.045em;
```

Use for title slides only.

Recommended maximum visible lines: **3**.

### Slide statement title

```css
font-family: var(--nl-display);
font-size: 66px;
font-weight: 650;
line-height: 1.04;
letter-spacing: -0.035em;
```

Preferred range: 58–72px.

Do not shrink below 54px just to fit a bad title. Rewrite the title.

### Section / transition title

```css
font-size: 80px;
font-weight: 650;
line-height: 1.0;
```

### Body lead

```css
font-family: var(--nl-body);
font-size: 31px;
font-weight: 400;
line-height: 1.42;
```

### Standard body

```css
font-size: 25px;
line-height: 1.48;
```

### Compact analytical body

```css
font-size: 21px;
line-height: 1.45;
```

Use only for reading-first decks or dense result slides.

### Technical label

```css
font-family: var(--nl-mono);
font-size: 17px;
font-weight: 500;
letter-spacing: 0.08em;
text-transform: uppercase;
```

### Source label

```css
font-family: var(--nl-body);
font-size: 15px;
line-height: 1.35;
color: var(--nl-muted);
```

Do not reduce source labels below 14px on the authored 1920×1080 stage.

## 4.2 Chinese / CJK typography

When the deck contains Chinese, Japanese, or Korean text:

Preferred Chinese display/body stack:

```css
font-family:
  "Noto Sans CJK SC",
  "Source Han Sans SC",
  "Microsoft YaHei",
  "PingFang SC",
  sans-serif;
```

For a more editorial Chinese title, if available:

```css
font-family:
  "Noto Serif CJK SC",
  "Source Han Serif SC",
  "Songti SC",
  "SimSun",
  serif;
```

Rules:

- do not apply Latin-style uppercase transforms to CJK;
- use `letter-spacing: 0` or very small positive tracking;
- allow 1.15–1.3 line-height for large Chinese titles;
- do not mix three unrelated Chinese fonts on one slide;
- preserve mathematical Latin/Greek variables in their mathematical font.

---

# 5. Spatial System

## 5.1 Global safe area

Use these stage margins by default:

```text
left/right: 112 px
top:        84 px
bottom:     78 px
```

The source strip may occupy the bottom 42–52px of the content area.

## 5.2 Grid

Use a 12-column conceptual grid.

Recommended content width:

```text
1696 px
```

Recommended column gap:

```text
24–32 px
```

Do not visibly draw the full grid. The grid should be felt through alignment.

## 5.3 Spacing scale

Prefer the following rhythm:

```text
8
12
16
24
32
48
64
88
120
```

Use large jumps between narrative layers rather than many tiny gaps.

## 5.4 Density

Speaker-led:

- one primary evidence object;
- one supporting explanation block;
- 2–4 short annotations maximum;
- generous empty regions.

Reading-first:

- one primary evidence object plus compact supporting detail;
- small multiples allowed if each remains readable;
- tables may be denser, but source text must remain legible.

---

# 6. Surface Grammar

Neural Lab may use panels, but panels must behave like **scientific fields**, not UI cards.

## Primary surface

```css
background: var(--nl-surface);
border: 1px solid var(--nl-line);
border-radius: 16px;
```

Use only when it helps separate a diagram/table/result from the background.

## Rules

- prefer one or two large surfaces over many small cards;
- avoid identical card grids;
- no glossy glassmorphism;
- no large blurred shadows;
- no gradient border effects;
- rounded corners should usually be 12–18px, never pill-shaped for major content containers.

---

# 7. Title-Slide Anatomy

The title slide should establish the technical identity without looking like a product landing page.

Recommended composition:

```text
┌───────────────────────────────────────────────────────────┐
│ small research context / venue                            │
│                                                           │
│ LARGE TITLE                              model geometry    │
│ LARGE TITLE                              / signal field    │
│                                                           │
│ subtitle / one-line research framing                      │
│                                                           │
│ authors · institution · date                              │
└───────────────────────────────────────────────────────────┘
```

## Title-slide rules

- title occupies roughly 50–62% of usable width;
- one diagrammatic visual may occupy the opposite region;
- diagram should hint at the topic, not explain the whole method;
- no CTA buttons;
- no fake navigation tabs;
- no metrics unless the user explicitly wants a result-first title slide;
- no visible words such as `Neural Lab`, `template`, `preview`, or `Option B`.

---

# 8. Statement / Problem Slide

Use for research motivation, bottlenecks, hypotheses, or central questions.

Preferred pattern:

```text
kicker / context

large claim-oriented title

visual dependency / simple comparison / one evidence cue

short interpretation
source
```

Do not use generic titles like `Background` if the actual claim can be stated.

Better:

> Sequential computation limits parallelism.

Worse:

> Background

---

# 9. Architecture Diagram Grammar

Architecture diagrams are a signature Neural Lab component.

## Nodes

Default node:

```css
background: #101B2A;
border: 1px solid #365069;
border-radius: 12px;
color: #E7EEF5;
```

Active / explained node:

```css
border-color: var(--nl-cyan);
background: var(--nl-cyan-soft);
```

Evidence/result node:

```css
border-color: var(--nl-amber);
background: var(--nl-amber-soft);
```

## Edges

Normal edge:

```css
stroke: #426079;
stroke-width: 2;
opacity: 0.65;
```

Active explanation edge:

```css
stroke: var(--nl-cyan);
stroke-width: 3;
opacity: 1;
```

## Labels

Use mono labels at 16–19px for:

- tensor dimensions;
- layer names;
- model stages;
- experiment identifiers.

Use normal body font for explanatory annotations.

## Architecture rules

- flow direction must be obvious;
- keep arrows orthogonal or gently diagonal where possible;
- use whitespace between subsystems;
- repeated blocks should visually encode repetition instead of literally drawing dozens of tiny layers;
- never use random node-glow decoration;
- do not animate edges continuously.

---

# 10. Equation Grammar

Equations should be treated as first-class scientific objects.

## Main equation

Recommended size:

```text
48–68 px equivalent
```

depending on complexity.

Place directly on the canvas or on an almost-flat scientific surface.

Do not put equations in bright rounded cards.

## Equation decomposition

Use semantic highlighting:

- current term: cyan;
- comparison/evidence term: amber;
- inactive terms: muted but still readable.

Never modify the equation itself between animation states.

Use callout annotations around the equation.

Example anatomy:

```text
            compatibility
                 ↓
softmax(QKᵀ / √dₖ) V
        ↑             ↑
      scaling      values
```

## Equation source

If the equation is from a paper, include the source pointer in the source strip.

---

# 11. Figure Grammar

Research figures are evidence, not decoration.

## For source figures

- keep the original figure visually dominant;
- place on a neutral surface if contrast is needed;
- do not recolor source pixels unless the user asks and scientific meaning remains intact;
- use cyan/amber overlays only as annotations outside or on top of the figure;
- retain enough context that the highlighted region is not misleading.

## For faithful redraws

Use the Neural Lab visual system, but mark provenance clearly:

```text
Original explanatory redraw based on §3.2 / Figure 1
```

or equivalent wording appropriate to the source.

Do not imply that a redraw is an original source figure.

---

# 12. Chart Grammar

Charts must prioritize exact comparison.

## Default chart palette

```text
primary / current method: cyan
baseline / neutral: muted blue-gray
important comparison: amber
negative/failure only: muted red
```

## Axes

- axis lines: `#365069`;
- grid lines: `rgba(145,161,178,0.14)`;
- tick labels: 16–18px;
- direct labels preferred over legends when practical.

## Bar charts

- use flat fills;
- no gradients;
- no 3D;
- no decorative shadows;
- bars may animate from zero only when zero is scientifically meaningful;
- otherwise use opacity reveal.

## Line charts

- 2–3px primary stroke;
- subdued comparison strokes;
- uncertainty bands should be visible if reported;
- markers only when individual observations matter.

## Tables

Use tables for exact values when a chart would hide precision.

Header:

```css
font-family: var(--nl-mono);
font-size: 16px;
color: var(--nl-muted);
text-transform: uppercase;
```

Rows:

- 18–22px text;
- thin horizontal separators;
- avoid boxed cell borders;
- highlight only the cells necessary to support the slide claim.

---

# 13. Result-Slide Anatomy

Recommended layout:

```text
claim-oriented title

┌──────────────────────────────┬──────────────────────────┐
│                              │ experiment context       │
│  main chart / comparison     │ metric / dataset         │
│                              │ one short interpretation │
└──────────────────────────────┴──────────────────────────┘

source strip
```

The chart should normally occupy 55–72% of usable width.

Do not replace a meaningful plot with giant decorative KPI numbers.

---

# 14. Ablation / Comparison Grammar

Ablation slides need restraint because they become dense quickly.

Preferred strategies:

1. one highlighted table row/column plus interpretation;
2. small multiple charts with shared axes;
3. baseline → intervention → consequence sequence;
4. direct delta annotations.

Use amber for the evidence being discussed.

Do not color every row differently.

---

# 15. Method / Pipeline Grammar

Pipeline slides should answer:

> What happens, in what order, and why?

Use a dominant left-to-right or top-to-bottom flow.

Recommended node widths:

```text
220–340 px
```

Recommended vertical node height:

```text
80–120 px
```

Use cyan for the active method path.

Use small mono tags for:

- input dimension;
- dataset split;
- model stage;
- iteration number;
- experimental condition.

Avoid decorative arrows with no semantic destination.

---

# 16. Source / Evidence Strip

Source information is part of the interface.

Recommended structure:

```text
SOURCE  ·  Vaswani et al. (2017)  ·  §3.2.1  ·  Eq. (1)  ·  Claim C06
```

or a shorter equivalent.

Style:

```css
font-family: var(--nl-body);
font-size: 15px;
color: var(--nl-muted);
border-top: 1px solid var(--nl-line-soft);
padding-top: 12px;
```

Do not use cyan for every source label. Keep citations quiet.

Interpretation notes should be visibly distinguishable from source labels.

---

# 17. Decorative Vocabulary

Decoration must reinforce the idea of a computational research field.

Allowed:

- thin coordinate/grid fragments;
- sparse node/edge geometry;
- short cyan signal traces;
- subtle rectangular framing lines;
- small mono identifiers;
- low-opacity tensor / matrix notation used only when topic-relevant.

Not allowed:

- random particles;
- holographic glow clouds;
- giant neon rings;
- fake terminal windows;
- binary rain;
- circuit-board wallpaper;
- arbitrary gradient blobs;
- decorative code that is not part of the research.

---

# 18. Motion System

Read `animation-patterns.md` for global research motion rules.

Neural Lab should favor:

### Research reveal

```text
opacity 0 → 1
translateY 18–24px → 0
420–560ms
```

### Architecture build

- reveal nodes in causal/process order;
- reveal connecting edges after their source node;
- leave the final full architecture visible.

### Evidence reveal

- show the whole chart/figure first;
- then reveal the cyan/amber evidence annotation;
- never hide contradictory context.

### Equation reveal

- full equation remains visible;
- focus individual terms with opacity/color changes;
- no equation morphing.

Avoid:

- bounce;
- elastic easing;
- repeated pulse loops;
- large zoom-in effects;
- animation that competes with data reading.

---

# 19. Typical Slide Families

A complete Neural Lab deck should vary composition across the narrative while retaining one design system.

Useful families:

1. **Title** — strong statement + restrained model geometry.
2. **Problem** — one bottleneck / before-state visualization.
3. **Core idea** — statement + conceptual diagram.
4. **Architecture** — system diagram dominates.
5. **Equation** — mathematical object + annotations.
6. **Mechanism** — ordered process visualization.
7. **Result** — chart/table dominates.
8. **Ablation** — exact comparison and interpretation.
9. **Limitations** — calm analytical layout, not warning theater.
10. **Conclusion** — synthesis using existing visual vocabulary.

Do not use the same 3-card grid for all ten families.

---

# 20. Anti-AI-Slop Rules

Neural Lab fails visually when it resembles generic AI-generated slideware.

Avoid:

- purple-to-blue gradients;
- glass cards everywhere;
- identical rounded cards in 3-column grids;
- huge decorative icons;
- generic robot/brain imagery;
- glowing chip illustrations;
- random hexagons;
- meaningless `01 / 02 / 03` labels;
- oversized dashboard metrics replacing evidence;
- fake product UI controls inside research slides;
- generic “futuristic” imagery unrelated to the actual method.

A slide should look designed around **this specific research argument**.

---

# 21. Scientific Integrity Overrides Design

Design rules are subordinate to evidence integrity.

Always preserve:

- exact reported values;
- units;
- metric definitions;
- axes/scales;
- equation meaning;
- uncertainty when reported;
- source attribution;
- distinction between reported finding and interpretation.

If the design would require scientific distortion, change the design.

---

# 22. Implementation Checklist

Before finalizing a Neural Lab deck, verify:

- [ ] fixed 1920×1080 stage;
- [ ] title typography uses a consistent scale;
- [ ] body text is not undersized;
- [ ] cyan consistently means logic/model flow;
- [ ] amber consistently means evidence/comparison;
- [ ] no more than two active accents on a normal slide;
- [ ] architecture diagrams have clear flow direction;
- [ ] equations are exact and readable;
- [ ] charts preserve scales and labels;
- [ ] source strips are readable;
- [ ] source figures are not visually misrepresented;
- [ ] no generic dashboard-card wall;
- [ ] no gratuitous neon/cyberpunk decoration;
- [ ] reduced-motion mode preserves meaning;
- [ ] screenshots show no clipping or panel overlap.

The intended result is not “a cool dark deck.”

It is:

> **a rigorous AI research presentation with a distinctive computational visual language.**
