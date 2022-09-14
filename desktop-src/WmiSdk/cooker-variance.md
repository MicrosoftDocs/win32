---
description: The COOKER\_VARIANCE counter type formula provides variability that use to characterize dispersion for a set of raw observations of one property in a Win32\_PerfRawData instance.
ms.assetid: 6b184a36-7d22-41ab-98e7-b185d1063bcb
ms.tgt_platform: multiple
title: COOKER_VARIANCE
ms.topic: article
ms.date: 05/31/2018
---

# COOKER\_VARIANCE

The COOKER\_VARIANCE counter type formula provides variability that use to characterize dispersion for a set of raw observations of one property in a [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) instance. The variance is calculated by dividing the sum of the square of the deviation from the mean of each counter by the number of counters. In other words, the variance is the average of the squared deviations from the mean for each counter. This counter type is defined only within WMI, and it is not available to the performance monitoring technologies, such as [Performance Counters Version 6.0](/windows/desktop/PerfCtrs/performance-counters-portal).

For more information about the counter type formula, see [Counter Types](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10)).

For more information about high-performance providers and scripting, see [WMI Performance Counter Types](wmi-performance-counter-types.md).

## Example Code

For code examples, see [Obtaining Statistical Performance Data](obtaining-statistical-performance-data.md).

## Related topics

<dl> <dt>

[Statistical Counter Types](statistical-counter-types.md)
</dt> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> </dl>

 

 
