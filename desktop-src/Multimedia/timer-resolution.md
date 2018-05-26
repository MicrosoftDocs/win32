---
title: Timer Resolution
description: Timer Resolution
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
- timeEndPeriod function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Timer Resolution

To determine the minimum and maximum timer resolutions supported by the timer services, use the [**timeGetDevCaps**](/windows/win32/TimeAPI/nf-timeapi-timegetdevcaps?branch=master) function. This function fills the **wPeriodMin** and **wPeriodMax** members of the [**TIMECAPS**](/windows/win32/TimeAPI/ns-timeapi-timecaps_tag?branch=master) structure with the minimum and maximum resolutions. This range can vary across computers and Windows platforms.

After you determine the minimum and maximum available timer resolutions, you must establish the minimum resolution you want your application to use. Use the [**timeBeginPeriod**](/windows/win32/TimeAPI/nf-timeapi-timebeginperiod?branch=master) and [**timeEndPeriod**](/windows/win32/TimeAPI/nf-timeapi-timeendperiod?branch=master) functions to set and clear this resolution. You must match each call to **timeBeginPeriod** with a call to **timeEndPeriod**, specifying the same minimum resolution in both calls. An application can make multiple **timeBeginPeriod** calls, as long as each call is matched with a call to **timeEndPeriod**.

In both [**timeBeginPeriod**](/windows/win32/TimeAPI/nf-timeapi-timebeginperiod?branch=master) and [**timeEndPeriod**](/windows/win32/TimeAPI/nf-timeapi-timeendperiod?branch=master), the *uPeriod* parameter indicates the minimum timer resolution, in milliseconds. You can specify any timer resolution value within the range supported by the timer.

## Related topics

<dl> <dt>

[About Multimedia Timers](about-multimedia-timers.md)
</dt> </dl>

 

 




