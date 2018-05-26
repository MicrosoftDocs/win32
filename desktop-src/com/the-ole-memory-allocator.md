---
title: The OLE Memory Allocator
description: The OLE Memory Allocator
ms.assetid: 026c62e5-c296-4059-b028-77c98fdb77ce
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The OLE Memory Allocator

The COM library provides an implementation of a memory allocator that is thread-safe. (That is, it cannot cause problems in multithreaded situations.) Whenever ownership of an allocated chunk of memory is passed through a COM interface or between a client and the COM library, you must use this COM allocator to allocate the memory. Allocation internal to an object can use any allocation scheme desired, but the COM memory allocator is a handy, efficient, and thread-safe allocator.

A call to the API function [**CoGetMalloc**](/windows/win32/combaseapi/nf-combaseapi-cogetmalloc?branch=master) provides a pointer to the OLE allocator, which is an implementation of the [**IMalloc**](/windows/win32/objidlbase/nn-objidl-imalloc?branch=master) interface. However, it is more efficient to call the helper functions [**CoTaskMemAlloc**](/windows/win32/combaseapi/nf-combaseapi-cotaskmemalloc?branch=master), [**CoTaskMemRealloc**](/windows/win32/combaseapi/nf-combaseapi-cotaskmemrealloc?branch=master), and [**CoTaskMemFree**](/windows/win32/combaseapi/nf-combaseapi-cotaskmemfree?branch=master), which wrap getting a pointer to the task memory allocator, calling the corresponding **IMalloc** method, and then releasing the pointer to the allocator.

## Related topics

<dl> <dt>

[Managing Memory Allocation](managing-memory-allocation.md)
</dt> <dt>

[The COM Library](the-com-library.md)
</dt> </dl>

 

 




