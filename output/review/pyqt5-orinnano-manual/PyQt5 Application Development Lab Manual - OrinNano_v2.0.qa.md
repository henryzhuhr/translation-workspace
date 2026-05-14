# PyQt5 Application Development Lab Manual - OrinNano_v2.0 QA Record

## Project

- Source document: `source/pyqt5-orinnano-manual/《PyQt5应用开发》实验手册 -OrinNano_v2.0.docx`
- Target document: `output/doc/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual - OrinNano_v2.0.en-001.docx`
- Source language: `zh-CN`
- Target language: `en-001`
- Style: professional technical manual
- Image localisation policy: images and screenshots are preserved as-is; Chinese text inside images is not localised.

## Tool Status

- python-docx: 1.2.0
- pdf2image: available
- deep-translator: available
- LibreOffice soffice: LibreOffice 26.2.3.2
- Poppler pdftoppm: 26.04.0
- Poppler pdfinfo: 26.04.0
- Poppler installation: completed with Homebrew after monitoring the install.

## Source Preflight

- Metadata pages: 132
- Metadata words: 9099
- Main paragraphs: 1257
- Non-empty main paragraphs: 802
- Tables: 21
- Table rows: 83
- Table cells: 182
- Media files: 211
- Drawing nodes: 215
- Chart parts: 0
- SmartArt/diagram parts: 0
- Embedded objects: 0
- Header parts: 1
- Footer parts: 1
- Footnotes: 1
- Endnotes: 1
- Comments: 0
- Text boxes: 0
- Hyperlinks: 0
- Field/TOC/reference markers: 69
- Track revisions setting: False
- Revision markers: 277
- Approximate editable CJK characters before translation: 14699

## Translation Scope

- Editable title, paragraph, table-cell, caption-like paragraph, and footer/header text was processed.
- Product names, code, commands, paths, variables, URLs, numbers, units, and version identifiers were preserved where detected.
- Images and screenshots were not redrawn or OCR-localised.
- Draft file: `work/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual.zh-CN-en-001.draft.md`
- Reviewed file: `work/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual.zh-CN-en-001.reviewed.md`

## Review Passes

- Pass 1 language review: automated pass generated international-English wording for editable text.
- Pass 2 terminology and format QA: fixed-term glossary was applied for key product and technology names.
- Residual editable CJK character count in final DOCX text: 0
- TODO marker count in final DOCX text: 0
- Final DOCX package validation: passed (`zipfile.testzip()` returned no bad entries).
- Final DOCX structure check: 21 tables, 211 media files, 215 drawing nodes, 69 field/TOC/reference markers, and 1 footer part were preserved, matching the source package counts.
- Final DOCX readability check: passed with `python-docx`.

## Render and Layout QA

- Render status: completed.
- Render artifacts:
  - `output/review/pyqt5-orinnano-manual/rendered-final/PyQt5 Application Development Lab Manual - OrinNano_v2.0.en-001.pdf`
  - `output/review/pyqt5-orinnano-manual/rendered-final/page-001.png` through `page-155.png`
  - `output/review/pyqt5-orinnano-manual/rendered-final/pdfinfo.txt`
  - `output/review/pyqt5-orinnano-manual/rendered-final/contact-sheet.png`
- PDF render result: 155 pages, A4, not encrypted.
- PNG render result: 155 pages generated at 120 DPI.
- Automated blank-page check: 0 blank-like pages detected.
- Visual layout inspection status: contact-sheet review completed for representative beginning, middle, and ending pages. No obvious blank rendering, missing images, or garbled text was observed in the sampled pages.

## Remaining Risks

- Image-contained Chinese remains visible in screenshots and other bitmap images by project scope.
- Automated translation may require human subject-matter review before customer-facing publication.
- The rendered English PDF is 155 pages, while the source metadata reported 132 pages; the page count increased because the English text is longer than the Chinese source.
- Directory/TOC fields rendered in English, but they may need manual refresh in Word or LibreOffice if further edits shift page numbers.

## Final Deliverables

- Final DOCX: `output/doc/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual - OrinNano_v2.0.en-001.docx`
- QA record: `output/review/pyqt5-orinnano-manual/PyQt5 Application Development Lab Manual - OrinNano_v2.0.qa.md`
