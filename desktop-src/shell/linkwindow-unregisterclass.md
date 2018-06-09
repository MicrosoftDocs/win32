---
Description: Unregisters a window class registered by LinkWindow\_RegisterClass.
ms.assetid: 9e5c4326-efd1-43ca-a087-a436fe3f9bbd
title: LinkWindow\_UnregisterClass function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LinkWindow\_UnregisterClass function

\[This function is available through Windows XP with Service Pack 2 (SP2) and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows.\]

Unregisters a window class registered by [**LinkWindow\_RegisterClass**](linkwindow-registerclass.md).

## Syntax


```C++
BOOL LinkWindow_UnregisterClass(void);
```



## Parameters

This function has no parameters.

## Return value

Type: **BOOL**

Returns **TRUE** if the operation was successful; **FALSE** otherwise.

## Remarks

This function does not have an associated header or library file so it must be called by ordinal value. Call [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) with the DLL name Shell32.dll to obtain a module handle. Then call [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) with that module handle and the ordinal number 259 to use this function.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[Overview of SysLink Controls](38cfac3d-de60-4882-a434-4f498330b77d)
</dt> </dl>

 

 




