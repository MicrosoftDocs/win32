---
Description: The CreateThread function creates a new thread for a process.
ms.assetid: df59eedd-45ec-4564-96a5-8cecb345cfcc
title: Thread Functions for Debugging
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Thread Functions for Debugging

The [**CreateThread**](https://msdn.microsoft.com/windows/desktop/202a4b42-513a-45de-894a-72e56c706a58) function creates a new thread for a process. Debuggers typically need to examine or change the contents of a thread's registers. To accomplish this, a debugger must obtain a handle to the thread by using the [**DuplicateHandle**](https://msdn.microsoft.com/windows/desktop/9c8da574-5bda-49f1-a6b6-c026639d6504) function and specifying the appropriate access to the thread (THREAD\_GET\_CONTEXT, THREAD\_SET\_CONTEXT, or both). The [**OpenThread**](https://msdn.microsoft.com/windows/desktop/d020ecc5-89d1-4a0d-a197-15a66e269e86) function enables a debugger to obtain the identifier of an existing thread.

A process with appropriate access to a thread can examine the thread's registers by using the [**GetThreadContext**](/windows/desktop/api/WinBase/nf-dbgeng-idebugadvanced4-getthreadcontext) function and set the contents of the thread's registers by using the [**SetThreadContext**](/windows/desktop/api/WinBase/nf-dbgeng-idebugadvanced4-setthreadcontext) function.

A process can also obtain THREAD\_SUSPEND\_RESUME access to a thread. This type of access enables a debugger to control a thread's execution with the [**SuspendThread**](https://msdn.microsoft.com/windows/desktop/1332abcb-3356-4890-a03c-843358c1a3ce) and [**ResumeThread**](https://msdn.microsoft.com/windows/desktop/ffc4e474-635b-4bf7-a68f-073899fb3fde) functions. For more information about threads, see [Processes and Threads](https://msdn.microsoft.com/windows/desktop/6bff848c-0c55-41e7-aff1-84c6b21a1b8d).

 

 



