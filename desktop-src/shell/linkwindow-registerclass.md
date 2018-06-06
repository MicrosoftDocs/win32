---
Description: Registers a window class that allows for the SysLink common control to be used in a window.
ms.assetid: 1e6dd741-81be-40bb-a8b5-d565f593c4e9
title: LinkWindow\_RegisterClass function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LinkWindow\_RegisterClass function

\[This function is available through Windows XP with Service Pack 2 (SP2) and Windows Server 2003. It might be altered or unavailable in subsequent versions of Windows. Use [**InitCommonControlsEx**](https://msdn.microsoft.com/VS|Controls|~\controls\common\functions\initcommoncontrolsex.htm) instead.\]

Registers a window class that allows for the [SysLink](https://www.bing.com/search?q=SysLink) common control to be used in a window.

## Syntax


```C++
BOOL LinkWindow_RegisterClass(void);
```



## Parameters

This function has no parameters.

## Return value

Type: **BOOL**

Returns **TRUE** if registration was successful; **FALSE** otherwise.

## Remarks

This function does not have an associated header or library file so it must be called by ordinal value. Call [**LoadLibrary**](https://msdn.microsoft.com/d936b4dd-058c-48e1-834b-b47ef6d8ef65) with the DLL name Shell32.dll to obtain a module handle. Then call [**GetProcAddress**](https://msdn.microsoft.com/a0d7fc09-f888-4f46-a571-d3719a627597) with that module handle and the ordinal number 258 to use this function.

Use [**LinkWindow\_UnregisterClass**](linkwindow-unregisterclass.md) to unregister the class after use.

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[Overview of SysLink Controls](https://www.bing.com/search?q=Overview+of+SysLink+Controls)
</dt> </dl>

 

 




