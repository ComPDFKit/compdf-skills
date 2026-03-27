# ComPDF Skills

AI agent skills for PDF processing powered by [ComPDF](https://www.compdf.com). Works with **39+ AI coding agents** including Claude Code, Cursor, GitHub Copilot, OpenCode, Windsurf, Gemini CLI, and more.

## Skills

| Skill | Description | Processing |
|---|---|---|
| **pdf-to-word-docx** | Convert PDF/images to Word, Excel, PPT, HTML, Markdown, JSON, CSV, and more (10 formats). AI layout analysis + OCR. | Local (Python SDK) |
| **pdf-editor-compdf** | Split, merge, extract, insert, rotate, delete pages. Document comparison, compression, format conversion (PDF/A, PDF/UA), watermark management. | Local (CLI) |
| **pdf-tools-compdf** | 50+ PDF operations via ComPDF Cloud REST API. Format conversion, page editing, OCR, watermarking, text extraction. | Cloud API |

## Install

### Via [skills.sh](https://skills.sh) (Recommended)

Install all skills:

```bash
npx skills add ComPDFKit/compdf-skills
```

Install a specific skill:

```bash
npx skills add ComPDFKit/compdf-skills@pdf-to-word-docx
npx skills add ComPDFKit/compdf-skills@pdf-editor-compdf
npx skills add ComPDFKit/compdf-skills@pdf-tools-compdf
```

### Via [ClawHub](https://clawhub.ai)

- [pdf-to-word-docx](https://clawhub.ai/youna12345/pdf-to-word-docx)
- [pdf-editor-compdf](https://clawhub.ai/youna12345/pdf-editor-compdf)
- [pdf-tools-compdf](https://clawhub.ai/youna12345/pdf-tools-compdf)

## Requirements

| Skill | Platform | Dependencies |
|---|---|---|
| pdf-to-word-docx | Windows / macOS | Python 3, `pip install ComPDFKitConversion`. AI model (~525MB) auto-downloads on first run. |
| pdf-editor-compdf | Windows / macOS | CLI binary auto-downloads. Windows: .NET Framework. macOS: ComPDFKit.framework. |
| pdf-tools-compdf | Any (cloud) | ComPDF API key ([get one free](https://api.compdf.com)). |

## License

See individual skill directories for license terms.

- **pdf-to-word-docx** — ComPDFKit SDK License (trial: 200 conversions)
- **pdf-editor-compdf** — ComPDFKit SDK License (30-day trial)
- **pdf-tools-compdf** — ComPDF Cloud API Terms of Service
