---
description: Initializes the trace.
ms.assetid: d2708e29-920d-4b13-8917-a6f2065ba58c
title: InitAsyncTrace function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InitAsyncTrace
api_type: 
- DllExport
api_location: 
- Exstrace.dll
---

# InitAsyncTrace function

Initializes the trace.

## Syntax


```C++
BOOL InitAsyncTrace(void);
```



## Parameters

This function has no parameters.

## Return value

This function returns **TRUE** if the function succeeds; otherwise, it returns **FALSE**.

## Remarks

Exstrace.dll is an optional component that installs with the Simple Mail Transfer Protocol (SMTP) and the Network News Transfer Protocol (NNTP).

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Exstrace.dll</dt> </dl> |



 

 
