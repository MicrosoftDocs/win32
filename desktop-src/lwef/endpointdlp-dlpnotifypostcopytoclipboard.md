---
Description: Provides the system with information about a document after a copy to clipboard operation is completed.
title: DlpNotifyPostCopyToClipboard function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyPostCopyToClipboard
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyPostCopyToClipboard function

Provides the system with information about a document after a copy to clipboard operation is completed.

## Syntax


```C++
void WINAPI DlpNotifyPostCopyToClipboard(_In_ const PDLP_DOCUMENT_INFO DocumentInfo, _In_ const PDLP_POSTOP_STATUS OpStatus);
```



## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A pointer to a [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure containing information about the document from which content was copied.

</dd> </dl>

<dl> <dt>

*OpStatus* \[in\]
</dt> <dd>

A pointer to a [DLP_POSTOP_STATUS](enpointdlp-dlp_postop_status.md) structure containing status information about the copy to clipboard operation.

</dd> </dl>


## Return value

Return void.

## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                             |
| DLL<br/>                      | EndpointDlp.dll |