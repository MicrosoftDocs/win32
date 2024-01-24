---
description: Retrieves the specified system information.
ms.assetid: c91b9a35-ca2b-4d81-973d-fe709144df90
title: ZwQuerySystemInformation function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ZwQuerySystemInformation
api_type: 
- DllExport
api_location: 
- Ntdll.dll
- ntoskrnl.exe
---

# ZwQuerySystemInformation function

\[**ZwQuerySystemInformation** is no longer available for use as of Windows 8. Instead, use the alternate functions listed in this topic.\]

Retrieves the specified system information.

## Syntax


```C++
NTSTATUS WINAPI ZwQuerySystemInformation(
  _In_      SYSTEM_INFORMATION_CLASS SystemInformationClass,
  _Inout_   PVOID                    SystemInformation,
  _In_      ULONG                    SystemInformationLength,
  _Out_opt_ PULONG                   ReturnLength
);
```



## Parameters

<dl> <dt>

*SystemInformationClass* \[in\]
</dt> <dd>

The type of system information to be retrieved. This parameter can be one of the following values from the **SYSTEM\_INFORMATION\_CLASS** enumeration type.

<dt>

<span id="SystemBasicInformation"></span><span id="systembasicinformation"></span><span id="SYSTEMBASICINFORMATION"></span>

<span id="SystemBasicInformation"></span><span id="systembasicinformation"></span><span id="SYSTEMBASICINFORMATION"></span>**SystemBasicInformation**


</dt> <dd>

The number of processors in the system in a **SYSTEM\_BASIC\_INFORMATION** structure. Use the [**GetSystemInfo**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsysteminfo) function instead.

</dd> <dt>

<span id="SystemPerformanceInformation"></span><span id="systemperformanceinformation"></span><span id="SYSTEMPERFORMANCEINFORMATION"></span>

<span id="SystemPerformanceInformation"></span><span id="systemperformanceinformation"></span><span id="SYSTEMPERFORMANCEINFORMATION"></span>**SystemPerformanceInformation**


</dt> <dd>

An opaque **SYSTEM\_PERFORMANCE\_INFORMATION** structure that can be used to generate an unpredictable seed for a random number generator. Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead.

</dd> <dt>

<span id="SystemTimeOfDayInformation"></span><span id="systemtimeofdayinformation"></span><span id="SYSTEMTIMEOFDAYINFORMATION"></span>

<span id="SystemTimeOfDayInformation"></span><span id="systemtimeofdayinformation"></span><span id="SYSTEMTIMEOFDAYINFORMATION"></span>**SystemTimeOfDayInformation**


</dt> <dd>

An opaque **SYSTEM\_TIMEOFDAY\_INFORMATION** structure that can be used to generate an unpredictable seed for a random number generator. Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead.

</dd> <dt>

<span id="SystemProcessInformation"></span><span id="systemprocessinformation"></span><span id="SYSTEMPROCESSINFORMATION"></span>

<span id="SystemProcessInformation"></span><span id="systemprocessinformation"></span><span id="SYSTEMPROCESSINFORMATION"></span>**SystemProcessInformation**


</dt> <dd>

An array of **SYSTEM\_PROCESS\_INFORMATION** structures, one for each process running in the system.

These structures contain information about the resource usage of each process, including the number of handles used by the process, the peak page-file usage, and the number of memory pages that the process has allocated.

</dd> <dt>

<span id="SystemProcessorPerformanceInformation"></span><span id="systemprocessorperformanceinformation"></span><span id="SYSTEMPROCESSORPERFORMANCEINFORMATION"></span>

<span id="SystemProcessorPerformanceInformation"></span><span id="systemprocessorperformanceinformation"></span><span id="SYSTEMPROCESSORPERFORMANCEINFORMATION"></span>**SystemProcessorPerformanceInformation**


</dt> <dd>

An array of **SYSTEM\_PROCESSOR\_PERFORMANCE\_INFORMATION** structures, one for each processor installed in the system.

</dd> <dt>

<span id="SystemInterruptInformation"></span><span id="systeminterruptinformation"></span><span id="SYSTEMINTERRUPTINFORMATION"></span>

<span id="SystemInterruptInformation"></span><span id="systeminterruptinformation"></span><span id="SYSTEMINTERRUPTINFORMATION"></span>**SystemInterruptInformation**


</dt> <dd>

