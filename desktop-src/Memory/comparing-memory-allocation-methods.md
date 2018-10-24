---
Description: The following is a brief comparison of the various memory allocation methods.
ms.assetid: b6101014-02d2-4b19-aec6-8772a2793d38
title: Comparing Memory Allocation Methods
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Comparing Memory Allocation Methods

The following is a brief comparison of the various memory allocation methods:

-   [**CoTaskMemAlloc**](https://msdn.microsoft.com/en-us/library/ms692727(v=VS.85).aspx)
-   [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc)
-   [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc)
-   [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc)
-   **malloc**
-   **new**
-   [**VirtualAlloc**](https://msdn.microsoft.com/en-us/library/Aa366887(v=VS.85).aspx)

Although the [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc), [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc), and [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) functions ultimately allocate memory from the same heap, each provides a slightly different set of functionality. For example, **HeapAlloc** can be instructed to raise an exception if memory could not be allocated, a capability not available with **LocalAlloc**. **LocalAlloc** supports allocation of handles which permit the underlying memory to be moved by a reallocation without changing the handle value, a capability not available with **HeapAlloc**.

Starting with 32-bit Windows, [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc) and [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc) are implemented as wrapper functions that call [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) using a handle to the process's default heap. Therefore, **GlobalAlloc** and **LocalAlloc** have greater overhead than **HeapAlloc**.

Because the different heap allocators provide distinctive functionality by using different mechanisms, you must free memory with the correct function. For example, memory allocated with [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) must be freed with [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree) and not [**LocalFree**](/windows/desktop/api/WinBase/nf-winbase-localfree) or [**GlobalFree**](/windows/desktop/api/WinBase/nf-winbase-globalfree). Memory allocated with [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc) or [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc) must be queried, validated, and released with the corresponding global or local function.

The [**VirtualAlloc**](https://msdn.microsoft.com/en-us/library/Aa366887(v=VS.85).aspx) function allows you to specify additional options for memory allocation. However, its allocations use a page granularity, so using **VirtualAlloc** can result in higher memory usage.

The **malloc** function has the disadvantage of being run-time dependent. The **new** operator has the disadvantage of being compiler dependent and language dependent.

The [**CoTaskMemAlloc**](https://msdn.microsoft.com/en-us/library/ms692727(v=VS.85).aspx) function has the advantage of working well in either C, C++, or Visual Basic. It is also the only way to share memory in a COM-based application, since MIDL uses **CoTaskMemAlloc** and [**CoTaskMemFree**](https://msdn.microsoft.com/en-us/library/ms680722(v=VS.85).aspx) to marshal memory.

## Related topics

<dl> <dt>

[Global and Local Functions](global-and-local-functions.md)
</dt> <dt>

[Heap Functions](heap-functions.md)
</dt> <dt>

[Virtual Memory Functions](virtual-memory-functions.md)
</dt> </dl>

 

 



