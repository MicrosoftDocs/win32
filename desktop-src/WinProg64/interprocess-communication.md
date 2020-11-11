---
title: Interprocess communication
description: The following techniques can be used for communication between 32-bit and 64-bit applications.
ms.assetid: 9a60ccfe-4ccf-44d7-9522-42609d95217b
keywords:
- interprocess communication 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Interprocess Communication Between 32-bit and 64-bit Applications

The following techniques can be used for communication between 32-bit and 64-bit applications:

-   64-bit versions of Windows use 32-bit handles for interoperability. When sharing a handle between 32-bit and 64-bit applications, only the lower 32 bits are significant, so it is safe to truncate the handle (when passing it from 64-bit to 32-bit) or sign-extend the handle (when passing it from 32-bit to 64-bit). Handles that can be shared include handles to user objects such as windows (**HWND**), handles to GDI objects such as pens and brushes (**HBRUSH** and **HPEN**), and handles to named objects such as mutexes, semaphores, and file handles.
-   Remote procedure calls (RPC) can be used.
-   COM LocalServers can be used if both 32-bit and 64-bit proxy/stub DLLs are registered for all interfaces used.
-   Shared memory can be used if pointer-dependent types are converted properly (or avoided).
-   The [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) and [**ShellExecute**](/windows/win32/api/shellapi/nf-shellapi-shellexecutea) functions can launch 32-bit and 64-bit processes from either 32-bit or 64-bit processes with certain limitations.

A 64-bit executable file located under %windir%\\System32 cannot be launched from a 32-bit process, because the file system redirector redirects the path. Do not disable redirection to accomplish this; use %windir%\\Sysnative instead. For more information, see [File System Redirector](file-system-redirector.md).

 

 