# Official ComPDF V2 API Reference Snapshot

Generated from the public official documentation. Refresh this file before release so every endpoint and field remains synchronized with the source pages.

## Conversion API catalog

Source: https://www.compdf.com/guides/api-reference/v2/api-overview

API Tool List â

This page summarizes every high-level API capability ComPDF provides, with each feature's purpose and how to invoke it.

Conversion API â

PDF to Others â

Function Description

PDF to Word Convert a PDF document to Word (.doc, .docx).

PDF to Excel Convert a PDF document to Excel (.xls, .xlsx).

PDF to PPT Convert a PDF document to PPT (.ppt, .pptx).

PDF to HTML Convert a PDF document to HTML (.html).

PDF to RTF Convert a PDF to RTF with layout retained.

PDF to Image Convert each page of a PDF to a separate image (.png, .jpg).

PDF to CSV Convert tables in a PDF to CSV.

PDF to TXT Convert a PDF document to plain text (.txt).

PDF to JSON Convert a PDF document to JSON data.

PDF to Markdown Convert a PDF document to Markdown.

PDF to OFD Convert a PDF to the OFD (Open Fixed-layout Document) format.

PDF to Editable PDF Turn scans or read-only PDFs into editable PDFs.

Others to PDF â

Function Description

Word to PDF Convert a Word file to PDF.

Excel to PDF Convert an Excel file to PDF.

PPT to PDF Convert a PPT file to PDF.

TXT to PDF Convert a plain-text TXT file to PDF.

HTML to PDF Convert an HTML page to PDF.

RTF to PDF Convert an RTF file to PDF.

PNG to PDF Convert PNG, JPG and other images to PDF.

CSV to PDF Convert a CSV file to PDF.

Image to Others â

Function Description

Image to Word Convert an image to Word.

Image to Excel Convert an image to Excel.

Image to PPT Convert an image to PPT.

Image to JSON Convert an image to JSON.

Image to TXT Use OCR to recognize text in an image and export it as plain text.

Image to HTML Convert an image to HTML.

Image to RTF Convert an image to RTF.

Image to CSV Convert an image to CSV.

Image to PDF Convert an image to PDF.

## PDF API catalog

Source: https://www.compdf.com/guides/api-reference/v2/api-overview-pdf

API Tool List â

This page summarizes every high-level API capability ComPDF provides, with each feature's purpose and how to invoke it.

PDF API â

Page Edit â

Function Description

Merge Merge multiple PDF files into one.

Split Split a PDF by custom pages or ranges.

Delete Delete specific pages from a PDF.

Extract Extract specific pages to create a new PDF.

Insert Pages Insert pages from another PDF or blank pages into a target PDF at a specified position.

Rotate Rotate PDF pages in 90Â° increments.

PDF Standard â

Function Description

PDF to PDF/A Convert a PDF to the long-term-archival PDF/A specification.

PDF Generation â

Function Description

PDF Generation Generate a PDF from JSON (or other data sources) and a template.

PDF Security â

Function Description

PDF Encryption Set open passwords, owner passwords, and operation permissions for PDFs through the Server API.

PDF Decryption Remove password protection from PDFs through the Server API and get the result file from the response download URL.

Add Watermark Add text or image watermarks to a PDF.

Remove Watermark Remove existing watermarks from a PDF.

PDF Advanced â

Function Description

Compression Losslessly compress and reduce PDF file size.

Document Comparison Compare two documents and highlight differences.

## Authentication

Source: https://www.compdf.com/guides/api-reference/v2/authentication

Authentication â

Every request must include the API token in the authentication header. Otherwise, the API returns an error.

The authentication header has the following format:

http
x-api-key : your_api_public_key_here

1

You can authenticate by setting x-api-key to the project's Public Key directly in the request header. (You can find the Public Key in the API Key section of the ComPDF API console.)

## Request workflow

Source: https://www.compdf.com/guides/api-reference/v2/request-workflow

Request Mode Guide â

ComPDF API offers three request modes for different business scenarios: synchronous , asynchronous , and pre-signed URL . This page compares them side by side and provides the full calling flow for each one to help you choose the best integration approach.

Overview of the Three Modes â

Dimension Synchronous (Sync) Asynchronous (Async) Pre-signed URL (Pre-signed)

Upload method Direct upload: send the file to ComPDF in one multipart/form-data request Direct upload: send the file to ComPDF in one multipart/form-data request The client uploads directly to object storage through a pre-signed URL, and the file does not pass through the business API

File count Single file (except merge endpoints) Single / multiple files Single / multiple files

Blocking Yes . The server returns only after processing finishes No . Returns taskId immediately No . Returns taskId and the upload address immediately

How to get results The sync response returns downloadUrl directly Poll task status / receive Webhook notifications Poll task status / receive Webhook notifications

Recommended file size Small files up to 10 MB 10 MB ~ 50 MB Large files / batch jobs / browser uploads

Server bandwidth usage High (both directions go through the business gateway) High (upload still goes through the business gateway) Low (upload goes through object storage CDN)

Implementation complexity â Easiest ââ Moderate âââ Slightly more complex (one extra signature step)

Typical scenarios Demos, small tools, instant-feedback pages Background batch jobs, async pipelines Browser/mobile uploads, very large files, cross-region uploads

Selection advice

If you are unsure, start with synchronous , then upgrade to asynchronous / pre-signed as needed.

If the business side should not block and files are relatively large, prefer asynchronous .

If files come from browsers or end users, are often larger than 50 MB, or you want to reduce your own server bandwidth pressure, use pre-signed URL .

Pros and Cons â

Synchronous (Sync) â

Pros

One request gets the result, so the logic is the simplest.

Easy to debug; good for examples and tutorials.

Cons

Processing time equals HTTP wait time, so it is prone to gateway / network timeouts .

Larger files are less stable; batch processing is not supported.

Client threads stay occupied, which limits throughput.

Asynchronous (Async) â

Pros

Returns taskId immediately, so the caller is non-blocking.

Supports batch processing and can work with Webhook callbacks for higher throughput.

Good for backend pipelines and scheduled jobs.

Cons

Uploads still go through the business gateway, so single-request body limits still apply .

Requires an extra "check status / handle callback" step.

Pre-signed URL (Pre-signed) â

Pros

Files are uploaded directly to object storage , bypassing the business gateway, so very large files are supported.

Greatly reduces inbound bandwidth / forwarding pressure on your own server.

Ideal for direct uploads from browsers, mini programs, or mobile apps.

Cons

The call chain is longest (get signature â upload â trigger task â query result).

The client must handle PUT / POST upload protocols.

Call Flow â

1. Synchronous Request Flow â

1 Client starts POST multipart/form-data file + parameter + x-api-key

2 Server processing Finish conversion / parsing task HTTP connection stays open

3 Sync response Returns downloadUrl code / status / taskId

4 Download result Via downloadUrl Link has an expiration time

Key points

One request completes the full "upload + process + return" flow, so the chain is shortest.

Because HTTP long connections are affected by gateway timeouts, we recommend tasks with a single file of 10 MB or less and an expected processing time under 60 seconds.

The sync API supports only one file (except merge endpoints).

See Complete Example for a full runnable sample.

2. Asynchronous Request Flow â

1 Submit task POST uploads files multipart/form-data

2 Return immediately taskId status = TaskWaiting

3 Server processing Async queue scheduling Client can do other work in parallel 4 Polling / callback Query task status or receive Webhook

5 Download result downloadUrl

Key points

You get taskId immediately after upload, so the caller is not blocked.

Query the status through Get Task List / Get Asset Details ; we recommend a polling interval of at least 3 seconds .

Pair it with Webhook Events to receive task-completion notifications and avoid useless polling.

It is well suited for backend batch jobs, overnight jobs, and products where users return later to check the result.

3. Pre-signed URL Request Flow â

1 Create task Get taskId and pre-signed uploadUrl

2 Upload file directly PUT to object storage Bypasses the business gateway

3 Execute task Notify the server Triggered with taskId 4 Server processing Async processing Supports very large files

5 Polling / callback Query task status or Webhook notifications

6 Download result Via downloadUrl Link has an expiration time

Key points

The biggest difference from the async flow is steps 1 and 2 : you first get a pre-signed URL, and the client uploads directly to object storage .

The upload step does not pass through the ComPDF business gateway, so it is not limited by the single-request body size , which makes it ideal for large files / browser uploads.

After you get the pre-signed URL, complete the upload within its validity period (usually 15 to 30 minutes).

The later stepsâ"execute â query / callback â download"âare the same as the async mode.

General Notes â

File download links returned by the API are usually deleted at 24:00 the next day ; please download them in time.

When calling the API, pay attention to the parameter style (query / form / json) and whether the auth header x-api-key is required.

HTTP status 200 means your HTTP request succeeded, not that file processing succeeded ; use the code field in the response body as the business result.

For mainland China access, replace https://api-server.compdf.com/ with https://api-server.compdf.cn/ in all request URLs.

If you want automatic notification when a task finishes, use Webhook Events to avoid high-frequency polling.

## Close task

Source: https://www.compdf.com/guides/api-reference/v2/request-close

Close Task Request â

After you send a task processing request, you can call the close task endpoint if needed:

Request method:

Method: POST.

Parameter style: Query.

Request parameters:

Parameter Data type Description Required

taskId String Task ID Yes

language Integer Error message language (1 = English, 2 = Chinese) No

Request URL:

https://api-server.compdf.com/server/v2/task/closeTask

Response:

json
" code " : " 200 " ,
" msg " : " success "

1
2

## Task list

Source: https://www.compdf.com/guides/api-reference/v2/task-list

Get Task List â

Query the current user's file processing task list. Use pagination parameters to browse historical tasks and inspect task-level metadata such as status, cost, source type, and target type.

Request Method â

Method: GET

Parameter style: Query

Request Parameters â

Parameter Data type Description Required

page Long Current page number No (defaults to 1)

size Long Items per page No (defaults to 10)

