---
Description: The performance counter type designates a formula required to obtain calculated performance counters. These are the same counter types used by Windows Performance Monitoring.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d4a9feca-80a2-4ce5-b4d7-4e83ef951c08
ms.tgt_platform: multiple
title: WMI Performance Counter Types
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WMI Performance Counter Types

The performance [counter type](Http://Go.Microsoft.Com/FWLink/p/?LinkID=44341) designates a formula required to obtain calculated performance counters. These are the same counter types used by Windows [Performance Monitoring](https://msdn.microsoft.com/library/windows/desktop/aa373083). In WMI performance classes, the raw data for the counter type formula comes from a [**Win32\_PerfRawData**](https://msdn.microsoft.com/library/aa394299) class and the calculated result is found in the same-named property of a corresponding [**Win32\_PerfFormattedData**](https://msdn.microsoft.com/library/aa394253) class.

Counter types appear as the **CounterType** qualifier for properties in [**Win32\_PerfRawData**](https://msdn.microsoft.com/library/aa394299) classes, and as the **CookingType** qualifier for properties in [**Win32\_PerfFormattedData**](https://msdn.microsoft.com/library/aa394253) classes.

For example, the **AvgDiskBytesPerRead** property in the [**Win32\_PerfRawData\_PerfDisk\_LogicalDisk**](https://msdn.microsoft.com/library/aa394307) class is the raw data source for the **AvgDiskBytesPerRead** property in the class [**Win32\_PerfFormattedData\_PerfDisk\_LogicalDisk**](https://msdn.microsoft.com/library/aa394261), which contains the same data as shown in System Monitor.

The following list organizes counter type descriptions by functional type:

-   [Base Counter Types](base-counter-types.md)
-   [Basic Algorithm Counter Types](basic-algorithm-counter-types.md)
-   [Counter Algorithm Counter Types](counter-algorithm-counter-types.md)
-   [Noncomputational Counter Types](noncomputational-counter-types.md)
-   [Precision Timer Algorithm Counter Types](precision-timer-algorithm-counter-types.md)
-   [Queue-length Algorithm Counter Types](queue-length-algorithm-counter-types.md)
-   [Statistical Counter Types](statistical-counter-types.md)
-   [Timer Algorithm Counter Types](timer-algorithm-counter-types.md)

 

 



