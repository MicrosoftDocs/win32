---
description: Terminating a process has the following results:Any remaining threads in the process are marked for termination.Any resources allocated by the process are freed.All kernel objects are closed.The process code is removed from memory.The process exit code is set.The process object is signaled.
ms.assetid: af24d157-2719-4052-8029-1eb8010047cc
title: Terminating a Process
ms.topic: article
ms.date: 05/31/2018
---

# Terminating a Process

Terminating a process has the following results:

-   Any remaining threads in the process are marked for termination.
-   Any resources allocated by the process are freed.
-   All kernel objects are closed.
-   The process code is removed from memory.
-   The process exit code is set.
-   The process object is signaled.

While open handles to kernel objects are closed automatically when a process terminates, the objects themselves exist until all open handles to them are closed. Therefore, an object will remain valid after a process that is using it terminates if another process has an open handle to it.

The [**GetExitCodeProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getexitcodeprocess) function returns the termination status of a process. While a process is executing, its termination status is STILL\_ACTIVE. When a process terminates, its termination status changes from STILL\_ACTIVE to the exit code of the process.

When a process terminates, the state of the process object becomes signaled, releasing any threads that had been waiting for the process to terminate. For more about synchronization, see [Synchronizing Execution of Multiple Threads](synchronizing-execution-of-multiple-threads.md).

When the system is terminating a process, it does not terminate any child processes that the process has created. Terminating a process does not generate notifications for WH\_CBT hook procedures.

Use the [**SetProcessShutdownParameters**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessshutdownparameters) function to specify certain aspects of the process termination at system shutdown, such as when a process should terminate relative to the other processes in the system.

## How Processes are Terminated

A process executes until one of the following events occurs:

-   Any thread of the process calls the [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) function. Note that some implementation of the C run-time library (CRT) call **ExitProcess** if the primary thread of the process returns.
-   The last thread of the process terminates.
-   Any thread calls the [**TerminateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess) function with a handle to the process.
-   For console processes, the default [console control handler](/windows/console/console-control-handlers) calls [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) when the console receives a CTRL+C or CTRL+BREAK signal.
-   The user shuts down the system or logs off.

Do not terminate a process unless its threads are in known states. If a thread is waiting on a kernel object, it will not be terminated until the wait has completed. This can cause the application to stop responding.

The primary thread can avoid terminating other threads by directing them to call [**ExitThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread) before causing the process to terminate (for more information, see [Terminating a Thread](terminating-a-thread.md)). The primary thread can still call [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) afterwards to ensure that all threads are terminated.

The exit code for a process is either the value specified in the call to [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) or [**TerminateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess), or the value returned by the main or [**WinMain**](/windows/win32/api/winbase/nf-winbase-winmain) function of the process. If a process is terminated due to a fatal exception, the exit code is the value of the exception that caused the termination. In addition, this value is used as the exit code for all the threads that were executing when the exception occurred.

If a process is terminated by [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess), the system calls the entry-point function of each attached DLL with a value indicating that the process is detaching from the DLL. DLLs are not notified when a process is terminated by [**TerminateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess). For more information about DLLs, see [Dynamic-Link Libraries](../dlls/dynamic-link-libraries.md).

If a process is terminated by [**TerminateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess), all threads of the process are terminated immediately with no chance to run additional code. This means that the thread does not execute code in termination handler blocks. In addition, no attached DLLs are notified that the process is detaching. If you need to have one process terminate another process, the following steps provide a better solution:

-   Have both processes call the [**RegisterWindowMessage**](/windows/win32/api/winuser/nf-winuser-registerwindowmessagea) function to create a private message.
-   One process can terminate the other process by broadcasting a private message using the [**BroadcastSystemMessage**](/windows/win32/api/winuser/nf-winuser-broadcastsystemmessage) function as follows:

    ``` syntax
     DWORD dwRecipients = BSM_APPLICATIONS;
        UINT uMessage = PM_MYMSG;
        WPARAM wParam = 0;
        LPARAM lParam = 0;

        BroadcastSystemMessage( 
            BSF_IGNORECURRENTTASK, // do not send message to this process
            &dwRecipients,         // broadcast only to applications
            uMessage,              // registered private message
            wParam,                // message-specific value
            lParam );              // message-specific value
    ```

-   The process receiving the private message calls [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) to terminate its execution.

The execution of the [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess), [**ExitThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread), [**CreateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread), [**CreateRemoteThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread), and [**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) functions is serialized within an address space. The following restrictions apply:

-   During process startup and DLL initialization routines, new threads can be created, but they do not begin execution until DLL initialization is finished for the process.
-   Only one thread at a time can be in a DLL initialization or detach routine.
-   The [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) function does not return until there are no threads are in their DLL initialization or detach routines.

 

 
