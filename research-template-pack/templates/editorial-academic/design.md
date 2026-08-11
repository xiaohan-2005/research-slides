# Editorial Academic — Full Design System V2

Use only after `editorial-academic` is selected in Phase 4.

Editorial Academic is a warm scholarly system for literature reviews, conceptual research, social science, policy analysis, and thesis narratives. It uses editorial pacing to improve argument flow while keeping evidence, interpretation, and citations explicit.

The design thesis is:

> **Strong argument hierarchy, disciplined margins, and visible evidence boundaries.**

It should feel authored and scholarly—not like a lifestyle magazine or faux book spread.

---

## 1. Fixed stage

- Authored canvas: 1920×1080
- Whole-stage scaling only
- Safe area: 120px horizontal, 88px top, 82px bottom
- Source rail: reserve roughly 48–54px at bottom
- Optional marginal rail: reserve 300–360px only when the slide genuinely needs side evidence/status notes

No responsive slide reflow.

---

## 2. Core tokens

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

  --ea-display:"Cormorant Garamond","Georgia","Times New Roman",serif;
  --ea-body:"Source Sans 3","Aptos","Segoe UI",sans-serif;
  --ea-mono:"IBM Plex Mono","Cascadia Mono","Consolas",monospace;
}
```

Semantic use:

- brick = disagreement, boundary, reported-vs-not-reported distinction, or key argumentative emphasis;
- olive = continuity, supporting context, corroboration;
- ink = principal claim;
- muted brown-gray = source/provenance/context.

Do not use brick simply because a slide needs “some color.”

---

## 3. Typography hierarchy

### Hero title

```css
font-family: var(--ea-display);
font-size: 104px;
font-weight: 600;
line-height: 0.96;
letter-spacing: -0.035em;
```

Use deliberate line breaks. Two strong lines are usually better than one compressed line.

### Slide statement

```css
font-family: var(--ea-display);
font-size: 66px;
font-weight: 600;
line-height: 1.02;
letter-spacing: -0.025em;
```

### Quotation / editorial lead

```css
font-family: var(--ea-display);
font-size: 42px;
font-style: italic;
line-height: 1.2;
```

Use only when the source sentence is genuinely important.

### Body lead

28–31px.

### Body

23–26px.

### Marginal label / source marker

14–17px mono or sans.

Do not use italics for long explanatory paragraphs. Italics are a pacing tool, not the body style.

---

## 4. Editorial layout grammar

Editorial Academic relies on rhythm rather than cards.

Preferred structures:

1. 7/5 asymmetric columns;
2. 8/4 argument + margin rail;
3. large statement + narrow evidence note;
4. figure occupying 55–65% + interpretive column;
5. quotation + source rail;
6. two aligned comparison columns separated by a central rule;
7. three evidence categories separated by vertical hairlines rather than boxes.

Rounded panels should be rare.

If a slide begins to resemble a card dashboard, redesign it.

---

## 5. Margin-rail contract

Marginal notes are powerful but are also the main source of overlap failures.

When using a margin rail:

- allocate a real fixed-width rail before writing body text;
- keep body and rail in separate grid columns;
- use a visible or implied vertical rule;
- never absolutely position a note on top of the body column;
- keep each note to one label + 1–3 short lines;
- do not place more than two note groups in one rail unless the slide is reading-first.

Recommended rail width:

```text
300–360 px on the 1920×1080 authored stage
```

Suitable rail labels:

```text
REPORTED
INTERPRETATION
BACKGROUND
SOURCE
LIMITATION
```

This rail is especially useful for the research-slides evidence model.

---

## 6. Title slide

Recommended anatomy:

```text
small contextual eyebrow

LARGE SERIF TITLE
LARGE SERIF TITLE
brick hairline
short italic / quiet framing line

                                 optional restrained source cue

author / venue / year rail
```

No magazine masthead, faux issue number, decorative cover lines, or unrelated photography.

---

## 7. Argument slide

State the actual argument in the title.

Preferred composition:

```text
argument title
hairline

main explanatory column        narrow evidence-status rail

short interpretive sentence    REPORTED
                               ...
                               INTERPRETATION
                               ...

