---
Description: Performance Counter classes allow script and program access to system performance data calculated by existing high-performance providers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71746363-6fec-4344-8c5e-5cc057ebdf76
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Performance Counter Classes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Performance Counter Classes

Performance Counter classes allow script and program access to system performance data calculated by existing high-performance providers. These classes consist of raw performance counter classes and formatted performance counter classes.

Different providers supply performance library data through WMI. The [WMIPerfClass](https://msdn.microsoft.com/library/aa394546) and [WMIPerfInst](https://msdn.microsoft.com/library/aa394547) providers supply classes for both version 1 and version 2 [Performance Counters](https://msdn.microsoft.com/library/windows/desktop/aa373083). These providers maintain compatibility with the classes available in earlier operating systems.

The classes in this section are the abstract base classes used to create performance counter classes. This is not a complete list of classes that you may find on your operating system. For more information, see [Performance Libraries and WMI](https://msdn.microsoft.com/library/aa392740).

## In this section

<dl> <dt>

[**Win32\_Perf**](win32-perf.md)
</dt> <dd>

The base class for the performance counter classes [**Win32\_PerfRawData**](win32-perfrawdata.md) and [**Win32\_PerfFormattedData**](win32-perfformatteddata.md).

</dd> <dt>

[**Win32\_PerfFormattedData**](win32-perfformatteddata.md)
</dt> <dd>

an abstract base class for the pre-installed, calculated data classes.

</dd> <dt>

[**Win32\_PerfRawData**](win32-perfrawdata.md)
</dt> <dd>

The abstract base class for all concrete raw performance counter classes.

</dd> </dl>

## Related topics

<dl> <dt>

[Win32 Classes](win32-provider.md)
</dt> </dl>

 

 



