---
description: A thread pool is a collection of worker threads that efficiently execute asynchronous callbacks on behalf of the application.
ms.assetid: abe0798a-0b60-4bdb-a61e-45393f1e958d
title: Thread Pools
ms.topic: article
ms.date: 05/31/2018
---

# Thread Pools

A *thread pool* is a collection of worker threads that efficiently execute asynchronous callbacks on behalf of the application. The thread pool is primarily used to reduce the number of application threads and provide management of the worker threads. Applications can queue work items, associate work with waitable handles, automatically queue based on a timer, and bind with I/O.

## Thread Pool Architecture

The following applications can benefit from using a thread pool:

-   An application that is highly parallel and can dispatch a large number of small work items asynchronously (such as distributed index search or network I/O).
-   An application that creates and destroys a large number of threads that each run for a short time. Using the thread pool can reduce the complexity of thread management and the overhead involved in thread creation and destruction.
-   An application that processes independent work items in the background and in parallel (such as loading multiple tabs).
-   An application that must perform an exclusive wait on kernel objects or block on incoming events on an object. Using the thread pool can reduce the complexity of thread management and increase performance by reducing the number of context switches.
-   An application that creates custom waiter threads to wait on events.

The original thread pool has been completely rearchitected in Windows Vista. The new thread pool is improved because it provides a single worker thread type (supports both I/O and non-I/O), does not use a timer thread, provides a single timer queue, and provides a dedicated persistent thread. It also provides clean-up groups, higher performance, multiple pools per process that are scheduled independently, and a new thread pool API.

The thread pool architecture consists of the following:

-   Worker threads that execute the callback functions
-   Waiter threads that wait on multiple wait handles
-   A work queue
-   A default thread pool for each process
-   A worker factory that manages the worker threads

## Best Practices

The new [thread pool API](thread-pool-api.md) provides more flexibility and control than the [original thread pool API](thread-pooling.md). However, there are a few subtle but important differences. In the original API, the wait reset was automatic; in the new API, the wait must be explicitly reset each time. The original API handled impersonation automatically, transferring the security context of the calling process to the thread. With the new API, the application must explicitly set the security context.

The following are best practices when using a thread pool:

-   The threads of a process share the thread pool. A single worker thread can execute multiple callback functions, one at a time. These worker threads are managed by the thread pool. Therefore, do not terminate a thread from the thread pool by calling [**TerminateThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminatethread) on the thread or by calling [**ExitThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread) from a callback function.
-   An I/O request can run on any thread in the thread pool. Canceling I/O on a thread pool thread requires synchronization because the cancel function might run on a different thread than the one that is handling the I/O request, which can result in cancellation of an unknown operation. To avoid this, always provide the [**OVERLAPPED**](/windows/win32/api/minwinbase/ns-minwinbase-overlapped) structure with which an I/O request was initiated when calling [**CancelIoEx**](/windows/win32/api/ioapiset/nf-ioapiset-cancelioex) for asynchronous I/O, or use your own synchronization to ensure that no other I/O can be started on the target thread before calling either the [**CancelSynchronousIo**](/windows/win32/api/ioapiset/nf-ioapiset-cancelsynchronousio) or **CancelIoEx** function.
-   Clean up all resources created in the callback function before returning from the function. These include TLS, security contexts, thread priority, and COM registration. Callback functions must also restore the thread state before returning.
-   Keep wait handles and their associated objects alive until the thread pool has signaled that it is finished with the handle.
-   Mark all threads that are waiting on lengthy operations (such as I/O flushes or resource cleanup) so that the thread pool can allocate new threads instead of waiting for this one.
-   Before unloading a DLL that uses the thread pool, cancel all work items, I/O, wait operations, and timers, and wait for executing callbacks to complete.
-   Avoid deadlocks by eliminating dependencies between work items and between callbacks, by ensuring a callback is not waiting for itself to complete, and by preserving the thread priority.
-   Do not queue too many items too quickly in a process with other components using the default thread pool. There is one default thread pool per process, including Svchost.exe. By default, each thread pool has a maximum of 500 worker threads. The thread pool attempts to create more worker threads when the number of worker threads in the ready/running state must be less than the number of processors.
-   Avoid the COM single-threaded apartment model, as it is incompatible with the thread pool. STA creates thread state which can affect the next work item for the thread. STA is generally long-lived and has thread affinity, which is the opposite of the thread pool.
-   Create a new thread pool to control thread priority and isolation, create custom characteristics, and possibly improve responsiveness. However, additional thread pools require more system resources (threads, kernel memory). Too many pools increases the potential for CPU contention.
-   If possible, use a waitable object instead of an APC-based mechanism to signal a thread pool thread. APCs do not work as well with thread pool threads as other signaling mechanisms because the system controls the lifetime of thread pool threads, so it is possible for a thread to be terminated before the notification is delivered.
-   Use the thread pool debugger extension, !tp. This command has the following usage:

    -   pool *address* *flags*
    -   obj *address* *flags*
    -   tqueue *address* *flags*
    -   waiter *address*
    -   worker *address*

    For pool, waiter, and worker, if the address is zero, the command dumps all objects. For waiter and worker, omitting the address dumps the current thread. The following flags are defined: 0x1 (single-line output), 0x2 (dump members), and 0x4 (dump pool work queue).

## Related topics

<dl> <dt>

[Thread Pool API](thread-pool-api.md)
</dt> <dt>

[Using the Thread Pool Functions](using-the-thread-pool-functions.md)
</dt> </dl>

 

 
