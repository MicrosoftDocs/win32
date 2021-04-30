---
description: Noncomputational counter types do not have an associated formula. The raw value is directly meaningful.
ms.assetid: 2a6bb3a3-0aec-437a-881a-c4e14fcff6da
ms.tgt_platform: multiple
title: Noncomputational Counter Types
ms.topic: article
ms.date: 05/31/2018
---

# Noncomputational Counter Types

Noncomputational counter types do not have an associated formula. The raw value is directly meaningful.

The **FilesToBeIndexed** property in the [**Win32\_PerfRawData\_ContentIndex\_IndexingService**](/windows/desktop/WmiSdk/retrieving-raw-and-formatted-performance-data) class is an example of the **PERF\_COUNTER\_RAWCOUNT** counter type. It contains a count of files that have not been indexed.

Counter types are designated by the constant defined in Winperf.h located in the Microsoft Windows Software Development Kit (SDK). The following table lists the noncomputational counter types that are provided.



| CounterType                                                                                                 | Description                                                                                                            |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [PERF\_COUNTER\_TEXT](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 2816<br/>                | This counter type shows a variable-length text string in Unicode. It does not display calculated values.               |
| [PERF\_COUNTER\_RAWCOUNT](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 65536<br/>           | Raw counter value that does not require calculations, and represents one sample which is the last observed value only. |
| [PERF\_COUNTER\_LARGE\_RAWCOUNT](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 65792<br/>    | Same as **PERF\_COUNTER\_RAWCOUNT**, but a 64-bit representation for larger values.                                    |
| [PERF\_COUNTER\_RAWCOUNT\_HEX](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))0<br/>                  | Most recently observed value in hexadecimal format. It does not display an average.                                    |
| [PERF\_COUNTER\_LARGE\_RAWCOUNT\_HEX](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10))Decimal 256<br/> | Same as **PERF\_COUNTER\_RAWCOUNT\_HEX**, but a 64-bit representation in hexadecimal for use with large values.        |



 

## Related topics

<dl> <dt>

[WMI Performance Counter Types](wmi-performance-counter-types.md)
</dt> </dl>

 

