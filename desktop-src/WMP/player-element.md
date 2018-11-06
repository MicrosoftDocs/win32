---
title: PLAYER Element
description: PLAYER Element
ms.assetid: 009090b3-0055-4700-9078-0749da239674
keywords:
- Windows Media Player skins,PLAYER element
- skins,PLAYER element
- PLAYER element
- reference for skins,PLAYER element
- elements,PLAYER
ms.topic: article
ms.date: 05/31/2018
---

# PLAYER Element

The **PLAYER** element lets you define event handlers and specify the **URL** property of the **Player** object at design time within a skin definition file. Within script code, the **Player** object is accessed through the **player** global attribute rather than through a name specified by an **id** attribute, which is not supported by the **PLAYER** element.

The **PLAYER** element supports the following attribute.



| Attribute             | Description                                          |
|-----------------------|------------------------------------------------------|
| [URL](player-url.md) | Specifies or retrieves the name of the file to play. |



 

The **PLAYER** element can implement event handlers for the following events fired from the **Player** object.



| Event                                                                                            | Description                                                                      |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [AudioLanguageChange](player-player-audiolanguagechange.md)                                     | Occurs when the current audio language changes.                                  |
| [Buffering](player-player-buffering.md)                                                         | Occurs when Windows Media Player begins or ends buffering.                       |
| [CdromMediaChange](player-player-cdrommediachange.md)                                           | Occurs when the CD media changes.                                                |
| [CurrentItemChange](player-player-currentitemchange.md)                                         | Occurs when the current item changes.                                            |
| [CurrentMediaItemAvailable](player-player-currentmediaitemavailable.md)                         | Occurs when the current media item becomes available.                            |
| [CurrentPlaylistChange](player-player-currentplaylistchange.md)                                 | Occurs when the current playlist changes.                                        |
| [CurrentPlaylistItemAvailable](player-player-currentplaylistitemavailable.md)                   | Occurs when the current playlist item becomes available.                         |
| [DomainChange](player-player-domainchange.md)                                                   | Occurs when the DVD domain changes.                                              |
| [Error](player-player-error.md)                                                                 | Occurs when the Windows Media Player control has an error condition.             |
| [MarkerHit](player-player-markerhit.md)                                                         | Occurs when Windows Media Player encounters a marker in the clip.                |
| [MediaChange](player-player-mediachange.md)                                                     | Occurs when a media item changes.                                                |
| [MediaCollectionAttributeStringAdded](player-player-mediacollectionattributestringadded.md)     | Occurs when an attribute value is added to the library.                          |
| [MediaCollectionAttributeStringChanged](player-player-mediacollectionattributestringchanged.md) | Occurs when an attribute value in the library is changed.                        |
| [MediaCollectionAttributeStringRemoved](player-player-mediacollectionattributestringremoved.md) | Occurs when an attribute value is removed from the library.                      |
| [MediaCollectionChange](player-player-mediacollectionchange.md)                                 | Occurs when the **MediaCollection** object changes.                              |
| [MediaError](player-player-mediaerror.md)                                                       | Occurs when the **Media** object has an error condition.                         |
| [ModeChange](player-player-modechange.md)                                                       | Occurs when switching between shuffle and normal mode.                           |
| [OpenPlaylistSwitch](player-player-openplaylistswitch.md)                                       | Occurs when a title on a DVD begins playing.                                     |
| [OpenStateChange](player-player-openstatechange.md)                                             | Occurs when *player*.**openState** changes.                                      |
| [PlaylistChange](player-player-playlistchange.md)                                               | Occurs when a playlist changes.                                                  |
| [PlaylistCollectionChange](player-player-playlistcollectionchange.md)                           | Occurs when something changes in the playlist collection.                        |
| [PlaylistCollectionPlaylistAdded](player-player-playlistcollectionplaylistadded.md)             | Occurs when a playlist is added to the playlist collection.                      |
| [PlaylistCollectionPlaylistRemoved](player-player-playlistcollectionplaylistremoved.md)         | Occurs when a playlist is removed from the playlist collection.                  |
| [PlayStateChange](player-player-playstatechange.md)                                             | Occurs when *player*.**playState** changes.                                      |
| [PositionChange](player-player-positionchange.md)                                               | Occurs when *player*.*controls*.**currentPosition** changes.                     |
| [ScriptCommand](player-player-scriptcommand.md)                                                 | Occurs when Windows Media Player encounters a script command embedded in a file. |
| [StatusChange](player-player-statuschange.md)                                                   | Occurs when the **status** property changes value.                               |



 

## Related topics

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




