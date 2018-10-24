---
Description: The WMIPerfClass Provider and the WMIPerfInst Provider dynamically provide performance counter data for the WMI Performance Counter Classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8bf6d218-9a31-4efd-a809-222aca364138
ms.tgt_platform: multiple
title: Performance Libraries and WMI
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Performance Libraries and WMI

The [WMIPerfClass Provider](wmiperfclass-provider.md) and the [WMIPerfInst Provider](wmiperfinst-provider.md) dynamically provide performance counter data for the WMI [Performance Counter Classes](https://msdn.microsoft.com/library/aa392738).

## WMIPerfClass and WMIPerfInst Providers

[WMIPerfClass Provider](wmiperfclass-provider.md) creates WMI [Performance Counter Classes](https://msdn.microsoft.com/library/aa392738) at system initialization. The [WMIPerfInst Provider](wmiperfinst-provider.md) dynamically provides performance counter data for these classes. The WMIPerfClass Provider provider supplies classes for both version 1 and version 2 [Performance Counters](https://msdn.microsoft.com/library/windows/desktop/aa373083).

Version 1 counters are found in the registry under **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services**. Services that provide performance data have a **Performance** subkey. WMI performance classes created from version 1 counters do not have "Counters" as part of their name.

The **GUID**s identifying a version 2 performance counter provider are found in the registry under **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Perflib\\\_V2Providers**.

WMIPerfClass is registered as a normal WMI class provider. WMIPerfInst is a WMI instance provider that supplies data from Performance Data Helper (PDH) for both version 1 and version 2 counters. For more information, see [Using the PDH Functions to Consume Counter Data](https://msdn.microsoft.com/library/windows/desktop/aa373214).

## Related topics

<dl> <dt>

[About WMI](about-wmi.md)
</dt> <dt>

[Monitoring Performance Data](monitoring-performance-data.md)
</dt> </dl>

 

 



