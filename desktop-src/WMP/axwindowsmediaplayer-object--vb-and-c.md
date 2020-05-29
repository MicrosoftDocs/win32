---
title: AxWindowsMediaPlayer Object (VB and C )
description: AxWindowsMediaPlayer Object (VB and C\ )
ms.assetid: d7eeac20-1afa-4e73-9af6-9772fbb65516
keywords:
- Windows Media Player,AxWindowsMediaPlayer object
- Windows Media Player Mobile,AxWindowsMediaPlayer object
- Windows Media Player object model,AxWindowsMediaPlayer object
- object model,AxWindowsMediaPlayer object
- ActiveX control,AxWindowsMediaPlayer object
- Windows Media Player ActiveX control,AxWindowsMediaPlayer object
- Windows Media Player Mobile ActiveX control,AxWindowsMediaPlayer object
- reference for object model,AxWindowsMediaPlayer object
- AxWindowsMediaPlayer object
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# AxWindowsMediaPlayer Object (VB and C#)

The AxWindowsMediaPlayer object is the root object for the Windows Media Player control. It supports the properties, methods, and events listed in the following tables.

The AxWindowsMediaPlayer object supports the following properties.



| Property                                                                             | Description                                                                                                                        |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [cdromCollection](axwmplib-axwindowsmediaplayer-cdromcollection--vb-and-c.md)       | Gets an **IWMPCdromCollection** interface.                                                                                         |
| [closedCaption](axwmplib-axwindowsmediaplayer-closedcaption--vb-and-c.md)           | Gets an IWMPClosedCaption interface.                                                                                               |
| [Ctlcontrols](axwmplib-axwindowsmediaplayer-ctlcontrols--vb-and-c.md)               | Gets an IWMPControls interface.                                                                                                    |
| [Ctlenabled](axwmplib-axwindowsmediaplayer-ctlenabled--vb-and-c.md)                 | Gets or sets a value indicating whether the Windows Media Player control is enabled.                                               |
| [currentMedia](axwmplib-axwindowsmediaplayer-currentmedia--vb-and-c.md)             | Gets or sets the IWMPMedia interface that corresponds to the current media item.                                                   |
| [currentPlaylist](axwmplib-axwindowsmediaplayer-currentplaylist--vb-and-c.md)       | Gets or sets the current **IWMPPlaylist** interface.                                                                               |
| [dvd](axwmplib-axwindowsmediaplayer-dvd--vb-and-c.md)                               | Gets an IWMPDVD interface.                                                                                                         |
| [enableContextMenu](axwmplib-axwindowsmediaplayer-enablecontextmenu--vb-and-c.md)   | Gets or sets a value indicating whether to enable the context menu, which appears when the right mouse button is clicked.          |
| [Error](axwmplib-axwindowsmediaplayer-error--vb-and-c.md)                           | Gets an IWMPError interface.                                                                                                       |
| [fullScreen](axwmplib-axwindowsmediaplayer-fullscreen--vb-and-c.md)                 | Gets or sets a value indicating whether video content is played back in full-screen mode.                                          |
| [isOnline](axwmplib-axwindowsmediaplayer-isonline--vb-and-c.md)                     | Gets a value indicating whether the user is connected to a network.                                                                |
| isRemote                                                                             | Not supported for .NET programming.                                                                                                |
| [mediaCollection](axwmplib-axwindowsmediaplayer-mediacollection--vb-and-c.md)       | Gets an IWMPMediaCollection interface.                                                                                             |
| [network](axwmplib-axwindowsmediaplayer-network--vb-and-c.md)                       | Gets an IWMPNetwork interface.                                                                                                     |
| [openState](axwmplib-axwindowsmediaplayer-openstate--vb-and-c.md)                   | Gets a value indicating the state of the content source.                                                                           |
| playerApplication                                                                    | Not supported for .NET programming.                                                                                                |
| [playlistCollection](axwmplib-axwindowsmediaplayer-playlistcollection--vb-and-c.md) | Gets an IWMPPlaylistCollection interface.                                                                                          |
| [playState](axwmplib-axwindowsmediaplayer-playstate--vb-and-c.md)                   | Gets a value indicating the state of the Windows Media Player operation.                                                           |
| [settings](axwmplib-axwindowsmediaplayer-settings--vb-and-c.md)                     | Gets an IWMPSettings interface.                                                                                                    |
| [status](axwmplib-axwindowsmediaplayer-status--vb-and-c.md)                         | Gets a value indicating the current status of Windows Media Player.                                                                |
| [stretchToFit](axwmplib-axwindowsmediaplayer-stretchtofit--vb-and-c.md)             | Gets or sets a value indicating whether video will stretch to fit size of the Windows Media Player control video display.          |
| [uiMode](axwmplib-axwindowsmediaplayer-uimode--vb-and-c.md)                         | Gets or sets a value indicating which controls are shown in the user interface when Windows Media Player is embedded in a webpage. |
| [URL](axwmplib-axwindowsmediaplayer-url--vb-and-c.md)                               | Gets or sets the name of the clip to play.                                                                                         |
| [versionInfo](axwmplib-axwindowsmediaplayer-versioninfo--vb-and-c.md)               | Gets a value that specifies the version of the Windows Media Player.                                                               |
| [windowlessVideo](axwmplib-axwindowsmediaplayer-windowlessvideo--vb-and-c.md)       | Gets or sets a value indicating whether the Windows Media Player control renders video in windowless mode.                         |



 

