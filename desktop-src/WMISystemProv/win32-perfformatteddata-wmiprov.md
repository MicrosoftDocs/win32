---
title: Win32\_PerfFormattedData class
description: An abstract base class for the preinstalled, calculated data classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec44f6c6-3ce6-43e3-87d2-f62febce46f4
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_PerfFormattedData class
- Win32_PerfFormattedData class, described
topic_type:
- apiref
api_name:
- Win32_PerfFormattedData
- Win32_PerfFormattedData.Caption
- Win32_PerfFormattedData.Description
- Win32_PerfFormattedData.Name
- Win32_PerfFormattedData.Frequency_Object
- Win32_PerfFormattedData.Frequency_PerfTime
- Win32_PerfFormattedData.Frequency_Sys100NS
- Win32_PerfFormattedData.Timestamp_Object
- Win32_PerfFormattedData.Timestamp_PerfTime
- Win32_PerfFormattedData.Timestamp_Sys100NS
api_location:
- WmiPerfInst.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_PerfFormattedData class

The **Win32\_PerfFormattedData** [performance counter class](https://msdn.microsoft.com/library/aa392397) is an abstract base class for the preinstalled, calculated data classes. An example of such a class is [**Win32\_PerfFormattedData\_PerfDisk\_LogicalDisk**](https://msdn.microsoft.com/library/dn750765). These classes contain calculated values provided by the high-performance [Formatted Performance Data Provider](https://msdn.microsoft.com/library/aa390431).

The following syntax is simplified from MOF code and shows all of the inherited properties.

## Syntax

``` syntax
class Win32_PerfFormattedData : Win32_Perf
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

The **Win32\_PerfFormattedData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PerfFormattedData** class has these properties.

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

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

</dd> <dt>

**Frequency\_PerfTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Frequency\_PerfTime** property. A value can be obtained by calling the Windows function [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

</dd> <dt>

**Frequency\_Sys100NS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Timestamp\_Sys100NS** property (10000000).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

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

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

</dd> <dt>

**Timestamp\_PerfTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

High Performance counter timestamp. A value can be obtained by calling the Windows function [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

</dd> <dt>

**Timestamp\_Sys100NS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp value in 100 nanosecond units.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

</dd> </dl>

## Remarks

The **Win32\_PerfFormattedData** class is derived from [**Win32\_Perf**](win32-perf-wmiprov.md), which is derived from [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483). The class is found in both the "Root\\CIMv2" and "Root\\WMI" namespaces.

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

[**Win32\_Perf**](win32-perf-wmiprov.md)
</dt> <dt>

[Performance Counter Classes](https://msdn.microsoft.com/library/aa392738)
</dt> <dt>

[Accessing WMI Preinstalled Performance Classes](https://msdn.microsoft.com/library/aa384740)
</dt> <dt>

[WMI Tasks: Performance Monitoring](https://msdn.microsoft.com/library/aa394597)
</dt> <dt>

[Accessing Performance Data in Script](https://msdn.microsoft.com/library/aa384728)
</dt> </dl>

 

 