Request URL â

https://api-server.compdf.com/server/v2/task/list

Response Parameters â

Parameter Data type Description

records Array Task records on the current page

total Long Total number of records

size Long Items per page

current Long Current page number

pages Long Total page count

createdBy String Creator

updatedBy String Updater

creationTime LocalDateTime Creation time

updateTime LocalDateTime Update time

id Long Task primary key ID

taskId String Task ID

taskUrl String Original task file folder

taskLoadUrl String Converted task file folder

taskFileNum Integer Number of files in the task

taskSuccessNum Integer Number of successful files

taskFailNum Integer Number of failed files

taskStatus String Task status

assetTypeId Integer Asset type used

taskCost Integer Task cost

taskTime Long Task duration

callbackUrl String Callback URL

server String Server address

sourceType String Source file format

targetType String Target file format

tenantId Long Tenant ID

Response Example â

json
{
" records " : [
{
" createdBy " : null,
" updatedBy " : null,
" creationTime " : " 2022-08-31 15:06:20 " ,
" updateTime " : " 2022-08-31 15:14:44 " ,
" id " : 771751854513061888 ,
" taskId " : " a300c232-0a2d-4e3c-95f2-cfb4604b2018 " ,
" taskUrl " : "" ,
" taskLoadUrl " : "" ,
" taskFileNum " : 3 ,
" taskSuccessNum " : 0 ,
" taskFailNum " : 0 ,
" taskStatus " : " TaskFinish " ,
" assetTypeId " : 0 ,
" taskCost " : 3 ,
" taskTime " : 0 ,
" callbackUrl " : "" ,
" server " : "" ,
" sourceType " : " pdf " ,
" targetType " : " docx " ,
" tenantId " : 1
},
{
" createdBy " : null,
" updatedBy " : null,
" creationTime " : " 2022-08-31 15:25:24 " ,
" updateTime " : " 2022-08-31 15:26:17 " ,
" id " : 771756653954465793 ,
" taskId " : " e74d60a6-fbd3-4d7d-9efa-0dc70297ee0b " ,
" taskUrl " : "" ,
" taskLoadUrl " : "" ,
" taskFileNum " : 3 ,
" taskSuccessNum " : 3 ,
" taskFailNum " : 0 ,
" taskStatus " : " TaskFinish " ,
" assetTypeId " : 0 ,
" taskCost " : 3 ,
" taskTime " : 3 ,
" callbackUrl " : "" ,
" server " : "" ,
" sourceType " : " pdf " ,
" targetType " : " docx " ,
" tenantId " : 1
}
],
" total " : 528 ,
" size " : 2 ,
" current " : 1 ,
" orders " : [],
" optimizeCountSql " : true,
" searchCount " : true,
" countId " : null,
" maxLimit " : null,
" pages " : 264
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57

Task Status â

Status Description

TaskStart Task created successfully

TaskWaiting Task waiting to be processed

TaskProcessing Task is being processed

TaskFinish Task processing completed

TaskOverdue Task waiting timed out

## Asset information

Source: https://www.compdf.com/guides/api-reference/v2/asset-info

Get Asset Information â

Query the remaining assets for the current user, including available balance and withheld balance by asset type.

Request Method â

Method: GET

Parameter style: Query

Request URL â

https://api-server.compdf.com/server/v2/asset/info

Response Parameters â

Parameter Data type Description

tenantAsset Array Asset information list

assetTypeName String Asset type

asset Integer Asset balance

withholdingAsset Integer Total withheld assets

Response Example â

json
{
" code " : " 200 " ,
" msg " : " success " ,
" data " : {
" tenantAsset " : [
{
" assetTypeName " : " SUBSCRIPTIONS " ,
" asset " : 12 ,
" withholdingAsset " : 0
},
{
" assetTypeName " : " PACKAGES " ,
" asset " : 1 ,
" withholdingAsset " : 0
}
]
}
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

Notes â

asset indicates the currently available balance for the asset type.

withholdingAsset indicates assets temporarily reserved by tasks that are being processed or have not yet settled.

## Webhook events

Source: https://www.compdf.com/guides/api-reference/v2/webhook-events

Webhook Events â

Events â

ComPDF API can notify your application about task status updates. You can create and manage your webhooks in the ComPDF API dashboard .

As shown below:

Available Webhook Events â

Event Event description

task.start Triggered when a task is created successfully. Fires every time a new task is created.

task.finish Triggered when all files in a task have finished processing, whether successful or not.

task.overdue Triggered when a waiting task times out. The task has not been executed since creation and reaches the threshold of one hour.

file.start Triggered when a file is uploaded successfully.

file.success Triggered when a file is processed successfully.

file.failed Triggered when file processing fails.

## Webhook request example

Source: https://www.compdf.com/guides/api-reference/v2/example

Webhook Request Example â

Request Mode â

POST https://your-webhook

1

Request Headers â

Content-Type: application/json
ComPDF-Signature: 8fef357511abec47a4a22313c1dcdb8b

1
2

Example â

Request Parameters

Parameter Data type Description

eventName String Current event type

webhookToken String ComPDF-Signature

sendTime Date Send time

eventObject String Object that triggered the current event

java
{
" eventName " : " task.finish " ,
" webhookToken " : " 8fef357511abec47a4a22313c1dcdb8b " ,
" sendTime " : Thu Dec 15 14 : 45 : 47 GMT + 08 : 00 2022 ,
" eventObject " : " e74d60a6-fbd3-4d7d-9efa-0dc70297ee0b "
}

1
2
3
4
5
6

Note:

eventObject :

If the current event type is a task object, eventObject is taskId

If the current event type is a file object, eventObject is fileKey

## OCR language codes

Source: https://www.compdf.com/guides/api-reference/v2/ocr-languages

OCR Language Codes â

The ocrRecognitionLang parameter specifies the OCR recognition language code. The current API uses the original OCR model language codes. Defaults to AUTO (automatic detection).

Code Language

AUTO Auto Detect

CHINESE Simplified Chinese

CHINESE_TRAD Traditional Chinese

ENGLISH English

KOREAN Korean

JAPANESE Japanese

LATIN Latin script

DEVANAGARI Devanagari script

CYRILLIC Cyrillic script

ARABIC Arabic script

TAMIL Tamil

TELUGU Telugu

KANNADA Kannada

THAI Thai

GREEK Greek

ESLAV East Slavic languages

## Compression parameters

Source: https://www.compdf.com/guides/api-reference/v2/optimization-flags

Compression Parameters â

optimizeFlags specifies which optimization actions to apply when compressing a PDF. When calling the PDF Compression API , you can pass multiple flags. In Try it, enter one flag per line; the request is submitted as a list.

You can also enter a JSON array, for example:

json
[ " RMNOTUSE " , " RMEPTOBJ " , " BCOMPRESSIMAGE " ]

1

Flag Description

RMNOTUSE Remove unused objects

RMEPTOBJ Remove empty objects

RMSPEATTR Remove special attributes

RMEMBFONT Remove embedded fonts

RMINVALINK Remove invalid links

RMINVABK Remove invalid bookmarks

BCOMPRESSIMAGE Compress images

RMBK Remove bookmarks

RMANNOT Remove annotations

RMFORM Remove forms

RMMULMEDIA Remove multimedia content

RMDOCINFO Remove document information

RMMEDTADATA Remove metadata

RMOBJDATA Remove object data

RMFILEATTACHMENT Remove file attachments

RMEXTERNCROSSREF Remove external cross-references

RMOTHERAPPDATA Remove other application data

RMHIDERLAYER Remove hidden layers

MERGEVISIBLELAYER Merge visible layers

USEFLATE Use Flate compression

FLAT_REPLACELZW Replace LZW compression with Flate

RMUNUSEDTARGET Remove unused targets

OPTIMIZEPAGECONTENT Optimize page content

OPTIMIZEPDFFASTWEBVIEW Optimize for Fast Web View (linearization)

RMFORMCOMMITIMPORTRESETACTION Remove form submit/import/reset actions

RMJSACTION Remove JavaScript actions

RMPAGETHUMBNAIL Remove page thumbnails

RMREPLACEIMAGE Replace images

RMLABEL Remove page labels

RMPRINTSETTINGS Remove print settings

RMSEARCHINDEX Remove search index

## PDF to Word

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-word

PDF to Word API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert PDF files to editable Word (DOCX) while preserving layout, text, and table structure as much as possible.

â  Tip: If the input file is a scanned PDF, enable OCR for better editable text results.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload PDF file

2 Call PDF to Word (sync)

3 Get conversion result URL

4 Download Word file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/docx

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images (0 = disabled, 1 = enabled). Default is 0. If enabled, formulas are saved as images; otherwise they remain as text.

pageLayoutMode string
Specify the layout mode: e_Box for fixed layout, e_Flow for reflowable layout. Default is e_Flow.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/docx \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to Excel

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-excel

PDF to Excel API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert table content in PDF files to editable Excel (XLSX) for further analysis and editing.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/xlsx

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

excelAllContent integer
Whether to convert all contents to Excel (1 = yes, 0 = no). Default is 1.

excelWorksheetOption string
Excel worksheet option: e_ForTable (one worksheet per table), e_ForPage (one worksheet per page), or e_ForDocument (one worksheet for the whole document). Default is e_ForTable.

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/xlsx \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to PPT

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-ppt

PDF to PPT API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert PDF files to editable PPT (PPTX) for presentation reuse and further editing.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/pptx

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
Page layout mode. Default: e_Flow. Supported values: e_Flow or e_Box.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/pptx \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to HTML

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-html

PDF to HTML API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert PDF content to HTML for web display and downstream integration.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/html

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
Specify the layout mode: e_Box for fixed layout, e_Flow for reflowable layout. Default is e_Flow.

htmlOption string
HTML option: e_SinglePage (single HTML), e_SinglePageWithBookmark (single HTML with bookmark outline), e_MultiPage (multiple HTML files), or e_MultiPageWithBookmark (multiple HTML files with page-to-page navigation). Default is e_SinglePage.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/html \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to RTF

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-rtf

PDF to RTF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert PDF files to RTF for editable rich text output with broad compatibility.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/rtf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
Page layout mode. Default: e_Flow. Supported values: e_Flow or e_Box.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/rtf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to image

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-image

PDF to Image API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Render PDF pages as image files with page-by-page output.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/img

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

imageFormat string
Image format. Supported values: JPG, JPEG, JPEG2000, PNG, BMP, TIFF, TGA, GIF, WEBP. Default is JPG.

imageColorMode string
Image color mode: e_Color (color), e_Gray (grayscale), e_Binary (black and white). Default is e_Color.

imageScaling number
Specify the image scaling ratio. Default is 1.0.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/img \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to CSV

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-csv

PDF to CSV API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Extract table data from PDF files and export it as CSV for analysis and processing.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/csv

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

excelWorksheetOption string
Excel worksheet option: e_ForTable (one worksheet per table), e_ForPage (one worksheet per page), or e_ForDocument (one worksheet for the whole document). Default is e_ForTable.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/csv \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to TXT

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-txt

PDF to TXT API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Extract plain text from PDF files and export it as TXT.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/txt

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

txtTableFormat integer
Whether to format tables when converting PDF to TXT (0 = disabled, 1 = enabled). Default is 1.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/txt \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to JSON

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-json

PDF to JSON API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Parse PDF content into structured JSON for system integration and downstream processing.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/json

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to retain page background images. 0 = do not retain, 1 = retain. Default: 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
Page layout mode. Default: e_Flow. Supported values: e_Flow or e_Box.

resolveType string
Extract JSON content type: TEXT (text only), TABLE (tables only), IMAGE (images only), or EXTRACT (extract all). Default is EXTRACT.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/json \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to Markdown

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-md

PDF to Markdown API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert PDF content to Markdown for knowledge organization and content reuse.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/markdown

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to retain page background images. 0 = do not retain, 1 = retain. Default: 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
Page layout mode. Default: e_Flow. Supported values: e_Flow or e_Box.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/markdown \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to OFD

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-ofd

PDF to OFD API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert PDF files to OFD format.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Execute synchronously

POST https://api-server.compdf.com/server/v2/process/pdf/ofd

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 1 for OFD output because the backend forces OCR on.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to retain page background images. 0 = do not retain, 1 = retain. Default: 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
Page layout mode. Default: e_Flow. Supported values: e_Flow or e_Box.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/ofd \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF to editable PDF

Source: https://www.compdf.com/guides/api-reference/v2/pdf-to-editable-pdf-tool-guide

PDF to Editable PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert scanned or non-editable PDFs into searchable, editable PDF files.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/editable

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Specify page numbers to convert, starting from 1, for example 1-3,6. Default is empty, which means all pages.

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 1 for editable/searchable PDF output.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes, default 0).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
é¡µé¢çå¼æ¨¡å¼ï¼é»è®¤ e_Flowï¼e_Flow æ e_Boxã

transparentText integer
Transparent text overlay (0 = no, 1 = yes, default 1).

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/editable \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Word to PDF

Source: https://www.compdf.com/guides/api-reference/v2/word-to-pdf

Word to PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert Word documents to PDF for fixed-layout output and distribution.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/docx/pdf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/docx/pdf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Excel to PDF

Source: https://www.compdf.com/guides/api-reference/v2/excel-to-pdf

Excel to PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert Excel spreadsheets to PDF for printing, sharing, and archiving.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/xlsx/pdf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/xlsx/pdf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PPT to PDF

Source: https://www.compdf.com/guides/api-reference/v2/ppt-to-pdf

PPT to PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert PPT presentations to PDF for easy cross-platform viewing and sharing.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pptx/pdf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pptx/pdf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## TXT to PDF

Source: https://www.compdf.com/guides/api-reference/v2/txt-to-pdf

TXT to PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert plain TXT content to PDF and quickly generate distributable documents.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/txt/pdf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/txt/pdf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## HTML to PDF

Source: https://www.compdf.com/guides/api-reference/v2/html-to-pdf

HTML to PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert HTML pages or content to PDF for reports, page archiving, and similar scenarios.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/html/pdf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/html/pdf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## RTF to PDF

Source: https://www.compdf.com/guides/api-reference/v2/rtf-to-pdf

RTF to PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert RTF content to PDF with both compatibility and fixed-layout output.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/rtf/pdf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/rtf/pdf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PNG and JPG to PDF

Source: https://www.compdf.com/guides/api-reference/v2/image-to-pdf

Image to PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert one or more images to PDF and combine them in the specified order.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/pdf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/pdf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## CSV to PDF

Source: https://www.compdf.com/guides/api-reference/v2/csv-to-pdf

CSV to PDF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert CSV data to PDF for presentation, sharing, and archiving.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/csv/pdf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/csv/pdf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to Word

Source: https://www.compdf.com/guides/api-reference/v2/image-to-word

Image to Word API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert text and layout content in images to editable Word (DOCX) files.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/docx

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

language integer
API error message language (1 = English, 2 = Chinese)

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images (0 = disabled, 1 = enabled). Default is 0. If enabled, formulas are saved as images; otherwise they remain as text.

pageLayoutMode string
Specify the layout mode: e_Box for fixed layout, e_Flow for reflowable layout. Default is e_Flow.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/docx \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to Excel

Source: https://www.compdf.com/guides/api-reference/v2/image-to-excel

Image to Excel API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Recognize tables in images and convert them to editable Excel (XLSX) files.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/xlsx

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

language integer
API error message language (1 = English, 2 = Chinese)

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

excelAllContent integer
Whether to convert all contents to Excel (1 = yes, 0 = no). Default is 1.

excelWorksheetOption string
Excel worksheet option: e_ForTable (one worksheet per table), e_ForPage (one worksheet per page), or e_ForDocument (one worksheet for the whole document). Default is e_ForTable.

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/xlsx \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to PPT

Source: https://www.compdf.com/guides/api-reference/v2/image-to-ppt

Image to PPT API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert image content to editable PPT (PPTX) for presentation reuse and editing.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/pptx

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

language integer
API error message language (1 = English, 2 = Chinese)

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
é¡µé¢çå¼æ¨¡å¼ï¼é»è®¤ e_Flowï¼e_Flow æ e_Boxã

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/pptx \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to JSON

Source: https://www.compdf.com/guides/api-reference/v2/image-to-json

Image to JSON API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Parse image content into structured JSON for system integration and downstream processing.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/json

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

language integer
API error message language (1 = English, 2 = Chinese)

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
æ¯å¦ä¿çé¡µé¢èæ¯å¾ï¼0=ä¸ä¿çï¼1=ä¿çï¼é»è®¤ 1ï¼ã

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
é¡µé¢çå¼æ¨¡å¼ï¼é»è®¤ e_Flowï¼e_Flow æ e_Boxã

resolveType string
Extract JSON content type: TEXT (text only), TABLE (tables only), IMAGE (images only), or EXTRACT (extract all). Default is EXTRACT.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/json \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to TXT

Source: https://www.compdf.com/guides/api-reference/v2/image-to-txt

Image to TXT API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Extract text from images and export it as TXT.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/txt

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

language integer
API error message language (1 = English, 2 = Chinese)

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

txtTableFormat integer
Whether to format tables when converting PDF to TXT (0 = disabled, 1 = enabled). Default is 1.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/txt \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to HTML

Source: https://www.compdf.com/guides/api-reference/v2/image-to-html

Image to HTML API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert image content to HTML for web display and further processing.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/html

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

language integer
API error message language (1 = English, 2 = Chinese)

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
Specify the layout mode: e_Box for fixed layout, e_Flow for reflowable layout. Default is e_Flow.

htmlOption string
HTML option: e_SinglePage (single HTML), e_SinglePageWithBookmark (single HTML with bookmark outline), e_MultiPage (multiple HTML files), or e_MultiPageWithBookmark (multiple HTML files with page-to-page navigation). Default is e_SinglePage.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/html \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to RTF

Source: https://www.compdf.com/guides/api-reference/v2/image-to-rtf

Image to RTF API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert text content in images to RTF rich text format.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/rtf

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

language integer
API error message language (1 = English, 2 = Chinese)

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

containPageBackgroundImage integer
Whether to include page background images during conversion (0 = disabled, 1 = enabled). This setting is effective only when OCR is enabled. Default is 1.

formulaToImage integer
Whether to convert formulas to images. 0 = keep editable, 1 = convert to images. Default: 0.

pageLayoutMode string
é¡µé¢çå¼æ¨¡å¼ï¼é»è®¤ e_Flowï¼e_Flow æ e_Boxã

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/rtf \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to CSV

Source: https://www.compdf.com/guides/api-reference/v2/image-to-csv

Image to CSV API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Recognize table data in images and export it as CSV.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/img/csv

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

language integer
API error message language (1 = English, 2 = Chinese)

enableOcr integer
Whether to use OCR (0 = disabled, 1 = enabled). Default is 0.

ocrRecognitionLang string
OCR recognition language code. See supported languages .

ocrOption string
OCR recognition scope. Default is ALL: INVALID_CHARACTER (pages with garbled text), SCAN_PAGE (scanned pages), INVALID_CHARACTER_AND_SCAN_PAGE (both), or ALL (all pages).

enableAiLayout integer
Enable AI layout analysis (0 = off, 1 = on, default 1).

isContainImg integer
Preserve images in the output (0 = no, 1 = yes, default 1).

isContainAnnot integer
Preserve annotations in the output (0 = no, 1 = yes, default 1).

excelWorksheetOption string
Excel worksheet option: e_ForTable (one worksheet per table), e_ForPage (one worksheet per page), or e_ForDocument (one worksheet for the whole document). Default is e_ForTable.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/img/csv \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Image to PDF

Source: https://www.compdf.com/guides/api-reference/v2/img-to-pdf

Image to PDF Guide â

Note : Before using the different functions, we recommend reading Request Workflow to understand the basic PDF processing flow. When using different functions, you can set each tool's special parameters when uploading files. The rest of the steps are the same.

Image to PDF:

java
{
" enableOcr " : 0 ,
" ocrRecognitionLang " : " AUTO "
}

1
2
3
4

Required parameters

enableOcr : Whether to use OCR (0: disabled; 1: enabled). Default: 0.

ocrRecognitionLang : OCR recognition language. Supported values:

AUTO: Auto, CHINESE: Simplified Chinese, CHINESE_TRAD: Traditional Chinese, ENGLISH: English, KOREAN: Korean, JAPANESE: Japanese, LATIN: Latin, DEVANAGARI: Devanagari, CYRILLIC: Cyrillic, ARABIC: Arabic, TAMIL: Tamil, TELUGU: Telugu, KANNADA: Kannada, THAI: Thai, GREEK: Greek, ESLAV: Eslav language family. Default: AUTO.

Request example:

Replace apiKey with the publicKey from the console, file with the file you want to convert, and language with the error message language you want.

curl java

curl
curl --location --request POST 'https://api-server.compdf.com/server/v2/process/img/pdf' \
--header 'x-api-key: apiKey' \
--header 'Accept: */*' \
--header 'Connection: keep-alive' \
--header 'Content-Type: multipart/form-data' \
--form 'file=@"file"' \
--form 'parameter="{ \"enableOcr\": 0, \"ocrRecognitionLang\": \"ENGLISH\" }"' \
--form 'language="1"'

1
2
3
4
5
6
7
8

java
import java . io . * ;
import okhttp3 . * ;
public class main {
public static void main ( String [] args ) throws IOException {
OkHttpClient client = new OkHttpClient (). newBuilder ()
. build ();
MediaType mediaType = MediaType . parse ( " text/plain " );
RequestBody body = new MultipartBody . Builder (). setType ( MultipartBody . FORM )
. addFormDataPart ( " file " , " {{file}} " ,
RequestBody . create ( MediaType . parse ( " application/octet-stream " ),
new File ( " <file> " )))
. addFormDataPart ( " language " , " {{language}} " )
. addFormDataPart ( " parameter " , " { \" enableOcr \" : 1 } " )
. build ();
Request request = new Request . Builder ()
. url ( " https://api-server.compdf.com/server/v2/process/img/pdf " )
. method ( " POST " , body )
. addHeader ( " x-api-key " , " {{apiKey}} " )
. build ();
Response response = client . newCall ( request ). execute ();
}
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

Response information:

A successful response returns HTTP 200 OK and a JSON response body with the task details.

Response mode: application/json

Response parameter Data type Description

code String HTTP request status; "200" means success

message String Request message

data Object Returned result

+taskId String Task ID

+taskFileNum int Number of processed files

+taskSuccessNum int Number of successful files

+taskFailNum int Number of failed files

+taskStatus String Task status

+assetTypeId int Asset type ID used

+taskCost int Task cost

+taskTime int Task duration

+sourceType String Source format

+targetType String Target format

+fileInfoDTOList Array Task file information

++fileKey String File key

++taskId String Task ID

++fileName String Source file name

++downFileName String Download file name

++fileUrl String Source file URL

++downloadUrl String File download URL for the result

++sourceType String Source format

++targetType String Target format

++fileSize int File size

++convertSize int Result file size

++convertTime int Processing time

++status String File processing status

++failureCode String Failure error code for file processing

++failureReason String Failure description

++fileParameter String Processing parameters

Response example:

json
" code " : " 200 " ,
" msg " : " success " ,
" data " : {
" taskId " : " f416dbcf-0c10-4f93-ab9e-a835c1f5dba1 " ,
" taskFileNum " : 1 ,
" taskSuccessNum " : 1 ,
" taskFailNum " : 0 ,
" taskStatus " : " <taskStatus> " ,
" assetTypeId " : 0 ,
" taskCost " : 1 ,
" taskTime " : 1 ,
" sourceType " : " <sourceType> " ,
" targetType " : " <targetType> " ,
" fileInfoDTOList " : [
{
" fileKey " : " <fileKey> " ,
" taskId " : " <taskId> " ,
" fileName " : " <fileName> " ,
" downFileName " : " <downFileName> " ,
" fileUrl " : " <fileUrl> " ,
" downloadUrl " : " <downloadUrl> " ,
" sourceType " : " <sourceType> " ,
" targetType " : " <targetType> " ,
" fileSize " : 24475 ,
" convertSize " : 6922 ,
" convertTime " : 8 ,
" status " : " <status> " ,
" failureCode " : "" ,
" failureReason " : "" ,
" fileParameter " : " <fileParameter> "
}
]
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33

Result:

File type Description

.pdf Generated PDF file

Asynchronous request

If you need to use the asynchronous file processing flow, read Asynchronous Request Guide .

## Merge

Source: https://www.compdf.com/guides/api-reference/v2/merge

PDF Merge API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Merge multiple PDF files into a single PDF in order, with per-file page ranges and passwords.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/merge

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File[] *

Choose Files
No file selected

List of PDF files to merge (at least 2). Submission order determines merge order.

password string
Default open password. Use this if all source PDFs share the same password; otherwise use passwords[] for per-file passwords.

language integer
API error message language. 1 = English, 2 = Chinese (default).

filePageRanges array

File 1

File 2

Each row maps 1:1 to a file in the upload list above; fill in one row per file in the same order.

ä¸ file[] åè¡¨ä¸ä¸å¯¹åºçé¡µèå´ï¼æ¯ä¸ªæä»¶åç¬ä¸é¡¹ãé¡µç ä» 1 å¼å§ï¼å¯å¡«å "all" æ "1-3,6"ï¼å¤æ®µä»¥è±æéå·åéï¼ã

passwords array

File 1

File 2

Each row maps 1:1 to a file in the upload list above; fill in one row per file in the same order.

ä¸ file[] åè¡¨ä¸ä¸å¯¹åºçæå¼å¯ç ï¼ä¸éè¦å¯ç çä½ç½®ç¨ç©ºå­ç¬¦ä¸²å ä½ã

outputFileName string
Output PDF file name. Defaults to merged.pdf if not provided.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Array Response data

data[].fileKey String Unique key of the file in the storage system.

data[].taskId String Task ID. Returned after task creation; used to launch conversion or query task status.

data[].fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data[].downFileName String Output file name after conversion.

data[].fileUrl String Source file storage URL or object storage key.

data[].downloadUrl String File download URL

data[].sourceType String Source file type or feature category, e.g. pdf, docx, img, documentAI, idp.

data[].targetType String Target file type or feature, e.g. docx, pdf, split, ocr.

data[].fileSize Integer Source file size in bytes.

data[].convertSize Integer Converted file size in bytes.

data[].convertTime Integer Conversion time for a single file, typically in milliseconds.

data[].status String File processing status. Common values: success, failed, processing, etc.

data[].failureCode String Error code when file conversion fails.

data[].failureReason String Error reason when file conversion fails.

data[].fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/merge \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected] \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": [
{
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
]
}

## Split

Source: https://www.compdf.com/guides/api-reference/v2/split

PDF Split API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Split a PDF file into multiple files by page range.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/split

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

zipFileName string
Output ZIP file name

pages string *
éè¦å¤ççé¡µèå´ãé¡µç ä» 1 å¼å§ï¼å¤æ®µä»¥è±æéå·åéï¼æ¯æ®µå¯å¡«ååé¡µé¡µç æ a-b é­åºé´ãç¤ºä¾ï¼1-3,6 è¡¨ç¤ºç¬¬ 1~3 é¡µåç¬¬ 6 é¡µã

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/split \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Delete pages

Source: https://www.compdf.com/guides/api-reference/v2/delete

PDF Page Deletion API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Delete pages at specified page numbers from a PDF file.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/delete

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pages string *
éè¦å¤ççé¡µèå´ãé¡µç ä» 1 å¼å§ï¼å¤æ®µä»¥è±æéå·åéï¼æ¯æ®µå¯å¡«ååé¡µé¡µç æ a-b é­åºé´ãç¤ºä¾ï¼1-3,6 è¡¨ç¤ºç¬¬ 1~3 é¡µåç¬¬ 6 é¡µã

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/delete \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Extract pages

Source: https://www.compdf.com/guides/api-reference/v2/extract

PDF Page Extraction API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Extract specified pages from a PDF and generate a new PDF file.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/extract

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pages string
éè¦å¤ççé¡µèå´ãé¡µç ä» 1 å¼å§ï¼å¤æ®µä»¥è±æéå·åéï¼æ¯æ®µå¯å¡«ååé¡µé¡µç æ a-b é­åºé´ãç¤ºä¾ï¼1-3,6 è¡¨ç¤ºç¬¬ 1~3 é¡µåç¬¬ 6 é¡µã

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/extract \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Insert pages

Source: https://www.compdf.com/guides/api-reference/v2/insert

PDF Page Insertion API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Insert pages from another PDF or blank pages into a target PDF at a specified position.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

Sync /pdf/insert

POST https://api-server.compdf.com/server/v2/process/pdf/insert

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

actionType string * FROM_PDF BLANK
Operation type. FROM_PDF: insert pages from another PDF (requires 2 files). BLANK: insert blank pages (requires 1 file with width/height).

file File[]

Choose Files
No file selected

Uploaded files. file[0] is the target PDF. file[1] is the source PDF whose pages will be inserted into the target PDF. FROM_PDF requires both files.

index integer *
Insert position, starting from 1. It indicates where pages from the second file will be inserted into the first file.

outputFileName string
Output file name

sourcePages string
Which pages to take from the second file, for example "1-3,6". Leave empty to insert all pages from the second file into the first file.

sourcePageRanges string
Backward-compatible alias of sourcePages

targetPassword string
Target PDF password

insertPassword string
Source PDF password

password string
Upload password for the main file

language integer
API error message language. 1 = English, 2 = Chinese.

â Response Properties

Field Type Description

actionType String Operation type. FROM_PDF: insert pages from another PDF (requires 2 files). BLANK: insert blank pages (requires 1 file with width/height).

code String Business status code

msg String Message

data Object Response data

data.actionType String Operation type. FROM_PDF: insert pages from another PDF (requires 2 files). BLANK: insert blank pages (requires 1 file with width/height).

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/insert \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected] \
--form [email protected]

