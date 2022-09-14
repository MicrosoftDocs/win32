---
description: AsyncStringTrace function - Finishes setting up a trace buffer with optional fields for sprintf-style traces.
ms.assetid: a5f3ecbe-d335-4fd0-99aa-4d5a748ca4e1
title: AsyncStringTrace function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AsyncStringTrace
api_type: 
- DllExport
api_location: 
- Exstrace.dll
---

# AsyncStringTrace function

Finishes setting up a trace buffer with optional fields for **sprintf**-style traces.

## Syntax


```C++
int AsyncStringTrace(
   LPARAM  lParam,
   LPCSTR  szFormat,
   va_list marker
);
```



## Parameters

<dl> <dt>

*lParam* 
</dt> <dd>

A 32-bit trace parameter that is used for application-level filtering.

</dd> <dt>

*szFormat* 
</dt> <dd>

A zero-terminated string that describes the format of the trace.

</dd> <dt>

*marker* 
</dt> <dd>

A marker for **vsprintf** functions.

</dd> </dl>

## Return value

This function returns the length of the trace statement, in bytes.

## Remarks

Exstrace.dll is an optional component that installs with the Simple Mail Transfer Protocol (SMTP) and the Network News Transfer Protocol (NNTP).

The **va\_list** data type is a standard type that is used to hold information needed by **va\_arg** and **va\_end** macros. For more information, see [Standard Types](/cpp/c-runtime-library/standard-types).

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|-----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Exstrace.dll</dt> </dl> |



 

