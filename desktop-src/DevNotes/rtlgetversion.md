---
Description: Gets version information about the currently running operating system.
ms.assetid: F04F0981-A07D-4B38-9DE4-B8461EAFC19F
title: RtlGetVersion function
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetVersion
api_type: 
- DllExport
api_location: 
- Ntdll.dll
- NtosKrnl.exe
---

# RtlGetVersion function

Gets version information about the currently running operating system.

## Syntax


```C++
NTSTATUS RtlGetVersion(
  _Out_ PRTL_OSVERSIONINFOW lpVersionInformation
);
```



## Parameters

<dl> <dt>

*lpVersionInformation* \[out\]
</dt> <dd>

Pointer to either a [**RTL\_OSVERSIONINFOW**](https://msdn.microsoft.com/en-us/library/Ff563624(v=VS.85).aspx) structure or a [**RTL\_OSVERSIONINFOEXW**](https://msdn.microsoft.com/en-us/library/Ff563620(v=VS.85).aspx) structure that contains the version information about the currently running operating system. A caller specifies which input structure is used by setting the **dwOSVersionInfoSize** member of the structure to the size in bytes of the structure that is used.

</dd> </dl>

## Return value

Returns STATUS\_SUCCESS.

## Remarks

**RtlGetVersion** is the equivalent of the [**GetVersionEx**](https://msdn.microsoft.com/en-us/library/ms724451(v=VS.85).aspx) function in the Windows SDK. See the example in the Windows SDK that shows how to get the system version.

When using **RtlGetVersion** to determine whether a particular version of the operating system is running, a caller should check for version numbers that are greater than or equal to the required version number. This ensures that a version test succeeds for later versions of Windows.

Because operating system features can be added in a redistributable DLL, checking only the major and minor version numbers is not the most reliable way to verify the presence of a specific system feature. A driver should use [**RtlVerifyVersionInfo**](https://msdn.microsoft.com/en-us/library/Ff563026(v=VS.85).aspx) to test for the presence of a specific system feature.

## Requirements



|                                     |                                                                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                                                                     |
| Target platform<br/>          | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl>                  |
| Header<br/>                   | <dl> <dt>Ntddk.h (include Ntddk.h)</dt> </dl>                                                     |
| Library<br/>                  | <dl> <dt>Ntdll.lib; </dt> <dt>NtosKrnl.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdll.dll; </dt> <dt>NtosKrnl.exe</dt> </dl> |



## See also

<dl> <dt>

[**PsGetVersion**](https://msdn.microsoft.com/en-us/library/Ff559941(v=VS.85).aspx)
</dt> </dl>

 

 




