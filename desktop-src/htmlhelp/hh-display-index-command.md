---
title: HH\_DISPLAY\_INDEX command
description: Selects the Index tab in the Navigation pane of the HTML Help Viewer and searches for the keyword specified in the dwData parameter.
ms.assetid: 9713739A-06FB-4d32-9813-64907D8CC189
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HH\_DISPLAY\_INDEX command

Selects the Index tab in the Navigation pane of the HTML Help Viewer and searches for the keyword specified in the *dwData* parameter.



| *pszFile*                                                                               | *dwData*                                                  |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Specifies a compiled help (.chm) file, or a specific topic within a compiled help file. | Specifies the keyword to select in the index (.hhk) file. |



 

## Example


```
HtmlHelp(
         hwnd,
         "cat.chm",
         HH_DISPLAY_INDEX,
         (DWORD)"meow") ;
```



## Return Value

The handle (*hwnd*) of the help window.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_DISPLAY\_TOC](hh-display-toc-command.md)
</dt> <dt>

[HH\_DISPLAY\_SEARCH](hh-display-search-command.md)
</dt> </dl>

 

 




