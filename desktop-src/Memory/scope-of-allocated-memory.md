---
Description: 'All memory a process allocates by using the memory allocation functions ( HeapAlloc, VirtualAlloc, GlobalAlloc, or LocalAlloc) is accessible only to the process.'
ms.assetid: 'b47200dc-6824-4fd8-8d9f-2aaa439a74ff'
title: Scope of Allocated Memory
---

# Scope of Allocated Memory

All memory a process allocates by using the memory allocation functions ( [**HeapAlloc**](heapalloc.md), [**VirtualAlloc**](virtualalloc.md), [**GlobalAlloc**](globalalloc.md), or [**LocalAlloc**](localalloc.md)) is accessible only to the process. However, memory allocated by a DLL is allocated in the address space of the process that called the DLL and is not accessible to other processes using the same DLL. To create shared memory, you must use file mapping.

Named file mapping provides an easy way to create a block of shared memory. A process can specify a name when it uses the [**CreateFileMapping**](createfilemapping.md) function to create a file-mapping object. Other processes can specify the same name to either the **CreateFileMapping** or [**OpenFileMapping**](openfilemapping.md) function to obtain a handle to the mapping object.

Each process specifies its handle to the file-mapping object in the [**MapViewOfFile**](mapviewoffile.md) function to map a view of the file into its own address space. The views of all processes for a single file-mapping object are mapped into the same sharable pages of physical storage. However, the virtual addresses of the mapped views can vary from one process to another, unless the [**MapViewOfFileEx**](mapviewoffileex.md) function is used to map the view at a specified address. Although sharable, the pages of physical storage used for a mapped file view are not global; they are not accessible to processes that have not mapped a view of the file.

Any pages committed by mapping a view of a file are released when the last process with a view of the mapping object either terminates or unmaps its view by calling the [**UnmapViewOfFile**](unmapviewoffile.md) function. At this time, the specified file (if any) associated with the mapping object is updated. A specified file can also be forced to update by calling the [**FlushViewOfFile**](flushviewoffile.md) function.

For more information, see [File Mapping](file-mapping.md). For an example of shared memory in a DLL, see [Using Shared Memory in a Dynamic-Link Library](base.using_shared_memory_in_a_dynamic_link_library).

If multiple processes have write access to shared memory, you must synchronize access to the memory. For more information, see [Synchronization](base.synchronization).

 

 



