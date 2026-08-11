# Research Slides

> **Turn papers, research notes and data into evidence-grounded, citation-aware presentations with Codex.**

[![License: MIT](https://img.shields.io/badge/License-MIT-111827.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-alpha-2563EB.svg)
![Codex](https://img.shields.io/badge/Codex-Skill-0F766E.svg)

<img src="assets/demo-cover.svg" width="100%" alt="Research Slides — Attention Is All You Need example" />

**Research Slides** is a Codex-first Agent Skill for academic and technical presentations.

It does not treat a paper like generic text to summarize. It asks Codex to preserve **claims, sources, equations, figures, quantitative results and limitations** while turning the material into a clear visual story.

## Why this exists

Most AI slide workflows optimize for speed and appearance.

Research Slides adds a second requirement:

> **Important claims should remain traceable to evidence.**

```text
Paper / Notes / Data
        ↓
Evidence extraction
        ↓
Claim ledger
        ↓
Narrative design
        ↓
Visual style discovery
        ↓
1920×1080 HTML deck
        ↓
Structural + evidence + visual validation
```

## What the Skill does

- **Research narrative, not paper transcription** — reorganizes source material around the scientific question and evidence.
- **Claim-aware** — separates reported findings, derived values, interpretation and background context.
- **Citation-aware** — maps important claims, numbers, figures and equations back to their sources.
- **Figure-aware** — treats figures as evidence rather than decoration.
- **Equation-aware** — preserves mathematical meaning and distinguishes source equations from explanatory annotations.
- **Visual style discovery** — generates real slide previews before committing to a full visual system.
- **Fixed-stage HTML** — authors every deck at 1920×1080 and scales the stage instead of reflowing slides like a webpage.
- **Validation-first** — requires evidence checks and structural checks before the deck is considered complete.

## Install in Codex

Codex supports reusable Skills built around `SKILL.md` plus supporting resources. This repository is structured as one Skill bundle.

### Option A — use Codex's bundled skill installer

In Codex, ask the built-in skill installer to install this repository root as `research-slides`:

```text
$skill-installer install the skill from xiaohan-2005/research-slides using repo path "." and name "research-slides"
```

The bundled installer installs user Skills under `$CODEX_HOME/skills` (normally `~/.codex/skills`). Restart Codex if the newly installed Skill does not appear immediately.

### Option B — clone manually

```bash
git clone https://github.com/xiaohan-2005/research-slides.git ~/.codex/skills/research-slides
```

Then restart Codex.

> The repository is currently in alpha. The Skill format and workflow are usable, but the example suite and runtime validation are still being expanded.

## Use with Codex

Once installed, ask for the research task normally or explicitly reference the Skill.

Example:

```text
Use the research-slides skill.
Turn this paper into a 12-slide group-meeting presentation.
Use a speaker-led density.
Keep every important quantitative claim traceable to the source.
Show me three real title-slide style previews before building the full deck.
```

A good run should follow the phases in [`SKILL.md`](SKILL.md):

```text
0  Detect task
1  Research intake
2  Evidence extraction
3  Narrative design
4  Visual style discovery
5  Generate presentation
6  Validate evidence + rendering
7  Deliver
```

## Skill architecture

`SKILL.md` is the entry point. Detailed rules are loaded only when the task needs them.

```text
research-slides/
├── AGENTS.md
├── SKILL.md
│
├── RESEARCH_RULES.md
├── STYLE_PRESETS.md
├── SLIDE_SYSTEM.md
├── viewport-base.css
├── html-template.md
├── animation-patterns.md
│
├── scripts/
│   └── validate_slides.py
│
└── examples/
    └── attention-is-all-you-need/
        ├── README.md
        ├── slide-outline.md
        ├── citations.md
        ├── analysis/
        │   ├── claim-ledger.md
        │   └── evidence-map.md
        ├── output/
        │   └── presentation.html
        └── validation/
            └── report.md
```

### Progressive disclosure

The Skill intentionally does **not** put every rule in one giant prompt.

| File | Job |
| --- | --- |
| [`SKILL.md`](SKILL.md) | executable workflow and trigger logic |
| [`RESEARCH_RULES.md`](RESEARCH_RULES.md) | evidence, citation, figure and equation integrity |
| [`STYLE_PRESETS.md`](STYLE_PRESETS.md) | concrete academic visual systems |
| [`SLIDE_SYSTEM.md`](SLIDE_SYSTEM.md) | narrative and slide-composition heuristics |
| [`viewport-base.css`](viewport-base.css) | mandatory fixed 1920×1080 stage behavior |
| [`html-template.md`](html-template.md) | HTML/controller architecture |
| [`animation-patterns.md`](animation-patterns.md) | research-specific motion patterns |
| [`scripts/validate_slides.py`](scripts/validate_slides.py) | deterministic static checks before visual review |

## End-to-end test case

### Attention Is All You Need

The first test case uses Vaswani et al. (2017) to exercise the full workflow rather than only showing a finished deck.

It includes:

- a 12-slide research narrative;
- a claim ledger;
- a slide-level evidence map;
- source-aware equations and quantitative results;
- original explanatory HTML/CSS/SVG visuals;
- a canonical 1920×1080 output;
- a validation report that records passes, failures and pending checks.

Start here:

- [`examples/attention-is-all-you-need/README.md`](examples/attention-is-all-you-need/README.md)
- [`claim-ledger.md`](examples/attention-is-all-you-need/analysis/claim-ledger.md)
- [`evidence-map.md`](examples/attention-is-all-you-need/analysis/evidence-map.md)
- [`canonical presentation`](examples/attention-is-all-you-need/output/presentation.html)
- [`validation report`](examples/attention-is-all-you-need/validation/report.md)

Current test status:

```text
Evidence validation      PASS
Structural validation    PASS by source inspection
Rendered visual review   PENDING
Release-ready             NO
```

The example is intentionally not labeled release-ready until every slide has been inspected in a rendered browser.

## Validate a generated deck

Run the deterministic static validator before visual review:

```bash
python scripts/validate_slides.py path/to/presentation.html
```

It checks common contract failures such as:

- missing `deck-viewport` / `deck-stage`;
- wrong authored dimensions;
- missing slide elements;
- missing keyboard navigation;
- missing reduced-motion handling;
- missing local assets;
- obvious responsive slide reflow.

Passing the script does **not** prove that the deck looks correct. Rendered inspection is still required for clipping, overlap, figure legibility, equations and citations.

## Research integrity contract

Research Slides should fail safely rather than manufacture confidence.

It must not:

- invent a citation;
- invent a numerical result;
- silently change a reported value;
- alter an equation's meaning for layout convenience;
- present interpretation as a source-reported finding;
- misrepresent a redraw as an original paper figure;
- hide an unresolved provenance problem behind polished design.

When evidence is incomplete, mark it as incomplete.

## Current status

This project is an **alpha research Skill**, not a finished one-command paper-to-slides product.

Completed:

- [x] Codex-oriented `SKILL.md`
- [x] repository `AGENTS.md`
- [x] research-integrity rules
- [x] concrete visual presets
- [x] fixed 1920×1080 stage contract
- [x] HTML presentation architecture
- [x] research animation guidance
- [x] static slide validator
- [x] first traceable paper-to-deck test case

Next engineering priorities:

- [ ] browser-based visual validation automation
- [ ] PDF structure / figure extraction
- [ ] machine-readable claim/source schema
- [ ] citation verification tooling
- [ ] data / notebook → research deck workflow
- [ ] additional test cases with different research structures

## Design philosophy

**Research clarity before decoration. Evidence before confidence. Visuals before walls of text.**

A slide is not finished when it looks convincing. It is finished when the argument is clear **and** the important evidence can still be traced.

## License

MIT — see [`LICENSE`](LICENSE).
