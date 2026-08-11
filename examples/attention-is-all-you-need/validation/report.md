# Validation Report — Attention Is All You Need

## Scope

This report tracks the first `research-slides` end-to-end test case and deliberately separates:

1. evidence validation;
2. structural HTML validation;
3. design-system migration validation;
4. rendered visual validation.

A structural or source-inspection pass is **not** treated as a rendered visual pass.

---

## Artifacts under review

Canonical output:

```text
examples/attention-is-all-you-need/output/presentation.html
```

Selected visual system:

```text
research-template-pack/templates/neural-lab/design.md
```

Supporting traceability artifacts:

```text
analysis/claim-ledger.md
analysis/evidence-map.md
slide-outline.md
citations.md
```

Legacy output retained for regression context:

```text
presentation.html
```

---

# 1. Evidence Validation

| Check | Status | Notes |
| --- | --- | --- |
| Important slide claims have source pointers | PASS | Every canonical slide includes a `source-label` with section/table/equation pointers. |
| Claim types distinguish reported findings from interpretation | PASS | Slide 3 explicitly labels explanatory interpretation. |
| Quantitative results identify their source | PASS | Translation metrics point to §6.1 / Table 2; ablations point to §6.2 / Table 3. |
| Equations preserve the source meaning | PASS | Scaled dot-product attention and positional encoding remain source equations. |
| Original explanatory visuals are distinguished from paper figures | PASS | Architecture/mechanism visuals are presented as explanatory redraws. |
| Later historical impact is treated as a 2017-paper finding | PASS | It is intentionally excluded from the evidence boundary. |
| Numerical-version consistency | PASS WITH NOTE | Canonical result slide uses proceedings-paper values consistently: EN→DE 28.4 and EN→FR 41.0. |

### Evidence result

**PASS**, with the proceedings-version note remaining part of the example contract.

---

# 2. Structural HTML Validation

Canonical file inspected:

```text
output/presentation.html
```

| Check | Status | Evidence in canonical HTML |
| --- | --- | --- |
| `.deck-viewport` exists | PASS | Full-window deck container is present. |
| `.deck-stage` exists | PASS | Authored slide stage is present. |
| Stage width is 1920px | PASS | Canonical CSS uses 1920px. |
| Stage height is 1080px | PASS | Canonical CSS uses 1080px. |
| Slides use fixed authored dimensions | PASS | `.slide` is 1920×1080. |
| Slide state uses `.active` / `.visible` | PASS | Both classes drive visibility and motion. |
| Slide count matches narrative plan | PASS | 12 slides. |
| Keyboard navigation exists | PASS | Arrow keys, PageUp/PageDown, Space, Home and End. |
| Touch navigation exists | PASS | Swipe handling via `touchstart` / `touchend`. |
| Progress/page feedback exists | PASS | Counter and progress bar are outside the authored slide canvas. |
| Reduced-motion support exists | PASS | `prefers-reduced-motion` handling is present. |
| Source labels exist | PASS | Every slide contains `.source-label`. |
| Fixed-stage behavior replaces responsive slide reflow | PASS | Whole 1920×1080 stage is scaled with a transform. |
| External/local asset dependency | PASS | Canonical deck is self-contained HTML/CSS/SVG. |

### Structural result

**PASS by source inspection.**

Repository command for a local/Codex checkout:

```bash
python scripts/validate_slides.py examples/attention-is-all-you-need/output/presentation.html
```

This report does not claim that the command was executed during the GitHub-editing session.

---

# 3. Neural Lab Migration Validation

The canonical deck was migrated from the earlier warm/light visual system to the selected Neural Lab design system.

| Design-system requirement | Status | Notes |
| --- | --- | --- |
| Deep navy research field | PASS | Canonical tokens use `#08111C` / `#050B12`. |
| Cyan = method / model flow | PASS | Architecture, active attention paths and primary method cues use cyan. |
| Amber = evidence / comparison | PASS | Evidence paths, selected result emphasis and cautionary comparison use amber. |
| Display/body/mono role separation | PASS | Separate display, body and technical mono stacks are defined. |
| Scientific surfaces, not generic card wall | PASS WITH NOTE | Panels are used selectively, though rendered review must confirm visual rhythm across all 12 slides. |
| Architecture grammar | PASS | Encoder/decoder blocks and dependency paths use restrained technical nodes/edges. |
| Equation grammar | PASS | Equations are large scientific objects rather than bright UI cards. |
| Chart grammar | PASS | Flat comparison bars, direct labels, no 3D/gradient chart effects. |
| Source/evidence strip | PASS | Source labels remain quiet, readable and bottom-aligned. |
| Anti-cyberpunk rule | PASS by source inspection | No particle effects, fake terminal windows, neon-glow card walls or random futuristic imagery. |
| Evidence integrity overrides style | PASS | Claims/source pointers were retained during migration. |

### Migration result

**COMPLETE by source inspection.**

The migration demonstrates the intended progressive workflow:

```text
research topic
   ↓
style shortlist
   ↓
neural-lab preview/design selection
   ↓
load one design.md
   ↓
apply one coherent visual thesis to the full deck
```

---

# 4. Legacy Regression Check

Legacy file:

```text
examples/attention-is-all-you-need/presentation.html
```

| Check | Status | Reason |
| --- | --- | --- |
| Canonical class names | FAIL | Uses `.viewport` / `.stage`. |
| Canonical authored dimensions | FAIL | Uses 1600×900. |
| Current fixed-stage support contract | FAIL | Predates the current Skill runtime. |

The legacy file is retained only as a migration/regression reference and is **not** canonical output.

---

# 5. Rendered Visual Validation

## Status: PENDING

The migrated Neural Lab deck still requires actual browser rendering and screenshot inspection.

Required checks:

- no title/body clipping on all 12 slides;
- no panel overlap;
- source labels remain readable;
- equations remain fully visible;
- architecture diagrams stay inside the safe area;
- Slide 5 attention lines and tokens remain legible;
- Slide 7 positional-encoding formulas and waveform do not collide;
- Slide 8 comparison table remains readable at presentation scale;
- Slide 10 result bars and labels remain legible;
- Slide 11 ablation labels do not collide;
- controls remain outside the authored stage;
- desktop viewport preserves 16:9;
- phone-sized viewport scales the same stage rather than reflowing;
- reduced-motion mode preserves the final scientific meaning.

A rendered inspection should be completed before this example is labeled release-ready.

---

# 6. Current Test-Case Status

```text
Evidence validation      PASS
Structural validation    PASS by source inspection
Neural Lab migration     COMPLETE by source inspection
Legacy regression        EXPECTED FAIL
Rendered visual review   PENDING
Release-ready             NO
```

## Next action

Render `output/presentation.html` in a browser at desktop and phone-sized viewports, inspect all 12 slides, fix any clipping/overlap/legibility issue, and then update this report with the actual rendered result.

The purpose of this report is to make the state of the Skill test **auditable**, not to make the example look more complete than it is.
