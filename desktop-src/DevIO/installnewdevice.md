---
description: Installs a new device. The user is prompted to select the device.
ms.assetid: 9bdee82c-1d0a-41ea-8b42-7ad96ac37663
title: InstallNewDevice function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InstallNewDevice
api_type: 
- DllExport
api_location: 
- NewDev.dll
---

# InstallNewDevice function

Installs a new device. The user is prompted to select the device.

## Syntax


```C++
BOOL WINAPI InstallNewDevice(
  _In_  HWND   hwndParent,
  _In_  LPGUID ClassGuid,
  _Out_ PDWORD pReboot
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

A handle to the top-level window to be used for any required user interface.

</dd> <dt>

*ClassGuid* \[in\]
</dt> <dd>

A pointer to a class **GUID**. This parameter is optional. If this parameter is **NULL**, the user starts at the detection choice page. If this parameter is **GUID\_NULL** or **GUID\_DEVCLASS\_UNKNOWN**, the user starts at the class selection page.

</dd> <dt>

*pReboot* \[out\]
</dt> <dd>

A pointer to a variable that receives the reboot status. This parameter can be **DI\_NEEDRESTART** or **DI\_NEEDREBOOT**.

</dd> </dl>

## Return value

If the function succeeds, the return value is nonzero.

If the function fails, the return value is zero. To get extended error information, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

## Remarks

This function has no associated import library. You must use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to NewDev.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| DLL<br/>                      | <dl> <dt>NewDev.dll</dt> </dl> |



## See also

<dl> <dt>

[Device Management Functions](device-management-functions.md)
</dt> </dl>

 