â Response Example

200 OK

{
"actionType": "<string>",
"code": "200",
"msg": "success",
"data": {
"actionType": "<string>",
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Rotate pages

Source: https://www.compdf.com/guides/api-reference/v2/rotate

PDF Page Rotation API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Rotate specific pages in a PDF to normalize reading and output orientation.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/rotation

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pages string *
éè¦å¤ççé¡µèå´ãé¡µç ä» 1 å¼å§ï¼å¤æ®µä»¥è±æéå·åéï¼æ¯æ®µå¯å¡«ååé¡µé¡µç æ a-b é­åºé´ãç¤ºä¾ï¼1-3,6 è¡¨ç¤ºç¬¬ 1~3 é¡µåç¬¬ 6 é¡µã

angle integer *
Rotation angle: 90, 180, or 270

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/rotation \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF/A conversion

Source: https://www.compdf.com/guides/api-reference/v2/pdf-convertType

PDF Standard Conversion API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Convert PDF files to a target standards-compliant format such as PDF/A.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/convertType

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

standard string *
PDF standard. Supported values: PDFTypeA1a, PDFTypeA1b, PDFTypeA2a, PDFTypeA2u, PDFTypeA2b, PDFTypeX4, PDFTypeE1, PDFTypeUA1. Default: PDFTypeA1a.

iccFile File

Choose File No file selected

ICC profile file

uaTitle string
PDF/UA title (optional for pdfua1)

uaLanguage string
PDF/UA language (optional for pdfua1)

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/convertType \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected] \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF generation

Source: https://www.compdf.com/guides/api-reference/v2/pdf-generate

PDF Generation API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Generate PDF files from templates or input parameters.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/generate

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

generationType string
Generation type: html or template. Auto-detected from template/data/templateFile/dataFile if omitted; defaults to html.

html string
HTML string. Mutually exclusive with htmlFile and htmlUrl.

htmlUrl string
HTTP/HTTPS HTML URL.

htmlFile File

Choose File No file selected

HTML file.

template string
HTML template string. Mutually exclusive with templateFile.

templateFile File

Choose File No file selected

HTML template file.

data string
Template data JSON string. Mutually exclusive with dataFile.

dataFile File

Choose File No file selected

Template data JSON file.

baseUri string
Relative resource base path or URL.

pageWidth number
Page width in pt. Mapped to request.pageSize.width.

pageHeight number
Page height in pt. Mapped to request.pageSize.height.

outputFileName string
Output file name.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/generate \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected] \
--form [email protected] \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## PDF encryption

