---
description: Sets the default CPU Sets assignment for threads in the specified process. Threads that are created, which don’t have CPU Sets explicitly set using SetThreadSelectedCpuSets, will inherit the sets specified by SetProcessDefaultCpuSets automatically.
ms.assetid: 7A510A8D-B06C-4B7B-9A87-BCFE0DE4D17B
title: SetProcessDefaultCpuSets function (Processthreadapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SetProcessDefaultCpuSets
api_type:
- DllExport
api_location:
- Kernel32.dll
- API-MS-Win-Core-ProcessThreads-L1-1-3.dll
- KernelBase.dll
---

# SetProcessDefaultCpuSets function

Sets the default CPU Sets assignment for threads in the specified process. Threads that are created, which don’t have CPU Sets explicitly set using [**SetThreadSelectedCpuSets**](setthreadselectedcpusets.md), will inherit the sets specified by **SetProcessDefaultCpuSets** automatically.

## Syntax


```C++
BOOL WINAPI SetProcessDefaultCpuSets(
  _In_     HANDLE Process,
  _In_opt_ ULONG  CpuSetIds,
  _In_     ULONG  CpuSetIdCound
);
```



## Parameters

<dl> <dt>

*Process* \[in\]
</dt> <dd>

Specifies the process for which to set the default CPU Sets. This handle must have the PROCESS\_SET\_LIMITED\_INFORMATION access right. The value returned by [**GetCurrentProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) can also be specified here.

</dd> <dt>

*CpuSetIds* \[in, optional\]
</dt> <dd>

Specifies the list of CPU Set IDs to set as the process default CPU set. If this is NULL, the **SetProcessDefaultCpuSets** clears out any assignment.

</dd> <dt>

*CpuSetIdCound* \[in\]
</dt> <dd>

Specifies the number of IDs in the list passed in the **CpuSetIds** argument. If that value is NULL, this should be 0.

</dd> </dl>

## Return value

This function cannot fail when passed valid parameters.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps \| UWP apps\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps \| UWP apps\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Processthreadsapi.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Windows.h</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl>       |



 

 
