---
Description: The Microsoft&\#160;Win32 provider retrieves and updates data relevant to Windows systems&\#8212;data such as the current settings of environment variables and the attributes of a logical disk.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 71c13736-0504-4d50-b8a4-5d68d4ba9a90
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32 Provider
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32 Provider

The Microsoft Win32 provider retrieves and updates data relevant to Windows systems—data such as the current settings of environment variables and the attributes of a logical disk. With the Win32 provider, management applications can use WMI to easily access this data. The Win32 provider retrieves its information by making Windows function calls and querying the system registry.

The Win32 provider defines the classes used to describe hardware or software available on Windows systems and the relationships between them.

As an instance and method provider, the Win32 provider implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/windows/desktop/92edf347-c694-4023-b83f-09531072c631) interface as well as the following [**IWbemServices**](https://msdn.microsoft.com/windows/desktop/58e2ecca-7d1f-4831-93fc-f946f8ada2c0) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/windows/desktop/5ba2ff28-034f-4949-9bde-8c98345ec7c6)
-   [**DeleteInstanceAsync**](https://msdn.microsoft.com/windows/desktop/7c726842-a274-41d1-b622-681bf9f6ae8b)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/windows/desktop/61966c03-80dc-4556-b2fc-97e879cf458c)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/windows/desktop/d8b55500-d84c-431b-93c6-99d1f1b845c3)
-   [**GetObjectAsync**](https://msdn.microsoft.com/windows/desktop/6868a14d-3776-43a0-b241-b40d42a97afc)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/windows/desktop/fef3eb72-74ba-49cd-b992-292405d29917)

The following table lists the Win32 provider class categories.



| Classes                                                                             | Description                                                               |
|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [Computer System Hardware Classes](computer-system-hardware-classes.md)<br/> | Hardware-related objects.<br/>                                      |
| [Operating System Classes](operating-system-classes.md)<br/>                 | Operating system related objects.<br/>                              |
| [Performance Counter Classes](performance-counter-classes.md)<br/>           | Raw and calculated performance data from performance counters.<br/> |
| [WMI Service Management Classes](wmi-service-management-classes.md)<br/>     | Management for WMI.<br/>                                            |



 

## Related topics

<dl> <dt>

[CIMWin32 WMI Provider](cimwin32-wmi-providers.md)
</dt> </dl>

 

 