Source: https://www.compdf.com/guides/api-reference/v2/pdf-encrypt

PDF Encryption API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Set a user password, owner password, and permission controls for one PDF.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

PDF Encryption (Sync)

POST https://api-server.compdf.com/server/v2/process/pdf/encrypt

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

userPassword string
User password. This is the password required to open the encrypted PDF. Fill in at least one of userPassword or ownerPassword.

ownerPassword string
Owner password. This is used for permission control and later permission removal. It can control permissions such as printing, copying, editing, commenting, and form filling. Use a value different from userPassword when possible.

algorithm string rc4 aes128 aes256
Encryption algorithm. Allowed values: rc4, aes128, aes256. Default: rc4.

allowPrint boolean
Whether printing is allowed. Enter true or false. Default: false.

allowCopy boolean
Whether copying PDF content is allowed. Enter true or false. Default: false.

allowDocumentChanges boolean
Whether modifying document content is allowed. Enter true or false. Default: false.

allowDocumentAssembly boolean
Whether page assembly is allowed, such as inserting, deleting, rotating, or reordering pages. Enter true or false. Default: false.

allowCommenting boolean
Whether adding or editing comments is allowed. Enter true or false. Default: false.

allowFormFieldEntry boolean
Whether filling form fields is allowed. Enter true or false. Default: false.

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/encrypt \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected] \
--form algorithm=rc4

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "saas/2026/06/30/ [email protected] ",
"taskId": "bce85055-093a-49da-94c3-7f3fdf3ee527",
"fileName": "input.pdf",
"downFileName": "encrypted.pdf",
"fileUrl": "https://example.com/source.pdf",
"downloadUrl": "https://example.com/result.pdf",
"sourceType": "pdf",
"targetType": "encrypt",
"fileSize": 123456,
"convertSize": 123000,
"convertTime": 1200,
"status": "success",
"failureCode": null,
"failureReason": null,
"fileParameter": "{\"userPassword\":\"123456\",\"algorithm\":\"rc4\"}"
}
}

