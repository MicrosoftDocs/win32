---
description: Address Windowing Extensions (AWE) is a set of extensions that allows an application to quickly manipulate physical memory greater than 4GB.
ms.assetid: 48a29922-8130-4540-86b0-0faa120566a6
title: Address Windowing Extensions
ms.topic: article
ms.date: 05/31/2018
---

# Address Windowing Extensions

Address Windowing Extensions (AWE) is a set of extensions that allows an application to quickly manipulate physical memory greater than 4GB. Certain data-intensive applications, such as database management systems and scientific and engineering software, need access to very large caches of data. In the case of very large data sets, restricting the cache to fit within an application's 2GB of user address space is a severe restriction. In these situations, the cache is too small to properly support the application.

AWE solves this problem by allowing applications to directly address huge amounts of memory while continuing to use 32-bit pointers. AWE allows applications to have data caches larger than 4GB (where sufficient physical memory is present). AWE uses physical nonpaged memory and window views of various portions of this physical memory within a 32-bit virtual address space.

AWE places a few restrictions on how this memory may be used, primarily because these restrictions allow extremely fast mapping, remapping, and freeing. Fast memory management is important for these potentially enormous address spaces.

-   Virtual address ranges allocated for the AWE are not sharable with other processes (and therefore not inheritable). In fact, two different AWE virtual addresses within the same process are not allowed to map the same physical page. These restrictions provide fast remapping and cleanup when memory is freed.
-   The physical pages that can be allocated for an AWE region are limited by the number of physical pages present in the machine, since this memory is never paged – it is locked down until the application explicitly frees it or exits. The physical pages allocated for a given process can be mapped into any AWE virtual region within the same process. Applications that use AWE must be careful not to take so much physical memory that they cause other applications to page excessively or prevent creation of new processes or threads due to lack of resources. Use the [**GlobalMemoryStatusEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex) function to monitor physical memory use.
-   AWE virtual addresses are always read/write and cannot be protected via calls to [**VirtualProtect**](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect) (that is, no read-only memory, noaccess memory, guard pages, and the like can be specified).
-   AWE address ranges cannot be used to buffer data for graphics or video calls.
-   An AWE memory range cannot be split, nor can pieces of it be deleted. Instead, the entire virtual address range must be deleted as a unit when deletion is required. This means you must specify **MEM\_RELEASE** when calling [**VirtualFree**](/windows/win32/api/memoryapi/nf-memoryapi-virtualfree).
-   Applications can map multiple regions simultaneously, provided they do not overlap.
-   Applications that use AWE are not supported in emulation mode. That is, an x86 application that uses AWE functions must be recompiled to run on another processor, whereas most applications can run without recompiling under an emulator on other platforms.

This solution addresses the physical memory issues in a very general, widely applicable manner. Some of the benefits of AWE are:

-   A small group of new functions is defined to manipulate AWE memory.
-   AWE provides a very fast remapping capability. Remapping is done by manipulating virtual memory tables, not by moving data in physical memory.
-   AWE provides page size granularity appropriate to the processor (for example, 4 KB on x86), which is more useful to applications than large pages (for example, 2MB or 4MB on x86).

An application must have the Lock Pages in Memory privilege to use AWE. To obtain this privilege, an administrator must add **Lock Pages in Memory** to the user's **User Rights Assignments**. For more information on how to do this, see "User Rights" in the operating system help.

The following functions make up the Address Windowing Extensions (AWE) API.



| Function                                                                          | Description                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) and [**VirtualAllocEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex) | Reserve a portion of virtual address space to use for AWE, using **MEM\_PHYSICAL**.                                                                                                                                                                       |
| [**AllocateUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-allocateuserphysicalpages)                    | Allocate physical memory for use with AWE.                                                                                                                                                                                                                |
| [**MapUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-mapuserphysicalpages)                              | Map (or invalidate) AWE virtual addresses onto any set of physical pages obtained with [**AllocateUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-allocateuserphysicalpages).                                                                                                    |
| [**MapUserPhysicalPagesScatter**](/windows/desktop/api/WinBase/nf-winbase-mapuserphysicalpagesscatter)                | Map (or invalidate) AWE virtual addresses onto any set of physical pages obtained with [**AllocateUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-allocateuserphysicalpages), but with finer control than that provided by [**MapUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-mapuserphysicalpages). |
| [**FreeUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-freeuserphysicalpages)                            | Free physical memory that was used for AWE.                                                                                                                                                                                                               |



 

 

 
