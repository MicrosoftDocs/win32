---
title: Actions Analysis Suggestions
description: Actions Analysis Suggestions
ms.assetid: 3246b1df-cb23-4f94-b8d6-f2615ba0d4e6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Actions Analysis Suggestions

-   Start by examining the graph in XPerfview, looking for prominent bumps and spikes, and checking the typical outstanding allocation size to see whether it is reasonable.

-   Next, run the heap action with "-frames -s\[t\|tc\|o\]", refining and using a cull list to obtain a more informative "-frames" summary. The idea is to identify heavy allocators in terms of outstanding size, total size or total count.

-   For each prominent item in the "-frames" output (item near the top of the list), perform "-stacks -s\[t\|tc\|o\] -requireFrames", requiring the "-frames" item being examined. The resultant call stacks provide a hint of why the allocations are being made.

 

 




