# Scientific Minimal — Full Design System V2

Use only after `scientific-minimal` is selected in Phase 4.

Scientific Minimal is a light, publication-adjacent research system for figures, equations, exact comparisons, and high-integrity scientific argument. It should feel **edited, typeset, and deliberate** rather than merely clean.

The design thesis is:

> **One scientific object at a time, given enough space to be understood.**

---

## 1. Fixed stage

- Authored canvas: 1920×1080
- Whole-stage scaling only
- Default safe area: 118px left/right, 86px top, 78px bottom
- Source rail: reserve roughly 46–54px at the bottom of the content area

Do not respond to smaller viewports by reflowing the slide into a webpage.

---

## 2. Core tokens

```css
:root {
  --sm-bg:#F8F7F2;
  --sm-paper:#FCFBF7;
  --sm-ink:#111418;
  --sm-soft:#404851;
  --sm-muted:#6B7280;
  --sm-line:#D9D7D0;

  --sm-blue:#315E8A;
  --sm-blue-soft:#EAF0F5;
  --sm-green:#2E7D64;
  --sm-green-soft:#E8F1ED;
  --sm-sand:#B38A54;
  --sm-sand-soft:#F1ECE2;

  --sm-display:"Source Serif 4","Georgia","Times New Roman",serif;
  --sm-body:"IBM Plex Sans","Aptos","Segoe UI",sans-serif;
  --sm-mono:"IBM Plex Mono","Cascadia Mono","Consolas",monospace;
  --sm-math:"STIX Two Math","Cambria Math","Times New Roman",serif;
}
```

Semantic use:

- blue = primary argument / active mechanism / principal evidence
- green = corroborating evidence / secondary process
- sand = caveat, trade-off, scaling term, or comparison that needs attention
- ink = main scientific statement
- muted slate = provenance, context, secondary explanation

Normally use only one active accent plus one secondary semantic accent on a slide.

---

## 3. Typography hierarchy

Typography carries most of the identity.

### Hero title

```css
font-family: var(--sm-display);
font-size: 100px;
font-weight: 600;
line-height: 0.98;
letter-spacing: -0.035em;
```

Use 2–3 deliberate lines maximum. Prefer manual line breaks when the title would otherwise wrap awkwardly.

### Slide statement

```css
font-family: var(--sm-display);
font-size: 62px;
font-weight: 600;
line-height: 1.03;
letter-spacing: -0.025em;
```

Preferred range: 58–68px.

### Editorial lead / interpretation

```css
font-family: var(--sm-display);
font-style: italic;
font-size: 30px;
line-height: 1.38;
color: var(--sm-soft);
```

Use sparingly. This is for one interpretive sentence, not a paragraph.

### Body lead

```css
font-family: var(--sm-body);
font-size: 29px;
line-height: 1.42;
```

### Standard body

```css
font-size: 23px;
line-height: 1.48;
```

### Technical label

```css
font-family: var(--sm-mono);
font-size: 16px;
letter-spacing: 0.09em;
text-transform: uppercase;
```

### Source rail

```css
font-family: var(--sm-body);
font-size: 15px;
line-height: 1.35;
color: var(--sm-muted);
```

Do not shrink titles to rescue crowded layouts. Rewrite, split, or remove secondary copy.

---

## 4. Layout grammar

Use a quiet 12-column conceptual grid. The audience should feel alignment, not see a dashboard grid.

Preferred structures:

- 62–72% evidence object + 28–38% interpretation;
- full-width equation + semantic annotations below;
- asymmetrical title slide with one small scientific motif;
- figure-first composition with a narrow interpretation rail;
- two-column comparison only when the scientific argument is genuinely comparative.

Avoid three equal cards as the default composition.

### White-space rule

Every slide should preserve at least one deliberately empty region. If every quadrant contains content, the slide is probably too dense for this style.

---

## 5. Title slide

Recommended anatomy:

```text
small technical kicker

LARGE SERIF TITLE
LARGE SERIF TITLE
short hairline
italic / quiet framing line

                           one restrained scientific motif

source / author rail
```

Suitable motifs:

- a two-point curve;
- a cropped axis fragment;
- a specimen outline;
- a sparse network edge;
- one equation glyph used as context.

The motif must be related to the research.

No hero photography, fake journal logo, decorative molecule wallpaper, or generic AI artwork.

---

## 6. Figure treatment

Source figures are evidence.

- Give the figure the largest visual share on the slide.
- Preserve original labels, axes, error bars, and scale.
- Use a neutral paper field if the source figure needs contrast.
- Add annotations outside the figure when possible.
- Use one blue leader line for the primary observation; sand only for caveats.
- Never recolor source data just to fit the template palette when color has scientific meaning.

A figure slide should usually have fewer than 60 words outside the figure.

---

## 7. Equation system — non-negotiable quality rule

Do **not** typeset an important equation as an ordinary text string such as:

```text
softmax(QK^T / sqrt(dk)) V
```

That is a fallback, not a finished scientific slide.

### Preferred HTML implementation: native MathML

Modern browsers can render MathML without an external dependency. Prefer semantic MathML when the environment supports it and verify the result visually.

Example structure:

