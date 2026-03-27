# ComPDF API Complete Tool Type Reference (executeTypeUrl)

## ComPDF AI API

### Intelligent Applications

| Feature | executeTypeUrl | Description |
|---|---|---|
| Intelligent Document Extraction | `idp/documentExtract` | Intelligently extract structured data from documents |
| Intelligent Document Parsing | `idp/documentParsing` | Parse document content and structure |

### Intelligent Tools

| Feature | executeTypeUrl | Description |
|---|---|---|
| Text Recognition (OCR) | `documentAI/ocr` | Recognize text in images/scanned documents |
| Table Extraction | `documentAI/tableRec` | Extract table data from images |
| Stamp Detection | `documentAI/detectionStamp` | Detect stamps in documents |
| Image Distortion Correction | `documentAI/dewarp` | Correct distortion in photographed/scanned images |
| Image Enhancement | `documentAI/magicColor` | Enhance image quality |

Supported image formats: JPG, PNG, JPEG, TIFF, BMP

---

## Format Conversion API

### PDF to Other Formats

| Feature | executeTypeUrl | Description |
|---|---|---|
| PDF → Word | `pdf/docx` | Convert PDF to Word document |
| PDF → Excel | `pdf/xlsx` | Convert PDF to Excel spreadsheet |
| PDF → PPT | `pdf/pptx` | Convert PDF to PowerPoint presentation |
| PDF → HTML | `pdf/html` | Convert PDF to HTML page |
| PDF → RTF | `pdf/rtf` | Convert PDF to Rich Text Format |
| PDF → Image | `pdf/img` | Convert PDF pages to images |
| PDF → CSV | `pdf/csv` | Convert PDF tables to CSV |
| PDF → TXT | `pdf/txt` | Extract plain text from PDF |
| PDF → JSON | `pdf/json` | Convert PDF content to JSON |
| PDF → Markdown | `pdf/markdown` | Convert PDF to Markdown |

### Other Formats to PDF

| Feature | executeTypeUrl | Description |
|---|---|---|
| Word → PDF | `doc/pdf` or `docx/pdf` | Convert Word document to PDF |
| Excel → PDF | `xls/pdf` or `xlsx/pdf` | Convert Excel spreadsheet to PDF |
| PPT → PDF | `ppt/pdf` or `pptx/pdf` | Convert PowerPoint to PDF |
| TXT → PDF | `txt/pdf` | Convert plain text to PDF |
| HTML → PDF | `html/pdf` | Convert HTML page to PDF |
| RTF → PDF | `rtf/pdf` | Convert Rich Text Format to PDF |
| PNG → PDF | `png/pdf` | Convert PNG image to PDF |
| CSV → PDF | `csv/pdf` | Convert CSV file to PDF |

### Image to Other Formats

| Feature | executeTypeUrl | Description |
|---|---|---|
| Image → Word | `img/docx` | Convert image to Word document |
| Image → Excel | `img/xlsx` | Convert image to Excel spreadsheet |
| Image → PPT | `img/pptx` | Convert image to PowerPoint |
| Image → JSON | `img/json` | Convert image content to JSON |
| Image → TXT | `img/txt` | Extract text from image |
| Image → HTML | `img/html` | Convert image to HTML |
| Image → RTF | `img/rtf` | Convert image to Rich Text Format |
| Image → CSV | `img/csv` | Convert image tables to CSV |
| Image → PDF | `img/pdf` | Convert image to PDF |

Supported image formats: JPG, PNG, JPEG, TIFF, BMP

---

## PDF Page Editing API

| Feature | executeTypeUrl | Description |
|---|---|---|
| Merge PDF | `pdf/merge` | Combine multiple PDFs into one |
| Split PDF | `pdf/split` | Split PDF into multiple files |
| Extract Pages | `pdf/extract` | Extract specific pages from PDF |
| Insert Pages | `pdf/insert` | Insert pages into PDF |
| Delete Pages | `pdf/delete` | Remove specific pages from PDF |
| Rotate Pages | `pdf/rotation` | Rotate PDF pages by angle |

---

## PDF Advanced Features API

| Feature | executeTypeUrl | Description |
|---|---|---|
| Add Watermark | `pdf/addWatermark` | Add text or image watermark to PDF |
| Remove Watermark | `pdf/delWatermark` | Remove watermark from PDF |
| PDF to Editable PDF | `pdf/editable` | Convert scanned PDF to editable PDF |
| PDF Compression | `pdf/compress` | Reduce PDF file size |
| Cover Comparison | `pdf/coverCompare` | Compare visual appearance of two PDFs |
| Content Comparison | `pdf/contentCompare` | Compare text content of two PDFs |
| PDF Standard Conversion | `pdf/convertType` | Convert PDF to PDF/A standard |
| PDF Generation | `pdf/generate` | Generate PDF from structured data |