## PDF decryption

Source: https://www.compdf.com/guides/api-reference/v2/pdf-decrypt

PDF Decryption API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Remove password protection from one encrypted PDF. Enter the source PDF open password or owner password in `password`.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

PDF Decryption (Sync)

POST https://api-server.compdf.com/server/v2/process/pdf/decrypt

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File

Choose File No file selected

Upload file

password string *
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/decrypt \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "saas/2026/06/30/ [email protected] ",
"taskId": "bce85055-093a-49da-94c3-7f3fdf3ee527",
"fileName": "encrypted.pdf",
"downFileName": "decrypted.pdf",
"fileUrl": "https://example.com/source.pdf",
"downloadUrl": "https://example.com/result.pdf",
"sourceType": "pdf",
"targetType": "decrypt",
"fileSize": 123456,
"convertSize": 123000,
"convertTime": 1200,
"status": "success",
"failureCode": null,
"failureReason": null,
"fileParameter": "{\"outputFileName\":\"decrypted.pdf\"}"
}
}

## Add watermark

Source: https://www.compdf.com/guides/api-reference/v2/watermark-guides

PDF Watermark API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Add text or image watermarks to PDF files.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/addWatermark

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

type string *
Watermark type: text or image

text string
Text watermark content

fontSize number
Text font size

fontColor string
Text color, e.g. #D32F2F

opacity number
Opacity (0â1)

rotation number
Rotation angle

horizalign string
Horizontal alignment: left, center, or right

vertalign string
Vertical alignment: top, center, or bottom

horizOffset number
Horizontal offset

vertOffset number
Vertical offset

pages string
åºç¨é¡µèå´ãé¡µç ä» 1 å¼å§ï¼æ ¼å¼å¦ "1-3,6"ï¼é»è®¤ allã

fullScreen boolean
Whether to tile

horizontalSpacing number
Horizontal spacing when tiling

verticalSpacing number
Vertical spacing when tiling

imageFile File

Choose File No file selected

Image watermark file (required when type=image)

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/addWatermark \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected] \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Remove watermark

Source: https://www.compdf.com/guides/api-reference/v2/del-watermark-guides

PDF Watermark Removal API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Remove watermarks from PDF files.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/delWatermark

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

mode string *
Delete mode: tagged or untagged

indices array
Watermark index in tagged mode

pages string
éè¦å¤ççé¡µèå´ãé¡µç ä» 1 å¼å§ï¼å¤æ®µä»¥è±æéå·åéï¼æ¯æ®µå¯å¡«ååé¡µé¡µç æ a-b é­åºé´ãç¤ºä¾ï¼1-3,6 è¡¨ç¤ºç¬¬ 1~3 é¡µåç¬¬ 6 é¡µã

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/delWatermark \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Compression

Source: https://www.compdf.com/guides/api-reference/v2/compress-guides

PDF Compression API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Reduce PDF file size while balancing output clarity and file volume.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/compress

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

optimizeFlags array
Optimization flag list used to specify which optimization actions to apply during compression. In Try it, enter one flag per line; the request is submitted as a list. You can also enter a JSON array, for example ["RMNOTUSE","RMEPTOBJ"]. See the full flag list in Compression Parameters .

imageQuality integer
Image quality (0â100)

colorImageUpperPpi integer
Color image maximum PPI

colorImageTargetPpi integer
Color image target PPI

colorImageCompressAlgorithm string
Color image compression algorithm: jpeg or flate

colorImageQuality integer
Color image quality (0â100)

grayscaleImageUpperPpi integer
Grayscale image maximum PPI

grayscaleImageTargetPpi integer
Grayscale image target PPI

monochromeImageUpperPpi integer
Black-and-white image maximum PPI

monochromeImageTargetPpi integer
Black-and-white image target PPI

monochromeImageCompressAlgorithm string
Black-and-white image compression algorithm: jbig2 or flate

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/compress \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## Document comparison

Source: https://www.compdf.com/guides/api-reference/v2/compare-documents

Document Comparison API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Compare two documents and output their differences.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/pdf/contentCompare

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

mode string *
Compare mode: content or overlay

basePassword string
Base PDF password

comparePassword string
Compare PDF password

