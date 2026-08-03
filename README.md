![ComPDF-Comprehensive PDF Solutions](images/ComPDF-ComprehensivePDFSolutions.png)

[English](README.md) | [繁體中文](README_TW.md) | [日本語](README_JA.md) | [简体中文](README_CN.md)

# ComPDF Skills

**ComPDF Skills** provide **PDF and image parsing, data extraction, document format conversion, and PDF processing capabilities** for AI agents, helping them build complete automated document workflows. Before large-model reasoning begins, ComPDF Skills can handle document parsing, OCR, data extraction, and structured preprocessing, turning unstructured files into data that AI can directly understand. This means only the necessary content is passed to the model, reducing token usage, lowering model cost, and significantly improving both document-processing efficiency and answer quality in agent workflows.

> - If ComPDF Skills help your workflow, we'd love your ⭐ **Star** on GitHub.
> - If you have questions, suggestions, or integration ideas, feel free to reach out through **Issues** and **Discussions**.

<p align="center">
  <a href="https://github.com/ComPDFKit/compdf-skills"><img src="https://img.shields.io/github/stars/ComPDFKit/compdf-skills?style=social" alt="GitHub Stars"></a>
  <a href="#"><img src="https://img.shields.io/badge/Agent%20Skills-Ready-3863F1" alt="Agent Skills Ready"></a>
  <a href="#"><img src="https://img.shields.io/badge/License-Free%20to%20Start-FF8A00" alt="Free to Start"></a>
</p>

<p align="center">
  <a href="#why-compdf-skills"><b>Why ComPDF Skills</b></a> •
  <a href="#supported-features"><b>Supported Features</b></a> •
  <a href="#license-and-free-access"><b>License & Free Access</b></a> •
  <a href="#installation-and-enablement"><b>Installation</b></a> •
  <a href="#use-cases-and-example-prompts"><b>Use Cases</b></a> •
  <a href="#support"><b>Support</b></a>
</p>

## Why ComPDF Skills

- Professional AI document-processing capabilities: support PDF and image parsing, OCR, data extraction, format conversion, and page-level processing, turning unstructured documents into structured data that AI agents can directly understand and use more accurately.

- More efficient, lower-cost AI workflows: complete document parsing and preprocessing before model reasoning, and pass only the necessary content to the LLM to reduce token usage, lower model cost, and improve both response speed and workflow efficiency.

- Broad output format support: support Word, Excel, PowerPoint, HTML, Markdown, JSON, CSV, RTF, TXT, image, and other output formats to meet data exchange needs across agent workflows and business systems.

- Free to start and easy to validate: include free monthly document-processing credits so teams can verify value quickly in day-to-day workflows.

## Supported Features

ComPDF Skills provide document conversion, PDF operations, and intelligent parsing and data extraction for agents, as detailed below:

### 1. PDF Parsing and Data Extraction

| Capability                        | Description                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Image Parsing and Data Extraction | Extract text, tables, fields, and structured content from image files for downstream AI workflows and automation. |
| PDF Parsing and Data Extraction   | Extract text, tables, fields, and structured content from PDF files for downstream AI workflows and automation.   |

### 2. PDF and Image Conversion

