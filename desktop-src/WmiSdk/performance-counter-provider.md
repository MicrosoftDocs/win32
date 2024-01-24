---
description: The Performance Counter provider is a high-performance provider that provides raw performance counter data to the WMI Performance Counter Classes derived from Win32\_PerfRawData. The \_\_Win32Provider instance name is &\#0034;NT5\_GenericPerfProvider\_V1&\#0034;.
ms.assetid: 2c7206e7-f5f8-4d40-b993-56122e48069b
ms.tgt_platform: multiple
title: Performance Counter Provider
ms.topic: article
ms.date: 05/31/2018
---

# Performance Counter Provider

\[The Performance Counter Provider is no longer available for use. Instead, use the [WMIPerfInst](wmiperfinst-provider.md) provider.\]

The Performance Counter provider is a high-performance provider that provides raw performance counter data to the WMI [Performance Counter Classes](/windows/desktop/CIMWin32Prov/performance-counter-classes) derived from [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata). The [**\_\_Win32Provider**](--win32provider.md) instance name is "NT5\_GenericPerfProvider\_V1".

The [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) classes are located in the WMI "Root\\CIMv2" namespace. Each WMI performance class corresponds to a performance object in a performance library. The properties of these classes represent the counters for the object. The WMI class name for a raw counter object is of the form **Win32\_PerfRawData\_\_*service\_name*\_*object\_name***. For example, the WMI class name that contains the logical disk counters is [**Win32\_PerfRawData\_PerfDisk\_LogicalDisk**](./retrieving-raw-and-formatted-performance-data.md).

You can use the corresponding [**Win32\_PerfFormattedData**](/windows/desktop/CIMWin32Prov/win32-perfformatteddata) class to get the pre-calculated performance data shown in [*System Monitor*](gloss-s.md). For example, use the [**Win32\_PerfFormattedData\_PerfDisk\_LogicalDisk**](./retrieving-raw-and-formatted-performance-data.md) class to get pre-calculated disk data.

For more information about how to write a client that can access raw performance data, see [Accessing Performance Data in C++](accessing-performance-data-in-c--.md).

As a high-performance provider, the Performance Counter provider implements the standard [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) interface, as well as the [**IWbemRefresher::Refresh**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemrefresher-refresh) method and the following [**IWbemHiPerfProvider**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemhiperfprovider) methods:

-   [**CreateRefreshableEnum**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemhiperfprovider-createrefreshableenum)
-   [**CreateRefreshableObject**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemhiperfprovider-createrefreshableobject)
-   [**CreateRefresher**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemhiperfprovider-createrefresher)
-   [**GetObjects**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemhiperfprovider-getobjects)
-   [**QueryInstances**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemhiperfprovider-queryinstances)
-   [**StopRefreshing**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemhiperfprovider-stoprefreshing)

## Related topics

<dl> <dt>

[WMI Providers](wmi-providers.md)
</dt> </dl>

 

 
