# Data Atlas Preview

## Metadata

- Slug: `data-atlas`
- Mood: analytical, structured, quantitative
- Tone: modern, evidence-forward, disciplined
- Best for: statistics, modeling, experiments, benchmarking, survey research, data-heavy technical reports
- Evidence focus: charts, uncertainty, comparisons, ablations, tables

## Visual Snapshot

A quantitative editorial system built around comparison rather than dashboards. Light stone canvas, strong numerical hierarchy, direct labels, visible baselines, restrained blue/green marks, and amber reserved for caveats or thresholds.

The slide should feel like a carefully edited data figure enlarged for presentation—not a business-intelligence screen.

## Preview Ingredients

- Background: stone `#F4F5F2`
- Ink: `#17202A`
- Primary comparison blue: `#315E8A`
- Secondary/corroborating green: `#2E7D64`
- Neutral baseline gray: `#7B8794`
- Caveat/threshold amber: `#B36A2E`
- Display: Manrope / Aptos Display / Segoe UI
- Body: IBM Plex Sans / Aptos / Segoe UI
- Technical labels and values: IBM Plex Mono / Consolas

Signature moves:

- chart-first composition;
- direct labels instead of detached legends;
- visible baseline/reference condition;
- delta annotations such as `Δ +2.04 BLEU` when the subtraction is meaningful and source-supported;
- uncertainty or interval information remains visible when reported;
- small context strip that tells the viewer metric, dataset, sample, or experimental condition.

Preferred visual families:

1. dot / dumbbell comparison;
2. line or lollipop ablation;
3. interval / error-bar plot;
4. synchronized small multiples;
5. exact-value table.

Use bars only when bar length from a meaningful zero/reference origin is the clearest encoding.

Avoid:

- KPI dashboards;
- decorative donut charts;
- unlabeled bars;
- rainbow palettes;
- giant numbers without metric and condition;
- fake precision;
- hiding uncertainty to make the chart cleaner.

## Preview Rules

- Create one real 1920×1080 title slide using actual research content.
- Hint at the data language with a restrained scale, comparison mark, or measured grid—not fake metrics.
- Keep the title itself dominant.
- Do not render template names, option labels, file paths, or workflow metadata.
- At thumbnail scale, remove any axis or note that cannot remain readable.

## Gallery Proof Rule

Show three different quantitative jobs:

1. title / measurement framing;
2. benchmark or direct comparison;
3. ablation / uncertainty / distribution.

The three thumbnails must demonstrate different analytical encodings, not three variants of the same bar chart.

After selection, read the full `design.md`.