An opaque **SYSTEM\_INTERRUPT\_INFORMATION** structure that can be used to generate an unpredictable seed for a random number generator. Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead.

</dd> <dt>

<span id="SystemExceptionInformation"></span><span id="systemexceptioninformation"></span><span id="SYSTEMEXCEPTIONINFORMATION"></span>

<span id="SystemExceptionInformation"></span><span id="systemexceptioninformation"></span><span id="SYSTEMEXCEPTIONINFORMATION"></span>**SystemExceptionInformation**


</dt> <dd>

An opaque **SYSTEM\_EXCEPTION\_INFORMATION** structure that can be used to generate an unpredictable seed for a random number generator. Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead.

</dd> <dt>

<span id="SystemRegistryQuotaInformation"></span><span id="systemregistryquotainformation"></span><span id="SYSTEMREGISTRYQUOTAINFORMATION"></span>

<span id="SystemRegistryQuotaInformation"></span><span id="systemregistryquotainformation"></span><span id="SYSTEMREGISTRYQUOTAINFORMATION"></span>**SystemRegistryQuotaInformation**


</dt> <dd>

A **SYSTEM\_REGISTRY\_QUOTA\_INFORMATION** structure.

</dd> <dt>

<span id="SystemLookasideInformation"></span><span id="systemlookasideinformation"></span><span id="SYSTEMLOOKASIDEINFORMATION"></span>

<span id="SystemLookasideInformation"></span><span id="systemlookasideinformation"></span><span id="SYSTEMLOOKASIDEINFORMATION"></span>**SystemLookasideInformation**


</dt> <dd>

An opaque **SYSTEM\_LOOKASIDE\_INFORMATION** structure that can be used to generate an unpredictable seed for a random number generator. Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead.

</dd> </dl> </dd> <dt>

*SystemInformation* \[in, out\]
</dt> <dd>

A pointer to a buffer that receives the requested information. The size and structure of this information varies depending on the value of the *SystemInformationClass* parameter, as indicated in the following table.

<dt>

<span id="SYSTEM_BASIC_INFORMATION"></span><span id="system_basic_information"></span>

<span id="SYSTEM_BASIC_INFORMATION"></span><span id="system_basic_information"></span>**SYSTEM\_BASIC\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemBasicInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold a single **SYSTEM\_BASIC\_INFORMATION** structure having the following layout:

``` syntax
typedef struct _SYSTEM_BASIC_INFORMATION {
    BYTE Reserved1[24];
    PVOID Reserved2[4];
    CCHAR NumberOfProcessors;
} SYSTEM_BASIC_INFORMATION;
```

The **NumberOfProcessors** member contains the number of processors present in the system. Use [**GetSystemInfo**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsysteminfo) instead to retrieve this information.

The other members of the structure are reserved for internal use by the operating system.

</dd> <dt>

<span id="SYSTEM_PERFORMANCE_INFORMATION"></span><span id="system_performance_information"></span>

<span id="SYSTEM_PERFORMANCE_INFORMATION"></span><span id="system_performance_information"></span>**SYSTEM\_PERFORMANCE\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemPerformanceInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold an opaque **SYSTEM\_PERFORMANCE\_INFORMATION** structure for use in generating an unpredictable seed for a random number generator. For this purpose, the structure has the following layout:

``` syntax
typedef struct _SYSTEM_PERFORMANCE_INFORMATION {
    BYTE Reserved1[312];
} SYSTEM_PERFORMANCE_INFORMATION;
```

Individual members of the structure are reserved for internal use by the operating system.

Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead to generate cryptographically random data.

</dd> <dt>

<span id="SYSTEM_TIMEOFDAY_INFORMATION"></span><span id="system_timeofday_information"></span>

<span id="SYSTEM_TIMEOFDAY_INFORMATION"></span><span id="system_timeofday_information"></span>**SYSTEM\_TIMEOFDAY\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemTimeOfDayInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold an opaque **SYSTEM\_TIMEOFDAY\_INFORMATION** structure for use in generating an unpredictable seed for a random number generator. For this purpose, the structure has the following layout:

``` syntax
typedef struct _SYSTEM_TIMEOFDAY_INFORMATION {
    BYTE Reserved1[48];
} SYSTEM_TIMEOFDAY_INFORMATION;
```

Individual members of the structure are reserved for internal use by the operating system.

Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead to generate cryptographically random data.

