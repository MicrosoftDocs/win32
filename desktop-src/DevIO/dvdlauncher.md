---
description: Verifies that the media region in the DVD drive matches the DVD drive region.
ms.assetid: 864de493-94c2-4f32-96a8-14cfea13dbef
title: DvdLauncher function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DvdLauncher
api_type: 
- DllExport
api_location: 
- StorProp.dll
---

# DvdLauncher function

Verifies that the media region in the DVD drive matches the DVD drive region.

## Syntax


```C++
BOOL WINAPI DvdLauncher(
  _In_ HWND HWnd,
  _In_ CHAR DriveLetter
);
```



## Parameters

<dl> <dt>

*HWnd* \[in\]
</dt> <dd>

A handle to the top-level window to be used for any required user interface.

</dd> <dt>

*DriveLetter* \[in\]
</dt> <dd>

The drive letter.

</dd> </dl>

## Return value

If the function succeeds and the regions match, the return value is nonzero. Otherwise, the return value is zero.

## Remarks

This function has no associated import library. You must use the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/desktop/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to StorProp.dll.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                          |
| DLL<br/>                      | <dl> <dt>StorProp.dll</dt> </dl> |



## See also

<dl> <dt>

[Device Management Functions](device-management-functions.md)
</dt> </dl>

 

