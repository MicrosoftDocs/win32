---
title: How to Register a Device with the Device Host
description: You can register either a running device or a non-running device.
ms.assetid: 40e30881-d5fb-4cf9-8dd7-0d50d2621d5c
ms.topic: article
ms.date: 05/31/2018
---

# How to Register a Device with the Device Host

You can register either a running device or a non-running device.

## Registering a Running Device

Devices are registered using the [**IUPnPRegistrar**](/windows/desktop/api/Upnphost/nn-upnphost-iupnpregistrar) interface. Only administrators are allowed to register running devices. To register a device that has a running device control object, an application must invoke [**IUPnPRegistrar::RegisterRunningDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-registerrunningdevice), passing the following:

-   The text of the device's description.
-   An **IUnknown** pointer to the device control object.
-   An initialization string that is passed to the device control object's [**IUPnPDeviceControl::Initialize**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpdevicecontrol-initialize) method.
-   The location of the resource directory.
-   The lifetime of the device.
-   The Device ID parameter (an OUT parameter), which is the return value of this call; a pointer to the Device ID is returned in C++.

## Registering a Non-Running Device

By default, only administrators and interactive users are allowed to register non-running devices. To register a device with a device control object that is not running, the application uses the [**IUPnPRegistrar::RegisterDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-registerdevice) method.

To programmatically register a device with a non-running device control object, the application must invoke [**IUPnPRegistrar::RegisterDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-registerdevice) and pass it the following parameters:

-   The text of the device's description.
-   The ProgID of the device control object.
-   An initialization string that is passed to the device control object's [**IUPnPDeviceControl::Initialize**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpdevicecontrol-initialize) method.
-   A container ID.
-   The location of the resource directory.
-   The lifetime of the device.
-   The Device ID parameter (an OUT parameter), which is the return value of this call; a pointer to the Device ID is returned in C++.

The registrations of non-running devices can be configured to persist across system boots (the devices are unpublished during the shutdown phase). Therefore, if they are configured this way, devices are published and announced every time the computer is booted.

 

 




