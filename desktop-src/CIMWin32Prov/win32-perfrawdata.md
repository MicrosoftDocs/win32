---
description: The abstract base class for all concrete raw performance counter classes.
ms.assetid: 3c457996-54d9-4425-8a57-15176d027e3a
ms.tgt_platform: multiple
title: Win32_PerfRawData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PerfRawData
- Win32_PerfRawData.Caption
- Win32_PerfRawData.Description
- Win32_PerfRawData.Name
- Win32_PerfRawData.Frequency_Object
- Win32_PerfRawData.Frequency_PerfTime
- Win32_PerfRawData.Frequency_Sys100NS
- Win32_PerfRawData.Timestamp_Object
- Win32_PerfRawData.Timestamp_PerfTime
- Win32_PerfRawData.Timestamp_Sys100NS
api_type: 
- DllExport
api_location: 
- WmiPerfInst.dll
---

# Win32\_PerfRawData class

The abstract base class for all concrete raw performance counter classes.

To appear in System Monitor, performance counter classes must be added to the root\\cimv2 namespace and derived from **Win32\_PerfRawData**. Data in these classes are provided by the high-performance [Performance Counter Provider](../wmisdk/performance-counter-provider.md).

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
[abstract, AMENDMENT]
class Win32_PerfRawData : Win32_Perf
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

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64)
</dt> </dl>

Short textual description for the statistic or metric.

This property is inherited from [**CIM\_StatisticalInformation**](cim-statisticalinformation.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the statistic or metric.

This property is inherited from [**CIM\_StatisticalInformation**](cim-statisticalinformation.md).

</dd> <dt>

**Frequency\_Object**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Timestamp\_Object** property. When sub-classed, the provider defines this property.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**Win32\_Perf**](win32-perf.md).

</dd> <dt>

**Frequency\_PerfTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Frequency\_PerfTime** property. A value can be obtained by calling the Windows function [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**Win32\_Perf**](win32-perf.md).

</dd> <dt>

**Frequency\_Sys100NS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Timestamp\_Sys100NS** property (10000000).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**Win32\_Perf**](win32-perf.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (256)
</dt> </dl>

Label by which the statistic or metric is known. When subclassed, this property can be overridden to be a key property.

This property is inherited from [**CIM\_StatisticalInformation**](cim-statisticalinformation.md).

</dd> <dt>

**Timestamp\_Object**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object-defined timestamp. The provider defines his property.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**Win32\_Perf**](win32-perf.md).

</dd> <dt>

**Timestamp\_PerfTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

High Performance counter timestamp. A value can be obtained by calling the Windows function [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**Win32\_Perf**](win32-perf.md).

</dd> <dt>

**Timestamp\_Sys100NS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp value in 100 nanosecond units.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

This property is inherited from [**Win32\_Perf**](win32-perf.md).

</dd> </dl>

## Remarks

The **Win32\_PerfRawData** class is derived from [**Win32\_Perf**](win32-perf.md), which is derived from [**CIM\_StatisticalInformation**](cim-statisticalinformation.md).

All classes derived from [**Win32\_Perf**](win32-perf.md) are designed to be used with a [*refresher*](../wmisdk/gloss-r.md) object. For more information about how to create and use a refresher object in the C++ programming language, see [Accessing Performance Data in C++](../wmisdk/accessing-performance-data-in-c--.md). For more information about how to create and use a refresher object in a script programming language, see [Refreshing WMI Data in Scripts](../wmisdk/refreshing-wmi-data-in-scripts.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                             |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>WmiPerfInst.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Perf**](win32-perf.md)
</dt> <dt>

[Performance Counter Classes](performance-counter-classes.md)
</dt> <dt>

[Accessing WMI Preinstalled Performance Classes](../wmisdk/accessing-wmi-preinstalled-performance-classes.md)
</dt> <dt>

[WMI Tasks: Performance Monitoring](../wmisdk/wmi-tasks--performance-monitoring.md)
</dt> <dt>

[Accessing Performance Data in Script](../wmisdk/accessing-performance-data-in-script.md)
</dt> </dl>

 

 
