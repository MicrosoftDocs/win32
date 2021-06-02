---
description: The InstallWiaDevice function installs a Windows Image Acquisition (WIA) device as root-enumerated device. It may popup a security warning if any installing file or coinstaller is not digitally signed and trusted.
ms.assetid: c7de27f5-5994-4fce-a6ec-6e7cfae2e591
title: InstallWiaDevice function (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InstallWiaDevice
api_type: 
- LibDef
api_location: 
- Wiaguid.lib
- Wiaguid.dll
---

# InstallWiaDevice function

The **InstallWiaDevice** function installs a Windows Image Acquisition (WIA) device as root-enumerated device. It may popup a security warning if any installing file or coinstaller is not digitally signed and trusted.

## Syntax


```C++
DWORD WINAPI InstallWiaDevice(
  _In_ PWIADEVICEINSTALL *pWiaDeviceInstall
);
```



## Parameters

<dl> <dt>

*pWiaDeviceInstall* \[in\]
</dt> <dd>

Type: **PWIADEVICEINSTALL\***

Pointer to a WIADEVICEINSTALL structure. The *szFriendlyName* member of the structure must be set to the actual device FriendlyName.

</dd> </dl>

## Return value

Type: **DWORD**

If the function succeeds, the return value is ERROR\_SUCCESS.

If the function fails, it returns a Win32 error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>       |
| Library<br/>                  | <dl> <dt>Wiaguid.lib</dt> </dl> |



 

 




