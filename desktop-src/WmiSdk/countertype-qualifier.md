---
description: The CounterType qualifier contains the integer value for the property counter type for properties in Win32\_PerfRawData classes. The CookingType contains the constants for property formula types in Win32\_PerfFormattedData classes.
ms.assetid: aa79fcdb-503f-4928-b2b7-f07baeaf9fb5
ms.tgt_platform: multiple
title: CounterType Qualifier
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CounterType
api_type: 
- NA
api_location: 
---

# CounterType Qualifier

The **CounterType** qualifier contains the integer value for the property counter type for properties in [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) classes. The **CookingType** contains the constants for property formula types in [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata) classes.

For more information and a breakdown of counter types by function, see [Counter Types](/previous-versions/windows/it-pro/windows-server-2003/cc785636(v=ws.10)).



| CounterType | CookingType                              |
|-------------|------------------------------------------|
| 0           | PERF\_COUNTER\_RAWCOUNT\_HEX             |
| 256         | PERF\_COUNTER\_LARGE\_RAWCOUNT\_HEX      |
| 2816        | PERF\_COUNTER\_TEXT                      |
| 65536       | PERF\_COUNTER\_RAWCOUNT                  |
| 65792       | PERF\_COUNTER\_LARGE\_RAWCOUNT           |
| 73728       | PERF\_DOUBLE\_RAW                        |
| 4195328     | PERF\_COUNTER\_DELTA                     |
| 4195584     | PERF\_COUNTER\_LARGE\_DELTA              |
| 4260864     | PERF\_SAMPLE\_COUNTER                    |
| 4523008     | PERF\_COUNTER\_QUEUELEN\_TYPE            |
| 4523264     | PERF\_COUNTER\_LARGE\_QUEUELEN\_TYPE     |
| 5571840     | PERF\_COUNTER\_100NS\_QUEUELEN\_TYPE     |
| 6620416     | PERF\_COUNTER\_OBJ\_TIME\_QUEUELEN\_TYPE |
| 272696320   | PERF\_COUNTER\_COUNTER                   |
| 272696576   | PERF\_COUNTER\_BULK\_COUNT               |
| 537003008   | PERF\_RAW\_FRACTION                      |
| 541132032   | PERF\_COUNTER\_TIMER                     |
| 541525248   | PERF\_PRECISION\_SYSTEM\_TIMER           |
| 542180608   | PERF\_100NSEC\_TIMER                     |
| 542573824   | PERF\_PRECISION\_100NS\_TIMER            |
| 543229184   | PERF\_OBJ\_TIME\_TIMER                   |
| 543622400   | PERF\_PRECISION\_OBJECT\_TIMER           |
| 549585920   | PERF\_SAMPLE\_FRACTION                   |
| 557909248   | PERF\_COUNTER\_TIMER\_INV                |
| 558957824   | PERF\_100NSEC\_TIMER\_INV                |
| 574686464   | PERF\_COUNTER\_MULTI\_TIMER              |
| 575735040   | PERF\_100NSEC\_MULTI\_TIMER              |
| 591463680   | PERF\_COUNTER\_MULTI\_TIMER\_INV         |
| 592512256   | PERF\_100NSEC\_MULTI\_TIMER\_INV         |
| 805438464   | PERF\_AVERAGE\_TIMER                     |
| 807666944   | PERF\_ELAPSED\_TIME                      |
| 1073742336  | PERF\_COUNTER\_NODATA                    |
| 1073874176  | PERF\_AVERAGE\_BULK                      |
| 1073939457  | PERF\_SAMPLE\_BASE                       |
| 1073939458  | PERF\_AVERAGE\_BASE                      |
| 1073939459  | PERF\_RAW\_BASE                          |
| 1073939712  | PERF\_PRECISION\_TIMESTAMP               |
| 1073939715  | PERF\_LARGE\_RAW\_BASE                   |
| 1107494144  | PERF\_COUNTER\_MULTI\_BASE               |
| 2147483648  | PERF\_COUNTER\_HISTOGRAM\_TYPE           |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



## See also

<dl> <dt>

[Qualifiers Specific to WMI Performance Classes](qualifiers-specific-to-wmi-performance-classes.md)
</dt> </dl>

 

