---
description: Starting with Windows Vista, the WmiPerfInst provider supplies raw and formatted performance counter data dynamically to WMI Performance Counter Classes derived from Win32\_Perf.
ms.assetid: 780f2564-73f8-46a7-99fe-9ea78b00dedb
ms.tgt_platform: multiple
title: WmiPerfInst Provider
ms.topic: article
ms.date: 05/31/2018
---

# WmiPerfInst Provider

Starting with Windows Vista, the WmiPerfInst provider supplies raw and formatted performance counter data dynamically to WMI [Performance Counter Classes](/windows/desktop/CIMWin32Prov/performance-counter-classes) derived from [**Win32\_Perf**](/windows/desktop/CIMWin32Prov/win32-perf). This provider replaces the [Formatted Performance Data Provider](formatted-performance-data-provider.md), also known as the "Cooked Counter Provider", and the [Performance Counter Provider](performance-counter-provider.md).

The WmiPerfInst provider supplies data to the WMI classes that are provided by the [WMIPerfClass](wmiperfclass-provider.md) provider. This provider is a bridge between Performance Data Helper (PDH) instances and the WMI performance classes supplied by the WmiPerfClass Provider. When WmiPerfInst receives a query for data, it loads the class and uses the class and property [qualifiers](qualifiers-specific-to-wmi-performance-classes.md) to locate the PDH instances. For more information, see [Using the PDH Functions to Consume Counter Data](/windows/desktop/PerfCtrs/using-the-pdh-functions-to-consume-counter-data).

It is not recommended that you develop new performance objects by creating a WMI high-performance provider and depend on the [*ADAP reverse adapter*](gloss-r.md) process to transfer the data to the performance libraries. The exception is when you are developing a Windows Driver Model driver and want to supply performance data. While the reverse adapter process continues to work for backward compatibility, the recommended method is to use [Performance Counters Version 6.0](/windows/desktop/PerfCtrs/performance-counters-portal).

The [**\_\_Win32Provider**](--win32provider.md) instance name of this provider is "WmiPerfInst".

## Related topics

<dl> <dt>

[WMI Providers](wmi-providers.md)
</dt> <dt>

[Performance Libraries and WMI](performance-libraries-and-wmi.md)
</dt> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> </dl>

 

 
