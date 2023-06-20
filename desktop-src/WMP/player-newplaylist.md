---
title: Player.newPlaylist method
description: The newPlaylist method creates a new Playlist object.
ms.assetid: 'a566006e-8647-4c51-ab77-762728f25a30'
keywords:
- newPlaylist method Windows Media Player
- newPlaylist method Windows Media Player , Player class
- Player class Windows Media Player , newPlaylist method
topic_type:
- apiref
api_name:
- Player.newPlaylist
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Player.newPlaylist method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **newPlaylist** method creates a new **Playlist** object.

## Syntax


```JScript
retVal = Player.newPlaylist(
  name,
  URL
)
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the name of the new playlist.

</dd> <dt>

*URL* \[in\]
</dt> <dd>

**String** containing the URL of the Windows Media metafile playlist to create the **Playlist** object with.

</dd> </dl>

## Return value

This method returns a **Playlist** object.

## Remarks

If the *URL* parameter is set to null or "" (empty string), an empty **Playlist** object will be created. If the *name* parameter is set to "", the name in the metafile is used.

The new playlist created with this method is not added to the library. To add a new playlist to the library, use *PlaylistCollection*.**importPlaylist** or *PlaylistCollection*.**newPlaylist**. Any leading or trailing spaces in the playlist name are automatically removed when it is added to the library.

Because the library allows multiple playlists with the same name, you may want to check for the presence of a playlist with a given name before adding a new one.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/>                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Player Object**](player-object.md)
</dt> <dt>

[**PlaylistCollection.importPlaylist**](playlistcollection-importplaylist.md)
</dt> <dt>

[**PlaylistCollection.newPlaylist**](playlistcollection-newplaylist.md)
</dt> <dt>

[**Windows Media Metafiles**](windows-media-metafiles.md)
</dt> </dl>

 

 





