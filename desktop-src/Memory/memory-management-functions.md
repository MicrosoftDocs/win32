---
Description: This topic describes the memory management functions
ms.assetid: 5a2a7a62-0bda-4a0d-93d2-25b4898871fd
title: Memory Management Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Memory Management Functions

This topic describes the memory management functions:

-   [General Memory Functions](#general-memory-functions)
-   [Data Execution Prevention Functions](#data-execution-prevention-functions)
-   [File Mapping Functions](#file-mapping-functions)
-   [AWE Functions](#awe-functions)
-   [Heap Functions](#heap-functions)
-   [Virtual Memory Functions](#virtual-memory-functions)
-   [Global and Local Functions](#global-and-local-functions)
-   [Bad Memory Functions](#bad-memory-functions)
-   [Enclave Functions](#enclave-functions)
-   [Obsolete Functions](#obsolete-functions)

## General Memory Functions

The following functions are used in memory management.



| Function                                                                         | Description                                                                                                                                            |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddSecureMemoryCacheCallback**](/windows/win32/WinBase/nf-winbase-addsecurememorycachecallback?branch=master)             | Registers a callback function to be called when a secured memory range is freed or its protections are changed.                                        |
| [**CopyMemory**](/windows/win32/WinBase/?branch=master)                                                 | Copies a block of memory from one location to another.                                                                                                 |
| [**CreateMemoryResourceNotification**](creatememoryresourcenotification.md)     | Creates a memory resource notification object.                                                                                                         |
| [**FillMemory**](fillmemory.md)                                                 | Fills a block of memory with a specified value.                                                                                                        |
| [**GetLargePageMinimum**](getlargepageminimum.md)                               | Retrieves the minimum size of a large page.                                                                                                            |
| [**GetPhysicallyInstalledSystemMemory**](/windows/win32/WinBase/?branch=master) | Retrieves the amount of RAM that is physically installed on the computer.                                                                              |
| [**GetSystemFileCacheSize**](getsystemfilecachesize.md)                         | Retrieves the current size limits for the working set of the system cache.                                                                             |
| [**GetWriteWatch**](getwritewatch.md)                                           | Retrieves the addresses of the pages that have been written to in a region of virtual memory.                                                          |
| [**GlobalMemoryStatusEx**](/windows/win32/WinBase/?branch=master)                             | Obtains information about the system's current usage of both physical and virtual memory.                                                              |
| [**MoveMemory**](/windows/win32/WinBase/nf-srbhelper-srbmovememory?branch=master)                                                 | Moves a block of memory from one location to another.                                                                                                  |
| [**QueryMemoryResourceNotification**](querymemoryresourcenotification.md)       | Retrieves the state of the specified memory resource object.                                                                                           |
| [**RemoveSecureMemoryCacheCallback**](/windows/win32/WinBase/nf-winbase-removesecurememorycachecallback?branch=master)       | Unregisters a callback function that was previously registered with the [**AddSecureMemoryCacheCallback**](/windows/win32/WinBase/nf-winbase-addsecurememorycachecallback?branch=master) function. |
| [**ResetWriteWatch**](resetwritewatch.md)                                       | Resets the write-tracking state for a region of virtual memory.                                                                                        |
| [**SecureMemoryCacheCallback**](/windows/win32/WinNT/nc-winnt-psecure_memory_cache_callback?branch=master)                   | An application-defined function that is called when a secured memory range is freed or its protections are changed.                                    |
| [**SecureZeroMemory**](/windows/win32/WinBase/?branch=master)                                     | Fills a block of memory with zeros.                                                                                                                    |
| [**SetSystemFileCacheSize**](setsystemfilecachesize.md)                         | Limits the size of the working set for the file system cache.                                                                                          |
| [**ZeroMemory**](/windows/win32/WinBase/nf-minitape-rtlzeromemory?branch=master)                                                 | Fills a block of memory with zeros.                                                                                                                    |



 

## Data Execution Prevention Functions

The following functions are used with [Data Execution Prevention](data-execution-prevention.md) (DEP).



| Function                                           | Description                            |
|----------------------------------------------------|----------------------------------------|
| [**GetProcessDEPPolicy**](/windows/win32/WinBase/nf-winbase-getprocessdeppolicy?branch=master) | Retrieves DEP settings for a process.  |
| [**GetSystemDEPPolicy**](/windows/win32/WinBase/nf-winbase-getsystemdeppolicy?branch=master)   | Retrieves DEP settings for the system. |
| [**SetProcessDEPPolicy**](/windows/win32/WinBase/nf-winbase-setprocessdeppolicy?branch=master) | Changes DEP settings for a process.    |



 

## File Mapping Functions

The following functions are used in [file mapping](file-mapping.md).



| Function                                                     | Description                                                                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateFileMapping**](/windows/win32/WinBase/nf-winbase-createfilemappinga?branch=master)               | Creates or opens a named or unnamed file mapping object for a specified file.                                                                                                      |
| [**CreateFileMappingFromApp**](/windows/win32/MemoryApi/nf-memoryapi-createfilemappingfromapp?branch=master) | Creates or opens a named or unnamed file mapping object for a specified file from a Windows Store app.                                                                             |
| [**CreateFileMappingNuma**](/windows/win32/WinBase/nf-winbase-createfilemappingnumaa?branch=master)       | Creates or opens a named or unnamed file mapping object for a specified file, and specifies the NUMA node for the physical memory.                                                 |
| [**FlushViewOfFile**](flushviewoffile.md)                   | Writes to the disk a byte range within a mapped view of a file.                                                                                                                    |
| [**GetMappedFileName**](base.getmappedfilename)              | Checks whether the specified address is within a memory-mapped file in the address space of the specified process. If so, the function returns the name of the memory-mapped file. |
| [**MapViewOfFile**](mapviewoffile.md)                       | Maps a view of a file mapping into the address space of a calling process.                                                                                                         |
| [**MapViewOfFile2**](mapviewoffile2.md)                     | Maps a view of a file or a pagefile-backed section into the address space of the specified process.                                                                                |
| [**MapViewOfFileEx**](mapviewoffileex.md)                   | Maps a view of a file mapping into the address space of a calling process. A caller can optionally specify a suggested memory address for the view.                                |
| [**MapViewOfFileExNuma**](/windows/win32/WinBase/nf-winbase-mapviewoffileexnuma?branch=master)           | Maps a view of a file mapping into the address space of a calling process, and specifies the NUMA node for the physical memory.                                                    |
| [**MapViewOfFileFromApp**](/windows/win32/MemoryApi/nf-memoryapi-mapviewoffilefromapp?branch=master)         | Maps a view of a file mapping into the address space of a calling process from a Windows Store app.                                                                                |
| [**MapViewOfFileNuma2**](mapviewoffilenuma2.md)             | Maps a view of a file or a pagefile-backed section into the address space of the specified process.                                                                                |
| [**OpenFileMapping**](/windows/win32/WinBase/nf-winbase-openfilemappinga?branch=master)                   | Opens a named file mapping object.                                                                                                                                                 |
| [**UnmapViewOfFile**](unmapviewoffile.md)                   | Unmaps a mapped view of a file from the calling process's address space.                                                                                                           |
| [**UnmapViewOfFile2**](unmapviewoffile2.md)                 | Unmaps a previously mapped view of a file or a pagefile-backed section.                                                                                                            |



 

## AWE Functions

The following are the [AWE functions](address-windowing-extensions.md).



| Function                                                           | Description                                                                                                           |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**AllocateUserPhysicalPages**](allocateuserphysicalpages.md)     | Allocates physical memory pages to be mapped and unmapped within any AWE region of the process.                       |
| [**FreeUserPhysicalPages**](freeuserphysicalpages.md)             | Frees physical memory pages previously allocated with [**AllocateUserPhysicalPages**](allocateuserphysicalpages.md). |
| [**MapUserPhysicalPages**](mapuserphysicalpages.md)               | Maps previously allocated physical memory pages at the specified address within an AWE region.                        |
| [**MapUserPhysicalPagesScatter**](/windows/win32/WinBase/nf-winbase-mapuserphysicalpagesscatter?branch=master) | Maps previously allocated physical memory pages at the specified address within an AWE region.                        |



 

## Heap Functions

The following are the [heap functions](heap-functions.md).



| Function                                             | Description                                                                 |
|------------------------------------------------------|-----------------------------------------------------------------------------|
| [**GetProcessHeap**](/windows/win32/HeapApi/nf-heapapi-getprocessheap?branch=master)             | Obtains a handle to the heap of the calling process.                        |
| [**GetProcessHeaps**](/windows/win32/HeapApi/nf-heapapi-getprocessheaps?branch=master)           | Obtains handles to all of the heaps that are valid for the calling process. |
| [**HeapAlloc**](/windows/win32/HeapApi/nf-heapapi-heapalloc?branch=master)                       | Allocates a block of memory from a heap.                                    |
| [**HeapCompact**](/windows/win32/HeapApi/nf-heapapi-heapcompact?branch=master)                   | Coalesces adjacent free blocks of memory on a heap.                         |
| [**HeapCreate**](/windows/win32/HeapApi/nf-heapapi-heapcreate?branch=master)                     | Creates a heap object.                                                      |
| [**HeapDestroy**](/windows/win32/HeapApi/nf-heapapi-heapdestroy?branch=master)                   | Destroys the specified heap object.                                         |
| [**HeapFree**](/windows/win32/HeapApi/nf-heapapi-heapfree?branch=master)                         | Frees a memory block allocated from a heap.                                 |
| [**HeapLock**](/windows/win32/HeapApi/nf-heapapi-heaplock?branch=master)                         | Attempts to acquire the lock associated with a specified heap.              |
| [**HeapQueryInformation**](/windows/win32/HeapApi/nf-heapapi-heapqueryinformation?branch=master) | Retrieves information about the specified heap.                             |
| [**HeapReAlloc**](/windows/win32/HeapApi/nf-heapapi-heaprealloc?branch=master)                   | Reallocates a block of memory from a heap.                                  |
| [**HeapSetInformation**](/windows/win32/HeapApi/nf-heapapi-heapsetinformation?branch=master)     | Sets heap information for the specified heap.                               |
| [**HeapSize**](/windows/win32/HeapApi/nf-heapapi-heapsize?branch=master)                         | Retrieves the size of a memory block allocated from a heap.                 |
| [**HeapUnlock**](/windows/win32/HeapApi/nf-heapapi-heapunlock?branch=master)                     | Releases ownership of the lock associated with a specified heap.            |
| [**HeapValidate**](/windows/win32/HeapApi/nf-heapapi-heapvalidate?branch=master)                 | Attempts to validate a specified heap.                                      |
| [**HeapWalk**](/windows/win32/HeapApi/nf-heapapi-heapwalk?branch=master)                         | Enumerates the memory blocks in a specified heap.                           |



 

## Virtual Memory Functions

The following are the [virtual memory functions](virtual-memory-functions.md).



| Function                                                               | Description                                                                                                                                                                               |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiscardVirtualMemory**](discardvirtualmemory.md)                   | Discards the memory contents of a range of memory pages, without decommitting the memory. The contents of discarded memory is undefined and must be rewritten by the application.         |
| [**OfferVirtualMemory**](offervirtualmemory.md)                       | Indicates that the data contained in a range of memory pages is no longer needed by the application and can be discarded by the system if necessary.                                      |
| [**PrefetchVirtualMemory**](prefetchvirtualmemory.md)                 | Prefetches virtual address ranges into physical memory.                                                                                                                                   |
| [**QueryVirtualMemoryInformation**](/windows/win32/MemoryApi/nf-memoryapi-queryvirtualmemoryinformation?branch=master) | Returns information about a page or a set of pages within the virtual address space of the specified process.                                                                             |
| [**ReclaimVirtualMemory**](reclaimvirtualmemory.md)                   | Reclaims a range of memory pages that were offered to the system with [**OfferVirtualMemory**](offervirtualmemory.md).                                                                   |
| [**VirtualAlloc**](virtualalloc.md)                                   | Reserves or commits a region of pages in the virtual address space of the calling process.                                                                                                |
| [**VirtualAllocEx**](virtualallocex.md)                               | Reserves or commits a region of pages in the virtual address space of the specified process.                                                                                              |
| [**VirtualAllocExNuma**](virtualallocexnuma.md)                       | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory.                                    |
| [**VirtualAllocFromApp**](/windows/win32/MemoryApi/nf-memoryapi-virtualallocfromapp?branch=master)                     | Reserves, commits, or changes the state of a region of pages in the virtual address space of the calling process. Memory allocated by this function is automatically initialized to zero. |
| [**VirtualFree**](virtualfree.md)                                     | Releases or decommits a region of pages within the virtual address space of the calling process.                                                                                          |
| [**VirtualFreeEx**](virtualfreeex.md)                                 | Releases or decommits a region of memory within the virtual address space of a specified process.                                                                                         |
| [**VirtualLock**](virtuallock.md)                                     | Locks the specified region of the process's virtual address space into physical memory.                                                                                                   |
| [**VirtualProtect**](virtualprotect.md)                               | Changes the access protection on a region of committed pages in the virtual address space of the calling process.                                                                         |
| [**VirtualProtectEx**](virtualprotectex.md)                           | Changes the access protection on a region of committed pages in the virtual address space of the calling process.                                                                         |
| [**VirtualProtectFromApp**](/windows/win32/MemoryApi/nf-memoryapi-virtualprotectfromapp?branch=master)                 | Changes the protection on a region of committed pages in the virtual address space of the calling process.                                                                                |
| [**VirtualQuery**](virtualquery.md)                                   | Provides information about a range of pages in the virtual address space of the calling process.                                                                                          |
| [**VirtualQueryEx**](virtualqueryex.md)                               | Provides information about a range of pages in the virtual address space of the calling process.                                                                                          |
| [**VirtualUnlock**](virtualunlock.md)                                 | Unlocks a specified range of pages in the virtual address space of a process.                                                                                                             |



 

## Global and Local Functions

The following are the [global and local functions](global-and-local-functions.md). These functions are provided for compatibility with 16-bit Windows and are used with Dynamic Data Exchange (DDE), the clipboard functions, and OLE data objects. Unless documentation specifically states that a global or local function should be used, new applications should use the corresponding [heap function](heap-functions.md) with the handle returned by [**GetProcessHeap**](/windows/win32/HeapApi/nf-heapapi-getprocessheap?branch=master). For equivalent functionality to the global or local function, set the heap function's *dwFlags* parameter to 0.



| Function                                                                     | Description                                                                                                                                                              | Corresponding heap function                                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**GlobalAlloc**](/windows/win32/WinBase/nf-winbase-globalalloc?branch=master), [**LocalAlloc**](/windows/win32/WinBase/nf-winbase-localalloc?branch=master)         | Allocates the specified number of bytes from the heap.                                                                                                                   | [**HeapAlloc**](/windows/win32/HeapApi/nf-heapapi-heapalloc?branch=master)                                                 |
| [**GlobalDiscard**](/windows/win32/WinBase/nf-winbase-globaldiscard?branch=master), [**LocalDiscard**](localdiscard.md) | Discards the specified global memory block.                                                                                                                              | Not applicable.                                                                |
| [**GlobalFlags**](/windows/win32/WinBase/nf-winbase-globalflags?branch=master), [**LocalFlags**](/windows/win32/WinBase/nf-winbase-localflags?branch=master)         | Returns information about the specified global memory object.                                                                                                            | Not applicable. Use [**HeapValidate**](/windows/win32/HeapApi/nf-heapapi-heapvalidate?branch=master) to validate the heap. |
| [**GlobalFree**](/windows/win32/WinBase/nf-winbase-globalfree?branch=master), [**LocalFree**](/windows/win32/WinBase/nf-winbase-localfree?branch=master)             | Frees the specified global memory object.                                                                                                                                | [**HeapFree**](/windows/win32/HeapApi/nf-heapapi-heapfree?branch=master)                                                   |
| [**GlobalHandle**](/windows/win32/WinBase/nf-winbase-globalhandle?branch=master), [**LocalHandle**](/windows/win32/WinBase/nf-winbase-localhandle?branch=master)     | Retrieves the handle associated with the specified pointer to a global memory block. This function should be used only with OLE and clipboard functions that require it. | Not applicable.                                                                |
| [**GlobalLock**](/windows/win32/WinBase/nf-winbase-globallock?branch=master), [**LocalLock**](/windows/win32/WinBase/nf-winbase-locallock?branch=master)             | Locks a global memory object and returns a pointer to the first byte of the object's memory block.                                                                       | Not applicable.                                                                |
| [**GlobalReAlloc**](/windows/win32/WinBase/nf-winbase-globalrealloc?branch=master), [**LocalReAlloc**](/windows/win32/WinBase/nf-winbase-localrealloc?branch=master) | Changes the size or attributes of a specified global memory object.                                                                                                      | [**HeapReAlloc**](/windows/win32/HeapApi/nf-heapapi-heaprealloc?branch=master)                                             |
| [**GlobalSize**](/windows/win32/WinBase/nf-winbase-globalsize?branch=master), [**LocalSize**](/windows/win32/WinBase/nf-winbase-localsize?branch=master)             | Retrieves the current size of the specified global memory object.                                                                                                        | [**HeapSize**](/windows/win32/HeapApi/nf-heapapi-heapsize?branch=master)                                                   |
| [**GlobalUnlock**](/windows/win32/WinBase/nf-winbase-globalunlock?branch=master), [**LocalUnlock**](/windows/win32/WinBase/nf-winbase-localunlock?branch=master)     | Decrements the lock count associated with a memory object. This function should be used only with OLE and clipboard functions that require it.                           | Not applicable.                                                                |



 

## Bad Memory Functions

The following are the bad memory functions.



| Function                                                                         | Description                                                                                                                                                                                        |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*BadMemoryCallbackRoutine*](/windows/win32/WinBase/?branch=master)                       | An application-defined function registered with the [**RegisterBadMemoryNotification**](registerbadmemorynotification.md) function that is called when one or more bad memory pages are detected. |
| [**GetMemoryErrorHandlingCapabilities**](getmemoryerrorhandlingcapabilities.md) | Gets the memory error handling capabilities of the system.                                                                                                                                         |
| [**RegisterBadMemoryNotification**](registerbadmemorynotification.md)           | Registers a bad memory notification that is called when one or more bad memory pages are detected.                                                                                                 |
| [**UnregisterBadMemoryNotification**](unregisterbadmemorynotification.md)       | Closes the specified bad memory notification handle.                                                                                                                                               |



 

## Enclave Functions

The following are the enclave functions.



| Function                                                 | Description                                                                                                                                                                                                         |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateEnclave**](/windows/win32/enclaveapi/nf-enclaveapi-createenclave?branch=master)                   | Creates a new uninitialized enclave. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave. |
| [**InitializeEnclave**](/windows/win32/enclaveapi/nf-enclaveapi-initializeenclave?branch=master)           | Initializes an enclave that you created and loaded with data.                                                                                                                                                       |
| [**IsEnclaveTypeSupported**](/windows/win32/enclaveapi/nf-enclaveapi-isenclavetypesupported?branch=master) | Retrieves whether the specified type of enclave is supported.                                                                                                                                                       |
| [**LoadEnclaveData**](/windows/win32/enclaveapi/nf-enclaveapi-loadenclavedata?branch=master)               | Loads data into an uninitialized enclave that you created by calling [**CreateEnclave**](/windows/win32/enclaveapi/nf-enclaveapi-createenclave?branch=master).                                                                                                        |



 

## Obsolete Functions

The following functions are provided only for compatibility with 16-bit versions of Windows:

-   [**IsBadCodePtr**](/windows/win32/WinBase/nf-winbase-isbadcodeptr?branch=master)
-   [**IsBadReadPtr**](/windows/win32/WinBase/nf-winbase-isbadreadptr?branch=master)
-   [**IsBadStringPtr**](/windows/win32/WinBase/nf-winbase-isbadstringptra?branch=master)
-   [**IsBadWritePtr**](/windows/win32/WinBase/nf-winbase-isbadwriteptr?branch=master)

The following function can return incorrect information and should not be used. Use the [**GlobalMemoryStatusEx**](/windows/win32/WinBase/?branch=master) function instead:

-   [**GlobalMemoryStatus**](/windows/win32/WinBase/nf-winbase-globalmemorystatus?branch=master)

 

 



