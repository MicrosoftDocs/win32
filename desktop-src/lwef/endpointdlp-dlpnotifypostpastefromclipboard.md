---
Description: Provides the system with information about a document after a paste from clipboard operation is completed.
title: DlpNotifyPostPasteFromClipboard function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyPostPasteFromClipboard
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyPostPasteFromClipboard function

Provides the system with information about a document after a paste from clipboard operation is completed.

## Syntax


```C++
void WINAPI DlpNotifyPostPasteFromClipboard(_In_ const PDLP_DOCUMENT_INFO DocumentInfo, _In_ const PDLP_POSTOP_STATUS OpStatus);
```



## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A pointer to a [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure containing information about the document into which content was copied.

</dd> </dl>

<dl> <dt>

*OpStatus* \[in\]
</dt> <dd>

A pointer to a [DLP_POSTOP_STATUS](enpointdlp-dlp_postop_status.md) structure containing status information about the paste from clipboard operation.

</dd> </dl>


## Return value

Return void.

## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                             |
| DLL<br/>                      | EndpointDlp.dll |