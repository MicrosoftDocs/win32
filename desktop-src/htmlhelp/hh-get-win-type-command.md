---
title: HH\_GET\_WIN\_TYPE command
description: Retrieves a pointer to the HH\_WINTYPE structure associated with a specified window type.
ms.assetid: '18F5020C-7AD0-4e4f-A241-06F5E7C4EA35'
---

# HH\_GET\_WIN\_TYPE command

Retrieves a pointer to the **HH\_WINTYPE** structure associated with a specified window type.



| *pszFile*                                                                                                                                                                                                                                                                                                          | *dwData*                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Specifies the name of the window type whose information you want to get and the name of the compiled help (.chm) file in which the window type is defined. The window name must begin with a greater-than (&gt;) character and must be preceded by the name of the compiled help file it is defined in.<br/> | Specifies the address of a pointer to an [**HH\_WINTYPE**](hh-wintype-structure.md) structure. Deep copy the structure to which *dwData* points before modifying the structure.<br/> |



 

## Example


```
HH_WINTYPE* pWinType ;
HtmlHelp(
          GetDesktopWindow(),
          "Help.chm>mainwin",
          HH_GET_WIN_TYPE,
          (DWORD) &amp;pWinType) ;
```



## Return Value

-   On success, the handle (hwnd) of the parent help window, if the specified window type has been defined.
-   On success, NULL, if the help window has not yet been created.
-   On failure, -1, if the specified window type has not been defined.

## Remarks

-   Always specify the name of the compiled help file in which the window type is defined when calling an API command. If the window type is not defined in a .chm file, then specify NULL.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_SET\_WIN\_TYPE](hh-set-win-type-command.md)
</dt> </dl>

 

 





