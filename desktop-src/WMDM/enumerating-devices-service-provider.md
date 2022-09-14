---
title: Enumerating devices (WMDM)
description: Windows Media Device Manager maintains a cache of connected devices. Learn how Windows Media Device Manager maintains or updates its cache.
ms.assetid: 7602da65-4c98-4766-b206-2129dad4cc2a
keywords:
- Windows Media Device Manager,enumerating devices
- Device Manager,enumerating devices
- programming guide,enumerating devices
- service providers,enumerating devices
- creating service providers,enumerating devices
- enumerating devices
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating devices (WMDM)

Windows Media Device Manager maintains a cache of connected devices that is updated when a Windows Media Device Manager application starts, when a Plug and Play (PnP) device connects or disconnects, or when the application calls [**IWMDeviceManager2::Reinitialize**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdevicemanager2-reinitialize). This cache is exposed to the application when it calls [**IWMDeviceManager::EnumDevices**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdevicemanager-enumdevices) or [**IWMDeviceManager2::EnumDevices2**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdevicemanager2-enumdevices2). Each device is exposed to the application as an [**IWMDMDevice**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice) interface. If the service provider is registered to handle PnP devices, Windows Media Device Manager will be aware of the current list of connected devices. If the service provider is registered to handle non-PnP devices, the service provider is responsible for discovering attached devices. A service provider can only be registered for PnP or non-PnP devices, never both.

The following actions show how Windows Media Device Manager maintains or updates its cache. Notice that the cache is never updated when a non-PnP device connects or disconnects.

A Windows Media Device Manager application starts

-   Windows Media Device Manager retrieves a list of attached PnP devices from the PnP subsystem, and calls [**IMDServiceProvider2::CreateDevice**](/windows/desktop/api/mswmdm/nf-mswmdm-imdserviceprovider2-createdevice) on the SP registered for each connected device. (It discovers the correct service provider by querying the WMDMSPCLSID device parameter for the class ID of the service provider responsible for this device. See [Device Parameters](device-parameters.md) for more information.) All devices returned are added to the Windows Media Device Manager cache of devices.
-   Windows Media Device Manager finds all non-PnP service providers registered with it and calls [**IMDServiceProvider::EnumDevices**](/windows/desktop/api/mswmdm/nf-mswmdm-imdserviceprovider-enumdevices) on each service provider to get a list devices from each one. All devices returned are added to the cache.

The application calls IWMDeviceManager/2::EnumDevices/2

-   Windows Media Device Manager returns its cached device list.

A PnP device connects

-   Windows Media Device Manager finds the relevant service provider and calls **IMDServiceProvider2::CreateDevice**, and adds the device to its cache.
-   If the application implements [**IWMDMNotification**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmnotification), Windows Media Device Manager calls [**IWMDMNotification::WMDMMessage**](/windows/desktop/api/mswmdm/nf-mswmdm-iwmdmnotification-wmdmmessage) with an arrival notification.

A PnP device disconnects

-   Windows Media Device Manager removes the item from its cache.
-   If the application implements IWMDMNotification, Windows Media Device Manager calls IWMDMNotification::WMDMMessage with a departure notification.

The application calls IWMDeviceManager2::Reinitialize

-   Refreshes the cache with all connected devices.

A non-PnP device connects or disconnects

-   Windows Media Device Manager is not informed of the arrival or departure, and takes no action.

## Related topics

<dl> <dt>

[**Creating a Service Provider**](creating-a-service-provider.md)
</dt> </dl>

 

 




