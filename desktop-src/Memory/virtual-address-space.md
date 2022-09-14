---
description: The virtual address space for a process is the set of virtual memory addresses that it can use. The address space for each process is private and cannot be accessed by other processes unless it is shared.
ms.assetid: 747f9f53-a595-4f4b-8b81-3123d59edb2f
title: Virtual Address Space (Memory Management)
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Address Space (Memory Management)

The virtual address space for a process is the set of virtual memory addresses that it can use. The address space for each process is private and cannot be accessed by other processes unless it is shared.

A virtual address does not represent the actual physical location of an object in memory; instead, the system maintains a *page table* for each process, which is an internal data structure used to translate virtual addresses into their corresponding physical addresses. Each time a thread references an address, the system translates the virtual address to a physical address.

The virtual address space for 32-bit Windows is 4 gigabytes (GB) in size and divided into two partitions: one for use by the process and the other reserved for use by the system. For more information about the virtual address space in 64-bit Windows, see [Virtual Address Space in 64-bit Windows](../winprog64/virtual-address-space.md).

For more information about virtual memory, see the following topics:

-   [Virtual Address Space and Physical Storage](virtual-address-space-and-physical-storage.md)
-   [Working Set](working-set.md)
-   [Page State](page-state.md)
-   [Scope of Allocated Memory](scope-of-allocated-memory.md)
-   [Data Execution Prevention](data-execution-prevention.md)
-   [Memory Protection](memory-protection.md)
-   [Memory Limits for Windows Releases](memory-limits-for-windows-releases.md)

## Default Virtual Address Space for 32-bit Windows

The following table shows the default memory range for each partition.



| Memory range                             | Usage                |
|------------------------------------------|----------------------|
| Low 2GB (0x00000000 through 0x7FFFFFFF)  | Used by the process. |
| High 2GB (0x80000000 through 0xFFFFFFFF) | Used by the system.  |



 

## Virtual Address Space for 32-bit Windows with 4GT

If [4-gigabyte tuning](4-gigabyte-tuning.md) (4GT) is enabled, the memory range for each partition is as follows.



| Memory range                             | Usage                |
|------------------------------------------|----------------------|
| Low 3GB (0x00000000 through 0xBFFFFFFF)  | Used by the process. |
| High 1GB (0xC0000000 through 0xFFFFFFFF) | Used by the system.  |



 

After 4GT is enabled, a process that has the [**IMAGE\_FILE\_LARGE\_ADDRESS\_AWARE**](/windows/win32/api/dbghelp/ns-dbghelp-loaded_image) flag set in its image header will have access to the additional 1 GB of memory above the low 2 GB.

## Adjusting the Virtual Address Space for 32-bit Windows

You can use the following command to set a boot entry option that configures the size of the partition that is available for use by the process to a value between 2048 (2 GB) and 3072 (3 GB):

[BCDEdit /set](/windows-hardware/drivers/devtest/bcdedit--set) **increaseuserva** *Megabytes*

After the boot entry option is set, the memory range for each partition is as follows.



| Memory range                            | Usage                |
|-----------------------------------------|----------------------|
| Low (0x00000000 through *Megabytes*)    | Used by the process. |
| High (*Megabytes*+1 through 0xFFFFFFFF) | Used by the system.  |



 

**Windows Server 2003:** Set the **/USERVA** switch in boot.ini to a value between 2048 and 3072.

 

 
