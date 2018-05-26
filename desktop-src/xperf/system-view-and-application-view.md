---
title: System View and Application View
description: System View and Application View
ms.assetid: 48993cfd-0cff-4e55-ba61-28e5d40bcd80
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# System View and Application View

There are two distinct views of heap data presented by WPA when performing heap analysis, the system view and the application view.

-   The system view is represented in memory pages and consists of the number of memory pages committed to contain allocations across the system.

-   The application view is represented by the number and size of the allocations made by a process. The application view does not include any of the heap manger overhead used to manage the allocations. Therefore, the sum of allocations made by a process will always be smaller than the total number of memory pages used by the heap.

 

 




