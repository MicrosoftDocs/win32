---
description: Property qualifiers specify information about the performance counter to which the property maps.
ms.assetid: f1761f71-af4e-4b89-aba7-b7f294c30ffc
ms.tgt_platform: multiple
title: Property Qualifiers for Performance Counter Classes
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Property Qualifiers for Performance Counter Classes

Property qualifiers specify information about the performance counter to which the property maps.

-   [Property Qualifiers for Raw and Formatted Performance Classes](#property-qualifiers-for-raw-and-formatted-performance-classes)
-   [Property Qualifiers for Raw Performance Classes](#property-qualifiers-for-raw-and-formatted-performance-classes)
-   [Property Qualifiers for Formatted Performance Classes](#property-qualifiers-for-raw-and-formatted-performance-classes)
-   [How to Interpret Property Qualifiers](#how-to-interpret-property-qualifiers)
-   [Related topics](#related-topics)

The performance counter is part of a performance object represented by a WMI [performance counter class](/windows/desktop/CIMWin32Prov/performance-counter-classes) Performance counter–specific qualifiers are automatically attached by the WbemPerfClass provider to [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) classes and properties in Root\\CIMv2.

This information applies to all instances of the performance class. Some qualifiers with **Boolean** values that are always false may not be present on specific classes.

## Property Qualifiers for Raw and Formatted Performance Classes

The following list lists qualifiers that apply to properties in classes that are derived either from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) or [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata).

<dl> <dt>

<span id="CounterType"></span><span id="countertype"></span><span id="COUNTERTYPE"></span>[**CounterType**](countertype-qualifier.md)
</dt> <dd>

**sint32**

Integer value in the counter type enumeration, as defined in Winperf.h or Perflib.h. The [**CounterType**](countertype-qualifier.md)qualifier indicates the formula or algorithm used to calculate the value shown in System Monitor for the counter which the property represents.

</dd> <dt>

<span id="DisplayName"></span><span id="displayname"></span><span id="DISPLAYNAME"></span>**DisplayName**
</dt> <dd>

**string**

The performance Counter name, as specified by Performance Data Helper (PDH).

</dd> <dt>

<span id="HelpIndex"></span><span id="helpindex"></span><span id="HELPINDEX"></span>**HelpIndex**
</dt> <dd>

**sint32**

Not used. Always contains 0.

</dd> <dt>

<span id="PerfIndex"></span><span id="perfindex"></span><span id="PERFINDEX"></span>**PerfIndex**
</dt> <dd>

**sint32**

Not used. Always contains 0.

</dd> </dl>

## Property Qualifiers for Raw Performance Classes

The following list lists qualifiers that apply to all properties of classes that are derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata).

<dl> <dt>

<span id="PerfDefault"></span><span id="perfdefault"></span><span id="PERFDEFAULT"></span>**PerfDefault**
</dt> <dd>

**boolean**

Indicates whether this property is the default counter to use in list boxes. This qualifier defaults to **False** for Performance Counters Version 6.0 because they do not supply data for it. For more information, see [Performance Counters](/windows/desktop/PerfCtrs/performance-counters-portal).

</dd> <dt>

<span id="DefaultScale"></span><span id="defaultscale"></span><span id="DEFAULTSCALE"></span>**DefaultScale**
</dt> <dd>

**sint32**

Power of 10 to use for display of the counter. For zero, the estimated maximum is 10^0, or 1.

</dd> <dt>

<span id="PerfDetail"></span><span id="perfdetail"></span><span id="PERFDETAIL"></span>[**PerfDetail**](perfdetail-qualifier.md)
</dt> <dd>

**sint32**

Audience level of knowledge. Not used. The value is always 100.

</dd> </dl>

## Property Qualifiers for Formatted Performance Classes

The following list lists qualifiers that apply to all properties of classes that are derived from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata).

<dl> <dt>

<span id="CookingType"></span><span id="cookingtype"></span><span id="COOKINGTYPE"></span>**CookingType**
</dt> <dd>

**string**

Formula type used to produce the result. Each counter type uses the other property qualifiers to calculate the result shown as the value of the current property. The **Counter**, **PerfTimeStamp**, and **PerfTimeFreq** qualifiers map to properties in a raw class which supply the data.

For more information, see [CounterType Qualifier](countertype-qualifier.md).

</dd> <dt>

<span id="Counter"></span><span id="counter"></span><span id="COUNTER"></span>**Counter**
</dt> <dd>

**string**

Name of a required property in the corresponding raw class to use as the counter value in the cooking formula. The value must be the property name of the data source property in the corresponding raw class.

</dd> <dt>

<span id="PerfTimeStamp"></span><span id="perftimestamp"></span><span id="PERFTIMESTAMP"></span>**PerfTimeStamp**
</dt> <dd>

**string**

Name of a property in a raw class to use as a frequency in the cooking formula. The appropriate default value at the class level will be used if this qualifier is not present for the property. The frequency represents the ticks per second of the time stamp.

</dd> <dt>

<span id="PerfTimeFreq"></span><span id="perftimefreq"></span><span id="PERFTIMEFREQ"></span>**PerfTimeFreq**
</dt> <dd>

**string**

Name of a property in a raw class to use as a timestamp in the cooking formula. The appropriate default value at the class level is used if this qualifier is not present for the property. An automatically generated time stamp may introduce error in a calculation because the timestamp is an approximation and does not account for overhead incurred by marshaling and actual data collection.

</dd> </dl>

## How to Interpret Property Qualifiers

Properties in the [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata) classes contain the calculated data supplied by the [Formatted Performance Data Provider](formatted-performance-data-provider.md). The property value is the final calculated result. The qualifiers supply a recipe.

The **Counter** and **Base** qualifiers point to the sources of data and **CookingType** specifies the formula used to produce the result. The timestamp and sample frequency also come from the corresponding raw class and are named in **PerfTimeStamp** and **PerfTimeFreq**.

For example, one of the formatted classes supplied by WMI, [**Win32\_PerfFormattedData\_PerfDisk\_LogicalDisk**](./retrieving-raw-and-formatted-performance-data.md), contains a property named **AvgDiskBytesPerRead**. The name of the property in the formatted class must be the same as the property in the raw class. The **AvgDiskBytesPerRead** property has the following qualifiers.

The following list lists the available property qualifiers for properties of all classes derived from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata).



| Qualifier         | Value                     |
|-------------------|---------------------------|
| **CookingType**   | PERF\_AVERAGE\_BULK       |
| **Counter**       | AvgDiskBytesPerRead       |
| **PerfTimeStamp** | Timestamp\_PerfTime       |
| **PerfTimeFreq**  | Frequency\_PerfTime       |
| **PerfIndex**     | 408                       |
| **HelpIndex**     | 409                       |
| **Base**          | AvgDiskBytesPerRead\_Base |



 

The **AvgDiskBytesPerRead** property reports the average number of bytes transferred from the disk during read operations. The formula for PERF\_AVERAGE\_BULK is:

(Sample2 - Sample1) / (Base Sample2 - Base Sample1)

The read operation is sampled at the frequency specified by **PerfTimeFreq** with the **PerfTimeStamp** value indicating the most recent sample. The raw counter data in bytes is taken from the **AvgDiskBytesPerRead** property in the [**Win32\_PerfRawData\_PerfDisk\_LogicalDisk**](./retrieving-raw-and-formatted-performance-data.md) class. The base number of operations data is taken from the **AvgDiskBytesPerRead\_Base** property in that same class.

For more information, see [Obtaining Statistical Performance Data](obtaining-statistical-performance-data.md) and [Monitoring Performance Data](monitoring-performance-data.md).

## Related topics

<dl> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> <dt>

[Qualifiers Specific to WMI Performance Classes](qualifiers-specific-to-wmi-performance-classes.md)
</dt> <dt>

[Performance Counter Classes](/windows/desktop/CIMWin32Prov/performance-counter-classes)
</dt> <dt>

[Accessing WMI Preinstalled Performance Classes](accessing-wmi-preinstalled-performance-classes.md)
</dt> <dt>

[WMI Tasks: Performance Monitoring](wmi-tasks--performance-monitoring.md)
</dt> </dl>

 

 
