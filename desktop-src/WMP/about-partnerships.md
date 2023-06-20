---
title: About Partnerships
description: About Partnerships
ms.assetid: d21813ed-efe0-48a2-a1bf-f10f4b7ac3e6
keywords:
- Windows Media Player,partnerships
- Windows Media Player object model,partnerships
- object model,partnerships
- Windows Media Player ActiveX control,partnerships
- ActiveX control,partnerships
- Windows Media Player Mobile ActiveX control,partnerships
- Windows Media Player Mobile,partnerships
- synchronizing devices,partnerships
- device synchronization,partnerships
- partnerships between devices and Windows Media Player
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Partnerships

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A partnership is a special relationship between a portable device and Windows Media Player. Users can establish a partnership for a particular device by using the Windows Media Player user interface. You can programmatically manage partnerships by using [IWMPSyncDevice::createPartnership](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-createpartnership) and [IWMPSyncDevice::deletePartnership](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-deletepartnership). The **createPartnership** method starts an asynchronous process that ends when the **CreatePartnershipComplete** event is received through the **IWMPEvents2** interface.

Windows Media Player 10 or later supports creating partnerships with up to 16 devices. Each partnership has an associated partnership index. You can retrieve the partnership index for a particular device by calling [IWMPSyncDevice::get\_partnershipIndex](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-get_partnershipindex). Partnership indices are numbered from 1 to 16. When a particular device does not have a partnership with Windows Media Player, **getPartnershipIndex** returns zero for the index.

You can retrieve the partnership status of a particular device by calling [IWMPSyncDevice::get\_status](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-get_status) and then inspecting the [WMPDeviceStatus](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpdevicestatus) value retrieved. Windows Media Player allows one partnership with one user's library on one computer for each device. This means that creating a new partnership destroys any existing partnership the current device might have with another computer. To know when the status changes for a device, you can receive the **DeviceStatusChange** event.

Windows Media Player cannot create a partnership with a device having the status **wmpdsManualDevice**.

## Related topics

<dl> <dt>

[**About Device Synchronization**](about-device-synchronization.md)
</dt> <dt>

[**IWMPEvents2 Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpevents2)
</dt> <dt>

[**Working with Portable Devices**](working-with-portable-devices.md)
</dt> </dl>

 

 




