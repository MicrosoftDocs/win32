---
title: About Device Synchronization
description: About Device Synchronization
ms.assetid: 87976357-f819-41ac-9645-36e799876881
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
- synchronizing devices,manual transfer
- device synchronization,manual transfer
- synchronizing devices,automatic synchronization
- device synchronization,automatic synchronization
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About Device Synchronization

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Windows Media Player 10 introduced a new model for synchronizing digital media content with portable devices. From the user's perspective, this means you can specify which playlists (including auto playlists) synchronize automatically with devices. You can also manually transfer digital media content to devices. From the developer's perspective, this means there is new functionality exposed that you can take advantage of in your applications. To do this, you must create a remoted instance of the Windows Media Player control.

There are two ways a user can copy digital media content to a device:

-   **Manual transfer.** The user selects digital media content in the library and then initiates a transfer of the content to the device. This is similar to the functionality provided by previous versions of Windows Media Player. The Windows Media Player SDK does not provide methods for transferring digital media to a device.
-   **Automatic synchronization.** The user specifies playlists that automatically synchronize with the device. This is a feature of Windows Media Player 10 or later. The Windows Media Player SDK provides functionality for managing automatic synchronization. This functionality is designed to let you build a custom user interface for your application to specify how device synchronization happens and to provide status information to users.

For automatic synchronization to work, a special relationship must be established between Windows Media Player and the device. This relationship is called a *partnership*.

The following sections provide more information about device synchronization.

-   [About Devices](about-devices.md)
-   [About Partnerships](about-partnerships.md)
-   [About the Synchronization Engine](about-the-synchronization-engine.md)
-   [About Playlist Synchronization](about-playlist-synchronization.md)

## Related topics

<dl> <dt>

[**About the Player Object Model**](about-the-player-object-model.md)
</dt> <dt>

[**Remoting the Windows Media Player Control**](remoting-the-windows-media-player-control.md)
</dt> <dt>

[**Working with Portable Devices**](working-with-portable-devices.md)
</dt> </dl>

 

 




