---
Description: The MSFT\_Providers class and the WMI troubleshooting classes are a group of the MSFT event classes coupled to WMI provider events.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5eaf7026-87bf-416b-9a6d-7f92f85b0882
ms.tgt_platform: multiple
title: Provider Configuration and Troubleshooting Classes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Provider Configuration and Troubleshooting Classes

The [**MSFT\_Providers**](https://msdn.microsoft.com/library/aa392509) class and the WMI troubleshooting classes are a group of the [MSFT event classes](msft-classes.md) coupled to WMI provider events.

The [**MSFT\_Providers**](https://msdn.microsoft.com/library/aa392509) class contains configuration information for providers and includes the following methods that allow you to load and unload providers, or suspend and resume provider operations:

-   [**Load Method of the MSFT\_Providers Class**](https://msdn.microsoft.com/library/aa392266)
-   [**UnLoad Method of the MSFT\_Providers Class**](https://msdn.microsoft.com/library/aa393944)
-   [**Resume Method of the MSFT\_Providers Class**](https://msdn.microsoft.com/library/aa393236)
-   [**Suspend Method of the MSFT\_Providers Class**](https://msdn.microsoft.com/library/aa393685)

The [WMI troubleshooting classes](wmi-troubleshooting-classes.md) are named to indicate whether the event is fired before or after a provider event. For example, the [**MSFT\_WmiProvider\_AccessCheck\_Pre**](https://msdn.microsoft.com/library/aa392546) object is generated immediately before calling the provider's implementation of **IWbemEventSecurity::AccessCheck**, while the [**MSFT\_WmiProvider\_AccessCheck\_Post**](https://msdn.microsoft.com/library/aa392545) object is called immediately after.

## Related topics

<dl> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> <dt>

[WMI Troubleshooting Classes](wmi-troubleshooting-classes.md)
</dt> </dl>

 

 



