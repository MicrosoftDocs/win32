---
title: Starting a Single Timer Event
description: Starting a Single Timer Event
ms.assetid: '56010877-1a02-4a7b-b58c-9f96b169acb2'
keywords: ["multimedia timers,events", "timers,events", "multimedia timers,starting events", "timers,starting events", "timeSetEvent function", "starting timer events", "single timer events"]
---

# Starting a Single Timer Event

> [!Note]  
> This topic describes an obsolete function. New applications should use the [**CreateTimerQueueTimer**](https://msdn.microsoft.com/library/windows/desktop/ms682485) function to create timers.

 

To start a single timer event, call the [**timeSetEvent**](timesetevent.md) function, specifying the amount of time before the callback occurs, the resolution, the address of the callback function (see [**TimeProc**](timeproc.md)), and the user data to supply with the callback function. An application can use a function like the following to start a single timer event.


```C++
UINT SetTimerCallback(NPSEQ npSeq,  // sequencer data
    UINT msInterval)                // event interval
{ 
    npSeq->wTimerID = timeSetEvent(
        msInterval,                    // delay
        wTimerRes,                     // resolution (global variable)
        OneShotCallback,               // callback function
        (DWORD)npSeq,                  // user data
        TIME_ONESHOT );                // single timer event
    if(! npSeq->wTimerID)
        return ERR_TIMER;
    else
        return ERR_NOERROR;
} 

```



For an example of the callback function OneShotCallback, see [Writing a Timer Callback Function](writing-a-timer-callback-function.md).

## Related topics

<dl> <dt>

[Using Multimedia Timers](using-multimedia-timers.md)
</dt> </dl>

 

 




