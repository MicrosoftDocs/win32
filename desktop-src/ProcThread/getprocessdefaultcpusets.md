---
description: Retrieves the list of CPU Sets in the process default set that was set by SetProcessDefaultCpuSets. If no default CPU Sets are set for a given process, then the RequiredIdCount is set to 0 and the function succeeds.
ms.assetid: 85DC5331-9EC0-4603-94FD-B49E725301B1
title: GetProcessDefaultCpuSets function (Processthreadapi.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- GetProcessDefaultCpuSets
api_type:
- DllExport
api_location:
- Kernel32.dll
- API-MS-Win-Core-ProcessThreads-L1-1-3.dll
- KernelBase.dll
---

# GetProcessDefaultCpuSets function

Retrieves the list of CPU Sets in the process default set that was set by [**SetProcessDefaultCpuSets**](setprocessdefaultcpusets.md). If no default CPU Sets are set for a given process, then the **RequiredIdCount** is set to 0 and the function succeeds.

## Syntax


```C++
BOOL WINAPI GetProcessDefaultCpuSets(
  _In_      HANDLE Process,
  _Out_opt_ PULONG CpuSetIds,
  _In_      ULONG  CpuSetIdCount,
  _Out_     PULONG RequiredIdCount
);
```



## Parameters

<dl> <dt>

*Process* \[in\]
</dt> <dd>

Specifies a process handle for the process to query. This handle must have the PROCESS\_QUERY\_LIMITED\_INFORMATION access right. The value returned by [**GetCurrentProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) can also be specified here.

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

Specifies the required capacity of the buffer to hold the entire list of process default CPU Sets. On successful return, this specifies the number of IDs filled into the buffer.

</dd> </dl>

## Return value

This API returns TRUE on success. If the buffer is not large enough the API returns FALSE, and the **GetLastError** value is ERROR\_INSUFFICIENT\_BUFFER. This API cannot fail when passed valid parameters and the return buffer is large enough.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps \| UWP apps\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps \| UWP apps\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Processthreadsapi.h</dt> </dl> |
| Library<br/>                  | <dl> <dt>Windows.h</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>Kernel32.dll</dt> </dl>       |



 

