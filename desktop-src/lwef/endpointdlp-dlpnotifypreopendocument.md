---
Description: Provides the system with information about a document before the open operation is initiated.
title: DlpNotifyPreOpenDocument function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyPreOpenDocument
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyPreOpenDocument function

Provides the system with information about a document before the open operation is initiated.

## Syntax


```C++
void WINAPI DlpNotifyPreOpenDocument(_In_ const PDLP_DOCUMENT_INFO DocumentInfo);
```



## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure representing the document to be opened.

</dd> </dl>


## Return value

Return void.

## Remarks


## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10                                             |
| Minimum supported server<br/> | Windows Server                                    |
| DLL<br/>                      | EndpointDlp.dll |