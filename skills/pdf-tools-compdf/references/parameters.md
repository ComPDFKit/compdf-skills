# ComPDF API Tool Parameter Details

Parameters are passed as JSON strings in the `parameter` field of the request. If not passed, default values are used.

---

## Format Conversion

### PDF to Word (`pdf/docx`)

```json
{
  "enableAiLayout": 1,
  "isContainImg": 1,
  "isContainAnnot": 1,
  "enableOcr": 0,
  "ocrRecognitionLang": "AUTO",
  "pageRanges": "",
  "pageLayoutMode": "e_Flow",
  "formulaToImage": 0,
  "ocrOption": "ALL",
  "isOutputDocumentPerPage": 0,
  "containPageBackgroundImage": 1
}
```

| Parameter | Description | Default |
|---|---|---|
| `enableAiLayout` | Enable AI layout analysis (0=off, 1=on) | 1 |
| `isContainImg` | Include images during conversion (0=off, 1=on) | 1 |
| `isContainAnnot` | Include annotations during conversion (0=off, 1=on) | 1 |
| `enableOcr` | Enable OCR (0=off, 1=on) | 0 |
| `ocrRecognitionLang` | OCR recognition language (see language list below) | AUTO |
| `pageRanges` | Page range, e.g., `"1,2,3-5"`, empty=all pages | "" |
| `pageLayoutMode` | Layout mode: `e_Box`=fixed layout, `e_Flow`=flow layout | e_Flow |
| `formulaToImage` | Convert formulas to images (0=off, 1=on), recommend on for complex formulas | 0 |
| `ocrOption` | OCR recognition scope (see options below) | ALL |
| `isOutputDocumentPerPage` | Output one document per page (0=off, 1=on) | 0 |
| `containPageBackgroundImage` | Include page background images during OCR (0=off, 1=on) | 1 |

**OCR Recognition Language (ocrRecognitionLang):**
AUTO, CHINESE (Simplified Chinese), CHINESE_TRAD (Traditional Chinese), ENGLISH, KOREAN, JAPANESE, LATIN, DEVANAGARI, CYRILLIC, ARABIC, TAMIL, TELUGU, KANNADA, THAI, GREEK, ESLAV (Slavic)

**OCR Recognition Scope (ocrOption):**
- `INVALID_CHARACTER` - Recognize invalid characters in PDF
- `SCAN_PAGE` - Recognize scanned pages in PDF
- `INVALID_CHARACTERAND_SCAN_PAGE` - Recognize invalid characters and scanned pages
- `ALL` - Recognize all characters on all pages

**Layout Mode Differences:**
- `e_Flow` (Flow layout): Suitable for editing, content can be dynamically adjusted. However, display may vary across different software versions.
- `e_Box` (Fixed layout): Maintain original PDF layout unchanged, but less convenient for editing.

---

### PDF to Image (`pdf/img`)

```json
{
  "imageType": "jpg",
  "imgDpi": "300",
  "pageRanges": ""
}
```

| Parameter | Description | Default |
|---|---|---|
| `imageType` | Output image format: `jpg`, `png` | jpg |
| `imgDpi` | Output image DPI | 300 |
| `pageRanges` | Page range, empty=all pages | "" |

---

### PDF to Excel (`pdf/xlsx`)

```json
{
  "isContainImg": 1,
  "isContainAnnot": 1,
  "pageRanges": ""
}
```

| Parameter | Description | Default |
|---|---|---|
| `isContainImg` | Include images (0/1) | 1 |
| `isContainAnnot` | Include annotations (0/1) | 1 |
| `pageRanges` | Page range, empty=all pages | "" |

---

### PDF to HTML (`pdf/html`)

```json
{
  "isContainImg": 1,
  "pageRanges": ""
}
```

| Parameter | Description | Default |
|---|---|---|
| `isContainImg` | Include images (0/1) | 1 |
| `pageRanges` | Page range, empty=all pages | "" |

---

### PDF to TXT (`pdf/txt`)

```json
{
  "pageRanges": ""
}
```

| Parameter | Description | Default |
|---|---|---|
| `pageRanges` | Page range, empty=all pages | "" |

---

### PDF Standard Conversion (`pdf/convertType`)

```json
{
  "convertType": "pdfa1a"
}
```

| Parameter | Description |
|---|---|
| `convertType` | Target PDF standard: `pdfa1a`, `pdfa1b`, `pdfa2a`, `pdfa2b`, `pdfa3a`, `pdfa3b` |

---

## Page Editing

### PDF Merge (`pdf/merge`)

Upload 2-5 files in a single task.

```json
{
  "pageOptions": "['1,2']"
}
```

| Parameter | Description |
|---|---|
| `pageOptions` | String-encoded array specifying page ranges for each uploaded file. Each array element (in single quotes) corresponds to one file in upload order. Format: `"['pages_for_file1','pages_for_file2']"`. Page numbers start from 1, use commas for individual pages and hyphens for ranges (e.g., `1,2,4,6,9-11`). Not passing = merge all pages of all files. |

**Examples:**
- 2 files, all pages from both: omit `pageOptions`
- 2 files, pages 1-3 from file 1, pages 2,5 from file 2: `"['1-3','2,5']"`
- 1 file, pages 1 and 2 only: `"['1,2']"`

---

### PDF Split (`pdf/split`)

