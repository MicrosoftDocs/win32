---
Description: A Dynamic-Link Library (DLL) can contain global data or local data.
ms.assetid: b1f6811e-c413-4124-9ccb-ea59b7a8a7ff
title: Dynamic-Link Library Data
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Dynamic-Link Library Data

A Dynamic-Link Library (DLL) can contain global data or local data.

## Variable Scope

Variables that are declared as global in a DLL source code file are treated as global variables by the compiler and linker, but each process that loads a given DLL gets its own copy of that DLL's global variables. The scope of static variables is limited to the block in which the static variables are declared. As a result, each process has its own instance of the DLL global and static variables by default.

> [!Note]  
> Your development tools may allow you to override the default behavior. For example, the Visual C++ compiler supports **\#pragma section** and the linker supports the /SECTION option. For more information, see the documentation included with your development tools.

 

## Dynamic Memory Allocation

When a DLL allocates memory using any of the memory allocation functions ([**GlobalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366574), [**LocalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366723), [**HeapAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366597), and [**VirtualAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366887)), the memory is allocated in the virtual address space of the calling process and is accessible only to the threads of that process.

A DLL can use file mapping to allocate memory that can be shared among processes. For a general discussion of how to use file mapping to create named shared memory, see [File Mapping](https://msdn.microsoft.com/library/windows/desktop/aa366556). For an example that uses the [**DllMain**](dllmain.md) function to set up shared memory using file mapping, see [Using Shared Memory in a Dynamic-Link Library](using-shared-memory-in-a-dynamic-link-library.md).

## Thread Local Storage

The thread local storage (TLS) functions enable a DLL to allocate an index for storing and retrieving a different value for each thread of a multithreaded process. For example, a spreadsheet application can create a new instance of the same thread each time the user opens a new spreadsheet. A DLL providing the functions for various spreadsheet operations can use TLS to save information about the current state of each spreadsheet (row, column, and so on). For a general discussion of thread local storage, see [Thread Local Storage](https://msdn.microsoft.com/library/windows/desktop/ms686749). For an example that uses the [**DllMain**](dllmain.md) function to set up thread local storage, see [Using Thread Local Storage in a Dynamic-Link Library](using-thread-local-storage-in-a-dynamic-link-library.md).

**Windows Server 2003 and Windows XP:** The Visual C++ compiler supports a syntax that enables you to declare thread-local variables: **\_declspec(thread)**. If you use this syntax in a DLL, you will not be able to load the DLL explicitly using [**LoadLibrary**](loadlibrary.md) or [**LoadLibraryEx**](/windows/win32/LibLoaderAPI/nf-libloaderapi-loadlibraryexa?branch=master) on versions of Windows prior to Windows Vista. If your DLL will be loaded explicitly, you must use the thread local storage functions instead of **\_declspec(thread)**.

 

 



