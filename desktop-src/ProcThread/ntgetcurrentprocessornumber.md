---
description: Retrieves the number of the processor the current thread was running on during the call to this function.
ms.assetid: f0141550-58e2-421a-934d-9a6c488d2b81
title: NtGetCurrentProcessorNumber function
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- NtGetCurrentProcessorNumber
api_type:
- DllExport
api_location:
- Ntdll.dll
---

# NtGetCurrentProcessorNumber function

\[**NtGetCurrentProcessorNumber** may be altered or unavailable in future versions of Windows. Applications should use the [**GetCurrentProcessorNumber**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocessornumber) function instead.\]

Retrieves the number of the processor the current thread was running on during the call to this function.

## Syntax


```C++
ULONG WINAPI NtGetCurrentProcessorNumber(void);
```



## Parameters

This function has no parameters.

## Return value

The function returns the current processor number.

## Remarks

This function is used to provide information for estimating process performance.

This function has no associated import library. You must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Ntdll.dll.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[Multiple Processors](multiple-processors.md)
</dt> <dt>

[Process and Thread Functions](process-and-thread-functions.md)
</dt> <dt>

[Processes](child-processes.md)
</dt> </dl>

 

 
