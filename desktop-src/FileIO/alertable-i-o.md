---
description: Alertable I/O is the method by which application threads process asynchronous I/O requests only when they are in an alertable state.
ms.assetid: d996f1cc-eeab-456b-818b-5307a79effd9
title: Alertable I/O
ms.topic: article
ms.date: 05/31/2018
---

# Alertable I/O

Alertable I/O is the method by which application threads process asynchronous I/O requests only when they are in an alertable state.

To understand when a thread is in an alertable state, consider the following scenario:

1.  A thread initiates an asynchronous read request by calling [**ReadFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-readfileex) with a pointer to a callback function.
2.  The thread initiates an asynchronous write request by calling [**WriteFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-writefileex) with a pointer to a callback function.
3.  The thread calls a function that fetches a row of data from a remote database server.

In this scenario, the calls to [**ReadFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-readfileex) and [**WriteFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-writefileex) will most likely return before the function call in step 3. When they do, the kernel places the pointers to the callback functions on the thread's Asynchronous Procedure Call (APC) queue. The kernel maintains this queue specifically to hold returned I/O request data until it can be processed by the corresponding thread.

When the row fetch is complete and the thread returns from the function, its highest priority is to process the returned I/O requests on the queue by calling the callback functions. To do this, it must enter an alertable state. A thread can only do this by calling one of the following functions with the appropriate flags:

-   [**SleepEx**](/windows/desktop/api/synchapi/nf-synchapi-sleepex)
-   [**WaitForSingleObjectEx**](/windows/desktop/api/synchapi/nf-synchapi-waitforsingleobjectex)
-   [**WaitForMultipleObjectsEx**](/windows/desktop/api/synchapi/nf-synchapi-waitformultipleobjectsex)
-   [**SignalObjectAndWait**](/windows/win32/api/synchapi/nf-synchapi-signalobjectandwait)
-   [**MsgWaitForMultipleObjectsEx**](/windows/desktop/api/winuser/nf-winuser-msgwaitformultipleobjectsex)

When the thread enters an alertable state, the following events occur:

1.  The kernel checks the thread's APC queue. If the queue contains callback function pointers, the kernel removes the pointer from the queue and sends it to the thread.
2.  The thread executes the callback function.
3.  Steps 1 and 2 are repeated for each pointer remaining in the queue.
4.  When the queue is empty, the thread returns from the function that placed it in an alertable state.

In this scenario, once the thread enters an alertable state it will call the callback functions sent to [**ReadFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-readfileex) and [**WriteFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-writefileex), then return from the function that placed it in an alertable state.

If a thread enters an alertable state while its APC queue is empty, the thread's execution will be suspended by the kernel until one of the following occurs:

-   The kernel object that is being waited on becomes signaled.
-   A callback function pointer is placed in the APC queue.

A thread that uses alertable I/O processes asynchronous I/O requests more efficiently than when they simply wait on the event flag in the [**OVERLAPPED**](/windows/desktop/api/minwinbase/ns-minwinbase-overlapped) structure to be set, and the alertable I/O mechanism is less complicated than [I/O completion ports](i-o-completion-ports.md) to use. However, alertable I/O returns the result of the I/O request only to the thread that initiated it. I/O completion ports do not have this limitation.

## Related topics

<dl> <dt>

[Asynchronous Procedure Calls](/windows/desktop/Sync/asynchronous-procedure-calls)
</dt> </dl>

 

 
