---
title: About Playlist Synchronization
description: About Playlist Synchronization
ms.assetid: bc7d52e0-7906-4b5b-82e6-a84e9c4f0ff0
keywords:
- Windows Media Player,playlist synchronization
- Windows Media Player object model,playlist synchronization
- object model,playlist synchronization
- Windows Media Player ActiveX control,playlist synchronization
- ActiveX control,playlist synchronization
- Windows Media Player Mobile ActiveX control,playlist synchronization
- Windows Media Player Mobile,playlist synchronization
- synchronizing devices,playlists
- device synchronization,playlists
- playlists,synchronization
- Windows Media metafile playlists,synchronization
- metafile playlists,synchronization
ms.topic: article
ms.date: 05/31/2018
---

# About Playlist Synchronization

Windows Media Player 10 or later is designed to synchronize digital media content to devices using a playlist synchronization model. This means that content intended to be copied to a device must be part of a playlist. When the user chooses to transfer individual digital media content from his or her computer to a device, Windows Media Player adds the content to a default playlist for copying.

The Windows Media Player device synchronization APIs are designed to work like this as well. Like Windows Media Player, your program can present the user with a list of playlists that he or she has defined. You can then enable the user to choose which playlists to synchronize with a particular device and to set the priority order for the synchronization process.

Because portable devices have a limited storage capacity, it is possible for the user to choose to synchronize more digital media content than the device can store. Windows Media Player synchronizes content in priority order. The user can define the priority order by using a dialog box that can be accessed from the **Devices** feature. In response to user input to your program, you can change the priority order programmatically by changing the values of certain playlist attributes. Collectively, these attributes are called the *Sync* attributes.

Each playlist in a library has 16 synchronization attributes: **Sync01** through **Sync16**. Each attribute represents the device that has the corresponding partnership index. The value of each attribute tells you two things:

-   Whether the playlist should be synchronized with the device.
-   The priority value for the playlist.

A value of zero indicates that Windows Media Player should not attempt to synchronize the playlist with the device. Any other value is a priority number. Lower values receive higher priority at synchronization time.

Playlists also have a **SyncOnly** attribute that indicates whether the playlist is available only for synchronization.

Individual items of digital media content contain metadata about synchronization as well. When you retrieve a **Media** object from the library, you can inspect the value of the **SyncState** attribute. This attribute provides extended information about whether the content has been successfully copied to the device or whether copying the content failed because it would not fit.

> [!Note]  
> You should avoid providing user interface elements that enable the user to create playlists from all library content for synchronization.

 

To optimize performance, Windows Media Player enforces a set of rules for creating synchronization playlists. Your program should only create synchronization playlists for content you provided. Allow Windows Media Player to create synchronization playlists for content that the user added to the library from other sources.

As an alternative to creating your own playlist user interface, you can present users with a default dialog box for choosing playlists and managing the partnership for a device. To do this, call [IWMPSyncDevice::showSettings](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpsyncdevice-showsettings). When you invoke this method, Windows Media Player displays its synchronization settings dialog box. When the user closes the dialog box, Windows Media Player automatically returns to its prior docking state and passes control back to your remoted program.

## Related topics

<dl> <dt>

[**About Device Synchronization**](about-device-synchronization.md)
</dt> <dt>

[**Managing Synchronization Playlists**](managing-synchronization-playlists.md)
</dt> <dt>

[**Playlist Attributes**](playlist-attributes.md)
</dt> </dl>

 

 




