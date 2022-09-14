---
description: I/O completion ports provide an efficient threading model for processing multiple asynchronous I/O requests on a multiprocessor system.
ms.assetid: 213c48e8-bb21-43ed-9c00-2a5cf8ac25f0
title: I/O Completion Ports
ms.topic: article
ms.date: 05/31/2018
---

# I/O Completion Ports

I/O completion ports provide an efficient threading model for processing multiple asynchronous I/O requests on a multiprocessor system. When a process creates an I/O completion port, the system creates an associated queue object for threads whose sole purpose is to service these requests. Processes that handle many concurrent asynchronous I/O requests can do so more quickly and efficiently by using I/O completion ports in conjunction with a pre-allocated thread pool than by creating threads at the time they receive an I/O request.

## How I/O Completion Ports Work

The [**CreateIoCompletionPort**](createiocompletionport.md) function creates an I/O completion port and associates one or more file handles with that port. When an asynchronous I/O operation on one of these file handles completes, an I/O completion packet is queued in first-in-first-out (FIFO) order to the associated I/O completion port. One powerful use for this mechanism is to combine the synchronization point for multiple file handles into a single object, although there are also other useful applications. Please note that while the packets are queued in FIFO order they may be dequeued in a different order.

> [!Note]
>
> The term *file handle* as used here refers to a system abstraction representing an overlapped I/O endpoint, not only a file on disk. For example, it can be a network endpoint, TCP socket, named pipe, or mail slot. Any system object that supports overlapped I/O can be used. For a list of related I/O functions, see the end of this topic.

 

