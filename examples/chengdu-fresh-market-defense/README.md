# Competition Defense Case — Chengdu Community Fresh Market

> **食品领“鲜”，美味相约——成都市社区生鲜店消费分析及市场挖掘**

This end-to-end case turns a 100-page Chinese market-research competition paper into a 14-slide, speaker-led HTML defense deck.

<img src="preview/cover.png" width="100%" alt="Cover of the Chengdu community fresh market competition defense deck" />

## Case profile

| | |
| --- | --- |
| **Scenario** | National competition defense / 竞赛答辩 |
| **Source** | 100-page Chinese market-survey paper |
| **Output** | 14-slide standalone HTML deck |
| **Density** | Speaker-led: low text, strong visual hierarchy |
| **Visual direction** | Deep-teal fresh-market network with orange and lime evidence accents |
| **Evidence structure** | C-side consumer demand + B-side merchant supply + competition + strategy |

## Deliverables

- [`presentation.html`](output/presentation.html) — standalone deck with embedded fonts and fieldwork imagery;
- [`source-paper.pdf`](source-paper.pdf) — the original national first-prize paper supplied for this case;
- [`evidence-map.md`](analysis/evidence-map.md) — slide-by-slide claim and source mapping;
- [`validation/report.md`](validation/report.md) — evidence, structural, desktop and phone checks.

## What this case tests

This is deliberately different from the repository's technical-paper example. It exercises:

- Chinese PDF extraction across a long, mixed-format report;
- consumer and merchant survey evidence in one narrative;
- direct-labeled charts for live competition speaking;
- a custom visual system derived from the research topic;
- explicit separation of reported findings, derived values and strategic interpretation;
- fixed-stage mobile scaling without responsive slide reflow.

## Evidence issue disclosed in the deck

The source reports `157 / 160` valid B-side questionnaires. The abstract gives `98.125%`, which matches the arithmetic, while one body page states `96.25%`.

The deck uses the derived value `157 ÷ 160 = 98.125%` and visibly records the inconsistency instead of silently choosing one number.

Time-sensitive market and competitor figures are labeled as **report-period context**, not as current market facts.

## Full-deck overview

<img src="preview/contact-sheet.png" width="100%" alt="Contact sheet showing all 14 slides of the competition defense deck" />

## Open and navigate

Download or open [`output/presentation.html`](output/presentation.html) in a browser.

- `←` / `→`, `PageUp` / `PageDown`, or `Space` to navigate;
- swipe horizontally on touch devices;
- the authored 1920×1080 stage scales as one unit on narrow screens.

The source paper remains the work of its original authors and is included here as the traceable input for this research-slide case study.