replaceColor string
Defines the color of replaced content (default: #93B9FD).

insertColor string
Defines the color of inserted content (default: #C0FFEC).

overlayBaseColor string
Base color in overlay mode

overlayCompareColor string
Compare color in overlay mode

fillAlphaBase integer
Base opacity in overlay mode (0â100)

fillAlphaCompare integer
Compare opacity in overlay mode (0â100)

outputFileName string
Output file name

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Array Response data

data[].fileKey String Unique key of the file in the storage system.

data[].taskId String Task ID. Returned after task creation; used to launch conversion or query task status.

data[].fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data[].downFileName String Output file name after conversion.

data[].fileUrl String Source file storage URL or object storage key.

data[].downloadUrl String File download URL

data[].sourceType String Source file type or feature category, e.g. pdf, docx, img, documentAI, idp.

data[].targetType String Target file type or feature, e.g. docx, pdf, split, ocr.

data[].fileSize Integer Source file size in bytes.

data[].convertSize Integer Converted file size in bytes.

data[].convertTime Integer Conversion time for a single file, typically in milliseconds.

data[].status String File processing status. Common values: success, failed, processing, etc.

data[].failureCode String Error code when file conversion fails.

data[].failureReason String Error reason when file conversion fails.

data[].fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/pdf/contentCompare \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": [
{
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
]
}

## AI overview

Source: https://www.compdf.com/guides/api-reference/v2/ai/overview

ComPDF AI Overview â

ComPDF AI provides Intelligent Document Processing (IDP) APIs under the POST /v2/process/idp/* family. These guides explain concepts, request modes, parsing configuration, and extraction schemas. For full field-level API details, see the corresponding API Reference .

Capabilities â

Capability Path Purpose

Document Parsing idp/documentParsing Parse document structure and produce JSON / tagged Markdown with bbox references

Document Extraction idp/documentExtract Extract key fields and table data; supports layout and vision modes

Core concepts â

Task â each parsing or extraction call creates a task and returns task metadata. Sync mode returns the result directly; async and presigned flows require status polling.

Extraction schema â describes the keys and table headers to extract. Both layout and vision modes take one fixed schema via extract_fields . The schema shape is { name, keys, tableHeaders } .

BBox grounding â layout mode can return page and bbox references so you can map results back to the source document.

Recommended path â

Prerequisites

First request: sync extraction

Request modes

Document parsing guide

Document extraction guide

FAQ & Billing

## AI quickstart

Source: https://www.compdf.com/guides/api-reference/v2/ai/quickstart

Prerequisites â

Get an API Key â

Sign in to the ComPDF console .

Create or copy a publicKey from the API Key page.

Keep the key secret. Do not commit it to frontend code or public repositories.

Authentication â

All ComPDF AI APIs use the API key in the request header:

http
x-api-key : <your-public-key>

1

Quick validation:

bash
curl --location ' https://api-server.compdf.com/server/v2/asset/info ' \
--header ' x-api-key: <your-public-key> '

1
2

code=200 means the key is valid.

Base URLs â

Region Base URL

Global https://api-server.compdf.com/server

China mainland https://api-server.compdf.cn/server

## AI first request

Source: https://www.compdf.com/guides/api-reference/v2/ai/first-request

First request: sync extraction â

This example calls POST /v2/process/idp/documentExtract , uploads a file, and extracts fields with mode=vision (the default mode). Both vision and layout modes take one fixed schema in extract_fields ; for layout extraction, explicitly pass mode=layout .

bash
curl --location --request POST ' https://api-server.compdf.com/server/v2/process/idp/documentExtract ' \
--header ' x-api-key: <your-public-key> ' \
--form ' file=@/path/to/handwriting.pdf ' \
--form ' mode=vision ' \
--form ' extract_fields={"name":"Form","keys":{"Name":{"prompt":"Applicant name","mapping":null}},"tableHeaders":{}} '

1
2
3
4
5

Parameter Required Description

file Yes Source PDF, image, or office document

mode No layout or vision ; defaults to vision

extract_fields Yes JSON string of a single schema used by both vision and layout ; an empty schema triggers AI field auto-extraction

enable_grounding No Whether to return bbox grounding, default true ; this field only needs to be passed when using layout mode.

## AI request modes

Source: https://www.compdf.com/guides/api-reference/v2/ai/request-modes

Request modes â

AI capability paths stay the same; the request prefix and upload workflow change.

Mode Endpoint example Best for

Sync POST /v2/process/idp/documentExtract Small files and interactive demos

Async POST /v2/processAsync/idp/documentExtract Large files, batch jobs, backend queues

Presigned POST /v2/presignedUrl/idp/documentExtract Direct browser upload to object storage and stricter security requirements

Async polling â

Start polling every 2-5 seconds, then back off for large files or busy queues. Stop after your business timeout and let the user retry later.

State Meaning

processing The task is running

completed The result is ready

failed Check failureCode / failureReason

expired The task or download link has expired

Webhook â

Pass callbackUrl for async tasks if you want the service to notify your endpoint when processing completes. See Webhook events .

## Document parsing API

Source: https://www.compdf.com/guides/api-reference/v2/documentParsing

Intelligent Full-Text Parsing API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Perform full-text intelligent parsing on documents and output structured data.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/idp/documentParsing

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Page range. Page numbers start from 1, for example 1-3,6. Empty means all pages.

enableOcr integer
Enable OCR (0 = off, 1 = on)

ocrRecognitionLang string
OCR è¯å«è¯­è¨ä»£ç ï¼ æ¥çæ¯æè¯­è¨ ã

ocrOption string
OCR strategy: ALL, SCAN_PAGE, INVALID_CHARACTER, or INVALID_CHARACTER_AND_SCAN_PAGE

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes)

imageType string
Query parameter image_type for AI Single-Point /parse, e.g. "url" (default).

contentFilter string
Query parameter content_filter for AI Single-Point /parse. Enum: all / table / heading / toc / image / formula. Defaults to "all".

parseOptions string
JSON string for parse configuration, passed as-is to the multipart field parse_options for AI Single-Point. See the ComPDF AI API Reference for full field definitions of parse_options.

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/idp/documentParsing \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected]

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## AI parsing guide

Source: https://www.compdf.com/guides/api-reference/v2/ai/parsing-guide

Document parsing guide â

idp/documentParsing converts a document into structured JSON and Markdown. It is commonly used before extraction, search, RAG, or review workflows.

bash
curl --location --request POST ' https://api-server.compdf.com/server/v2/process/idp/documentParsing ' \
--header ' x-api-key: <your-public-key> ' \
--form ' file=@/path/to/document.pdf ' \
--form ' pageRanges=1-3 ' \
--form ' parseOptions={"applyDocumentTree":true,"mergeTables":true} '

1
2
3
4
5

What this endpoint returns â

For a typical request, the response body contains:

Path What it is used for

code , message , x_request_id Request status and troubleshooting

file_type Parsed input type, for example PDF

result Main parse result object, including page output and summary counters

metrics Page-level processing metadata such as dpi , angle , and duration

image_process Extra image-processing output; usually empty for standard parsing requests

The most commonly used fields inside result are:

Path What it is used for

result.pages Per-page parse output, including structured and content

result.markdown A merged Markdown view of the document

result.catalog Document tree / TOC when hierarchy detection is enabled

result.valid_page_number Number of successfully parsed pages

result.total_page_number Total page count of the input file

result.success_count Count of successfully processed pages or result units

result.detail Flat paragraph-level list merging all pages in reading order

result.excel_base64 Base64-encoded Excel output when export format includes Excel

Recommended reading order â

Start with Parse options to understand request parameters such as image_type , content_filter , options_json , and ignore_labels .

Then read Response structure for the top-level JSON contract.

Use Page details when you need to map headings, tables, and footnotes back to page coordinates.

Use Metrics when you are monitoring processing quality or performance.

## AI parsing options

Source: https://www.compdf.com/guides/api-reference/v2/ai/parsing-guide/parse-options

Parse options â

This page focuses on the request parameters for the parser-style document parsing endpoint. The examples below keep the file upload flow only and use the current public parameter names.

Request parameters â

Parameter Location Type Required Default Description

file form file Yes â Input document file

image_type query string No url How images are embedded in Markdown: url or base64

content_filter query string No all Keep only selected content block types

options_json form JSON string No Built-in defaults Parser configuration merged with the server defaults

image_type â

image_type controls how image content is represented in the Markdown result:

Value Meaning

url Embed image content as accessible URLs

base64 Embed image content inline as Base64

Use url for most frontend and knowledge-base integrations. Choose base64 when you need a fully self-contained Markdown artifact.

content_filter â

content_filter narrows the result to selected block types. Common patterns:

Value Meaning

all Return all content blocks

text Keep only text-related content

table Keep only table-related content

image Keep only image-related content

If your workflow only needs one category, filtering at request time is usually simpler than post-filtering in downstream code.

options_json â

options_json is a JSON string that controls parsing behaviour. Typical options include:

generating a document tree / catalog

merging related table fragments

re-levelling title hierarchy

ignoring headers, footers, footnotes, and similar auxiliary content

Example:

json
{
" applyDocumentTree " : true,
" mergeTables " : true,
" relevelTitles " : true,
" ignore_labels " : [
" number " ,
" footnote " ,
" header " ,
" header_image " ,
" footer " ,
" footer_image " ,
" aside_text "
]
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14

ignore_labels â

ignore_labels is typically passed inside options_json to suppress auxiliary block types in the parse output. The supported labels are:

number

footnote

header

header_image

footer

footer_image

aside_text

To keep all supported auxiliary content, pass an empty array explicitly:

bash
--form ' options_json={"ignore_labels":[]} '

1

Recommendations â

For real-time previews, prefer image_type=url to keep payloads smaller.

For search, extraction, or RAG workflows, use content_filter=text or content_filter=table to reduce downstream processing.

For layout-heavy documents, combine document-tree and table-merge options, then inspect the output with Response overview .

## AI parsing response overview

Source: https://www.compdf.com/guides/api-reference/v2/ai/parsing-guide/response-overview

Response structure â

documentParsing returns a JSON response directly â no secondary download via downloadUrl is needed.

Top-level shape â

The API directly returns the parse result JSON:

json
{
" code " : 200 ,
" message " : " Success " ,
" x_request_id " : " 6512815b16964dc3a04939ebf685d975 " ,
" file_type " : " PDF " ,
" result " : {
" pages " : [ ... ],
" detail " : [ ... ],
" catalog " : {},
" markdown " : " # Sample PDF ... " ,
" valid_page_number " : 1 ,
" total_page_number " : 1 ,
" success_count " : 1 ,
" excel_base64 " : ""
},
" metrics " : [ ... ],
" image_process " : []
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

Key fields â

Field Meaning

code Business status code. 200 for success; 06001 for insufficient assets (page quota exhausted)

message Human-readable response message

x_request_id Request trace ID for troubleshooting

file_type Detected input type, for example PDF

result Main parse result, including page output and summary counters

metrics Per-page processing metrics for quality and performance analysis

image_process Extra image-processing output; usually empty for standard parse scenarios

The result object â

result is the main payload. Common fields include:

Field Meaning

result.pages Array of per-page parse results, with structured (blocks) and content (lightweight text)

result.detail Flat paragraph-level view merging all page blocks into one ordered array

result.markdown Merged Markdown output

result.catalog Document tree / table of contents

result.valid_page_number Number of successfully parsed pages

result.total_page_number Total pages in the input file

result.success_count Count of successful pages or result units

result.excel_base64 Base64-encoded Excel output when export format includes Excel

Asset insufficient error â

When your page quota is exhausted, the API returns:

json
{
" code " : " 06001 " ,
" msg " : " You have run out of the files which could be processed " ,
" data " : null
}

1
2
3
4
5

How it is usually consumed â

For a full-text reading view, start with result.markdown

For per-page rendering, inspect result.pages

For flat paragraph-level processing, inspect result.detail

For navigation or hierarchy, inspect result.catalog

For quality or performance monitoring, inspect metrics

Reading with other pages â

For the structure inside each page, go to Page details

For request-side tuning, go to Parse options

For metric interpretation, go to Metrics

## AI parsing page details

Source: https://www.compdf.com/guides/api-reference/v2/ai/parsing-guide/page-details

Page details â

result.pages returns parse output page by page. Each page object includes metadata, a structured block list, and a lightweight content list. Additionally, result.detail provides a flat paragraph-level view across all pages.

Page object fields â

Field Type Meaning

page_id int Page number (1-based)

angle float Page rotation angle (after correction)

height int Page pixel height

width int Page pixel width

image_id string Original image identifier (usually empty)

durations float Processing time for this page (seconds)

status string Processing status, e.g. Success

structured array Structured block list for fine-grained rendering and positioning

content array Lightweight content list for quick text access

structured â structured blocks â

Best for detailed rendering, highlight positioning, and content reconstruction. Each block:

Field Type Meaning

id int Block sequence number

type string Block type, e.g. doc_title , paragraph_title , text , table , image

text string Extracted text

pos float[] Quadrilateral coordinates [x1,y1, x2,y2, x3,y3, x4,y4] (top-left, top-right, bottom-right, bottom-left)

outline_level int Heading level (-1 for non-heading)

content int[] Referenced text block IDs linking to the content array

json
{
" id " : 0 ,
" type " : " doc_title " ,
" text " : " # Sample PDF " ,
" pos " : [ 141 , 154 , 509 , 154 , 509 , 220 , 141 , 220 ],
" outline_level " : -1 ,
" content " : [ 0 ]
}

1
2
3
4
5
6
7
8

Common block types:

Type Meaning

doc_title Document title

paragraph_title Paragraph heading

text Body text

table Table

image Image

figure Figure / chart

header / footer Page header / footer

footnote Footnote

formula Formula

content â lightweight content â

Better for quick consumption â concatenate into page-level text or build search indexes. Each item:

Field Type Meaning

id int Content block ID, linked from structured[].content

type string Block type

text string Text content

pos float[] Quadrilateral coordinates

score float Recognition confidence

angle float Text angle

json
{
" id " : 0 ,
" type " : " doc_title " ,
" text " : " # Sample PDF " ,
" pos " : [ 141 , 154 , 509 , 154 , 509 , 220 , 141 , 220 ],
" score " : 0.5958 ,
" angle " : 0
}

1
2
3
4
5
6
7
8

result.detail â cross-page paragraph view â

result.detail aggregates all paragraphs in reading order into a single flat array, eliminating the need to iterate through pages manually. Each record:

Field Type Meaning

paragraph_id int Paragraph sequence number

page_id int Source page number

type string Fixed as paragraph

sub_type string Paragraph sub-type, e.g. doc_title , paragraph_title , text , table

text string Paragraph text

position float[] Quadrilateral coordinates

outline_level int Heading level

tags string[] Custom tags

json
{
" paragraph_id " : 1 ,
" page_id " : 1 ,
" type " : " paragraph " ,
" sub_type " : " doc_title " ,
" text " : " # Sample PDF " ,
" position " : [ 141 , 154 , 509 , 154 , 509 , 220 , 141 , 220 ],
" outline_level " : -1 ,
" tags " : []
}

1
2
3
4
5
6
7
8
9
10

Typical usage â

For UI highlighting, read structured[].pos or content[].pos

For block-level filtering, select by structured[].type

For reading views, use result.markdown or iterate through content

For structured downstream processing, iterate result.pages and consume structured

For cross-page paragraph processing, iterate result.detail directly

Related pages â

See Response overview for the top-level object layout

See Metrics for processing-quality and performance fields

## AI parsing metrics

Source: https://www.compdf.com/guides/api-reference/v2/ai/parsing-guide/metrics

Metrics â

metrics explains how each page was processed. It is useful for troubleshooting, quality monitoring, and performance analysis.

Common fields â

Returned fields may vary slightly by document and processing path, but common metrics usually include:

Field Meaning

page Page number

dpi Effective or detected processing resolution

angle Page skew or correction angle

duration / cost_time Processing time for the page

width / height Page image dimensions

status Processing status for the page

Why these fields matter â

Low dpi often correlates with weaker OCR quality

A non-zero angle means the page required rotation correction

A high duration often indicates dense tables, large images, or complex layouts

Abnormal status values help you isolate failing pages quickly

Recommended usage â

Review metrics together with result.pages during quality analysis

Aggregate duration values for page-level performance monitoring

Record failing page numbers together with x_request_id for retries and support cases

Troubleshooting tips â

If a few pages have poor text quality, inspect dpi and angle first

If a whole document is slow, look for oversized image pages or dense table pages

If only selected pages fail, compare them with the page structure described in Page details

## Document extraction API

Source: https://www.compdf.com/guides/api-reference/v2/documentExtract

Intelligent Document Extraction API

Global endpoint China mainland endpoint

BASE URL https://api-server.compdf.com/server/

â Feature Description

Intelligently extract key fields and structured information from documents.

â Request Mode

Synchronous Request (Sync) â

The API returns the result file directly after processing. Recommended for small files and real-time interactive scenarios that need immediate feedback.

Asynchronous Request (Async)

The API first returns task acceptance information, then you query progress and results with taskId. Suitable for large files and batch workloads.

Secure Request Mode

Upload and process files through secure mechanisms such as pre-signed URLs. Suitable for high-security and privacy compliance scenarios.

âCall Flow

1 Upload file

2 Call API (sync)

3 Get result URL

4 Download file

âUsage Limits

Download validity 24 hours

synchronousæ§è¡

POST https://api-server.compdf.com/server/v2/process/idp/documentExtract

Run (Try it)

â Request Parameters

x-api-key *

Authentication credential sent in the header: x-api-key

Body Parameters multipart/form-data

file File *

Choose File No file selected

Upload file

password string
File password (if the PDF is password-protected)

language integer
API error message language (1 = English, 2 = Chinese)

pageRanges string
Page range. Page numbers start from 1, for example 1-3,6. Empty means all pages.

enableOcr integer
Enable OCR (0 = off, 1 = on)

ocrRecognitionLang string
OCR è¯å«è¯­è¨ä»£ç ï¼ æ¥çæ¯æè¯­è¨ ã

ocrOption string
OCR strategy: ALL, SCAN_PAGE, INVALID_CHARACTER, or INVALID_CHARACTER_AND_SCAN_PAGE

isOutputDocumentPerPage integer
Whether to output one file per page (0 = no, 1 = yes)

mode string layout vision
æ½åæ¨¡å¼ï¼visionï¼é»è®¤ï¼åºäºè§è§æ¨¡åéé¡µæ½åï¼æåä½è¯å«æææ´å¥½ï¼æ layoutï¼åºäºçé¢ç»æçä¸ä½åæ½åï¼æ¯æå¤§æä»¶ãè·¨é¡µä¸ç»ææº¯æºï¼ãä¸¤ç§æ¨¡å¼åä½¿ç¨ extract_fields ä¼ å¥åºå®æ½å schemaã

extractFields string
æ½å schema ç JSON å­ç¬¦ä¸²ï¼snake_case å«åï¼ï¼vision ä¸ layout æ¨¡å¼åä½¿ç¨æ­¤å­æ®µï¼layout æ¨¡å¼ä¸åä½¿ç¨ document_types æ°ç»ã

enableGrounding boolean
å¯éãsnake_case å½¢å¼ï¼

optionsJson string
å¯éãoptions_json æ¯ä¸ä¸ª JSON å­ç¬¦ä¸²ï¼å¯åå«æ¨¡åéç½®åæ°å ignore_labelsï¼ignore_labels ä»æ¯æ numberãfootnoteãheaderãheader_imageãfooterãfooter_imageãaside_textï¼ä¼ å¥å³è¡¨ç¤ºå¿½ç¥ãå®æ´ç¤ºä¾ï¼{"use_doc_unwarping":false,"use_chart_recognition":false,"use_seal_recognition":false,"use_ocr_for_image_block":false,"use_layout_detection":true,"layout_shape_mode":"auto","merge_tables":true,"relevel_titles":true,"concatenate_pages":false,"ignore_labels":[]}

â Response Properties

Field Type Description

code String Business status code

msg String Message

data Object Response data

data.fileKey String Unique key of the file in the storage system.

data.taskId String Task ID

data.fileName String Source file name. Required in presigned mode to generate the object storage upload URL.

data.downFileName String Output file name after conversion.

data.fileUrl String Source file storage URL or object storage key.

data.downloadUrl String File download URL

data.sourceType String Source file type

data.targetType String Target file type

data.fileSize Integer Source file size in bytes.

data.convertSize Integer Converted file size in bytes.

data.convertTime Integer Conversion time for a single file, typically in milliseconds.

data.status String File processing status. Common values: success, failed, processing, etc.

data.failureCode String Error code when file conversion fails.

data.failureReason String Error reason when file conversion fails.

data.fileParameter String Conversion parameter JSON string submitted when creating the task.

ð Request Example

cURL Python JavaScript

curl --request POST \
--url https://api-server.compdf.com/server/v2/process/idp/documentExtract \
--header 'x-api-key: YOUR API-KEY' \
--form [email protected] \
--form mode=vision

â Response Example

200 OK

{
"code": "200",
"msg": "success",
"data": {
"fileKey": "<string>",
"taskId": "<string>",
"fileName": "<string>",
"downFileName": "<string>",
"fileUrl": "<string>",
"downloadUrl": "<string>",
"sourceType": "<string>",
"targetType": "<string>",
"fileSize": 0,
"convertSize": 0,
"convertTime": 0,
"status": "<string>",
"failureCode": "<string>",
"failureReason": "<string>",
"fileParameter": "<string>"
}
}

## AI extraction guide

Source: https://www.compdf.com/guides/api-reference/v2/ai/extract-guide

Document extraction guide â

This guide documents the extraction API with both supported modes: vision and layout .

Guide structure â

Modes

Extract schema

Response structure

Modes at a glance â

Mode Best for Notes

vision Handwritten forms, free-layout scans, image-heavy pages Vision-language extraction mode

layout Stable business documents such as invoices, orders, and contracts Structured extraction mode with optional grounding

Recommended reading order â

Start with Modes to understand the differences and selection advice for the two modes

Then read Extract schema to learn how to write extract schema

Finally read Response structure to understand how the returned results carry field values and grounding information

## AI extraction modes

Source: https://www.compdf.com/guides/api-reference/v2/ai/extract-guide/modes

Extraction modes â

Intelligent document extraction supports two processing modes through the mode field at the unified endpoint /v2/process/idp/documentExtract . When omitted, the backend defaults to vision . Both modes use the same fixed extract_fields schema input :

mode Description Schema input Best for

vision Vision-language model running independently on each page. Handles handwriting and free-form layouts more robustly. extract_fields

layout Layout-aware integrated extraction. Supports large files, cross-page extraction, and bbox grounding for traceable results. extract_fields

Vision mode ( mode=vision , default) â

extract_fields is the JSON string of a single schema object:

bash
curl --location --request POST ' https://api-server.compdf.com/server/v2/process/idp/documentExtract ' \
--header ' x-api-key: public_key ' \
--form ' file=@/path/to/handwriting.pdf ' \
--form ' mode=vision ' \
--form ' extract_fields={"name":"Form","keys":{"Name":{"prompt":"Applicant name","mapping":null}},"tableHeaders":{}} '

1
2
3
4
5

Layout mode ( mode=layout ) â

layout uses the same extract_fields input â a JSON string of one fixed schema object:

bash
curl --location --request POST ' https://api-server.compdf.com/server/v2/process/idp/documentExtract ' \
--header ' x-api-key: public_key ' \
--form ' file=@/path/to/invoice.pdf ' \
--form ' mode=layout ' \
--form ' extract_fields={"name":"ShipmentList","keys":{"OrderNo":{"prompt":null,"mapping":null},"Consignee":{"prompt":null,"mapping":null}},"tableHeaders":{"Table_1":{"No":{"prompt":null,"mapping":null},"ISBN":{"prompt":null,"mapping":null},"BookName":{"prompt":null,"mapping":null},"Qty":{"prompt":null,"mapping":null}}}} ' \
--form ' enable_grounding=true '

1
2
3
4
5
6

When using layout mode, if you need to map results back to the original text, you can enable the enable_grounding parameter; the returned results will include coordinate information for the text blocks corresponding to the fields, facilitating result tracing and highlighting. Additionally, layout mode supports the same options_json parameter as the parsing feature. See Parse options for details.

How to choose â

Start with layout when the document structure is stable, the file is long, or you need to map results back to the source

Switch to vision when the document is handwriting-heavy, scan quality is uneven, or the page layout is highly free-form

Request examples â

bash
--form ' mode=vision '

1

bash
--form ' mode=layout ' \
--form ' enable_grounding=true '

1
2

Next, read Extract schema .

## AI extract fields

Source: https://www.compdf.com/guides/api-reference/v2/ai/extract-guide/extract-fields

Extract schema â

extract_fields is the key input for document extraction. It defines which fields and table headers you want to extract, plus the prompts associated with them.

Base structure â

Both modes use the same single-schema shape:

json
{
" name " : " Invoice " ,
" keys " : {
" Title " : { " prompt " : " Invoice title " , " mapping " : null },
" Date " : { " prompt " : " Invoice date " , " mapping " : null }
},
" tableHeaders " : {
" LineItems " : {
" Item " : { " prompt " : " Item name " , " mapping " : null },
" Amount " : { " prompt " : " Item total " , " mapping " : null }
}
}
}

1
2
3
4
5
6
7
8
9
10
11
12
13

Custom field extraction â fill in keys / tableHeaders to extract a predefined schema.

You can iterate on a schema in the Online Tools site and use its "Export Schema" button to copy the JSON. Paste it directly into extract_fields for both vision and layout modes.

Field reference â

Field Type Meaning

name string Schema name for identification

keys object Scalar key-value fields

tableHeaders object Table field definitions grouped by table name

prompt string Instructional prompt for the model; can be null

mapping string Optional mapping metadata for your downstream system; can be null

When to use keys â

Populate keys when you already know which scalar fields you need, for example:

invoice number

issue date

consignee

contract ID

When to use tableHeaders â

If the target document contains line-item tables, fee tables, or other repeated tabular structures, define them in tableHeaders so the output lands in a more stable format.

json
{
" name " : " auto " ,
" keys " : {},
" tableHeaders " : {}
}

1
2
3
4
5

Recommendations â

Next, see Response structure for how extracted values and grounding data are returned.

## AI extraction response structure

Source: https://www.compdf.com/guides/api-reference/v2/ai/extract-guide/response-structure

Response structure â

The extraction result can be understood as "field output plus optional grounding data". When enable_grounding is enabled, the response can include bbox references back to the source page.

Top-level view â

The API returns a standard task-level response. The extraction result (fields, tables, pages, etc.) is available in the downloaded file referenced by downloadUrl or fileUrl .

json
{
" code " : " 200 " ,
" msg " : " success " ,
" data " : {
" fileKey " : " <string> " ,
" taskId " : " <string> " ,
" fileName " : " <string> " ,
" downFileName " : " <string> " ,
" fileUrl " : " <string> " ,
" downloadUrl " : " <string> " ,
" sourceType " : " <string> " ,
" targetType " : " <string> " ,
" fileSize " : 0 ,
" convertSize " : 0 ,
" convertTime " : 0 ,
" status " : " <string> " ,
" failureCode " : " <string> " ,
" failureReason " : " <string> " ,
" fileParameter " : " <string> "
}
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

The result file downloaded from downloadUrl contains the actual extraction payload:

text
result
name / key
value
page
bboxes

1
2
3
4
5

Field output â

Scalar field results commonly include:

Field Meaning

name / key Field name

value Extracted field value

page Source page number, when returned

bbox Source-page coordinates, especially when grounding is enabled

Table output â

Table-style output is commonly organised as "table name -> rows -> cells". In practice, this usually means:

a table identifier

a list of row records

cell values mapped to the schema-defined headers

If your schema defines tableHeaders , the returned table data usually follows the same header structure, which makes it easier to map into downstream business objects.

Extraction result example â

Below is an actual extraction result organised by page:

json
{
" Page-1 " : {
" æ¹éåå· " : " PXD222085 " ,
" åè´§æ¹å¼ " : " æ±½è¿ " ,
" å®¢æ·åå· " : " 5444412/1891133 " ,
" å®¡æ¹æ¥æ " : " 2024-05-07 " ,
" æ¶è´§åä½ " : " Shanghai Hexiaoxiao Information Technology Co., Ltd. " ,
" åä½ç¼ç  " : " 21002214 " ,
" ä»å¨èç³»äºº " : "" ,
" tables " : [
[
{
" åºå· " : " 1 " ,
" æ°é " : " 98 " ,
" ISBN " : " 978-7-5197-8886-5 " ,
" ç æ´ " : " 4,862.00 " ,
" å¾ä¹¦åç§° " : " Legal Matters Around Zhang San " ,
" ææ£ " : " 66.00 " ,
" åä»· " : " 49.00 " ,
" ååæ° " : " 2+10(14) " ,
" è´§ä½å· " : " 01-02-027-005 "
},
{
" åºå· " : " 2 " ,
" æ°é " : " 3 " ,
" ISBN " : " 978-7-5197-9009-7 " ,
" ç æ´ " : " 255.00 " ,
" å¾ä¹¦åç§° " : " Bankruptcy Trial Practice and Frontier Issues " ,
" ææ£ " : " 66.00 " ,
" åä»· " : " 85.00 " ,
" ååæ° " : " 0+3(8) " ,
" è´§ä½å· " : " 01-02-063-002 "
}
]
]
}
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37

Asset insufficient error â

When your page quota is exhausted, the API returns:

json
{
" code " : " 06001 " ,
" msg " : " You have run out of the files which could be processed " ,
" data " : null
}

1
2
3
4
5

enable_grounding â

When you pass:

bash
--form ' enable_grounding=true '

1

the backend attempts to include positional references for extracted fields or table cells. This is useful for:

highlighting extracted values in the source PDF

jumping from extracted results back to the original page

human review and verification workflows

How to use the result â

If you only need values, read fields

If you need line-item detail, read tables

If you need UI highlighting, consume page and bbox together

If you need full context, combine extraction output with documentParsing

Reading with other pages â

For mode selection, see Modes

For schema design, see Extract schema
