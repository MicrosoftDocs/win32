---
title: Graph Analysis Guidelines
description: Graph Analysis Guidelines
ms.assetid: f2804bdd-2040-4e6f-9a9a-88cc123265dd
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Graph Analysis Guidelines

-   Outstanding allocations should be noted when a particular activity completes. This can be determined by examining contiguous processes and events combined with knowledge of the scenario or test matrix used to collect the data.

-   The legend of each heap graph contains the heap handles associated with processes and threads.

-   Areas of peak usage are obvious from the display within the graphs. Areas with large transient allocations will show as slopes in the total allocation count or total allocation size graphs.

-   Areas where one or more heaps show growth in size or allocation count should be noted. These areas will appear as slopes in the lines. The steepness of the slope of the lines is an indication of the rate of growth in the size or count of the allocations.

-   If the application is performing allocations with short lifetimes, the heap lines in the outstanding size and outstanding allocation count graphs will contain spikes and troughs while the Heap Allocation Total Size and Heap Allocation Total Count graphs will show increases. The size and frequency of the spikes and troughs is an indication of the size or frequency of the transient allocations. Note that the outstanding size graph is scaled and processes with a large outstanding size will decrease the height of the spikes and troughs. Expanding the vertical size of the graph may be necessary to visualize these areas.

-   In some cases the graphs for the totals will show trends more clearly than the outstanding graphs. This is particularly true for small incremental growth in allocation count or allocation size over longer time intervals.

 

 




