---
description: When the application calls the LoadLibrary or LoadLibraryEx functions, the system attempts to locate the DLL (for details, see Dynamic-Link Library Search Order).
ms.assetid: 81e237a9-3c32-46a5-88d3-c978f43dad54
title: Run-Time Dynamic Linking
ms.topic: article
ms.date: 05/31/2018
---

# Run-Time Dynamic Linking

When the application calls the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) functions, the system attempts to locate the DLL (for details, see [Dynamic-Link Library Search Order](dynamic-link-library-search-order.md)). If the search succeeds, the system maps the DLL module into the virtual address space of the process and increments the reference count. If the call to **LoadLibrary** or **LoadLibraryEx** specifies a DLL whose code is already mapped into the virtual address space of the calling process, the function simply returns a handle to the DLL and increments the DLL reference count. Note that two DLLs that have the same base file name and extension but are found in different directories are not considered to be the same DLL.

The system calls the entry-point function in the context of the thread that called [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa). The entry-point function is not called if the DLL was already loaded by the process through a call to **LoadLibrary** or **LoadLibraryEx** with no corresponding call to the [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) function.

If the system cannot find the DLL or if the entry-point function returns FALSE, [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) returns NULL. If **LoadLibrary** or **LoadLibraryEx** succeeds, it returns a handle to the DLL module. The process can use this handle to identify the DLL in a call to the [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress), [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary), or [**FreeLibraryAndExitThread**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibraryandexitthread) function.

The [**GetModuleHandle**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlea) function returns a handle used in [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress), [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary), or [**FreeLibraryAndExitThread**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibraryandexitthread). The **GetModuleHandle** function succeeds only if the DLL module is already mapped into the address space of the process by load-time linking or by a previous call to [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa). Unlike **LoadLibrary** or **LoadLibraryEx**, **GetModuleHandle** does not increment the module reference count. The [**GetModuleFileName**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea) function retrieves the full path of the module associated with a handle returned by **GetModuleHandle**, **LoadLibrary**, or **LoadLibraryEx**.

The process can use [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) to get the address of an exported function in the DLL using a DLL module handle returned by [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa), [**GetModuleHandle**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulehandlea).

When the DLL module is no longer needed, the process can call [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) or [**FreeLibraryAndExitThread**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibraryandexitthread). These functions decrement the module reference count and unmap the DLL code from the virtual address space of the process if the reference count is zero.

Run-time dynamic linking enables the process to continue running even if a DLL is not available. The process can then use an alternate method to accomplish its objective. For example, if a process is unable to locate one DLL, it can try to use another, or it can notify the user of an error. If the user can provide the full path of the missing DLL, the process can use this information to load the DLL even though it is not in the normal search path. This situation contrasts with load-time linking, in which the system simply terminates the process if it cannot find the DLL.

Run-time dynamic linking can cause problems if the DLL uses the [**DllMain**](dllmain.md) function to perform initialization for each thread of a process, because the entry-point is not called for threads that existed before [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) is called. For an example showing how to deal with this problem, see [Using Thread Local Storage in a Dynamic-Link Library](using-thread-local-storage-in-a-dynamic-link-library.md).

## Related topics

<dl> <dt>

[Using Run-time Dynamic Linking](using-run-time-dynamic-linking.md)
</dt> </dl>

 

 
