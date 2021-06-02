---
description: Synchronous pipe I/O and asynchronous pipe I/O. The ReadFile, WriteFile, TransactNamedPipe, and ConnectNamedPipe functions can perform input and output operations on a pipe either synchronously or asynchronously.
ms.assetid: 5ab9bb7f-1f99-4041-bba8-2863f34dbcaf
title: Synchronous and Overlapped Pipe I/O
ms.topic: article
ms.date: 05/31/2018
---

# Synchronous and Overlapped Pipe I/O

The [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile), [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile), [**TransactNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-transactnamedpipe), and [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) functions can perform input and output operations on a pipe either synchronously or asynchronously. When a function runs synchronously, it does not return until the operation it is performing is completed. This means that the execution of the calling thread can be blocked for an indefinite period while it waits for a time-consuming operation to be completed. When a function runs asynchronously, it returns immediately, even if the operation has not been completed. This enables a time-consuming operation to be executed in the background while the calling thread is free to perform other tasks.

Using asynchronous I/O enables a pipe server to use a loop that performs the following steps:

1.  Specify multiple event objects in a call to the wait function, and wait for one of the objects to be set to the signaled state.
2.  Use the wait function's return value to determine which overlapped operation has finished.
3.  Perform the tasks necessary to clean up the completed operation and initiate the next operation for that pipe handle. This can involve starting another overlapped operation for the same pipe handle.

Overlapped operations make it possible for one pipe to read and write data simultaneously and for a single thread to perform simultaneous I/O operations on multiple pipe handles. This enables a single-threaded pipe server to handle communications with multiple pipe clients efficiently. For an example, see [Named Pipe Server Using Overlapped I/O](named-pipe-server-using-overlapped-i-o.md).

For a pipe server to use synchronous operations to communicate with more than one client, it must create a separate thread for each pipe client so that one or more threads can run while other threads are waiting. For an example of a multithreaded pipe server that uses synchronous operations, see [Multithreaded Pipe Server](multithreaded-pipe-server.md).

## Enabling Asynchronous Operation

The [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile), [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile), [**TransactNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-transactnamedpipe), and [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) functions can be performed asynchronously only if you enable overlapped mode for the specified pipe handle and specify a valid pointer to an [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure. If the **OVERLAPPED** pointer is **NULL**, the function return value can incorrectly indicate that the operation has been completed. Therefore, it is strongly recommended that if you create a handle with FILE\_FLAG\_OVERLAPPED and want asynchronous behavior, you should always specify a valid **OVERLAPPED** structure.

The **hEvent** member of the specified [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure must contain a handle to a manual-reset event object. This is a synchronization object created by the [**CreateEvent**](/windows/desktop/api/synchapi/nf-synchapi-createeventa) function. The thread that initiates the overlapped operation uses the event object to determine when the operation has finished. You should not use the pipe handle for synchronization when performing simultaneous operations on the same handle because there is no way of knowing which operation's completion caused the pipe handle to be signaled. The only reliable technique for performing simultaneous operations on the same pipe handle is to use a separate **OVERLAPPED** structure with its own event object for each operation. For more information about event objects, see [Synchronization](/windows/desktop/Sync/synchronization).

Also, you can be notified when an overlapped operation completes by using the [**GetQueuedCompletionStatus**](/windows/desktop/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) or [**GetQueuedCompletionStatusEx**](/windows/desktop/FileIO/getqueuedcompletionstatusex-func) functions. In this case, you do not need to assign the manual-reset event in the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure, and the completion happens against the pipe handle in the same way as an asynchronous read or write operation. For more information, see [I/O Completion Ports](/windows/desktop/FileIO/i-o-completion-ports).

When [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile), [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile), [**TransactNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-transactnamedpipe), and [**ConnectNamedPipe**](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) operations are performed asynchronously, one of the following occurs:

-   If the operation is complete when the function returns, the return value indicates the success or failure of the operation. If an error occurs, the return value is zero and the [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) function returns something other than ERROR\_IO\_PENDING.
-   If the operation has not finished when the function returns, the return value is zero and [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) returns ERROR\_IO\_PENDING. In this case, the calling thread must wait until the operation has finished. The calling thread must then call the [**GetOverlappedResult**](/windows/desktop/api/ioapiset/nf-ioapiset-getoverlappedresult) function to determine the results.

## Using Completion Routines

The [**ReadFileEx**](/windows/desktop/api/fileapi/nf-fileapi-readfileex) and [**WriteFileEx**](/windows/desktop/api/fileapi/nf-fileapi-writefileex) functions provide another form of overlapped I/O. Unlike the overlapped [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile) and [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile) functions, which use an event object to signal completion, the extended functions specify a *completion routine*. A completion routine is a function that is queued for execution when the read or write operation is finished. The completion routine is not executed until the thread that called **ReadFileEx** and **WriteFileEx** starts an *alertable wait operation* by calling one of the [alertable wait functions](/windows/desktop/Sync/wait-functions) with the *fAlertable* parameter set to **TRUE**. In an alertable wait operation, the functions also return when a **ReadFileEx** or **WriteFileEx** completion routine is queued for execution. A pipe server can use the extended functions to perform a sequence of read and write operations for each client that connects to it. Each read or write operation in the sequence specifies a completion routine, and each completion routine initiates the next step in the sequence. For an example, see [Named Pipe Server Using Completion Routines](named-pipe-server-using-completion-routines.md).

 

 
