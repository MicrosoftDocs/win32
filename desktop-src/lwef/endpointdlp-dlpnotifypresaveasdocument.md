---
Description: Provides the system with information about a document before a save as operation is initiated.
title: DlpNotifyPreSaveAsDocument function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyPreSaveAsDocument
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyPreSaveAsDocument function

Provides the system with information about a document before a save as operation is initiated.

## Syntax


```C++
void WINAPI DlpNotifyPreSaveAsDocument(_In_ const PDLP_DOCUMENT_INFO DocumentInfo, _In_ LPCWSTR Destination);
```



## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A pointer to a [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure containing information about the document to be saved.

</dd> </dl>

<dl> <dt>

*Destination* \[in\]
</dt> <dd>

A **LPCWSTR** containing the destination path of the document to be saved.

</dd> </dl>


## Return value

Return void.

## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |
| DLL<br/>                      | EndpointDlp.dll |