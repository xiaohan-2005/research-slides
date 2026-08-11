# Animation Patterns for Research Slides

Use motion to explain scientific structure, not to decorate slides.

The default rule is simple:

> If an animation does not help the audience understand sequence, causality, comparison, uncertainty, or evidence, remove it.

Read this file during **Phase 5 — Generate the Presentation** after the visual direction has been selected.

---

## Motion Principles

1. **Meaning before spectacle** — Motion should reveal logic, not merely attract attention.
2. **One animated argument at a time** — Avoid multiple unrelated effects competing on one slide.
3. **Preserve the final state** — A slide must remain understandable after all animation has completed and when exported as a static image/PDF.
4. **Do not animate scientific values** in a way that temporarily shows false intermediate numbers.
5. **Do not animate axes, scales, or uncertainty deceptively.** The final chart geometry must match the source data.
6. **Respect reduced motion.** Every deck must remain usable under `prefers-reduced-motion`.
7. **Use opacity and transforms first.** Avoid expensive effects that make browser rendering unstable.

---

## Effect-to-Research-Job Guide

| Research job | Recommended motion | Avoid |
| --- | --- | --- |
| Introduce a research question | quiet fade + one focal highlight | bouncing titles, decorative particles |
| Explain a pipeline / method | ordered reveal along process direction | revealing all nodes simultaneously |
| Explain an equation | reveal semantic terms or annotations in order | changing the mathematical expression itself |
| Compare methods | reveal common baseline first, then differences | bars growing from inconsistent scales |
| Explain architecture | staged node/edge emphasis | continuous moving lines with no explanatory role |
| Present results | chart appears once, then key evidence highlight | count-up animations that obscure exact values |
| Show uncertainty | reveal interval/region with the estimate | animated uncertainty that changes width arbitrarily |
| Discuss limitations | restrained emphasis / de-emphasis | dramatic warning effects that exaggerate severity |
| Conclude | consolidate previous visual vocabulary | introducing a new animation language on the last slide |

---

## Pattern 1 — Research Reveal

Use for title slides, research questions, short claims, and interpretation statements.

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition:
    opacity 520ms cubic-bezier(.16, 1, .3, 1),
    transform 520ms cubic-bezier(.16, 1, .3, 1);
}

.slide.visible .reveal {
  opacity: 1;
  transform: translateY(0);
}

.slide.visible .reveal:nth-child(2) { transition-delay: 90ms; }
.slide.visible .reveal:nth-child(3) { transition-delay: 180ms; }
.slide.visible .reveal:nth-child(4) { transition-delay: 270ms; }
```

Use short stagger intervals. Research decks should feel controlled rather than theatrical by default.

---

## Pattern 2 — Method Sequence

Use when the order of operations is part of the scientific explanation.

Example:

```text
Input
  ↓
Representation
  ↓
Model / inference
  ↓
Prediction / result
```

Recommended behavior:

1. reveal the input
2. reveal the first transformation
3. reveal the connection
4. reveal the next component
5. leave the completed pipeline visible

```css
.method-step {
  opacity: .22;
  transition: opacity 360ms ease, transform 360ms ease;
}

.slide.visible .method-step.is-active,
.slide.visible .method-step.is-complete {
  opacity: 1;
}

.method-edge {
  transform: scaleX(0);
  transform-origin: left center;
  transition: transform 360ms ease;
}

.slide.visible .method-edge.is-complete {
  transform: scaleX(1);
}
```

Do not loop the sequence continuously. The audience needs time to inspect the final architecture.

---

## Pattern 3 — Equation Decomposition

Use when the audience needs to understand the role of terms in an equation.

**Do not rewrite the equation between animation states.** Keep one mathematically correct equation and reveal annotations around it.

Recommended sequence:

```text
full equation remains present
        ↓
highlight term A + annotation
        ↓
highlight term B + annotation
        ↓
show interpretation / consequence
```

```css
.eq-term {
  transition: color 260ms ease, background-color 260ms ease, opacity 260ms ease;
}

