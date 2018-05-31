---
title: HH\_HELP\_CONTEXT command
description: Displays a help topic based on a mapped topic ID.
ms.assetid: 09C20812-FD9A-4e07-AC7F-0C85DFB7A7E6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HH\_HELP\_CONTEXT command

Displays a help topic based on a mapped topic ID.

If a window type is not specified, a default window type is used. If the window type or default window type is open, the help topic replaces the current topic in the window.



| *pszFile*                                                                                                                                                                                                   | *dwData*                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Specifies the compiled help (.chm) file that contains the mapping information. To specify a defined window type, insert a greater-than (&gt;) character followed by the name of the window type.<br/> | Specifies the numeric ID of the topic to display. You must map symbolic IDs of dialog boxes to numeric IDs in the \[MAP\] section of your project (.hhp) file.<br/> |



 

## Example


```
HtmlHelp(
          GetDesktopWindow(),
          "help.chm",
          HH_HELP_CONTEXT,
          5000) ;
```



## Remarks

-   A default help window contains only the Topic pane and is not a three-pane Help Viewer.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_DISPLAY\_TOPIC](hh-display-topic-command.md)
</dt> </dl>

 

 





