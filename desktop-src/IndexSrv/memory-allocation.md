---
title: Memory Allocation
description: Memory Allocation
ms.assetid: 33fdbe59-c1c9-4cac-becf-c5103fd6b955
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Memory Allocation

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Ownership of command trees may be transferred by means of several different methods in OLE DB. A transfer of ownership occurs when a component that allocates a command tree is no longer responsible for freeing the allocated resources. For example, command trees may be obtained by data consumers by means of the [**ICommandTree::GetCommandTree**](/previous-versions/windows/desktop/api/cmdtree/nf-cmdtree-icommandtree-getcommandtree) method. In order for this transfer to succeed, a standard for allocation and de-allocation must be identified.

In general, the standard OLE task allocator interface ([**IMalloc**](https://www.bing.com/search?q=**IMalloc**)), obtained by calling [**CoGetMalloc**](https://www.bing.com/search?q=**CoGetMalloc**), should be used for allocating and releasing the memory. [**DBCOMMANDTREE**](dbcommandtree.md) nodes and the values embedded therein are allocated using [**IMalloc::Alloc**](https://www.bing.com/search?q=**IMalloc::Alloc**) and released by means of [**IMalloc::Free**](https://www.bing.com/search?q=**IMalloc::Free**), with the following exceptions:

-   **BSTR** functions: [**SysAllocString**](https://www.bing.com/search?q=**SysAllocString**), [**SysFreeString**](https://www.bing.com/search?q=**SysFreeString**) family of functions
-   **OLE** interfaces: [**IUnknown::AddRef**](https://www.bing.com/search?q=**IUnknown::AddRef**), [**IUnknown::Release**](https://www.bing.com/search?q=**IUnknown::Release**)
-   SafeArrays: [**SafeArrayAllocData**](https://www.bing.com/search?q=**SafeArrayAllocData**), [**SafeArrayDestroy**](https://www.bing.com/search?q=**SafeArrayDestroy**) family of functions.

All other pointers embedded in a command tree are assumed to have been dynamically allocated with [**IMalloc::Alloc**](https://www.bing.com/search?q=**IMalloc::Alloc**) and will be released with [**IMalloc::Free**](https://www.bing.com/search?q=**IMalloc::Free**).

When allocating a tree that will not change ownership, you can use any method of allocation except in the three cases above, because those values also have special copy functions.

 

 




