---
description: Represent differences between samples over time, and often use a base value for the calculation.
ms.assetid: 613268ab-386b-421d-a5b5-aab6a065999c
ms.tgt_platform: multiple
title: Basic Algorithm Counter Types
ms.topic: article
ms.date: 05/31/2018
---

# Basic Algorithm Counter Types

Basic algorithm counter types generally represent differences between samples over time, and often use a base value for the calculation. For example, the **PercentFreeSpace** property of the [**Win32\_PerfFormattedData\_PerfDisk\_PhysicalDisk**](/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data) class represents the ratio of the free space available on the physical disk unit to the total usable space provided by the selected physical disk drive. This class also contains the base value, **PercentFreeSpace\_Base**. The percentage of free disk space is obtained by dividing **PercentFreeSpace** by **PercentFreeSpace\_Base** and multiplying by 100%.

The basic algorithms in the following table are provided.



| CounterType Constant                                                                                    | Description                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PERF\_RAW\_FRACTION](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 537003008<br/>       | Ratio of a subset to its set as a percentage. This counter type displays the current percentage only, not an average over time.                                    |
| [PERF\_SAMPLE\_FRACTION](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 549585920<br/>    | Average ratio of hits to all operations during the last two sample intervals. This counter type requires a base property with the PERF\_SAMPLE\_BASE counter type. |
| [PERF\_COUNTER\_DELTA](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 4195328<br/>        | This counter type shows the change in the measured attribute between the two most recent sample intervals.                                                         |
| [PERF\_COUNTER\_LARGE\_DELTA](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 4195584<br/> | Same as PERF\_COUNTER\_DELTA but a 64-bit representation for larger values.                                                                                        |
| [PERF\_ELAPSED\_TIME](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 807666944<br/>       | Total time between when the process started and the time when this value is calculated.                                                                            |



 

## Related topics

<dl> <dt>

[WMI Performance Counter Types](wmi-performance-counter-types.md)
</dt> </dl>

 

