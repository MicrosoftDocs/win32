---
Description: The CreateThread function creates a new thread for a process.
ms.assetid: df59eedd-45ec-4564-96a5-8cecb345cfcc
title: Thread Functions for Debugging
ms.topic: article
ms.date: 05/31/2018
---

# Thread Functions for Debugging

The [**CreateThread**](https://msdn.microsoft.com/library/ms682453(v=VS.85).aspx) function creates a new thread for a process. Debuggers typically need to examine or change the contents of a thread's registers. To accomplish this, a debugger must obtain a handle to the thread by using the [**DuplicateHandle**](https://msdn.microsoft.com/library/ms724251(v=VS.85).aspx) function and specifying the appropriate access to the thread (THREAD\_GET\_CONTEXT, THREAD\_SET\_CONTEXT, or both). The [**OpenThread**](https://msdn.microsoft.com/library/ms684335(v=VS.85).aspx) function enables a debugger to obtain the identifier of an existing thread.

A process with appropriate access to a thread can examine the thread's registers by using the [**GetThreadContext**](https://msdn.microsoft.com/library/ms679362(v=VS.85).aspx) function and set the contents of the thread's registers by using the [**SetThreadContext**](https://msdn.microsoft.com/library/ms680632(v=VS.85).aspx) function.

A process can also obtain THREAD\_SUSPEND\_RESUME access to a thread. This type of access enables a debugger to control a thread's execution with the [**SuspendThread**](https://msdn.microsoft.com/library/ms686345(v=VS.85).aspx) and [**ResumeThread**](https://msdn.microsoft.com/library/ms685086(v=VS.85).aspx) functions. For more information about threads, see [Processes and Threads](https://msdn.microsoft.com/library/ms684841(v=VS.85).aspx).

 

 



