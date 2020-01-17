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
ms.date: 05/31/2018
---

# Canceling a Timer Event

> [!Note]  
> This topic describes an obsolete function. New applications should use the [**CreateTimerQueueTimer**](https://docs.microsoft.com/windows/desktop/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-createtimerqueuetimer) function to create timers.

 

For every periodic timer creating by calling [**timeSetEvent**](https://msdn.microsoft.com/library/Dd757634(v=VS.85).aspx), the application must cancel the timer by calling the [**timeKillEvent**](https://msdn.microsoft.com/library/Dd757630(v=VS.85).aspx) function before it frees the memory that contains the callback function. To cancel a timer event, it might call the following function.


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

 

 