| Capability            | Description                                                                                                                                               |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PDF to Word           | Convert PDF files into editable Word documents while preserving the original layout, text, images, and formatting as much as possible.                    |
| PDF to Excel          | Convert PDF files into Excel workbooks with support for tables, numbers, and structured business data.                                                    |
| PDF to Slide          | Convert PDF pages into editable PowerPoint slides while preserving the original layout and visual structure as much as possible.                          |
| PDF to HTML           | Convert PDF files into HTML for web display and content reuse while retaining text, images, tables, and layout.                                           |
| PDF to RTF            | Convert PDF files into RTF documents with support for text and image content.                                                                             |
| PDF to Image          | Convert PDF pages into PNG, JPG, JPEG, JPEG2000, BMP, TIFF, TGA, GIF, and WEBP images with configurable resolution and DPI.                               |
| PDF to CSV            | Extract tables from PDF files and export them as CSV, either table by table or as merged output.                                                          |
| PDF to TXT            | Extract text from PDF or scanned PDF files and save it as plain text.                                                                                     |
| PDF to JSON           | Extract text, tables, and images from PDF files and save them as structured JSON.                                                                         |
| PDF to Markdown       | Convert PDF files into Markdown for easier reuse in knowledge bases, developer docs, blog systems, and AI workflows.                                      |
| PDF to Searchable PDF | Run OCR on scanned PDFs and output searchable PDFs with selectable, copyable, and highlightable text for retrieval, archiving, and downstream processing. |
| PDF to Searchable OFD | Run OCR on scanned PDFs and convert them into searchable OFD files for OFD archiving, document circulation, and localized office scenarios.               |
| Word to PDF           | Convert Word documents into PDF while preserving layout, fonts, images, and page structure as much as possible for sharing, archiving, and printing.      |
| PNG to PDF            | Convert PNG images into PDF for easier packaging, sharing, printing, and archiving of screenshots, design files, or supporting image materials.           |
| RTF to PDF            | Convert RTF documents into PDF while preserving core text styling and layout for consistent cross-device viewing and formal output.                       |
| Excel to PDF          | Convert Excel workbooks or spreadsheets into PDF for report sharing, printing, archiving, and preventing accidental formula edits.                        |
| TXT to PDF            | Convert plain TXT files into PDF, making logs, notes, and text instructions easier to organize as fixed-layout documents.                                 |
| CSV to PDF            | Convert CSV table data into PDF for snapshot sharing, review, printing, and business archiving.                                                           |
| Slide to PDF          | Convert PowerPoint presentations into PDF for presentation distribution, cross-device viewing, and formal record keeping.                                 |
| HTML to PDF           | Convert HTML pages or content fragments into PDF for webpage preservation, report export, email archiving, and printable output.                          |
| Image to Word         | Convert JPG, JPEG, PNG, and BMP image files into editable Word documents.                                                                                 |
| Image to Excel        | Convert image files into Excel workbooks with support for tables, text, and numeric content.                                                              |
| Image to PPT          | Convert image files into editable PowerPoint slides while preserving visible layout and content structure as much as possible.                            |
| Image to PDF          | Convert JPG, JPEG, PNG, BMP, and similar image files into PDF for consolidating, sharing, printing, and archiving one or multiple images.                 |
| Image to HTML         | Convert image files into HTML while preserving text, layout, tables, and major visual elements as much as possible.                                       |
| Image to RTF          | Convert image files into RTF documents with support for extracted text and images.                                                                        |
| Image to CSV          | Extract tables from image files and export them as CSV.                                                                                                   |
| Image to TXT          | Extract text from image files and save it as plain text.                                                                                                  |
| Image to JSON         | Extract text, tables, and images from image files and save them as structured JSON.                                                                       |

### 3. PDF Editing and Protection

| Capability       | Description                                                                      |
| ---------------- | -------------------------------------------------------------------------------- |
| Merge PDF Files  | Combine multiple PDF files into a single PDF document.                           |
| Split PDF Files  | Split one PDF file into multiple smaller PDF files.                              |
| Rotate PDF Pages | Rotate selected PDF pages by 90, 180, or 270 degrees.                            |
| Insert Pages     | Insert blank pages, image pages, or pages from another PDF into an existing PDF. |
| Delete Pages     | Remove one or more pages from a PDF file.                                        |
| Extract Pages    | Extract selected pages or page ranges and save them as a new file.               |
| Add Watermark    | Add text or image watermarks to PDF files for branding or usage control.         |
| Remove Watermark | Remove text or image watermarks from supported PDF files.                        |
| Encrypt PDF      | Protect PDF files with AES encryption and permission controls.                   |
| Decrypt PDF      | Remove passwords from authorized PDF files for internal processing or reuse.     |

## License and Free Access

