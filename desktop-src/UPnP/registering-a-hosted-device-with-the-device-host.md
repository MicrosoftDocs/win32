---
title: Registering a Hosted Device With the Device Host
description: Registering a hosted device means providing the device host with the device description and its device control object.
ms.assetid: 1d85b412-9b1b-415d-8664-8d96a6644793
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Hosted Device With the Device Host

Registering a hosted device means providing the device host with the device description and its device control object. The device host then constructs a complete UPnP device description, publishes it, and announces the device on the network using the UPnP discovery protocol. Once a device is published, it is available to control points.

Devices are registered in two ways:

-   An application creates an instance of the device control object and passes a pointer to it to the device host.
-   The application passes the ProgID for a registered device control object to the device host. The device host instantiates it when the device host receives the first request for the device.

Regardless of which method is used, the device host publishes and announces the device as soon as it is registered. The difference between the two approaches has to do with when the device code is loaded. When the application passes in a pointer to the device control object, the device code is loaded and running at the time of registration. When the application passes a ProgID, the device code is only loaded when an action is invoked, a property is queried, or an event subscription request arrives. The second approach is slightly more efficient. However, it is not suitable for devices that must be running before any control or event subscription requests arrive, because using this approach, device control objects are only created when they are needed. This second method can also create performance issues when it receives the first request for a device type.

If you want to ensure that a device is announced by the device host on the network automatically when the computer is started, invoke [**IUPnPRegistrar::RegisterDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-registerdevice). **RegisterDevice** ensures that your device code is only loaded when a control or event subscription request is received.

If your devices are transient or bridged, invoke [**IUPnPRegistrar::RegisterRunningDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-registerrunningdevice), and the device is not automatically re-advertised when the computer is restarted.

## Discovery Announcement Lifetime

Each device registered with the device host is associated with a lifetime, which is specified by the device upon registration. The lifetime of the device is the period of time for which the device's discovery announcements are valid. The lifetime is passed to the control point as a header in the initial discovery announcement. The device host automatically refreshes the announcement prior to the expiration time. The values of the discovery announcement lifetime should be 15 minutes or more (the default is 30 minutes).

## Device Identifiers Created at Registration

When creating a device description template, the device developer must provide the resource path to the service description and associated icons. The resource path is determined by the device application.

Since the same device can be registered multiple times on the same computer, the UDN specified in the device description template is not sufficient to uniquely identify a device. Therefore, when a device is registered, the device host creates a device identifier. This device identifier, in association with the UDN in the device description template, can be used to uniquely identify a device.

This identifier is also used when the device is temporarily unregistered and then re-registered. When a device is unregistered temporarily, the device host does not delete the UDN. Reasons for not deleting the UDN include:

-   The device is being upgraded.
-   You are changing the properties of the device.
-   A service is temporarily unavailable.
-   You are adding a new service to a device.
-   You are updating the DLL.
-   The device is in stand-by mode.

Refer to the following sections for further information on registration:

-   [How to Register a Device with the Device Host](how-to-register-a-device-with-the-device-host.md)
-   [Unregistering a Device](unregistering-a-device.md)
-   [**IUPnPRegistrar::UnregisterDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-unregisterdevice)
-   [**IUPnPReregistrar**](/windows/desktop/api/Upnphost/nn-upnphost-iupnpreregistrar)

 

 




