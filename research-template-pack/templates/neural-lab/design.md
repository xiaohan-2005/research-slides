# Neural Lab Design System

## Concept

Neural Lab is a computational research visual system for AI and machine learning presentations.

The goal is not to imitate a futuristic interface. It should feel like a serious research environment: precise, technical, and evidence-oriented.

Reference feeling:

- ML conference keynote
- scientific visualization system
- advanced research notebook
- model analysis environment

Avoid:

- gaming aesthetics
- excessive neon
- cyberpunk decoration
- dashboard card walls

---

## Canvas

Fixed stage:

```text
1920 × 1080
```

Background:

```css
--bg: #08111C;
--surface: #101B2A;
--surface-light: #172536;
```

The entire deck uses one dark scientific canvas.

---

## Typography

### Display

Font:

```text
Space Grotesk
```

Weight:

```text
600 / 700
```

Use for:

- research statements
- section titles
- major conclusions

### Body

Font:

```text
IBM Plex Sans
```

Weight:

```text
400 / 500
```

### Technical Labels

Font:

```text
IBM Plex Mono
```

Use for:

- equations labels
- architecture blocks
- dataset names
- experiment settings

---

## Color System

```css
:root {
  --background: #08111C;
  --surface: #101B2A;
  --text: #F4F7FA;
  --muted: #91A1B2;
  --line: #26384A;
  --cyan: #53D6C5;
  --amber: #F2B84B;
}
```

Rules:

- cyan = active scientific signal
- amber = important comparison or evidence emphasis
- white = conclusion/main message
- gray = supporting explanation

Never use more than two accent colors on one slide.

---

## Layout Grammar

### Default Structure

```text
title

main evidence area

small source / experiment metadata
```

The slide should feel like a research canvas, not a webpage.

---

## Signature Components

### Architecture Diagram

Use:

- thin cyan connection lines
- dark nodes
- small mono labels
- directional flow

Avoid:

- colorful blocks
- 3D effects
- excessive shadows

---

### Equation Block

Equations appear as scientific objects.

Rules:

- large scale
- enough whitespace
- variable explanations nearby
- highlight only meaningful terms

Do not put equations inside rounded cards.

---

### Evidence Marker

Small metadata strip:

```text
SOURCE
Table 2
Section 4.1
```

Style:

- IBM Plex Mono
- muted gray
- bottom aligned

---

### Result Comparison

Use:

- horizontal comparisons
- direct labels
- visible metric names
- baseline markers

Avoid:

- decorative percentage circles
- fake dashboards

---

## Animation

Motion should explain research flow.

Allowed:

- architecture nodes appearing sequentially
- equation terms revealing by dependency
- result comparisons entering in reading order

Avoid:

- bouncing cards
- excessive zoom
- decorative particle effects

---

## Research Integrity

This design system never changes scientific meaning for visual effect.

Required:

- source labels remain readable
- equations remain exact
- benchmark values preserve units
- diagrams distinguish redraws from original figures

The visual system serves the evidence.
