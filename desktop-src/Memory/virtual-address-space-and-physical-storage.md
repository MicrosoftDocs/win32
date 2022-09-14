---
description: The maximum amount of physical memory supported by Microsoft Windows ranges from 2 GB to 2 TB, depending on the version of Windows.
ms.assetid: 5e8fca7a-b85f-4bbd-80c1-e580a815fdce
title: Virtual Address Space and Physical Storage
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Address Space and Physical Storage

The maximum amount of physical memory supported by Microsoft Windows ranges from 2 GB to 24 TB, depending on the version of Windows. For more information, see [Memory Limits for Windows Releases](memory-limits-for-windows-releases.md). The virtual address space of each process can be smaller or larger than the total physical memory available on the computer. The subset of the virtual address space of a process that resides in physical memory is known as the *working set*. If the threads of a process attempt to use more physical memory than is currently available, the system pages some of the memory contents to disk. The total amount of virtual address space available to a process is limited by physical memory and the free space on disk available for the paging file.

Physical storage and the virtual address space of each process are organized into *pages*, units of memory, whose size depends on the host computer. For example, on x86 computers the host page size is 4 kilobytes.

To maximize its flexibility in managing memory, the system can move pages of physical memory to and from a paging file on disk. When a page is moved in physical memory, the system updates the page maps of the affected processes. When the system needs space in physical memory, it moves the least recently used pages of physical memory to the paging file. Manipulation of physical memory by the system is completely transparent to applications, which operate only in their virtual address spaces.

 

 



