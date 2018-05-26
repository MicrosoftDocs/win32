---
title: Hard Faults
description: Hard Faults
ms.assetid: e1496e8a-2029-4747-b57e-f6501d203d07
keywords:
- usage graph
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Hard Faults

**Overview:** Counts hard page faults over a time interval, as shown in the following screen shot.

![screen shot of a graph showing the count of disk accesses required to retrieve memory pages](images/gr-img023.png)

**Graph Type:** Event graph

**Y-axis Units:** Count of system hard faults

**Required Flags:** HARD\_FAULTS

**Events Captured:** Hard fault events

**Legend Description:** Shows hard fault count

**Graph Description:** Hard faults occur when the operating system retrieves memory pages from disk rather than from the in-memory pages that the memory manager maintains.

For more information on this topic see **Windows Internals** by David A. Solomon and Mark E. Russinovich (4th edition, Microsoft Press, 2005).

 

 




