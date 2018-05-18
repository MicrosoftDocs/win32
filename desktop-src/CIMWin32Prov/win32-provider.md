---
Description: 'The Microsoft&\#160;Win32 provider retrieves and updates data relevant to Windows systems&\#8212;data such as the current settings of environment variables and the attributes of a logical disk.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '71c13736-0504-4d50-b8a4-5d68d4ba9a90'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Win32 Provider
---

# Win32 Provider

The Microsoft Win32 provider retrieves and updates data relevant to Windows systems—data such as the current settings of environment variables and the attributes of a logical disk. With the Win32 provider, management applications can use WMI to easily access this data. The Win32 provider retrieves its information by making Windows function calls and querying the system registry.

The Win32 provider defines the classes used to describe hardware or software available on Windows systems and the relationships between them.

As an instance and method provider, the Win32 provider implements the standard [**IWbemProviderInit**](wmi.iwbemproviderinit) interface as well as the following [**IWbemServices**](wmi.iwbemservices) methods:

-   [**CreateInstanceEnumAsync**](wmi.iwbemservices_createinstanceenumasync)
-   [**DeleteInstanceAsync**](wmi.iwbemservices_deleteinstanceasync)
-   [**ExecMethodAsync**](wmi.iwbemservices_execmethodasync)
-   [**ExecQueryAsync**](wmi.iwbemservices_execqueryasync)
-   [**GetObjectAsync**](wmi.iwbemservices_getobjectasync)
-   [**PutInstanceAsync**](wmi.iwbemservices_putinstanceasync)

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

 

 




