# ComPDF Skills

As part of the KDAN ecosystem, ComPDF Skills work with **39+ AI coding agents** including Claude Code, Cursor, GitHub Copilot, OpenCode, Windsurf, Gemini CLI, and more.



If you find this library helpful, please consider giving us a ⭐ **Star** on GitHub! Have feedback or questions? Join the conversation in our [Discussions](https://github.com/orgs/ComPDFKit/discussions).


**Why ComPDF?**

* **Easy to Use** — Complete complex PDF processing workflows with minimal code. Also supports integration with various low-code platforms, agents, MCP tools, and enterprise workflows such as [Salesforce](https://github.com/ComPDFKit/compdf-web-example-salesforce), [SharePoint](https://www.compdf.com/pdf-sdk/sharepoint?utm_source=github&utm_medium=compdf-skills&utm_campaign=compdf_skills_repo&ref_platform_id=github_compdfkit), [Make](https://www.make.com/en/integrations/compdfkit-pdf-converter), [Zapier](https://zapier.com/apps/compdf/integrations), [ClawHub Skills](https://clawhub.ai/u/compdf-youna), [MCP.SO](https://mcp.so/server/comidp-mcp-server/ComPDF), and [MCPMarket](https://mcpmarket.com/en/server/comidp).

* [**Comprehensive Feature Support**](https://www.compdf.com/pdf-sdk/features-list?utm_source=github&utm_medium=compdf-skills&utm_campaign=compdf_skills_repo&ref_platform_id=github_compdfkit)

* **Secure & Reliable** — Enterprise-grade infrastructure with data privacy compliance.


## Provided Skills

| Skill                 | Description                                                                                                                                     | Processing         |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **pdf-to-word-docx**  | Convert PDF/images to Word, Excel, PPT, HTML, Markdown, JSON, CSV, and more (10 formats). AI layout analysis + OCR.                             | Local (Python SDK) |
| **pdf-editor-compdf** | Split, merge, extract, insert, rotate, delete pages. Document comparison, compression, format conversion (PDF/A, PDF/UA), watermark management. | Local (CLI)        |
| **pdf-tools-compdf**  | 50+ PDF operations via ComPDF Cloud REST API. Format conversion, page editing, OCR, watermarking, text extraction.                              | Cloud API          |


## Free Trial & License

See individual skill directories for license terms.

* **pdf-to-word-docx** — ComPDF Conversion SDK License (trial: 200 conversions)
* **pdf-editor-compdf** — ComPDF SDK License (30-day trial)
* **pdf-tools-compdf** — ComPDF Cloud API Terms of Service (200+ free API calls per months)


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

| Skill             | Platform        | Dependencies                                                                                                                                                 |
| ----------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| pdf-to-word-docx  | Windows / macOS | Python 3, `pip install ComPDFKitConversion`. AI model (~525MB) auto-downloads on first run.                                                                  |
| pdf-editor-compdf | Windows / macOS | CLI binary auto-downloads. Windows: .NET Framework. macOS: ComPDFKit.framework.                                                                              |
| pdf-tools-compdf  | Any (cloud)     | ComPDF API key ([get one free](https://api.compdf.com?utm_source=github&utm_medium=compdf-skills&utm_campaign=compdf_skills_repo&ref_platform_id=github_compdfkit)). |
