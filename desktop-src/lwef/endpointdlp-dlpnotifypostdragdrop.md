---
Description: Provides the system with information about a document after a drag drop operation is completed.
title: DlpNotifyPreDragDrop function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyPreDragDrop
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyPreDragDrop function

Provides the system with information about a document after a drag drop operation is completed.

## Syntax


```C++
void WINAPI DlpNotifyPreDragDrop(_In_ const PDLP_DOCUMENT_INFO DocumentInfo);
```



## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A pointer to a [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure containing information about the document associated with the drag drop operation.

</dd> </dl>

<dl> <dt>

*OpStatus* \[in\]
</dt> <dd>

A pointer to a [DLP_POSTOP_STATUS](enpointdlp-dlp_postop_status.md) structure containing status information about the drag drop.

</dd> </dl>


## Return value

Return void.

## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                             |
| DLL<br/>                      | EndpointDlp.dll |