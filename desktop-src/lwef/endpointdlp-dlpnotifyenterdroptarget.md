---
Description: Provides the system with information about a document when a drop target is entered.
title: DlpNotifyEnterDropTarget function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyEnterDropTarget
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyEnterDropTarget function

Provides the system with information about a document when a drop target is entered.

## Syntax


```C++
void WINAPI DlpNotifyEnterDropTarget(_In_ const PDLP_DOCUMENT_INFO DocumentInfo);
```



## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A pointer to a [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure containing information about the document associated with the drop operation.

</dd> </dl>


## Return value

Return void.

## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                             |
| DLL<br/>                      | EndpointDlp.dll |