---
description: Determines whether the app must pull the data from the system clipboard rather than taking it from its internal cache.
title: DlpMustPasteFromSystemClipboard function (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpMustPasteFromSystemClipboard
api_type: 
- DllExport
api_location: 
- EndpointDlp.dll
---

# DlpMustPasteFromSystemClipboard function

Determines whether the app must pull the data from the system clipboard rather than taking it from its internal cache.

## Syntax


```C++
BOOL WINAPI DlpMustPasteFromSystemClipboard();
```


## Return value

TRUE if calling into the OS clipboard is mandatory; otherwise, FALSE.

## Remarks


## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |
| DLL<br/>                      | EndpointDlp.dll |