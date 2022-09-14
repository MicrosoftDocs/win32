---
description: The CreateTimerQueue function creates a queue for timers.
ms.assetid: ee85a6c3-3a1d-4f94-9112-cb8247b2a189
title: Timer Queues
ms.topic: article
ms.date: 05/31/2018
---

# Timer Queues

The [**CreateTimerQueue**](/windows/win32/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-createtimerqueue) function creates a queue for timers. Timers in this queue, known as *timer-queue timers*, are lightweight objects that enable you to specify a callback function to be called when the specified due time arrives. The wait operation is performed by a thread in the [thread pool](../procthread/thread-pooling.md).

To add a timer to the queue, call the [**CreateTimerQueueTimer**](/windows/win32/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-createtimerqueuetimer) function. To update a timer-queue timer, call the [**ChangeTimerQueueTimer**](/windows/win32/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-changetimerqueuetimer) function. You can specify a callback function to be executed by a worker thread from the thread pool when the timer expires.

To cancel a pending timer, call the [**DeleteTimerQueueTimer**](/windows/win32/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-deletetimerqueuetimer) function. When you are finished with the queue of timers, call the [**DeleteTimerQueueEx**](/windows/win32/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-deletetimerqueueex) function to delete the timer queue. Any pending timers in the queue are canceled and deleted.

## Related topics

<dl> <dt>

[Using Timer Queues](using-timer-queues.md)
</dt> </dl>

 

 
