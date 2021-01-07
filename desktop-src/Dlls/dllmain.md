---
description: An optional entry point into a dynamic-link library (DLL). When the system starts or terminates a process or thread, it calls the entry-point function for each loaded DLL using the first thread of the process.
ms.assetid: 0c3e3083-9297-4626-b2a7-0062d1c2cf9e
title: DllMain entry point (Process.h)
ms.topic: reference
ms.date: 07/22/2020
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DllMain
api_type: 
- UserDefined
api_location: 
- process.h
---

# DllMain entry point

An optional entry point into a dynamic-link library (DLL). When the system starts or terminates a process or thread, it calls the entry-point function for each loaded DLL using the first thread of the process. The system also calls the entry-point function for a DLL when it is loaded or unloaded using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) functions.

## Example

```cpp
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

This is an example from the [Dynamic-Link Library Entry-Point Function](dynamic-link-library-entry-point-function.md).


> [!WARNING]
> There are significant limits on what you can safely do in a DLL entry point. See [General Best Practices](dynamic-link-library-best-practices.md) for specific Windows APIs that are unsafe to call in DllMain. If you need anything but the simplest initialization then do that in an initialization function for the DLL. You can require applications to call the initialization function after DllMain has run and before they call any other functions in the DLL.

 

## Syntax


```C++
BOOL WINAPI DllMain(
  _In_ HINSTANCE hinstDLL,
  _In_ DWORD     fdwReason,
  _In_ LPVOID    lpvReserved
);
```



## Parameters

<dl> <dt>

*hinstDLL* \[in\]
</dt> <dd>

A handle to the DLL module. The value is the base address of the DLL. The **HINSTANCE** of a DLL is the same as the **HMODULE** of the DLL, so *hinstDLL* can be used in calls to functions that require a module handle.

</dd> <dt>

*fdwReason* \[in\]
</dt> <dd>

The reason code that indicates why the DLL entry-point function is being called. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DLL_PROCESS_ATTACH"></span><span id="dll_process_attach"></span><dl> <dt>**DLL\_PROCESS\_ATTACH**</dt> <dt>1</dt> </dl> | The DLL is being loaded into the virtual address space of the current process as a result of the process starting up or as a result of a call to [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya). DLLs can use this opportunity to initialize any instance data or to use the [**TlsAlloc**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-tlsalloc) function to allocate a thread local storage (TLS) index.<br/> The *lpReserved* parameter indicates whether the DLL is being loaded statically or dynamically.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <span id="DLL_PROCESS_DETACH"></span><span id="dll_process_detach"></span><dl> <dt>**DLL\_PROCESS\_DETACH**</dt> <dt>0</dt> </dl> | The DLL is being unloaded from the virtual address space of the calling process because it was loaded unsuccessfully or the reference count has reached zero (the processes has either terminated or called [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) one time for each time it called [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya)).<br/> The *lpReserved* parameter indicates whether the DLL is being unloaded as a result of a [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) call, a failure to load, or process termination.<br/> The DLL can use this opportunity to call the [**TlsFree**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-tlsfree) function to free any TLS indices allocated by using [**TlsAlloc**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-tlsalloc) and to free any thread local data.<br/> Note that the thread that receives the **DLL\_PROCESS\_DETACH** notification is not necessarily the same thread that received the **DLL\_PROCESS\_ATTACH** notification.<br/> |
| <span id="DLL_THREAD_ATTACH"></span><span id="dll_thread_attach"></span><dl> <dt>**DLL\_THREAD\_ATTACH**</dt> <dt>2</dt> </dl>    | The current process is creating a new thread. When this occurs, the system calls the entry-point function of all DLLs currently attached to the process. The call is made in the context of the new thread. DLLs can use this opportunity to initialize a TLS slot for the thread. A thread calling the DLL entry-point function with **DLL\_PROCESS\_ATTACH** does not call the DLL entry-point function with **DLL\_THREAD\_ATTACH**. <br/> Note that a DLL's entry-point function is called with this value only by threads created after the DLL is loaded by the process. When a DLL is loaded using [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya), existing threads do not call the entry-point function of the newly loaded DLL.<br/>                                                                                                                                                                       |
| <span id="DLL_THREAD_DETACH"></span><span id="dll_thread_detach"></span><dl> <dt>**DLL\_THREAD\_DETACH**</dt> <dt>3</dt> </dl>    | A thread is exiting cleanly. If the DLL has stored a pointer to allocated memory in a TLS slot, it should use this opportunity to free the memory. The system calls the entry-point function of all currently loaded DLLs with this value. The call is made in the context of the exiting thread.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |



 

</dd> <dt>

*lpvReserved* \[in\]
</dt> <dd>

If *fdwReason* is **DLL\_PROCESS\_ATTACH**, *lpvReserved* is **NULL** for dynamic loads and non-NULL for static loads.

If *fdwReason* is **DLL\_PROCESS\_DETACH**, *lpvReserved* is **NULL** if [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) has been called or the DLL load failed and non-**NULL** if the process is terminating.

</dd> </dl>

## Return value

When the system calls the **DllMain** function with the **DLL\_PROCESS\_ATTACH** value, the function returns **TRUE** if it succeeds or **FALSE** if initialization fails. If the return value is **FALSE** when **DllMain** is called because the process uses the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) function, **LoadLibrary** returns NULL. (The system immediately calls your entry-point function with **DLL\_PROCESS\_DETACH** and unloads the DLL.) If the return value is **FALSE** when **DllMain** is called during process initialization, the process terminates with an error. To get extended error information, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror).

When the system calls the **DllMain** function with any value other than **DLL\_PROCESS\_ATTACH**, the return value is ignored.

## Remarks

**DllMain** is a placeholder for the library-defined function name. You must specify the actual name you use when you build your DLL. For more information, see the documentation included with your development tools.

During initial process startup or after a call to [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya), the system scans the list of loaded DLLs for the process. For each DLL that has not already been called with the **DLL\_PROCESS\_ATTACH** value, the system calls the DLL's entry-point function. This call is made in the context of the thread that caused the process address space to change, such as the primary thread of the process or the thread that called **LoadLibrary**. Access to the entry point is serialized by the system on a process-wide basis. Threads in *DllMain* hold the loader lock so no additional DLLs can be dynamically loaded or initialized.

If the DLL's entry-point function returns FALSE following a **DLL\_PROCESS\_ATTACH** notification, it receives a **DLL\_PROCESS\_DETACH** notification and the DLL is unloaded immediately. However, if the **DLL\_PROCESS\_ATTACH** code throws an exception, the entry-point function will not receive the **DLL\_PROCESS\_DETACH** notification.

There are cases in which the entry-point function is called for a terminating thread even if the entry-point function was never called with **DLL\_THREAD\_ATTACH** for the thread:

-   The thread was the initial thread in the process, so the system called the entry-point function with the **DLL\_PROCESS\_ATTACH** value.
-   The thread was already running when a call to the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) function was made, so the system never called the entry-point function for it.

When a DLL is unloaded from a process as a result of an unsuccessful load of the DLL, termination of the process, or a call to [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary), the system does not call the DLL's entry-point function with the **DLL\_THREAD\_DETACH** value for the individual threads of the process. The DLL is only sent a **DLL\_PROCESS\_DETACH** notification. DLLs can take this opportunity to clean up all resources for all threads known to the DLL.

When handling **DLL\_PROCESS\_DETACH**, a DLL should free resources such as heap memory only if the DLL is being unloaded dynamically (the *lpReserved* parameter is **NULL**). If the process is terminating (the *lpvReserved* parameter is non-**NULL**), all threads in the process except the current thread either have exited already or have been explicitly terminated by a call to the [**ExitProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-exitprocess) function, which might leave some process resources such as heaps in an inconsistent state. In this case, it is not safe for the DLL to clean up the resources. Instead, the DLL should allow the operating system to reclaim the memory.

If you terminate a process by calling [**TerminateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminateprocess) or [**TerminateJobObject**](/windows/desktop/api/jobapi2/nf-jobapi2-terminatejobobject), the DLLs of that process do not receive **DLL\_PROCESS\_DETACH** notifications. If you terminate a thread by calling [**TerminateThread**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-terminatethread), the DLLs of that thread do not receive **DLL\_THREAD\_DETACH** notifications.

The entry-point function should perform only simple initialization or termination tasks. It must not call the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa) function (or a function that calls these functions), because this may create dependency loops in the DLL load order. This can result in a DLL being used before the system has executed its initialization code. Similarly, the entry-point function must not call the [**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) function (or a function that calls **FreeLibrary**) during process termination, because this can result in a DLL being used after the system has executed its termination code.

Because Kernel32.dll is guaranteed to be loaded in the process address space when the entry-point function is called, calling functions in Kernel32.dll does not result in the DLL being used before its initialization code has been executed. Therefore, the entry-point function can call functions in Kernel32.dll that do not load other DLLs. For example, *DllMain* can create [synchronization objects](/windows/desktop/Sync/synchronization-objects) such as critical sections and mutexes, and use TLS. Unfortunately, there is not a comprehensive list of safe functions in Kernel32.dll.

Calling functions that require DLLs other than Kernel32.dll may result in problems that are difficult to diagnose. For example, calling User, Shell, and COM functions can cause access violation errors, because some functions load other system components. Conversely, calling functions such as these during termination can cause access violation errors because the corresponding component may already have been unloaded or uninitialized.

Because DLL notifications are serialized, entry-point functions should not attempt to communicate with other threads or processes. Deadlocks may occur as a result.

For information on best practices when writing a DLL, see https://docs.microsoft.com/windows/win32/dlls/dynamic-link-library-best-practices.

If your DLL is linked with the C run-time library (CRT), the entry point provided by the CRT calls the constructors and destructors for global and static C++ objects. Therefore, these restrictions for *DllMain* also apply to constructors and destructors and any code that is called from them.

Consider calling [**DisableThreadLibraryCalls**](/windows/win32/api/libloaderapi/nf-libloaderapi-disablethreadlibrarycalls) when receiving **DLL\_PROCESS\_ATTACH**, unless your DLL is linked with static C run-time library (CRT).


## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Process.h</dt> </dl> |



## See also

<dl> <dt>

[Dynamic-Link Library Entry-Point Function](dynamic-link-library-entry-point-function.md)
</dt> <dt>

[Dynamic-Link Library Functions](dynamic-link-library-functions.md)
</dt> <dt>

[**FreeLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary)
</dt> <dt>

[**GetModuleFileName**](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea)
</dt> <dt>

[**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya)
</dt> <dt>

[**TlsAlloc**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-tlsalloc)
</dt> <dt>

[**TlsFree**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-tlsfree)
</dt> <dt>

[**DisableThreadLibraryCalls**](/windows/win32/api/libloaderapi/nf-libloaderapi-disablethreadlibrarycalls)





</dt> </dl>
