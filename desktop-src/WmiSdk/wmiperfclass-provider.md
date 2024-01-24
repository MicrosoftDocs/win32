---
description: Starting with Windows Vista, this provider creates the WMI Performance Counter Classes.
ms.assetid: 5bb3d5e0-cdeb-4fea-a8ca-cf934e056206
ms.tgt_platform: multiple
title: WmiPerfClass Provider
ms.topic: article
ms.date: 05/31/2018
---

# WmiPerfClass Provider

Starting with Windows Vista, this provider creates the WMI [Performance Counter Classes](/windows/desktop/CIMWin32Prov/performance-counter-classes). Data is dynamically supplied to these WMI performance classes by the [WMIPerfInst](wmiperfinst-provider.md) provider. The AutoDiscovery/AutoPurge (ADAP) process no longer transfers performance counter objects into WMI performance classes in the WMI repository. For more information, see [Performance Libraries and WMI](performance-libraries-and-wmi.md).

For more information, see [Performance Libraries and WMI](performance-libraries-and-wmi.md).

While it is not recommended that you develop new performance objects by creating a WMI high-performance provider and depend on the [*ADAP reverse adapter*](gloss-r.md) process to transfer the data to the performance libraries, the exception is development of a Windows Driver Model driver that supplies performance data. While the reverse adapter process continues to work for backward compatibility, the recommended method is to use [Performance Counters Version 6.0](/windows/desktop/PerfCtrs/performance-counters-portal).

The [**\_\_Win32Provider**](--win32provider.md) instance name of this provider is "WmiPerfClass".

## Related topics

<dl> <dt>

[WMI Providers](wmi-providers.md)
</dt> <dt>

[Performance Libraries and WMI](performance-libraries-and-wmi.md)
</dt> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> </dl>

 

 