</dd> <dt>

<span id="SYSTEM_PROCESS_INFORMATION"></span><span id="system_process_information"></span>

<span id="SYSTEM_PROCESS_INFORMATION"></span><span id="system_process_information"></span>**SYSTEM\_PROCESS\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemProcessInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold an array that contains as many **SYSTEM\_PROCESS\_INFORMATION** structures as there are processes running in the system. Each structure has the following layout:

``` syntax
typedef struct _SYSTEM_PROCESS_INFORMATION {
    ULONG NextEntryOffset;
    ULONG NumberOfThreads;
    BYTE Reserved1[48];
    PVOID Reserved2[3];
    HANDLE UniqueProcessId;
    PVOID Reserved3;
    ULONG HandleCount;
    BYTE Reserved4[4];
    PVOID Reserved5[11];
    SIZE_T PeakPagefileUsage;
    SIZE_T PrivatePageCount;
    LARGE_INTEGER Reserved6[6];
} SYSTEM_PROCESS_INFORMATION;
```

The **NumberOfThreads** member contains the total number of currently running threads in the process.

The **HandleCount** member contains the total number of handles being used by the process in question; use [**GetProcessHandleCount**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-getprocesshandlecount) to retrieve this information instead.

The **PeakPagefileUsage** member contains the maximum number of bytes of page-file storage used by the process, and the **PrivatePageCount** member contains the number of memory pages allocated for the use of this process.

You can also retrieve this information using either the [**GetProcessMemoryInfo**](/windows/desktop/api/psapi/nf-psapi-getprocessmemoryinfo) function or the [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) class.

The other members of the structure are reserved for internal use by the operating system.

</dd> <dt>

<span id="SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION"></span><span id="system_processor_performance_information"></span>

<span id="SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION"></span><span id="system_processor_performance_information"></span>**SYSTEM\_PROCESSOR\_PERFORMANCE\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemProcessorPerformanceInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold an array that contains as many **SYSTEM\_PROCESS\_INFORMATION** structures as there are processors (CPUs) installed in the system. Each structure has the following layout:

``` syntax
typedef struct
_SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION {
    LARGE_INTEGER IdleTime;
    LARGE_INTEGER KernelTime;
    LARGE_INTEGER UserTime;
    LARGE_INTEGER Reserved1[2];
    ULONG Reserved2;
} SYSTEM_PROCESSOR_PERFORMANCE_INFORMATION;
```

The **IdleTime** member contains the amount of time that the system has been idle, in 1/100ths of a nanosecond.

The **KernelTime** member contains the amount of time that the system has spent executing in Kernel mode (including all threads in all processes, on all processors), in 1/100ths of a nanosecond.

The **UserTime** member contains the amount of time that the system has spent executing in User mode (including all threads in all processes, on all processors), in 1/100ths of a nanosecond.

Use [**GetSystemTimes**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getsystemtimes) instead to retrieve this information.

</dd> <dt>

<span id="SYSTEM_INTERRUPT_INFORMATION"></span><span id="system_interrupt_information"></span>

<span id="SYSTEM_INTERRUPT_INFORMATION"></span><span id="system_interrupt_information"></span>**SYSTEM\_INTERRUPT\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemInterruptInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold an array that contains as many opaque **SYSTEM\_INTERRUPT\_INFORMATION** structures as there are processors (CPUs) installed on the system. Each structure, or the array as a whole, can be used to generate an unpredictable seed for a random number generator. For this purpose, the structure has the following layout:

``` syntax
typedef struct _SYSTEM_INTERRUPT_INFORMATION {
    BYTE Reserved1[24];
} SYSTEM_INTERRUPT_INFORMATION;
```

Individual members of the structure are reserved for internal use by the operating system.

Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead to generate cryptographically random data.

</dd> <dt>

<span id="SYSTEM_EXCEPTION_INFORMATION"></span><span id="system_exception_information"></span>

<span id="SYSTEM_EXCEPTION_INFORMATION"></span><span id="system_exception_information"></span>**SYSTEM\_EXCEPTION\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemExceptionInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold an opaque **SYSTEM\_EXCEPTION\_INFORMATION** structure for use in generating an unpredictable seed for a random number generator. For this purpose, the structure has the following layout:

``` syntax
typedef struct _SYSTEM_EXCEPTION_INFORMATION {
    BYTE Reserved1[16];
} SYSTEM_EXCEPTION_INFORMATION;
```

