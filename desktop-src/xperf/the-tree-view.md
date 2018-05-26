---
title: The Tree View
description: The Tree View
ms.assetid: fe6152b8-757e-4bb2-b822-606a5e4e0431
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Tree View

The tree view is usually the first step in summary table analysis. Sort the summary table by allocation type and allocation size. The resulting tree view displays the allocations responsible for persistent heap usage.

A call stack for investigation can be selected by clicking on the corresponding row and then using the right arrow on the keyboard to expand the visible portion of the stack. Holding down the right arrow key does recursive expansion down the path determined by the sorting order specified by the column selection. Conversely, holding down the left arrow collapses the visible portion of the stack. The mouse can also be used to expand and contract individual rows by clinking on the \[+\] or \[-\].

The following screen shot shows a Tree view sorted by allocation size.

![screen shot of a tree view sorted by allocation size](images/he-img14.png)

This tree view, **Tree view sorted by allocation size**, shows the atiumdag.dll responsible for the bulk of the allocation size in the first call stack. The question mark where the function name would typcially appear indicates that symbols for this module are not available. This it is not unexpected since atiumdag.dll is the ATI Universal DirectX video driver for which there are no publicly available symbols.

 

 




