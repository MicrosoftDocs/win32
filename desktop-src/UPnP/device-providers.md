---
title: Device Providers
description: Device providers are registered objects that the computer starts on every system startup.
ms.assetid: 80c08993-0a8b-4ee9-93cd-bcc3c00e843b
ms.topic: article
ms.date: 05/31/2018
---

# Device Providers

Device providers are registered objects that the computer starts on every system startup. Device providers register and unregister running devices with the device host in response to some event. These devices are devices that have been automatically started at system startup time. For security reasons, a device provider should generally run as [LocalService](/windows/desktop/Services/localservice-account), rather than [LocalSystem](/windows/desktop/Services/localsystem-account).

Device providers can be used for transient devices. Device providers can also be used to bridge devices to polled media. For example, a peripheral device such as a digital music player is connected to a computer via a serial port. To expose the music player as a UPnP-based device, a device control object and a set of service objects are required. These objects implement the UPnP-based music player actions as serial commands. However, the music player must be plugged into the serial port and available for control before these objects are registered.

Because the serial port does not offer an explicit notification mechanism when devices are connected, polling code is required. This code can be implemented in a device provider object, a service, or in a standalone application. When the computer is started, the device host instantiates the device provider object, and then invokes its [**Start**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpdeviceprovider-start) method. When the device provider detects the presence of a music player device, it instantiates the appropriate device control object and registers it by calling [**IUPnPRegistrar::RegisterRunningDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-registerrunningdevice). This method publishes the device and announces it to the UPnP-based network.

The same functionality can also be achieved by implementing a service that polls the serial port. However, device providers simplify things by requiring only the core functionality—the polling—to be implemented because device providers rely on the device host to start and stop them. Using device providers is simpler than implementing a service.

At registration time, and on every subsequent system startup, the computer instantiates the device provider object, and then invokes its [**IUPnPDeviceProvider::Start**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpdeviceprovider-start) method, passing it the initialization string specified during registration.

Once the [**Start**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpdeviceprovider-start) method is called, the device provider performs any necessary processing, and when necessary, the device provider registers devices by calling [**IUPnPRegistrar::RegisterRunningDevice**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpregistrar-registerrunningdevice), as described in the section [Registering a Hosted Device with the Device Host](registering-a-hosted-device-with-the-device-host.md).

When the computer is shut down, the device host invokes the [**IUPnPDeviceProvider::Stop**](/windows/desktop/api/Upnphost/nf-upnphost-iupnpdeviceprovider-stop) method to indicate that the device provider terminate its operations.

 

 