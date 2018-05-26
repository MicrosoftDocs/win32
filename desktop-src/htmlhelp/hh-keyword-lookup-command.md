---
title: HH\_KEYWORD\_LOOKUP command
description: Looks up one or more keywords in a compiled help (.chm) file.
ms.assetid: F91C9EB5-6660-47bd-AA8D-484B4E0DF1F6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HH\_KEYWORD\_LOOKUP command

Looks up one or more keywords in a compiled help (.chm) file.

The keywords to search for and the action to be taken if no matches are found are specified in the **HH\_AKLINK** structure.



| *pszFile*                                                       | *dwData*                                                          |
|-----------------------------------------------------------------|-------------------------------------------------------------------|
| Specifies the compiled help (.chm) file that contains keywords. | Points to an [**HH\_AKLINK**](/windows/previous-versions/HtmlHelp/ns-htmlhelp-taghh_aklink?branch=master) structure. |



 

## Example


```
HH_AKLINK link;
   link.cbStruct =     sizeof(HH_AKLINK) ;
   link.fReserved =    FALSE ;
   link.pszKeywords =  "open" ;
   link.pszUrl =       NULL ;
   link.pszMsgText =   NULL ;
   link.pszMsgTitle =  NULL ;
   link.pszWindow =    NULL ;
   link.fIndexOnFail = TRUE ;
HtmlHelp(
          GetDesktopWindow(),
          "c:\\myhelp.chm",
          HH_KEYWORD_LOOKUP,
          (DWORD)&amp;link);
```



## Return Value

The handle (*hwnd*) of the help window.

## Remarks

-   You must first call the [HH\_DISPLAY\_TOPIC](hh-display-topic-command.md) command before calling this command to ensure that the help window is created.
-   Help authors insert keywords into topic files using the HTML Help Compiler Information feature.
-   A keyword lookup can also be invoked using the HTML Help ActiveX control [KLink](klink.md) command.
-   ALink Name/Keyword lookups are case sensitive, and multiple keywords are delimited by a semicolon (;).

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_ALINK\_LOOKUP](hh-alink-lookup-command.md)
</dt> </dl>

 

 




