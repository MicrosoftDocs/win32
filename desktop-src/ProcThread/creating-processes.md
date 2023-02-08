---
description: Learn how to use the CreateProcess function, which creates a new process that runs independently of the creating process.
ms.assetid: 4c3f76a3-e9f5-4d73-b5ef-eabfa9d6e4d4
title: Create processes
ms.topic: article
ms.date: 02/08/2023
---

# Create processes

The [CreateProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) function creates a new process that runs independently of the creating process. However, for simplicity, the relationship is called a parent-child relationship.

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

