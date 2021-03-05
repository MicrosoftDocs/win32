---
description: Called by the compiler to implement structured exception handling extensions.
ms.assetid: 6EAE0B4E-35E1-48EB-A8A9-0C1DC5387B03
title: '__C_specific_handler function (Wdm.h)'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __C_specific_handler
- __C_specific_handler
api_type: 
- DllExport
api_location: 
- ntoskrnl.exe
- NTDll.dll
- wpdupfltr.sys
---

# \_\_C\_specific\_handler function

Called by the compiler to implement structured exception handling extensions.

The relative address of the language specific handler is present in the UNWIND\_INFO whenever flags UNW\_FLAG\_EHANDLER or UNW\_FLAG\_UHANDLER are set. The language specific handler is called as part of the search for an exception handler or as part of an unwind. For more information see [Language Specific Handler](/cpp/build/language-specific-handler).

## Syntax


```C++
_CRTIMP  __C_specific_handler(
  _In_    struct _EXCEPTION_RECORD   *ExceptionRecord,
  _In_    void                       *EstablisherFrame,
  _Inout_ struct _CONTEXT            *ContextRecord,
  _Inout_ struct _DISPATCHER_CONTEXT *DispatcherContext
);
```



## Parameters

<dl> <dt>

*ExceptionRecord* \[in\]
</dt> <dd>

Supplies a pointer to an exception record, which has the standard Win64 definition.

</dd> <dt>

*EstablisherFrame* \[in\]
</dt> <dd>

The address of the base of the fixed stack allocation for this function.

</dd> <dt>

*ContextRecord* \[in, out\]
</dt> <dd>

Points to the exception context at the time the exception was raised (in the exception handler case) or the current "unwind" context (in the termination handler case).

</dd> <dt>

*DispatcherContext* \[in, out\]
</dt> <dd>

Points to the dispatcher context for this function.

</dd> </dl>

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wdm.h</dt> </dl>        |
| Library<br/> | <dl> <dt>NtosKrnl.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Ntoskrnl.exe</dt> </dl> |



 

