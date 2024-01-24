---
description: The working set of a process is the set of pages in the virtual address space of the process that are currently resident in physical memory.
ms.assetid: ff05276a-1d40-4844-b649-10e32e3f1937
title: Working Set
ms.topic: article
ms.date: 05/31/2018
---

# Working Set

The working set of a process is the set of pages in the virtual address space of the process that are currently resident in physical memory. The working set contains only pageable memory allocations; nonpageable memory allocations such as [Address Windowing Extensions](address-windowing-extensions.md) (AWE) or [large page allocations](large-page-support.md) are not included in the working set.

When a process references pageable memory that is not currently in its working set, a *page fault* occurs. The system page fault handler attempts to resolve the page fault and, if it succeeds, the page is added to the working set. (Accessing AWE or large page allocations never causes a page fault, because these allocations are not pageable.)

A *hard page fault* must be resolved by reading page contents from the page's *backing store*, which is either the system paging file or a memory-mapped file created by the process. A *soft page fault* can be resolved without accessing the backing store. A soft page fault occurs when:

-   The page is in the working set of some other process, so it is already resident in memory.
-   The page is in transition, because it either has been removed from the working sets of all processes that were using the page and has not yet been repurposed, or it is already resident as a result of a memory manager prefetch operation.
-   A process references an allocated virtual page for the first time (sometimes called a *demand-zero fault*).

Pages can be removed from a process working set as a result of the following actions:

-   The process reduces or empties the working set by calling the [**SetProcessWorkingSetSize**](/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsize), [**SetProcessWorkingSetSizeEx**](/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex) or [**EmptyWorkingSet**](/windows/win32/api/psapi/nf-psapi-emptyworkingset) function.
-   The process calls the [**VirtualUnlock**](/windows/win32/api/memoryapi/nf-memoryapi-virtualunlock) function on a memory range that is not locked.
-   The process unmaps a mapped view of a file using the [**UnmapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-unmapviewoffile) function.
-   The memory manager trims pages from the working set to create more available memory.
-   The memory manager must remove a page from the working set to make room for a new page (for example, because the working set is at its maximum size).

If several processes share a page, removing the page from the working set of one process does not affect other processes. After a page is removed from the working sets of all processes that were using it, the page becomes a *transition page*. Transition pages remain cached in RAM until the page is either referenced again by some process or repurposed (for example, filled with zeros and given to another process). If a transition page has been modified since it was last written to disk (that is, if the page is "dirty"), then the page must be written to its backing store before it can be repurposed. The system may start writing dirty transition pages to their backing store as soon as such pages become available.

Each process has a minimum and maximum working set size that affect the virtual memory paging behavior of the process. To obtain the current size of the working set of a specified process, use the [**GetProcessMemoryInfo**](/windows/win32/api/psapi/nf-psapi-getprocessmemoryinfo) function. To obtain or change the minimum and maximum working set sizes, use the [**GetProcessWorkingSetSizeEx**](/windows/win32/api/memoryapi/nf-memoryapi-getprocessworkingsetsizeex) and [**SetProcessWorkingSetSizeEx**](/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex) functions.

The process status application programming interface (PSAPI) provides a number of functions that return detailed information about the working set of a process. For details, see [Working Set Information](../psapi/working-set-information.md).

 

 
