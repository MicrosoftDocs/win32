---
title: HH\_GET\_WIN\_HANDLE command
description: Returns the handle (hwnd) of a specified window type.
ms.assetid: 908E3E61-6990-40cc-8B7F-489150EB28D2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HH\_GET\_WIN\_HANDLE command

Returns the handle (hwnd) of a specified window type.



| *pszFile*                                                                                | *dwData*                                                               |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Specifies the name of the compiled help (.chm) file in which the window type is defined. | Specifies the name of the window type whose handle you want to return. |



 

## Example


```
HtmlHelp(
         hwndCaller,
         "c:\\MyHelpFile.chm",
         HH_GET_WIN_HANDLE,
         (DWORD) "MyWindowType") ;
```



## Return Value

-   The handle (hwnd) of the window type specified in the *dwData* parameter.
-   NULL, if the help window has not yet been created.

## Remarks

-   Always specify the name of the compiled help (.chm) file in which the window type is defined when calling an API command. If the window type is not defined in a compiled help file, then specify NULL.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_GET\_WIN\_TYPE](hh-get-win-type-command.md)
</dt> <dt>

[HH\_SET\_WIN\_TYPE](hh-set-win-type-command.md)
</dt> </dl>

 

 




