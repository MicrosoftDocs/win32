---
description: Sets the selected CPU Sets assignment for the specified thread. This assignment overrides the process default assignment, if one is set.
ms.assetid: A73F7118-CC4A-45E6-869A-DFF6924D10C8
title: SetThreadSelectedCpuSets function (Processthreadapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- SetThreadSelectedCpuSets
api_type:
- DllExport
api_location:
- Kernel32.dll
- API-MS-Win-Core-ProcessThreads-L1-1-3.dll
- KernelBase.dll
---

# SetThreadSelectedCpuSets function

Sets the selected CPU Sets assignment for the specified thread. This assignment overrides the process default assignment, if one is set.

## Syntax


```C++
BOOL WINAPI SetThreadSelectedCpuSets(
  _In_       HANDLE Thread,
  _In_ const ULONG  *CpuSetIds,
  _In_       ULONG  CpuSetIdCount
);
```



## Parameters

<dl> <dt>

*Thread* \[in\]
</dt> <dd>

Specifies the thread on which to set the CPU Set assignment. This handle must have the THREAD\_SET\_LIMITED\_INFORMATION access right. The value returned by [**GetCurrentThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthread) can also be used.

</dd> <dt>

*CpuSetIds* \[in\]
</dt> <dd>

Specifies the list of CPU Set IDs to set as the thread selected CPU set. If this is NULL, the API clears out any assignment, reverting to process default assignment if one is set.

</dd> <dt>

*CpuSetIdCount* \[in\]
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



 

 
