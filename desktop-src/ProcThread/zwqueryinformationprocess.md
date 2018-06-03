---
Description: Retrieves information about the specified process.
ms.assetid: c36c023f-7f9a-4ba5-a41f-f2f755a24eb6
title: ZwQueryInformationProcess function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ZwQueryInformationProcess function

\[**ZwQueryInformationProcess** may be altered or unavailable in future versions of Windows. Applications should use the alternate functions listed in this topic.\]

Retrieves information about the specified process.

## Syntax


```C++
NTSTATUS WINAPI ZwQueryInformationProcess(
  _In_      HANDLE           ProcessHandle,
  _In_      PROCESSINFOCLASS ProcessInformationClass,
  _Out_     PVOID            ProcessInformation,
  _In_      ULONG            ProcessInformationLength,
  _Out_opt_ PULONG           ReturnLength
);
```



## Parameters

<dl> <dt>

*ProcessHandle* \[in\]
</dt> <dd>

A handle to the process for which information is to be retrieved.

</dd> <dt>

*ProcessInformationClass* \[in\]
</dt> <dd>

The type of process information to be retrieved. This parameter can be one of the following values from the **PROCESSINFOCLASS** enumeration.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="ProcessBasicInformation"></span><span id="processbasicinformation"></span><span id="PROCESSBASICINFORMATION"></span><dl> <dt><strong>ProcessBasicInformation</strong></dt> <dt>0</dt> </dl></td>
<td>Retrieves a pointer to a PEB structure that can be used to determine whether the specified process is being debugged, and a unique value used by the system to identify the specified process. <br/> It is best to use the [<strong>CheckRemoteDebuggerPresent</strong>](https://msdn.microsoft.com/windows/desktop/e7eb2d48-4ef3-4708-8895-2bc33d2c3e91) and [<strong>GetProcessId</strong>](/windows/desktop/api/WinBase/nf-processthreadsapi-getprocessid) functions to obtain this information.<br/></td>
</tr>
<tr class="even">
<td><span id="ProcessDebugPort"></span><span id="processdebugport"></span><span id="PROCESSDEBUGPORT"></span><dl> <dt><strong>ProcessDebugPort</strong></dt> <dt>7</dt> </dl></td>
<td>Retrieves a <strong>DWORD_PTR</strong> value that is the port number of the debugger for the process. A nonzero value indicates that the process is being run under the control of a ring 3 debugger.<br/> It is best to use the [<strong>CheckRemoteDebuggerPresent</strong>](https://msdn.microsoft.com/windows/desktop/e7eb2d48-4ef3-4708-8895-2bc33d2c3e91) or [<strong>IsDebuggerPresent</strong>](https://msdn.microsoft.com/windows/desktop/7bc4bcb7-3f85-4349-a1da-c4ebee2d3e3f) function.<br/></td>
</tr>
<tr class="odd">
<td><span id="ProcessWow64Information"></span><span id="processwow64information"></span><span id="PROCESSWOW64INFORMATION"></span><dl> <dt><strong>ProcessWow64Information</strong></dt> <dt>26</dt> </dl></td>
<td>Determines whether the process is running in the WOW64 environment (WOW64 is the x86 emulator that allows Win32-based applications to run on 64-bit Windows).<br/> It is best to use the [<strong>IsWow64Process</strong>](/windows/desktop/api/WinBase/nf-wow64apiset-iswow64process) function to obtain this information.<br/></td>
</tr>
<tr class="even">
<td><span id="ProcessImageFileName"></span><span id="processimagefilename"></span><span id="PROCESSIMAGEFILENAME"></span><dl> <dt><strong>ProcessImageFileName</strong></dt> <dt>27</dt> </dl></td>
<td>Retrieves a <strong>UNICODE_STRING</strong> value containing the name of the image file for the process.<br/></td>
</tr>
<tr class="odd">
<td><span id="ProcessBreakOnTermination"></span><span id="processbreakontermination"></span><span id="PROCESSBREAKONTERMINATION"></span><dl> <dt><strong>ProcessBreakOnTermination</strong></dt> <dt>29</dt> </dl></td>
<td>Retrieves a <strong>ULONG</strong> value indicating whether the process is considered critical.<br/>
<blockquote>
[!Note]<br />
This value can be used starting in Windows XP with SP3. Starting in Windows 8.1, [<strong>IsProcessCritical</strong>](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-isprocesscritical) should be used instead.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

*ProcessInformation* \[out\]
</dt> <dd>

A pointer to a buffer supplied by the calling application into which the function writes the requested information. The size of the information written varies depending on the value of the *ProcessInformationClass* parameter:

<dl> <dt>

<span id="PROCESS_BASIC_INFORMATION"></span><span id="process_basic_information"></span>PROCESS\_BASIC\_INFORMATION
</dt> <dd>

When the *ProcessInformationClass* parameter is **ProcessBasicInformation**, the buffer pointed to by the *ProcessInformation* parameter should be large enough to hold a single **PROCESS\_BASIC\_INFORMATION** structure having the following layout:

``` syntax
typedef struct _PROCESS_BASIC_INFORMATION {
    PVOID Reserved1;
    PPEB PebBaseAddress;
    PVOID Reserved2[2];
    ULONG_PTR UniqueProcessId;
    PVOID Reserved3;
} PROCESS_BASIC_INFORMATION;
```

The **UniqueProcessId** member points to the system's unique identifier for this process. It is best to use the [**GetProcessId**](/windows/desktop/api/WinBase/nf-processthreadsapi-getprocessid) function to retrieve this information.

The **PebBaseAddress** member points to a [**PEB**](/windows/desktop/api/Winternl/ns-winternl-_peb) structure.

The other members of this structure are reserved for internal use by the operating system.

</dd> <dt>

<span id="ULONG_PTR"></span><span id="ulong_ptr"></span>ULONG\_PTR
</dt> <dd>

When the *ProcessInformationClass* parameter is **ProcessWow64Information**, the buffer pointed to by the *ProcessInformation* parameter should be large enough to hold a **ULONG\_PTR**. If this value is nonzero, the process is running in a WOW64 environment; otherwise, if the value is equal to zero, the process is not running in a WOW64 environment.

It is best to use the [**IsWow64Process**](/windows/desktop/api/WinBase/nf-wow64apiset-iswow64process) function to determine whether a process is running in the WOW64 environment.

</dd> <dt>

<span id="UNICODE_STRING"></span><span id="unicode_string"></span>UNICODE\_STRING
</dt> <dd>

When the *ProcessInformationClass* parameter is **ProcessImageFileName**, the buffer pointed to by the *ProcessInformation* parameter should be large enough to hold a **UNICODE\_STRING** structure as well as the string itself. The string stored in the **Buffer** member is the name of the image file.

If the buffer is too small, the function fails with the STATUS\_INFO\_LENGTH\_MISMATCH error code and the *ReturnLength* parameter is set to the required buffer size.

</dd> </dl> </dd> <dt>

*ProcessInformationLength* \[in\]
</dt> <dd>

The size of the buffer pointed to by the *ProcessInformation* parameter, in bytes.

</dd> <dt>

*ReturnLength* \[out, optional\]
</dt> <dd>

A pointer to a variable in which the function returns the size of the requested information. If the function was successful, this is the size of the information written to the buffer pointed to by the *ProcessInformation* parameter, but if the buffer was too small, this is the minimum size of buffer needed to receive the information successfully.

</dd> </dl>

## Return value

Returns an NTSTATUS success or error code.

The forms and significance of NTSTATUS error codes are listed in the Ntstatus.h header file available in the DDK, and are described in the DDK documentation under Kernel-Mode Driver Architecture / Design Guide / Driver Programming Techniques / Logging Errors.

## Remarks

The **ZwQueryInformationProcess** function and the structures that it returns are internal to the operating system and subject to change from one release of Windows to another. To maintain the compatibility of your application, it is better to use public functions mentioned in the description of the *ProcessInformationClass* parameter instead.

If you do use **ZwQueryInformationProcess**, access the function through [run-time dynamic linking](https://msdn.microsoft.com/windows/desktop/0ffce2b1-ce50-4550-aa68-6628fdcac01a). This gives your code an opportunity to respond gracefully if the function has been changed or removed from the operating system. Signature changes, however, may not be detectable.

This function has no associated import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions to dynamically link to Ntdll.dll.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl> |



## See also

<dl> <dt>

[**CheckRemoteDebuggerPresent**](https://msdn.microsoft.com/windows/desktop/e7eb2d48-4ef3-4708-8895-2bc33d2c3e91)
</dt> <dt>

[**GetProcessId**](/windows/desktop/api/WinBase/nf-processthreadsapi-getprocessid)
</dt> <dt>

[**IsDebuggerPresent**](https://msdn.microsoft.com/windows/desktop/7bc4bcb7-3f85-4349-a1da-c4ebee2d3e3f)
</dt> <dt>

[**IsWow64Process**](/windows/desktop/api/WinBase/nf-wow64apiset-iswow64process)
</dt> </dl>

 

 




