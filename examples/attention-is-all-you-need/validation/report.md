# Validation Report — Attention Is All You Need

## Scope

This report tracks the first `research-slides` end-to-end test case.

It deliberately separates:

1. evidence validation;
2. structural HTML validation;
3. rendered visual validation.

A structural pass is **not** treated as a visual pass.

---

## Artifacts under review

Canonical output:

```text
examples/attention-is-all-you-need/output/presentation.html
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

The legacy file predates the current fixed-stage Skill contract.

---

# 1. Evidence Validation

| Check | Status | Notes |
| --- | --- | --- |
| Important slide claims have source pointers | PASS | Every canonical slide includes a `source-label` with section/table/equation pointers. |
| Claim types distinguish reported findings from interpretation | PASS | `claim-ledger.md` separates reported and interpretation claims; Slide 3 explicitly labels interpretation. |
| Quantitative results identify their source | PASS | Translation metrics point to §6.1 / Table 2; ablations point to §6.2 / Table 3. |
| Equations preserve the source meaning | PASS | Scaled dot-product attention and positional encoding are presented as source equations rather than rewritten claims. |
| Original explanatory visuals are distinguished from paper figures | PASS | Architecture and mechanism diagrams are described as original redraws/explanatory visuals. |
| Later historical impact is presented as a 2017-paper finding | PASS | It is intentionally excluded from the evidence boundary. |
| Numerical-version consistency | PASS WITH NOTE | Canonical result slide uses the official proceedings-paper values consistently: EN→DE 28.4 and EN→FR 41.0. Do not mix values from other public versions in the same deck. |

### Evidence result

**PASS**, with the version-consistency note above remaining part of the example contract.

---

# 2. Structural HTML Validation

Canonical file inspected:

```text
output/presentation.html
```

| Check | Status | Evidence in canonical HTML |
| --- | --- | --- |
| `.deck-viewport` exists | PASS | Present as the full-window deck container. |
| `.deck-stage` exists | PASS | Present as the authored slide stage. |
| Stage width is 1920px | PASS | `.deck-stage { width: 1920px; }` |
| Stage height is 1080px | PASS | `.deck-stage { height: 1080px; }` |
| Slides use fixed authored dimensions | PASS | `.slide` is 1920×1080. |
| Slide state uses `.active` / `.visible` | PASS | Both classes drive visibility and animation state. |
| Slide count matches narrative plan | PASS | 12 slides, matching `slide-outline.md`. |
| Keyboard navigation exists | PASS | Arrow keys, PageUp/PageDown, Space, Home and End are handled. |
| Touch navigation exists | PASS | `touchstart` / `touchend` swipe handling is included. |
| Progress / page feedback exists | PASS | Page counter and progress bar are outside the slide stage. |
| Reduced-motion support exists | PASS | `@media (prefers-reduced-motion: reduce)` included. |
| Source labels exist | PASS | Every slide includes `.source-label`. |
| Obvious mobile slide reflow added | PASS | The deck scales the fixed 1920×1080 stage rather than reflowing slide content. |
| External/local asset dependency | PASS | Canonical deck uses inline HTML/CSS/SVG and does not require adjacent research-image files. |

### Structural result

**PASS by source inspection.**

The repository validator for future local/Codex runs is:

```bash
python scripts/validate_slides.py examples/attention-is-all-you-need/output/presentation.html
```

This report does not claim that command was executed inside a local checkout during this repository-editing session; the listed predicates were inspected directly in the committed canonical HTML.

---

# 3. Legacy Regression Check

Legacy file:

```text
examples/attention-is-all-you-need/presentation.html
```

Known incompatibilities with the current Skill contract:

| Check | Status | Reason |
| --- | --- | --- |
| Canonical class names | FAIL | Uses `.viewport` / `.stage` rather than `.deck-viewport` / `.deck-stage`. |
| Canonical authored dimensions | FAIL | Uses 1600×900 rather than 1920×1080. |
| Current fixed-stage support contract | FAIL | Predates `viewport-base.css` and `html-template.md`. |

The legacy file is retained only as a migration/regression reference. It is **not** the canonical example output.

---

# 4. Rendered Visual Validation

## Status: PENDING

The canonical deck still needs a browser-rendered visual inspection.

Required checks:

- no title or body text clipping;
- no card/panel overlap;
- source labels remain readable on every slide;
- equations remain fully visible;
- SVG diagrams remain inside the authored canvas;
- slide 10 result bars and labels are legible;
- slide 11 ablation labels do not collide;
- controls remain outside the authored stage;
- desktop rendering preserves 16:9 without reflow;
- phone-sized viewport scales the same 16:9 stage rather than rearranging content;
- reduced-motion mode leaves every slide scientifically understandable.

A rendered inspection should be performed before this example is labeled release-ready.

---

# 5. Current Test-Case Status

```text
Evidence validation      PASS
Structural validation    PASS by source inspection
Legacy regression        EXPECTED FAIL
Rendered visual review   PENDING
Release-ready             NO
```

## Next action

Render `output/presentation.html` in a browser at a desktop viewport and at least one phone-sized viewport, capture/inspect all 12 slides, fix any clipping or overlap, then update this report with the actual visual-review result.

The purpose of this report is not to make the example look complete. It is to make the state of the Skill test **auditable**.
