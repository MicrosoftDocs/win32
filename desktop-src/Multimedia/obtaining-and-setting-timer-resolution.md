---
title: Obtaining and Setting Timer Resolution
description: Obtaining and Setting Timer Resolution
ms.assetid: 237a6770-89b9-4922-b9e9-0e0bf3e0c9b6
keywords:
- multimedia timers,resolution
- timers,resolution
- minimum timer resolution
- maximum timer resolution
- multimedia timers,maximum resolution
- timers,maximum resolution
- multimedia timers,minimum resolution
- timers,minimum resolution
- timeGetDevCaps function
- timeBeginPeriod function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining and Setting Timer Resolution

The following example calls the [**timeGetDevCaps**](/windows/win32/TimeAPI/nf-timeapi-timegetdevcaps?branch=master) function to determine the minimum and maximum timer resolutions supported by the timer services. Before it sets up any timer events, the example establishes the minimum timer resolution by using the [**timeBeginPeriod**](/windows/win32/TimeAPI/nf-timeapi-timebeginperiod?branch=master) function.


```C++
#define TARGET_RESOLUTION 1         // 1-millisecond target resolution

TIMECAPS tc;
UINT     wTimerRes;

if (timeGetDevCaps(&amp;tc, sizeof(TIMECAPS)) != TIMERR_NOERROR) 
{
    // Error; application can't continue.
}

wTimerRes = min(max(tc.wPeriodMin, TARGET_RESOLUTION), tc.wPeriodMax);
timeBeginPeriod(wTimerRes); 
```



## Related topics

<dl> <dt>

[Using Multimedia Timers](using-multimedia-timers.md)
</dt> </dl>

 

 




