---
title: About the Synchronization Engine
description: About the Synchronization Engine
ms.assetid: bb57ffb0-3833-463b-b66c-c23224fa2ba7
keywords:
- Windows Media Player,synchronization engine
- Windows Media Player object model,synchronization engine
- object model,synchronization engine
- Windows Media Player ActiveX control,synchronization engine
- ActiveX control,synchronization engine
- Windows Media Player Mobile ActiveX control,synchronization engine
- Windows Media Player Mobile,synchronization engine
- synchronizing devices,synchronization engine
- device synchronization,synchronization engine
- synchronization engine
ms.topic: article
ms.date: 05/31/2018
---

# About the Synchronization Engine

The synchronization engine is the component of Windows Media Player that manages copying digital media content to portable devices. Windows Media Player supports a single instance of the synchronization engine for each device. You must use a remoted instance of the Windows Media Player control to perform synchronization tasks programmatically. In effect, your program shares the synchronization engine instances with Windows Media Player and all other programs that use the Player interfaces for device synchronization.

You can use [IWMPSyncDevice::start](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-start) and [IWMPSyncDevice::stop](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-stop) to control when the synchronization engine does its work. In most cases, you should not use these methods. Instead, you should let the synchronization engine schedule its work automatically. The **start** and **stop** methods exist so that you can use them if your program is designed to replace the Windows Media Player user interface. In this case, you might want to provide a start/stop button similar to the one Windows Media Player provides in the **Devices** tab.

You can monitor the synchronization progress for a device by polling [IWMPSyncDevice::get\_progress](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-get_progress). This method retrieves a progress value for the entire synchronization process with a particular device. The value retrieved is a number that represents the percentage of synchronization complete. There are two events you can receive that are related to synchronization. The **DeviceSyncError** event notifies you when a problem occurs. The **DeviceSyncStateChange** event alerts you when the synchronization engine has changed state for the current device.

You can limit the amount of device storage that Windows Media Player uses for synchronization by calling [IWMPSyncDevice2::setItemInfo](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice2-setiteminfo) with the **PercentSpaceReserved** attribute. Using this interface requires Windows Media Player 11.

## Related topics

<dl> <dt>

[**About Device Synchronization**](about-device-synchronization.md)
</dt> <dt>

[**IWMPEvents2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents2)
</dt> <dt>

[**Showing Synchronization Progress**](showing-synchronization-progress.md)
</dt> </dl>

 

 




