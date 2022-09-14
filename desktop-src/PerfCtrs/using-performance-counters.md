---
description: To consume counter data, see Consuming Counter Data.
ms.assetid: fff8bc4a-3d7a-4d70-ba03-347f9f063c84
title: Using Performance Counters
ms.topic: article
ms.date: 08/17/2020
---

# Using Performance Counters

Performance counter **consumers** are software components that collect and make use of performance counter data. Example consumers provided by Microsoft include Performance Monitor (perfmon.exe), Resource Monitor (resmon.exe), Log Manager (logman.exe) and typeperf.exe. Third-party software components may also collect performance data via performance collection APIs or via WMI performance counter classes.

Performance counter **providers** are software components that publish performance counter data. Performance counters can be provided by operating system components, device drivers, and services. Many performance counters are provided as part of the Windows operating system. Additional counters may be provided by third-party software components via the performance counter provider APIs.

- Use [Performance Counter Tools](performance-counters-tools.md) when you want to collect or view the counter data from a system.
- Use [Performance Counter Consumer APIs](consuming-counter-data.md) when you want to write a program that collects counter data from the local system.
- Use [WMI Performance Counter Classes](/windows/desktop/WmiSdk/monitoring-performance-data) when you want to collect counter data from a local or remote system using WMI.
- Use [Work Unit performance counter](using-workunit-perf_counters.md) when you want learn about the deeper processes running within an application.
- Use [Performance Counter Provider APIs](providing-counter-data.md) when you want to publish performance counter data from your software component.

## See also

[About Performance Counters](about-performance-counters.md)

[Performance Counters Reference](performance-counters-reference.md)
