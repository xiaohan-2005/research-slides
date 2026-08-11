# Data Atlas — Full Design System

Use after `data-atlas` is selected in Phase 4.

Data Atlas is a quantitative research system for statistics, modeling, experiments, benchmarking, and survey-heavy work. It makes the chart or table the central evidence object and keeps uncertainty, conditions, and baselines visible.

## Fixed stage

- 1920×1080
- whole-stage scaling only
- safe area: 108–116px horizontal, 82px top, 78px bottom

## Tokens

```css
:root {
  --da-bg:#F5F6F3;
  --da-paper:#FFFFFF;
  --da-ink:#17202A;
  --da-soft:#475467;
  --da-muted:#7B8794;
  --da-line:#D9DEE3;
  --da-blue:#315E8A;
  --da-blue-soft:#E8EFF5;
  --da-green:#2E7D64;
  --da-green-soft:#E6F0EC;
  --da-amber:#B36A2E;
  --da-amber-soft:#F4EADF;
  --da-red:#B85C5C;
  --da-display:"Manrope","Aptos Display","Segoe UI",sans-serif;
  --da-body:"IBM Plex Sans","Aptos","Segoe UI",sans-serif;
  --da-mono:"IBM Plex Mono","Consolas",monospace;
}
```

## Typography

- title slide: 90–104px, 650–700
- slide statement: 58–68px
- body lead: 29–31px
- chart annotation: 18–22px
- axis/ticks: 15–18px
- mono metric/condition label: 15–17px
- source label: 14–16px

## Core layout

Prefer one of four patterns:

1. 65% chart + 35% interpretation
2. full-width chart + narrow evidence rail
3. two synchronized small multiples with shared scale
4. exact-value table + one summary statement

Avoid dashboard mosaics. A slide is not a BI screen.

## Chart grammar

Primary series = blue. Supporting/positive comparison = green. Caveat, threshold, or scientifically meaningful difference = amber. Red only for genuinely adverse or failed conditions.

Rules:

- direct labels whenever possible
- preserve zero when analytically required
- preserve error bars / confidence intervals / bands
- show sample size or condition near the chart when it changes interpretation
- show baseline visibly
- no 3D, glow, gradients, pseudo-KPI tiles, decorative radial charts
- no arbitrary category colors when one ordered palette is clearer

## Quantitative callout

Large numbers are allowed only when they summarize a real metric with context.

Recommended anatomy:

```text
28.4 BLEU
WMT14 EN→DE · Transformer big
Source · Table 2
```

Never show a large number without metric, condition, and provenance.

## Table grammar

- row-first readability
- light horizontal rules
- mono or semibold numeric columns
- highlight one comparison at a time
- preserve units in header or cell
- avoid zebra striping unless the table is long

## Uncertainty grammar

Uncertainty is a first-class visual layer.

Use:

- confidence bands
- error bars
- ranges
- posterior/interval labels
- sample-size notes

Do not simplify away uncertainty just to make the chart cleaner.

## Model-comparison slide

Use shared scale and direct labels. Baseline is muted; selected/current method is blue; statistically or scientifically important contrast may be amber.

## Ablation slide

Use ordered comparisons, not a colorful matrix. Keep experimental conditions visible. If rows change more than one factor, say so on the slide.

## Source rail

Bottom rail with muted text and thin rule. Include table/figure/section or dataset pointer when possible.

## Motion

Charts appear as complete evidence first; annotations enter second. Avoid animated bar growth when the visual origin is not meaningful. Use opacity reveal instead.

## CJK

Use `Noto Sans CJK SC` / `Source Han Sans SC` / `Microsoft YaHei` for Chinese body and display; keep numerals/metrics in the Latin/mono stack when appropriate.

## Anti-patterns

Avoid:

- executive KPI dashboard cards
- pie/donut charts for easy-to-compare values
- rainbow categorical palettes
- fake precision
- hidden uncertainty
- decorative axes
- oversized numbers replacing the actual distribution or comparison

The intended result is **data storytelling without data simplification**.