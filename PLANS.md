# PyQt5 OrinNano 实验手册英文翻译执行计划

## 概要

- 任务：将 `《PyQt5应用开发》实验手册 -OrinNano_v2.0.docx` 翻译为英文 Word 文档。
- 源语言：`zh-CN`。
- 目标语言：`en-001` 国际英文。
- 译文风格：专业技术手册。
- 分支：`translation/pyqt5-orinnano-manual-zh-CN-en-001`。
- 工作树：`/Users/henryzhu/project/translation-workspace/.worktrees/pyqt5-orinnano-manual-zh-CN-en-001`。
- 所有翻译、抽取、回写、审校和验收工作都必须在该工作树内完成，并遵循仓库 `AGENTS.md`。
- 执行本计划时必须落地真实项目文档，不能只停留在分析、说明或计划文本。

## 当前状态

- 已创建独立翻译分支。
- 已创建独立工作树。
- 已将源文档复制到：
  `source/pyqt5-orinnano-manual/《PyQt5应用开发》实验手册 -OrinNano_v2.0.docx`
- `source/` 下的源文档副本只能读取，不得覆盖、改写或直接编辑。

## 必须产出的文件

- 源文档副本：
  `source/pyqt5-orinnano-manual/《PyQt5应用开发》实验手册 -OrinNano_v2.0.docx`
- 初译工作稿：
  `work/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual.zh-CN-en-001.draft.md`
- 审校工作稿：
  `work/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual.zh-CN-en-001.reviewed.md`
- 术语表：
  `glossary/terms.csv`
- 风格指南：
  `glossary/style-guide.md`
- 最终英文 Word 文档：
  `output/doc/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual - OrinNano_v2.0.en-001.docx`
- QA 记录：
  `output/review/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual - OrinNano_v2.0.qa.md`
- 渲染验收产物：
  `output/review/pyqt5-orinnano-manual/` 或 `tmp/docs/`，并在最终 QA 记录中注明具体位置。

## 执行步骤

1. 在工作树内核验工具环境和依赖。
   - 使用 `python-docx` 读取、抽取和回写 DOCX。
   - 使用 LibreOffice `soffice` 将 DOCX 渲染为 PDF。
   - 使用 Poppler `pdftoppm` 或 `pdf2image` 将 PDF 渲染为 PNG。
   - 如果缺少渲染依赖且无法安装，必须在 QA 文档中记录限制和版式风险。

2. 创建项目脚手架文档。
   - 确保以下目录存在：`work/pyqt5-orinnano-manual/`、`glossary/`、`output/doc/pyqt5-orinnano-manual/`、`output/review/pyqt5-orinnano-manual/`、`tmp/docs/`。
   - 创建 `glossary/terms.csv`，字段为：
     `source,target,source_lang,target_lang,note,status`。
   - 创建 `glossary/style-guide.md`，记录国际英文技术手册风格、术语规则和不可翻译项。

3. 对源 DOCX 做预检查，并把结果写入 QA。
   - 如果渲染工具可用，记录源文档页数。
   - 记录段落、表格、图片/媒体、绘图对象、字段、页眉页脚、批注、脚注、文本框、嵌入对象和修订痕迹情况。
   - 初步检查已知风险：约 132 页、21 个表格、211 个媒体文件、215 个绘图节点、69 个字段或目录/引用标记、1 个页脚；未发现批注、脚注、文本框、嵌入对象或修订痕迹。
   - 图片和截图中的中文不做本地化处理，必须在 QA 中作为已知风险记录。

4. 抽取可编辑文本并创建初译工作稿。
   - 抽取标题、正文段落、表格单元格、图题/表题、页脚文本，以及需要处理的目录可见文本。
   - 保留结构标识，确保译文能映射回 DOCX 的原始位置。
   - 保留代码、命令、文件路径、API 名称、产品名、URL、变量、占位符、数字、单位、版本号、引用和交叉引用标记。

5. 将可编辑内容翻译为国际英文。
   - 使用清晰、正式、专业的技术手册英文。
   - `OrinNano`、`PyQt5`、`QtDesigner`、`Anaconda3`、`TensorFlow 2`、`Jetson`、命令名、路径和代码标识符等产品/技术名称保持不变，除非上下文明确需要翻译其周边说明。
   - 不改变事实、责任主体、条件、数字、操作顺序、警告语或安全要求。
   - 不翻译、不重绘图片内容。

6. 执行两轮审校并创建审校工作稿。
   - 第一轮：检查准确性、流畅度、语序和专业表达。
   - 第二轮：检查术语一致性、专名、数字、单位、标点、代码、链接、交叉引用、表格内容和残留中文。
   - 最终交付前必须清除所有 `TODO(...)`、占位说明和机器翻译痕迹。

7. 将审校后的英文译文回写为最终 DOCX。
   - 以 `source/` 下的源 DOCX 副本作为格式模板。
   - 尽量保留原文档样式、标题层级、表格结构、图片、绘图对象、题注、编号、页脚、页面设置和字段结构。
   - 最终文件只能保存到：
     `output/doc/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual - OrinNano_v2.0.en-001.docx`

8. 渲染并检查最终 DOCX。
   - 将最终 DOCX 渲染为 PDF 和 PNG 页面。
   - 检查文字重叠、文字截断、乱码、表格破版、图片/题注错位、页眉页脚异常和明显分页问题。
   - 对比源文档和译文档的章节顺序、标题层级、表格数量、媒体数量、目录结构和关键格式。

9. 完成 QA 记录。
   - 记录依赖和工具状态。
   - 记录源文档预检查结果。
   - 记录翻译范围和图片中文不本地化策略。
   - 记录两轮审校检查项。
   - 记录渲染和视觉验收结果。
   - 记录最终交付文件路径。
   - 明确列出任何剩余版式风险或本地化风险。

## 验收标准

- 工作树保持在 `translation/pyqt5-orinnano-manual-zh-CN-en-001` 分支。
- `source/` 下的源 DOCX 副本在复制后未被修改。
- `glossary/terms.csv` 和 `glossary/style-guide.md` 已存在。
- `work/pyqt5-orinnano-manual/` 下已存在初译工作稿和审校工作稿。
- `output/doc/pyqt5-orinnano-manual/` 下已存在最终英文 `.docx`。
- `output/review/pyqt5-orinnano-manual/` 下已存在 QA 记录。
- 最终可编辑文本不包含 `TODO(...)`、占位说明或机器翻译提示语。
- 已完成最终渲染检查；如果无法渲染，必须在 QA 中明确说明原因和版式风险。

