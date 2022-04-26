---
description: 'This topic describes the memory management functions:'
ms.assetid: 5a2a7a62-0bda-4a0d-93d2-25b4898871fd
title: Memory Management Functions
ms.topic: article
ms.date: 11/06/2018
---

# Memory Management Functions

- [General memory functions](#general-memory-functions)
- [Data execution prevention functions](#data-execution-prevention-functions)
- [File mapping functions](#file-mapping-functions)
- [AWE functions](#awe-functions)
- [Heap functions](#heap-functions)
- [Virtual memory functions](#virtual-memory-functions)
- [Global and local functions](#global-and-local-functions)
- [Bad memory functions](#bad-memory-functions)
- [Enclave functions](#enclave-functions)
- [ATL thunk functions](#atl-thunk-functions)
- [Obsolete functions](#obsolete-functions)

## General memory functions

| Function | Description |
|-|-|
| [**AddSecureMemoryCacheCallback**](/windows/desktop/api/WinBase/nf-winbase-addsecurememorycachecallback) | Registers a callback function to be called when a secured memory range is freed or its protections are changed. |
| [**CopyMemory**](/previous-versions/windows/desktop/legacy/aa366535(v=vs.85)) | Copies a block of memory from one location to another. |
| [**CreateMemoryResourceNotification**](/windows/win32/api/memoryapi/nf-memoryapi-creatememoryresourcenotification) | Creates a memory resource notification object. |
| [**FillMemory**](/previous-versions/windows/desktop/legacy/aa366561(v=vs.85)) | Fills a block of memory with a specified value. |
| [**GetLargePageMinimum**](/windows/win32/api/memoryapi/nf-memoryapi-getlargepageminimum) | Retrieves the minimum size of a large page. |
| [**GetPhysicallyInstalledSystemMemory**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getphysicallyinstalledsystemmemory) | Retrieves the amount of RAM that is physically installed on the computer. |
| [**GetSystemFileCacheSize**](/windows/win32/api/memoryapi/nf-memoryapi-getsystemfilecachesize) | Retrieves the current size limits for the working set of the system cache. |
| [**GetWriteWatch**](/windows/win32/api/memoryapi/nf-memoryapi-getwritewatch) | Retrieves the addresses of the pages that have been written to in a region of virtual memory. |
| [**GlobalMemoryStatusEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex) | Obtains information about the system's current usage of both physical and virtual memory. |
| [**MoveMemory**](/previous-versions/windows/desktop/legacy/aa366788(v=vs.85)) | Moves a block of memory from one location to another. |
| [**QueryMemoryResourceNotification**](/windows/win32/api/memoryapi/nf-memoryapi-querymemoryresourcenotification) | Retrieves the state of the specified memory resource object. |
| [**RemoveSecureMemoryCacheCallback**](/windows/desktop/api/WinBase/nf-winbase-removesecurememorycachecallback) | Unregisters a callback function that was previously registered with the [**AddSecureMemoryCacheCallback**](/windows/desktop/api/WinBase/nf-winbase-addsecurememorycachecallback) function. |
| [**ResetWriteWatch**](/windows/win32/api/memoryapi/nf-memoryapi-resetwritewatch) | Resets the write-tracking state for a region of virtual memory. |
| [**SecureMemoryCacheCallback**](/windows/desktop/api/WinNT/nc-winnt-psecure_memory_cache_callback) | An application-defined function that is called when a secured memory range is freed or its protections are changed. |
| [**SecureZeroMemory**](/previous-versions/windows/desktop/legacy/aa366877(v=vs.85)) | Fills a block of memory with zeros. |
| [**SetSystemFileCacheSize**](/windows/win32/api/memoryapi/nf-memoryapi-setsystemfilecachesize) | Limits the size of the working set for the file system cache. |
| [**ZeroMemory**](/previous-versions/windows/desktop/legacy/aa366920(v=vs.85)) | Fills a block of memory with zeros. |

## Data execution prevention functions

These functions are used with [Data Execution Prevention](data-execution-prevention.md) (DEP).

| Function | Description |
|-|-|
| [**GetProcessDEPPolicy**](/windows/desktop/api/WinBase/nf-winbase-getprocessdeppolicy) | Retrieves DEP settings for a process. |
| [**GetSystemDEPPolicy**](/windows/desktop/api/WinBase/nf-winbase-getsystemdeppolicy) | Retrieves DEP settings for the system. |
| [**SetProcessDEPPolicy**](/windows/desktop/api/WinBase/nf-winbase-setprocessdeppolicy) | Changes DEP settings for a process. |

## File mapping functions

These functions are used in [file mapping](file-mapping.md).

| Function | Description |
|-|-|
| [**CreateFileMappingA**](/windows/win32/api/winbase/nf-winbase-createfilemappinga) | Creates or opens a named or unnamed file-mapping object for a specified file. |
| [**CreateFileMappingW**](/windows/win32/api/memoryapi/nf-memoryapi-createfilemappingw) | Creates or opens a named or unnamed file-mapping object for a specified file. |
| [**CreateFileMapping2**](/windows/win32/api/memoryapi/nf-memoryapi-createfilemapping2) | Creates or opens a named or unnamed file mapping object for a specified file. You can specify specify a preferred NUMA node for the physical memory as an extended parameter; see the *ExtendedParameters* parameter. |
| [**CreateFileMappingFromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-createfilemappingfromapp) | Creates or opens a named or unnamed file-mapping object for a specified file from a Windows Store app. |
| [**CreateFileMappingNuma**](/windows/desktop/api/WinBase/nf-winbase-createfilemappingnumaa) | Creates or opens a named or unnamed file-mapping object for a specified file, and specifies the NUMA node for the physical memory. |
| [**FlushViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-flushviewoffile) | Writes to the disk a byte range within a mapped view of a file. |
| [**GetMappedFileName**](/windows/win32/api/psapi/nf-psapi-getmappedfilenamea) | Checks whether the specified address is within a memory-mapped file in the address space of the specified process. If so, the function returns the name of the memory-mapped file. |
| [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) | Maps a view of a file mapping into the address space of a calling process. |
| [**MapViewOfFile2**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile2) | Maps a view of a file or a pagefile-backed section into the address space of the specified process. |
| [**MapViewOfFile3**](/windows/desktop/api/MemoryApi/nf-memoryapi-mapviewoffile3) | Maps a view of a file or a pagefile-backed section into the address space of the specified process. |
| [**MapViewOfFile3FromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-mapviewoffile3fromapp) | Maps a view of a file mapping into the address space of a calling process from a Windows Store app. |
| [**MapViewOfFileEx**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffileex) | Maps a view of a file mapping into the address space of a calling process. A caller can optionally specify a suggested memory address for the view. |
| [**MapViewOfFileExNuma**](/windows/desktop/api/WinBase/nf-winbase-mapviewoffileexnuma) | Maps a view of a file mapping into the address space of a calling process, and specifies the NUMA node for the physical memory. |
| [**MapViewOfFileFromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-mapviewoffilefromapp) | Maps a view of a file mapping into the address space of a calling process from a Windows Store app. |
| [**MapViewOfFileNuma2**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffilenuma2) | Maps a view of a file or a pagefile-backed section into the address space of the specified process. |
| [**OpenFileMapping**](/windows/win32/api/winbase/nf-winbase-openfilemappinga) | Opens a named file-mapping object. |
| [**OpenFileMappingFromApp**](/windows/win32/api/memoryapi/nf-memoryapi-openfilemappingfromapp) | Opens a named file-mapping object. |
| [**UnmapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-unmapviewoffile) | Unmaps a mapped view of a file from the calling process's address space. |
| [**UnmapViewOfFile2**](/windows/win32/api/memoryapi/nf-memoryapi-unmapviewoffile2) | Unmaps a previously mapped view of a file or a pagefile-backed section. |
| [**UnmapViewOfFileEx**](/windows/desktop/api/MemoryApi/nf-memoryapi-unmapviewoffileex) | Unmaps a previously mapped view of a file or a pagefile-backed section. |

## AWE functions

These are the [AWE functions](address-windowing-extensions.md).

| Function | Description |
|-|-|
| [**AllocateUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-allocateuserphysicalpages) | Allocates physical memory pages to be mapped and unmapped within any AWE region of the process. |
| [**AllocateUserPhysicalPagesNuma**](/windows/win32/api/memoryapi/nf-memoryapi-allocateuserphysicalpagesnuma) | Allocates physical memory pages to be mapped and unmapped within any AWE region of the process, and specifies the NUMA node for the physical memory. |
| [**FreeUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-freeuserphysicalpages) | Frees physical memory pages previously allocated with [**AllocateUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-allocateuserphysicalpages). |
| [**MapUserPhysicalPages**](/windows/win32/api/memoryapi/nf-memoryapi-mapuserphysicalpages) | Maps previously allocated physical memory pages at the specified address within an AWE region. |
| [**MapUserPhysicalPagesScatter**](/windows/desktop/api/WinBase/nf-winbase-mapuserphysicalpagesscatter) | Maps previously allocated physical memory pages at the specified address within an AWE region. |

## Heap functions

These are the [heap functions](heap-functions.md).

| Function | Description |
|-|-|
| [**GetProcessHeap**](/windows/desktop/api/HeapApi/nf-heapapi-getprocessheap) | Obtains a handle to the heap of the calling process. |
| [**GetProcessHeaps**](/windows/desktop/api/HeapApi/nf-heapapi-getprocessheaps) | Obtains handles to all of the heaps that are valid for the calling process. |
| [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) | Allocates a block of memory from a heap. |
| [**HeapCompact**](/windows/desktop/api/HeapApi/nf-heapapi-heapcompact) | Coalesces adjacent free blocks of memory on a heap. |
| [**HeapCreate**](/windows/desktop/api/HeapApi/nf-heapapi-heapcreate) | Creates a heap object. |
| [**HeapDestroy**](/windows/desktop/api/HeapApi/nf-heapapi-heapdestroy) | Destroys the specified heap object. |
| [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree) | Frees a memory block allocated from a heap. |
| [**HeapLock**](/windows/desktop/api/HeapApi/nf-heapapi-heaplock) | Attempts to acquire the lock associated with a specified heap. |
| [**HeapQueryInformation**](/windows/desktop/api/HeapApi/nf-heapapi-heapqueryinformation) | Retrieves information about the specified heap. |
| [**HeapReAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heaprealloc) | Reallocates a block of memory from a heap. |
| [**HeapSetInformation**](/windows/desktop/api/HeapApi/nf-heapapi-heapsetinformation) | Sets heap information for the specified heap. |
| [**HeapSize**](/windows/desktop/api/HeapApi/nf-heapapi-heapsize) | Retrieves the size of a memory block allocated from a heap. |
| [**HeapUnlock**](/windows/desktop/api/HeapApi/nf-heapapi-heapunlock) | Releases ownership of the lock associated with a specified heap. |
| [**HeapValidate**](/windows/desktop/api/HeapApi/nf-heapapi-heapvalidate) | Attempts to validate a specified heap. |
| [**HeapWalk**](/windows/desktop/api/HeapApi/nf-heapapi-heapwalk) | Enumerates the memory blocks in a specified heap. |

## Virtual memory functions

These are the [virtual memory functions](virtual-memory-functions.md).

| Function | Description |
|-|-|
| [**DiscardVirtualMemory**](/windows/win32/api/memoryapi/nf-memoryapi-discardvirtualmemory) | Discards the memory contents of a range of memory pages, without decommitting the memory. The contents of discarded memory is undefined and must be rewritten by the application. |
| [**OfferVirtualMemory**](/windows/win32/api/memoryapi/nf-memoryapi-offervirtualmemory) | Indicates that the data contained in a range of memory pages is no longer needed by the application and can be discarded by the system if necessary. |
| [**PrefetchVirtualMemory**](/windows/win32/api/memoryapi/nf-memoryapi-prefetchvirtualmemory) | Prefetches virtual address ranges into physical memory. |
| [**QueryVirtualMemoryInformation**](/windows/desktop/api/MemoryApi/nf-memoryapi-queryvirtualmemoryinformation) | Returns information about a page or a set of pages within the virtual address space of the specified process. |
| [**ReclaimVirtualMemory**](/windows/win32/api/memoryapi/nf-memoryapi-reclaimvirtualmemory) | Reclaims a range of memory pages that were offered to the system with [**OfferVirtualMemory**](/windows/win32/api/memoryapi/nf-memoryapi-offervirtualmemory). |
| [**SetProcessValidCallTargets**](/windows/desktop/api/MemoryApi/nf-memoryapi-setprocessvalidcalltargets) | Provides CFG with a list of valid indirect call targets and specifies whether they should be marked valid or not. |
| [**VirtualAlloc**](/windows/desktop/api/MemoryApi/nf-memoryapi-virtualalloc) | Reserves or commits a region of pages in the virtual address space of the calling process. |
| [**VirtualAlloc2**](/windows/desktop/api/MemoryApi/nf-memoryapi-virtualalloc2) | Reserves, commits, or changes the state of a region of memory within the virtual address space of a specified process. The function initializes the memory it allocates to zero. |
| [**VirtualAlloc2FromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-virtualallocfromapp) | Reserves, commits, or changes the state of a region of pages in the virtual address space of the calling process. Memory allocated by this function is automatically initialized to zero. |
| [**VirtualAllocEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex) | Reserves or commits a region of pages in the virtual address space of the specified process. |
| [**VirtualAllocExNuma**](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocexnuma) | Reserves or commits a region of memory within the virtual address space of the specified process, and specifies the NUMA node for the physical memory. |
| [**VirtualAllocFromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-virtualallocfromapp) | Reserves, commits, or changes the state of a region of pages in the virtual address space of the calling process. Memory allocated by this function is automatically initialized to zero. |
| [**VirtualFree**](/windows/win32/api/memoryapi/nf-memoryapi-virtualfree) | Releases or decommits a region of pages within the virtual address space of the calling process. |
| [**VirtualFreeEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualfreeex) | Releases or decommits a region of memory within the virtual address space of a specified process. |
| [**VirtualLock**](/windows/win32/api/memoryapi/nf-memoryapi-virtuallock) | Locks the specified region of the process's virtual address space into physical memory. |
| [**VirtualProtect**](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotect) | Changes the access protection on a region of committed pages in the virtual address space of the calling process. |
| [**VirtualProtectEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotectex) | Changes the access protection on a region of committed pages in the virtual address space of the calling process. |
| [**VirtualProtectFromApp**](/windows/desktop/api/MemoryApi/nf-memoryapi-virtualprotectfromapp) | Changes the protection on a region of committed pages in the virtual address space of the calling process. |
| [**VirtualQuery**](/windows/win32/api/memoryapi/nf-memoryapi-virtualquery) | Provides information about a range of pages in the virtual address space of the calling process. |
| [**VirtualQueryEx**](/windows/win32/api/memoryapi/nf-memoryapi-virtualqueryex) | Provides information about a range of pages in the virtual address space of the calling process. |
| [**VirtualUnlock**](/windows/win32/api/memoryapi/nf-memoryapi-virtualunlock) | Unlocks a specified range of pages in the virtual address space of a process. |

## Global and local functions

Also see [global and local functions](global-and-local-functions.md). These functions are provided for compatibility with 16-bit Windows and are used with Dynamic Data Exchange (DDE), the clipboard functions, and OLE data objects. Unless documentation specifically states that a global or local function should be used, new applications should use the corresponding [heap function](heap-functions.md) with the handle returned by [**GetProcessHeap**](/windows/desktop/api/HeapApi/nf-heapapi-getprocessheap). For equivalent functionality to the global or local function, set the heap function's *dwFlags* parameter to 0.

| Function | Description | Corresponding heap function |
|-|-|-|
| [**GlobalAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalalloc), [**LocalAlloc**](/windows/desktop/api/WinBase/nf-winbase-localalloc) | Allocates the specified number of bytes from the heap. | [**HeapAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heapalloc) |
| [**GlobalDiscard**](/windows/desktop/api/WinBase/nf-winbase-globaldiscard), [**LocalDiscard**](/windows/win32/api/minwinbase/nf-minwinbase-localdiscard) | Discards the specified global memory block. | Not applicable. |
| [**GlobalFlags**](/windows/desktop/api/WinBase/nf-winbase-globalflags), [**LocalFlags**](/windows/desktop/api/WinBase/nf-winbase-localflags) | Returns information about the specified global memory object. | Not applicable. Use [**HeapValidate**](/windows/desktop/api/HeapApi/nf-heapapi-heapvalidate) to validate the heap. |
| [**GlobalFree**](/windows/desktop/api/WinBase/nf-winbase-globalfree), [**LocalFree**](/windows/desktop/api/WinBase/nf-winbase-localfree) | Frees the specified global memory object. | [**HeapFree**](/windows/desktop/api/HeapApi/nf-heapapi-heapfree) |
| [**GlobalHandle**](/windows/desktop/api/WinBase/nf-winbase-globalhandle), [**LocalHandle**](/windows/desktop/api/WinBase/nf-winbase-localhandle) | Retrieves the handle associated with the specified pointer to a global memory block. This function should be used only with OLE and clipboard functions that require it. | Not applicable. |
| [**GlobalLock**](/windows/desktop/api/WinBase/nf-winbase-globallock), [**LocalLock**](/windows/desktop/api/WinBase/nf-winbase-locallock) | Locks a global memory object and returns a pointer to the first byte of the object's memory block. | Not applicable. |
| [**GlobalReAlloc**](/windows/desktop/api/WinBase/nf-winbase-globalrealloc), [**LocalReAlloc**](/windows/desktop/api/WinBase/nf-winbase-localrealloc) | Changes the size or attributes of a specified global memory object. | [**HeapReAlloc**](/windows/desktop/api/HeapApi/nf-heapapi-heaprealloc) |
| [**GlobalSize**](/windows/desktop/api/WinBase/nf-winbase-globalsize), [**LocalSize**](/windows/desktop/api/WinBase/nf-winbase-localsize) | Retrieves the current size of the specified global memory object. | [**HeapSize**](/windows/desktop/api/HeapApi/nf-heapapi-heapsize) |
| [**GlobalUnlock**](/windows/desktop/api/WinBase/nf-winbase-globalunlock), [**LocalUnlock**](/windows/desktop/api/WinBase/nf-winbase-localunlock) | Decrements the lock count associated with a memory object. This function should be used only with OLE and clipboard functions that require it. | Not applicable. |

## Bad memory functions

| Function | Description |
|-|-|
| [**BadMemoryCallbackRoutine**](/previous-versions/windows/desktop/legacy/hh691011(v=vs.85)) | An application-defined function registered with the [**RegisterBadMemoryNotification**](/windows/win32/api/memoryapi/nf-memoryapi-registerbadmemorynotification) function that is called when one or more bad memory pages are detected. |
| [**GetMemoryErrorHandlingCapabilities**](/windows/win32/api/memoryapi/nf-memoryapi-getmemoryerrorhandlingcapabilities) | Gets the memory error handling capabilities of the system. |
| [**RegisterBadMemoryNotification**](/windows/win32/api/memoryapi/nf-memoryapi-registerbadmemorynotification) | Registers a bad memory notification that is called when one or more bad memory pages are detected. |
| [**UnregisterBadMemoryNotification**](/windows/win32/api/memoryapi/nf-memoryapi-unregisterbadmemorynotification) | Closes the specified bad memory notification handle. |

## Enclave functions

| Function | Description |
|-|-|
| [**CreateEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-createenclave) | Creates a new uninitialized enclave. An enclave is an isolated region of code and data within the address space for an application. Only code that runs within the enclave can access data within the same enclave. |
| [**InitializeEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-initializeenclave) | Initializes an enclave that you created and loaded with data. |
| [**IsEnclaveTypeSupported**](/windows/desktop/api/enclaveapi/nf-enclaveapi-isenclavetypesupported) | Retrieves whether the specified type of enclave is supported. |
| [**LoadEnclaveData**](/windows/desktop/api/enclaveapi/nf-enclaveapi-loadenclavedata) | Loads data into an uninitialized enclave that you created by calling [**CreateEnclave**](/windows/desktop/api/enclaveapi/nf-enclaveapi-createenclave). |

## ATL thunk functions

| Function | Description |
|-|-|
| [**AtlThunk_AllocateData**](/windows/desktop/api/atlthunk/nf-atlthunk-atlthunk_allocatedata) | Allocates space in memory for an ATL thunk. |
| [**AtlThunk_DataToCode**](/windows/desktop/api/atlthunk/nf-atlthunk-atlthunk_datatocode) | Returns an executable function corresponding to the AtlThunkData_t parameter. |
| [**AtlThunk_FreeData**](/windows/desktop/api/atlthunk/nf-atlthunk-atlthunk_freedata) | Frees memory associated with an ATL thunk. |
| [**AtlThunk_InitData**](/windows/desktop/api/atlthunk/nf-atlthunk-atlthunk_initdata) | Initializes an ATL thunk. |

## Obsolete Functions

These functions are provided only for compatibility with 16-bit versions of Windows:

- [**IsBadCodePtr**](/windows/desktop/api/WinBase/nf-winbase-isbadcodeptr)
- [**IsBadReadPtr**](/windows/desktop/api/WinBase/nf-winbase-isbadreadptr)
- [**IsBadStringPtr**](/windows/desktop/api/WinBase/nf-winbase-isbadstringptra)
- [**IsBadWritePtr**](/windows/desktop/api/WinBase/nf-winbase-isbadwriteptr)

The function below can return incorrect information, and should not be used. Instead, use the [**GlobalMemoryStatusEx**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex) function.

- [**GlobalMemoryStatus**](/windows/desktop/api/WinBase/nf-winbase-globalmemorystatus)
