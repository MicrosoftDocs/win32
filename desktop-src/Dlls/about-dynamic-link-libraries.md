---
description: Dynamic linking allows a module to include only the information needed to locate an exported DLL function at load time or run time.
ms.assetid: df2a8e4c-7ad0-46ea-9643-1528a9ea1503
title: About Dynamic-Link Libraries
ms.topic: article
ms.date: 05/31/2018
---

# About Dynamic-Link Libraries

Dynamic linking allows a module to include only the information needed to locate an exported DLL function at load time or run time. Dynamic linking differs from the more familiar static linking, in which the linker copies a library function's code into each module that calls it.

## Types of Dynamic Linking

There are two methods for calling a function in a DLL:

-   In *load-time dynamic linking*, a module makes explicit calls to exported DLL functions as if they were local functions. This requires you to link the module with the import library for the DLL that contains the functions. An import library supplies the system with the information needed to load the DLL and locate the exported DLL functions when the application is loaded.
-   In *run-time dynamic linking*, a module uses the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function to load the DLL at run time. After the DLL is loaded, the module calls the [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) function to get the addresses of the exported DLL functions. The module calls the exported DLL functions using the function pointers returned by **GetProcAddress**. This eliminates the need for an import library.

## DLLs and Memory Management

Every process that loads the DLL maps it into its virtual address space. After the process loads the DLL into its virtual address, it can call the exported DLL functions.

The system maintains a per-process reference count for each DLL. When a thread loads the DLL, the reference count is incremented by one. When the process terminates, or when the reference count becomes zero (run-time dynamic linking only), the DLL is unloaded from the virtual address space of the process.

Like any other function, an exported DLL function runs in the context of the thread that calls it. Therefore, the following conditions apply:

-   The threads of the process that called the DLL can use handles opened by a DLL function. Similarly, handles opened by any thread of the calling process can be used in the DLL function.
-   The DLL uses the stack of the calling thread and the virtual address space of the calling process.
-   The DLL allocates memory from the virtual address space of the calling process.

For more information about DLLs, see the following topics:

-   [Advantages of Dynamic Linking](advantages-of-dynamic-linking.md)
-   [Dynamic-Link Library Creation](dynamic-link-library-creation.md)
-   [Dynamic-Link Library Entry-Point Function](dynamic-link-library-entry-point-function.md)
-   [Load-Time Dynamic Linking](load-time-dynamic-linking.md)
-   [Run-Time Dynamic Linking](run-time-dynamic-linking.md)
-   [Dynamic-Link Library Search Order](dynamic-link-library-search-order.md)
-   [Dynamic-Link Library Data](dynamic-link-library-data.md)
-   [Dynamic-Link Library Redirection](dynamic-link-library-redirection.md)
-   [Dynamic-Link Library Updates](dynamic-link-library-updates.md)
-   [Dynamic-Link Library Security](dynamic-link-library-security.md)
-   [AppInit DLLs and Secure Boot](secure-boot-and-appinit-dlls.md)

 

 
