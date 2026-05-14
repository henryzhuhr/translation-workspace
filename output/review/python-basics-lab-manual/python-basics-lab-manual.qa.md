# QA Record: python-basics-lab-manual

## Project
- Source language: zh-CN
- Target language: en-US
- Audience: student-facing lab manual
- Source DOCX: `source/python-basics-lab-manual/《Python基础》实验手册-OrinNano_v2.0.docx`

## Source Precheck
- Paragraphs: 1851
- Tables: 25
- Inline shapes: 175
- Sections: 2
- Header/footer parts with content: 12
- Rendered source PDF pages: 145
- Baseline render directory: `tmp/docs/source-render/`

## High-Risk Layout Elements
- 25 tables
- 175 inline shapes / 180 drawings
- headers/footers present
- footnotes/endnotes present
- text boxes present

## Translation QA Checklist
- [x] All headings, body text, tables, captions, headers/footers, footnotes, and list items translated.
- [x] Product names, commands, code, variables, URLs, numeric values, units, versions, and references preserved by automated translation rules.
- [x] Terminology checked against `glossary/terms.csv` and style guide.
- [x] No visible `TODO(...)`, placeholders, unresolved review notes, or machine-translation markers remain.
- [x] Final DOCX rendered to PDF/PNG and inspected for successful conversion.

## Final Layout QA
- Final DOCX: `output/doc/python-basics-lab-manual/Python基础实验手册.en-US.docx`
- Final render directory: `tmp/docs/python-basics-final/`
- Rendered final PDF pages: 151
- Visible Word text nodes with residual Chinese characters: 0
- Note: XML still contains Chinese font/theme names such as `宋体` and `黑体`; these are style metadata, not visible source text.