After installing ComPDF Skills, [sign up to get a License](https://www.compdf.com/compdf-portal/signin?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=github_compdfkit_skills_en) and pass the API Key to your agents to start using it for free.

![get-license](images/get-license.png)

## Installation and Enablement

We recommend installing ComPDF Skills from the GitHub Skills repository and keeping each skill directory together with its `SKILL.md`, `docs/`, `scripts/`, and any bundled resources. If the public repository URL is not finalized yet, replace the placeholders below with the actual repository URL or repository path before publishing.

### 1. Get Skills from GitHub

Option A: for platforms that support the Agent Skills standard, install directly from the repository path:

```bash
npx skills add https://github.com/ComPDFKit/compdf-skills -y
```

Option B: manually clone or download the GitHub repository and copy the target skill folder:

```bash
git clone https://github.com/ComPDFKit/compdf-skills.git
```

Copy the target skill directory into each agent's supported Skills or Rules location and keep the full folder structure intact.

### 2. Enable in Mainstream Agent Products

#### Claude Code

1. Install and sign in to Claude Code.
2. Install from the GitHub Skills distribution, or use the published skill install entry if one is available.
3. If you use the repository-folder method, place the skill directory into Claude Code's skills location and restart the session.
4. Start with a natural-language task, or explicitly invoke the skill by name.

If the platform-side published entry is available, the install command usually follows this shape:

```bash
claude skill add <namespace>/<skill-name>
claude skill install <skill-url>
```

#### Windsurf

1. Open your project workspace.
2. Place the downloaded skill folder in `.windsurf/skills/compdf-skills/`, or use the cross-agent compatible path `.agents/skills/compdf-skills/`.
3. Make sure the directory includes `SKILL.md` and all required support files.
4. Open Cascade and Windsurf will automatically discover the skill.
5. Describe the task normally for automatic activation, or use `@compdf-skills` to invoke it manually.

#### Cline

1. Install and open Cline.
2. Place the downloaded skill folder in the project-level path `.cline/skills/compdf-skills/`, or the global path `~/.cline/skills/compdf-skills/`.
3. Open the Cline panel and confirm the skill is discovered and enabled from the Skills entry.
4. Start with a natural-language task, or trigger the skill explicitly with `/compdf-skills`.

#### Cursor

Cursor's current official workflow emphasizes Rules and `AGENTS.md` rather than a standalone native Skills directory.

1. Pull the core instruction files from the ComPDF Skills GitHub repository.
2. Convert the shared guidance into a project rule such as `.cursor/rules/compdf-skills.mdc`, or place an `AGENTS.md` file at the project root as the compatibility layer.
3. Open Cursor Agent or Cursor CLI. The rule files will load automatically based on configuration.
4. Ask for tasks such as conversion, extraction, OCR, or watermarking directly in the agent.

#### Internal Enterprise Agent Platforms

1. Mirror the ComPDF Skills GitHub repository into the internal source-control or artifact system.
2. Maintain `SKILL.md`, versioning, license files, and support scripts in one controlled package.
3. Mount the skills directory into the enterprise agent platform, or transform the core instructions into platform-native rule templates.
4. We recommend the workflow `ComPDF preprocessing + AI reasoning`: parse, convert, and extract first, then pass the result to the model.

## Use Cases and Example Prompts

Upload a PDF, image, or other source file. Enter a task instruction such as extracting tables, converting formats, merging PDFs, or adding watermarks. The agent calls the corresponding ComPDF Skill and returns the result. If deeper analysis is needed, pass the processed output to AI afterward.

**Example scenarios:**

* In ChatGPT, custom agents, and enterprise agent platforms that support skills, users upload reports, white papers, or proposal PDFs, convert them to Markdown or Word first, and then ask AI for summaries, key takeaways, or content restructuring
* In skills-based workflows for invoices, statements, scanned tables, and image attachments, users extract tables and structured data first, then continue with finance review, reimbursement prep, system entry, or automated routing
* When organizing contracts, bids, quotations, delivery files, or archived documents in agent workflows, users first merge, split, watermark, and convert PDFs, then hand them off to AI for organization, naming, or outbound preparation
* In multi-step workflows, users first turn PDF or image files into lightweight CSV, JSON, TXT, or Markdown outputs, then let downstream agents handle field normalization, knowledge-base ingestion, approval flows, or workflow automation

**Example prompts:**

* Convert this PDF into Word and preserve the layout as much as possible.
* Extract all tables from this PDF and export them as CSV.
* Convert this image into JSON and return structured content.
* Merge these PDFs, add a watermark, and return the final file.
* Convert this report into Markdown first, then summarize the key points.

## Support

If you have any questions or suggestions, you are welcome to:

- Submit an `Issue`
- Join the `Discussions`
- [Contact the ComPDF team](https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=github_compdfkit_skills_en) for commercial licensing, enterprise deployment, or large-scale rollout needs

If ComPDF Skills help your workflow, we'd love your ⭐ **Star**.

---

<p align="center">
  <b>Built by the ComPDF team.</b><br>
  <a href="https://www.compdf.com/?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=github_compdfkit_skills_en">Website</a> ·
  <a href="https://www.compdf.com/contact-sales?utm_source=github&utm_medium=referral&utm_campaign=compdf_skills_repo_en&ref_platform_id=github_compdfkit_skills_en">Contact Sales</a> ·
  <a href="#installation-and-enablement">Installation</a>
</p>
