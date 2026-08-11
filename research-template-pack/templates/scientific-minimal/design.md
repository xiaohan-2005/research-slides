# Scientific Minimal — Full Design System

Use after `scientific-minimal` is selected in Phase 4.

Scientific Minimal is a light, publication-adjacent research system. It prioritizes figures, equations, exact comparisons, and readable source trails. The visual tone is calm and rigorous rather than decorative.

## Fixed stage

- 1920×1080 authored canvas
- whole-stage scaling only
- default safe area: 112px left/right, 84px top, 78px bottom

## Tokens

```css
:root {
  --sm-bg:#F7F7F4;
  --sm-paper:#FFFFFF;
  --sm-ink:#171717;
  --sm-soft:#3F4750;
  --sm-muted:#667085;
  --sm-line:#D8DBDF;
  --sm-blue:#315E8A;
  --sm-blue-soft:#EAF0F5;
  --sm-green:#2E7D64;
  --sm-green-soft:#E7F1ED;
  --sm-amber:#B36A2E;
  --sm-display:"Source Serif 4","Georgia",serif;
  --sm-body:"IBM Plex Sans","Aptos","Segoe UI",sans-serif;
  --sm-mono:"IBM Plex Mono","Consolas",monospace;
}
```

Semantic use:

- blue = primary evidence / active argument
- green = corroborating or positive comparison
- amber = caveat / trade-off / uncertainty cue
- black = main conclusion

## Typography

- hero title: 96–108px serif, 1.00 line-height
- slide statement: 60–68px serif, 1.04
- body lead: 29–32px sans, 1.42
- body: 23–26px sans, 1.48
- technical label: 16–18px mono
- source label: 14–16px sans

Do not shrink a title below 54px; rewrite it instead.

## Layout grammar

Use a 12-column conceptual grid with large white margins. Prefer:

- 60–72% evidence object + 28–40% interpretation
- one figure or one equation as the dominant object
- thin dividing rules instead of card containers
- asymmetry when it improves hierarchy

Panels are allowed only when an evidence object needs a neutral field. Avoid repeated rounded cards.

## Title slide

- title left-aligned or centered with generous negative space
- one restrained scientific motif: a line plot fragment, equation fragment, axis, or specimen outline
- metadata in a small bottom rail
- no hero illustration unrelated to the research

## Figure slide

- source figure dominates
- use a white or very light neutral field
- annotations use blue first, amber only for caveats
- crop only when the omitted context cannot change interpretation
- keep source/caption information readable

## Equation slide

- equation 48–66px equivalent
- direct placement on canvas; no rounded formula card
- highlight semantic terms with blue/green only when explaining them
- variable definitions aligned in a narrow side column

## Chart grammar

- direct labels over legends when practical
- flat marks; no gradients, 3D, glow, or ornamental axes
- gridlines light and sparse
- uncertainty bands/error bars preserved when reported
- do not truncate axes merely to exaggerate differences

## Table grammar

- thin horizontal rules
- no boxed cells unless scientifically necessary
- header 15–17px mono or small caps
- body 18–22px
- highlight only the cells required by the slide claim

## Method diagram

- line-first, low-decoration diagrams
- blue for the active path
- neutral gray for supporting structure
- labels should read like scientific notation, not product UI

## Source rail

Recommended bottom rail:

```text
SOURCE · Author et al. · §4.2 · Figure 3 · Claim C14
```

Use muted gray with a thin top rule. The citation should feel like part of the scientific interface.

## Motion

Favor opacity + 16–22px vertical reveal, 380–520ms. For figures, reveal the full figure first, then annotation. Equations stay mathematically complete while emphasis changes.

## CJK

Use `Noto Serif CJK SC` / `Source Han Serif SC` for display when available, and `Noto Sans CJK SC` / `Source Han Sans SC` for body. Do not add Latin-style uppercase tracking to Chinese.

## Anti-patterns

Avoid:

- dashboard layouts
- purple/blue gradients
- glassmorphism
- giant KPI numbers without evidence context
- decorative lab photography unrelated to the paper
- faux journal mastheads
- excessive rounded rectangles

The intended result is a deck that feels **scientifically edited**, not templated.