---
Description: 'This topic describes the memory management functions:'
ms.assetid: '5a2a7a62-0bda-4a0d-93d2-25b4898871fd'
title: Memory Management Functions
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
| [**AddSecureMemoryCacheCallback**](addsecurememorycachecallback.md)             | Registers a callback function to be called when a secured memory range is freed or its protections are changed.                                        |
| [**CopyMemory**](copymemory.md)                                                 | Copies a block of memory from one location to another.                                                                                                 |
| [**CreateMemoryResourceNotification**](creatememoryresourcenotification.md)     | Creates a memory resource notification object.                                                                                                         |
| [**FillMemory**](fillmemory.md)                                                 | Fills a block of memory with a specified value.                                                                                                        |
| [**GetLargePageMinimum**](getlargepageminimum.md)                               | Retrieves the minimum size of a large page.                                                                                                            |
| [**GetPhysicallyInstalledSystemMemory**](getphysicallyinstalledsystemmemory.md) | Retrieves the amount of RAM that is physically installed on the computer.                                                                              |
| [**GetSystemFileCacheSize**](getsystemfilecachesize.md)                         | Retrieves the current size limits for the working set of the system cache.                                                                             |
| [**GetWriteWatch**](getwritewatch.md)                                           | Retrieves the addresses of the pages that have been written to in a region of virtual memory.                                                          |
| [**GlobalMemoryStatusEx**](globalmemorystatusex.md)                             | Obtains information about the system's current usage of both physical and virtual memory.                                                              |
| [**MoveMemory**](movememory.md)                                                 | Moves a block of memory from one location to another.                                                                                                  |
| [**QueryMemoryResourceNotification**](querymemoryresourcenotification.md)       | Retrieves the state of the specified memory resource object.                                                                                           |
| [**RemoveSecureMemoryCacheCallback**](removesecurememorycachecallback.md)       | Unregisters a callback function that was previously registered with the [**AddSecureMemoryCacheCallback**](addsecurememorycachecallback.md) function. |
| [**ResetWriteWatch**](resetwritewatch.md)                                       | Resets the write-tracking state for a region of virtual memory.                                                                                        |
| [**SecureMemoryCacheCallback**](securememorycachecallback.md)                   | An application-defined function that is called when a secured memory range is freed or its protections are changed.                                    |
| [**SecureZeroMemory**](securezeromemory.md)                                     | Fills a block of memory with zeros.                                                                                                                    |
| [**SetSystemFileCacheSize**](setsystemfilecachesize.md)                         | Limits the size of the working set for the file system cache.                                                                                          |
| [**ZeroMemory**](zeromemory.md)                                                 | Fills a block of memory with zeros.                                                                                                                    |



 

## Data Execution Prevention Functions

The following functions are used with [Data Execution Prevention](data-execution-prevention.md) (DEP).



| Function                                           | Description                            |
|----------------------------------------------------|----------------------------------------|
| [**GetProcessDEPPolicy**](getprocessdeppolicy.md) | Retrieves DEP settings for a process.  |
| [**GetSystemDEPPolicy**](getsystemdeppolicy.md)   | Retrieves DEP settings for the system. |
| [**SetProcessDEPPolicy**](setprocessdeppolicy.md) | Changes DEP settings for a process.    |



 

## File Mapping Functions

The following functions are used in [file mapping](file-mapping.md).