source rail
```

This structure is ideal for separating what a paper reports from what the presenter infers.

Avoid generic titles such as `Discussion` when a claim-oriented title is possible.

---

## 8. Quotation slide

Use a quotation only when its wording matters.

Rules:

- keep it short enough to read in one glance;
- source sits adjacent or immediately below;
- do not create a quotation slide just for visual breathing room;
- no giant decorative quotation marks competing with the text;
- preserve exact wording and punctuation if quoting.

If paraphrase is sufficient, use an argument slide instead.

---

## 9. Figure slide

- figure remains primary evidence;
- brick may mark the point being discussed;
- olive may mark supporting/context material;
- do not recolor the source figure if color carries scientific meaning;
- captions/source pointers stay visible;
- interpretation should be a narrow column, not a full second essay.

The figure should usually occupy more visual area than the accompanying prose.

---

## 10. Conceptual diagram

Prefer:

- sparse lines;
- labeled relationships;
- textual nodes rather than icons;
- limited color;
- editorial annotations aligned to margins.

Avoid glossy infographics, stock icons, arrows with no semantic role, and faux hand-drawn ornament.

---

## 11. Comparison grammar

Use a central rule or aligned paired columns.

Brick can mark:

- a disagreement;
- changed assumption;
- evidence boundary;
- key contrast.

Olive can mark:

- continuity;
- retained structure;
- corroborating evidence.

Do not color the entire left side red and right side green unless the evidence really has a positive/negative semantics.

---

## 12. Conclusion / synthesis grammar

Avoid a three-card summary wall.

Preferred V2 pattern:

```text
conclusion statement
short framing line
hairline

DEMONSTRATED      | MEASURED        | NOT CLAIMED
large phrase      | large phrase    | large phrase
small context     | small context   | small context

source rail
```

Use vertical hairlines rather than boxes.

This is especially useful for evidence-boundary conclusions.

---

## 13. Table grammar

Tables should resemble well-edited academic tables:

- thin rules;
- strong row/column hierarchy;
- no full cell boxing;
- 18–22px body text;
- brick only for the row/cell currently discussed;
- exact values aligned consistently.

If the table is too dense, extract the comparison needed for the slide.

---

## 14. Source rail

Recommended:

```text
SOURCE · Smith (2024), pp. 18–21 · Claim C07
```

Use muted mono or sans text with a thin rule.

The source rail is not decorative footer copy; it is part of the research interface.

---

## 15. Motion

Use slow editorial reveal:

- opacity 0 → 1;
- translateY 12–18px → 0;
- 420–600ms.

Reveal quotation and source together.

Figures appear before interpretation annotations.

Margin-rail notes may reveal after the main argument, but should never move across the body text.

---

## 16. CJK

Preferred display:

```css
"Noto Serif CJK SC","Source Han Serif SC","Songti SC","SimSun",serif
```

Preferred body:

```css
"Noto Sans CJK SC","Source Han Sans SC","Microsoft YaHei","PingFang SC",sans-serif
```

Rules:

- spacious Chinese headings;
- avoid excessive character tracking;
- no Latin-style uppercase transforms;
- use Chinese serif emphasis sparingly, not for every paragraph.

---

## 17. Gallery / thumbnail art direction

The public Gallery should prove editorial argument range.

Recommended trio:

1. title / reading frame;
2. argument with a safe fixed margin rail;
3. synthesis with hairline-separated evidence categories.

At thumbnail scale:

- shorten prose aggressively;
- remove any note that cannot remain readable;
- keep margin notes inside their rail;
- use no more than 2–3 lines per note group;
- avoid small decorative labels that become clutter.

The Gallery should look intentionally art-directed, not like a full essay shrunk to 30% size.

---

## 18. Anti-patterns

Avoid:

- faux magazine mastheads;
- script fonts;
- ornate borders;
- scrapbook textures;
- decorative giant quotation marks;
- generic sepia photography;
- floating notes without a reserved rail;
- card grids;
- vintage styling that overwhelms the research;
- paragraphs squeezed beside large titles;
- conclusion cards that all carry equal visual weight.

The intended result is:

> **Scholarly editorial clarity with explicit evidence boundaries and zero typographic collision.**