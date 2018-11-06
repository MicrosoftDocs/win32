---
Description: 'This topic describes the memory management functions:'
ms.assetid: 5a2a7a62-0bda-4a0d-93d2-25b4898871fd
title: Memory Management Functions
ms.topic: article
ms.date: 05/31/2018
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
| [**AddSecureMemoryCacheCallback**](/windows/desktop/api/WinBase/nf-winbase-addsecurememorycachecallback)             | Registers a callback function to be called when a secured memory range is freed or its protections are changed.                                        |
| [**CopyMemory**](https://msdn.microsoft.com/en-us/library/Aa366535(v=VS.85).aspx)                                                 | Copies a block of memory from one location to another.                                                                                                 |
| [**CreateMemoryResourceNotification**](https://msdn.microsoft.com/en-us/library/Aa366541(v=VS.85).aspx)     | Creates a memory resource notification object.                                                                                                         |
| [**FillMemory**](https://msdn.microsoft.com/en-us/library/Aa366561(v=VS.85).aspx)                                                 | Fills a block of memory with a specified value.                                                                                                        |
| [**GetLargePageMinimum**](https://msdn.microsoft.com/en-us/library/Aa366568(v=VS.85).aspx)                               | Retrieves the minimum size of a large page.                                                                                                            |
| [**GetPhysicallyInstalledSystemMemory**](https://msdn.microsoft.com/en-us/library/Cc300158(v=VS.85).aspx) | Retrieves the amount of RAM that is physically installed on the computer.                                                                              |
| [**GetSystemFileCacheSize**](https://msdn.microsoft.com/en-us/library/Aa965224(v=VS.85).aspx)                         | Retrieves the current size limits for the working set of the system cache.                                                                             |
| [**GetWriteWatch**](https://msdn.microsoft.com/en-us/library/Aa366573(v=VS.85).aspx)                                           | Retrieves the addresses of the pages that have been written to in a region of virtual memory.                                                          |
| [**GlobalMemoryStatusEx**](https://msdn.microsoft.com/en-us/library/Aa366589(v=VS.85).aspx)                             | Obtains information about the system's current usage of both physical and virtual memory.                                                              |
| [**MoveMemory**](https://msdn.microsoft.com/en-us/library/Aa366788(v=VS.85).aspx)                                                 | Moves a block of memory from one location to another.                                                                                                  |
| [**QueryMemoryResourceNotification**](https://msdn.microsoft.com/en-us/library/Aa366799(v=VS.85).aspx)       | Retrieves the state of the specified memory resource object.                                                                                           |
| [**RemoveSecureMemoryCacheCallback**](/windows/desktop/api/WinBase/nf-winbase-removesecurememorycachecallback)       | Unregisters a callback function that was previously registered with the [**AddSecureMemoryCacheCallback**](/windows/desktop/api/WinBase/nf-winbase-addsecurememorycachecallback) function. |
| [**ResetWriteWatch**](https://msdn.microsoft.com/en-us/library/Aa366874(v=VS.85).aspx)                                       | Resets the write-tracking state for a region of virtual memory.                                                                                        |
| [**SecureMemoryCacheCallback**](/windows/desktop/api/WinNT/nc-winnt-psecure_memory_cache_callback)                   | An application-defined function that is called when a secured memory range is freed or its protections are changed.                                    |
| [**SecureZeroMemory**](https://msdn.microsoft.com/en-us/library/Aa366877(v=VS.85).aspx)                                     | Fills a block of memory with zeros.                                                                                                                    |
| [**SetSystemFileCacheSize**](https://msdn.microsoft.com/en-us/library/Aa965240(v=VS.85).aspx)                         | Limits the size of the working set for the file system cache.                                                                                          |
| [**ZeroMemory**](https://msdn.microsoft.com/en-us/library/Aa366920(v=VS.85).aspx)                                                 | Fills a block of memory with zeros.                                                                                                                    |



 

## Data Execution Prevention Functions

The following functions are used with [Data Execution Prevention](data-execution-prevention.md) (DEP).



| Function                                           | Description                            |
|----------------------------------------------------|----------------------------------------|
| [**GetProcessDEPPolicy**](/windows/desktop/api/WinBase/nf-winbase-getprocessdeppolicy) | Retrieves DEP settings for a process.  |
| [**GetSystemDEPPolicy**](/windows/desktop/api/WinBase/nf-winbase-getsystemdeppolicy)   | Retrieves DEP settings for the system. |
| [**SetProcessDEPPolicy**](/windows/desktop/api/WinBase/nf-winbase-setprocessdeppolicy) | Changes DEP settings for a process.    |



 

## File Mapping Functions

The following functions are used in [file mapping](file-mapping.md).



| Function                                                     | Description                                                                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga)               | Creates or opens a named or unnamed file mapping object for a specified file.                                                                                                      |
| [**CreateFileMappingFromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-createfilemappingfromapp) | Creates or opens a named or unnamed file mapping object for a specified file from a Windows Store app.                                                                             |
| [**CreateFileMappingNuma**](/windows/desktop/api/WinBase/nf-winbase-createfilemappingnumaa)       | Creates or opens a named or unnamed file mapping object for a specified file, and specifies the NUMA node for the physical memory.                                                 |
| [**FlushViewOfFile**](https://msdn.microsoft.com/en-us/library/Aa366563(v=VS.85).aspx)                   | Writes to the disk a byte range within a mapped view of a file.                                                                                                                    |
| [**GetMappedFileName**](https://msdn.microsoft.com/library/ms683195(v=VS.85).aspx)              | Checks whether the specified address is within a memory-mapped file in the address space of the specified process. If so, the function returns the name of the memory-mapped file. |
| [**MapViewOfFile**](https://msdn.microsoft.com/en-us/library/Aa366761(v=VS.85).aspx)                       | Maps a view of a file mapping into the address space of a calling process.                                                                                                         |
| [**MapViewOfFile2**](https://msdn.microsoft.com/en-us/library/Mt492557(v=VS.85).aspx)                     | Maps a view of a file or a pagefile-backed section into the address space of the specified process.                                                                                |
| [**MapViewOfFileEx**](https://msdn.microsoft.com/en-us/library/Aa366763(v=VS.85).aspx)                   | Maps a view of a file mapping into the address space of a calling process. A caller can optionally specify a suggested memory address for the view.                                |
| [**MapViewOfFileExNuma**](/windows/desktop/api/WinBase/nf-winbase-mapviewoffileexnuma)           | Maps a view of a file mapping into the address space of a calling process, and specifies the NUMA node for the physical memory.                                                    |
| [**MapViewOfFileFromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-mapviewoffilefromapp)         | Maps a view of a file mapping into the address space of a calling process from a Windows Store app.                                                                                |
| [**MapViewOfFileNuma2**](https://msdn.microsoft.com/en-us/library/Mt492558(v=VS.85).aspx)             | Maps a view of a file or a pagefile-backed section into the address space of the specified process.                                                                                |
| [**OpenFileMapping**](/windows/desktop/api/WinBase/nf-winbase-openfilemappinga)                   | Opens a named file mapping object.                                                                                                                                                 |
| [**UnmapViewOfFile**](https://msdn.microsoft.com/en-us/library/Aa366882(v=VS.85).aspx)                   | Unmaps a mapped view of a file from the calling process's address space.                                                                                                           |
| [**UnmapViewOfFile2**](https://msdn.microsoft.com/en-us/library/Mt492559(v=VS.85).aspx)                 | Unmaps a previously mapped view of a file or a pagefile-backed section.                                                                                                            |



 

## AWE Functions

The following are the [AWE functions](address-windowing-extensions.md).



| Function                                                           | Description                                                                                                           |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**AllocateUserPhysicalPages**](https://msdn.microsoft.com/en-us/library/Aa366528(v=VS.85).aspx)     | Allocates physical memory pages to be mapped and unmapped within any AWE region of the process.                       |
| [**FreeUserPhysicalPages**](https://msdn.microsoft.com/en-us/library/Aa366566(v=VS.85).aspx)             | Frees physical memory pages previously allocated with [**AllocateUserPhysicalPages**](https://msdn.microsoft.com/en-us/library/Aa366528(v=VS.85).aspx). |
| [**MapUserPhysicalPages**](https://msdn.microsoft.com/en-us/library/Aa366753(v=VS.85).aspx)               | Maps previously allocated physical memory pages at the specified address within an AWE region.                        |
| [**MapUserPhysicalPagesScatter**](/windows/desktop/api/WinBase/nf-winbase-mapuserphysicalpagesscatter) | Maps previously allocated physical memory pages at the specified address within an AWE region.                        |



 

## Heap Functions

The following are the [heap functions](heap-functions.md).



| Function                                             | Description                                                                 |
|------------------------------------------------------|-----------------------------------------------------------------------------|
| [**GetProcessHeap**](/windows/desktop/api/HeapApi/nf-heapapi-getprocessheap)             | Obtains a handle to the heap of the calling process.                        |
| [**GetProcessHeaps**](/windows/desktop/api/HeapApi/nf-heapapi-getprocessheaps)           | Obtains handles to all of the heaps that are valid for the calling process. |
| [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc)                       | Allocates a block of memory from a heap.                                    |
| [**HeapCompact**](/windows/desktop/api/HeapApi/nf-heapapi-heapcompact)                   | Coalesces adjacent free blocks of memory on a heap.                         |
| [**HeapCreate**](/windows/desktop/api/HeapApi/nf-heapapi-heapcreate)                     | Creates a heap object.                                                      |
| [**HeapDestroy**](/windows/desktop/api/HeapApi/nf-heapapi-heapdestroy)                   | Destroys the specified heap object.                                         |
| [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree)                         | Frees a memory block allocated from a heap.                                 |
| [**HeapLock**](/windows/desktop/api/HeapApi/nf-heapapi-heaplock)                         | Attempts to acquire the lock associated with a specified heap.              |
| [**HeapQueryInformation**](/windows/desktop/api/HeapApi/nf-heapapi-heapqueryinformation) | Retrieves information about the specified heap.                             |
| [**HeapReAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heaprealloc)                   | Reallocates a block of memory from a heap.                                  |
| [**HeapSetInformation**](/windows/desktop/api/HeapApi/nf-heapapi-heapsetinformation)     | Sets heap information for the specified heap.                               |
| [**HeapSize**](/windows/desktop/api/HeapApi/nf-heapapi-heapsize)                         | Retrieves the size of a memory block allocated from a heap.                 |
| [**HeapUnlock**](/windows/desktop/api/HeapApi/nf-heapapi-heapunlock)                     | Releases ownership of the lock associated with a specified heap.            |
| [**HeapValidate**](/windows/desktop/api/HeapApi/nf-heapapi-heapvalidate)                 | Attempts to validate a specified heap.                                      |
| [**HeapWalk**](/windows/desktop/api/HeapApi/nf-heapapi-heapwalk)                         | Enumerates the memory blocks in a specified heap.                           |



 

## Virtual Memory Functions

The following are the [virtual memory functions](virtual-memory-functions.md).



| Function                                                               | Description                                                                                                                                                                               |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiscardVirtualMemory**](https://msdn.microsoft.com/en-us/library/Dn781432(v=VS.85).aspx)                   | Discards the memory contents of a range of memory pages, without decommitting the memory. The contents of discarded memory is undefined and must be rewritten by the application.         |
| [**OfferVirtualMemory**](https://msdn.microsoft.com/en-us/library/Dn781436(v=VS.85).aspx)                       | Indicates that the data contained in a range of memory pages is no longer needed by the application and can be discarded by the system if necessary.                                      |
| [**PrefetchVirtualMemory**](https://msdn.microsoft.com/en-us/library/Hh780543(v=VS.85).aspx)                 | Prefetches virtual address ranges into physical memory.                                                                                                                                   |
| [**QueryVirtualMemoryInformation**](/windows/desktop/api/MemoryApi/nf-memoryapi-queryvirtualmemoryinformation) | Returns information about a page or a set of pages within the virtual address space of the specified process.                                                                             |
| [**ReclaimVirtualMemory**](https://msdn.microsoft.com/en-us/library/Dn781437(v=VS.85).aspx)                   | Reclaims a range of memory pages that were offered to the system with [**OfferVirtualMemory**](https://msdn.microsoft.com/en-us/library/Dn781436(v=VS.85).aspx).                                                                   |
| [**VirtualAlloc**](https://msdn.microsoft.com/en-us/library/Aa366887(v=VS.85).aspx)                                   | Reserves or commits a region of pages in the virtual address space of the calling process.                                                                                                |
| [**VirtualAllocEx**](https://msdn.microsoft.com/en-us/library/Aa366890(v=VS.85).aspx)                               | Reserves or commits a region of pages in the virtual address space of the specified process.                                                                                              |
| [**VirtualAllocExNuma**](https://msdn.microsoft.com/en-us/library/Aa366891(v=VS.85).aspx)                       | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory.                                    |
| [**VirtualAllocFromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-virtualallocfromapp)                     | Reserves, commits, or changes the state of a region of pages in the virtual address space of the calling process. Memory allocated by this function is automatically initialized to zero. |
| [**VirtualFree**](https://msdn.microsoft.com/en-us/library/Aa366892(v=VS.85).aspx)                                     | Releases or decommits a region of pages within the virtual address space of the calling process.                                                                                          |
| [**VirtualFreeEx**](https://msdn.microsoft.com/en-us/library/Aa366894(v=VS.85).aspx)                                 | Releases or decommits a region of memory within the virtual address space of a specified process.                                                                                         |
| [**VirtualLock**](https://msdn.microsoft.com/en-us/library/Aa366895(v=VS.85).aspx)                                     | Locks the specified region of the process's virtual address space into physical memory.                                                                                                   |
| [**VirtualProtect**](https://msdn.microsoft.com/en-us/library/Aa366898(v=VS.85).aspx)                               | Changes the access protection on a region of committed pages in the virtual address space of the calling process.                                                                         |
| [**VirtualProtectEx**](https://msdn.microsoft.com/en-us/library/Aa366899(v=VS.85).aspx)                           | Changes the access protection on a region of committed pages in the virtual address space of the calling process.                                                                         |
| [**VirtualProtectFromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-virtualprotectfromapp)                 | Changes the protection on a region of committed pages in the virtual address space of the calling process.                                                                                |
| [**VirtualQuery**](https://msdn.microsoft.com/en-us/library/Aa366902(v=VS.85).aspx)                                   | Provides information about a range of pages in the virtual address space of the calling process.                                                                                          |
| [**VirtualQueryEx**](https://msdn.microsoft.com/en-us/library/Aa366907(v=VS.85).aspx)                               | Provides information about a range of pages in the virtual address space of the calling process.                                                                                          |
| [**VirtualUnlock**](https://msdn.microsoft.com/en-us/library/Aa366910(v=VS.85).aspx)                                 | Unlocks a specified range of pages in the virtual address space of a process.                                                                                                             |



 

## Global and Local Functions

The following are the [global and local functions](global-and-local-functions.md). These functions are provided for compatibility with 16-bit Windows and are used with Dynamic Data Exchange (DDE), the clipboard functions, and OLE data objects. Unless documentation specifically states that a global or local function should be used, new applications should use the corresponding [heap function](heap-functions.md) with the handle returned by [**GetProcessHeap**](/windows/desktop/api/HeapApi/nf-heapapi-getprocessheap). For equivalent functionality to the global or local function, set the heap function's *dwFlags* parameter to 0.



| Function                                                                     | Description                                                                                                                                                              | Corresponding heap function                                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc), [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc)         | Allocates the specified number of bytes from the heap.                                                                                                                   | [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc)                                                 |
| [**GlobalDiscard**](/windows/desktop/api/WinBase/nf-winbase-globaldiscard), [**LocalDiscard**](https://msdn.microsoft.com/en-us/library/Aa366727(v=VS.85).aspx) | Discards the specified global memory block.                                                                                                                              | Not applicable.                                                                |
| [**GlobalFlags**](/windows/desktop/api/WinBase/nf-winbase-globalflags), [**LocalFlags**](/windows/desktop/api/WinBase/nf-winbase-localflags)         | Returns information about the specified global memory object.                                                                                                            | Not applicable. Use [**HeapValidate**](/windows/desktop/api/HeapApi/nf-heapapi-heapvalidate) to validate the heap. |
| [**GlobalFree**](/windows/desktop/api/WinBase/nf-winbase-globalfree), [**LocalFree**](/windows/desktop/api/WinBase/nf-winbase-localfree)             | Frees the specified global memory object.                                                                                                                                | [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree)                                                   |
| [**GlobalHandle**](/windows/desktop/api/WinBase/nf-winbase-globalhandle), [**LocalHandle**](/windows/desktop/api/WinBase/nf-winbase-localhandle)     | Retrieves the handle associated with the specified pointer to a global memory block. This function should be used only with OLE and clipboard functions that require it. | Not applicable.                                                                |
| [**GlobalLock**](/windows/desktop/api/WinBase/nf-winbase-globallock), [**LocalLock**](/windows/desktop/api/WinBase/nf-winbase-locallock)             | Locks a global memory object and returns a pointer to the first byte of the object's memory block.                                                                       | Not applicable.                                                                |
| [**GlobalReAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalrealloc), [**LocalReAlloc**](/windows/desktop/api/WinBase/nf-winbase-localrealloc) | Changes the size or attributes of a specified global memory object.                                                                                                      | [**HeapReAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heaprealloc)                                             |
| [**GlobalSize**](/windows/desktop/api/WinBase/nf-winbase-globalsize), [**LocalSize**](/windows/desktop/api/WinBase/nf-winbase-localsize)             | Retrieves the current size of the specified global memory object.                                                                                                        | [**HeapSize**](/windows/desktop/api/HeapApi/nf-heapapi-heapsize)                                                   |
| [**GlobalUnlock**](/windows/desktop/api/WinBase/nf-winbase-globalunlock), [**LocalUnlock**](/windows/desktop/api/WinBase/nf-winbase-localunlock)     | Decrements the lock count associated with a memory object. This function should be used only with OLE and clipboard functions that require it.                           | Not applicable.                                                                |



 

## Bad Memory Functions

The following are the bad memory functions.



| Function                                                                         | Description                                                                                                                                                                                        |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*BadMemoryCallbackRoutine*](https://msdn.microsoft.com/en-us/library/Hh691011(v=VS.85).aspx)                       | An application-defined function registered with the [**RegisterBadMemoryNotification**](https://msdn.microsoft.com/en-us/library/Hh691013(v=VS.85).aspx) function that is called when one or more bad memory pages are detected. |
| [**GetMemoryErrorHandlingCapabilities**](https://msdn.microsoft.com/en-us/library/Hh691012(v=VS.85).aspx) | Gets the memory error handling capabilities of the system.                                                                                                                                         |
| [**RegisterBadMemoryNotification**](https://msdn.microsoft.com/en-us/library/Hh691013(v=VS.85).aspx)           | Registers a bad memory notification that is called when one or more bad memory pages are detected.                                                                                                 |
| [**UnregisterBadMemoryNotification**](https://msdn.microsoft.com/en-us/library/Hh691014(v=VS.85).aspx)       | Closes the specified bad memory notification handle.                                                                                                                                               |



 

## Enclave Functions

The following are the enclave functions.



| Function                                                 | Description                                                                                                                                                                                                         |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-createenclave)                   | Creates a new uninitialized enclave. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave. |
| [**InitializeEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-initializeenclave)           | Initializes an enclave that you created and loaded with data.                                                                                                                                                       |
| [**IsEnclaveTypeSupported**](/windows/desktop/api/enclaveapi/nf-enclaveapi-isenclavetypesupported) | Retrieves whether the specified type of enclave is supported.                                                                                                                                                       |
| [**LoadEnclaveData**](/windows/desktop/api/enclaveapi/nf-enclaveapi-loadenclavedata)               | Loads data into an uninitialized enclave that you created by calling [**CreateEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-createenclave).                                                                                                        |



 

## Obsolete Functions

The following functions are provided only for compatibility with 16-bit versions of Windows:

-   [**IsBadCodePtr**](/windows/desktop/api/WinBase/nf-winbase-isbadcodeptr)
-   [**IsBadReadPtr**](/windows/desktop/api/WinBase/nf-winbase-isbadreadptr)
-   [**IsBadStringPtr**](/windows/desktop/api/WinBase/nf-winbase-isbadstringptra)
-   [**IsBadWritePtr**](/windows/desktop/api/WinBase/nf-winbase-isbadwriteptr)

The following function can return incorrect information and should not be used. Use the [**GlobalMemoryStatusEx**](https://msdn.microsoft.com/en-us/library/Aa366589(v=VS.85).aspx) function instead:

-   [**GlobalMemoryStatus**](/windows/desktop/api/WinBase/nf-winbase-globalmemorystatus)

 

 



