---
title: Notes on WPA Process Heap Analysis
description: Notes on WPA Process Heap Analysis
ms.assetid: 64ed2b5b-153f-4cf9-97f4-dd0dd18dbcef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Notes on WPA Process Heap Analysis

> [!Note]  
> It is assumed the reader has completed and understands the Quick Start exercise in the previous section before using this section of the document.

 

The most important metrics for heap analysis are typically ranked by importance in the following order:

1.  Outstanding size - A large outstanding size will have an impact on both the process footprint and overall system performance. This is due to contention for system resources such as memory and page file space.

2.  Peak size - Peak size measures the maximum heap usage for a process. If peak size is inordinately large a process can consume memory pages from the standby list or force other processes to trim their working sets.

3.  Outstanding count - Outstanding counts increase the heap overhead by 8 bytes per allocation. These 8 bytes are used by the heap manager to manage an allocation. In a situation with large numbers of allocations, this overhead can become significant. The result of this increased overhead can be reduced data density and lower overall process performance.

4.  Total size and Total Count - Total size and total count of allocations are important from both a CPU usage perspective and from a data locality perspective. Modern CPUs are highly dependent on processor caches for maximum execution efficiency. Accessing large amounts of data in random patterns will reduce the effectiveness of the CPU caches and overall execution speed.

> [!Note]  
> The heap WPA provider does not have rundown support. Rundown support for the heap provider would entail enumerating the heaps within the target process and each allocation, including the size and address. The CPU and elapsed time cost of doing this rundown is significant. As a result, the complete event data generated for sizes, number, addresses, or lifetimes of all the allocations from processes started outside of WPA are not available

 

 

 




