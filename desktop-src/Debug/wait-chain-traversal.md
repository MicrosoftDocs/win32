---
Description: Wait Chain Traversal (WCT) enables debuggers to diagnose application hangs and deadlocks.
ms.assetid: d266a663-b101-4936-9574-f6ce223419ae
title: Wait Chain Traversal
ms.topic: article
ms.date: 08/10/2020
---

# Wait Chain Traversal

Wait Chain Traversal (WCT) enables debuggers to diagnose application hangs and deadlocks.

A *wait chain* is an alternating sequence of threads and synchronization objects where each thread waits for the object that follows. Each object that follows is, in turn, owned by the subsequent thread in the chain.

A thread waits for a synchronization object from the time the thread requests the object until the thread has acquired it. This "lock" is owned by a thread from the time the thread acquires it, until the thread releases it. In other words, when thread 1 is waiting for a lock that is owned by thread 2, thread 1 is "waiting" for thread 2.

WCT supports the following synchronization primitives:

- [Advanced Local Procedure Call (ALPC)](/windows/win32/etw/alpc)
- [Component Object Model (COM)](/windows/win32/com/the-component-object-model)
- [Critical sections](/windows/win32/sync/critical-section-objects)
- [Mutexes](/windows/win32/sync/mutex-objects)
- [SendMessage](/windows/win32/api/winuser/nf-winuser-sendmessage)
- [Wait](/windows/win32/sync/wait-functions) operations on [processes and threads](/windows/win32/procthread/processes-and-threads)

To retrieve the wait chain for one or more threads, create a WCT session using the [OpenThreadWaitChainSession](/windows/desktop/api/Wct/nf-wct-openthreadwaitchainsession) and [GetThreadWaitChain](/windows/desktop/api/Wct/nf-wct-getthreadwaitchain) functions. WCT sessions are represented by a handle of type **HWCT**.

## Sessions can be synchronous or asynchronous

Synchronous sessions cannot be canceled, and block the calling thread, until a wait chain has been retrieved.

Asynchronous sessions do not block the calling thread, and can be canceled by the application using the [CloseThreadWaitChainSession](/windows/desktop/api/Wct/nf-wct-closethreadwaitchainsession) function. Results from asynchronous operations are made available through a [WaitChainCallback](https://msdn.microsoft.com/library/ms681421(v=VS.85).aspx) callback function provided by the application.

For asynchronous sessions, the caller can specify a pointer to a context data structure through [GetThreadWaitChain](/windows/desktop/api/Wct/nf-wct-getthreadwaitchain) (this same pointer is passed to the [WaitChainCallback](https://msdn.microsoft.com/library/ms681421(v=VS.85).aspx) callback function).

The context data structure is user-defined and opaque to WCT. It can be used by the application to communicate context between a WCT query and a callback function. Typically, you pass an event handle through this structure and, when the callback is executed, this event is signalled and a monitoring thread is informed that the query has been completed.

See [Using WCT](using-wct.md) for an example of wait chain traversal.

## Related topics

[Using WCT](using-wct.md), [WCT Reference](wct-reference.md), [MSDN Magazine 2007 July - Bugslayer: Wait Chain Traversal](https://docs.microsoft.com/archive/msdn-magazine/2007/july/bugslayer-wait-chain-traversal)
