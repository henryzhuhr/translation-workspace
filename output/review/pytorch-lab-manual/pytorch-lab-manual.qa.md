# QA Record: pytorch-lab-manual

## Project
- Source language: zh-CN
- Target language: en-US
- Audience: student-facing lab manual
- Source DOCX: `source/pytorch-lab-manual/深度学习与Pytorch实验手册-OrinNano_v2.1.docx`

## Source Precheck
- Paragraphs: 4066
- Tables: 21
- Inline shapes: 209
- Sections: 1
- Header/footer parts with content: 6
- Rendered source PDF pages: 252
- Baseline render directory: `tmp/docs/source-render/`

## High-Risk Layout Elements
- 21 tables
- 209 inline shapes / 333 drawings
- headers/footers present
- 6 embedded objects

## Translation QA Checklist
- [x] All headings, body text, tables, captions, headers/footers, footnotes, and list items translated.
- [x] Product names, commands, code, variables, URLs, numeric values, units, versions, and references preserved by automated translation rules.
- [x] Terminology checked against `glossary/terms.csv` and style guide.
- [x] No visible `TODO(...)`, placeholders, unresolved review notes, or machine-translation markers remain.
- [x] Final DOCX rendered to PDF/PNG and inspected for successful conversion.

## Final Layout QA
- Final DOCX: `output/doc/pytorch-lab-manual/PyTorch实验手册.en-US.docx`
- Final render directory: `tmp/docs/pytorch-final/`
- Rendered final PDF pages: 264
- Visible Word text nodes with residual Chinese characters: 1
- Residual Chinese is inside a literal command/path (`Pt_demo/03.TensorBoard的使用`) and was preserved to avoid changing an executable path.
