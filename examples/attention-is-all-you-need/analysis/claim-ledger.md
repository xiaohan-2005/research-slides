# Claim Ledger — Attention Is All You Need

This file is the evidence ledger for the demo. It separates source-reported findings from presentation interpretation before content reaches a slide.

## Claim types

- **Reported** — directly stated or shown in the paper.
- **Derived** — calculated from reported values.
- **Interpretation** — explanatory wording added for presentation clarity.
- **Background** — external context; intentionally minimized in this demo.

## Ledger

| ID | Statement | Type | Source pointer | Slide(s) | Evidence role / note |
| --- | --- | --- | --- | --- | --- |
| C01 | Recurrent sequence models constrain parallelization because hidden states are computed sequentially across positions. | Reported | §1 Introduction | 2 | Frames the computational bottleneck motivating the Transformer. |
| C02 | The Transformer removes recurrence and convolution from its main sequence-transduction architecture and relies on attention mechanisms. | Reported | Abstract; §1; §3 | 1–3 | Central thesis of the paper. |
| C03 | The encoder and decoder each use stacks of six layers in the reported base architecture. | Reported | §3.1 | 4 | Architecture parameter. |
| C04 | The base model uses d_model = 512. | Reported | §3.1 | 4 | Architecture parameter. |
| C05 | The position-wise feed-forward network maps 512 dimensions to 2048 and back to 512. | Reported | §3.3 | 4 | Method detail used in the architecture slide. |
| C06 | Scaled dot-product attention is defined as softmax(QKᵀ / √d_k)V. | Reported | §3.2.1, Eq. (1) | 5 | Exact source equation; mathematical meaning must not be altered. |
| C07 | Scaling by √d_k addresses the effect of large dot products pushing softmax toward regions with very small gradients. | Reported | §3.2.1 | 5 | Explanation given by the authors after Eq. (1). |
| C08 | The base Transformer uses 8 attention heads with d_k = d_v = 64. | Reported | §3.2.2 | 6 | Multi-head configuration. |
| C09 | Multiple heads allow the model to attend jointly to information from different representation subspaces at different positions. | Reported | §3.2.2 | 6 | Author motivation for multi-head attention. |
| C10 | Positional encodings are added to token embeddings because the architecture contains neither recurrence nor convolution. | Reported | §3.5 | 7 | Connects architecture choice to sequence-order representation. |
| C11 | The paper uses sinusoidal positional encodings and reports similar results for learned positional embeddings. | Reported | §3.5; Table 3 row E | 7, 11 | Used to distinguish design choice from empirical necessity. |
| C12 | Full self-attention has O(n²d) complexity per layer, O(1) sequential operations, and O(1) maximum path length. | Reported | §4, Table 1 | 8 | Complexity/path-length comparison. |
| C13 | A recurrent layer is listed with O(nd²) complexity, O(n) sequential operations, and O(n) maximum path length. | Reported | §4, Table 1 | 8 | Baseline comparison. |
| C14 | The WMT14 English–German training set contains about 4.5 million sentence pairs. | Reported | §5.1 | 9 | Training-data context. |
| C15 | Training used 8 NVIDIA P100 GPUs. | Reported | §5.2 | 9 | Hardware context. |
| C16 | The base model trained for 100,000 steps, about 12 hours under the reported setup. | Reported | §5.2 | 9 | Training-time context. |
| C17 | The learning-rate schedule used 4,000 warmup steps. | Reported | §5.3 | 9 | Optimization detail. |
| C18 | The Transformer big model reports 28.4 BLEU on WMT14 English→German. | Reported | §6.1, Table 2 | 10 | Headline result used in the demo. |
| C19 | The final conference paper reports 41.0 BLEU on WMT14 English→French in the result discussion. | Reported | §6.1 | 10 | Keep tied to the exact paper/version used by this example. |
| C20 | The ablation table shows lower dev BLEU with one attention head than with the base eight-head setting. | Reported | §6.2, Table 3 | 11 | Supports a cautious statement that the single-head variant performed worse in this experiment. |
| C21 | Learned positional embeddings perform nearly the same as the sinusoidal encoding in the reported ablation. | Reported | §6.2, Table 3 row E | 11 | Do not overstate as proof that positional encoding choice never matters. |
| C22 | “Connect positions by learned relevance, not by stepping through time.” | Interpretation | Derived from §1–§4 | 3 | Presentation shorthand. Must be visibly labeled as interpretation, not quoted as source text. |
| C23 | Replacing sequential recurrence with global content-dependent routing is a useful way to conceptualize the architectural trade. | Interpretation | Derived from §1–§4 | 12 | Presenter interpretation, not an author quote. |
| C24 | Later historical impact of Transformers is intentionally outside the evidence boundary of this demo. | Interpretation / scope rule | Demo policy | 12 | Prevents post-2017 claims from being smuggled into a paper-only walkthrough. |

## Unresolved / version-sensitive items

- Do not mix numbers from different versions of the paper without labeling the version.
- English→French values have appeared differently across versions/locations; this example should keep one internally consistent source and avoid merging values from different versions.
- If the source paper version changes, re-check C18–C21 before regenerating the deck.

## Validation rule

Every quantitative statement in the presentation must map to a **Reported** or **Derived** ledger item. Every explanatory statement that goes beyond the source wording should be treated as **Interpretation**.
