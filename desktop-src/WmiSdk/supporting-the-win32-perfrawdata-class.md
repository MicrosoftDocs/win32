---
description: When writing a high-performance provider that derives classes from Win32\_PerfRawData, you must follow specific conventions so that WMI can supply data to the property values.
ms.assetid: 04abb2f9-800f-497a-ac8f-8ef210746273
ms.tgt_platform: multiple
title: Supporting the Win32_PerfRawData Class
ms.topic: article
ms.date: 05/31/2018
---

# Supporting the Win32\_PerfRawData Class

When writing a high-performance provider that derives classes from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata), you must follow specific conventions so that WMI can supply data to the property values.

> [!Note]  
> Writing a WMI high-performance provider to create performance counters is not recommended on any version of the Windows operating system. For more information, see [Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md)and [Performance Libraries and WMI](performance-libraries-and-wmi.md).

 

The following procedure describes how to support the [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) class with your high-performance provider.

**To support the Win32\_PerfRawData class**

1.  Create your class in the Root\\CIMv2 namespace.

    The class must be derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) and have the **Hiperf** qualifier set to **TRUE**. You can also add WDM (driver) performance data classes to the root\\wmi namespace. For more information about creating your own class for WMI, see [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md).

2.  Specify the provider as "NT5\_GenericPerfProvider\_V1" in the **Provider** qualifier.
3.  Specify the following class-level qualifiers:

    -   **HiPerf**
    -   **Locale**
    -   **PerfDetail**
    -   **Provider**

    For more information, see [**Class Qualifiers for Performance Counter Classes**](class-qualifiers-for-performance-counter-classes.md). Do not define the **GenericPerfCtr** qualifier because that is reserved for the ADAP process that transfers performance library data into WMI classes.

4.  Populate the appropriate timestamp and frequency properties used to compute counter-type formulas.

    These properties are inherited from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) and, if you are writing a high-performance provider, you must fill these out for the class to be displayed in System Monitor.

5.  Include a key property called **Name** in your class (this property is not required for singleton classes).

    You must not use any key property other than **Name** on your class.

6.  Create properties data-typed as either **DWORD** (**uint32**) or **QWORD** (**uint64**). These properties become performance counters when transferred to the performance libraries.
7.  Specify the following property level qualifiers for all properties in your class:

    -   **DisplayName**
    -   **CounterType**
    -   **DefaultScale**
    -   **Description**
    -   **PerfDefault**
    -   **PerfDetail**

    For more information, see [**Property Qualifiers for Performance Counter Classes**](property-qualifiers-for-performance-counter-classes.md). In addition, the Winperf.h header file contains values that you can specify for **PerfDetail** and **CounterType**.

    WMI uses the **DisplayName**, **Locale**, and **Description** qualifiers for localization. You must add amended qualifiers to the MS\_409 (English) namespace so that System Monitor can properly display your class data. This means that you amend the property definition by adding a **Description** qualifier with explanatory text and fill in the **DisplayName** value. You must also add amended qualifiers to any other locale namespace that your class supports. If a user requests data from a locale for which you do not provide amended qualifiers, WMI defaults to the definitions specified in the MS\_409 namespace.

8.  Create a base property for any property that has a counter type expecting a base value.

    This property immediately follows the property and is named *propertyname***\_Base**. For example, the average property **AvgDiskBytesPerRead** in the [**Win32\_PerfRawData\_PerfDisk\_LogicalDisk**](./retrieving-raw-and-formatted-performance-data.md) class requires a base property named **AvgDiskBytesPerRead\_Base** to count the number of samples. To determine if the counter type you want to use requires a base property, locate the counter type by name or decimal value in [WMI Performance Counter Types](wmi-performance-counter-types.md).

9.  Make sure your provider meets the [performance requirements](supporting-the-win32-perfformatteddata-class.md).

## Related topics

<dl> <dt>

[Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md)
</dt> </dl>

 

 
