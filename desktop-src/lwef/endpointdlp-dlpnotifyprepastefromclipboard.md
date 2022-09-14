---
description: Provides the system with information about a document before a paste from clipboard operation is initiated.
title: DlpNotifyPrePasteFromClipboard function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyPrePasteFromClipboard
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyPrePasteFromClipboard function

Provides the system with information about a document before a paste from clipboard operation is initiated.

## Syntax


```C++
void WINAPI DlpNotifyPrePasteFromClipboard(_In_ const PDLP_DOCUMENT_INFO DocumentInfo);
```



## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A pointer to a [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure containing information about the document into which content is being pasted.

</dd> </dl>




## Return value

Return void.

## Remarks


## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |
| DLL<br/>                      | EndpointDlp.dll |