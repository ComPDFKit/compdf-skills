# ComPDF Skills — AI Agent–Ready PDF Processing Toolkit

As part of the KDAN ecosystem, ComPDF Skills work with **39+ AI coding agents** including Claude Code, Cursor, GitHub Copilot, OpenCode, Windsurf, Gemini CLI, and more.

Get started in seconds — no complex setup, just `npx skills add` and you're ready to process PDFs through your AI agent.

> ⭐ Star this repo if you find it helpful! Questions or feedback? Join our [Discussions](https://github.com/ComPDFKit/compdf-skills/discussions).

**Why ComPDF Skills?**

* **Works Everywhere** — Compatible with 39+ AI coding agents and integrates with Salesforce, SharePoint, Make, Zapier, and MCP tools
* **10+ Output Formats** — Word, Excel, PPT, HTML, Markdown, JSON, CSV, RTF, TXT, Image — all from a single skill
* **Local & Cloud Options** — Choose local processing for sensitive documents or cloud API for zero-install convenience
* **Free to Start** — 200 free conversions (SDK trial) or 200+ free monthly API calls
* **Enterprise-Grade** — Secure infrastructure with data privacy compliance

## Requirements

| Skill             | Platform        | Dependencies                                                                                                                                                         |
| ----------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pdf-to-word-docx  | Windows / macOS | Python 3, `pip install ComPDFKitConversion`. AI model (~525MB) auto-downloads on first run.                                                                          |
| pdf-editor-compdf | Windows / macOS | CLI binary auto-downloads. Windows: .NET Framework. macOS: ComPDFKit.framework.                                                                                      |
| pdf-tools-compdf  | Any (cloud)     | ComPDF API key ([get one free](https://api.compdf.com?utm_source=github&utm_medium=compdf-skills&utm_campaign=compdf_skills_repo&ref_platform_id=github_compdfkit)). |

## Free Trial & License

Each ComPDF Skill uses a different license mechanism. See the table below for details and the individual skill sections for step-by-step guidance. If you need to upgrade or purchase, [contact our sales](https://www.compdf.com/contact-sales?utm_source=github&utm_medium=compdf-skills&utm_campaign=compdf_skills_repo&ref_platform_id=github_compdfkit).

| Skill                 | License Type                  | How to Get It                                                                      | Free Trial Limit            | License Storage                                                                        |
| --------------------- | ----------------------------- | ---------------------------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------- |
| **pdf-to-word-docx**  | Commercial (Proprietary)      | Auto-downloaded from `download.compdf.com` on first run                            | 200 conversions             | `scripts/license.xml`                                                                  |
| **pdf-editor-compdf** | Commercial (Proprietary)      | Email activation — skill sends request to `wms.compdf.com/api/license/skillsTrial` | 30-day time-limited trial   | `scripts/win/license_key_windows.xml` (Win)<br>`scripts/mac/license_key_mac.xml` (Mac) |
| **pdf-tools-compdf**  | API Key (Apache 2.0 for code) | Register at ComPDF Cloud console (`api-dashboard.compdf.com/api/keys`)             | 200+ free API call / month) | `config/public_key.txt` (optional, user-consented)                                     |

## Provided Skills

| Skill                 | What It Does                                                                                                                       | Best For                                               | Runs On            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------ |
| **pdf-to-word-docx**  | Convert PDF/image to 10 formats (Word, Excel, PPT, HTML, Image, TXT, JSON, Markdown, RTF, CSV, etc.) with AI layout analysis & OCR | Document conversion, content extraction, archiving     | Local (Python SDK) |
| **pdf-editor-compdf** | Split, merge, extract, insert, rotate, delete pages. Document comparison, compression, PDF/A/UA conversion, watermark management   | Page editing, document assembly, compliance conversion | Local (CLI)        |
| **pdf-tools-compdf**  | 50+ PDF operations via ComPDF Cloud REST API. Format conversion, page editing, OCR, watermarking, text extraction                  | Cloud integration, lightweight calling, no local deps  | Cloud API          |

### pdf-to-word-docx — Convert PDFs/images to 10 Formats

This is a local skill for image and PDF conversion. Converts PDFs and images to Word, Excel, PPT, HTML, Markdown, JSON, CSV, RTF, TXT, and Image with AI-powered layout analysis and OCR.

**Usage examples:**

```bash
# PDF to Word (default: AI layout analysis enabled)
npx skills run pdf-to-word-docx word input.pdf output.docx

# PDF to Excel, one worksheet per page
npx skills run pdf-to-word-docx excel input.pdf output.xlsx --excel-worksheet-option for-page

# PDF to Markdown (great for LLM data prep)
npx skills run pdf-to-word-docx markdown input.pdf output.md

# Scanned image to Word (OCR auto-enabled)
npx skills run pdf-to-word-docx word scan.png output.docx --ocr-language english

# PDF to HTML, multi-page with bookmarks
npx skills run pdf-to-word-docx html input.pdf output_dir --html-option multiple-page-with-bookmark

# PDF with specific page range
npx skills run pdf-to-word-docx word input.pdf output.docx --page-ranges "1-3,5"
```

**When to use:** Batch document archiving, content extraction for LLM input, invoice/contract digitization, scanned document OCR.

> **Trial:** 200 free conversions with auto-downloaded `license.xml` from `download.compdf.com`. AI model (~525MB) downloads on first run. To upgrade, replace `scripts/license.xml` with your purchased license file — no conversion limits.

### pdf-editor-compdf — Full PDF Page Editing

The **pdf-editor-compdf** is designed to edit, compare, and compress PDFs. All processing is **100% local** — no file leaves your machine.

**Usage examples:**

```bash
# Split a PDF into individual pages
npx skills run pdf-editor-compdf split "report.pdf" --mode all --overwrite

# Merge multiple PDFs
npx skills run pdf-editor-compdf merge "a.pdf" "b.pdf" --output "merged.pdf" --overwrite

# Extract pages 2-5
npx skills run pdf-editor-compdf extract "input.pdf" --range 2-5 --output "out.pdf" --overwrite

# Convert to PDF/A-1a for archiving
npx skills run pdf-editor-compdf convert "report.pdf" --standard pdfa-1a --overwrite

# Compress images in a PDF
npx skills run pdf-editor-compdf optimize "report.pdf" --compress-images --image-quality 50 --overwrite

# Add "CONFIDENTIAL" watermark
npx skills run pdf-editor-compdf watermark-text "report.pdf" --text "CONFIDENTIAL" --overwrite

# Compare two PDF versions visually
npx skills run pdf-editor-compdf compare "old.pdf" "new.pdf" --overwrite
```

**When to use:** Contract splitting/merging, version comparison, watermarking, PDF/A compliance for legal/regulatory archives, file size optimization.

> **Trial:** 30-day free SDK license — on first use, provide your email; the skill sends an activation request to `wms.compdf.com/api/license/skillsTrial` and stores the license in `scripts/*/license_key_*.xml`. Run `--help` to confirm activation. CLI binary auto-downloads. To upgrade, [Contact Sales](https://www.compdf.com/contact-sales).

### pdf-tools-compdf — 50+ Cloud PDF Operations

Process PDFs through ComPDF Cloud REST API. Convert formats, edit pages, apply OCR, extract text and tables, and more — no local dependencies required. Works on any platform.

**Usage examples:**

```bash
# PDF to Word (cloud)
npx skills run pdf-tools-compdf --convert pdf/docx --file input.pdf

# PDF to Image
npx skills run pdf-tools-compdf --convert pdf/img --file input.pdf

# Merge PDFs
npx skills run pdf-tools-compdf --convert pdf/merge --file "file1.pdf,file2.pdf"

# OCR a scanned document
npx skills run pdf-tools-compdf --convert documentAI/ocr --file scan.pdf

# Extract structured data with AI
npx skills run pdf-tools-compdf --convert idp/documentExtract --file invoice.pdf

# Compress PDF
npx skills run pdf-tools-compdf --convert pdf/compress --file input.pdf
```

**When to use:** Lightweight cloud integration, no-install environments, batch processing via API, AI-powered document extraction and parsing.

> **Trial:** 200+ free API calls per month. Register at [ComPDF Cloud dashboard](https://api-dashboard.compdf.com/api/keys?utm_source=github&utm_medium=compdf-skills&utm_campaign=compdf_skills_repo&ref_platform_id=github_compdfkit) to get your API Public Key. Authentication is via `x-api-key` HTTP header. The key can be stored in `config/public_key.txt` (optional, user-consented). No local license file required.

## Install

ComPDF Skills are available through multiple installation channels. Choose the one that fits your workflow.

### Via [skills.sh](https://skills.sh) (Recommended)

Install all skills at once with a single command — works across **20+ AI coding agents**:

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

Browse and install individual skills directly from ClawHub:

- [pdf-to-word-docx](https://clawhub.ai/youna12345/pdf-to-word-docx)
- [pdf-editor-compdf](https://clawhub.ai/youna12345/pdf-editor-compdf)
- [pdf-tools-compdf](https://clawhub.ai/youna12345/pdf-tools-compdf)

### Via MCP (Model Context Protocol)

For MCP-compatible agents, use the ComPDF MCP servers:

- [MCP.SO — ComPDF MCP Server](https://mcp.so/server/comidp-mcp-server/ComPDF)
- [MCPMarket — ComPDF MCP Server](https://mcpmarket.com/en/server/comidp)

### Compatible Agents

The `npx skills add` command works out of the box with these AI coding agents:

| Agent              | Notes                                                      |
| ------------------ | ---------------------------------------------------------- |
| **Claude Code**    | Skills load as procedural knowledge across sessions        |
| **Cursor**         | SKILL.md files are auto-referenced by Cursor agents        |
| **GitHub Copilot** | Skills augment project context for edits and chats         |
| **Windsurf**       | Project-specific knowledge persists across sessions        |
| **Gemini CLI**     | Compatible via the skills CLI for repo-scoped install      |
| **OpenCode**       | Full skills.sh integration for repo-scoped skills          |
| **Cline**          | Reads SKILL.md files for project-specific patterns         |
| **Codex**          | OpenAI's coding agent, compatible with skills CLI          |
| **VS Code**        | GitHub Copilot Chat supports the skills CLI                |
| **Zed**            | SKILL.md files are auto-referenced by the built-in agent   |
| **Roo**            | Autonomous coding agent with skills CLI support            |
| **Trae**           | AI coding agent with skills CLI compatibility              |
| **Goose**          | Block's on-machine agent, extends with procedural guidance |
| **AMP**            | Research agent that loads skills as procedural knowledge   |
| **Antigravity**    | Google's developer agent platform                          |
| **ClawdBot**       | Supports skills CLI across sessions                        |
| **Droid**          | Autonomous engineering agent                               |
| **Kilo**           | AI coding agent with project-scoped capabilities           |
| **Kiro CLI**       | Terminal agent with SKILL.md support                       |
| **Nous Research**  | Open agent tooling with skills CLI support                 |
| More Agent ...     |                                                            |

