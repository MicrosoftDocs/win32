---
Description: 'Initializes the trace.'
ms.assetid: 'd2708e29-920d-4b13-8917-a6f2065ba58c'
title: InitAsyncTrace function
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Exstrace.dll</dt> </dl> |



 

 




