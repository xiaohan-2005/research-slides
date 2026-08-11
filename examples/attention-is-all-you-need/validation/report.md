# Validation Report — Attention Is All You Need

## Scope

This report tracks the first `research-slides` end-to-end test case and deliberately separates:

1. evidence validation;
2. structural HTML validation;
3. design-system migration validation;
4. rendered visual validation.

A structural pass is **not** treated as a browser-interaction pass.

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

The current committed canonical HTML was reconstructed locally from the repository and verified against the Git blob SHA before validation.

```text
GitHub blob SHA:  a094e226bade8ff0d76132657d6c098b250f5bbe
Local git hash:   a094e226bade8ff0d76132657d6c098b250f5bbe
Match:            YES
```

The repository validator was then actually executed:

```bash
python scripts/validate_slides.py examples/attention-is-all-you-need/output/presentation.html
```

Executed result:

```text
PASS  deck viewport class
PASS  deck stage class
PASS  slide elements exist — 12 detected
PASS  1920px authored stage width
PASS  1080px authored stage height
PASS  slide visibility uses active/visible state
PASS  keyboard navigation
PASS  touch/swipe navigation
PASS  reduced-motion support
PASS  source/citation labels present — 12 detected
PASS  local referenced assets exist
PASS  no obvious responsive slide reflow

Static validation PASSED.
```

### Structural result

**PASS — validator actually executed against the current canonical blob.**

---

# 3. Neural Lab Migration Validation

The canonical deck was migrated from the earlier warm/light visual system to the selected Neural Lab design system.

| Design-system requirement | Status | Notes |
| --- | --- | --- |
| Deep navy research field | PASS | Canonical tokens use `#08111C` / `#050B12`. |
| Cyan = method / model flow | PASS | Architecture, active attention paths and primary method cues use cyan. |
| Amber = evidence / comparison | PASS | Evidence paths, selected result emphasis and cautionary comparison use amber. |
| Display/body/mono role separation | PASS | Separate display, body and technical mono stacks are defined. |
| Scientific surfaces, not generic card wall | PASS | Panels support evidence groupings rather than replacing every slide with identical cards. |
| Architecture grammar | PASS | Encoder/decoder blocks and dependency paths use restrained technical nodes/edges. |
| Equation grammar | PASS | Equations are large scientific objects rather than bright UI cards. |
| Chart grammar | PASS | Flat comparison bars, direct labels, no 3D/gradient chart effects. |
| Source/evidence strip | PASS | Source labels remain quiet, readable and bottom-aligned. |
| Anti-cyberpunk rule | PASS | No particle effects, fake terminal windows, neon-glow card walls or random futuristic imagery. |
| Evidence integrity overrides style | PASS | Claims/source pointers were retained during migration. |

### Migration result

**COMPLETE.**

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

## 5.1 Static rendered review

The current canonical blob was rendered into **12 separate 1920×1080 pages** using a print/static HTML renderer, then inspected as a full contact sheet and at full resolution for the densest slides.

Reviewed at full resolution:

- Slide 1 — title / graph composition;
- Slide 4 — encoder–decoder architecture;
- Slide 5 — equation + attention mechanism layout;
- Slide 7 — positional encoding equation + waveform;
- Slide 8 — complexity comparison table;
- Slide 10 — BLEU comparison bars;
- Slide 11 — ablation chart + interpretation panels;
- Slide 12 — conclusion / evidence-boundary statement.

The remaining slides were inspected in the 12-slide contact sheet.

### Static-render findings

| Check | Status | Notes |
| --- | --- | --- |
| Title/body clipping | PASS | No visible clipping across the 12 rendered pages. |
| Panel overlap | PASS | No visible panel collisions in the static render. |
| Source-strip readability | PASS | Source strips remain visible and separated from main content. |
| Slide 4 architecture density | PASS | Encoder and decoder stacks remain readable. |
| Slide 7 equation/waveform collision | PASS | No collision observed. |
| Slide 8 comparison-table density | PASS | Table and two interpretation panels remain readable. |
| Slide 10 bar labels | PASS | Labels and exact values remain visible. |
| Slide 11 ablation labels | PASS | Labels do not collide in the static render. |
| Slide 12 conclusion hierarchy | PASS | Main evidence-boundary statement remains visually dominant. |

### Renderer caveat

The static renderer does not implement every browser CSS/SVG feature. In particular, it did not fully reproduce CSS-driven SVG `stroke` styling and `place-items`, so Slide 1 node-label centering and Slide 5 attention-edge appearance cannot be judged from that renderer alone. These are browser-specific checks.

## 5.2 Chromium interactive browser review

### Status: PENDING — environment policy limitation

Chromium was launched in the validation environment, but the managed browser policy blocked all attempted local test origins:

```text
file://        blocked
127.0.0.1      blocked
data:          blocked
```

Because of that policy, this session could not truthfully mark the following browser-specific checks as complete:

- CSS/SVG appearance in Chromium;
- interactive navigation screenshots;
- control overlay behavior;
- desktop interactive viewport behavior;
- phone-sized viewport scaling;
- reduced-motion browser behavior.

This is an environment limitation, not a claimed pass.

---

# 6. Current Test-Case Status

```text
Evidence validation          PASS
Static validator             PASS — actually executed
Neural Lab migration         COMPLETE
Static rendered visual QA    PASS with renderer caveat
Chromium interactive QA      PENDING — environment URL policy
Legacy regression            EXPECTED FAIL
Release-ready                NO
```

## Next action

Open `output/presentation.html` in an unrestricted Chromium/Chrome environment and complete the remaining browser-specific checks, especially:

1. Slide 1 node-label centering;
2. Slide 5 attention-edge rendering;
3. presentation-control placement at a 16:9 desktop viewport;
4. phone-sized viewport scaling without reflow;
5. reduced-motion behavior.

Only then should the test case be marked fully release-ready.

The purpose of this report is to make the state of the Skill test **auditable**, including tool/environment limitations rather than hiding them.
