---
title: Obtaining the System Time
description: Obtaining the System Time
ms.assetid: '33dfcd56-11d9-45b9-b983-8354526101a7'
keywords: ["multimedia timers,system time", "timers,system time", "system time", "timeGetTime function", "timeGetSystemTime function"]
---

# Obtaining the System Time

Typically, before an application begins using the multimedia timer services, it retrieves the current *system time*. The system time is the time, in milliseconds, since the Microsoft Windows operating system was started. You can use the [**timeGetTime**](timegettime.md) or [**timeGetSystemTime**](timegetsystemtime.md) function to retrieve the system time. These two functions are very similar: **timeGetTime** returns the system time, and **timeGetSystemTime** fills an [**MMTIME**](mmtime.md) structure with the system time.

 

 




