---
title: Player.currentPlaylist
description: The currentPlaylist property specifies or retrieves the current Playlist object.
ms.assetid: fabfb927-5f64-4fc4-8ee5-e2449082dfbc
keywords:
- Player.currentPlaylist Windows Media Player
topic_type:
- apiref
api_name:
- Player.currentPlaylist
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.currentPlaylist

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The currentPlaylist property specifies or retrieves the current **Playlist** object.

## Syntax

*player* .**currentPlaylist**

## Possible Values

This property is a read/write **Playlist** object.

## Remarks

If the *Settings*.**autoStart** property is true, playback begins automatically whenever you set **currentPlaylist**.

This property takes a Playlist object, which can be acquired in several ways, such as by calling *PlaylistArray*.**item** or *PlaylistCollection*.**newPlaylist**. To load a **Playlist** item using a file name, set the URL property or use *Player*.**newPlaylist**.

## Examples

The following JScript example retrieves the first playlist in the library. It then uses **currentPlaylist** to make the retrieved playlist the current playlist, and then to display the name of the current playlist. The **Player** object was created with ID = "Player".


```JScript
// Retrieve the first playlist from the library.
var firstPL = Player.playlistCollection.getAll().item(0);

// Make the retrieved playlist the current playlist.
Player.currentPlaylist = firstPL;

// Display the name of the current playlist.
document.write("Found first playlist. Name: " + Player.currentPlaylist.name);
```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**Player.newPlaylist**](player-newplaylist.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> <dt>

[**PlaylistArray.item**](playlistarray-item.md)
</dt> <dt>

[**PlaylistCollection.newPlaylist**](playlistcollection-newplaylist.md)
</dt> <dt>

[**Settings.autoStart**](settings-autostart.md)
</dt> </dl>

 

 





