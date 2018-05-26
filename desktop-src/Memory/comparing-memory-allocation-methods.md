---
Description: The following is a brief comparison of the various memory allocation methods.
ms.assetid: b6101014-02d2-4b19-aec6-8772a2793d38
title: Comparing Memory Allocation Methods
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Comparing Memory Allocation Methods

The following is a brief comparison of the various memory allocation methods:

-   [**CoTaskMemAlloc**](_com_cotaskmemalloc)
-   [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master)
-   [**HeapAlloc**](/windows/win32/HeapApi/nf-heapapi-heapalloc?branch=master)
-   [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master)
-   **malloc**
-   **new**
-   [**VirtualAlloc**](virtualalloc.md)

Although the [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master), [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master), and [**HeapAlloc**](/windows/win32/HeapApi/nf-heapapi-heapalloc?branch=master) functions ultimately allocate memory from the same heap, each provides a slightly different set of functionality. For example, **HeapAlloc** can be instructed to raise an exception if memory could not be allocated, a capability not available with **LocalAlloc**. **LocalAlloc** supports allocation of handles which permit the underlying memory to be moved by a reallocation without changing the handle value, a capability not available with **HeapAlloc**.

Starting with 32-bit Windows, [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master) and [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master) are implemented as wrapper functions that call [**HeapAlloc**](/windows/win32/HeapApi/nf-heapapi-heapalloc?branch=master) using a handle to the process's default heap. Therefore, **GlobalAlloc** and **LocalAlloc** have greater overhead than **HeapAlloc**.

Because the different heap allocators provide distinctive functionality by using different mechanisms, you must free memory with the correct function. For example, memory allocated with [**HeapAlloc**](/windows/win32/HeapApi/nf-heapapi-heapalloc?branch=master) must be freed with [**HeapFree**](/windows/win32/HeapApi/nf-heapapi-heapfree?branch=master) and not [**LocalFree**](/windows/win32/WinBase/nf-winbase-localfree?branch=master) or [**GlobalFree**](/windows/win32/WinBase/nf-winbase-globalfree?branch=master). Memory allocated with [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master) or [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master) must be queried, validated, and released with the corresponding global or local function.

The [**VirtualAlloc**](virtualalloc.md) function allows you to specify additional options for memory allocation. However, its allocations use a page granularity, so using **VirtualAlloc** can result in higher memory usage.

The **malloc** function has the disadvantage of being run-time dependent. The **new** operator has the disadvantage of being compiler dependent and language dependent.

The [**CoTaskMemAlloc**](_com_cotaskmemalloc) function has the advantage of working well in either C, C++, or Visual Basic. It is also the only way to share memory in a COM-based application, since MIDL uses **CoTaskMemAlloc** and [**CoTaskMemFree**](_com_cotaskmemfree) to marshal memory.

## Related topics

<dl> <dt>

[Global and Local Functions](global-and-local-functions.md)
</dt> <dt>

[Heap Functions](heap-functions.md)
</dt> <dt>

[Virtual Memory Functions](virtual-memory-functions.md)
</dt> </dl>

 

 



