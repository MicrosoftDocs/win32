---
title: HH\_ALINK\_LOOKUP command
description: Looks up one or more Associative link (ALink) names in a compiled help (.chm) file.
ms.assetid: 'E9BA3037-1402-4021-A1BB-B15774AAD5A3'
---

# HH\_ALINK\_LOOKUP command

Looks up one or more Associative link (ALink) names in a compiled help (.chm) file.

The ALink names to search for, and the action to be taken if no matches are found, are specified in the **HH\_AKLINK** structure.



| *pszFile*                                                          | *dwData*                                                          |
|--------------------------------------------------------------------|-------------------------------------------------------------------|
| Specifies the compiled help (.chm) file that contains ALink names. | Points to an [**HH\_AKLINK**](hh-aklink-structure.md) structure. |



 

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
         "c:\\MyHelp.chm",
         HH_ALINK_LOOKUP,
         (DWORD) &amp;link) ;
```



## Return Value

The handle (hwnd) of the help window.

## Remarks

-   You must first call the [HH\_DISPLAY\_TOPIC](hh-display-topic-command.md) command before calling this command, to ensure that the help window is created.
-   Help authors insert ALink names into target topic files using the HTML Help **Compiler Information** feature.
-   An ALink name lookup can also be invoked using the HTML Help ActiveX control [ALink](alink.md) command.
-   ALink name/KLink keyword lookups are case sensitive. Multiple keywords are delimited by a semicolon.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_KEYWORD\_LOOKUP](hh-keyword-lookup-command.md)
</dt> </dl>

 

 




