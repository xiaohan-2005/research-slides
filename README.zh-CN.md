# Research Slides

[English](README.md) · **简体中文**

> **把论文、研究笔记和数据，转化为有证据链、有引用、可用于真实汇报的 Codex 学术演示稿。**

[![GitHub stars](https://img.shields.io/github/stars/xiaohan-2005/research-slides?style=social)](https://github.com/xiaohan-2005/research-slides/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-111827.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-alpha-2563EB.svg)
![Codex](https://img.shields.io/badge/Codex-Skill-0F766E.svg)

<img src="assets/demo-cover.svg" width="100%" alt="Research Slides — 面向 Codex 的科研演示 Skill" />

<div align="center">

**Codex-first · 证据可追溯 · 引用可追溯 · 固定 16:9**

[**开始使用**](SKILL.md) · [**国一竞赛答辩案例**](examples/chengdu-fresh-market-defense/README.md) · [**Attention Is All You Need 案例**](examples/attention-is-all-you-need/README.md)

如果这个项目对你的科研、课程汇报或竞赛答辩有帮助，欢迎 **⭐ Star**，也能帮助更多人发现它。

</div>

---

## 先看效果

<a href="examples/chengdu-fresh-market-defense/README.md">
  <img src="examples/chengdu-fresh-market-defense/preview/contact-sheet.png" width="100%" alt="Research Slides 成都社区生鲜店竞赛答辩案例总览" />
</a>

上面的真实案例将一篇约 **100 页的全国一等奖市场研究论文**，整理为 **14 页演讲型竞赛答辩演示稿**。

它不是简单把论文“缩写成 PPT”，而是保留并重新组织：

- 问卷调查和商户调研证据；
- 关键数字、图表和现场素材；
- 每页结论对应的证据来源；
- 原文中存在的数据口径或一致性问题；
- 明确区分“论文原始结论”和“演示中的解释/策略建议”。

[**查看完整案例 →**](examples/chengdu-fresh-market-defense/README.md) · [**查看 HTML 演示稿**](examples/chengdu-fresh-market-defense/output/presentation.html) · [**查看原始论文**](examples/chengdu-fresh-market-defense/source-paper.pdf) · [**查看证据映射**](examples/chengdu-fresh-market-defense/analysis/evidence-map.md)

---

## 它解决什么问题？

很多 AI 做 PPT 的流程主要优化两个东西：

1. **生成得快**；
2. **看起来漂亮**。

但科研汇报、论文组会、数学建模答辩、市场调研竞赛真正麻烦的是第三件事：

> **重要结论能不能追溯回原始证据？**

Research Slides 的核心链路是：

```text
结论 claim
   ↓
来源 source
   ↓
证据 evidence
   ↓
页面 slide
```

因此它会尽量保留论文中的：

- 关键结论；
- 数据和定量结果；
- 图表；
- 公式；
- 引用；
- 限制条件；
- 证据与页面之间的映射关系。

目标不是做一份“像论文的 PPT”，而是把复杂研究材料重新组织成一条**适合演讲的研究故事线**。

---

## 核心特点

### 1. 不是逐段摘要，而是重建汇报逻辑

Research Slides 会围绕科学问题、研究设计、证据和结论重新组织材料，而不是机械按论文目录搬运。

### 2. 重要结论可追溯

它会区分：

- 原文报告的发现；
- 根据原始数据计算得到的值；
- 演示者自己的解释；
- 背景知识。

这样可以降低“AI 把自己的解释说成论文结论”的风险。

### 3. 图表不是装饰

论文图、统计图、机制图和公式都被视为论证的一部分，而不是为了让页面显得丰富而随便插图。

### 4. 先选真实视觉方向，再生成整套页面

不是让用户用抽象词描述“高级、简约、科技感”。

流程会先根据真实标题和研究主题生成候选视觉方向，再让用户选择：

```text
风格候选
   ↓
真实标题页预览
   ↓
选择一个方向
   ↓
加载对应设计系统
   ↓
生成完整演示稿
```

### 5. 固定 1920×1080 演示舞台

最终 HTML 按 **1920×1080** 固定舞台设计，并整体缩放，避免在手机或不同浏览器中变成普通纵向网页。

### 6. 带验证环节

仓库包含静态验证脚本，用于检查常见结构错误：

```bash
python scripts/validate_slides.py path/to/presentation.html
```

脚本通过后仍需要进行渲染检查，以发现文字裁切、重叠、图表过小、公式和引用不可读等视觉问题。

---

## 快速开始

```bash
git clone https://github.com/xiaohan-2005/research-slides.git
cd research-slides
```

然后在 Codex 中打开仓库，让它遵循 [`SKILL.md`](SKILL.md)。

可以直接这样说：

```text
Use the research-slides skill in this repository.
Turn this paper into a 12-slide group-meeting presentation.
Use speaker-led density.
Keep every important quantitative claim traceable to its source.
Show me three real title-slide previews before building the full deck.
```

也可以直接用中文描述你的任务，例如：

```text
调用这个仓库里的 research-slides skill。
把我提供的论文做成一份 14 页竞赛答辩演示稿。
少文字、强视觉，适合现场演讲。
重要数字和结论必须能够追溯到原文证据。
先给我 3 个基于真实题目的标题页视觉方案，再生成完整演示稿。
```

> 当前仓库处于 alpha 阶段。核心工作流已经可用，PDF 结构化提取、浏览器级自动验证等能力仍在持续完善。

---

## 两个完整案例

### ① 全国一等奖市场研究论文 → 竞赛答辩

[`examples/chengdu-fresh-market-defense/`](examples/chengdu-fresh-market-defense/README.md)

包含：

- 原始论文 PDF；
- 证据映射；
- 14 页 HTML 演示稿；
- 页面预览；
- 桌面端/手机端固定舞台验证；
- 验证报告。

### ② Attention Is All You Need → 学术组会

[`examples/attention-is-all-you-need/`](examples/attention-is-all-you-need/README.md)

用于测试技术论文场景，包括：

- 12 页研究叙事；
- claim ledger；
- evidence map；
- 公式与定量结果；
- Neural Lab 视觉系统；
- 静态验证报告。

---

## 视觉系统

目前包含四套真正不同的研究视觉语法，而不是同一模板换颜色。

### Neural Lab

<img src="assets/style-gallery/neural-lab.svg" width="100%" alt="Neural Lab" />

适合：模型架构、深度学习、算法、公式、消融实验。

### Scientific Minimal

<img src="assets/style-gallery/scientific-minimal.svg" width="100%" alt="Scientific Minimal" />

适合：论文组会、实验结果、图表驱动型研究。

### Data Atlas

<img src="assets/style-gallery/data-atlas.svg" width="100%" alt="Data Atlas" />

适合：统计分析、调查研究、数据密集型汇报。

### Editorial Academic

<img src="assets/style-gallery/editorial-academic.svg" width="100%" alt="Editorial Academic" />

适合：文献综述、政策研究、社会科学和概念型论证。

[**查看完整模板包 →**](research-template-pack/README.md)

---

## 研究完整性原则

Research Slides 更倾向于“明确承认证据不足”，而不是生成一个看起来很确定但来源不可靠的结论。

它不应该：

- 编造引用；
- 编造数字；
- 偷偷修改论文中的报告值；
- 为了排版改变公式含义；
- 把解释性内容包装成论文原结论；
- 把重绘图误称为论文原图；
- 用漂亮设计掩盖来源不清的问题。

如果证据不完整，就应明确标记为不完整。

---

## 当前状态

已完成：

- [x] 面向 Codex 的 `SKILL.md`
- [x] Research integrity rules
- [x] Progressive visual discovery
- [x] 4 套研究视觉系统
- [x] 固定 1920×1080 演示舞台
- [x] HTML 演示架构
- [x] 静态页面验证器
- [x] Attention Is All You Need 技术论文案例
- [x] 全国一等奖市场研究竞赛答辩案例

下一阶段：

- [ ] 浏览器级视觉验证自动化
- [ ] PDF 结构与图片提取
- [ ] 机器可读的 claim/source schema
- [ ] 引用验证工具
- [ ] Data / Notebook → Research Deck
- [ ] 更多不同研究结构的真实案例

---

## License

MIT — 见 [`LICENSE`](LICENSE)。
