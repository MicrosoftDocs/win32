---
title: Device Host Security Considerations
description: Using the device host creates security issues.
ms.assetid: 7cb445ea-5df4-4030-babd-62527b4d6210
ms.topic: article
ms.date: 05/31/2018
---

# Device Host Security Considerations

Using the device host creates security issues because of the following:

-   Devices hosted on a computer running Windows XP sends announcements on all networks.
-   Devices hosted on a computer running Windows XP allow control of devices from all networks.

This increases the risk to home consumers, because devices such as a media player or a bridged lighting or HVAC system hosted on a computer running Windows XP are visible and can be controlled from control points outside the home.

When you are creating a hosted device, you need to take into consideration some security issues.

-   To reduce the scope of discovery and attack of UPnP-based devices, the TTL of all SSDP messages is 1. This means that a registered device is only discovered by control points on the same network. You can configure a higher TTL in the registry.
-   Registering a non-running device requires pre-registering the device .dll with COM, which requires administrator privilege.
-   Registering a running device requires Administrator, Local Service, or Local System privilege.
-   When the device host is started, it is run as [LocalService](/windows/desktop/Services/localservice-account). This gives the device the ability to generate audits and read the **HKEY\_LOCAL\_MACHINE** registry key. The device does have access to **HKEY\_CURRENT\_USER**. The LocalService account can use resources to which LocalService has been granted access, as well as those that grant access to AuthenticatedUser. The device has restricted file system access.
-   The file system ACLs must be updated to allow [LocalService](/windows/desktop/Services/localservice-account) access to the resource directory.
-   If your device must have more security access, you can create your own process for the device and register it by using [**IUPnPRegistrar::RegisterRunningDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-registerrunningdevice).

 

 