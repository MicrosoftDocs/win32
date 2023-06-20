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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Writing a Timer Callback Function

\[The feature associated with this page, [Multimedia Timers](/windows/win32/multimedia/multimedia-timers), is a legacy feature. It has been superseded by [Multimedia Class Scheduler Service](/windows/win32/procthread/multimedia-class-scheduler-service). **Multimedia Class Scheduler Service** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Multimedia Class Scheduler Service** instead of **Multimedia Timers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 