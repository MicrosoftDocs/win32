---
description: 'You can consume performance data by using one of the following interfaces: The Performance Data Helper (PDH) interface, which provides high-level access to data from both version 1 and version 2 performance counter providers.The registry interface, which provides low-level access to data from performance counter providers.The performance library interface, which provides direct access to data from version 2 performance counter providers.The PDH interface is easier to use than the registry interface and is recommended for most performance data collection tasks. The PDH interface is essentially a higher-level abstraction of the functionality that the registry interface provides. Use the performance library interface only if you cannot use the PDH abstraction-layer functions.'
ms.assetid: a42f6cdd-47e9-4f43-aeaf-37a5abb0fa36
title: Consuming Counter Data
ms.topic: article
ms.date: 08/17/2020
---

# Consuming Counter Data

Programs that want to read and make use of Windows Performance Counter data can use one of several interfaces as appropriate for the scenario.

- Scripts can use the [WMI Performance Counter Classes](/windows/desktop/WmiSdk/monitoring-performance-data) or the [TypePerf](/windows-server/administration/windows-commands/typeperf) tool.
- .NET programs can use the [PerformanceCounter Class](/dotnet/api/system.diagnostics.performancecounter).
- The [Performance Data Helper (PDH) library](using-the-pdh-functions-to-consume-counter-data.md) provides high-level access to data from both V1 and V2 performance counter providers via a Win32 (C/C++) API.
- The [registry interface](using-the-registry-functions-to-consume-counter-data.md) provides access to data from both V1 and V2 performance counter providers via the special `HKEY_PERFORMANCE_DATA` registry key.
- The [PerfLib V2 Consumer functions](using-the-perflib-functions-to-consume-counter-data.md) provide low-level access to data from V2 performance counter providers via a Win32 (C/C++) API.

The PDH interface is recommended for most C/C++ performance data collection tasks because it is easier to use than the registry and PerfLib interfaces.
