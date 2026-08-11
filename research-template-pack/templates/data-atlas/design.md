# Data Atlas — Full Design System V2

Use only after `data-atlas` is selected in Phase 4.

Data Atlas is a quantitative research system for statistics, modeling, experiments, benchmarking, survey work, and data-heavy technical reports. It treats the chart, interval, table, or distribution as the primary evidence object.

The design thesis is:

> **Show the comparison structure first; let the number inherit meaning from context.**

A Data Atlas slide should resemble an edited scientific figure enlarged for presentation—not a BI dashboard.

---

## 1. Fixed stage

- Authored canvas: 1920×1080
- Whole-stage scaling only
- Safe area: 112px horizontal, 82px top, 78px bottom
- Source/context rail: reserve 46–54px at the bottom

No responsive slide reflow.

---

## 2. Core tokens

```css
:root {
  --da-bg:#F4F5F2;
  --da-paper:#FFFFFF;
  --da-ink:#17202A;
  --da-soft:#475467;
  --da-muted:#7B8794;
  --da-line:#D7DCE0;
  --da-grid:#E1E5E8;

  --da-blue:#315E8A;
  --da-blue-soft:#E7EEF4;
  --da-green:#2E7D64;
  --da-green-soft:#E6F0EC;
  --da-amber:#B36A2E;
  --da-amber-soft:#F4EADF;
  --da-red:#B85C5C;

  --da-display:"Manrope","Aptos Display","Segoe UI",sans-serif;
  --da-body:"IBM Plex Sans","Aptos","Segoe UI",sans-serif;
  --da-mono:"IBM Plex Mono","Cascadia Mono","Consolas",monospace;
}
```

Semantic use:

- blue = primary/current method or main analytical series;
- green = corroborating result / alternative that also matters;
- neutral gray = baseline, historical reference, or comparison condition;
- amber = threshold, caveat, sensitivity, or scientifically important contrast;
- red = genuinely adverse/failing state only.

Never assign colors merely to make a chart more colorful.

---

## 3. Typography

### Hero title

```css
font-size: 96px;
font-weight: 700;
line-height: 0.98;
letter-spacing: -0.04em;
```

### Slide statement

```css
font-size: 62px;
font-weight: 700;
line-height: 1.03;
letter-spacing: -0.03em;
```

### Body lead

```css
font-size: 29px;
line-height: 1.42;
```

### Chart annotation

18–22px.

### Axis / tick

15–18px.

### Metric / condition label

15–17px mono.

### Source rail

14–16px.

Do not use tiny typography to preserve an overcomplicated chart. Reduce the chart complexity instead.

---

## 4. Layout grammar

Preferred patterns:

1. **65% chart + 35% interpretation**
2. **full-width chart + narrow evidence/context rail**
3. **two synchronized small multiples with shared scale**
4. **exact-value table + one summary statement**
5. **one direct comparison + delta annotation**

Avoid dashboard mosaics. A slide is not a collection of widgets.

### Context strip

Every quantitative slide should make the following findable when relevant:

- metric;
- dataset/sample;
- condition/model version;
- baseline/reference;
- uncertainty definition;
- source pointer.

This context should be compact, not repeated in giant text.

---

## 5. Chart-family priority

Choose the encoding that best matches the analytical question.

### A. Dot / dumbbell plot — preferred for direct comparison

Use when comparing two or a few values on one shared scale.

Why it is preferred:

- preserves the scale;
- makes the difference visible;
- avoids oversized bars when zero is not the analytical point;
- supports direct labels naturally.

Recommended anatomy:

```text
baseline ●────────────● current
         26.36        28.40

Δ +2.04 BLEU
```

Only compute/display the delta when the arithmetic is correct and meaningful.

### B. Line / lollipop plot — preferred for ablation sequences

Use when x has a meaningful order such as:

- head count;
- model width;
- training step;
- regularization strength;
- sample size.

Show exact values near important points. Highlight the selected/base condition, but do not imply monotonicity when the data does not support it.

### C. Interval / error-bar plot — preferred for uncertainty

Use for:

- confidence intervals;
- credible intervals;
- standard errors;
- bootstrap ranges;
- repeated-run variability.

Never remove uncertainty merely because it makes the slide busier.

### D. Small multiples

Use when the audience must compare the same measure across datasets, subgroups, time windows, or methods.

Requirements:

- shared scales whenever comparisons depend on scale;
- consistent annotation positions;
- minimal repeated labels.

### E. Table

Use when exact values matter more than shape.

### F. Bar chart

Bars are allowed when:

- length from zero is genuinely meaningful;
- category comparison is easier with bars than dots;
- the axis origin does not distort interpretation.

Do not default to bars merely because values exist.

---

## 6. Direct-label grammar

Prefer direct labeling over legends.

Good:

```text
26.36  ConvS2S ensemble      ●
28.40  Transformer big                      ●
```

