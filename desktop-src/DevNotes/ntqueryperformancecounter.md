---
description: Returns the current value of a performance counter and, optionally, the frequency of the performance counter.
ms.assetid: ab8973b7-a358-4e50-85e8-9dbff4e67010
title: NtQueryPerformanceCounter function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NtQueryPerformanceCounter
api_type: 
- DllExport
api_location: 
- Ntdll.dll
---

# NtQueryPerformanceCounter function

\[This function is not supported and should not be used. Use the **QueryPerformanceCounter** and **QueryPerformanceFrequency** functions instead.\]

Returns the current value of a performance counter and, optionally, the frequency of the performance counter.

## Syntax


```C++
NTSTATUS NtQueryPerformanceCounter(
  _Out_     PLARGE_INTEGER PerformanceCounter,
  _Out_opt_ PLARGE_INTEGER PerformanceFrequency
);
```



## Parameters

<dl> <dt>

*PerformanceCounter* \[out\]
</dt> <dd>

The address of a variable to receive the current performance counter value.

</dd> <dt>

*PerformanceFrequency* \[out, optional\]
</dt> <dd>

The address of a variable to receive the performance counter frequency.

</dd> </dl>

## Return value

If the function succeeds, it returns the **NTSTATUS** code **STATUS\_SUCCESS**; otherwise, it returns an error code such as **STATUS\_ACCESS\_VIOLATION**.

## Remarks

No header file is available for **NtQueryPerformanceCounter**. You should use the alternative functions named above, although you can also use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Ntdll.dll.

Performance frequency is the frequency of the performance counter in hertz, specifically in counts per second. This value is implementation dependent. If the implementation does not have hardware to support performance timing, the value returned is 0.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter)
</dt> <dt>

[**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency)
</dt> </dl>

 

 
