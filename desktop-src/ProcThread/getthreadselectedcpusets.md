---
description: Returns the explicit CPU Set assignment of the specified thread, if any assignment was set using the SetThreadSelectedCpuSets API. If no explicit assignment is set, RequiredIdCount is set to 0 and the function returns TRUE.
ms.assetid: 9ACF72F8-A64C-4FFF-B340-C920E80238CA
title: GetThreadSelectedCpuSets function (Processthreadapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- GetThreadSelectedCpuSets
api_type:
- DllExport
api_location:
- Kernel32.dll
- API-MS-Win-Core-ProcessThreads-L1-1-3.dll
- KernelBase.dll
---

# GetThreadSelectedCpuSets function

Returns the explicit CPU Set assignment of the specified thread, if any assignment was set using the [**SetThreadSelectedCpuSets**](setthreadselectedcpusets.md) API. If no explicit assignment is set, **RequiredIdCount** is set to 0 and the function returns TRUE.

## Syntax


```C++
BOOL WINAPI GetThreadSelectedCpuSets(
  _In_      HANDLE Thread,
  _Out_opt_ PULONG CpuSetIds,
  _In_      ULONG  CpuSetIdCount,
  _Out_     PULONG RequiredIdCount
);
```



## Parameters

<dl> <dt>

*Thread* \[in\]
</dt> <dd>

Specifies the thread for which to query the selected CPU Sets. This handle must have the THREAD\_QUERY\_LIMITED\_INFORMATION access right. The value returned by [**GetCurrentThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthread) can also be specified here.

</dd> <dt>

*CpuSetIds* \[out, optional\]
</dt> <dd>

Specifies an optional buffer to retrieve the list of CPU Set identifiers.

</dd> <dt>

*CpuSetIdCount* \[in\]
</dt> <dd>

Specifies the capacity of the buffer specified in **CpuSetIds**. If the buffer is NULL, this must be 0.

</dd> <dt>

*RequiredIdCount* \[out\]
</dt> <dd>

Specifies the required capacity of the buffer to hold the entire list of thread selected CPU Sets. On successful return, this specifies the number of IDs filled into the buffer.

</dd> </dl>

## Return value

This API returns TRUE on success. If the buffer is not large enough, the **GetLastError** value is ERROR\_INSUFFICIENT\_BUFFER. This API cannot fail when passed valid parameters and the return buffer is large enough.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps \| UWP apps\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps \| UWP apps\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Processthreadsapi.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Windows.h</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl>       |



 

