---
title: HH\_CLOSE\_ALL command
description: Closes all windows opened directly or indirectly by the calling program.
ms.assetid: DFCB4403-F311-4477-A06D-35562BD311F9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HH\_CLOSE\_ALL command

Closes all windows opened directly or indirectly by the calling program.



| *hwndCaller*  | *pszFile*     | *dwData*      |
|---------------|---------------|---------------|
| Must be NULL. | Must be NULL. | Must be zero. |



 

## Example


```
HtmlHelp(
         NULL,
         NULL,
         HH_CLOSE_ALL,
         0) ;
```



## Return Value

NULL.

## Remarks

-   This command closes any compiled help (.chm) files that are open.
-   This command only closes help windows that have been created by the calling program.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




