---
description: Learn how to use the CreateProcess function, which creates a new process that runs independently of the creating process.
ms.assetid: 4c3f76a3-e9f5-4d73-b5ef-eabfa9d6e4d4
title: Create processes
ms.topic: concept-article
ms.date: 07/18/2025
---

# Create processes

The [CreateProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function creates a new process that runs independently of the creating process. For simplicity, this relationship is called a parent-child relationship.

> [!IMPORTANT]
> **Security — handle inheritance**: Set *bInheritHandles* to `FALSE` unless the child process specifically needs access to inherited handles. Inherited handles (file handles, sockets, tokens) can leak sensitive resources to child processes. When inheritance is required, use `STARTUPINFOEX` with `UpdateProcThreadAttribute(PROC_THREAD_ATTRIBUTE_HANDLE_LIST, ...)` to explicitly list only the handles the child needs.

> [!IMPORTANT]
> **lpCommandLine must be writable**: When passing a command line as the *lpCommandLine* parameter (second parameter), the buffer **must be a writable character array** — not a string literal or `const` pointer. The Unicode version (`CreateProcessW`) may modify this buffer in place. Passing a read-only string causes an access violation.

> [!NOTE]
> **Modern alternatives**: For simpler process creation scenarios, consider [System.Diagnostics.Process](/dotnet/api/system.diagnostics.process) (.NET), `_wspawnl`/`_wsystem` (CRT), or [ShellExecuteEx](/windows/win32/api/shellapi/nf-shellapi-shellexecuteexw) (for launching documents/URLs with verb handling). Use `CreateProcess` when you need full control over handle inheritance, process attributes, security descriptors, or creation flags.

The following code demonstrates how to create a process.


```cpp
#include <windows.h>
#include <stdio.h>
#include <tchar.h>

void _tmain( int argc, TCHAR *argv[] )
{
    STARTUPINFO si;
    PROCESS_INFORMATION pi;

    ZeroMemory( &si, sizeof(si) );
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi) );

    if( argc != 2 )
    {
        printf("Usage: %s [cmdline]\n", argv[0]);
        return;
    }

    // Start the child process. 
    if( !CreateProcess( NULL,   // No module name (use command line)
        argv[1],        // Command line
        NULL,           // Process handle not inheritable
        NULL,           // Thread handle not inheritable
        FALSE,          // Set handle inheritance to FALSE
        0,              // No creation flags
        NULL,           // Use parent's environment block
        NULL,           // Use parent's starting directory 
        &si,            // Pointer to STARTUPINFO structure
        &pi )           // Pointer to PROCESS_INFORMATION structure
    ) 
    {
        printf( "CreateProcess failed (%d).\n", GetLastError() );
        return;
    }

    // Wait until child process exits.
    WaitForSingleObject( pi.hProcess, INFINITE );

    // Close process and thread handles. 
    CloseHandle( pi.hProcess );
    CloseHandle( pi.hThread );
}
```

If [CreateProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) succeeds, it returns a [PROCESS_INFORMATION](/windows/win32/api/processthreadsapi/ns-processthreadsapi-process_information) structure that contains handles and identifiers for the new process and its primary thread. The thread and process handles are created with full access rights, although you can restrict access if you specify security descriptors. When you no longer need these handles, close them by using the [CloseHandle](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function.

You can also create a process by using the [CreateProcessAsUser](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessasusera) or [CreateProcessWithLogonW](/windows/desktop/api/WinBase/nf-winbase-createprocesswithlogonw) functions. These functions let you specify the security context of the user account in which the process runs.

