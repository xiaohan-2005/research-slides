# Research Slides

> **Turn papers, data and research notes into beautiful, citation-aware presentations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-111827.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-v0.1%20alpha-2563EB.svg)
![Agent-first](https://img.shields.io/badge/agent--first-SKILL.md-0F766E.svg)

<img src="assets/demo-cover.svg" width="100%" />

## 🚀 Live Demo

### Attention Is All You Need → research presentation

A 12-slide visual walkthrough of the Transformer paper.

**[Open Transformer Demo](docs/demo.html)**

The demo includes:

- a research narrative instead of a paper summary
- original HTML/CSS scientific visuals
- slide-level source mapping
- equation-aware explanations
- explicit separation between reported results and interpretation

## What is Research Slides?

Research Slides is an **agent-first skill for academic presentations**. Instead of treating a paper like generic text, it asks the agent to preserve evidence, citations, equations, figures and research structure while turning the material into a clear visual story.

## What makes this different?

Most AI slide tools optimize for **speed and appearance**. Research Slides also optimizes for **traceability**.

```text
Paper / Notes / Data
        ↓
   Understand
        ↓
 Verify claims & sources
        ↓
  Design the narrative
        ↓
 Build citation-aware slides
        ↓
       Review
```

## Research-first principles

- **Never invent numbers.** Reported values must be traceable to a supplied or verified source.
- **Never fabricate citations.** Unknown provenance is marked as unknown instead of guessed.
- **Figure-aware.** Figures are treated as evidence, not decoration.
- **Equation-aware.** Mathematical notation should remain mathematically faithful.
- **Show, don't tell.** Visual structure should explain research rather than simply restyle paragraphs.
- **Progressive disclosure.** The agent loads detailed rules only when the task needs them.

## Use with a coding agent

Start from [`SKILL.md`](SKILL.md).

Example:

```text
Use the research-slides skill from this repository.
Turn this paper into a 12-slide group-meeting presentation.
Keep every quantitative claim traceable to the source.
```

## Repository map

```text
research-slides/
├── SKILL.md
├── RESEARCH_RULES.md
├── STYLE_PRESETS.md
├── SLIDE_SYSTEM.md
├── docs/
│   └── demo.html
└── examples/
    └── attention-is-all-you-need/
        └── presentation.html
```

## Roadmap

- [x] Core `SKILL.md`
- [x] Research-integrity rules
- [x] Scientific slide system
- [x] First paper-to-slides demo
- [x] Online demo entry
- [ ] PDF structure/figure extraction pipeline
- [ ] Citation verification CLI
- [ ] More academic visual systems
- [ ] Data/notebook → presentation workflow

## Design philosophy

**Research clarity before decoration. Evidence before confidence. Visuals before walls of text.**

If a beautiful slide cannot tell the viewer where an important claim came from, it is not finished.

## License

MIT — see [LICENSE](LICENSE).