Individual members of the structure are reserved for internal use by the operating system.

Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead to generate cryptographically random data.

</dd> <dt>

<span id="SYSTEM_REGISTRY_QUOTA_INFORMATION"></span><span id="system_registry_quota_information"></span>

<span id="SYSTEM_REGISTRY_QUOTA_INFORMATION"></span><span id="system_registry_quota_information"></span>**SYSTEM\_REGISTRY\_QUOTA\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemRegistryQuotaInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold a single **SYSTEM\_REGISTRY\_QUOTA\_INFORMATION** structure having the following layout:

``` syntax
typedef struct _SYSTEM_REGISTRY_QUOTA_INFORMATION {
    ULONG RegistryQuotaAllowed;
    ULONG RegistryQuotaUsed;
    PVOID Reserved1;
} SYSTEM_REGISTRY_QUOTA_INFORMATION;
```

The **RegistryQuotaAllowed** member contains the maximum size, in bytes, that the Registry can attain on this system.

The **RegistryQuotaUsed** member contains the current size of the Registry, in bytes.

Use [**GetSystemRegistryQuota**](/windows/desktop/api/Winbase/nf-winbase-getsystemregistryquota) instead to retrieve this information.

The other member of the structure is reserved for internal use by the operating system.

</dd> <dt>

<span id="SYSTEM_LOOKASIDE_INFORMATION"></span><span id="system_lookaside_information"></span>

<span id="SYSTEM_LOOKASIDE_INFORMATION"></span><span id="system_lookaside_information"></span>**SYSTEM\_LOOKASIDE\_INFORMATION**


</dt> <dd>

When the *SystemInformationClass* parameter is **SystemLookasideInformation**, the buffer pointed to by the *SystemInformation* parameter should be large enough to hold an opaque **SYSTEM\_LOOKASIDE\_INFORMATION** structure for use in generating an unpredictable seed for a random number generator. For this purpose, the structure has the following layout:

``` syntax
typedef struct _SYSTEM_LOOKASIDE_INFORMATION {
    BYTE Reserved1[32];
} SYSTEM_LOOKASIDE_INFORMATION;
```

Individual members of the structure are reserved for internal use by the operating system.

Use the [**CryptGenRandom**](/windows/desktop/api/wincrypt/nf-wincrypt-cryptgenrandom) function instead to generate cryptographically random data.

</dd> </dl> </dd> <dt>

*SystemInformationLength* \[in\]
</dt> <dd>

The size of the buffer pointed to by the *SystemInformation* parameter, in bytes.

</dd> <dt>

*ReturnLength* \[out, optional\]
</dt> <dd>

An optional pointer to a location where the function writes the actual size of the information requested. If that size is less than or equal to the *SystemInformationLength* parameter, the function copies the information into the *SystemInformation* buffer; otherwise, it returns an NTSTATUS error code and returns in *ReturnLength* the size of buffer required to receive the requested information.

</dd> </dl>

## Return value

Returns an NTSTATUS success or error code.

The forms and significance of NTSTATUS error codes are listed in the Ntstatus.h header file available in the DDK, and are described in the DDK documentation.

## Remarks

The **ZwQuerySystemInformation** function and the structures that it returns are internal to the operating system and subject to change from one release of Windows to another. To maintain the compatibility of your application, it is better to use the alternate functions previously mentioned instead.

If you do use **ZwQuerySystemInformation**, access the function through [run-time dynamic linking](/windows/desktop/Dlls/using-run-time-dynamic-linking). This gives your code an opportunity to respond gracefully if the function has been changed or removed from the operating system. Signature changes, however, may not be detectable.

This function has no associated import library. You must use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to Ntdll.dll.

## Requirements



| Requirement | Value |
|----------------|--------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**GetSystemInfo**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsysteminfo)
</dt> <dt>

[**GetProcessHandleCount**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-getprocesshandlecount)
</dt> <dt>

[**GetProcessMemoryInfo**](/windows/desktop/api/psapi/nf-psapi-getprocessmemoryinfo)
</dt> <dt>

[**GetSystemTimes**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getsystemtimes)
</dt> <dt>

[**GetSystemRegistryQuota**](/windows/desktop/api/Winbase/nf-winbase-getsystemregistryquota)
</dt> </dl>

 

