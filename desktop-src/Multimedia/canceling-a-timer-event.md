---
title: Canceling a Timer Event
description: Canceling a Timer Event
ms.assetid: 4c1be031-e3d5-4d7c-b197-c40c61fc4e2f
keywords:
- multimedia timers,events
- timers,events
- timeKillEvent function
- cancelling timer events
- multimedia timers,cancelling events
- timers,cancelling events
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Canceling a Timer Event

\[The feature associated with this page, [Multimedia Timers](/windows/win32/multimedia/multimedia-timers), is a legacy feature. It has been superseded by [Multimedia Class Scheduler Service](/windows/win32/procthread/multimedia-class-scheduler-service). **Multimedia Class Scheduler Service** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Multimedia Class Scheduler Service** instead of **Multimedia Timers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This topic describes an obsolete function. New applications should use the [**CreateTimerQueueTimer**](/windows/desktop/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-createtimerqueuetimer) function to create timers.

 

For every periodic timer creating by calling [**timeSetEvent**](/previous-versions//dd757634(v=vs.85)), the application must cancel the timer by calling the [**timeKillEvent**](/previous-versions//dd757630(v=vs.85)) function before it frees the memory that contains the callback function. To cancel a timer event, it might call the following function.


```C++
void DestroyTimer(NPSEQ npSeq)
{
    if(npSeq->wTimerID) {                // is timer event pending?
        timeKillEvent(npSeq->wTimerID);  // cancel the event
        npSeq->wTimerID = 0;
    }
} 
```



## Related topics

<dl> <dt>

[Using Multimedia Timers](using-multimedia-timers.md)
</dt> </dl>

 

 