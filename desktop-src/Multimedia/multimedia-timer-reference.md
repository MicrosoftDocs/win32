---
title: Multimedia Timer Reference
description: Multimedia Timer Reference
ms.assetid: e96bc9a6-4e9d-4231-9e35-4a6ff59e6521
keywords:
- Windows multimedia,timer reference
- multimedia,timer reference
- multimedia input,timer reference
- multimedia timers,reference
- timers,reference
- reference for timers,about
- timer reference,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Multimedia Timer Reference

\[The feature associated with this page, [Multimedia Timers](/windows/win32/multimedia/multimedia-timers), is a legacy feature. It has been superseded by [Multimedia Class Scheduler Service](/windows/win32/procthread/multimedia-class-scheduler-service). **Multimedia Class Scheduler Service** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Multimedia Class Scheduler Service** instead of **Multimedia Timers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes the functions and structures associated with multimedia timer services. These elements are grouped as follows.

## Retrieving the System Time

-   [**MMTIME**](/previous-versions//dd757347(v=vs.85))
-   [**timeGetSystemTime**](/windows/desktop/api/TimeAPI/nf-timeapi-timegetsystemtime)
-   [**timeGetTime**](/windows/desktop/api/TimeAPI/nf-timeapi-timegettime)

## Retrieving Timer Information

-   [**TIMECAPS**](/windows/desktop/api/TimeAPI/ns-timeapi-timecaps)
-   [**timeGetDevCaps**](/windows/desktop/api/TimeAPI/nf-timeapi-timegetdevcaps)

## Time Events

-   [**timeKillEvent**](/previous-versions//dd757630(v=vs.85))
-   [**TimeProc**](/previous-versions//dd757631(v=vs.85))
-   [**timeSetEvent**](/previous-versions//dd757634(v=vs.85))

## Time Periods

-   [**timeBeginPeriod**](/windows/desktop/api/TimeAPI/nf-timeapi-timebeginperiod)
-   [**timeEndPeriod**](/windows/desktop/api/TimeAPI/nf-timeapi-timeendperiod)

## Related topics

<dl> <dt>

[Multimedia Timers](multimedia-timers.md)
</dt> </dl>

 

 