---
Description: The COOKER\_AVERAGE counter type formula provides the statistical midpoint of the data for a counter.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5121cd02-b122-48fd-995a-cf6c77948fd8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: COOKER\_AVERAGE
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# COOKER\_AVERAGE

The COOKER\_AVERAGE counter type formula provides the statistical midpoint of the data for a counter. The formula for this counter type sums repeated observations of one property in a [**Win32\_PerfRawData**](https://msdn.microsoft.com/library/aa394299) instance, and divides the sum by the number of observations. This counter type is defined only within WMI, and it is not available to the performance monitoring technologies, such as [Performance Counters Version 6.0](https://msdn.microsoft.com/library/windows/desktop/aa373083).

For more information about the counter type formula, see [Counter Types](http://go.microsoft.com/fwlink/p/?linkid=44341).

For more information about WMI high-performance providers and scripting, see [WMI Performance Counter Types](wmi-performance-counter-types.md).

## Example Code

For code examples, see [Obtaining Statistical Performance Data](obtaining-statistical-performance-data.md).

## Related topics

<dl> <dt>

[Statistical Counter Types](statistical-counter-types.md)
</dt> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> </dl>

 

 



