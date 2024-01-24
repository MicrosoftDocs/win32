---
description: Each process has a default heap provided by the system. Applications that make frequent allocations from the heap can improve performance by using private heaps.
ms.assetid: cfb683fa-4f46-48b5-9a28-f4625a9cb8cd
title: Heap Functions
ms.topic: article
ms.date: 05/31/2018
---

# Heap Functions

Each process has a default heap provided by the system. Applications that make frequent allocations from the heap can improve performance by using private heaps.

A private heap is a block of one or more pages in the address space of the calling process. After creating the private heap, the process uses functions such as [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) and [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree) to manage the memory in that heap.

The heap functions can also be used to manage memory in the process's default heap, using the handle returned by the [**GetProcessHeap**](/windows/desktop/api/HeapApi/nf-heapapi-getprocessheap) function. New applications should use the heap functions instead of the [global and local functions](global-and-local-functions.md) for this purpose.

There is no difference between memory allocated from a private heap and that allocated by using the other memory allocation functions. For a complete list of functions, see the table in [Memory Management Functions](memory-management-functions.md).

> [!Note]  
> A thread should call heap functions only for the process's default heap and private heaps that the thread creates and manages, using handles returned by the [**GetProcessHeap**](/windows/desktop/api/HeapApi/nf-heapapi-getprocessheap) or [**HeapCreate**](/windows/desktop/api/HeapApi/nf-heapapi-heapcreate) function.

 

The [**HeapCreate**](/windows/desktop/api/HeapApi/nf-heapapi-heapcreate) function creates a private heap object from which the calling process can allocate memory blocks by using the [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) function. **HeapCreate** specifies both an initial size and a maximum size for the heap. The initial size determines the number of committed, read/write pages initially allocated for the heap. The maximum size determines the total number of reserved pages. These pages create a contiguous block in the virtual address space of a process into which the heap can grow. Additional pages are automatically committed from this reserved space if requests by **HeapAlloc** exceed the current size of committed pages, assuming that the physical storage for it is available. Once the pages are committed, they are not decommitted until the process is terminated or until the heap is destroyed by calling the [**HeapDestroy**](/windows/desktop/api/HeapApi/nf-heapapi-heapdestroy) function.

The memory of a private heap object is accessible only to the process that created it. If a dynamic-link library (DLL) creates a private heap, it does so in the address space of the process that called the DLL. It is accessible only to that process.

The [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) function allocates a specified number of bytes from a private heap and returns a pointer to the allocated block. This pointer can be used in the [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree), [**HeapReAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heaprealloc), [**HeapSize**](/windows/desktop/api/HeapApi/nf-heapapi-heapsize), and [**HeapValidate**](/windows/desktop/api/HeapApi/nf-heapapi-heapvalidate) functions.

Memory allocated by [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) is not movable. The address returned by **HeapAlloc** is valid until the memory block is freed or reallocated; the memory block does not need to be locked.

Because the system cannot compact a private heap, it can become fragmented. Applications that allocate large amounts of memory in various allocation sizes can use the [low-fragmentation heap](low-fragmentation-heap.md) to reduce heap fragmentation.

A possible use for the heap functions is to create a private heap when a process starts up, specifying an initial size sufficient to satisfy the memory requirements of the process. If the call to the [**HeapCreate**](/windows/desktop/api/HeapApi/nf-heapapi-heapcreate) function fails, the process can terminate or notify the user of the memory shortage; if it succeeds, however, the process is assured of having the memory it needs.

Memory requested by [**HeapCreate**](/windows/desktop/api/HeapApi/nf-heapapi-heapcreate) may or may not be contiguous. Memory allocated within a heap by [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) is contiguous. You should not write to or read from memory in a heap except that allocated by **HeapAlloc**, nor should you assume any relationship between two areas of memory allocated by **HeapAlloc**.

You should not refer in any way to memory that has been freed by [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree). After the memory is freed, any information that may have been in it is gone forever. If you require information, do not free memory containing the information. Function calls that return information about memory (such as [**HeapSize**](/windows/desktop/api/HeapApi/nf-heapapi-heapsize)) may not be used with freed memory, as they may return bogus data.

The [**HeapDestroy**](/windows/desktop/api/HeapApi/nf-heapapi-heapdestroy) function destroys a private heap object. It decommits and releases all the pages of the heap object, and it invalidates the handle to the heap.

## Related topics

<dl> <dt>

[Comparing Memory Allocation Methods](comparing-memory-allocation-methods.md)
</dt> </dl>

 

 



