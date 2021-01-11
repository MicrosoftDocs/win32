---
description: Some formulas require both a counter property and base property.
ms.assetid: c14be351-e712-40bd-bab7-5b9ef6cd8a00
ms.tgt_platform: multiple
title: Base Counter Types
ms.topic: article
ms.date: 05/31/2018
---

# Base Counter Types

Some formulas require both a counter property and base property. The base value is the denominator in the formula for the counter type. In raw data [Performance Counter Classes](/windows/desktop/CIMWin32Prov/performance-counter-classes) derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata), the base property must immediately follow the counter property. The base property must have the same name as the preceding counter, with **\_Base** appended.

For example, the **AvgDiskBytesPerRead** property in [**Win32\_PerfRawData\_PerfDisk\_LogicalDisk**](./retrieving-raw-and-formatted-performance-data.md) contains the raw value, in bytes, transferred from the disk during read operations. It has a base property, **AvgDiskBytesPerRead\_Base**, which represents the accumulated number of operations. When WMI applies the formula for the specified counter type, **PERF\_AVERAGE\_BASE**, **AvgDiskBytesPerRead** is divided by **AvgDiskBytesPerRead\_Base** to produce the average value. This value appears in System Monitor and is stored in the corresponding [**Win32\_PerfFormattedData\_PerfDisk\_LogicalDisk**](./retrieving-raw-and-formatted-performance-data.md) property. Base properties are only used in raw data classes.

In classes derived from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata), the **Counter** qualifier specifies the numerator property in the raw class and the **Base** qualifier specifies the base denominator property.

The following table lists the **CounterType** constant values.



| CounterType Constant                                                                                      | Description                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [PERF\_AVERAGE\_BASE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 1073939458<br/>        | Base value used to calculate the **PERF\_AVERAGE\_TIMER** and **PERF\_AVERAGE\_BULK** counter types.                                                                                             |
| [PERF\_COUNTER\_MULTI\_BASE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 1107494144<br/> | Base value used to calculate the **PERF\_COUNTER\_MULTI\_TIMER**, **PERF\_COUNTER\_MULTI\_TIMER\_INV**, **PERF\_100NSEC\_MULTI\_TIMER**, and **PERF\_100NSEC\_MULTI\_TIMER\_INV** counter types. |
| [PERF\_LARGE\_RAW\_BASE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 1073939712<br/>     | Base value found in the calculation of **PERF\_RAW\_FRACTION**, 64 bits.                                                                                                                         |
| [PERF\_RAW\_BASE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 1073939459<br/>            | Base value used to calculate the **PERF\_RAW\_FRACTION** counter type.                                                                                                                           |
| [PERF\_SAMPLE\_BASE](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 1073939457<br/>         | Base value used to calculate the **PERF\_SAMPLE\_COUNTER** and **PERF\_SAMPLE\_FRACTION** counter types.                                                                                         |



 

## Related topics

<dl> <dt>

[WMI Performance Counter Types](wmi-performance-counter-types.md)
</dt> <dt>

[Counter Types](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))
</dt> </dl>

 

