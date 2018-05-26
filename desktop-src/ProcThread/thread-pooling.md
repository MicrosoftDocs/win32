---
Description: There are many applications that create threads that spend a great deal of time in the sleeping state waiting for an event to occur.
ms.assetid: a5e52080-35d4-47f5-9050-90889e3bf2f8
title: Thread Pooling
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Thread Pooling

There are many applications that create threads that spend a great deal of time in the sleeping state waiting for an event to occur. Other threads may enter a sleeping state only to be awakened periodically to poll for a change or update status information. *Thread pooling* enables you to use threads more efficiently by providing your application with a pool of worker threads that are managed by the system. At least one thread monitors the status of all wait operations queued to the thread pool. When a wait operation has completed, a worker thread from the thread pool executes the corresponding callback function.

This topic describes the original thread pool API. The thread pool API introduced in Windows Vista is simpler, more reliable, has better performance, and provides more flexibility for developers. For information on the current thread pool API, see [Thread Pools](thread-pools.md).

You can also queue work items that are not related to a wait operation to the thread pool. To request that a work item be handled by a thread in the thread pool, call the [**QueueUserWorkItem**](/windows/win32/WinBase/?branch=master) function. This function takes a parameter to the function that will be called by the thread selected from the thread pool. There is no way to cancel a work item after it has been queued.

[Timer-queue timers](base.timer_queues) and [registered wait operations](base.wait_functions) also use the thread pool. Their callback functions are queued to the thread pool. You can also use the [**BindIoCompletionCallback**](/windows/win32/WinBase/nf-winbase-bindiocompletioncallback?branch=master) function to post asynchronous I/O operations. On completion of the I/O , the callback is executed by a thread pool thread.

The thread pool is created the first time you call [**QueueUserWorkItem**](/windows/win32/WinBase/?branch=master) or [**BindIoCompletionCallback**](/windows/win32/WinBase/nf-winbase-bindiocompletioncallback?branch=master), or when a timer-queue timer or registered wait operation queues a callback function. By default, the number of threads that can be created in the thread pool is about 500. Each thread uses the default stack size and runs at the default priority.

There are two types of worker threads in the thread pool: I/O and non-I/O. An *I/O worker thread* is a thread that waits in an alertable wait state. Work items are queued to I/O worker threads as asynchronous procedure calls (APC). You should queue a work item to an I/O worker thread if it should be executed in a thread that waits in an alertable state.

A *non-I/O worker thread* waits on I/O completion ports. Using non-I/O worker threads is more efficient than using I/O worker threads. Therefore, you should use non-I/O worker threads whenever possible. Both I/O and non-I/O worker threads do not exit if there are pending asynchronous I/O requests. Both types of threads can be used by work items that initiate asynchronous I/O completion requests. However, avoid posting asynchronous I/O completion requests in non-I/O worker threads if they could take a long time to complete.

To use thread pooling, the work items and all the functions they call must be thread-pool safe. A safe function does not assume that the thread executing it is a dedicated or persistent thread. In general, you should avoid using [thread local storage](thread-local-storage.md) or making an asynchronous call that requires a persistent thread, such as the [**RegNotifyChangeKeyValue**](base.regnotifychangekeyvalue) function. However, such functions can be called on a dedicated thread (created by the application) or queued to a persistent worker thread (using [**QueueUserWorkItem**](/windows/win32/WinBase/?branch=master) with the WT\_EXECUTEINPERSISTENTTHREAD option).

## Related topics

<dl> <dt>

[Alertable I/O](fs.alertable_i_o)
</dt> <dt>

[Asynchronous Procedure Calls](base.asynchronous_procedure_calls)
</dt> <dt>

[I/O Completion Ports](fs.i_o_completion_ports)
</dt> <dt>

[Thread Pools](thread-pools.md)
</dt> </dl>

 

 



