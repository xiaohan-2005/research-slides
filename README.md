# Research Slides

> **Turn papers, data and research notes into beautiful, citation-aware presentations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-111827.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-v0.1%20alpha-2563EB.svg)
![Agent-first](https://img.shields.io/badge/agent--first-SKILL.md-0F766E.svg)

Research Slides is an **agent-first skill for academic presentations**. Instead of treating a paper like generic text, it asks the agent to preserve evidence, citations, equations, figures and research structure while turning the material into a clear visual story.

## ✨ First demo

### Attention Is All You Need → research presentation

The first example turns Vaswani et al. (2017) into a citation-aware research deck using original HTML/CSS visuals rather than copied paper figures.

**[Open the demo files →](examples/attention-is-all-you-need/)**

The demo includes:

- a 12-slide research narrative
- a self-contained HTML presentation
- slide-level source mapping
- original diagrams for the Transformer and self-attention
- explicit separation between reported results and interpretation

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

### Research-first principles

- **Never invent numbers.** Reported values must be traceable to a supplied or verified source.
- **Never fabricate citations.** Unknown provenance is marked as unknown instead of guessed.
- **Figure-aware.** Figures are treated as evidence, not decoration.
- **Equation-aware.** Mathematical notation should remain mathematically faithful.
- **Show, don't tell.** Visual structure should explain the research rather than simply restyle paragraphs.
- **Progressive disclosure.** The agent loads detailed rules only when the task needs them.

## Use with a coding agent

Point a coding agent at this repository and ask it to start from [`SKILL.md`](SKILL.md).

Example:

```text
Use the research-slides skill from this repository.
Turn this paper into a 12-slide group-meeting presentation.
Keep every quantitative claim traceable to the source.
```

The core skill is designed to be readable by coding agents with repository/filesystem access. Agent-specific packaging will be added after the core workflow is stable.

## Repository map

```text
research-slides/
├── README.md
├── SKILL.md
├── RESEARCH_RULES.md
├── STYLE_PRESETS.md
├── SLIDE_SYSTEM.md
├── scripts/
└── examples/
    └── attention-is-all-you-need/
```

## Current scope — v0.1 alpha

Research Slides is currently a **research prototype**, not a finished one-command slide generator. The v0.1 goal is to make the reasoning and presentation workflow strong before adding more automation.

Current focus:

- paper → structured slide narrative
- citation-aware claim mapping
- scientific visual systems
- reproducible HTML presentations
- lightweight validation utilities

## Roadmap

- [x] Core `SKILL.md`
- [x] Research-integrity rules
- [x] Scientific slide system
- [x] First paper-to-slides demo
- [ ] PDF structure/figure extraction pipeline
- [ ] Citation verification CLI
- [ ] More academic visual systems
- [ ] Data/notebook → presentation workflow
- [ ] Agent-specific installers
- [ ] One-command HTML/PDF export

## Design philosophy

**Research clarity before decoration. Evidence before confidence. Visuals before walls of text.**

If a beautiful slide cannot tell the viewer where an important claim came from, it is not finished.

## License

MIT — see [LICENSE](LICENSE).
