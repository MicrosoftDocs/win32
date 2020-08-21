---
title: Writing a Timer Callback Function
description: Writing a Timer Callback Function
ms.assetid: 85260b6b-42de-43f4-83b7-94edbf660006
keywords:
- multimedia timers,callback functions
- timers,callback functions
- writing timer callback functions
- multimedia timers,writing callback functions
- timers,writing callback functions
ms.topic: article
ms.date: 05/31/2018
---

# Writing a Timer Callback Function

> [!Note]  
> This topic describes an obsolete function. New applications should use the [**CreateTimerQueueTimer**](/windows/desktop/api/threadpoollegacyapiset/nf-threadpoollegacyapiset-createtimerqueuetimer) function to create timers.

 

The following callback function, OneShotTimer, invalidates the identifier for the single timer event and calls a timer routine to handle the application-specific tasks. For more information, see [**TimeProc**](/previous-versions//dd757631(v=vs.85)).


```C++
void CALLBACK OneShotTimer(UINT wTimerID, UINT msg, 
    DWORD dwUser, DWORD dw1, DWORD dw2) 
{ 
    NPSEQ npSeq;             // pointer to sequencer data 
    npSeq = (NPSEQ)dwUser;
    npSeq->wTimerID = 0;     // invalidate timer ID (no longer in use)
    TimerRoutine(npSeq);     // handle tasks 
} 
```



## Related topics

<dl> <dt>

[Using Multimedia Timers](using-multimedia-timers.md)
</dt> </dl>

 

 