# Attention Is All You Need — End-to-End Test Case

This example tests the complete `research-slides` workflow on Vaswani et al. (2017), from research evidence to a fixed-stage HTML presentation.

## Source

**Vaswani et al. (2017), _Attention Is All You Need_**

The example uses the official proceedings-paper values as the numerical authority for the reported translation results.

## What this example tests

```text
paper
  ↓
research structure
  ↓
claim ledger
  ↓
evidence map
  ↓
narrative plan
  ↓
visual discovery
  ↓
Neural Lab design system
  ↓
1920×1080 HTML deck
  ↓
validation
```

This is not only a finished presentation. It is a traceable Skill test case.

## Selected visual direction

The canonical output currently uses:

```text
research-template-pack/templates/neural-lab/design.md
```

Why it fits this paper:

- architecture diagrams are central to the story;
- equations need first-class visual treatment;
- benchmark and ablation evidence need precise comparison;
- the dark technical system matches an AI / model-analysis context without using generic cyberpunk decoration.

Neural Lab uses cyan for model/logic flow and amber for evidence/comparison emphasis. The design system must remain subordinate to scientific traceability.

## Files

```text
attention-is-all-you-need/
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

### Evidence artifacts

- [`analysis/claim-ledger.md`](analysis/claim-ledger.md) — slide-worthy claims, claim types and source pointers.
- [`analysis/evidence-map.md`](analysis/evidence-map.md) — connects slide messages to evidence and visual treatment.
- [`citations.md`](citations.md) — citation/version notes for the example.

### Presentation

- [`output/presentation.html`](output/presentation.html) — canonical 12-slide, 1920×1080 Neural Lab deck.

The older root-level `presentation.html` predates the current fixed-stage contract and is retained only as a regression/migration reference.

### Validation

- [`validation/report.md`](validation/report.md) — evidence, structure, migration and rendered-review status.

## Evidence boundary

The example intentionally distinguishes between:

- source-reported findings;
- derived values;
- explanatory interpretation;
- later historical context.

Later Transformer/LLM impact is not presented as a finding of the 2017 paper.

## Current status

```text
Evidence mapping          PASS
Canonical 1920×1080       PASS by source inspection
Neural Lab migration      COMPLETE
Rendered visual review    PENDING
Release-ready             NO
```

The example should not be labeled release-ready until every slide has been inspected in a rendered browser for clipping, overlap, legibility and fixed-stage behavior.
