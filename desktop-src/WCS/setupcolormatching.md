---
title: SetupColorMatching function
description: The SetupColorMatching function creates a Color Management dialog box that lets the user choose whether to enable color management, and if so, provides control over the color profiles used and over the rendering intent.
ms.assetid: 7d3b6d3f-49f4-46f5-a43b-868e53965d8f
keywords:
- SetupColorMatching function Windows Color System
topic_type:
- apiref
api_name:
- SetupColorMatching
- SetupColorMatchingA
- SetupColorMatchingW
api_location:
- icmui.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetupColorMatching function

The **SetupColorMatching** function creates a Color Management dialog box that lets the user choose whether to enable color management, and if so, provides control over the color profiles used and over the [rendering intent](https://www.bing.com/search?q=rendering intent).

## Syntax


```C++
BOOL WINAPI SetupColorMatching(
   PCOLORMATCHSETUP pcms
);
```



## Parameters

<dl> <dt>

*pcms* 
</dt> <dd>

Pointer to a [**COLORMATCHSETUP**](colormatchsetup.md) structure that on entry contains information used to initialize the dialog box.

When **SetupColorMatching** returns, if the user clicked the OK button, this structure contains information about the user's selection. Otherwise, if an error occurred or the user canceled the dialog box, the structure is left unchanged.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE** indicating that no errors occurred and the user clicked the OK button.

If this function fails, the return value is **FALSE** indicating that an error occurred or the dialog was canceled. For extended error information, call **GetLastError**.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Icmui.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Icmui.dll</dt> </dl> |
| Unicode and ANSI names<br/>   | **SetupColorMatchingW** (Unicode) and **SetupColorMatchingA** (ANSI)<br/>      |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





