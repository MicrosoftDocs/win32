---
Description: The global and local functions are supported for porting from 16-bit code, or for maintaining source code compatibility with 16-bit Windows.
ms.assetid: 97707ce7-4c65-4d0e-ba69-47fdaee73a9b
title: Global and Local Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Global and Local Functions

The global and local functions are supported for porting from 16-bit code, or for maintaining source code compatibility with 16-bit Windows. Starting with 32-bit Windows, the global and local functions are implemented as wrapper functions that call the corresponding [heap functions](heap-functions.md) using a handle to the process's default heap. Therefore, the global and local functions have greater overhead than other memory management functions.

The [heap functions](heap-functions.md) provide more features and control than the global and local functions. New applications should use the heap functions unless documentation specifically states that a global or local function should be used. For example, some Windows functions allocate memory that must be freed with [**LocalFree**](/windows/win32/WinBase/nf-winbase-localfree?branch=master), and the global functions are still used with Dynamic Data Exchange (DDE), the clipboard functions, and OLE data objects. For a complete list of global and local functions, see the table in [Memory Management Functions](memory-management-functions.md).

Windows memory management does not provide a separate local heap and global heap, as 16-bit Windows does. As a result, the global and local families of functions are equivalent and choosing between them is a matter of personal preference. Note that the change from a 16-bit segmented memory model to a 32-bit virtual memory model has made some of the related global and local functions and their options unnecessary or meaningless. For example, there are no longer near and far pointers, because both local and global allocations return 32-bit virtual addresses.

Memory objects allocated by [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master) and [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master) are in private, committed pages with read/write access that cannot be accessed by other processes. Memory allocated by using **GlobalAlloc** with **GMEM\_DDESHARE** is not actually shared globally as it is in 16-bit Windows. This value has no effect and is available only for compatibility. Applications requiring shared memory for other purposes must use file-mapping objects. Multiple processes can map a view of the same file-mapping object to provide named shared memory. For more information, see [File Mapping](file-mapping.md).

Memory allocations are limited only by the available physical memory, including storage in the paging file on disk. When you allocate fixed memory, [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master) and [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master) return a pointer that the calling process can immediately use to access the memory. When you allocate moveable memory, the return value is a handle. To get a pointer to a movable memory object, use the [**GlobalLock**](/windows/win32/WinBase/nf-winbase-globallock?branch=master) and [**LocalLock**](/windows/win32/WinBase/nf-winbase-locallock?branch=master) functions.

The actual size of the memory allocated can be larger than the requested size. To determine the actual number of bytes allocated, use the [**GlobalSize**](/windows/win32/WinBase/nf-winbase-globalsize?branch=master) or [**LocalSize**](/windows/win32/WinBase/nf-winbase-localsize?branch=master) function. If the amount allocated is greater than the amount requested, the process can use the entire amount.

The [**GlobalReAlloc**](/windows/win32/WinBase/nf-winbase-globalrealloc?branch=master) and [**LocalReAlloc**](/windows/win32/WinBase/nf-winbase-localrealloc?branch=master) functions change the size or the attributes of a memory object allocated by [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master) and [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master). The size can increase or decrease.

The [**GlobalFree**](/windows/win32/WinBase/nf-winbase-globalfree?branch=master) and [**LocalFree**](/windows/win32/WinBase/nf-winbase-localfree?branch=master) functions release memory allocated by [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master), [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master), [**GlobalReAlloc**](/windows/win32/WinBase/nf-winbase-globalrealloc?branch=master), or [**LocalReAlloc**](/windows/win32/WinBase/nf-winbase-localrealloc?branch=master). To discard the specified memory object without invalidating the handle, use the [**GlobalDiscard**](/windows/win32/WinBase/nf-winbase-globaldiscard?branch=master) or [**LocalDiscard**](localdiscard.md) function. The handle can be used later by **GlobalReAlloc** or **LocalReAlloc** to allocate a new block of memory associated with the same handle.

To return information about a specified memory object, use the [**GlobalFlags**](/windows/win32/WinBase/nf-winbase-globalflags?branch=master) or [**LocalFlags**](/windows/win32/WinBase/nf-winbase-localflags?branch=master) function. The information includes the object's lock count and indicates whether the object is discardable or has already been discarded. To return a handle to the memory object associated with a specified pointer, use the [**GlobalHandle**](/windows/win32/WinBase/nf-winbase-globalhandle?branch=master) or [**LocalHandle**](/windows/win32/WinBase/nf-winbase-localhandle?branch=master) function.

## Related topics

<dl> <dt>

[Comparing Memory Allocation Methods](comparing-memory-allocation-methods.md)
</dt> </dl>

 

 



