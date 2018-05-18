---
title: Timer Resolution
description: Timer Resolution
ms.assetid: '237a6770-89b9-4922-b9e9-0e0bf3e0c9b6'
keywords: ["multimedia timers,resolution", "timers,resolution", "minimum timer resolution", "maximum timer resolution", "multimedia timers,maximum resolution", "timers,maximum resolution", "multimedia timers,minimum resolution", "timers,minimum resolution", "timeGetDevCaps function", "timeBeginPeriod function", "timeEndPeriod function"]
---

# Timer Resolution

To determine the minimum and maximum timer resolutions supported by the timer services, use the [**timeGetDevCaps**](timegetdevcaps.md) function. This function fills the **wPeriodMin** and **wPeriodMax** members of the [**TIMECAPS**](timecaps.md) structure with the minimum and maximum resolutions. This range can vary across computers and Windows platforms.

After you determine the minimum and maximum available timer resolutions, you must establish the minimum resolution you want your application to use. Use the [**timeBeginPeriod**](timebeginperiod.md) and [**timeEndPeriod**](timeendperiod.md) functions to set and clear this resolution. You must match each call to **timeBeginPeriod** with a call to **timeEndPeriod**, specifying the same minimum resolution in both calls. An application can make multiple **timeBeginPeriod** calls, as long as each call is matched with a call to **timeEndPeriod**.

In both [**timeBeginPeriod**](timebeginperiod.md) and [**timeEndPeriod**](timeendperiod.md), the *uPeriod* parameter indicates the minimum timer resolution, in milliseconds. You can specify any timer resolution value within the range supported by the timer.

## Related topics

<dl> <dt>

[About Multimedia Timers](about-multimedia-timers.md)
</dt> </dl>

 

 




