---
name: pdf-tools-compdf
description: >
  Process, convert, edit, and extract data from PDF files using the ComPDF Cloud API. Supports format conversion (Word, Excel, Image), page manipulation (merge, split, compress), watermarking, and OCR text recognition. Use when converting PDF formats, reorganizing pages, adding watermarks, or extracting document content and tables into a structured format for LLM processing or text analysis.
  keywords: PDF to Word, compress PDF, OCR, merge PDF, extract text, powered by the ComPDF Cloud API.
---

# PDF Toolkit

Process PDF files through ComPDF Cloud REST API. Supports 50+ document processing operations.

Official documentation: <https://api.compdf.com/api-reference/overview>

## When to Run

- User requests to convert file format (e.g., "convert this PDF to Word", "convert Excel to PDF")
- User requests to edit PDF pages (e.g., "merge these two PDFs", "delete page 3", "rotate PDF")
- User requests to add or remove watermarks from PDF
- User requests to compress PDF files
- User requests OCR recognition of scanned documents or text in images
- User requests AI extraction or parsing of document content
- User requests to extract tables from images
- User requests batch processing of multiple document files
- User requests to compare differences between two PDF documents
- User mentions ComPDF, compdf, or related keywords

## Workflow

### Step 1 — Obtain API Key

Check whether `config/public_key.txt` exists and contains a non-empty value.

- **If the file exists and is non-empty**: use the stored key (trim whitespace).
- **If the file is missing or empty**: ask the user for their ComPDF API Public Key. Inform them it can be obtained at <https://api-dashboard.compdf.com/api/keys>. After the user provides the key, ask whether they would like to save it locally for future sessions.
  - If the user agrees, write the key to `config/public_key.txt`.
  - If the user declines, use the key for the current session only without saving.

> The key file is **not included in the published skill package**. It is created at runtime only when the user explicitly opts in. The user may delete `config/public_key.txt` at any time to revoke local storage.

### Step 2 — Confirm External Upload Intent

**Before uploading any file**, explicitly inform the user:

> ⚠️ **External Upload Confirmation Required**
>
> Your file will be uploaded to ComPDF's servers (api-server.compdf.com or api-server.compdf.cn) for processing. Please confirm that:
> 1. You consent to uploading this file to external servers.
> 2. The file does not contain highly sensitive or confidential data, or you accept the associated risk.
> 3. You have reviewed ComPDF's Privacy Policy at <https://www.compdf.com/privacy-policy>.

**Only proceed with the upload after receiving explicit user confirmation.**

### Step 3 — Determine Base URL

Ask or infer the user's network environment:

| Environment | Base URL |
|---|---|
| International | `https://api-server.compdf.com/server/v2` |
| Mainland China | `https://api-server.compdf.cn/server/v2` |

### Step 4 — Select Tool

Look up the `executeTypeUrl` for the user's task in `references/tool-list.md`.

Quick reference for common operations:

| Operation | executeTypeUrl |
|---|---|
| PDF → Word | `pdf/docx` |
| PDF → Excel | `pdf/xlsx` |
| PDF → Image | `pdf/img` |
| PDF → Markdown | `pdf/markdown` |
| Word → PDF | `docx/pdf` |
| Merge PDF | `pdf/merge` |
| Split PDF | `pdf/split` |
| Add Watermark | `pdf/addWatermark` |
| PDF Compression | `pdf/compress` |
| OCR | `documentAI/ocr` |
| AI Document Extraction | `idp/documentExtract` |
| AI Document Parsing | `idp/documentParsing` |

For the full list of 50+ tools, see `references/tool-list.md`.

### Step 5 — Build Parameters (optional)

If the selected tool supports custom parameters, look up its JSON schema in `references/parameters.md`. Parameters are passed as a **JSON string** in the `parameter` form-data field. If omitted, server defaults apply.

### Step 6 — Send Request

After the user has explicitly confirmed the external upload:

1. Send a `POST` request to `{baseUrl}/process/{executeTypeUrl}`.
2. Include the user-provided API key in the `x-api-key` header for the current session only.
3. Send the selected file as multipart form-data.
4. Include the `parameter` field only when the selected tool supports custom parameters.
5. Use the synchronous `/process/` endpoint so the complete result is returned in a single response.

Do not send the request until the user has confirmed that the file may be transmitted to ComPDF Cloud.

### Step 7 — Handle Response

**1. Check `code` field** — `"200"` means success; anything else is an error.

**2. Check `taskStatus`** (should be `TaskFinish` for synchronous calls):

| Status | Meaning | Action |
|---|---|---|
| `TaskFinish` | Processing complete | Proceed to download |
| `TaskProcessing` | Still processing internally | Notify user; suggest retrying shortly |
| `TaskOverdue` | Timed out | Retry or split into smaller tasks |

**3. Extract download link** from `fileInfoDTOList[].downloadUrl`.

**4. Warn the user**: download links expire at **24:00 the next day**.

**5. On failure**: read `failureCode` and `failureReason`, then look up troubleshooting advice in `references/error-codes.md`.

**6. On quota exhaustion** (`code` = `"06001"`): inform the user:

> For more credits, please visit <https://api.compdf.com/api/pricing-old>

### Auxiliary Endpoints

| Purpose | Method & Path |
|---|---|
| List supported tools | `GET {baseUrl}/tool/support` |
| Check remaining credits | `GET {baseUrl}/asset/info` |
| List tasks | `GET {baseUrl}/task/list?page=1&size=10` |
| Close a task | `POST {baseUrl}/task/closeTask?taskId={taskId}` |

## Output Format

**On success:**

```
Processing complete!

File: {fileName} → {downFileName}
Status: {taskStatus}
Time taken: {convertTime}ms
Original size: {fileSize} bytes
Result size: {convertSize} bytes
Download link: {downloadUrl}

⚠️ The download link will expire at 24:00 tomorrow, please save it promptly.
```

**On failure:**

```
Processing failed.

Error code: {failureCode}
Reason: {failureReason}
Suggestion: {troubleshooting suggestion from references/error-codes.md}
```

## Critical Rules

1. **HTTP 200 ≠ success** — always check `code` and `taskStatus` in the JSON body.
2. **Max 5 files per task** — split into multiple tasks if more files are needed.
3. **Free tier limit** — 200 files within 30 days.
4. **File type auto-detection** — the API detects uploaded file types; no need to rename extensions.
5. **Encrypted PDFs** — provide the password in the `password` form-data field (separate from `parameter`).
6. **China domain** — mainland China users must replace `compdf.com` with `compdf.cn`.
7. **User-controlled API Key storage** — the key file (`config/public_key.txt`) is never shipped with the skill package. It is created at runtime only when the user explicitly opts in. The user may delete it at any time.
8. **External upload confirmation** — always obtain explicit user consent before uploading files to ComPDF servers.

## License & Copyright

Copyright © 2014-2026 PDF Technologies, Inc., a KDAN Company. All Rights Reserved.

ComPDF and ComPDFKit are trademarks of [PDF Technologies, Inc.](https://www.compdf.com/), a KDAN Company.

This skill package is licensed under the Apache License 2.0. See `LICENSE.txt` for the full license text.

The ComPDF Cloud API is a commercial service provided by PDF Technologies, Inc. Use of the API is subject to the [ComPDF Terms of Service](https://www.compdf.com/terms-of-service) and [Privacy Policy](https://www.compdf.com/privacy-policy).