| Function                                                     | Description                                                                                                                                                                        |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateFileMapping**](createfilemapping.md)               | Creates or opens a named or unnamed file mapping object for a specified file.                                                                                                      |
| [**CreateFileMappingFromApp**](createfilemappingfromapp.md) | Creates or opens a named or unnamed file mapping object for a specified file from a Windows Store app.                                                                             |
| [**CreateFileMappingNuma**](createfilemappingnuma.md)       | Creates or opens a named or unnamed file mapping object for a specified file, and specifies the NUMA node for the physical memory.                                                 |
| [**FlushViewOfFile**](flushviewoffile.md)                   | Writes to the disk a byte range within a mapped view of a file.                                                                                                                    |
| [**GetMappedFileName**](base.getmappedfilename)              | Checks whether the specified address is within a memory-mapped file in the address space of the specified process. If so, the function returns the name of the memory-mapped file. |
| [**MapViewOfFile**](mapviewoffile.md)                       | Maps a view of a file mapping into the address space of a calling process.                                                                                                         |
| [**MapViewOfFile2**](mapviewoffile2.md)                     | Maps a view of a file or a pagefile-backed section into the address space of the specified process.                                                                                |
| [**MapViewOfFileEx**](mapviewoffileex.md)                   | Maps a view of a file mapping into the address space of a calling process. A caller can optionally specify a suggested memory address for the view.                                |
| [**MapViewOfFileExNuma**](mapviewoffileexnuma.md)           | Maps a view of a file mapping into the address space of a calling process, and specifies the NUMA node for the physical memory.                                                    |
| [**MapViewOfFileFromApp**](mapviewoffilefromapp.md)         | Maps a view of a file mapping into the address space of a calling process from a Windows Store app.                                                                                |
| [**MapViewOfFileNuma2**](mapviewoffilenuma2.md)             | Maps a view of a file or a pagefile-backed section into the address space of the specified process.                                                                                |
| [**OpenFileMapping**](openfilemapping.md)                   | Opens a named file mapping object.                                                                                                                                                 |
| [**UnmapViewOfFile**](unmapviewoffile.md)                   | Unmaps a mapped view of a file from the calling process's address space.                                                                                                           |
| [**UnmapViewOfFile2**](unmapviewoffile2.md)                 | Unmaps a previously mapped view of a file or a pagefile-backed section.                                                                                                            |



 

## AWE Functions

The following are the [AWE functions](address-windowing-extensions.md).



| Function                                                           | Description                                                                                                           |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**AllocateUserPhysicalPages**](allocateuserphysicalpages.md)     | Allocates physical memory pages to be mapped and unmapped within any AWE region of the process.                       |
| [**FreeUserPhysicalPages**](freeuserphysicalpages.md)             | Frees physical memory pages previously allocated with [**AllocateUserPhysicalPages**](allocateuserphysicalpages.md). |
| [**MapUserPhysicalPages**](mapuserphysicalpages.md)               | Maps previously allocated physical memory pages at the specified address within an AWE region.                        |
| [**MapUserPhysicalPagesScatter**](mapuserphysicalpagesscatter.md) | Maps previously allocated physical memory pages at the specified address within an AWE region.                        |



 

## Heap Functions

The following are the [heap functions](heap-functions.md).



| Function                                             | Description                                                                 |
|------------------------------------------------------|-----------------------------------------------------------------------------|
| [**GetProcessHeap**](getprocessheap.md)             | Obtains a handle to the heap of the calling process.                        |
| [**GetProcessHeaps**](getprocessheaps.md)           | Obtains handles to all of the heaps that are valid for the calling process. |
| [**HeapAlloc**](heapalloc.md)                       | Allocates a block of memory from a heap.                                    |
| [**HeapCompact**](heapcompact.md)                   | Coalesces adjacent free blocks of memory on a heap.                         |
| [**HeapCreate**](heapcreate.md)                     | Creates a heap object.                                                      |
| [**HeapDestroy**](heapdestroy.md)                   | Destroys the specified heap object.                                         |
| [**HeapFree**](heapfree.md)                         | Frees a memory block allocated from a heap.                                 |
| [**HeapLock**](heaplock.md)                         | Attempts to acquire the lock associated with a specified heap.              |
| [**HeapQueryInformation**](heapqueryinformation.md) | Retrieves information about the specified heap.                             |
| [**HeapReAlloc**](heaprealloc.md)                   | Reallocates a block of memory from a heap.                                  |
| [**HeapSetInformation**](heapsetinformation.md)     | Sets heap information for the specified heap.                               |
| [**HeapSize**](heapsize.md)                         | Retrieves the size of a memory block allocated from a heap.                 |
| [**HeapUnlock**](heapunlock.md)                     | Releases ownership of the lock associated with a specified heap.            |
| [**HeapValidate**](heapvalidate.md)                 | Attempts to validate a specified heap.                                      |
| [**HeapWalk**](heapwalk.md)                         | Enumerates the memory blocks in a specified heap.                           |



 

