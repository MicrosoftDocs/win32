---
description: Learn how to use wait chain traversal (WCT) to let debuggers diagnose application hangs and deadlocks.
ms.assetid: d266a663-b101-4936-9574-f6ce223419ae
title: Wait chain traversal
ms.topic: article
ms.date: 02/06/2023
ms.custom: contperf-fy21q1
---

# Wait chain traversal

Wait chain traversal (WCT) allows debuggers to diagnose application hangs and deadlocks.

A *wait chain* is an alternating sequence of threads and synchronization objects where each thread waits for the object that follows. Each object that follows is, in turn, owned by the subsequent thread in the chain.

A thread waits for a synchronization object from the time the thread requests the object until it's acquired. This *lock* is owned by a thread from the time the thread acquires it, until the thread releases it. In other words, when thread 1 is waiting for a lock that's owned by thread 2, thread 1 is *waiting* for thread 2.

WCT supports the following synchronization primitives:

- [Advanced local procedure call (ALPC)](../etw/alpc.md)
- [Microsoft Component Object Model (COM)](../com/the-component-object-model.md)
- [Critical section objects](../sync/critical-section-objects.md)
- [Mutex objects](../sync/mutex-objects.md)
- [SendMessage function](/windows/win32/api/winuser/nf-winuser-sendmessage)
- [Wait](../sync/wait-functions.md) operations on [processes and threads](../procthread/processes-and-threads.md)

To retrieve the wait chain for one or more threads, create a WCT session by using the [OpenThreadWaitChainSession](/windows/desktop/api/Wct/nf-wct-openthreadwaitchainsession) and [GetThreadWaitChain](/windows/desktop/api/Wct/nf-wct-getthreadwaitchain) functions. WCT sessions are represented by a handle of type *HWCT*.

## Sessions can be synchronous or asynchronous

You can't cancel synchronous sessions, and block the calling thread, until a wait chain has been retrieved.

Asynchronous sessions don't block the calling thread, and can be canceled by the application using the [CloseThreadWaitChainSession](/windows/desktop/api/Wct/nf-wct-closethreadwaitchainsession) function. Results from asynchronous operations are made available through a [WaitChainCallback](/windows/win32/api/wct/nc-wct-pwaitchaincallback) callback function provided by the application.

For asynchronous sessions, the caller can specify a pointer to a context data structure through [GetThreadWaitChain](/windows/desktop/api/Wct/nf-wct-getthreadwaitchain). This same pointer is passed to the [WaitChainCallback](/windows/win32/api/wct/nc-wct-pwaitchaincallback) callback function).

The context data structure is user defined and opaque to WCT. It can be used by the application to communicate context between a WCT query and a callback function. Typically, you pass an event handle through this structure and, when the callback is executed, this event is signalled and a monitoring thread is informed that the query has been completed.

For an example of wait chain traversal, see [Using WCT](using-wct.md).

## See also

- [Using WCT](using-wct.md)
- [WCT reference](wct-reference.md)
- [Bugslayer: Wait Chain Traversal](/archive/msdn-magazine/2007/july/bugslayer-wait-chain-traversal) from *MSDN Magazine*