The AxWindowsMediaPlayer object supports the following methods.



| Method                                                       | Description                                               |
|--------------------------------------------------------------|-----------------------------------------------------------|
| [close](axwmplib-axwindowsmediaplayer-close.md)             | Releases Windows Media Player resources.                  |
| [launchURL](axwmplib-axwindowsmediaplayer-launchurl.md)     | Sends a URL to the user's default browser to be rendered. |
| [newMedia](axwmplib-axwindowsmediaplayer-newmedia.md)       | Returns an IWMPMedia interface for a new media item.      |
| [newPlaylist](axwmplib-axwindowsmediaplayer-newplaylist.md) | returns an IWMPPlaylist interface for a new playlist.     |
| [openPlayer](axwmplib-axwindowsmediaplayer-openplayer.md)   | Opens Windows Media Player using the specified URL.       |



 

The AxWindowsMediaPlayer object supports the following events.



| Event                                                                                                              | Description                                                                                                |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [AudioLanguageChange](axwmplib-axwindowsmediaplayer-audiolanguagechange.md)                                       | Occurs when the current audio language changes.                                                            |
| [Buffering](axwmplib-axwindowsmediaplayer-buffering.md)                                                           | Occurs when the Windows Media Player control begins or ends buffering.                                     |
| [CdromBurnError](axwmplib-axwindowsmediaplayer-cdromburnerror.md)                                                 | Occurs when a generic error happens during a CD burning operation.                                         |
| [CdromBurnMediaError](axwmplib-axwindowsmediaplayer-cdromburnmediaerror.md)                                       | Occurs when an error happens while burning an individual media item to a CD.                               |
| [CdromBurnStateChange](axwmplib-axwindowsmediaplayer-cdromburnstatechange.md)                                     | Occurs when a CD burning operation changes state.                                                          |
| [CdromMediaChange](axwmplib-axwindowsmediaplayer-cdrommediachange.md)                                             | Occurs when a CD or DVD is inserted into or ejected from a CD or DVD drive.                                |
| [CdromRipMediaError](axwmplib-axwindowsmediaplayer-cdromripmediaerror.md)                                         | Occurs when an error happens while ripping an individual track from a CD.                                  |
| [CdromRipStateChange](axwmplib-axwindowsmediaplayer-cdromripstatechange.md)                                       | Occurs when a CD ripping operation changes state.                                                          |
| [Click](axwmplib-axwindowsmediaplayer-click.md)                                                                   | Occurs when the user clicks a mouse button.                                                                |
| CreatePartnershipComplete                                                                                          | Not supported for .NET programming.                                                                        |
| [CurrentItemChange](axwmplib-axwindowsmediaplayer-currentitemchange.md)                                           | Occurs when [IWMPControls.currentItem](wmplibiwmpcontrols-iwmpcontrols-currentitem--vb-and-c.md) changes. |
| [CurrentMediaItemAvailable](axwmplib-axwindowsmediaplayer-currentmediaitemavailable.md)                           | Occurs when a graphic metadata item in the current media item becomes available.                           |
| [CurrentPlaylistChange](axwmplib-axwindowsmediaplayer-currentplaylistchange.md)                                   | Occurs when something changes within the current playlist.                                                 |
| [CurrentPlaylistItemAvailable](axwmplib-axwindowsmediaplayer-currentplaylistitemavailable.md)                     | Occurs when the current playlist item becomes available.                                                   |
| DeviceConnect                                                                                                      | Not supported for .NET programming.                                                                        |
| DeviceDisconnect                                                                                                   | Not supported for .NET programming.                                                                        |
| DeviceStatusChange                                                                                                 | Not supported for .NET programming.                                                                        |
| DeviceSyncError                                                                                                    | Not supported for .NET programming.                                                                        |
| DeviceSyncStateChange                                                                                              | Not supported for .NET programming.                                                                        |
| [Disconnect](axwmplib-axwindowsmediaplayer-disconnect.md)                                                         | Reserved for future use.                                                                                   |
| [DomainChange](axwmplib-axwindowsmediaplayer-domainchange.md)                                                     | Occurs when the DVD domain changes.                                                                        |
| [DoubleClick](axwmplib-axwindowsmediaplayer-doubleclick.md)                                                       | Occurs when the user double-clicks a mouse button.                                                         |
| [DurationUnitChange](axwmplib-axwindowsmediaplayer-durationunitchange.md)                                         | Reserved for future use.                                                                                   |
| [EndOfStream](axwmplib-axwindowsmediaplayer-endofstream.md)                                                       | Reserved for future use.                                                                                   |
| [Error](axwmplib-axwindowsmediaplayer-error.md)                                                                   | Occurs when the Windows Media Player control has an error condition.                                       |
| [FolderScanStateChange](axwmplib-axwindowsmediaplayer-folderscanstatechange.md)                                   | Occurs when a folder monitoring operation changes state.                                                   |
| [KeyDown](axwmplib-axwindowsmediaplayer-keydown.md)                                                               | Occurs when a key is pressed.                                                                              |
| [KeyPress](axwmplib-axwindowsmediaplayer-keypress.md)                                                             | Occurs when a key is pressed and then released.                                                            |
| [KeyUp](axwmplib-axwindowsmediaplayer-keyup.md)                                                                   | Occurs when a key is released.                                                                             |
| [LibraryConnect](axwmplib-axwindowsmediaplayer-libraryconnect.md)                                                 | Occurs when a library becomes available.                                                                   |
| [LibraryDisconnect](axwmplib-axwindowsmediaplayer-librarydisconnect.md)                                           | Occurs when a library is no longer available.                                                              |
| [MarkerHit](axwmplib-axwindowsmediaplayer-markerhit.md)                                                           | Occurs when a marker is reached.                                                                           |
| [MediaChange](axwmplib-axwindowsmediaplayer-mediachange.md)                                                       | Occurs when a media item changes.                                                                          |
| [MediaCollectionAttributeStringAdded](axwmplib-axwindowsmediaplayer-mediacollectionattributestringadded.md)       | Occurs when an attribute value is added to the library.                                                    |
| [MediaCollectionAttributeStringChanged](axwmplib-axwindowsmediaplayer-mediacollectionattributestringchanged.md)   | Occurs when an attribute value in the library is changed.                                                  |
| [MediaCollectionAttributeStringRemoved](axwmplib-axwindowsmediaplayer-mediacollectionattributestringremoved.md)   | Occurs when an attribute value is removed from the library.                                                |
| [MediaCollectionChange](axwmplib-axwindowsmediaplayer-mediacollectionchange.md)                                   | Occurs when the media collection changes.                                                                  |
| [MediaCollectionMediaAdded](axwmplib-axwindowsmediaplayer-mediacollectionmediaadded.md)                           | Occurs when a media item is added to the local library.                                                    |
| [MediaCollectionMediaRemoved](axwmplib-axwindowsmediaplayer-mediacollectionmediaremoved.md)                       | Occurs when a media item is removed from the local library.                                                |
| [MediaError](axwmplib-axwindowsmediaplayer-mediaerror.md)                                                         | Occurs when the **Media** object has an error condition.                                                   |
| [ModeChange](axwmplib-axwindowsmediaplayer-modechange.md)                                                         | Occurs when a mode of Windows Media Player is changed.                                                     |
| [MouseDown](axwmplib-axwindowsmediaplayer-mousedown.md)                                                           | Occurs when a mouse button is pressed.                                                                     |
| [MouseMove](axwmplib-axwindowsmediaplayer-mousemove.md)                                                           | Occurs when the mouse pointer is moved.                                                                    |
| [MouseUp](axwmplib-axwindowsmediaplayer-mouseup.md)                                                               | Occurs when a mouse button is released.                                                                    |
| [NewStream](axwmplib-axwindowsmediaplayer-newstream.md)                                                           | Reserved for future use.                                                                                   |
| [OpenPlaylistSwitch](axwmplib-axwindowsmediaplayer-openplaylistswitch.md)                                         | Occurs when a title on a DVD begins playing.                                                               |
| [OpenStateChange](axwmplib-axwindowsmediaplayer-openstatechange.md)                                               | Occurs when the Windows Media Player control changes state.                                                |
| PlayerDockedStateChange                                                                                            | Not supported for .NET programming.                                                                        |
| PlayerReconnect                                                                                                    | Not supported for .NET programming.                                                                        |
| [PlaylistChange](axwmplib-axwindowsmediaplayer-playlistchange.md)                                                 | Occurs when a playlist changes.                                                                            |
| [PlaylistCollectionChange](axwmplib-axwindowsmediaplayer-playlistcollectionchange.md)                             | Occurs when something changes in the playlist collection.                                                  |
| [PlaylistCollectionPlaylistAdded](axwmplib-axwindowsmediaplayer-playlistcollectionplaylistadded.md)               | Occurs when a playlist is added to the playlist collection.                                                |
| [PlaylistCollectionPlaylistRemoved](axwmplib-axwindowsmediaplayer-playlistcollectionplaylistremoved.md)           | Occurs when a playlist is removed from the playlist collection.                                            |
| [PlaylistCollectionPlaylistSetAsDeleted](axwmplib-axwindowsmediaplayer-playlistcollectionplaylistsetasdeleted.md) | Reserved for future use.                                                                                   |
| [PlayStateChange](axwmplib-axwindowsmediaplayer-playstatechange.md)                                               | Occurs when the play state of the Windows Media Player control changes.                                    |
| [PositionChange](axwmplib-axwindowsmediaplayer-positionchange.md)                                                 | Occurs when the current position of the media item has been changed.                                       |
| [ScriptCommand](axwmplib-axwindowsmediaplayer-scriptcommand.md)                                                   | Occurs when a synchronized command or URL is received.                                                     |
| [StatusChange](axwmplib-axwindowsmediaplayer-statuschange.md)                                                     | Occurs when the **status** property changes value.                                                         |
| [StringCollectionChange](axwmplib-axwindowsmediaplayer-stringcollectionchange.md)                                 | Occurs when a string collection changes.                                                                   |
| SwitchedToControl                                                                                                  | Not supported for .NET programming.                                                                        |
| SwitchedToPlayerApplication                                                                                        | Not supported for .NET programming.                                                                        |
| [Warning](axwmplib-axwindowsmediaplayer-warning.md)                                                               | Reserved for future use.                                                                                   |



 

