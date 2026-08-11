# Editorial Academic — Full Design System

Use after `editorial-academic` is selected in Phase 4.

Editorial Academic is a warm scholarly system for literature reviews, conceptual research, social science, policy analysis, and thesis narratives. It uses editorial pacing to improve argument flow while keeping evidence and citations explicit.

## Fixed stage

- 1920×1080
- whole-stage scaling only
- safe area: 118px horizontal, 88px top, 82px bottom

## Tokens

```css
:root {
  --ea-bg:#F3EFE6;
  --ea-paper:#FAF7F0;
  --ea-ink:#231F1B;
  --ea-soft:#4F4740;
  --ea-muted:#746A61;
  --ea-line:#D5CDC1;
  --ea-brick:#9F3F32;
  --ea-brick-soft:#EAD8D2;
  --ea-olive:#6D7458;
  --ea-olive-soft:#E3E5D8;
  --ea-display:"Cormorant Garamond","Georgia",serif;
  --ea-body:"Source Sans 3","Aptos","Segoe UI",sans-serif;
  --ea-mono:"IBM Plex Mono","Consolas",monospace;
}
```

## Typography

- hero title: 100–112px serif, 600–650
- slide statement: 62–72px serif
- quotation: 44–56px serif
- body lead: 28–31px sans
- body: 23–26px sans
- marginal/source note: 14–17px mono/sans

Use italics sparingly for emphasis or source titles, not for whole paragraphs.

## Layout grammar

Editorial Academic relies on rhythm rather than cards.

Preferred structures:

- 7/5 asymmetric columns
- large statement + narrow marginal evidence note
- figure occupying 55–65% with interpretive column
- quotation + source rail
- two-column comparison with a visible central rule

Use rules, margins, and type hierarchy to separate content. Rounded panels should be rare.

## Title slide

- large serif title with deliberate line breaks
- small contextual eyebrow above or below
- one restrained line, figure fragment, or source cue
- author/institution/date aligned to an edge, not floating in the center

## Argument slide

State the actual argument in the title. Use one supporting paragraph, excerpt, diagram, or evidence object. Avoid generic `Background`, `Discussion`, or `Conclusion` titles when a claim-oriented title is possible.

## Quotation slide

Use only source text that genuinely matters. Keep quotation short enough to read on screen and include the source adjacent to it. Do not use quotation slides as decorative breathing space.

## Figure slide

- figure remains primary evidence
- brick red may mark the point under discussion
- olive may distinguish contextual/supporting material
- do not recolor the source figure itself unless scientifically safe
- captions/source pointers stay visible

## Conceptual diagram

Prefer sparse lines, labeled relationships, and editorial annotations. No glossy icons or faux infographics.

## Comparison grammar

Use a central rule or two aligned text/figure columns. Brick can mark the key disagreement or change; olive can mark continuity/support.

## Table grammar

Tables should resemble well-edited academic tables:

- thin rules
- strong row/column hierarchy
- no full cell boxing
- 18–22px body text
- brick only for the row/cell being discussed

## Source rail

Use marginal or bottom source notes with restrained mono labels. Example:

```text
SOURCE  ·  Smith (2024), pp. 18–21  ·  Claim C07
```

## Motion

Use slow editorial reveal: opacity + 12–18px movement, 420–600ms. Reveal quotation/source together. Figures appear before interpretation annotations.

## CJK

Preferred display: `Noto Serif CJK SC`, `Source Han Serif SC`, `Songti SC`. Body: `Noto Sans CJK SC`, `Source Han Sans SC`, `Microsoft YaHei`. Keep Chinese titles spacious and avoid excessive letter spacing.

## Anti-patterns

Avoid:

- faux magazine mastheads
- script fonts
- ornate borders
- scrapbook textures
- decorative quotation marks larger than the content
- generic sepia photography
- card grids
- vintage styling that overwhelms the research

The intended result is **scholarly editorial clarity**, not magazine imitation.