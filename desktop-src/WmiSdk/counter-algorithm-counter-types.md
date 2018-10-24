---
Description: Counter algorithm counter types may calculate rates or averages bytes for a sample or over a time period for a particular operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4423e35e-2a93-4f68-8494-89df05268cc9
ms.tgt_platform: multiple
title: Counter Algorithm Counter Types
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Counter Algorithm Counter Types

Counter algorithm counter types may calculate rates or averages bytes for a sample or over a time period for a particular operation.

The **AvgDiskBytesPerTransfer** property in the [**Win32\_PerfRawData\_PerfDisk\_PhysicalDisk**](https://msdn.microsoft.com/library/aa394308) class uses the PERF\_AVERAGE\_BULK countertype. In this case, the transfer is the operation, and the accumulating number of bytes that are sent is the counter data. For any two samples, dividing the difference of accumulated bytes by the difference in accumulating transfers will produce the average number of bytes per transfer during the period between the samples.

The following counter algorithms are provided:



| CounterType                                                                                              | Description                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PERF\_AVERAGE\_BULK](http://go.microsoft.com/fwlink/p/?linkid=44341)Decimal 1073874176<br/>       | Number of items processed, on average, during an operation. This counter type displays a ratio of the items processed (such as bytes sent) to the number of operations completed, and requires a base property with PERF\_AVERAGE\_BASE as the counter type. |
| [PERF\_COUNTER\_COUNTER](http://go.microsoft.com/fwlink/p/?linkid=44341)Decimal 272696320<br/>     | Average number of operations completed during each second of the sample interval. .                                                                                                                                                                          |
| [PERF\_SAMPLE\_COUNTER](http://go.microsoft.com/fwlink/p/?linkid=44341)Decimal 4260864<br/>        | Average number of operations completed in one second. This counter type requires a base property with the counter type PERF\_SAMPLE\_BASE.                                                                                                                   |
| [PERF\_COUNTER\_BULK\_COUNT](http://go.microsoft.com/fwlink/p/?linkid=44341)Decimal 272696576<br/> | Average number of operations completed during each second of the sample interval. This counter type is the same as the PERF\_COUNTER\_COUNTER type, but it uses larger fields to accommodate larger values.                                                  |



 

## Related topics

<dl> <dt>

[WMI Performance Counter Types](wmi-performance-counter-types.md)
</dt> </dl>

 

 




