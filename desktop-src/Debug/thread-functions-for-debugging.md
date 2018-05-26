---
Description: The CreateThread function creates a new thread for a process.
ms.assetid: df59eedd-45ec-4564-96a5-8cecb345cfcc
title: Thread Functions for Debugging
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Thread Functions for Debugging

The [**CreateThread**](base.createthread) function creates a new thread for a process. Debuggers typically need to examine or change the contents of a thread's registers. To accomplish this, a debugger must obtain a handle to the thread by using the [**DuplicateHandle**](base.duplicatehandle) function and specifying the appropriate access to the thread (THREAD\_GET\_CONTEXT, THREAD\_SET\_CONTEXT, or both). The [**OpenThread**](base.openthread) function enables a debugger to obtain the identifier of an existing thread.

A process with appropriate access to a thread can examine the thread's registers by using the [**GetThreadContext**](/windows/win32/WinBase/nf-dbgeng-idebugadvanced4-getthreadcontext?branch=master) function and set the contents of the thread's registers by using the [**SetThreadContext**](/windows/win32/WinBase/nf-dbgeng-idebugadvanced4-setthreadcontext?branch=master) function.

A process can also obtain THREAD\_SUSPEND\_RESUME access to a thread. This type of access enables a debugger to control a thread's execution with the [**SuspendThread**](base.suspendthread) and [**ResumeThread**](base.resumethread) functions. For more information about threads, see [Processes and Threads](base.processes_and_threads).

 

 



