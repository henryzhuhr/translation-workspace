# Style Guide — zh-CN → en-US

## General
- Use natural, professional, formal American English.
- Prefer active voice for instructions; passive voice acceptable for descriptions.
- Keep sentences concise but complete.

## Preserve (do not translate or modify)
- Product names: PyQt5, Qt, QtDesigner, PyCharm, Anaconda3, OrinNano
- Code, API names, variable names, commands, file paths, URLs, placeholders
- Version numbers, dates, numeric values, units
- Figure/table/section cross-reference numbers

## Terminology Rules
- Consistent translation for all Qt widget names (Label, TextEdit, SpinBox, PushButton, CheckBox, etc.)
- "信号与槽" → "Signals and Slots" (must be consistent across all chapters)
- Lab manual chapter/section structure terms must be uniform:
  - 实验目的 → Objective
  - 基础知识 → Background
  - 实验步骤 → Procedure
  - 实验结果 → Results
- "窗口" → "Window", "控件" → "Widget", "布局" → "Layout"

## Formatting
- Chinese quotation marks 「」→ English double quotes
- Chinese book title marks 《》→ italic or plain title
- Full-width punctuation → half-width
- Keep numbering schemes consistent (e.g., "2.1.1" not "II.1.a")

## Uncertain Terms
- Mark as `TODO(term)` — never guess silently
- Add to glossary/terms.csv with status=pending

## Prohibited
- No TODOs, placeholder text, or MT hints in final delivery
- No silent omission of any heading, table, footnote, header, footer, or figure caption
