# Slide Outline — Attention Is All You Need

This outline is a research narrative, not a section-by-section transcription of the paper.

| # | Slide | Research job | Primary source |
|---|---|---|---|
| 01 | Attention Is All You Need | Establish the paper and thesis | Paper title + abstract |
| 02 | The bottleneck was sequential computation | Frame the problem with recurrent sequence models | §1 Introduction |
| 03 | Replace recurrence with attention | State the central architectural move | §1–§3 |
| 04 | Transformer at a glance | Explain encoder/decoder stacks and core dimensions | §3.1 |
| 05 | Scaled dot-product attention | Explain the core equation and why scaling is used | §3.2.1, Eq. (1) |
| 06 | Multi-head attention | Show parallel representation subspaces | §3.2.2 |
| 07 | No recurrence means position must be injected | Explain sinusoidal positional encoding | §3.5 |
| 08 | Why self-attention? | Compare complexity, sequential operations and path length | §4, Table 1 |
| 09 | Training recipe | Ground the system in data, hardware and optimization choices | §5 |
| 10 | Translation results | Present the reported WMT14 results without exaggeration | §6.1, Table 2 |
| 11 | What did the ablations say? | Show evidence about heads, width and positional encoding | §6.2, Table 3 |
| 12 | What changed — and what remained open | Separate the paper's demonstrated contribution from future work | §7 Conclusion |

## Narrative rules used

1. One scientific question per slide.
2. Reported findings are visually separated from interpretation.
3. Figures in the demo are original explanatory diagrams, not copied paper figures.
4. Quantitative claims are mapped in `citations.md`.
5. The deck avoids claims about later Transformer impact; it stays focused on what the 2017 paper itself demonstrated.
