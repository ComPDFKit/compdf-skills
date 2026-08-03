#!/usr/bin/env python3
"""Create a reviewable snapshot of all ComPDF V2 API pages used by this skill."""

from __future__ import annotations

import html
import re
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests


BASE = "https://www.compdf.com/guides/api-reference/v2/"
PAGES = [
    ("Conversion API catalog", "api-overview"),
    ("PDF API catalog", "api-overview-pdf"),
    ("Authentication", "authentication"),
    ("Request workflow", "request-workflow"),
    ("Close task", "request-close"),
    ("Task list", "task-list"),
    ("Asset information", "asset-info"),
    ("Webhook events", "webhook-events"),
    ("Webhook request example", "example"),
    ("OCR language codes", "ocr-languages"),
    ("Compression parameters", "optimization-flags"),
    ("PDF to Word", "pdf-to-word"),
    ("PDF to Excel", "pdf-to-excel"),
    ("PDF to PPT", "pdf-to-ppt"),
    ("PDF to HTML", "pdf-to-html"),
    ("PDF to RTF", "pdf-to-rtf"),
    ("PDF to image", "pdf-to-image"),
    ("PDF to CSV", "pdf-to-csv"),
    ("PDF to TXT", "pdf-to-txt"),
    ("PDF to JSON", "pdf-to-json"),
    ("PDF to Markdown", "pdf-to-md"),
    ("PDF to OFD", "pdf-to-ofd"),
    ("PDF to editable PDF", "pdf-to-editable-pdf-tool-guide"),
    ("Word to PDF", "word-to-pdf"),
    ("Excel to PDF", "excel-to-pdf"),
    ("PPT to PDF", "ppt-to-pdf"),
    ("TXT to PDF", "txt-to-pdf"),
    ("HTML to PDF", "html-to-pdf"),
    ("RTF to PDF", "rtf-to-pdf"),
    ("PNG and JPG to PDF", "image-to-pdf"),
    ("CSV to PDF", "csv-to-pdf"),
    ("Image to Word", "image-to-word"),
    ("Image to Excel", "image-to-excel"),
    ("Image to PPT", "image-to-ppt"),
    ("Image to JSON", "image-to-json"),
    ("Image to TXT", "image-to-txt"),
    ("Image to HTML", "image-to-html"),
    ("Image to RTF", "image-to-rtf"),
    ("Image to CSV", "image-to-csv"),
    ("Image to PDF", "img-to-pdf"),
    ("Merge", "merge"),
    ("Split", "split"),
    ("Delete pages", "delete"),
    ("Extract pages", "extract"),
    ("Insert pages", "insert"),
    ("Rotate pages", "rotate"),
    ("PDF/A conversion", "pdf-convertType"),
    ("PDF generation", "pdf-generate"),
    ("PDF encryption", "pdf-encrypt"),
    ("PDF decryption", "pdf-decrypt"),
    ("Add watermark", "watermark-guides"),
    ("Remove watermark", "del-watermark-guides"),
    ("Compression", "compress-guides"),
    ("Document comparison", "compare-documents"),
    ("AI overview", "ai/overview"),
    ("AI quickstart", "ai/quickstart"),
    ("AI first request", "ai/first-request"),
    ("AI request modes", "ai/request-modes"),
    ("Document parsing API", "documentParsing"),
    ("AI parsing guide", "ai/parsing-guide"),
    ("AI parsing options", "ai/parsing-guide/parse-options"),
    ("AI parsing response overview", "ai/parsing-guide/response-overview"),
    ("AI parsing page details", "ai/parsing-guide/page-details"),
    ("AI parsing metrics", "ai/parsing-guide/metrics"),
    ("Document extraction API", "documentExtract"),
    ("AI extraction guide", "ai/extract-guide"),
    ("AI extraction modes", "ai/extract-guide/modes"),
    ("AI extract fields", "ai/extract-guide/extract-fields"),
    ("AI extraction response structure", "ai/extract-guide/response-structure"),
]


def page_text(source: str) -> str:
    last_error = None
    for attempt in range(3):
        try:
            response = requests.get(
                source,
                headers={"User-Agent": "Mozilla/5.0 (compatible; compdf-api-skill-reference-sync/1.0)"},
                timeout=60,
            )
            response.raise_for_status()
            document = response.text
            break
        except requests.RequestException as error:
            last_error = error
            if attempt == 2:
                raise RuntimeError(f"Unable to download {source}") from error
            time.sleep(2**attempt)
    main = re.search(r"<main\b[^>]*>(.*?)</main>", document, flags=re.IGNORECASE | re.DOTALL)
    if not main:
        raise RuntimeError("No server-rendered <main> section found")
    content = main.group(1)
    content = re.sub(r"<(?:script|style)\b.*?</(?:script|style)>", "", content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r"</?(?:p|div|section|article|header|footer|li|tr|table|h[1-6]|pre|blockquote)[^>]*>", "\n", content, flags=re.IGNORECASE)
    content = re.sub(r"<br\s*/?>", "\n", content, flags=re.IGNORECASE)
    content = re.sub(r"<[^>]+>", " ", content)
    content = html.unescape(content).replace("\r", "")
    content = re.sub(r"[ \t]+", " ", content)
    content = re.sub(r" *\n *", "\n", content)
    content = re.sub(r"\n{3,}", "\n\n", content).strip()
    if len(content) < 100:
        raise RuntimeError("The documentation page did not contain enough readable content")
    return content


def main() -> None:
    output = Path(__file__).resolve().parent.parent / "references" / "official-api-reference.md"
    sections = [
        "# Official ComPDF V2 API Reference Snapshot",
        "",
        "Generated from the public official documentation. Refresh this file before release so every endpoint and field remains synchronized with the source pages.",
        "",
    ]
    sources = [BASE + path for _, path in PAGES]
    with ThreadPoolExecutor(max_workers=4) as executor:
        contents = list(executor.map(page_text, sources))
    for position, ((title, _), source, content) in enumerate(zip(PAGES, sources, contents), start=1):
        print(f"[{position}/{len(PAGES)}] {source}")
        sections.extend([f"## {title}", "", f"Source: {source}", "", content, ""])
    output.write_text("\n".join(sections).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
