---
description: 'The memory manager creates the following memory pools that the system uses to allocate memory: nonpaged pool and paged pool.'
ms.assetid: 68ee9c72-f3a3-4f1f-a827-ed4210a665e4
title: Memory Pools
ms.topic: article
ms.date: 05/31/2018
---

# Memory Pools

The memory manager creates the following memory pools that the system uses to allocate memory: nonpaged pool and paged pool. Both memory pools are located in the region of the address space that is reserved for the system and mapped into the virtual address space of each process. The nonpaged pool consists of virtual memory addresses that are guaranteed to reside in physical memory as long as the corresponding kernel objects are allocated. The paged pool consists of virtual memory that can be paged in and out of the system. To improve performance, systems with a single processor have three paged pools, and multiprocessor systems have five paged pools.

The handles for [kernel objects](../sysinfo/kernel-objects.md) are stored in the paged pool, so the number of handles you can create is based on available memory.

The system records the limits and current values for its nonpaged pool, paged pool, and page file usage. For more information, see [Memory Performance Information](memory-performance-information.md).

 

 
