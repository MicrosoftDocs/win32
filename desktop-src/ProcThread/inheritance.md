---
description: A child process can inherit several properties and resources from its parent process.
ms.assetid: c530e723-2d40-4022-a259-dfc650604e44
title: Inheritance (Processes and Threads)
ms.topic: article
ms.date: 05/31/2018
---

# Inheritance

A child process can inherit several properties and resources from its parent process. You can also prevent a child process from inheriting properties from its parent process. The following can be inherited:

-   Open handles returned by the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function. This includes handles to files, console input buffers, console screen buffers, named pipes, serial communication devices, and mailslots.
-   Open handles to process, thread, mutex, event, semaphore, named-pipe, anonymous-pipe, and file-mapping objects. These are returned by the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa), [**CreateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread), [**CreateMutex**](/windows/desktop/api/synchapi/nf-synchapi-createmutexa), [**CreateEvent**](/windows/desktop/api/synchapi/nf-synchapi-createeventa), [**CreateSemaphore**](/windows/desktop/api/winbase/nf-winbase-createsemaphorea), [**CreateNamedPipe**](/windows/desktop/api/winbase/nf-winbase-createnamedpipea), [**CreatePipe**](/windows/desktop/api/namedpipeapi/nf-namedpipeapi-createpipe), and [**CreateFileMapping**](/windows/desktop/api/winbase/nf-winbase-createfilemappinga) functions, respectively.
-   Environment variables.
-   The current directory.
-   The console, unless the process is detached or a new console is created. A child console process can also inherit the parent's standard handles, as well as access to the input buffer and the active screen buffer.
-   The error mode, as set by the [**SetErrorMode**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-seterrormode) function.
-   The processor affinity mask.
-   The association with a job.

The child process does not inherit the following:

-   Priority class.
-   Handles returned by [**LocalAlloc**](/windows/desktop/api/winbase/nf-winbase-localalloc), [**GlobalAlloc**](/windows/desktop/api/winbase/nf-winbase-globalalloc), [**HeapCreate**](/windows/desktop/api/heapapi/nf-heapapi-heapcreate), and [**HeapAlloc**](/windows/desktop/api/heapapi/nf-heapapi-heapalloc).
-   Pseudo handles, as in the handles returned by the [**GetCurrentProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) or [**GetCurrentThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthread) function. These handles are valid only for the calling process.
-   DLL module handles returned by the [**LoadLibrary**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibrarya) function.
-   GDI or USER handles, such as **HBITMAP** or **HMENU**.

## Inheriting Handles

A child process can inherit some of its parent's handles, but not inherit others. To cause a handle to be inherited, you must do two things:

-   Specify that the handle is to be inherited when you create, open, or duplicate the handle. Creation functions typically use the **bInheritHandle** member of a [**SECURITY\_ATTRIBUTES**](/previous-versions/windows/desktop/legacy/aa379560(v=vs.85)) structure for this purpose. [**DuplicateHandle**](/windows/desktop/api/handleapi/nf-handleapi-duplicatehandle) uses the *bInheritHandles* parameter.
-   Specify that inheritable handles are to be inherited by setting the *bInheritHandles* parameter to TRUE when calling the [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function. Additionally, to inherit the standard input, standard output, and standard error handles, the **dwFlags** member of the [**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa) structure must include STARTF\_USESTDHANDLES.

To specify a list of the handles that should be inherited by a specific child process, call the [**UpdateProcThreadAttribute**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-updateprocthreadattribute) function with the *PROC_THREAD_ATTRIBUTE_HANDLE_LIST* flag.

An inherited handle refers to the same object in the child process as it does in the parent process. It also has the same value and access privileges. Therefore, when one process changes the state of the object, the change affects both processes. To use a handle, the child process must retrieve the handle value and "know" the object to which it refers. Usually, the parent process communicates this information to the child process through its command line, environment block, or some form of [interprocess communication](/windows/desktop/ipc/interprocess-communications).

Use the [**SetHandleInformation**](/windows/win32/api/handleapi/nf-handleapi-sethandleinformation) function to control if an existing handle is inheritable or not.

## Inheriting Environment Variables

A child process inherits the environment variables of its parent process by default. However, [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) enables the parent process to specify a different block of environment variables. For more information, see [Environment Variables](environment-variables.md).

## Inheriting the Current Directory

The [**GetCurrentDirectory**](/windows/desktop/api/winbase/nf-winbase-getcurrentdirectory) function retrieves the current directory of the calling process. A child process inherits the current directory of its parent process by default. However, [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) enables the parent process to specify a different current directory for the child process. To change the current directory of the calling process, use the [**SetCurrentDirectory**](/windows/desktop/api/winbase/nf-winbase-setcurrentdirectory) function.
