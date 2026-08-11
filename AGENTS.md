# AGENTS.md

## Purpose

This repository is **Codex-first**. Its primary deliverable is a portable `research-slides` Skill that Codex can use to turn research material into evidence-grounded, citation-aware HTML presentations.

Do not add Claude Code-specific marketplace, command, or plugin packaging unless explicitly requested in a future task.

## Start Here

When working in this repository:

1. Read `SKILL.md` first.
2. Read only the supporting files needed for the current task.
3. Preserve the Skill as portable Markdown + supporting resources rather than coupling it to one proprietary command surface.

Supporting files currently include:

- `RESEARCH_RULES.md` — evidence, claims, figures, equations, and citation integrity.
- `STYLE_PRESETS.md` — visual systems for research decks.
- `SLIDE_SYSTEM.md` — research narrative and slide composition rules.
- `viewport-base.css` — mandatory 1920×1080 fixed-stage CSS.
- `examples/` — demonstrations and test cases.

## Product Direction

The project should solve this job:

> Given a paper, research notes, data, or an existing research deck, produce a clear, visually strong presentation while preserving scientific traceability.

The key differentiator is not generic slide generation. It is the combination of:

- research narrative design
- claim/source traceability
- figure- and equation-aware presentation
- fixed-stage HTML output
- visual validation

## Codex Development Rules

### 1. Prefer executable guidance over vague prose

When improving the Skill, write instructions that Codex can actually follow:

- identify inputs
- define ordered steps
- specify output artifacts
- define failure conditions
- define validation checks

Avoid advice such as “make it professional” without concrete implementation rules.

### 2. Use progressive disclosure

Keep `SKILL.md` as the workflow entry point.

Move detailed material into support files when it would otherwise make the main Skill unnecessarily large. `SKILL.md` should explicitly say when each support file must be read.

### 3. Keep the core Skill portable

Do not require Claude Code-specific commands, marketplace manifests, or `.claude-plugin` files.

Do not assume one IDE or one Codex client unless the feature truly requires it.

If a Codex-specific capability is added, document a portable fallback where practical.

### 4. Preserve scientific integrity

Never introduce fabricated citations, numbers, experimental results, equations, or figure attributions into examples or generated assets.

When a demo uses a real paper or dataset, keep a claim/source map or equivalent traceability artifact.

### 5. Treat examples as tests

Examples should exercise the Skill rather than act as decoration.

A good example should demonstrate several of the following:

- source extraction
- narrative restructuring
- equations
- figures or diagrams
- quantitative results
- citations
- limitations
- final HTML rendering

### 6. Fixed stage is non-negotiable

Generated decks use a 1920×1080 stage and scale uniformly to the viewport.

Do not convert slides into responsive webpages that reflow at mobile widths.

Use `viewport-base.css` as the canonical stage behavior.

### 7. Validate after changes

For HTML presentation changes, verify at least:

- slide count
- navigation
- 16:9 stage scaling
- no clipped content
- no panel overlap
- readable citations/source labels
- no broken local assets

For Skill changes, verify:

- YAML frontmatter remains valid
- the trigger description still matches the actual job
- every referenced support file exists
- the workflow has a clear input → process → output path
- no contradictory instructions exist across support files

## Repository Hygiene

- Keep names descriptive and stable.
- Avoid duplicate copies of large instructions unless packaging requires them.
- Prefer small scripts that validate or transform artifacts over large framework dependencies.
- Do not add a build system unless it clearly improves the Skill workflow.
- Do not add a framework just to make the demo look more sophisticated.

## Near-Term Priorities

Unless a user task overrides this order, prioritize:

1. Codex-usable Skill quality.
2. Supporting HTML architecture and validation rules.
3. Research extraction / verification utilities.
4. Strong examples that test the Skill.
5. Distribution and showcase polish only after the workflow is reliable.
