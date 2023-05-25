---
title: Device Extensions for Accelerated Metadata Transfer
description: Device Extensions for Accelerated Metadata Transfer
ms.assetid: a79b54d4-dad5-411b-aaff-b58bb549d4d1
keywords:
- Windows Media Player,device extensions
- Windows Media Player,extensions
- Windows Media Player,accelerated metadata transfer
- Windows Media Player,metadata accelerated transfer
- accelerated metadata transfer
- metadata,accelerated transfer
- device extensions,accelerated metadata transfer
- extensions,accelerated metadata transfer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Extensions for Accelerated Metadata Transfer

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player 10 introduced new and extended functionality for synchronizing digital media files with portable devices. Users can connect a device to a computer, transfer content to the device, and then disconnect the device to enjoy content away from the computer.

When the user reconnects the device to the computer, it is possible that the content stored on the device changed since the previous connection. For example, simply playing a particular digital media file causes the play count for that item to change. Because current portable devices can store large quantities of digital media content, the process of discovering changes would be too time consuming if Windows Media Player were required to enumerate and inspect each digital media item. Instead, portable device manufacturers can implement special functionality to enable Windows Media Player 10 or later to efficiently retrieve information about changes made to the content stored on a device.

The following sections describe the conventions used to implement this functionality.

-   [About the Metadata](about-the-metadata.md)
-   [MTP Device Extensions for Metadata Transfer](mtp-device-extensions-for-metadata-transfer.md)
-   [Windows Media Device Manager Device Extensions for Metadata Transfer](windows-media-device-manager-device-extensions-for-metadata-transfer.md)

## Related topics

<dl> <dt>

[**Windows Media Player**](windows-media-player.md)
</dt> </dl>

 

 




