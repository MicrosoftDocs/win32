---
title: Player.openState
description: The openState property retrieves a value indicating the state of the content source.
ms.assetid: d38eadad-d0f0-40a9-92c6-1c745a0d4f1b
keywords:
- Player.openState Windows Media Player
topic_type:
- apiref
api_name:
- Player.openState
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Player.openState

The **openState** property retrieves a value indicating the state of the content source.

## Syntax

*player* .**openState**

## Possible Values

This property is a read only **Number** (**long**). The C-style enumeration constant can be derived by prefixing the state value with "wmpos". For example, the constant for the PlaylistOpening state is **wmposPlaylistOpening**.



| Value | State                   | Description                                                                                                                                            |
|-------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | Undefined               | Windows Media Player is in an undefined state.                                                                                                         |
| 1     | PlaylistChanging        | New playlist is about to be loaded.                                                                                                                    |
| 2     | PlaylistLocating        | Windows Media Player is attempting to locate the playlist. The playlist can be local (library or metafile with an .asx file name extension) or remote. |
| 3     | PlaylistConnecting      | Connecting to the playlist.                                                                                                                            |
| 4     | PlaylistLoading         | Playlist has been found and is now being retrieved.                                                                                                    |
| 5     | PlaylistOpening         | Playlist has been retrieved and is now being parsed and loaded.                                                                                        |
| 6     | PlaylistOpenNoMedia     | Playlist is open.                                                                                                                                      |
| 7     | PlaylistChanged         | A new playlist has been assigned to **currentPlaylist**.                                                                                               |
| 8     | MediaChanging           | A new media item is about to be loaded.                                                                                                                |
| 9     | MediaLocating           | Windows Media Player is locating the media item. The file can be local or remote.                                                                      |
| 10    | MediaConnecting         | Connecting to the server that holds the media item.                                                                                                    |
| 11    | MediaLoading            | Media item has been located and is now being retrieved.                                                                                                |
| 12    | MediaOpening            | Media item has been retrieved and is now being opened.                                                                                                 |
| 13    | MediaOpen               | Media item is now open.                                                                                                                                |
| 14    | BeginCodecAcquisition   | Starting codec acquisition.                                                                                                                            |
| 15    | EndCodecAcquisition     | Codec acquisition is complete.                                                                                                                         |
| 16    | BeginLicenseAcquisition | Acquiring a license to play DRM protected content.                                                                                                     |
| 17    | EndLicenseAcquisition   | License to play DRM protected content has been acquired.                                                                                               |
| 18    | BeginIndividualization  | Begin DRM Individualization.                                                                                                                           |
| 19    | EndIndividualization    | DRM individualization has been completed.                                                                                                              |
| 20    | MediaWaiting            | Waiting for media item.                                                                                                                                |
| 21    | OpeningUnknownURL       | Opening a URL with an unknown type.                                                                                                                    |



 

## Remarks

Windows Media Player states are not guaranteed to occur in any particular order. Furthermore, not every state necessarily occurs during a sequence of events. You should not write code that relies upon state order.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.OpenStateChange Event**](player-player-openstatechange.md)
</dt> </dl>

 

 





