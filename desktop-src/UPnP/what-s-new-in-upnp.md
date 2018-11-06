---
title: What's New in the UPnP APIs
description: The UPnP™ APIs have new features and updated documentation for Windows XP SP2. The following table identifies the new documentation.
ms.assetid: ad72d9b8-6db4-4b9b-9b10-ae3980521d7e
ms.topic: article
ms.date: 05/31/2018
---

# What's New in the UPnP APIs

The UPnP™ APIs have new features and updated documentation for Windows XP SP2. The following table identifies the new documentation.



| Feature                                                          | Description                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUPnPRemoteEndpointInfo**](/windows/desktop/api/Upnphost/nn-upnphost-iupnpremoteendpointinfo)       | This new interface allows a hosted device to obtain information about a requester (that is, a control point) and the request. It includes three methods, each of which provides a different type of information.                                                                                                                                                              |
| [Implementing Device Behavior](implementing-device-behavior.md) | This topic includes a new section that explains how to obtain endpoint information by using the new [**IUPnPRemoteEndpointInfo**](/windows/desktop/api/Upnphost/nn-upnphost-iupnpremoteendpointinfo) interface.                                                                                                                                                                                                     |
| [Configuration Settings](configuration-settings.md)             | This new topic provides information about the registry settings that affect the behavior of the UPnP APIs.                                                                                                                                                                                                                                                                    |
| [Device Error Codes](device-error-codes.md)                     | This new topic explains how an error code from a device is converted to an HRESULT value and vice versa. An understanding of this process is necessary in order to evaluate an HRESULT value that is returned by the [**IUPnPService::InvokeAction**](/windows/desktop/api/Upnp/nf-upnp-iupnpservice-invokeaction) and [**IUPnPService::QueryStateVariable**](/windows/desktop/api/Upnp/nf-upnp-iupnpservice-querystatevariable) methods. |



 

 

 




