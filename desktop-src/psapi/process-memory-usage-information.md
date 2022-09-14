---
title: Process Memory Usage Information
description: The GetProcessMemoryInfo function takes a process handle as input and fills a PROCESS\_MEMORY\_COUNTERS structure with information about the memory statistics for the process.
ms.assetid: 683c899e-a7e8-4440-8f13-2a713c1618bf
ms.topic: article
ms.date: 05/31/2018
---

# Process Memory Usage Information

The [**GetProcessMemoryInfo**](/windows/desktop/api/Psapi/nf-psapi-getprocessmemoryinfo) function takes a process handle as input and fills a [**PROCESS\_MEMORY\_COUNTERS**](/windows/desktop/api/Psapi/ns-psapi-process_memory_counters) structure with information about the memory statistics for the process. The **cb** member receives the size of the structure. The **PageFaultCount** member receives the number of page faults. The remaining members receive the current and peak memory usage in the following categories:

-   working set
-   paged pool
-   nonpaged pool
-   pagefile

The *working set* is the amount of memory physically mapped to the process context at a given time. Memory in the *paged pool* is system memory that can be transferred to the paging file on disk (paged) when it is not being used. Memory in the *nonpaged pool* is system memory that cannot be paged to disk as long as the corresponding objects are allocated. The *pagefile* usage represents how much memory is set aside for the process in the system paging file. When memory usage is too high, the virtual memory manager pages selected memory to disk. When a thread needs a page that is not in memory, the memory manager reloads it from the paging file.

 

 