When a file handle is associated with a completion port, the status block passed in will not be updated until the packet is removed from the completion port. The only exception is if the original operation returns synchronously with an error. A thread (either one created by the main thread or the main thread itself) uses the [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function to wait for a completion packet to be queued to the I/O completion port, rather than waiting directly for the asynchronous I/O to complete. Threads that block their execution on an I/O completion port are released in last-in-first-out (LIFO) order, and the next completion packet is pulled from the I/O completion port's FIFO queue for that thread. This means that, when a completion packet is released to a thread, the system releases the last (most recent) thread associated with that port, passing it the completion information for the oldest I/O completion.

Although any number of threads can call [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) for a specified I/O completion port, when a specified thread calls **GetQueuedCompletionStatus** the first time, it becomes associated with the specified I/O completion port until one of three things occurs: The thread exits, specifies a different I/O completion port, or closes the I/O completion port. In other words, a single thread can be associated with, at most, one I/O completion port.

When a completion packet is queued to an I/O completion port, the system first checks how many threads associated with that port are running. If the number of threads running is less than the concurrency value (discussed in the next section), one of the waiting threads (the most recent one) is allowed to process the completion packet. When a running thread completes its processing, it typically calls [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) again, at which point it either returns with the next completion packet or waits if the queue is empty.

Threads can use the [**PostQueuedCompletionStatus**](postqueuedcompletionstatus.md) function to place completion packets in an I/O completion port's queue. By doing so, the completion port can be used to receive communications from other threads of the process, in addition to receiving I/O completion packets from the I/O system. The **PostQueuedCompletionStatus** function allows an application to queue its own special-purpose completion packets to the I/O completion port without starting an asynchronous I/O operation. This is useful for notifying worker threads of external events, for example.

The I/O completion port handle and every file handle associated with that particular I/O completion port are known as *references to the I/O completion port*. The I/O completion port is released when there are no more references to it. Therefore, all of these handles must be properly closed to release the I/O completion port and its associated system resources. After these conditions are satisfied, an application should close the I/O completion port handle by calling the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function.

> [!Note]
>
> An I/O completion port is associated with the process that created it and is not sharable between processes. However, a single handle is sharable between threads in the same process.

 

## Threads and Concurrency

The most important property of an I/O completion port to consider carefully is the concurrency value. The concurrency value of a completion port is specified when it is created with [**CreateIoCompletionPort**](createiocompletionport.md) via the *NumberOfConcurrentThreads* parameter. This value limits the number of runnable threads associated with the completion port. When the total number of runnable threads associated with the completion port reaches the concurrency value, the system blocks the execution of any subsequent threads associated with that completion port until the number of runnable threads drops below the concurrency value.

The most efficient scenario occurs when there are completion packets waiting in the queue, but no waits can be satisfied because the port has reached its concurrency limit. Consider what happens with a concurrency value of one and multiple threads waiting in the [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) function call. In this case, if the queue always has completion packets waiting, when the running thread calls **GetQueuedCompletionStatus**, it will not block execution because, as mentioned earlier, the thread queue is LIFO. Instead, this thread will immediately pick up the next queued completion packet. No thread context switches will occur, because the running thread is continually picking up completion packets and the other threads are unable to run.

> [!Note]
>
> In the previous example, the extra threads appear to be useless and never run, but that assumes that the running thread never gets put in a wait state by some other mechanism, terminates, or otherwise closes its associated I/O completion port. Consider all such thread execution ramifications when designing the application.

 

The best overall maximum value to pick for the concurrency value is the number of CPUs on the computer. If your transaction required a lengthy computation, a larger concurrency value will allow more threads to run. Each completion packet may take longer to finish, but more completion packets will be processed at the same time. You can experiment with the concurrency value in conjunction with profiling tools to achieve the best effect for your application.

The system also allows a thread waiting in [**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) to process a completion packet if another running thread associated with the same I/O completion port enters a wait state for other reasons, for example the [**SuspendThread**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-suspendthread) function. When the thread in the wait state begins running again, there may be a brief period when the number of active threads exceeds the concurrency value. However, the system quickly reduces this number by not allowing any new active threads until the number of active threads falls below the concurrency value. This is one reason to have your application create more threads in its thread pool than the concurrency value. Thread pool management is beyond the scope of this topic, but a good rule of thumb is to have a minimum of twice as many threads in the thread pool as there are processors on the system. For additional information about thread pooling, see [Thread Pools](/windows/desktop/ProcThread/thread-pools).

## Supported I/O Functions

The following functions can be used to start I/O operations that complete by using I/O completion ports. You must pass the function an instance of the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure and a file handle previously associated with an I/O completion port (by a call to [**CreateIoCompletionPort**](createiocompletionport.md)) to enable the I/O completion port mechanism:

-   [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex)
-   [**ConnectNamedPipe**](/windows/desktop/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe)
-   [**DeviceIoControl**](/windows/desktop/api/ioapiset/nf-ioapiset-deviceiocontrol)
-   [**LockFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-lockfileex)
-   [**ReadDirectoryChangesW**](/windows/desktop/api/WinBase/nf-winbase-readdirectorychangesw)
-   [**ReadFile**](/windows/desktop/api/FileAPI/nf-fileapi-readfile)
-   [**TransactNamedPipe**](/windows/desktop/api/namedpipeapi/nf-namedpipeapi-transactnamedpipe)
-   [**WaitCommEvent**](/windows/desktop/api/winbase/nf-winbase-waitcommevent)
-   [**WriteFile**](/windows/desktop/api/FileAPI/nf-fileapi-writefile)
-   [**WSASendMsg**](/windows/desktop/api/winsock2/nf-winsock2-wsasendmsg)
-   [**WSASendTo**](/windows/desktop/api/winsock2/nf-winsock2-wsasendto)
-   [**WSASend**](/windows/desktop/api/winsock2/nf-winsock2-wsasend)
-   [**WSARecvFrom**](/windows/desktop/api/winsock2/nf-winsock2-wsarecvfrom)
-   [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg)
-   [**WSARecv**](/windows/desktop/api/winsock2/nf-winsock2-wsarecv)

## Related topics

<dl> <dt>


</dt> <dt>

[About Processes and Threads](/windows/desktop/ProcThread/about-processes-and-threads)
</dt> <dt>

[**BindIoCompletionCallback**](/windows/desktop/api/winbase/nf-winbase-bindiocompletioncallback)
</dt> <dt>

[**CreateIoCompletionPort**](createiocompletionport.md)
</dt> <dt>

[**GetQueuedCompletionStatus**](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus)
</dt> <dt>

[**GetQueuedCompletionStatusEx**](getqueuedcompletionstatusex-func.md)
</dt> <dt>

[**PostQueuedCompletionStatus**](postqueuedcompletionstatus.md)
</dt> </dl>

 

 