Less desirable:

- color legend in a distant corner;
- unlabeled bars requiring visual cross-reference;
- legend categories named `Series 1`, `Series 2`.

Labels should sit close to the marks they describe without colliding.

---

## 7. Baseline / reference grammar

A comparison is incomplete if the viewer cannot tell what the current value is being compared against.

Use one of:

- muted baseline point/line;
- explicit reference line;
- before/after pair;
- benchmark band;
- named control condition.

Do not visually hide the baseline just to make the current method appear stronger.

---

## 8. Delta annotations

A delta may be shown when:

- both values share the same metric and condition;
- the subtraction/ratio is mathematically meaningful;
- the source values are traceable;
- the computation is simple enough to verify.

Examples:

```text
Δ +2.04 BLEU
+8.2 percentage points
0.7× training time
```

Avoid ambiguous percent-change language. Distinguish percentage points from percent change.

Derived values should be marked as derived when needed by the evidence model.

---

## 9. Uncertainty is first-class

When the source reports uncertainty, preserve it visually.

Allowed forms:

- confidence bands;
- error bars;
- ranges;
- posterior intervals;
- violin/box summaries when distribution shape matters;
- repeated-run dots.

Include the uncertainty definition when it is not obvious.

Do not show a single crisp point estimate when the source's scientific conclusion depends on its interval.

---

## 10. Quantitative callouts

Large numbers are allowed only when they summarize a real metric with context.

Correct anatomy:

```text
28.4 BLEU
WMT14 EN→DE · Transformer big
Source · Table 2
```

Wrong anatomy:

```text
28.4
```

with no metric, condition, or provenance.

A callout should support a chart or argument, not replace the distribution/comparison that gives the number meaning.

---

## 11. Ablation grammar

Ablation slides should answer:

> What changed, what stayed comparable, and what outcome moved?

Rules:

- x-order must correspond to a real ordered condition when using a line;
- show selected/base condition explicitly;
- use the same scale across compared panels;
- state when multiple factors changed at once;
- do not use a heatmap simply because the table is rectangular;
- avoid a different accent color for every setting.

For the Attention head-count example, a line/lollipop view is preferred over five decorative bars because the x values are ordered and the point of the slide is non-monotonic behavior.

---

## 12. Table grammar

- row-first readability;
- thin horizontal rules;
- numeric columns aligned consistently;
- mono or tabular numerals for exact values;
- highlight one analytical comparison at a time;
- preserve units in header or cells;
- avoid zebra striping unless the table is genuinely long.

A dense table should be cropped/redesigned into the evidence needed for the slide rather than simply reduced in size.

---

## 13. Axes and scales

- axis lines: quiet gray;
- grid lines: sparse, low contrast;
- zero line emphasized only when scientifically meaningful;
- do not truncate an axis solely to exaggerate a difference;
- if a non-zero domain is analytically appropriate, make the scale legible and avoid bar encodings that imply zero-based length.

Use shared scales for comparisons whenever scale equality is part of the argument.

---

## 14. Statistical integrity

Never imply statistical significance through styling alone.

If significance is reported, show the actual convention/source-supported annotation.

Do not invent:

- p-values;
- confidence intervals;
- effect sizes;
- sample sizes;
- error bars;
- significance stars.

If the source reports only point estimates, the slide should not fabricate uncertainty graphics.

---

## 15. Motion

Charts should appear as complete evidence first; annotations enter second.

Recommended:

- opacity reveal;
- subtle highlight of selected mark;
- annotation leader entering after the plot is visible.

Avoid animated bar growth when zero is not the meaningful origin. Avoid counting-number animations that imply precision theatre.

---

## 16. Gallery / thumbnail art direction

The public Gallery should prove analytical range.

For each Data Atlas gallery trio, prefer:

1. title / measurement framing;
2. benchmark using a dot/dumbbell/shared scale;
3. ablation, interval, or distribution using a different chart family.

At thumbnail scale:

- keep exact values only where legible;
- remove redundant axis labels;
- preserve one visible scale/baseline cue;
- avoid tiny legends;
- do not use three near-identical bar charts.

---

## 17. CJK

Use:

```css
"Noto Sans CJK SC","Source Han Sans SC","Microsoft YaHei","PingFang SC",sans-serif
```

Keep numerals/metrics in the Latin or mono stack when that improves tabular alignment.

---

## 18. Anti-patterns

Avoid:

- executive KPI dashboards;
- card mosaics;
- donut/pie charts for easy-to-compare values;
- rainbow categorical palettes;
- giant metric numbers with no condition;
- hidden uncertainty;
- fake precision;
- decorative axes;
- ambiguous percent changes;
- three different chart types when one shared comparison would be clearer;
- oversized bars when a dot/dumbbell plot is more honest.

The intended result is:

> **Data storytelling with visible scale, context, baseline, and uncertainty—not data simplification.**