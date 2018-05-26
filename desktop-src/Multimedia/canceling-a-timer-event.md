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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Canceling a Timer Event

> [!Note]  
> This topic describes an obsolete function. New applications should use the [**CreateTimerQueueTimer**](https://msdn.microsoft.com/library/windows/desktop/ms682485) function to create timers.

 

For every periodic timer creating by calling [**timeSetEvent**](/windows/win32/TimeAPI/?branch=master), the application must cancel the timer by calling the [**timeKillEvent**](/windows/win32/TimeAPI/?branch=master) function before it frees the memory that contains the callback function. To cancel a timer event, it might call the following function.


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

 

 




