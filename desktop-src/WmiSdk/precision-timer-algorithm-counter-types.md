---
description: The precision timer algorithm counter types obtain more accurate readings than system timers.
ms.assetid: f7159645-6287-47a3-895e-20dae6e0892a
ms.tgt_platform: multiple
title: Precision Timer Algorithm Counter Types
ms.topic: article
ms.date: 05/31/2018
---

# Precision Timer Algorithm Counter Types

The precision timer algorithm counter types obtain more accurate readings than system timers. The service that provides the data also provides a timestamp, which eliminates the errors that can occur because of the small and variable time that elapses between capture of the system timestamp and collection of the data from the performance DLL. This base timestamp for precision timers is a PERF\_PRECISION\_TIMESTAMP property, which must immediately follow the PERF\_PRECISION\_TIMER property.



| CounterType Constant                                                                                         | Description                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [PERF\_PRECISION\_SYSTEM\_TIMER](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 541525248<br/> | Similar to PERF\_COUNTER\_TIMER except that it uses a counter defined time base instead of the system timestamp.             |
| [PERF\_PRECISION\_100NS\_TIMER](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 542573824<br/>  | Similar to PERF\_100NSEC\_TIMER except that it uses a 100ns counter defined time base instead of the system 100ns timestamp. |



 

## Related topics

<dl> <dt>

[WMI Performance Counter Types](wmi-performance-counter-types.md)
</dt> </dl>

 

