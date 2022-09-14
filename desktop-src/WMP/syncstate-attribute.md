---
title: SyncState Attribute
description: The SyncState attribute is a string representation of a 32-bit value that Windows Media Player uses when it synchronizes playlists with portable devices.
ms.assetid: affc3d1c-7fe6-4811-acfc-57285cb181ca
keywords:
- SyncState Attribute Windows Media Player
topic_type:
- apiref
api_name:
- SyncState
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SyncState Attribute

The **SyncState** attribute is a string representation of a 32-bit value that Windows Media Player uses when it synchronizes playlists with portable devices.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Photo Items](photo-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute consists of sixteen 2-bit values, each of which specifies the synchronization state of a portable device. The most significant bit (MSB) of this 32-bit value corresponds to device 16. The least significant bit (LSB) corresponds to device 1.

The MSB of each 2-bit value indicates whether Windows Media Player synchronized the content with the corresponding device. A value of 1 indicates that it did. A value of 0 indicates that it did not.

If the MSB is 0, the LSB specifies why the synchronization failed. A value of 1 in the LSB indicates that there was not enough free space for the content. A value of 0 in the LSB indicates some other reason prevented synchronization.

To retrieve the synchronization state of a given device, you should do the following:

1.  Invoke **IWMPSyncDevice::get\_status** to determine whether a given device is synchronized.
2.  If it is synchronized, invoke **IWMPSyncDevice::get\_partnershipIndex** to retrieve the index of the device's bit pair in the **SyncState** attribute.
3.  Using this index, mask the corresponding bit pair of the **SyncState** attribute and examine the result to determine the synchronization state of the playlist with the device.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------|
| Version<br/> | Windows Media Player 10 or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> <dt>

[**Determining Playlist Synchronization State**](determining-playlist-synchronization-state.md)
</dt> <dt>

[**IWMPSyncDevice::get\_partnershipIndex**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-get_partnershipindex)
</dt> <dt>

[**IWMPSyncDevice::get\_status**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-get_status)
</dt> </dl>

 

 





