---
title: HH\_DISPLAY\_TOC command
description: Selects the Contents tab in the Navigation pane of the HTML Help Viewer.
ms.assetid: 15D66EC6-71E5-43ad-8D75-9711293FFAB8
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HH\_DISPLAY\_TOC command

Selects the Contents tab in the Navigation pane of the HTML Help Viewer.



| *pszFile*                                                                               | *dwData*                                                            |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Specifies a compiled help (.chm) file, or a specific topic within a compiled help file. | Specifies NULL or a pointer to a topic within a compiled help file. |



 

## Example


```
HtmlHelp(
         GetDesktopWindow(),
         "c:\\MyHelpFile.chm::/intro.htm",
         HH_DISPLAY_TOC,
         NULL) ;
```



## Return Value

The handle (*hwnd*) of the help window.

## Remarks

-   This command provides the same functionality as **HH\_DISPLAY\_TOPIC**.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_DISPLAY\_INDEX](hh-display-index-command.md)
</dt> <dt>

[HH\_DISPLAY\_SEARCH](hh-display-search-command.md)
</dt> <dt>

[HH\_DISPLAY\_TOPIC](hh-display-topic-command.md)
</dt> </dl>

 

 