```json
{
  "pageOptions": "['1-3','4','5-6']"
}
```

| Parameter | Description |
|---|---|
| `pageOptions` | String-encoded array specifying how to split the PDF. Each array element (in single quotes) defines the page range for one output PDF file. Format: `"['range1','range2','range3']"`. Page numbers start from 1. Use hyphens for ranges and commas for individual pages within each element. |

**Examples:**
- Split into 3 files (pages 1-3, page 4, pages 5-6): `"['1-3','4','5-6']"`
- Split into 2 files (pages 1-5, pages 6-10): `"['1-5','6-10']"`

---

### PDF Extract Pages (`pdf/extract`)

```json
{
  "pageOptions": "['1,3,5-8']"
}
```

| Parameter | Description |
|---|---|
| `pageOptions` | String-encoded array specifying pages to extract. Format: `"['page_range']"`. Page numbers start from 1. Use commas for individual pages and hyphens for ranges inside the single-quoted element. |

**Examples:**
- Extract page 1 only: `"['1']"`
- Extract pages 1, 3, and 5-8: `"['1,3,5-8']"`

---

### PDF Delete Pages (`pdf/delete`)

```json
{
  "pageOptions": "['2,4,6']"
}
```

| Parameter | Description |
|---|---|
| `pageOptions` | String-encoded array specifying pages to delete. Format: `"['page_range']"`. Page numbers start from 1. Use commas for individual pages and hyphens for ranges inside the single-quoted element. |

**Examples:**
- Delete page 1 only: `"['1']"`
- Delete pages 2, 4, and 6: `"['2,4,6']"`

---

### PDF Rotate Pages (`pdf/rotation`)

```json
{
  "pageOptions": "['1-5']",
  "rotation": "90"
}
```

| Parameter | Description |
|---|---|
| `pageOptions` | String-encoded array specifying pages to rotate. Format: `"['page_range']"`. Page numbers start from 1. Use commas for individual pages and hyphens for ranges inside the single-quoted element. |
| `rotation` | Rotation angle: `90`, `180`, `270` |

**Examples:**
- Rotate page 1 by 90°: `"pageOptions": "['1']"`, `"rotation": "90"`
- Rotate pages 1-5 by 180°: `"pageOptions": "['1-5']"`, `"rotation": "180"`

---

### PDF Insert Pages (`pdf/insert`)

Upload 2 files: the main PDF and the PDF to insert. No additional parameters required.

---

## Advanced Features

### Add Watermark (`pdf/addWatermark`)

```json
{
  "type": "text",
  "scale": "1",
  "opacity": "0.5",
  "rotation": "0.785",
  "targetPages": "1-2",
  "vertalign": "center",
  "horizalign": "left",
  "xoffset": "100",
  "yoffset": "100",
  "content": "CONFIDENTIAL",
  "textColor": "#FF0000",
  "front": "",
  "fullScreen": "111",
  "horizontalSpace": "10",
  "verticalSpace": "10",
  "extension": ""
}
```

| Parameter | Description |
|---|---|
| `type` | Watermark type: `text`=text watermark, `image`=image watermark |
| `scale` | Scale ratio (image watermark property) |
| `opacity` | Opacity: 0 (fully transparent) ~ 1 (fully opaque) |
| `rotation` | Rotation angle (radians), positive=counter-clockwise rotation. 0.785 ≈ 45° |
| `targetPages` | Target page range, e.g., `"1,2,4,6,9-11"`, page numbers start from 1 |
| `vertalign` | Vertical alignment: `top`, `center`, `bottom` |
| `horizalign` | Horizontal alignment: `left`, `center`, `right` |
| `xoffset` | Horizontal offset |
| `yoffset` | Vertical offset |
| `content` | Text content (required for text watermark) |
| `textColor` | Text color, hexadecimal format like `"#FF0000"` |
| `front` | Place watermark in foreground layer |
| `fullScreen` | Watermark fills entire page |
| `horizontalSpace` | Horizontal spacing (effective in full-screen mode, default 50) |
| `verticalSpace` | Vertical spacing (effective in full-screen mode, default 50) |
| `extension` | Extension information, base64 encoded |

**Note:** Image watermarks require uploading watermark image file in the `image` field of the request.

---

### Remove Watermark (`pdf/delWatermark`)

No additional parameters required. Simply upload the PDF file directly.

---

### PDF Compression (`pdf/compress`)

```json
{
  "quality": "50"
}
```

| Parameter | Description |
|---|---|
| `quality` | Compression quality, integer 1-100 |

**Compression Quality Reference:**

| Range | Effect |
|---|---|
| 90-100 | Minimal compression, close to original quality |
| 70-85 | Medium compression, high visual quality |
| 50-69 | High compression, acceptable quality |
| 30-49 | Very high compression, obvious quality loss |
| 0-29 | Extreme compression, poor quality |

---

### Document Comparison

#### Cover Comparison (`pdf/coverCompare`) / Content Comparison (`pdf/contentCompare`)

Upload exactly 2 PDF files, no additional parameters required.

---

## General Notes

- All parameters are passed as JSON strings in the `parameter` field
- Page numbers start from 1
- When the `parameter` field is not passed, default values are used
- The `password` field is independent of `parameter`, passed directly as form-data
- For more parameter details on specific tools, please refer to the official documentation: <https://api.compdf.com/api-reference/overview>
