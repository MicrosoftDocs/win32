---
Description: The WDM (Windows Driver Model) provider grants access to the classes, instances, methods, and events of hardware drivers that conform to the WDM model.
ms.assetid: 2f9749ff-b318-4228-80fd-e3846dde21d2
title: WDM Provider
ms.topic: article
ms.date: 05/31/2018
---

# WDM Provider

The WDM (Windows Driver Model) provider grants access to the classes, instances, methods, and events of hardware drivers that conform to the WDM model. The classes for hardware drivers reside in the "root\\wmi namespace".

WDM classes are defined primarily in Wmi.mof.

WDM is an operating system interface through which hardware components provide information and event notification. The WDM provider is a class, instance, event, and method provider that allows management applications access to data and events from WMI-for-WDM enabled device drivers. The classes created by the WDM provider to represent device driver data reside only in the "Root\\WMI" namespace. This namespace must already exist before the WDM provider will process the installed WDM drivers.

The WDM provider records information about WDM operations in the WmiProv.log file. For more information, see [WMI Log Files](https://msdn.microsoft.com/library/aa394564).

As a class, instance, method, and event provider, the WDM provider implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface, as well as the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateClassEnumAsync**](https://msdn.microsoft.com/library/aa392096)
-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)
-   [**ExecNotificationQueryAsync**](https://msdn.microsoft.com/library/aa392106)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The WDM provider supports the [**WMIEvent**](https://msdn.microsoft.com/library/windows/desktop/aa394532) extrinsic event, which notifies WMI regarding events from WDM-based drivers. You can register your event consumers for **WMIEvent** events as you would any other event. For more information, see [Receiving a WMI Event](https://msdn.microsoft.com/library/aa393013). No class creation events are raised when starting a driver.

The WDM provider supports the following class:

-   [**WMIBinaryMofResource**](wmibinarymofresource.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> <dt>

[Accessing Data from Device Drivers](https://msdn.microsoft.com/library/aa384721)
</dt> </dl>

 

 



