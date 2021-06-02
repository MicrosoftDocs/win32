---
description: Writing a WMI high-performance provider to create performance counters is not recommended.
ms.assetid: 6a22d6f7-d9e2-45fa-876d-921a4bc4f574
ms.tgt_platform: multiple
title: Making an Instance Provider into a High-Performance Provider
ms.topic: article
ms.date: 05/31/2018
---

# Making an Instance Provider into a High-Performance Provider

Writing a WMI high-performance provider to create performance counters is not recommended. Starting with Windows Vista, the WMI [Performance Counter Classes](/windows/desktop/CIMWin32Prov/performance-counter-classes) are no longer migrated into the Windows performance libraries by the AutoDiscovery/AutoPurge (ADAP) reverse adapter. To create a performance counter provider, use [Performance Counters Version 2.0](/windows/desktop/PerfCtrs/performance-counters-portal). After performance library objects are created, the [WMIPerfClass Provider](wmiperfclass-provider.md) parses the objects and creates or refreshes a WMI class derived from [**Win32\_Perf**](/windows/desktop/CIMWin32Prov/win32-perf) for each performance object. The [WMIPerfInst Provider](wmiperfinst-provider.md) then dynamically provides raw and formatted performance counter data to the WMI performance classes.

The following high-level procedure provides the steps required to create a high-performance provider.

**To create a high-performance provider**

1.  Register your provider with WMI. For more information, see [Registering a High-Performance Provider](registering-a-high-performance-provider.md).
2.  Implement your provider. For more information, see [Writing an Instance Provider](writing-an-instance-provider.md).
3.  Implement the high-performance interface. For more information, see [Implementing the High-Performance Interface](implementing-the-high-performance-interface.md).
4.  Derive and write your Managed Object Format (MOF) schema to obtain raw performance data. For more information, see [Supporting the Win32\_PerfRawData Class](supporting-the-win32-perfrawdata-class.md).
5.  Derive and write your MOF schema to obtain precalculated data. By supporting this class, the provider is not required to perform the calculations. This data will be the same that appears in the System Monitor in Perfmon. For more information, see [Supporting the Win32\_PerfFormattedData Class](supporting-the-win32-perfformatteddata-class.md).

## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Performance Libraries and WMI](performance-libraries-and-wmi.md)
</dt> </dl>

 

 
