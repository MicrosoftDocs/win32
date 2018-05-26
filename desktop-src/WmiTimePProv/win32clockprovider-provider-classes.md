---
Description: This section provides reference information for Win32ClockProvider provider classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 69C4CEF4-AD41-40B1-980B-92028485D76B
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32ClockProvider Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32ClockProvider Provider

This section provides reference information for **Win32ClockProvider** provider classes.

## In this section

<dl> <dt>

[**Win32\_CurrentTime**](win32-currenttime.md)
</dt> <dd>

The [**Win32\_CurrentTime**](win32-currenttime.md) abstract is a singleton [WMI class](https://msdn.microsoft.com/library/aa393244) that describes a point in time by using the component items, such as milliseconds, seconds, minutes, hours, days, days of the week, week in the month, months, quarters, and years.

</dd> <dt>

[**Win32\_LocalTime**](win32-localtime.md)
</dt> <dd>

The [**Win32\_LocalTime**](win32-localtime.md) [WMI class](https://msdn.microsoft.com/library/aa393244) describes a point in time returned as **Win32\_LocalTime** objects that result from a query. These are returned as the value for the **TargetInstance** property in the [**\_\_InstanceModificationEvent**](https://msdn.microsoft.com/library/aa394651) system class. The **Hour** property is returned as the local time on a 24-hour clock.

</dd> <dt>

[**Win32\_UTCTime**](win32-utctime.md)
</dt> <dd>

The [**Win32\_UTCTime**](win32-utctime.md)[WMI class](https://msdn.microsoft.com/library/aa393244) describes a point in time that is returned as **Win32\_UTCTime** objects that result from a query. These are returned as the value for the **TargetInstance** property in the [**\_\_InstanceModificationEvent**](https://msdn.microsoft.com/library/aa394651) system class. The **Hour** property is returned as the Coordinated Universal Time (UTC) time on a 24–hour clock.

</dd> </dl>

 

 



