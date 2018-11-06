---
Description: A child process can inherit several properties and resources from its parent process.
ms.assetid: c530e723-2d40-4022-a259-dfc650604e44
title: Inheritance
ms.topic: article
ms.date: 05/31/2018
---

# Inheritance

A child process can inherit several properties and resources from its parent process. You can also prevent a child process from inheriting properties from its parent process. The following can be inherited:

-   Open handles returned by the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function. This includes handles to files, console input buffers, console screen buffers, named pipes, serial communication devices, and mailslots.
-   Open handles to process, thread, mutex, event, semaphore, named-pipe, anonymous-pipe, and file-mapping objects. These are returned by the [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx), [**CreateThread**](https://msdn.microsoft.com/en-us/library/ms682453(v=VS.85).aspx), [**CreateMutex**](https://msdn.microsoft.com/library/windows/desktop/ms682411), [**CreateEvent**](https://msdn.microsoft.com/library/windows/desktop/ms682396), [**CreateSemaphore**](https://msdn.microsoft.com/library/windows/desktop/ms682438), [**CreateNamedPipe**](https://msdn.microsoft.com/library/windows/desktop/aa365150), [**CreatePipe**](https://msdn.microsoft.com/library/windows/desktop/aa365152), and [**CreateFileMapping**](https://msdn.microsoft.com/library/windows/desktop/aa366537) functions, respectively.
-   Environment variables.
-   The current directory.
-   The console, unless the process is detached or a new console is created. A child console process can also inherits the parent's standard handles, as well as access to the input buffer and the active screen buffer.
-   The error mode, as set by the [**SetErrorMode**](https://msdn.microsoft.com/library/windows/desktop/ms680621) function.
-   The process affinity mask.
-   The association with a job.

The child process does not inherit the following:

-   Priority class.
-   Handles returned by [**LocalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366723), [**GlobalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366574), [**HeapCreate**](https://msdn.microsoft.com/library/windows/desktop/aa366599), and [**HeapAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366597).
-   Pseudo handles, as in the handles returned by the [**GetCurrentProcess**](https://msdn.microsoft.com/en-us/library/ms683179(v=VS.85).aspx) or [**GetCurrentThread**](https://msdn.microsoft.com/en-us/library/ms683182(v=VS.85).aspx) function. These handles are valid only for the calling process.
-   DLL module handles returned by the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) function.
-   GDI or USER handles, such as **HBITMAP** or **HMENU**.

## Inheriting Handles

A child process can inherit some of its parent's handles, but not inherit others. To cause a handle to be inherited, you must do two things:

-   Specify that the handle is to be inherited when you create, open, or duplicate the handle. Creation functions typically use the **bInheritHandle** member of a [**SECURITY\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/desktop/aa379560) structure for this purpose. [**DuplicateHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724251) uses the *bInheritHandles* parameter.
-   Specify that inheritable handles are to be inherited by setting the *bInheritHandles* parameter to TRUE when calling the [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) function. Additionally, to inherit the standard input, standard output, and standard error handles, the **dwFlags** member of the [**STARTUPINFO**](https://msdn.microsoft.com/en-us/library/ms686331(v=VS.85).aspx) structure must include STARTF\_USESTDHANDLES.

An inherited handle refers to the same object in the child process as it does in the parent process. It also has the same value and access privileges. Therefore, when one process changes the state of the object, the change affects both processes. To use a handle, the child process must retrieve the handle value and "know" the object to which it refers. Usually, the parent process communicates this information to the child process through its command line, environment block, or some form of [interprocess communication](https://msdn.microsoft.com/library/windows/desktop/aa365574).

The [**DuplicateHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724251) function is useful if a process has an inheritable open handle that you do not want to be inherited by the child process. In this case, use **DuplicateHandle** to open a duplicate of the handle that cannot be inherited, then use the [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211) function to close the inheritable handle. You can also use the **DuplicateHandle** function to open an inheritable duplicate of a handle that cannot be inherited.

## Inheriting Environment Variables

A child process inherits the environment variables of its parent process by default. However, [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) enables the parent process to specify a different block of environment variables. For more information, see [Environment Variables](environment-variables.md).

## Inheriting the Current Directory

The [**GetCurrentDirectory**](https://msdn.microsoft.com/library/windows/desktop/aa364934) function retrieves the current directory of the calling process. A child process inherits the current directory of its parent process by default. However, [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) enables the parent process to specify a different current directory for the child process. To change the current directory of the calling process, use the [**SetCurrentDirectory**](https://msdn.microsoft.com/library/windows/desktop/aa365530) function.

 

 



