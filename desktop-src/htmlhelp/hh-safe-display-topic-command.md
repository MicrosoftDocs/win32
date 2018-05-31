---
title: HH\_SAFE\_DISPLAY\_TOPIC command
description: Opens a help topic in a specified help window, and disables all shortcuts in the current process. Shortcuts will remain disabled as long as the calling process is active. This command can be used in place of HH\_DISPLAY\_TOPIC Command.
ms.assetid: F95B712A-1C01-4bab-B87C-5174D586AFB5
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HH\_SAFE\_DISPLAY\_TOPIC command

Opens a help topic in a specified help window, and disables all shortcuts in the current process. Shortcuts will remain disabled as long as the calling process is active. This command can be used in place of [HH\_DISPLAY\_TOPIC Command](hh-display-topic-command.md).

If a window type is not specified, a default window type is used. If the window type or default window type is open, the help topic replaces the current topic in the window.



| *pszFile*                                                                                                                                                                                                           | *dwData*                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Specifies a compiled help (.chm) file, or a specific topic within a compiled help file. To specify a defined window type, insert a greater-than (&gt;) character followed by the name of the window type<br/> | Specifies NULL or a pointer to a topic within a compiled help file. |



 

## Example


```
HWND hwnd =
   HtmlHelp(
             GetDesktopWindow(),
             "file:///c:\\help.chm::/intro.htm>mainwin",
             HH_SAFE_DISPLAY_TOPIC,
             NULL) ;
```



## Return Value

-   The handle (*hwnd*) of the help window.

## Remarks

-   A default help window contains only the Topic pane and is not a three-pane Help Viewer.
-   The HH\_SAFE\_DISPLAY\_TOPIC command will only work with the following standard protocols:
    -   ftp:
    -   http:
    -   https:
    -   ms-its:
    -   its:
    -   file:
    -   mk@msitstore:

## Related topics

<dl> <dt>

[HH\_HELP\_CONTEXT Command](hh-help-context-command.md)
</dt> <dt>

[HH\_DISPLAY\_TOPIC Command](hh-display-topic-command.md)
</dt> </dl>

 

 