## Virtual Memory Functions

The following are the [virtual memory functions](virtual-memory-functions.md).



| Function                                                               | Description                                                                                                                                                                               |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DiscardVirtualMemory**](discardvirtualmemory.md)                   | Discards the memory contents of a range of memory pages, without decommitting the memory. The contents of discarded memory is undefined and must be rewritten by the application.         |
| [**OfferVirtualMemory**](offervirtualmemory.md)                       | Indicates that the data contained in a range of memory pages is no longer needed by the application and can be discarded by the system if necessary.                                      |
| [**PrefetchVirtualMemory**](prefetchvirtualmemory.md)                 | Prefetches virtual address ranges into physical memory.                                                                                                                                   |
| [**QueryVirtualMemoryInformation**](queryvirtualmemoryinformation.md) | Returns information about a page or a set of pages within the virtual address space of the specified process.                                                                             |
| [**ReclaimVirtualMemory**](reclaimvirtualmemory.md)                   | Reclaims a range of memory pages that were offered to the system with [**OfferVirtualMemory**](offervirtualmemory.md).                                                                   |
| [**VirtualAlloc**](virtualalloc.md)                                   | Reserves or commits a region of pages in the virtual address space of the calling process.                                                                                                |
| [**VirtualAllocEx**](virtualallocex.md)                               | Reserves or commits a region of pages in the virtual address space of the specified process.                                                                                              |
| [**VirtualAllocExNuma**](virtualallocexnuma.md)                       | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory.                                    |
| [**VirtualAllocFromApp**](virtualallocfromapp.md)                     | Reserves, commits, or changes the state of a region of pages in the virtual address space of the calling process. Memory allocated by this function is automatically initialized to zero. |
| [**VirtualFree**](virtualfree.md)                                     | Releases or decommits a region of pages within the virtual address space of the calling process.                                                                                          |
| [**VirtualFreeEx**](virtualfreeex.md)                                 | Releases or decommits a region of memory within the virtual address space of a specified process.                                                                                         |
| [**VirtualLock**](virtuallock.md)                                     | Locks the specified region of the process's virtual address space into physical memory.                                                                                                   |
| [**VirtualProtect**](virtualprotect.md)                               | Changes the access protection on a region of committed pages in the virtual address space of the calling process.                                                                         |
| [**VirtualProtectEx**](virtualprotectex.md)                           | Changes the access protection on a region of committed pages in the virtual address space of the calling process.                                                                         |
| [**VirtualProtectFromApp**](virtualprotectfromapp.md)                 | Changes the protection on a region of committed pages in the virtual address space of the calling process.                                                                                |
| [**VirtualQuery**](virtualquery.md)                                   | Provides information about a range of pages in the virtual address space of the calling process.                                                                                          |
| [**VirtualQueryEx**](virtualqueryex.md)                               | Provides information about a range of pages in the virtual address space of the calling process.                                                                                          |
| [**VirtualUnlock**](virtualunlock.md)                                 | Unlocks a specified range of pages in the virtual address space of a process.                                                                                                             |



 

## Global and Local Functions

The following are the [global and local functions](global-and-local-functions.md). These functions are provided for compatibility with 16-bit Windows and are used with Dynamic Data Exchange (DDE), the clipboard functions, and OLE data objects. Unless documentation specifically states that a global or local function should be used, new applications should use the corresponding [heap function](heap-functions.md) with the handle returned by [**GetProcessHeap**](getprocessheap.md). For equivalent functionality to the global or local function, set the heap function's *dwFlags* parameter to 0.



