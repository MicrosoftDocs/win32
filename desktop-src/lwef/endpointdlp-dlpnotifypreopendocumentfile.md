---
Description: Provides the system with information about a document before an open operation is initiated.
title: DlpNotifyPreOpenDocumentFile function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyPreOpenDocumentFile
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyPreOpenDocumentFile function

Provides the system with information about a document before an open operation is initiated.

## Syntax


```C++
void WINAPI DlpNotifyPreOpenDocumentFile(_In_ const PDLP_DOCUMENT_INFO DocumentInfo);
```



## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A pointer to a [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure containing information about the document to be opened.

</dd> </dl>


## Return value

Return void.

## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                             |
| DLL<br/>                      | EndpointDlp.dll |