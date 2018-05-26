---
Description: Alertable I/O is the method by which application threads process asynchronous I/O requests only when they are in an alertable state.
ms.assetid: d996f1cc-eeab-456b-818b-5307a79effd9
title: Alertable I/O
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Alertable I/O

Alertable I/O is the method by which application threads process asynchronous I/O requests only when they are in an alertable state.

To understand when a thread is in an alertable state, consider the following scenario:

1.  A thread initiates an asynchronous read request by calling [**ReadFileEx**](/windows/win32/FileAPI/nf-fileapi-readfileex?branch=master) with a pointer to a callback function.
2.  The thread initiates an asynchronous write request by calling [**WriteFileEx**](/windows/win32/FileAPI/nf-fileapi-writefileex?branch=master) with a pointer to a callback function.
3.  The thread calls a function that fetches a row of data from a remote database server.

In this scenario, the calls to [**ReadFileEx**](/windows/win32/FileAPI/nf-fileapi-readfileex?branch=master) and [**WriteFileEx**](/windows/win32/FileAPI/nf-fileapi-writefileex?branch=master) will most likely return before the function call in step 3. When they do, the kernel places the pointers to the callback functions on the thread's Asynchronous Procedure Call (APC) queue. The kernel maintains this queue specifically to hold returned I/O request data until it can be processed by the corresponding thread.

When the row fetch is complete and the thread returns from the function, its highest priority is to process the returned I/O requests on the queue by calling the callback functions. To do this, it must enter an alertable state. A thread can only do this by calling one of the following functions with the appropriate flags:

-   [**SleepEx**](https://msdn.microsoft.com/library/windows/desktop/ms686307)
-   [**WaitForSingleObjectEx**](https://msdn.microsoft.com/library/windows/desktop/ms687036)
-   [**WaitForMultipleObjectsEx**](https://msdn.microsoft.com/library/windows/desktop/ms687028)
-   [**SignalObjectAndWait**](https://msdn.microsoft.com/library/windows/desktop/ms686293)
-   [**MsgWaitForMultipleObjectsEx**](https://msdn.microsoft.com/library/windows/desktop/ms684245)

When the thread enters an alertable state, the following events occur:

1.  The kernel checks the thread's APC queue. If the queue contains callback function pointers, the kernel removes the pointer from the queue and sends it to the thread.
2.  The thread executes the callback function.
3.  Steps 1 and 2 are repeated for each pointer remaining in the queue.
4.  When the queue is empty, the thread returns from the function that placed it in an alertable state.

In this scenario, once the thread enters an alertable state it will call the callback functions sent to [**ReadFileEx**](/windows/win32/FileAPI/nf-fileapi-readfileex?branch=master) and [**WriteFileEx**](/windows/win32/FileAPI/nf-fileapi-writefileex?branch=master), then return from the function that placed it in an alertable state.

If a thread enters an alertable state while its APC queue is empty, the thread's execution will be suspended by the kernel until one of the following occurs:

-   The kernel object that is being waited on becomes signaled.
-   A callback function pointer is placed in the APC queue.

A thread that uses alertable I/O processes asynchronous I/O requests more efficiently than when they simply wait on the event flag in the [**OVERLAPPED**](https://msdn.microsoft.com/library/windows/desktop/ms684342) structure to be set, and the alertable I/O mechanism is less complicated than [I/O completion ports](i-o-completion-ports.md) to use. However, alertable I/O returns the result of the I/O request only to the thread that initiated it. I/O completion ports do not have this limitation.

## Related topics

<dl> <dt>

[Asynchronous Procedure Calls](https://msdn.microsoft.com/library/windows/desktop/ms681951)
</dt> </dl>

 

 



