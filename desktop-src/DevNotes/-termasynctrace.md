---
Description: 'Terminates the trace.'
ms.assetid: 'e823ed82-1966-4e44-b062-0c8ab0fb5f6e'
title: TermAsyncTrace function
---

# TermAsyncTrace function

Terminates the trace.

## Syntax


```C++
BOOL TermAsyncTrace(void);
```



## Parameters

This function has no parameters.

## Return value

This function returns **TRUE** if it succeeds; otherwise, it returns **FALSE**.

## Remarks

Exstrace.dll is an optional component that installs with the Simple Mail Transfer Protocol (SMTP) and the Network News Transfer Protocol (NNTP).

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](base.loadlibrary) and [**GetProcAddress**](base.getprocaddress) functions.

## Requirements



|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Exstrace.dll</dt> </dl> |



 

 




