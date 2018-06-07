---
Description: Wait Chain Traversal (WCT) enables debuggers to diagnose application hangs and deadlocks.
ms.assetid: d266a663-b101-4936-9574-f6ce223419ae
title: Wait Chain Traversal
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Wait Chain Traversal

Wait Chain Traversal (WCT) enables debuggers to diagnose application hangs and deadlocks. A *wait chain* is an alternating sequence of threads and synchronization objects; each thread waits for the object that follows it, which is owned by the subsequent thread in the chain.

A thread waits for a synchronization object from the time it requests it until it has acquired it. A lock is owned by a thread from the time the thread acquires it, until it releases it. Lock ownership is equivalent to the lock waiting for the thread to release it. Therefore, if thread 1 waits for a lock that is owned by thread 2, this is the same as saying that thread 1 waits for thread 2. WCT currently supports the following synchronization primitives:

-   ALPC
-   COM
-   Critical sections
-   Mutexes
-   **SendMessage**
-   Wait operations on processes and threads

To retrieve the wait chain for one or more threads, create a WCT session using the [**OpenThreadWaitChainSession**](/windows/desktop/api/Wct/nf-wct-openthreadwaitchainsession) and [**GetThreadWaitChain**](/windows/desktop/api/Wct/nf-wct-getthreadwaitchain) functions. WCT sessions are represented by a handle of type **HWCT**. Sessions can be either synchronous or asynchronous in nature. Synchronous sessions will block the calling thread until a wait chain has been retrieved. Synchronous sessions cannot be canceled. Asynchronous sessions do not block the calling thread and can be canceled by the application using the [**CloseThreadWaitChainSession**](/windows/desktop/api/Wct/nf-wct-closethreadwaitchainsession) function. Results from asynchronous operations are made available through a [*WaitChainCallback*](/windows/desktop/api/Wct/nc-wct-pwaitchaincallback) callback function provided by the application.

For asynchronous sessions, the caller can specify a pointer to a context data structure through [**GetThreadWaitChain**](/windows/desktop/api/Wct/nf-wct-getthreadwaitchain). The same pointer is passed to the callback function. This context data structure is user-defined and opaque to WCT. It can be used by the application to communicate context between a WCT query and a callback function. A common approach is to pass an event handle through this structure; when the callback is executed, it signals this event and informs some monitoring thread that the query has been completed.

## Related topics

<dl> <dt>

[Using WCT](using-wct.md)
</dt> <dt>

[WCT Reference](wct-reference.md)
</dt> </dl>

 

 



