---
description: When writing a high-performance provider that derives classes from Win32\_PerfFormattedData, you must follow specific conventions so that WMI can calculate the property values.
ms.assetid: 57912f6f-45ca-491c-8a6c-77e2a6937ccc
ms.tgt_platform: multiple
title: Supporting the Win32_PerfFormattedData Class
ms.topic: article
ms.date: 05/31/2018
---

# Supporting the Win32\_PerfFormattedData Class

When writing a high-performance provider that derives classes from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata), you must follow specific conventions so that WMI can calculate the property values.

> [!Note]  
> Writing a WMI high-performance provider to create performance counters is not recommended on any version of the Windows operating system. For more information, see [Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md)and [Performance Libraries and WMI](performance-libraries-and-wmi.md).

 

The following procedure describes how to support the Win32\_PerfFormattedData class.

**To support the Win32\_PerfFormattedData class**

1.  Create your class in the same namespace as the corresponding raw class. The class must be derived from [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata) and have the **HiPerf** qualifier set to **TRUE**. For more information about creating your own class for WMI, see [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md).
2.  Specify "HiPerfCooker\_v1" in the [**Provider**](class-qualifiers-for-performance-counter-classes.md) qualifier.
3.  Specify the following class-level qualifiers in addition to the qualifiers used for the raw classes:

    -   [**AutoCook**](class-qualifiers-for-performance-counter-classes.md)
    -   [**Autocook\_RawClass**](class-qualifiers-for-performance-counter-classes.md)
    -   [**Cooked**](class-qualifiers-for-performance-counter-classes.md)
    -   [**Costly**](class-qualifiers-for-performance-counter-classes.md)
    -   [**Dynamic**](dynamic-qualifier.md)
    -   [**HiPerf**](class-qualifiers-for-performance-counter-classes.md)
    -   [**Locale**](class-qualifiers-for-performance-counter-classes.md)
    -   [**PerfDefault**](class-qualifiers-for-performance-counter-classes.md)
    -   [**Provider**](class-qualifiers-for-performance-counter-classes.md)
    -   [**Singleton**](standard-wmi-qualifiers.md)

    > [!Note]  
    > Do not set any value for **GenericPerfCtr**, **PerfIndex**, or **HelpIndex** because these will be set by the ADAP process. For more information, see [**Class Qualifiers for Performance Counter Classes**](class-qualifiers-for-performance-counter-classes.md).

     

4.  Include a key property called **Name** in your class (this property is not required for singleton classes).

    The value of the **Name** property must be the same as the corresponding raw class. You must not use any key property other than **Name** on your class.

5.  Create properties data typed as either **DWORD** (**uint32**) or **QWORD** (**uint64**).

    The properties must correspond either to a property in the raw class or a property in the class you are creating.

6.  Specify the following property level qualifiers for all properties in your class in addition to the **PerfIndex** and **PerfDetail** qualifiers used for the raw class properties:

    -   [**Base**](property-qualifiers-for-performance-counter-classes.md)
    -   [**CookingType**](property-qualifiers-for-performance-counter-classes.md)
    -   [**Counter**](property-qualifiers-for-performance-counter-classes.md)
    -   [**PerfTimeStamp**](property-qualifiers-for-performance-counter-classes.md)
    -   [**PerfTimeFreq**](property-qualifiers-for-performance-counter-classes.md)
    -   [**SampleWindow**](property-qualifiers-for-performance-counter-classes.md)

    For more information, see [**Property Qualifiers for Performance Counter Classes**](property-qualifiers-for-performance-counter-classes.md). In addition, the Winperf.h header file contains values that you can specify for **PerfDetail** and **CounterType**.

7.  Make sure your provider meets the [performance requirements](#performance-requirements).

## Performance Requirements

When you write a high-performance provider, its performance must meet the following requirements:

-   Opening the high-performance DLL file can take no more than 100 milliseconds. Overall, opening each the high-performance provider and performance library cannot exceed 5 seconds.
-   Data refresh can take no more than 10 milliseconds per collect. On an overall refresh and collect operation, all the high-performance providers together cannot take more than 800 milliseconds.
-   The overall CPU load for all high-performance providers cannot exceed 6-7% CPU overhead interactively or 5% for logging.

## Related topics

<dl> <dt>

[Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md)
</dt> </dl>

 

 
