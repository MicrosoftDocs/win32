---
title: Undersize Data Structures
description: Undersize Data Structures
ms.assetid: 'b68f7c83-11fe-4596-a4bc-0e74f509ff01'
---

# Undersize Data Structures

Sustained growth of dynamic data structures, such as arrays or buffers, often results in a large number of transient allocations. In the screen shot below, a butterfly view based on the functions that call the **ntdll.dll.RtlpReAllocateHeap** function, reveal two conditions that result in inefficient array or buffer management.

-   A regular increase in the size of a data structure.

-   Data structures that have an inappropriate initial size.

![screen shot of a butterfly view of outstanding allocations pivoted on ntdll.dll!rtlpreallocateheap, sorted by size](images/he-img26.png)

Drilling down this path, sorted by size, reveals that the **MSHTML.DLL!CImplAry::EnsureSize** routine is responsible for a large transient allocation size from a large number of reallocation calls. Drilling down further to the actual allocation timestamp information shows allocations of different sizes.

Since the array is grown in most instances on this call path, increasing the initial allocation size should result in a CPU improvement. Also, increasing the initial allocation size can result in a reduction in the peak outstanding size during this phase of execution.

 

 




