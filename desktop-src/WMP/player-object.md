---
title: Player Object
description: The Player object is the root object for the Windows Media Player control. It supports the properties, methods, and events listed in the following tables.
ms.assetid: '694bd6cc-c816-478a-87b9-1526e2d18869'
keywords:
- Player Object Windows Media Player
topic_type:
- apiref
api_name:
- Player Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Player Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Player object is the root object for the Windows Media Player control. It supports the properties, methods, and events listed in the following tables.

The Player object supports the following properties. Properties marked with an asterisk (\*) are not accessible to skins.



| Property                                             | Description                                                                                                                                  |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [cdromCollection](player-cdromcollection.md)        | Retrieves the [CdromCollection](cdromcollection-object.md) object.                                                                          |
| [closedCaption](player-closedcaption.md)            | Retrieves the [ClosedCaption](closedcaption-object.md) object.                                                                              |
| [controls](player-controls.md)                      | Retrieves the [Controls](controls-object.md) object.                                                                                        |
| [currentMedia](player-currentmedia.md)              | Specifies or retrieves the current [Media](media-object.md) object.                                                                         |
| [currentPlaylist](player-currentplaylist.md)        | Specifies or retrieves the current [Playlist](playlist-object.md) object.                                                                   |
| [dvd](player-dvd.md)                                | Retrieves the [DVD](dvd-object.md) object.                                                                                                  |
| [enableContextMenu](player-enablecontextmenu.md) \* | Specifies or retrieves a value indicating whether to enable the context menu, which appears when the right mouse button is clicked.          |
| [enabled](player-enabled.md) \*                     | Specifies or retrieves a value indicating whether the Windows Media Player control is enabled.                                               |
| [error](player-error.md)                            | Retrieves the [Error](error-object.md) object.                                                                                              |
| [fullScreen](player-fullscreen.md) \*               | Specifies or retrieves a value indicating whether video content is played back in full-screen mode.                                          |
| [isOnline](player-isonline.md)                      | Retrieves a value indicating whether the user is connected to a network.                                                                     |
| [isRemote](player-isremote.md) \*                   | Retrieves a value indicating whether the Windows Media Player control is running in remote mode.                                             |
| [mediaCollection](player-mediacollection.md)        | Retrieves the [MediaCollection](mediacollection-object.md) object.                                                                          |
| [network](player-network.md)                        | Retrieves the [Network](network-object.md) object.                                                                                          |
| [openState](player-openstate.md)                    | Retrieves a value indicating the state of the content source.                                                                                |
| [playerApplication](player-playerapplication.md) \* | Retrieves the [PlayerApplication](playerapplication-object.md) object when a remoted Windows Media Player control is running.               |
| [playlistCollection](player-playlistcollection.md)  | Retrieves the [PlaylistCollection](playlistcollection-object.md) object.                                                                    |
| [playState](player-playstate.md)                    | Retrieves a value indicating the state of the Windows Media Player operation.                                                                |
| [settings](player-settings.md)                      | Retrieves the [Settings](settings-object.md) object.                                                                                        |
| [status](player-status.md)                          | Retrieves a value indicating the current status of Windows Media Player.                                                                     |
| [stretchToFit](player-stretchtofit.md) \*           | Specifies or retrieves a value indicating whether video will stretch to fit size of the Windows Media Player control video display.          |
| [uiMode](player-uimode.md) \*                       | Specifies or retrieves a value indicating which controls are shown in the user interface when Windows Media Player is embedded in a webpage. |
| [URL](player-url.md)                                | Specifies or retrieves the name of the clip to play.                                                                                         |
| [versionInfo](player-versioninfo.md)                | Retrieves a String value specifying the version of the Windows Media Player.                                                                 |
| [windowlessVideo](player-windowlessvideo.md) \*     | Specifies or retrieves a value indicating whether the Windows Media Player control renders video in windowless mode.                         |



 

\* Not accessible to skins.

The Player object supports the following methods.



| Method                                | Description                                               |
|---------------------------------------|-----------------------------------------------------------|
| [close](player-close.md)             | Releases Windows Media Player resources.                  |
| [launchURL](player-launchurl.md)     | Sends a URL to the user's default browser to be rendered. |
| [newMedia](player-newmedia.md)       | Creates a new [Media](media-object.md) object.           |
| [newPlaylist](player-newplaylist.md) | Creates a new [Playlist](playlist-object.md) object.     |
| [openPlayer](player-openplayer.md)   | Opens Windows Media Player using the specified URL.       |



 

The Player object supports the following events. Events marked with an asterisk (\*) are not accessible to skins. For information about handling mouse and keyboard events in skins, see [External Events](external-events.md).



