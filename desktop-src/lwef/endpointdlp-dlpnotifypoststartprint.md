---
description: Provides the system with information about a document after an print operation has started.
title: DlpNotifyPostStartPrint function (endpointdlp.h)
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

# DlpNotifyPostStartPrint function

Provides the system with information about a document after a print operation has started.

## Syntax


```C++
void WINAPI DlpNotifyPostStartPrint(_In_ const PDLP_DOCUMENT_INFO DocumentInfo, _In_ const PDLP_PRINT_INFO PrintInfo);
```

## Parameters

<dl> <dt>

*DocumentInfo* \[in\]
</dt> <dd>

A pointer to a [PDLP_DOCUMENT_INFO](endpointdlp-dlp_document_info.md) structure containing information about the document associated with the print operation.

</dd> </dl>

<dl> <dt>

*PrintInfo* \[in\]
</dt> <dd>

A pointer to a [DLP_PRINT_INFO](endpointdlp-dlp_print_info.md) structure containing information about the print operation.

</dd> </dl>


## Return value

Return void.

## Remarks


## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |
| DLL<br/>                      | EndpointDlp.dll |