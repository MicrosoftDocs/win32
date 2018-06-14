---
Description: The base class for the performance counter classes Win32\_PerfRawData and Win32\_PerfFormattedData.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c754b619-a70f-4a56-8a43-2b36c8f8370b
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_Perf class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_Perf class

The base class for the performance counter classes [**Win32\_PerfRawData**](win32-perfrawdata.md) and [**Win32\_PerfFormattedData**](win32-perfformatteddata.md).

**Win32\_Perf** defines the required timestamp and frequency properties used in the [**CounterType**](https://msdn.microsoft.com/en-us/library/Aa389383(v=VS.85).aspx) algorithms for the performance counter classes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, AMENDMENT]
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

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) (64)
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

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://www.bing.com/search?q=Scripting+in+WMI).

</dd> <dt>

**Frequency\_PerfTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Frequency\_PerfTime** property. A value can be obtained by calling the Windows function [**QueryPerformanceCounter**](https://www.bing.com/search?q=**QueryPerformanceCounter**).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://www.bing.com/search?q=Scripting+in+WMI).

</dd> <dt>

**Frequency\_Sys100NS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Frequency in ticks per second of the **Timestamp\_Sys100NS** property (10000000).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://www.bing.com/search?q=Scripting+in+WMI).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) (256)
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

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://www.bing.com/search?q=Scripting+in+WMI).

</dd> <dt>

**Timestamp\_PerfTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

High Performance counter timestamp. A value can be obtained by calling the Windows function [**QueryPerformanceCounter**](https://www.bing.com/search?q=**QueryPerformanceCounter**).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://www.bing.com/search?q=Scripting+in+WMI).

</dd> <dt>

**Timestamp\_Sys100NS**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Timestamp value in 100 nanosecond units.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://www.bing.com/search?q=Scripting+in+WMI).

</dd> </dl>

## Remarks

The **Win32\_Perf** class derives from [**CIM\_StatisticalInformation**](cim-statisticalinformation.md).

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                             |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                     |
| DLL<br/>                      | <dl> <dt>WmiPerfInst.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_StatisticalInformation**](cim-statisticalinformation.md)
</dt> <dt>

[Performance Counter Classes](performance-counter-classes.md)
</dt> <dt>

[Accessing WMI Preinstalled Performance Classes](https://msdn.microsoft.com/en-us/library/Aa384740(v=VS.85).aspx)
</dt> <dt>

[WMI Tasks: Performance Monitoring](https://msdn.microsoft.com/en-us/library/Aa394597(v=VS.85).aspx)
</dt> <dt>

[Accessing Performance Data in Script](https://msdn.microsoft.com/en-us/library/Aa384728(v=VS.85).aspx)
</dt> </dl>

 

 




