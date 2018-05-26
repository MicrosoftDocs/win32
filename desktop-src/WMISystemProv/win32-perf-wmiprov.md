---
title: Win32\_Perf class
description: The base class for the performance counter classes Win32\_PerfRawData and Win32\_PerfFormattedData.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7045cba-ec4f-471b-b02b-0dd9f9f1ef3b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_Perf class
- Win32_Perf class, described
topic_type:
- apiref
api_name:
- Win32_Perf
- Win32_Perf.Caption
- Win32_Perf.Description
- Win32_Perf.Name
- Win32_Perf.Frequency_Object
- Win32_Perf.Frequency_PerfTime
- Win32_Perf.Frequency_Sys100NS
- Win32_Perf.Timestamp_Object
- Win32_Perf.Timestamp_PerfTime
- Win32_Perf.Timestamp_Sys100NS
api_location:
- WmiPerfInst.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_Perf class

The **Win32\_Perf** abstract class is the base class for the performance counter classes [**Win32\_PerfRawData**](win32-perfrawdata-wmiprov.md) and [**Win32\_PerfFormattedData**](win32-perfformatteddata-wmiprov.md). It defines the required timestamp and frequency properties used in the [**CounterType**](https://msdn.microsoft.com/library/aa389383) algorithms for the performance counter classes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_Perf : CIM_StatisticalInformation
{
  string Caption;
  string Description;
  string Name;
  uint64 Frequency_Object;
  uint64 Frequency_PerfTime;
  uint64 Frequency_Sys100NS;
  uint64 Timestamp_Object;
  uint64 Timestamp_PerfTime;
  uint64 Timestamp_Sys100NS;
};
```

## Members

The **Win32\_Perf** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_Perf** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description for the statistic or metric.

This property is inherited from [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the statistic or metric.

This property is inherited from [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483).

</dd> <dt>

**Frequency\_Object**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Timestamp\_Object** property. When sub-classed, the provider defines this property.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Frequency\_PerfTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Frequency\_PerfTime** property. A value can be obtained by calling the Windows function [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Frequency\_Sys100NS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Timestamp\_Sys100NS** property (10000000).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Label by which the statistic or metric is known. When subclassed, this property can be overridden to be a key property.

This property is inherited from [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483).

</dd> <dt>

**Timestamp\_Object**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object-defined timestamp. The provider defines his property.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Timestamp\_PerfTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

High Performance counter timestamp. A value can be obtained by calling the Windows function [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Timestamp\_Sys100NS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp value in 100 nanosecond units.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> </dl>

## Remarks

The **Win32\_Perf** class derives from [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483).

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                             |
| Namespace<br/>                | Root\\WMI<br/>                                                                       |
| MOF<br/>                      | <dl> <dt>Wmi.mof</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>WmiPerfInst.dll</dt> </dl> |



## See also

<dl> <dt>

[Performance Counter Classes](https://msdn.microsoft.com/library/aa392738)
</dt> <dt>

[Accessing WMI Preinstalled Performance Classes](https://msdn.microsoft.com/library/aa384740)
</dt> <dt>

[WMI Tasks: Performance Monitoring](https://msdn.microsoft.com/library/aa394597)
</dt> <dt>

[Accessing Performance Data in Script](https://msdn.microsoft.com/library/aa384728)
</dt> <dt>

[**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483)
</dt> </dl>

 

 





