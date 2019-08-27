---
title: Timer Resolution
description: Timer Resolution
ms.assetid: '2e5e94fe-8175-417f-8c59-9d5cf052ea89'
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
- timeEndPeriod function
ms.topic: article
ms.date: 05/31/2018
---

# Timer Resolution

To determine the minimum and maximum timer resolutions supported by the timer services, use the [**timeGetDevCaps**](/windows/desktop/api/TimeAPI/nf-timeapi-timegetdevcaps) function. This function fills the **wPeriodMin** and **wPeriodMax** members of the [**TIMECAPS**](/windows/desktop/api/TimeAPI/ns-timeapi-timecaps) structure with the minimum and maximum resolutions. This range can vary across computers and Windows platforms.

After you determine the minimum and maximum available timer resolutions, you must establish the minimum resolution you want your application to use. Use the [**timeBeginPeriod**](/windows/desktop/api/TimeAPI/nf-timeapi-timebeginperiod) and [**timeEndPeriod**](/windows/desktop/api/TimeAPI/nf-timeapi-timeendperiod) functions to set and clear this resolution. You must match each call to **timeBeginPeriod** with a call to **timeEndPeriod**, specifying the same minimum resolution in both calls. An application can make multiple **timeBeginPeriod** calls, as long as each call is matched with a call to **timeEndPeriod**.

In both [**timeBeginPeriod**](/windows/desktop/api/TimeAPI/nf-timeapi-timebeginperiod) and [**timeEndPeriod**](/windows/desktop/api/TimeAPI/nf-timeapi-timeendperiod), the *uPeriod* parameter indicates the minimum timer resolution, in milliseconds. You can specify any timer resolution value within the range supported by the timer.

## Related topics

<dl> <dt>

[About Multimedia Timers](about-multimedia-timers.md)
</dt> </dl>

 

 




