---
title: Memory Allocation
description: Memory Allocation
ms.assetid: 33fdbe59-c1c9-4cac-becf-c5103fd6b955
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Memory Allocation

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Ownership of command trees may be transferred by means of several different methods in OLE DB. A transfer of ownership occurs when a component that allocates a command tree is no longer responsible for freeing the allocated resources. For example, command trees may be obtained by data consumers by means of the [**ICommandTree::GetCommandTree**](/windows/previous-versions/cmdtree/nf-cmdtree-icommandtree-getcommandtree?branch=master) method. In order for this transfer to succeed, a standard for allocation and de-allocation must be identified.

In general, the standard OLE task allocator interface ([**IMalloc**](_com_imalloc)), obtained by calling [**CoGetMalloc**](_com_cogetmalloc), should be used for allocating and releasing the memory. [**DBCOMMANDTREE**](dbcommandtree.md) nodes and the values embedded therein are allocated using [**IMalloc::Alloc**](_com_imalloc_alloc) and released by means of [**IMalloc::Free**](_com_imalloc_free), with the following exceptions:

-   **BSTR** functions: [**SysAllocString**](_oa96_sysallocstring), [**SysFreeString**](_oa96_sysfreestring) family of functions
-   **OLE** interfaces: [**IUnknown::AddRef**](_com_iunknown_addref), [**IUnknown::Release**](_com_iunknown_release)
-   SafeArrays: [**SafeArrayAllocData**](_oa96_safearrayallocdata), [**SafeArrayDestroy**](_oa96_safearraydestroy) family of functions.

All other pointers embedded in a command tree are assumed to have been dynamically allocated with [**IMalloc::Alloc**](_com_imalloc_alloc) and will be released with [**IMalloc::Free**](_com_imalloc_free).

When allocating a tree that will not change ownership, you can use any method of allocation except in the three cases above, because those values also have special copy functions.

 

 




