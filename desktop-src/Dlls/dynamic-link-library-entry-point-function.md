---
description: A DLL can optionally specify an entry-point function.
ms.assetid: ec035fc6-0a6f-4e52-a4cc-8d7a25a94366
title: Dynamic-Link Library Entry-Point Function
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic-Link Library Entry-Point Function

A DLL can optionally specify an entry-point function. If present, the system calls the entry-point function whenever a process or thread loads or unloads the DLL. It can be used to perform simple initialization and cleanup tasks. For example, it can set up thread local storage when a new thread is created, and clean it up when the thread is terminated.

If you are linking your DLL with the C run-time library, it may provide an entry-point function for you, and allow you to provide a separate initialization function. Check the documentation for your run-time library for more information.

If you are providing your own entry-point, see the [**DllMain**](dllmain.md) function. The name **DllMain** is a placeholder for a user-defined function. You must specify the actual name you use when you build your DLL. For more information, see the documentation included with your development tools.

## Calling the Entry-Point Function

The system calls the entry-point function whenever any one of the following events occurs:

-   A process loads the DLL. For processes using load-time dynamic linking, the DLL is loaded during process initialization. For processes using run-time linking, the DLL is loaded before [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) returns.
-   A process unloads the DLL. The DLL is unloaded when the process terminates or calls the [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) function and the reference count becomes zero. If the process terminates as a result of the [**TerminateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminateprocess) or [**TerminateThread**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminatethread) function, the system does not call the DLL entry-point function.
-   A new thread is created in a process that has loaded the DLL. You can use the [**DisableThreadLibraryCalls**](/windows/win32/api/libloaderapi/nf-libloaderapi-disablethreadlibrarycalls) function to disable notification when threads are created.
-   A thread of a process that has loaded the DLL terminates normally, not using [**TerminateThread**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminatethread) or [**TerminateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminateprocess). When a process unloads the DLL, the entry-point function is called only once for the entire process, rather than once for each existing thread of the process. You can use [**DisableThreadLibraryCalls**](/windows/win32/api/libloaderapi/nf-libloaderapi-disablethreadlibrarycalls) to disable notification when threads are terminated.

Only one thread at a time can call the entry-point function.

The system calls the entry-point function in the context of the process or thread that caused the function to be called. This allows a DLL to use its entry-point function for allocating memory in the virtual address space of the calling process or to open handles accessible to the process. The entry-point function can also allocate memory that is private to a new thread by using thread local storage (TLS). For more information about thread local storage, see [Thread Local Storage](/windows/desktop/ProcThread/thread-local-storage).

## Entry-Point Function Definition

The DLL entry-point function must be declared with the standard-call calling convention. If the DLL entry point is not declared correctly, the DLL is not loaded, and the system displays a message indicating that the DLL entry point must be declared with WINAPI.

In the body of the function, you may handle any combination of the following scenarios in which the DLL entry point has been called:

-   A process loads the DLL (**DLL\_PROCESS\_ATTACH**).
-   The current process creates a new thread (**DLL\_THREAD\_ATTACH**).
-   A thread exits normally (**DLL\_THREAD\_DETACH**).
-   A process unloads the DLL (**DLL\_PROCESS\_DETACH**).

The entry-point function should perform only simple initialization tasks. It must not call the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function (or a function that calls these functions), because this may create dependency loops in the DLL load order. This can result in a DLL being used before the system has executed its initialization code. Similarly, the entry-point function must not call the [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) function (or a function that calls **FreeLibrary**) during process termination, because this can result in a DLL being used after the system has executed its termination code.

Because Kernel32.dll is guaranteed to be loaded in the process address space when the entry-point function is called, calling functions in Kernel32.dll does not result in the DLL being used before its initialization code has been executed. Therefore, the entry-point function can create [synchronization objects](/windows/desktop/Sync/synchronization-objects) such as critical sections and mutexes, and use TLS, because these functions are located in Kernel32.dll. It is not safe to call the registry functions, for example, because they are located in Advapi32.dll.

Calling other functions may result in problems that are difficult to diagnose. For example, calling User, Shell, and COM functions can cause access violation errors, because some functions in their DLLs call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) to load other system components. Conversely, calling those functions during termination can cause access violation errors because the corresponding component may already have been unloaded or uninitialized.

The following example demonstrates how to structure the DLL entry-point function.

``` syntax
BOOL WINAPI DllMain(
    HINSTANCE hinstDLL,  // handle to DLL module
    DWORD fdwReason,     // reason for calling function
    LPVOID lpReserved )  // reserved
{
    // Perform actions based on the reason for calling.
    switch( fdwReason ) 
    { 
        case DLL_PROCESS_ATTACH:
         // Initialize once for each new process.
         // Return FALSE to fail DLL load.
            break;

        case DLL_THREAD_ATTACH:
         // Do thread-specific initialization.
            break;

        case DLL_THREAD_DETACH:
         // Do thread-specific cleanup.
            break;

        case DLL_PROCESS_DETACH:
         // Perform any necessary cleanup.
            break;
    }
    return TRUE;  // Successful DLL_PROCESS_ATTACH.
}
```

## Entry-Point Function Return Value

When a DLL entry-point function is called because a process is loading, the function returns **TRUE** to indicate success. For processes using load-time linking, a return value of **FALSE** causes the process initialization to fail and the process terminates. For processes using run-time linking, a return value of FALSE causes the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function to return **NULL**, indicating failure. (The system immediately calls your entry-point function with **DLL\_PROCESS\_DETACH** and unloads the DLL.) The return value of the entry-point function is disregarded when the function is called for any other reason.

 

 
