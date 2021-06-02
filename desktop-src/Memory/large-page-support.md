---
description: Large-page support enables server applications to establish large-page memory regions, which is particularly useful on 64-bit Windows.
ms.assetid: 060115af-38d1-499c-b30c-47cd0cf42d20
title: Large-Page Support
ms.topic: article
ms.date: 05/31/2018
---

# Large-Page Support

Large-page support enables server applications to establish large-page memory regions, which is particularly useful on 64-bit Windows. Each large-page translation uses a single translation buffer inside the CPU. The size of this buffer is typically three orders of magnitude larger than the native page size; this increases the efficiency of the translation buffer, which can increase performance for frequently accessed memory.

The following procedure describes how to use large-page support.

**To use large-page support**

1.  Obtain the **SeLockMemoryPrivilege** privilege by calling the [**AdjustTokenPrivileges**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) function. For more information, see [Assigning Privileges to an Account](../secbp/assigning-privileges-to-an-account.md) and [Changing Privileges in a Token](../secbp/changing-privileges-in-a-token.md).
2.  Retrieve the minimum large-page size by calling the [**GetLargePageMinimum**](/windows/win32/api/memoryapi/nf-memoryapi-getlargepageminimum) function.
3.  Include the **MEM\_LARGE\_PAGES** value when calling the [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) function. The size and alignment must be a multiple of the large-page minimum.

When writing applications that use large-page memory, keep the following considerations in mind:

-   Large-page memory regions may be difficult to obtain after the system has been running for a long time because the physical space for each large page must be contiguous, but the memory may have become fragmented. Allocating large pages under these conditions can significantly affect system performance. Therefore, applications should avoid making repeated large-page allocations and instead allocate all large pages one time, at startup.
-   The memory is always read/write and nonpageable (always resident in physical memory).
-   The memory is part of the process private bytes but not part of the working set, because the working set by definition contains only pageable memory.
-   Large-page allocations are not subject to job limits.
-   Large-page memory must be reserved and committed as a single operation. In other words, large pages cannot be used to commit a previously reserved range of memory.
-   WOW64 on Intel Itanium-based systems does not support 32-bit applications that use this feature. The applications should be recompiled as native 64-bit applications.

 

 