| Event                                                                                            | Description                                                                      |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [AudioLanguageChange](player-player-audiolanguagechange.md)                                     | Occurs when the current audio language changes.                                  |
| [Buffering](player-player-buffering.md)                                                         | Occurs when the Windows Media Player control begins or ends buffering.           |
| [CdromMediaChange](player-player-cdrommediachange.md)                                           | Occurs when a CD or DVD is inserted into or ejected from a CD or DVD drive.      |
| [Click](player-player-click.md) \*                                                              | Occurs when the user clicks a mouse button.                                      |
| [CurrentItemChange](player-player-currentitemchange.md)                                         | Occurs when *Controls*.**currentItem** changes.                                  |
| [CurrentMediaItemAvailable](player-player-currentmediaitemavailable.md)                         | Occurs when a graphic metadata item in the current media item becomes available. |
| [CurrentPlaylistChange](player-player-currentplaylistchange.md)                                 | Occurs when something changes within the current playlist.                       |
| [CurrentPlaylistItemAvailable](player-player-currentplaylistitemavailable.md)                   | Occurs when the current playlist item becomes available.                         |
| **Disconnect**                                                                                   | Reserved for future use.                                                         |
| [DomainChange](player-player-domainchange.md)                                                   | Occurs when the DVD domain changes.                                              |
| [DoubleClick](player-player-doubleclick.md) \*                                                  | Occurs when the user double-clicks a mouse button.                               |
| **DurationUnitChange**                                                                           | Reserved for future use.                                                         |
| **EndOfStream**                                                                                  | Reserved for future use.                                                         |
| [Error](player-player-error.md)                                                                 | Occurs when the Windows Media Player control has an error condition.             |
| [KeyDown](player-player-keydown.md) \*                                                          | Occurs when a key is pressed.                                                    |
| [KeyPress](player-player-keypress.md) \*                                                        | Occurs when a key is pressed and then released.                                  |
| [KeyUp](player-player-keyup.md) \*                                                              | Occurs when a key is released.                                                   |
| [MarkerHit](player-player-markerhit.md)                                                         | Occurs when a marker is reached.                                                 |
| [MediaChange](player-player-mediachange.md)                                                     | Occurs when a media item changes.                                                |
| [MediaCollectionAttributeStringAdded](player-player-mediacollectionattributestringadded.md)     | Occurs when an attribute value is added to the library.                          |
| [MediaCollectionAttributeStringChanged](player-player-mediacollectionattributestringchanged.md) | Occurs when an attribute value in the library is changed.                        |
| [MediaCollectionAttributeStringRemoved](player-player-mediacollectionattributestringremoved.md) | Occurs when an attribute value is removed from the library.                      |
| [MediaCollectionChange](player-player-mediacollectionchange.md)                                 | Occurs when the media collection changes.                                        |
| [MediaCollectionMediaAdded](player-player-mediacollectionmediaadded.md)                         | Occurs when a media item is added to the local library.                          |
| [MediaCollectionMediaRemoved](player-player-mediacollectionmediaremoved.md)                     | Occurs when a media item is removed from the local library.                      |
| [MediaError](player-player-mediaerror.md)                                                       | Occurs when the **Media** object has an error condition.                         |
| [ModeChange](player-player-modechange.md)                                                       | Occurs when a mode of Windows Media Player is changed.                           |
| [MouseDown](player-player-mousedown.md) \*                                                      | Occurs when a mouse button is pressed.                                           |
| [MouseMove](player-player-mousemove.md) \*                                                      | Occurs when the mouse pointer is moved.                                          |
| [MouseUp](player-player-mouseup.md) \*                                                          | Occurs when a mouse button is released.                                          |
| **NewStream**                                                                                    | Reserved for future use.                                                         |
| [OpenPlaylistSwitch](player-player-openplaylistswitch.md)                                       | Occurs when a title on a DVD begins playing.                                     |
| [OpenStateChange](player-player-openstatechange.md)                                             | Occurs when the Windows Media Player control changes state.                      |
| [PlaylistChange](player-player-playlistchange.md)                                               | Occurs when a playlist changes.                                                  |
| [PlaylistCollectionChange](player-player-playlistcollectionchange.md)                           | Occurs when something changes in the playlist collection.                        |
| [PlaylistCollectionPlaylistAdded](player-player-playlistcollectionplaylistadded.md)             | Occurs when a playlist is added to the playlist collection.                      |
| [PlaylistCollectionPlaylistRemoved](player-player-playlistcollectionplaylistremoved.md)         | Occurs when a playlist is removed from the playlist collection.                  |
| **PlaylistCollectionPlaylistSetAsDeleted**                                                       | Reserved for future use.                                                         |
| [PlayStateChange](player-player-playstatechange.md)                                             | Occurs when the play state of the Windows Media Player control changes.          |
| [PositionChange](player-player-positionchange.md)                                               | Occurs when the current position of the media item has been changed.             |
| [ScriptCommand](player-player-scriptcommand.md)                                                 | Occurs when a synchronized command or URL is received.                           |
| [StatusChange](player-player-statuschange.md)                                                   | Occurs when the **status** property changes value.                               |
| [StringCollectionChange](player-player-stringcollectionchange.md)                               | Occurs when a string collection changes.                                         |
| **Warning**                                                                                      | Reserved for future use.                                                         |



 

\* Not accessible to skins. For information about handling mouse and keyboard events in skins, see [Ambient Event Handlers](ambient-event-handlers.md).

When embedded in a webpage, the **Player** object can be accessed by using the ID value specified in the OBJECT tag. Within a skin definition file, it is accessed by using the **player** global attribute. For illustration purposes, **player** will be used as the object ID in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




