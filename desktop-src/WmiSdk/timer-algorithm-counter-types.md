---
description: Timer algorithm counter types are based on the amount of increased use of the performance object over a sample period.
ms.assetid: 4ec49efc-2b0f-4205-8b58-fb121da32b4e
ms.tgt_platform: multiple
title: Timer Algorithm Counter Types
ms.topic: article
ms.date: 05/31/2018
---

# Timer Algorithm Counter Types

Timer algorithm counter types are based on the amount of increased use of the performance object over a sample period. The counter data is an increasing quantum measure of the total activity for an object up to the time that the sample takes place. The difference between the two samples indicates the total time that the object is active during the sample time period.

Dividing by the sample period results in a proportion of time that the object is active during a time period. Dividing by the number of internal polling interrupts determines the average use between polling samples.

For example, the **AvgDiskSecPerRead** property in the [**Win32\_PerfRawData\_PerfDisk\_PhysicalDisk**](/previous-versions//aa394308(v=vs.85)) class uses the **PERF\_AVERAGE\_TIMER** countertype. It calculates the average time in seconds of a read of data from the disk, and requires the base property **AvgDiskSecPerRead\_Base**. Unlike **PERF\_COUNTER\_TIMER**, the average timer base represents an accumulating number of operations, and the counter data is a running time value, which means that when divided by the time base, it yields the total time of all operations in seconds.



| Counter Type Constant                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PERF\_COUNTER\_TIMER](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 541132032<br/>             | Average time that a component is active as a percentage of the total sample time.<br/>                                                                                                                                                                                                                                                                                                         |
| [PERF\_COUNTER\_TIMER\_INV](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 557909248<br/>        | Average percentage of time observed during sample interval that the object is not active. This counter type is the same as **PERF\_100NSEC\_TIMER\_INV** except that it measures time in units of ticks of the system performance timer rather than in 100ns units.<br/>                                                                                                                       |
| [PERF\_AVERAGE\_TIMER](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 805438464<br/>             | Average time to complete a process or operation. This counter type displays a ratio of the total elapsed time of the sample interval to the number of processes or operations completed during that time.<br/> This counter type requires a base property with **PERF\_AVERAGE\_BASE** as the counter type.<br/>                                                                         |
| [PERF\_100NSEC\_TIMER](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 542180608<br/>             | Active time of one component as a percentage of the total elapsed time in units of 100ns of the sample interval.<br/>                                                                                                                                                                                                                                                                          |
| [PERF\_100NSEC\_TIMER\_INV](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 558957824<br/>        | Percentage of time the object was not in use. This counter type is the same as **PERF\_COUNTER\_TIMER\_INV** except that it measures time in 100ns units rather than in system performance timer ticks.<br/>                                                                                                                                                                                   |
| [PERF\_COUNTER\_MULTI\_TIMER](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 574686464<br/>      | Active time of one or more components as a percentage of the total time of the sample interval. This counter type differs from **PERF\_100NSEC\_MULTI\_TIMER** in that it measures time in units of ticks of the system performance timer, rather than in 100ns units.<br/> This counter type requires a base property with the **PERF\_COUNTER\_MULTI\_BASE** counter type.<br/>        |
| [PERF\_COUNTER\_MULTI\_TIMER\_INV](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 591463680<br/> | Inactive time of one or more components as a percentage of the total time of the sample interval. This counter type differs from **PERF\_100NSEC\_MULTI\_TIMER\_INV** in that it measures time in units of ticks of the system performance timer, rather than in 100ns units.<br/> This counter type requires a base property with the **PERF\_COUNTER\_MULTI\_BASE** counter type.<br/> |
| [PERF\_100NSEC\_MULTI\_TIMER](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 575735040<br/>      | This counter type shows the active time of one or more components as a percentage of the total time (100ns units) of the sample interval.<br/> This counter type requires a base property with the **PERF\_COUNTER\_MULTI\_BASE** counter type.<br/>                                                                                                                                     |
| [PERF\_100NSEC\_MULTI\_TIMER\_INV](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 592512256<br/> | Inactive time of one or more components as a percentage of the total time of the sample interval. Counters of this type measure time in 100ns units.<br/> This counter type requires a base property with the **PERF\_COUNTER\_MULTI\_BASE** counter type.<br/>                                                                                                                          |
| [PERF\_OBJ\_TIME\_TIMER](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))<br/> Decimal 543229184<br/>           | A 64-bit timer in object-specific units.<br/>                                                                                                                                                                                                                                                                                                                                                  |



 

## Related topics

<dl> <dt>

[WMI Performance Counter Types](wmi-performance-counter-types.md)
</dt> </dl>

 