```html
<math display="block" aria-label="scaled dot-product attention">
  <mrow>
    <mi>Attention</mi><mo>(</mo><mi>Q</mi><mo>,</mo><mi>K</mi><mo>,</mo><mi>V</mi><mo>)</mo>
    <mo>=</mo>
    <mi>softmax</mi><mo>(</mo>
    <mfrac>
      <mrow><mi>Q</mi><msup><mi>K</mi><mi>T</mi></msup></mrow>
      <msqrt><msub><mi>d</mi><mi>k</mi></msub></msqrt>
    </mfrac>
    <mo>)</mo><mi>V</mi>
  </mrow>
</math>
```

If MathML rendering is unavailable, use verified HTML/CSS or inline SVG math. Never knowingly ship broken radicals, superscripts, or misaligned fractions.

### Equation scale

- primary equation: approximately 52–72px visual size;
- one equation per slide whenever possible;
- preserve the complete equation in every animation state.

### Semantic annotation

Treat the equation as one visual object, then annotate 2–4 meaningful terms using hairline leaders below or beside it.

For scaled dot-product attention, a suitable mapping is:

- `QKᵀ` → compatibility;
- `√dₖ` → scale;
- `V` → weighted values.

Annotations should never collide with the equation or with one another.

### Formula QA

Before delivery, visually verify:

- fraction line alignment;
- radical coverage;
- superscript/subscript placement;
- baseline consistency;
- no fallback tofu/missing-glyph boxes;
- no annotation overlap.

---

## 8. Architecture / method diagrams

The method grammar is line-first and quiet.

- rectangular modules with 2–4px corner radius;
- thin, low-contrast borders;
- blue = active attention or main mechanism;
- green = feed-forward / corroborating path;
- sand = masked/caveat/conditional path;
- neutral blocks stay nearly paper-colored;
- repeat counts such as `×6` should be encoded with brackets or concise labels rather than drawing every repeated layer.

Use arrows only when they express actual flow.

Avoid product-UI panels, shadows, floating cards, or decorative circuitry.

---

## 9. Chart grammar

Charts should look closer to a journal figure than a dashboard.

- direct labels preferred;
- flat fills;
- hairline axes;
- sparse gridlines;
- value labels only where they support the claim;
- preserve uncertainty/error bars when reported;
- keep baseline or reference line visible when scientifically meaningful;
- no gradients, 3D, glow, drop shadows, or giant KPI tiles.

### Result composition

A strong result slide often uses:

```text
claim-oriented title

        chart / figure

one small interpretation line
source rail
```

Do not repeat the same numeric result again as a giant decorative number unless repetition genuinely improves comprehension.

---

## 10. Tables

- thin horizontal rules;
- no box around every cell;
- header in mono/small technical label;
- 18–22px body text;
- highlight only one row/column/cell group at a time;
- do not encode more than two semantic highlight colors.

If the table is unreadable at presentation scale, redesign it instead of shrinking it.

---

## 11. Source rail

Recommended pattern:

```text
SOURCE · Author et al. · §4.2 · Figure 3 · Claim C14
```

Use a single hairline above the rail. Keep it quiet, readable, and consistent across the deck.

Gallery thumbnails may abbreviate the rail to avoid unreadable micro-copy, but the final deck may not omit necessary provenance.

---

## 12. Motion

Scientific Minimal motion should almost disappear into the presentation.

Recommended:

- opacity 0 → 1;
- translateY 16–20px → 0;
- 380–520ms;
- subtle term emphasis rather than equation morphing.

For source figures: show the complete figure first, then reveal the annotation.

No bounce, elastic easing, repeated pulses, large zooms, or animated decoration.

---

## 13. CJK

Preferred display stack:

```css
"Noto Serif CJK SC","Source Han Serif SC","Songti SC","SimSun",serif
```

Preferred body stack:

```css
"Noto Sans CJK SC","Source Han Sans SC","Microsoft YaHei","PingFang SC",sans-serif
```

Rules:

- do not force Latin uppercase tracking onto Chinese;
- large Chinese titles may use 1.12–1.24 line-height;
- keep mathematical variables in the math font;
- avoid mixing multiple unrelated Chinese serif families.

---

## 14. Gallery / thumbnail art direction

The public Gallery is not a literal screenshot dump of full slides.

For each template, create three art-directed thumbnails:

1. title / thesis;
2. method / equation;
3. result / evidence.

At thumbnail scale:

- reduce secondary copy aggressively;
- keep one visual memory point per thumbnail;
- preserve typography and layout grammar;
- remove explanatory text that becomes unreadable noise;
- never allow labels or notes to collide.

The Gallery should prove the style can support different scientific jobs, not prove that a full slide can be shrunk until nobody can read it.

---

## 15. Anti-patterns

Avoid:

- dashboard layouts;
- purple/blue gradients;
- glassmorphism;
- repeated rounded-card walls;
- giant KPI numbers detached from evidence;
- formula strings typed as ordinary paragraph text;
- decorative lab photography unrelated to the source;
- faux journal mastheads;
- unreadable micro-citations;
- full-slide screenshots mechanically shrunk into gallery thumbnails.

The intended result is:

> **A scientifically edited presentation with typographic authority, high-quality mathematical composition, and generous visual restraint.**