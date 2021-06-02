---
description: To map the data from a file to the virtual memory of a process, you must create a view of the file.
ms.assetid: b1ebd9a4-cde4-4c0c-80d2-5ccb655cd3a4
title: Creating a File View
ms.topic: article
ms.date: 05/31/2018
---

# Creating a File View

To map the data from a file to the virtual memory of a process, you must create a view of the file. The [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) and [**MapViewOfFileEx**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffileex) functions use the file mapping object handle returned by [**CreateFileMapping**](/windows/desktop/api/WinBase/nf-winbase-createfilemappinga) to create a view of the file or a portion of the file in the process's virtual address space. These functions fail if the access flags conflict with those specified when **CreateFileMapping** created the file mapping object.

The [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) function returns a pointer to the file view. By dereferencing a pointer in the range of addresses specified in **MapViewOfFile**, an application can read data from the file and write data to the file. Writing to the file view results in changes to the file mapping object. The actual writing to the file on disk is handled by the system. Data is not actually transferred at the time the file mapping object is written to. Instead, much of the file input and output (I/O) is cached to improve general system performance. Applications can override this behavior by calling the [**FlushViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-flushviewoffile) function to force the system to perform disk transactions immediately.

The [**MapViewOfFileEx**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffileex) function works exactly like the [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) function except that it allows a process to specify the base address of the view of the file in the process's virtual address space in the *lpvBase* parameter. If there is not enough space at the specified address, the call fails. Therefore, if you must map a file to the same address in multiple processes, the processes should negotiate an appropriate address: The *lpvBase* parameter must be an integral multiple of the system memory allocation granularity or the call fails. To obtain the system's memory allocation granularity, use the [**GetSystemInfo**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsysteminfo) function, which fills in the members of a [**SYSTEM\_INFO**](/windows/win32/api/sysinfoapi/ns-sysinfoapi-system_info) structure.

An application can create multiple file views from the same file mapping object. A file view can be a different size than the file mapping object from which it is derived, but it must be smaller than the file mapping object. The offset specified by the *dwOffsetHigh* and *dwOffsetLow* parameters of [**MapViewOfFile**](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffile) must be a multiple of the allocation granularity of the system.

## Related topics

<dl> <dt>

[Creating a View Within a File](creating-a-view-within-a-file.md)
</dt> </dl>

 

 
