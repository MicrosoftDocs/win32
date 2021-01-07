---
description: Specify information about the performance object to which the WMI performance counter class is mapped.
ms.assetid: 7b8b7f00-95d8-4c1e-8638-157d0f4c7c32
ms.tgt_platform: multiple
title: Class Qualifiers for Performance Counter Classes
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Class Qualifiers for Performance Counter Classes

Class qualifiers specify information about the performance object to which the WMI [performance counter class](/windows/desktop/CIMWin32Prov/performance-counter-classes) is mapped. For more information, see [Monitoring Performance Data](monitoring-performance-data.md).

-   [Qualifiers for Raw and Formatted PerformanceClasses](#qualifiers-for-raw-and-formatted-performanceclasses)
-   [Qualifiers for Raw Performance Classes](#)
-   [Qualifiers for Formatted Performance Classes](#)
-   [Related topics](#related-topics)


Performance counter–specific qualifiers are automatically attached by the "WbemPerfClass" provider to [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) classes and properties in Root\\CIMv2.

This information applies to all instances of the class. Some qualifiers with **Boolean** values that are always **False** may not be present on specific classes.

## Qualifiers for Raw and Formatted PerformanceClasses

The following qualifiers apply to all classes that are derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) and [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata).

<dl> <dt>

<span id="Cooked"></span><span id="cooked"></span><span id="COOKED"></span>**Cooked**
</dt> <dd>

**boolean**

Indicates whether the class contains cooked data.

</dd> <dt>

<span id="DisplayName"></span><span id="displayname"></span><span id="DISPLAYNAME"></span>**DisplayName**
</dt> <dd>

**string**

Performance object name. For more information, see [Performance Counters](/windows/desktop/PerfCtrs/performance-counters-portal).

</dd> <dt>

<span id="DetailLevel"></span><span id="detaillevel"></span><span id="DETAILLEVEL"></span>**DetailLevel**
</dt> <dd>

**sint32**

Does not provide detail data. Always contains value of 100.

</dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>**Dynamic**
</dt> <dd>

**boolean**

Always set to **True** because instances are always dynamic.

</dd> <dt>

<span id="GenericPerfCtr"></span><span id="genericperfctr"></span><span id="GENERICPERFCTR"></span>**GenericPerfCtr**
</dt> <dd>

**boolean**

Indicates whether the class comes from a legacy performance library. Always set to **True**.

</dd> <dt>

<span id="HelpIndex"></span><span id="helpindex"></span><span id="HELPINDEX"></span>**HelpIndex**
</dt> <dd>

**sint32**

Indexes are no longer valid. This qualifier is always zero.

</dd> <dt>

<span id="HiPerf_"></span><span id="hiperf_"></span><span id="HIPERF_"></span>**HiPerf** 
</dt> <dd>

**boolean**

Indicates that the class is a high-performance class. Always set to **True**.

</dd> <dt>

<span id="Locale"></span><span id="locale"></span><span id="LOCALE"></span>**Locale**
</dt> <dd>

**sint32**

Locale identifier. Value is always 1033 (U.S. English).

</dd> <dt>

<span id="PerfIndex"></span><span id="perfindex"></span><span id="PERFINDEX"></span>**PerfIndex**
</dt> <dd>

**int32**

Indexes are no longer valid. This qualifier is always zero.

</dd> <dt>

<span id="Provider"></span><span id="provider"></span><span id="PROVIDER"></span>**Provider**
</dt> <dd>

**string**

Name of the instance provider. Value is "WbemPerfV2".

</dd> <dt>

<span id="RegistryKey"></span><span id="registrykey"></span><span id="REGISTRYKEY"></span>**RegistryKey**
</dt> <dd>

**string**

Name of the driver in the **HKEY\_LOCAL\_MACHINE\\CurrentControlSet\\Services** key, under which the performance key can be located. This name is also the name of the service that provides the performance counter.

</dd> <dt>

<span id="Singleton"></span><span id="singleton"></span><span id="SINGLETON"></span>**Singleton**
</dt> <dd>

**boolean**

If **True**, indicates that only a single instance of the class exists.

</dd> </dl>

## Qualifiers for Raw Performance Classes

The following qualifiers apply to all classes that are derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata).

<dl> <dt>

<span id="Costly"></span><span id="costly"></span><span id="COSTLY"></span>**Costly**
</dt> <dd>

**boolean**

Indicates whether obtaining instances of this class is a costly operation. Always set to **True** for classes with "\_Costly" appended to the end of the class name.

</dd> <dt>

<span id="DetailLevel"></span><span id="detaillevel"></span><span id="DETAILLEVEL"></span>**DetailLevel**
</dt> <dd>

**uint32**

Does not provide detail data. Always contains value of 100.

</dd> <dt>

<span id="PerfDefault"></span><span id="perfdefault"></span><span id="PERFDEFAULT"></span>**PerfDefault**
</dt> <dd>

**boolean**

Value is always **False**.

</dd> </dl>

## Qualifiers for Formatted Performance Classes

The following qualifiers apply to all classes that are derived from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata).

<dl> <dt>

<span id="AutoCook"></span><span id="autocook"></span><span id="AUTOCOOK"></span>**AutoCook**
</dt> <dd>

**int32**

Indicates that the values in class instances are automatically calculated from the corresponding raw data class. Value is always 1.

</dd> <dt>

<span id="AutoCook_RawClass"></span><span id="autocook_rawclass"></span><span id="AUTOCOOK_RAWCLASS"></span>**AutoCook\_RawClass**
</dt> <dd>

**string**

Name of the raw class to use for calculation for the formatted class. This qualifier is required.

</dd> </dl>

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

 

 
