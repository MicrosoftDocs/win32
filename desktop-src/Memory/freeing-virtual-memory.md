---
description: The VirtualFree function decommits and releases pages according to the following rules.
ms.assetid: 8fbd7960-f3f0-4326-ad1d-12b636c0039e
title: Freeing Virtual Memory
ms.topic: article
ms.date: 05/31/2018
---

# Freeing Virtual Memory

The [**VirtualFree**](/windows/win32/api/memoryapi/nf-memoryapi-virtualfree) function decommits and releases pages according to the following rules:

-   Decommits one or more committed pages, changing the state of the pages to reserved. Decommitting pages releases the physical storage associated with the pages, making it available to be allocated by any process. Any block of committed pages can be decommitted.
-   Releases a block of one or more reserved pages, changing the state of the pages to free. Releasing a block of pages makes the range of reserved addresses available to be allocated by the process. Reserved pages can be released only by freeing the entire block that was initially reserved by [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc).
-   Decommits and releases a block of one or more committed pages simultaneously, changing the state of the pages to free. The specified block must include the entire block initially reserved by [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc), and all of the pages must be currently committed.

After a memory block is released or decommitted, you can never refer to it again. Any information that may have been in that memory is gone forever. Attempting to read from or write to a free page results in an access violation exception. If you require information, do not decommit or free memory containing that information.

To specify that the data in a memory range is no longer of interest, call [**VirtualAlloc**](/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc) with **MEM\_RESET**. The pages will not be read from or written to the paging file. However, the memory block can be used again later.

 

 
