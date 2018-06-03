---
title: LegitCheck function
description: Returns a value that indicates whether the copy of Windows running on the current system is genuine.
ms.assetid: 467d778e-842e-416a-89f6-b4639934f1bd
keywords:
- LegitCheck function Windows Genuine
topic_type:
- apiref
api_name:
- LegitCheck
api_location:
- LegitLib.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LegitCheck function

\[This function is no longer available for use as of Windows 7.\]

Returns a value that indicates whether the copy of Windows running on the current system is genuine.

The **LegitCheck** function is not declared in a public header and has no associated import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to LegitLib.dll.

## Syntax


```C++
int __stdcall LegitCheck(void);
```



## Parameters

This function has no parameters.

## Return value

This function returns zero if the copy of Windows running on the current system is genuine. If the value of this parameter is any other value, the copy of Windows running on the current system is not genuine.

## Remarks

The Windows Genuine Advantage (WGA) functions are available only on Windows Vista and Windows XP installations that have been validated by clicking **Validate Windows** on [http://www.microsoft.com/genuine](http://go.microsoft.com/fwlink/p/?linkid=157937).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | None supported<br/>                                                               |
| End of client support<br/>    | Windows Vista<br/>                                                                |
| End of server support<br/>    | None supported<br/>                                                               |
| DLL<br/>                      | <dl> <dt>LegitLib.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Genuine Advantage API Functions](windows-genuine-advantage-api-functions.md)
</dt> </dl>

 

 





