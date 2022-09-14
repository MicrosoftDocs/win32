---
title: PlaylistCollection.importPlaylist method
description: The importPlaylist method adds a static playlist to the library. | PlaylistCollection.importPlaylist method
ms.assetid: '0611ba42-fd8f-4fb9-9fbb-809a82775c2a'
keywords:
- importPlaylist method Windows Media Player
- importPlaylist method Windows Media Player , PlaylistCollection class
- PlaylistCollection class Windows Media Player , importPlaylist method
topic_type:
- apiref
api_name:
- PlaylistCollection.importPlaylist
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# PlaylistCollection.importPlaylist method

The **importPlaylist** method adds a static playlist to the library.

## Syntax


```JScript
retVal = PlaylistCollection.importPlaylist(
  playlist
)
```



## Parameters

<dl> <dt>

*playlist* \[in\]
</dt> <dd>

**Playlist** object to be added.

</dd> </dl>

## Return value

This method returns the **Playlist** object that was added.

## Remarks

Playlists that do not contain any media items cannot be added to the library by using this method. To create an empty playlist in the library, use the **newPlaylist** method. You can then fill the resulting playlist with media items by using *Playlist*.**appendItem** or *Playlist*.**insertItem**.

If you pass this method an auto playlist, the query is executed once and the result is added to the library as a static playlist. To add an auto playlist to the library and preserve its automatic behavior, use *MediaCollection*.**add**. For more information, see [Static and Auto Playlists](static-and-auto-playlists.md).

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Managing Playlists**](managing-playlists.md)
</dt> <dt>

[**MediaCollection Object**](mediacollection-object.md)
</dt> <dt>

[**MediaCollection.add**](mediacollection-add.md)
</dt> <dt>

[**Playlist.appendItem**](playlist-appenditem.md)
</dt> <dt>

[**Playlist.insertItem**](playlist-insertitem.md)
</dt> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> <dt>

[**PlaylistCollection.newPlaylist**](playlistcollection-newplaylist.md)
</dt> <dt>

[**PlaylistCollection.remove**](playlistcollection-remove.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





