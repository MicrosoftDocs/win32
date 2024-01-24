---
description: To determine the size of a page on the current computer, use the GetSystemInfo function.
ms.assetid: 953ddfc4-6126-41fb-81a3-0ce1f0fb223f
title: Working with Pages
ms.topic: article
ms.date: 05/31/2018
---

# Working with Pages

To determine the size of a page on the current computer, use the [**GetSystemInfo**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsysteminfo) function.

The [**VirtualQuery**](/windows/win32/api/memoryapi/nf-memoryapi-virtualquery) and [**VirtualQueryEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualqueryex) functions return information about a region of consecutive pages beginning at a specified address in the address space of a process. **VirtualQuery** returns information about memory in the calling process. **VirtualQueryEx** returns information about memory in a specified process and is used to support debuggers that need information about a process being debugged. The region of pages is bounded by the specified address rounded down to the nearest page boundary. It extends through all subsequent pages with the following attributes in common:

-   The state of all pages is the same: either committed, reserved, or free.
-   If the initial page is not free, all pages in the region are part of the same initial allocation of pages that were reserved by a call to [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc).
-   The access protection of all pages is the same (that is, **PAGE\_READONLY**, **PAGE\_READWRITE**, or **PAGE\_NOACCESS**).

The [**VirtualLock**](/windows/win32/api/memoryapi/nf-memoryapi-virtuallock) function enables a process to lock one or more pages of committed memory into physical memory (RAM), preventing the system from swapping the pages out to the paging file. It can be used to ensure that critical data is accessible without disk access. Locking pages into memory is dangerous because it restricts the system's ability to manage memory. Excessive use of **VirtualLock** can degrade system performance by causing executable code to be swapped out to the paging file. The [**VirtualUnlock**](/windows/win32/api/memoryapi/nf-memoryapi-virtualunlock) function unlocks memory locked by **VirtualLock**.

The [**VirtualProtect**](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect) function enables a process to modify the access protection of any committed page in the address space of a process. For example, a process can allocate read/write pages to store sensitive data, and then it can change the access to read only or no access to protect against accidental overwriting. **VirtualProtect** is typically used with pages allocated by [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc), but it also works with pages committed by any of the other allocation functions. However, **VirtualProtect** changes the protection of entire pages, and pointers returned by the other functions are not necessarily aligned on page boundaries. The [**VirtualProtectEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotectex) function is similar to **VirtualProtect**, except it changes the protection of memory in a specified process. Changing the protection is useful to debuggers in accessing the memory of a process being debugged.

 

 
