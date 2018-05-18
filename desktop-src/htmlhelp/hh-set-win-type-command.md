---
title: HH\_SET\_WIN\_TYPE command
description: Creates a new help window or modifies an existing help window at run time.
ms.assetid: '49992165-6B8F-4014-858B-53B0041907D7'
---

# HH\_SET\_WIN\_TYPE command

Creates a new help window or modifies an existing help window at run time.



| *pszFile*                                                                                                                                                                                                                                                                                                                     | *dwData*                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Specifies the name of the window type that you want to create or modify and the name of the compiled help (.chm) file in which the window type is defined. The window type name must begin with a greater-than (&gt;) character and must be preceded by the name of the compiled help file in which it is defined.<br/> | Points to an [**HH\_WINTYPE**](hh-wintype-structure.md) structure. |



 

## Example


```
HH_WINTYPE WinType ;
...
HtmlHelp(
          GetDesktopWindow(),
          "..\\help.chm>mainwin",
          HH_SET_WIN_TYPE,
          (DWORD) &amp;WinType) ;
```



## Return Value

-   On success, the handle (*hwnd*) of the help window.
-   On success, NULL, if the help window has not yet been created.
-   On failure, NULL, if the specified window type has not been defined.

## Remarks

-   Using the window type specified in *pszFile* to display multiple compiled help files is permitted, but not recommended.
-   Always specify the name of the compiled help file in which the window type is defined when calling an API command. If the window type is not defined in a help file, then specify NULL.
-   If a NULL is passed to **HH\_SET\_WIN\_TYPE**, the name of the window type is placed into an array and is treated as a [global window type](about-global-windows.md). A global window type is a window type that is not specific to a particular compiled help file. Only use global window types if you require backward compatibility for existing applications.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_GET\_WIN\_TYPE](hh-get-win-type-command.md)
</dt> </dl>

 

 





