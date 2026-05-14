# QA Record: nlp-lab-manual

## Project
- Source language: zh-CN
- Target language: en-US
- Audience: student-facing lab manual
- Source DOCX: `source/nlp-lab-manual/《自然语言处理》实验手册-OrinNano（新麦克风阵列）_v2.1.docx`

## Source Precheck
- Paragraphs: 3775
- Tables: 19
- Inline shapes: 268
- Sections: 1
- Header/footer parts with content: 6
- Rendered source PDF pages: 215
- Baseline render directory: `tmp/docs/source-render/`

## High-Risk Layout Elements
- 19 tables
- 268 inline shapes / 273 drawings
- headers/footers present
- footnotes/endnotes present

## Translation QA Checklist
- [x] All headings, body text, tables, captions, headers/footers, footnotes, and list items translated.
- [x] Product names, commands, code, variables, URLs, numeric values, units, versions, and references preserved by automated translation rules.
- [x] Terminology checked against `glossary/terms.csv` and style guide.
- [x] No visible `TODO(...)`, placeholders, unresolved review notes, or machine-translation markers remain.
- [x] Final DOCX rendered to PDF/PNG and inspected for successful conversion.

## Final Layout QA
- Final DOCX: `output/doc/nlp-lab-manual/NLP实验手册.en-US.docx`
- Final render directory: `tmp/docs/nlp-final/`
- Rendered final PDF pages: 241
- Visible Word text nodes with residual Chinese characters: 0
