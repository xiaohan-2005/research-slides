# Research Template Pack

Distinctive visual systems for `research-slides`, loaded progressively so Codex does not consume every full design specification up front.

## Read Order

1. Read `research-template-pack/selection-index.json` first.
2. Shortlist candidates using metadata only:
   - `mood`
   - `tone`
   - `best_for`
   - `avoid_for`
   - `formality`
   - `density`
   - `scheme`
   - `evidence_focus`
3. For title-slide style discovery, read only the shortlisted candidates' `preview.md` files.
4. Generate three real 1920×1080 title-slide previews using the user's actual deck title/subtitle/context.
5. After the user chooses a direction, read exactly that template's full `design.md`.
6. Do not read every `design.md` in the pack.

## Default Preview Mix

Use three genuinely different directions:

- one safe academic option from `STYLE_PRESETS.md`;
- one distinctive option from this template pack;
- one wildcard that is either another shortlisted template or a custom design derived from the research topic.

The wildcard must still respect research integrity, fixed-stage behavior, and anti-AI-slop rules.

## Preview Contract

A preview is a real title slide, not a selection card.

Never place internal workflow text inside the rendered slide:

- no `Option A/B/C`;
- no `preview`;
- no template name or slug;
- no file paths;
- no user requirement notes;
- no `generated from` labels;
- no internal metadata.

Visible text should come from real deck content such as title, subtitle, author, date, venue, paper/project name, or a genuine contextual phrase.

## Final-Deck Contract

After selection:

- preserve the chosen typography, palette, spacing rhythm, figure treatment, annotation grammar, chart language, and decorative vocabulary;
- generate on the fixed 1920×1080 stage defined by `viewport-base.css`;
- use the full `design.md` as a design recipe, not content to copy;
- let research content override decorative conventions when the two conflict;
- keep citations/source labels readable and structurally consistent;
- verify screenshots for text clipping and panel overlap.

## Current Templates

- `neural-lab` — dark computational system for AI/ML, systems, architecture, equations, and ablations.
- `scientific-minimal` — publication-adjacent light system for figures, equations, experiments, and formal defenses.
- `data-atlas` — quantitative system for statistics, benchmarking, uncertainty, comparisons, and data-heavy reports.
- `editorial-academic` — warm scholarly system for literature reviews, conceptual argument, policy, and thesis narratives.

These templates are intentionally different in **visual grammar**, not merely accent color.

The public README gallery uses separate assets under `assets/style-gallery/` so the human-facing visual library does not need to be loaded into Codex during normal Skill execution.