## Related topics

<dl> <dt>

[**Interfaces for Visual Basic .NET and C#**](interfaces-for-visual-basic--net-and-c.md)
</dt> <dt>

[**IWMPCdromCollection Interface (VB and C#)**](iwmpcdromcollection--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption Interface (VB and C#)**](iwmpclosedcaption--vb-and-c.md)
</dt> <dt>

[**IWMPControls Interface (VB and C#)**](iwmpcontrols--vb-and-c.md)
</dt> <dt>

[**IWMPDVD Interface (VB and C#)**](iwmpdvd--vb-and-c.md)
</dt> <dt>

[**IWMPError Interface (VB and C#)**](iwmperror--vb-and-c.md)
</dt> <dt>

[**IWMPMedia Interface (VB and C#)**](iwmpmedia--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> <dt>

[**IWMPNetwork Interface (VB and C#)**](iwmpnetwork--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylist Interface (VB and C#)**](iwmpplaylist--vb-and-c.md)
</dt> <dt>

[**IWMPPlaylistCollection Interface (VB and C#)**](iwmpplaylistcollection--vb-and-c.md)
</dt> <dt>

[**IWMPSettings Interface (VB and C#)**](iwmpsettings--vb-and-c.md)
</dt> <dt>

[**Object Model Reference for Visual Basic .NET and C#**](object-model-reference-for-visual-basic--net-and-c.md)
</dt> <dt>

[**WMPOpenState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpopenstate)
</dt> <dt>

[**WMPPlayState**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmpplaystate)
</dt> </dl>

 

 




