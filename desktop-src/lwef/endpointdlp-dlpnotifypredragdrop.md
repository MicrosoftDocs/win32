---
description: Provides the system with information about a document before a drag drop operation is initiated.
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

Provides the system with information about a document before a drag drop operation is initiated.

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


## Return value

Return void.

## Remarks


## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |
| DLL<br/>                      | EndpointDlp.dll |