---
title: About Devices
description: About Devices
ms.assetid: 9e68c5eb-5fcb-4d7d-8dbb-7e951f253df8
keywords:
- Windows Media Player,synchronizing devices
- Windows Media Player object model,synchronizing devices
- object model,synchronizing devices
- Windows Media Player ActiveX control,synchronizing devices
- ActiveX control,synchronizing devices
- Windows Media Player Mobile ActiveX control,synchronizing devices
- Windows Media Player Mobile,synchronizing devices
- synchronizing devices,about
- device synchronization,about
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Devices

Portable devices are hardware devices that users carry to enjoy digital media content when they are away from their computer. Typically, portable devices are battery operated. Some devices can play music only. Other devices can play video and music.

Some devices support automatic synchronization of digital media content with Windows Media Player. Other devices support only manual transfer. You can determine whether a particular device supports automatic synchronization by calling [IWMPSyncDevice::get\_status](/windows/win32/wmp/nf-wmp-iwmpsyncdevice-get_status?branch=master) and then inspecting the [WMPDeviceStatus](/windows/win32/wmp/ne-wmp-wmpdevicestatus?branch=master) value retrieved. If the retrieved value is **wmpdsManualDevice**, the device does not support automatic synchronization.

You can enumerate the devices connected to the user's computer. To do this, first use [IWMPSyncServices::get\_deviceCount](/windows/win32/wmp/nf-wmp-iwmpsyncservices-get_devicecount?branch=master) to retrieve the count of devices. Then, in a loop, call [IWMPSyncServices::getDevice](/windows/win32/wmp/nf-wmp-iwmpsyncservices-getdevice?branch=master), passing the appropriate index value each time. You can use [IWMPSyncDevice::get\_connected](/windows/win32/wmp/nf-wmp-iwmpsyncdevice-get_connected?branch=master) to evaluate whether a particular device is currently connected.

To know when devices connect or disconnect, you can receive the **DeviceConnect** and **DeviceDisconnect** events. These events are received through the **IWMPEvents2** interface.

The **IWMPSyncDevice** interface provides additional methods to enable you to get or set information about a device. For example:

-   The **get\_FriendlyName** and **put\_FriendlyName** methods enable you to retrieve and specify the user-defined device name.
-   The **get\_deviceName** method enables you to retrieve the device name that users see in the Windows XP shell.
-   The **getItemInfo** method enables you to retrieve metadata from devices.

## Related topics

<dl> <dt>

[**About Device Synchronization**](about-device-synchronization.md)
</dt> <dt>

[**IWMPEvents2 Interface**](/windows/win32/wmp/nn-wmp-iwmpevents2?branch=master)
</dt> <dt>

[**IWMPSyncDevice Interface**](/windows/win32/wmp/nn-wmp-iwmpsyncdevice?branch=master)
</dt> <dt>

[**Working with Portable Devices**](working-with-portable-devices.md)
</dt> </dl>

 

 




