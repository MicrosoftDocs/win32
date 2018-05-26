---
title: Win32\_PerfRawData class
description: The abstract base class for all concrete raw performance counter classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f08de9dc-6ca2-4166-b531-0e6fd0e3883b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_PerfRawData class
- Win32_PerfRawData class, described
topic_type:
- apiref
api_name:
- Win32_PerfRawData
- Win32_PerfRawData.Caption
- Win32_PerfRawData.Description
- Win32_PerfRawData.Name
- Win32_PerfRawData.Frequency_Object
- Win32_PerfRawData.Frequency_Sys100NS
- Win32_PerfRawData.Timestamp_Object
- Win32_PerfRawData.Timestamp_Sys100NS
- Win32_PerfRawData.Frequency_PerfTime
- Win32_PerfRawData.Timestamp_PerfTime
api_location:
- WmiPerfInst.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_PerfRawData class

The performance counter class **Win32\_PerfRawData** is the abstract base class for all concrete raw performance counter classes. To appear in System Monitor, performance counter classes must be added to the root\\cimv2 namespace and derived from **Win32\_PerfRawData**. Data in these classes are provided by the high-performance [Performance Counter Provider](https://msdn.microsoft.com/library/aa392739).

The following properties are inherited when a class is derived from **Win32\_PerfRawData**:

-   **Timestamp\_PerfTime**
-   **Timestamp\_Sys100NS**
-   **Timestamp\_Object**
-   **Frequency\_PerfTime**
-   **Frequency\_Sys100NS**
-   **Frequency\_Object**

In each case, the properties must be filled out by the provider or the class cannot be displayed in System Monitor. These properties are used to compute counter type formulas by consumers of performance data.

The following syntax is simplified from MOF code and shows all inherited properties.

## Syntax

``` syntax
class Win32_PerfRawData : Win32_Perf
{
  string Caption;
  string Description;
  string Name;
  uint64 Frequency_Object;
  uint64 Frequency_Sys100NS;
  uint64 Timestamp_Object;
  uint64 Timestamp_Sys100NS;
  uint64 Frequency_PerfTime;
  uint64 Timestamp_PerfTime;
};
```

## Members

The **Win32\_PerfRawData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PerfRawData** class has these properties.

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

Frequency, in ticks per second, of the **Timestamp\_Perftime** property. A value could be obtained by calling the Windows function [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp). This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md)

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

High-performance counter timestamp. A value could be obtained by calling the Windows function [**QueryPerformanceCounter**](_win32_queryperformancecounter_cpp). This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md)

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

This property is inherited from [**Win32\_Perf**](win32-perf-wmiprov.md).

</dd> </dl>

## Remarks

The **Win32\_PerfRawData** class is derived from [**Win32\_Perf**](win32-perf-wmiprov.md), which is derived from [**CIM\_StatisticalInformation**](https://msdn.microsoft.com/library/aa388483).

All classes derived from [**Win32\_Perf**](win32-perf-wmiprov.md) are designed to be used with a [*refresher*](https://msdn.microsoft.com/library/aa390834#wmi-gloss-refresher) object. For more information about how to create and use a refresher object in the C++ programming language, see [Accessing Performance Data in C++](https://msdn.microsoft.com/library/aa384724). For more information about how to create and use a refresher object in a script programming language, see [Refreshing WMI Data in Scripts](https://msdn.microsoft.com/library/aa393026).

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

 

 





