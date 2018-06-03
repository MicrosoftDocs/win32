---
Description: Verifies that the media region in the DVD drive matches the DVD drive region.
ms.assetid: 864de493-94c2-4f32-96a8-14cfea13dbef
title: DvdLauncher function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to StorProp.dll.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                          |
| DLL<br/>                      | <dl> <dt>StorProp.dll</dt> </dl> |



## See also

<dl> <dt>

[Device Management Functions](device-management-functions.md)
</dt> </dl>

 

 