| Function                                                                     | Description                                                                                                                                                              | Corresponding heap function                                                    |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**GlobalAlloc**](globalalloc.md), [**LocalAlloc**](localalloc.md)         | Allocates the specified number of bytes from the heap.                                                                                                                   | [**HeapAlloc**](heapalloc.md)                                                 |
| [**GlobalDiscard**](globaldiscard.md), [**LocalDiscard**](localdiscard.md) | Discards the specified global memory block.                                                                                                                              | Not applicable.                                                                |
| [**GlobalFlags**](globalflags.md), [**LocalFlags**](localflags.md)         | Returns information about the specified global memory object.                                                                                                            | Not applicable. Use [**HeapValidate**](heapvalidate.md) to validate the heap. |
| [**GlobalFree**](globalfree.md), [**LocalFree**](localfree.md)             | Frees the specified global memory object.                                                                                                                                | [**HeapFree**](heapfree.md)                                                   |
| [**GlobalHandle**](globalhandle.md), [**LocalHandle**](localhandle.md)     | Retrieves the handle associated with the specified pointer to a global memory block. This function should be used only with OLE and clipboard functions that require it. | Not applicable.                                                                |
| [**GlobalLock**](globallock.md), [**LocalLock**](locallock.md)             | Locks a global memory object and returns a pointer to the first byte of the object's memory block.                                                                       | Not applicable.                                                                |
| [**GlobalReAlloc**](globalrealloc.md), [**LocalReAlloc**](localrealloc.md) | Changes the size or attributes of a specified global memory object.                                                                                                      | [**HeapReAlloc**](heaprealloc.md)                                             |
| [**GlobalSize**](globalsize.md), [**LocalSize**](localsize.md)             | Retrieves the current size of the specified global memory object.                                                                                                        | [**HeapSize**](heapsize.md)                                                   |
| [**GlobalUnlock**](globalunlock.md), [**LocalUnlock**](localunlock.md)     | Decrements the lock count associated with a memory object. This function should be used only with OLE and clipboard functions that require it.                           | Not applicable.                                                                |



 

## Bad Memory Functions

The following are the bad memory functions.



| Function                                                                         | Description                                                                                                                                                                                        |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [*BadMemoryCallbackRoutine*](badmemorycallbackroutine.md)                       | An application-defined function registered with the [**RegisterBadMemoryNotification**](registerbadmemorynotification.md) function that is called when one or more bad memory pages are detected. |
| [**GetMemoryErrorHandlingCapabilities**](getmemoryerrorhandlingcapabilities.md) | Gets the memory error handling capabilities of the system.                                                                                                                                         |
| [**RegisterBadMemoryNotification**](registerbadmemorynotification.md)           | Registers a bad memory notification that is called when one or more bad memory pages are detected.                                                                                                 |
| [**UnregisterBadMemoryNotification**](unregisterbadmemorynotification.md)       | Closes the specified bad memory notification handle.                                                                                                                                               |



 

## Enclave Functions

The following are the enclave functions.



| Function                                                 | Description                                                                                                                                                                                                         |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateEnclave**](createenclave.md)                   | Creates a new uninitialized enclave. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave. |
| [**InitializeEnclave**](initializeenclave.md)           | Initializes an enclave that you created and loaded with data.                                                                                                                                                       |
| [**IsEnclaveTypeSupported**](isenclavetypesupported.md) | Retrieves whether the specified type of enclave is supported.                                                                                                                                                       |
| [**LoadEnclaveData**](loadenclavedata.md)               | Loads data into an uninitialized enclave that you created by calling [**CreateEnclave**](createenclave.md).                                                                                                        |



 

## Obsolete Functions

The following functions are provided only for compatibility with 16-bit versions of Windows:

-   [**IsBadCodePtr**](isbadcodeptr.md)
-   [**IsBadReadPtr**](isbadreadptr.md)
-   [**IsBadStringPtr**](isbadstringptr.md)
-   [**IsBadWritePtr**](isbadwriteptr.md)

The following function can return incorrect information and should not be used. Use the [**GlobalMemoryStatusEx**](globalmemorystatusex.md) function instead:

-   [**GlobalMemoryStatus**](globalmemorystatus.md)

 

 



