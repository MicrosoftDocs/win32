---
Description: The CreateTimerQueue function creates a queue for timers.
ms.assetid: ee85a6c3-3a1d-4f94-9112-cb8247b2a189
title: Timer Queues
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Timer Queues

The [**CreateTimerQueue**](/windows/desktop/api/WinBase/) function creates a queue for timers. Timers in this queue, known as *timer-queue timers*, are lightweight objects that enable you to specify a callback function to be called when the specified due time arrives. The wait operation is performed by a thread in the [thread pool](https://msdn.microsoft.com/windows/desktop/a5e52080-35d4-47f5-9050-90889e3bf2f8).

To add a timer to the queue, call the [**CreateTimerQueueTimer**](/windows/desktop/api/WinBase/) function. To update a timer-queue timer, call the [**ChangeTimerQueueTimer**](/windows/desktop/api/WinBase/) function. You can specify a callback function to be executed by a worker thread from the thread pool when the timer expires.

To cancel a pending timer, call the [**DeleteTimerQueueTimer**](/windows/desktop/api/WinBase/) function. When you are finished with the queue of timers, call the [**DeleteTimerQueueEx**](/windows/desktop/api/WinBase/) function to delete the timer queue. Any pending timers in the queue are canceled and deleted.

## Related topics

<dl> <dt>

[Using Timer Queues](using-timer-queues.md)
</dt> </dl>

 

 



