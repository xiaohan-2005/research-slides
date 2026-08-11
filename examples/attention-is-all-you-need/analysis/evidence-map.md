# Evidence Map — Attention Is All You Need

This map connects the research story to concrete evidence. It is intentionally slide-oriented: each slide should answer one question and point to the evidence that supports its message.

| Slide | Main message | Claim IDs | Evidence | Treatment |
| --- | --- | --- | --- | --- |
| 01 | The paper proposes an attention-only sequence-transduction architecture. | C02 | Abstract; §1 | Title/thesis slide. No extra historical claims. |
| 02 | Sequential hidden-state computation is the bottleneck being challenged. | C01 | §1 | Original explanatory timeline comparing ordered recurrent steps. |
| 03 | The architectural move is to replace recurrence with attention-based dependency routing. | C02, C22 | §1–§3 | Reported thesis + clearly labeled interpretation. |
| 04 | The Transformer is a stacked encoder–decoder with repeated attention and feed-forward blocks. | C03, C04, C05 | §3.1; §3.3 | Original architecture redraw; not presented as the paper's original figure. |
| 05 | Scaled dot-product attention converts query–key compatibility into weighted values. | C06, C07 | §3.2.1, Eq. (1) | Preserve the equation exactly; annotate terms around it. |
| 06 | Multi-head attention creates multiple learned attention projections in parallel. | C08, C09 | §3.2.2 | Use eight visual head blocks only because h=8 is a source-reported configuration. |
| 07 | Without recurrence/convolution, order information is injected through positional encodings. | C10, C11 | §3.5; Table 3 row E | Show the sinusoidal equations and note the learned-position ablation separately. |
| 08 | Self-attention changes the trade-off among per-layer complexity, sequential work, and dependency path length. | C12, C13 | §4, Table 1 | Recreate the comparison table faithfully; do not imply unconditional superiority. |
| 09 | The reported result depends on a concrete training setup, not architecture alone. | C14, C15, C16, C17 | §5.1–§5.3 | Data/hardware/optimization context in compact cards. |
| 10 | The reported translation results are strong under the paper's evaluation setup. | C18, C19 | §6.1, Table 2 | Show exact metrics and task labels; avoid mixing paper versions. |
| 11 | Ablations provide evidence about heads and positional encoding choices. | C20, C21 | §6.2, Table 3 | Present as experiment-specific evidence, not universal laws. |
| 12 | The demonstrated contribution is attention-only transduction; later impact is outside this demo's evidence boundary. | C23, C24 | §7 + demo scope | Visually separate demonstrated contribution, interpretation, and open questions. |

## Evidence hierarchy used in this example

1. Exact equations and reported numerical results.
2. Tables and architecture descriptions in the paper.
3. Author explanations around those results.
4. Presentation interpretation, explicitly labeled.

## Figure policy

This example uses original HTML/CSS explanatory diagrams rather than copied paper figures. A redraw must:

- preserve the scientific relationship being explained;
- avoid implying it is the paper's original figure;
- cite the section or equation it explains;
- avoid adding nodes, arrows, metrics, or causal relations unsupported by the source.

## Review questions

Before accepting a regenerated slide, ask:

- Which claim IDs does this slide communicate?
- What is the strongest source supporting them?
- Is the visual showing evidence, explanation, or both?
- Has interpretation been visually distinguished from a reported finding?
- Could a reviewer locate the original evidence from the source pointer shown here?
