# ComPDF API Error Code Reference

## HTTP Status Codes

| Status Code | Description |
|---|---|
| 200 | HTTP request successful (does not indicate file processing success—check `code` and `taskStatus` in JSON) |
| 401 | API Key missing or invalid |
| 413 | Request body exceeds size limit |

## Business Error Codes

### 01xxx - System Errors

| Code | Description | Troubleshooting |
|---|---|---|
| 01001 | System internal error | Retry later; if issue persists, contact support@compdf.com |
| 01002 | Failed to upload processed file to server | Retry the task |
| 01003 | File upload failed | Check network connection and file size |
| 01004 | File download failed | Check if download link has expired |
| 01005 | File cannot be empty | Verify the uploaded file is not empty |
| 01006 | File parameter exception | Check JSON format in `parameter` field is correct |
| 01201 | System memory issue | File may be too large; try batch processing |
| 01202 | Unknown error | Contact technical support |
| 01203 | File not found or cannot be opened | Verify file path and format are correct |
| 01204 | Unsupported security mechanism | File uses unsupported encryption method |
| 01206 | CSV file not found | Confirm valid CSV file was uploaded |
| 01207 | DocumentAI API call failed | AI service temporarily unavailable; retry later |
| 01208 | Failed to write recognition results to file | Retry the task |

### 02xxx - File Format Errors

| Code | Description | Troubleshooting |
|---|---|---|
| 02001 | File format error | Verify file format matches executeTypeUrl |
| 02002 | Unsupported conversion format | Check `references/tool-list.md` for supported conversion types |
| 02201 | File is encrypted | Provide correct password in `password` field |
| 02203 | PDF file exception | File may be corrupted; try repairing with another tool before re-uploading |
| 02204 | Unsupported file format (PDF only) | This tool accepts PDF input only |
| 02206 | File content invalid or page does not exist | Check specified page number does not exceed total pages |
| 02207 | Cannot open file: unsupported format or file is encrypted | Verify format is correct and provide password if encrypted |
| 02208 | ExcelXml initialization failed | Excel file may be corrupted |
| 02209 | Conversion timeout—file too large | Use async mode or split file and batch process |
| 02210 | File conversion failed | Check if file is corrupted; try re-uploading |
| 02211 | Converted file size abnormal | Source file may have issues; check and retry |

### 03xxx - Parameter Errors

| Code | Description | Troubleshooting |
|---|---|---|
| 03000 | Parameter validation error | Check field names and values in `parameter` JSON match documentation |

### 04xxx - File Operation Errors

| Code | Description | Troubleshooting |
|---|---|---|
| 04001 | fileKey not found | Task may have expired; resubmit the task |
| 04002 | File size is zero | File is empty; upload valid file |
| 04003 | File not found or cannot be opened | Verify file path and upload success |
| 04004 | Comparison file compression failed | Retry document comparison task |
| 04005 | Document comparison requires exactly two files | Ensure exactly 2 files were uploaded |

### 05xxx - Task Errors

| Code | Description | Troubleshooting |
|---|---|---|
| 05001 | Invalid task | taskId is incorrect or task has been cleaned up |
| 05002 | Task status exception | Recreate the task |
| 05003 | Single task file limit reached (5 files) | Split into multiple tasks |
| 05004 | Task expired without execution | Resubmit the task |
| 05005 | Task requires at least one file | Ensure file was uploaded |

### 06xxx - Quota Errors

| Code | Description | Troubleshooting |
|---|---|---|
| 06001 | File processing quota exhausted | Purchase quota or wait for quota reset; visit https://api.compdf.com/api/pricing-old for more credits |

### 07xxx - Feature Errors

| Code | Description | Troubleshooting |
|---|---|---|
| 07001 | Unsupported feature | Verify the feature is available in current plan |

## Task Status (taskStatus)

| Status Value | Description |
|---|---|
| `TaskStart` | Task created successfully |
| `TaskWaiting` | Task waiting for processing |
| `TaskProcessing` | Task is processing |
| `TaskFinish` | Task processing complete |
| `TaskOverdue` | Task waiting timed out |