.eq-term.muted { opacity: .34; }
.eq-term.focus { opacity: 1; }
```

If MathJax/KaTeX is unavailable, use faithful HTML/Unicode notation or an SVG rendering. Never simplify a source equation solely to make animation easier.

---

## Pattern 4 — Evidence Highlight

Use on a figure, table, or chart after the full evidence is visible.

Good sequence:

1. show the whole figure
2. pause
3. highlight the region supporting the slide's claim
4. show one concise interpretation

```css
.evidence-focus {
  opacity: 0;
  transform: scale(.98);
  transition: opacity 320ms ease, transform 320ms ease;
}

.slide.visible .evidence-focus {
  opacity: 1;
  transform: scale(1);
}
```

Use overlays, outlines, arrows, or labels that do not hide the original values.

Never crop away contradictory or important contextual information without making the crop explicit.

---

## Pattern 5 — Comparison Reveal

For model comparisons, ablations, baselines, or before/after logic.

Recommended order:

1. reveal the comparison frame and metric
2. reveal baseline(s)
3. reveal target method
4. reveal the delta / interpretation

The chart axes and scales must be visible before values animate in.

For bar charts, the bar may animate from zero **only when zero is a meaningful axis origin and the final geometry exactly matches the data**.

Otherwise use opacity reveal rather than growth animation.

---

## Pattern 6 — Architecture Attention

Use for neural networks, graphical models, system diagrams, or process graphs.

Recommended motion:

- fade non-relevant nodes to lower opacity
- emphasize the active node/edge group
- return the full system to normal opacity when the explanation completes

```css
.arch-node,
.arch-edge {
  transition: opacity 280ms ease, filter 280ms ease, stroke-width 280ms ease;
}

.arch-dim { opacity: .22; }
.arch-focus { opacity: 1; }
```

Avoid endless edge pulses. Architecture motion should answer “where should I look now?”

---

## Pattern 7 — Uncertainty Reveal

For confidence intervals, posterior intervals, prediction bands, or error bars:

1. reveal axes and central estimate
2. reveal the uncertainty region
3. reveal the interpretation

The interval width must be fixed by the actual result. Do not animate from a narrower/wider false interval as a dramatic effect.

Use opacity or a mask that uncovers the already-correct interval geometry.

---

## Pattern 8 — Progressive Annotation

Useful for source figures that are scientifically dense.

Keep the original figure visible, then reveal annotations one by one:

- label
- arrow
- region outline
- short explanation

This is preferred to redrawing a complex source figure when a faithful redraw would risk scientific distortion.

---

## Navigation-Triggered Motion

Animations should replay when a slide becomes visible, but must not repeatedly fire because of small viewport changes.

Recommended model:

```javascript
function showSlide(index) {
  slides.forEach((slide, i) => {
    const active = i === index;
    slide.classList.toggle('active', active);
    slide.classList.toggle('visible', active);
  });
}
```

Use `.visible` as the animation trigger so it matches the fixed-stage slide architecture.

---

## Reduced Motion

The mandatory `viewport-base.css` already provides a reduced-motion baseline.

If a custom animation depends on intermediate steps for comprehension, also provide a final-state rule:

```css
@media (prefers-reduced-motion: reduce) {
  .reveal,
  .method-step,
  .evidence-focus {
    opacity: 1 !important;
    transform: none !important;
  }
}
```

The scientific meaning must not disappear when motion is disabled.

---

## Animation Failure Conditions

Revise the slide if motion:

- temporarily shows a false number or false mathematical state
- changes a chart scale during comparison
- hides source/citation information
- makes a figure harder to inspect
- loops continuously without explanatory value
- causes text, equations, or panels to move outside the 1920×1080 canvas
- prevents the final static state from communicating the argument
- becomes the most memorable part of a slide whose evidence is weak

The final question is always:

> What scientific relationship became easier to understand because of this motion?

If there is no clear answer, use a simple reveal or no animation.
