---
title: HH\_DISPLAY\_SEARCH command
description: Selects the Search tab in the Navigation pane of the HTML Help Viewer, but does not actually perform a search.
ms.assetid: CD1CE76C-4598-4820-82D0-7F5ED4D32651
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HH\_DISPLAY\_SEARCH command

Selects the **Search** tab in the Navigation pane of the HTML Help Viewer, but does not actually perform a search.



| *pszFile*                                                                               | *dwData*                                                                              |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Specifies a compiled help (.chm) file, or a specific topic within a compiled help file. | Specifies a pointer to an [**HH\_FTS\_QUERY**](/windows/previous-versions/HtmlHelp/ns-htmlhelp-taghh_fts_query?branch=master) structure. |



 

## Example


```
HH_FTS_QUERY q ;

HtmlHelp(
         hwnd,
         "cat.chm",
         HH_DISPLAY_SEARCH,
         (DWORD)&amp;q) ;
```



## Return Value

The handle (*hwnd*) of the help window.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_DISPLAY\_INDEX](hh-display-index-command.md)
</dt> <dt>

[HH\_DISPLAY\_TOC](hh-display-toc-command.md)
</dt> </dl>

 

 




