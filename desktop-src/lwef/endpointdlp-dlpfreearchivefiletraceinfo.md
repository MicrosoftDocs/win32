---
description: Frees the members of a DlpTraceInfoEx data structure.
title: DlpFreeArchiveFileTraceInfo function (endpointdlp.h)
ms.topic: reference
ms.date: 06/14/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpFreeArchiveFileTraceInfo
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpFreeArchiveFileTraceInfo function

Frees the members of a `DlpTraceInfoEx` data structure allocated by `DlpGetArchiveFileTraceInfo`.

## Syntax

```C++
void WINAPI DlpFreeArchiveFileTraceInfo(_Inout_opt_ DlpTraceInfoEx* archiveTraceInfo);
```

## Parameters

`archiveTraceInfo` [in/out]: A reference to an to trace structure to free. It can be NULL.

## Remarks

## Requirements


| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 11, version 22H2 (10.0; Build 22621)           |
| DLL<br/>                      | EndpointDlp.dll |