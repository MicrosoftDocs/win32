---
description: The virtual memory functions enable a process to manipulate or determine the status of pages in its virtual address space.
ms.assetid: 9488a854-1ef0-488f-b3d1-57c1acb82a88
title: Virtual Memory Functions
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Memory Functions

The virtual memory functions enable a process to manipulate or determine the status of pages in its virtual address space. They can perform the following operations:

-   Reserve a range of a process's virtual address space. Reserving address space does not allocate any physical storage, but it prevents other allocation operations from using the specified range. It does not affect the virtual address spaces of other processes. Reserving pages prevents needless consumption of physical storage, while enabling a process to reserve a range of its address space into which a dynamic data structure can grow. The process can allocate physical storage for this space, as needed.
-   Commit a range of reserved pages in a process's virtual address space so that physical storage (either in RAM or on disk) is accessible only to the allocating process.
-   Specify read/write, read-only, or no access for a range of committed pages. This differs from the standard allocation functions that always allocate pages with read/write access.
-   Free a range of reserved pages, making the range of virtual addresses available for subsequent allocation operations by the calling process.
-   Decommit a range of committed pages, releasing their physical storage and making it available for subsequent allocation by any process.
-   Lock one or more pages of committed memory into physical memory (RAM) so that the system cannot swap the pages out to the paging file.
-   Obtain information about a range of pages in the virtual address space of the calling process or a specified process.
-   Change the access protection for a specified range of committed pages in the virtual address space of the calling process or a specified process.

For more information, see the following topics.

-   [Allocating Virtual Memory](allocating-virtual-memory.md)
-   [Comparing Memory Allocation Methods](comparing-memory-allocation-methods.md)
-   [Freeing Virtual Memory](freeing-virtual-memory.md)
-   [Working With Pages](working-with-pages.md)
-   [Memory Management Functions](memory-management-functions.md)

 

 



