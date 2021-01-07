---
description: The WMI high-performance Formatted Performance Data Provider calculates the statistical counter types on a specified number of raw counter data samples.
ms.assetid: a7e32ef2-fad1-449c-beee-07db4b93e3fe
ms.tgt_platform: multiple
title: Statistical Counter Types
ms.topic: article
ms.date: 05/31/2018
---

# Statistical Counter Types

The WMI high-performance [Formatted Performance Data Provider](formatted-performance-data-provider.md) calculates the statistical counter types on a specified number of raw counter data samples. The algorithms for the counter types do not require inherited timestamp or frequency properties (such as **TimeStamp\_PerfTime** or **Frequency\_PerfTime**) that other counter types require.

Instead, the statistical counter types support a **qualifier** that identifies how many samples to use. A sample is collected when the [**Refresh**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemrefresher-refresh) method is called for the performance object. For scripts use the [**SWbemRefresher.Refresh**](swbemrefresher-refresh.md) method. The calculated data contains the result of the calculation performed on the **SampleWindow** number of samples from the raw data property. The raw data for the calculation comes frm the property name specified in the **Counter** qualifier.

For more information, see [Obtaining Statistical Performance Data](obtaining-statistical-performance-data.md) and [Accessing WMI Preinstalled Performance Classes](accessing-wmi-preinstalled-performance-classes.md).



| CounterType Constant                    | Description                                                                                                                                                                                |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [COOKER\_AVERAGE](cooker-average.md)   | Sums repeated observations of one property in a [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) class and divides the sum by the number of observations.                              |
| [COOKER\_MAX](cooker-max.md)           | Largest value from a set of observations of a property in a [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) class.                                                                    |
| [COOKER\_MIN](cooker-min.md)           | Smallest value from a set of observations of a property in a [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) class.                                                                   |
| [COOKER\_RANGE](cooker-range.md)       | Difference between the [Min](cooker-min.md) and [Max](cooker-max.md) values for a set of raw observations of a property in a [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) class. |
| [COOKER\_VARIANCE](cooker-variance.md) | Measure of variability that can be used to characterize dispersion for a set of raw observations of a property in a [**Win32\_PerfRawData**](/windows/desktop/CIMWin32Prov/win32-perfrawdata) class.            |



 

## Related topics

<dl> <dt>

[WMI Performance Counter Types](wmi-performance-counter-types.md)
</dt> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> <dt>

[Refreshing WMI Data in Scripts](refreshing-wmi-data-in-scripts.md)
</dt> <dt>

[Accessing Performance Data in Script](accessing-performance-data-in-script.md)
</dt> <dt>

[Accessing Performance Data in C++](accessing-performance-data-in-c--.md)
</dt> </dl>

 

 
