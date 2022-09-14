---
description: Each process on 32-bit Microsoft Windows has its own virtual address space that enables addressing up to 4 gigabytes of memory.
ms.assetid: f259f3cb-81c0-4b5f-b6fa-9681a278019a
title: About Memory Management
ms.topic: article
ms.date: 05/31/2018
---

# About Memory Management

Each process on 32-bit Microsoft Windows has its own virtual address space that enables addressing up to 4 gigabytes of memory. Each process on 64-bit Windows has a virtual address space of 8 terabytes. All threads of a process can access its virtual address space. However, threads cannot access memory that belongs to another process, which protects a process from being corrupted by another process.

For information on the virtual address space and the memory management functions, see the following topics.

-   [Virtual Address Space](virtual-address-space.md)
-   [Memory Pools](memory-pools.md)
-   [Memory Performance Information](memory-performance-information.md)
-   [Virtual Memory Functions](virtual-memory-functions.md)
-   [Heap Functions](heap-functions.md)
-   [File Mapping](file-mapping.md)
-   [Large Memory Support](large-memory-support.md)
-   [Global and Local Functions](global-and-local-functions.md)
-   [Standard C Library Functions](standard-c-library-functions.md)
-   [Comparing Memory Allocation Methods](comparing-memory-allocation-methods.md)

 

 



