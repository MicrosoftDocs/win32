---
Description: Provides the system with information about a document after the open operation is completed.
title: DlpNotifyPostOpenDocument function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpNotifyPostOpenDocument
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpNotifyPostOpenDocument function

Provides the system with information about a document after the open operation is completed.

## Syntax


```C++
void WINAPI DlpNotifyPostOpenDocument(_In_ const PDLP_DOCUMENT_INFO DocumentInfo, _In_ const PDLP_POSTOP_STATUS OpStatus); 
```

## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure representing the document to be opened.

</dd> </dl>

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A [PDLP_POSTOP_STATUS](endpointdlp-dlp_document_info.md) structure representing the document to be opened.

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