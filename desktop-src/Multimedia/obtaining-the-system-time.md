---
title: Obtaining the System Time
description: Obtaining the System Time
ms.assetid: 33dfcd56-11d9-45b9-b983-8354526101a7
keywords:
- multimedia timers,system time
- timers,system time
- system time
- timeGetTime function
- timeGetSystemTime function
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining the System Time

Typically, before an application begins using the multimedia timer services, it retrieves the current *system time*. The system time is the time, in milliseconds, since the Microsoft Windows operating system was started. You can use the [**timeGetTime**](/windows/desktop/api/TimeAPI/nf-timeapi-timegettime) or [**timeGetSystemTime**](/windows/desktop/api/TimeAPI/nf-timeapi-timegetsystemtime) function to retrieve the system time. These two functions are very similar: **timeGetTime** returns the system time, and **timeGetSystemTime** fills an [**MMTIME**](/previous-versions//dd757347(v=vs.85)) structure with the system time.

 

 