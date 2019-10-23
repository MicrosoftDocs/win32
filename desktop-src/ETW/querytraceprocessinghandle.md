---
Description: Queries the system for the trace processing handle.
ms.assetid: 87666275-8752-4EC8-9C01-16D36AE4C5E8
title: QueryTraceProcessingHandle function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- QueryTraceProcessingHandle
api_type: 
- DllExport
api_location: 
- AdvAPI32.dll
---

# QueryTraceProcessingHandle function

Queries the system for the trace processing handle.

## Syntax


```C++
ULONG WINAPI QueryTraceProcessingHandle(
  _In_      TRACEHANDLE                  ProcessingHandle,
  _In_      ETW_PROCESS_HANDLE_INFO_TYPE InformationClass,
  _In_opt_  PVOID                        InBuffer,
  _In_      ULONG                        InBufferSize,
  _Out_opt_ PVOID                        OutBuffer,
  _In_      ULONG                        OutBufferSize,
  _Out_     PULONG                       ReturnLength
);
```



## Parameters

<dl> <dt>

*ProcessingHandle* \[in\]
</dt> <dd>

A valid handle created with [**OpenTrace**](opentrace.md) that the data should be queried from.

</dd> <dt>

*InformationClass* \[in\]
</dt> <dd>

An [**ETW\_PROCESS\_HANDLE\_INFO\_TYPE**](etw-process-handle-info-type.md) value that specifies what kind of operation will be done on the handle.

</dd> <dt>

*InBuffer* \[in, optional\]
</dt> <dd>

Reserved for future use. May be null.

</dd> <dt>

*InBufferSize* \[in\]
</dt> <dd>

Size in bytes of the *InBuffer*.

</dd> <dt>

*OutBuffer* \[out, optional\]
</dt> <dd>

Buffer provided by the caller to contain output data.

</dd> <dt>

*OutBufferSize* \[in\]
</dt> <dd>

Size in bytes of *OutBuffer.*

</dd> <dt>

*ReturnLength* \[out\]
</dt> <dd>

The size in bytes of the data that the API wrote into *OutBuffer*. Important for variable length returns.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/en-us/library/ms681381(v=VS.85).aspx).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>AdvAPI32.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AdvAPI32.dll</dt> </dl> |



 

 




