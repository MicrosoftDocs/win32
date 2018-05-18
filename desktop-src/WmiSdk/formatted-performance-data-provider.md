---
Description: 'Supplies calculated (&\#0034;cooked&\#0034;) performance counter data. Supplies dynamic data to the WMI classes derived from Win32\_PerfFormattedData. Also known as the Cooked Counter Provider.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '59823f7c-3046-4608-99df-1f43e2934e7e'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Formatted Performance Data Provider
---

# Formatted Performance Data Provider

\[The Formatted Performance Data Provider, also known as the "Cooked Counter Provider," is no longer available for use. Instead, use the [WMIPerfInst](wmiperfinst-provider.md) provider.\]

The high-performance Formatted Performance Data provider supplies calculated ("cooked") performance counter data, such as the percentage of time a disk spends writing data. This provider supplies dynamic data to the WMI classes derived from [**Win32\_PerfFormattedData**](https://msdn.microsoft.com/library/aa394253). The difference between this provider and the [Performance Counter provider](performance-counter-provider.md) is that the Performance Counter provider supplies raw data and the Cooked Counter provider supplies performance data that appears exactly as in [*System Monitor*](gloss-s.md#wmi-gloss-system-monitor). The [**\_\_Win32Provider**](--win32provider.md) instance name is "HiPerfCooker\_v1".

The WMI formatted class name for a counter object is of the form "Win32\_PerfFormattedData\_*service\_name*\_*object\_name*". For example, the WMI class name that contains the logical disk counters is **Win32\_PerfFormattedData\_PerfDisk\_LogicalDisk**. These classes are located in the "Root\\CIMv2" namespace.

Because performance data classes are added and modified dynamically on a given system, it is not possible to formally document the properties of all known performance objects. To determine what classes are available to you, and to identify what members those classes have, see [Retrieving Documentation for Raw and Formatted Performance Data Objects](retrieving-raw-and-formatted-performance-data.md).

The [**Win32\_PerfFormattedData**](https://msdn.microsoft.com/library/aa394253) classes use the **CookingType** qualifier in [WMI Performance Counter Types](wmi-performance-counter-types.md) to specify the formula for calculating performance data. This qualifier is the same as the **CounterType** qualifier in the [**Win32\_PerfRawData**](https://msdn.microsoft.com/library/aa394299) classes.

As a high-performance provider, the Cooked Counter provider implements the standard [**IWbemProviderInit**](iwbemproviderinit.md) interface, as well as the [**IWbemRefresher::Refresh**](iwbemrefresher-refresh.md) method and the following [**IWbemHiPerfProvider**](iwbemhiperfprovider.md) methods:

-   [**CreateRefreshableEnum**](iwbemhiperfprovider-createrefreshableenum.md)
-   [**CreateRefreshableObject**](iwbemhiperfprovider-createrefreshableobject.md)
-   [**CreateRefresher**](iwbemhiperfprovider-createrefresher.md)
-   [**GetObjects**](iwbemhiperfprovider-getobjects.md)
-   [**QueryInstances**](iwbemhiperfprovider-queryinstances.md)
-   [**StopRefreshing**](iwbemhiperfprovider-stoprefreshing.md)

## Related topics

<dl> <dt>

[WMI Providers](wmi-providers.md)
</dt> </dl>

 

 



