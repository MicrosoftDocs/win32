---
description: Queue-length algorithm counter types increment the number of items in a queue at each sample interval as specified by the appropriate frequency property&\#8212;Frequency\_PerfTime, and so on.
ms.assetid: 514b1a79-ed9d-4ec6-a6ea-b3490291ce18
ms.tgt_platform: multiple
title: Queue-length Algorithm Counter Types
ms.topic: article
ms.date: 05/31/2018
---

# Queue-length Algorithm Counter Types

Queue-length algorithm counter types increment the number of items in a queue at each sample interval as specified by the appropriate frequency property Frequency\_PerfTime, and so on. The cooked result divides by the number of samples to produce the average queue length.

An example is the **AvgDiskQueueLength** property in the [**Win32\_PerfRawData\_PerfDisk\_LogicalDisk**](./retrieving-raw-and-formatted-performance-data.md) that uses the PERF\_COUNTER\_100NS\_QUEUELEN\_TYPE counter type.



| CounterType Constant                                                                                                 | Description                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PERF\_COUNTER\_QUEUELEN\_TYPE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 4523008<br/>            | Average length of a queue to a resource over time. It shows the difference between the queue lengths observed during the last two sample intervals divided by the duration of the interval.                       |
| [PERF\_COUNTER\_LARGE\_QUEUELEN\_TYPE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 4523264<br/>     | Average length of a queue to a resource over time. Counters of this type display the difference between the queue lengths observed during the last two sample intervals, divided by the duration of the interval. |
| [PERF\_COUNTER\_100NS\_QUEUELEN\_TYPE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 5571840<br/>     | Average length of a queue to a resource over time in 100 nanosecond units.                                                                                                                                        |
| [PERF\_COUNTER\_OBJ\_TIME\_QUEUELEN\_TYPE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 6620416<br/> | Time an object is in a queue.                                                                                                                                                                                     |



 

## Related topics

<dl> <dt>

[WMI Performance Counter Types](wmi-performance-counter-types.md)
</dt> </dl>

 

