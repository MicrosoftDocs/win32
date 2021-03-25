---
title: PlaylistCollection.newPlaylist method
description: The newPlaylist method creates a new playlist in the library.
ms.assetid: '428b5779-4dc0-466b-9834-6b2c43324013'
keywords:
- newPlaylist method Windows Media Player
- newPlaylist method Windows Media Player , PlaylistCollection class
- PlaylistCollection class Windows Media Player , newPlaylist method
topic_type:
- apiref
api_name:
- PlaylistCollection.newPlaylist
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# PlaylistCollection.newPlaylist method

The **newPlaylist** method creates a new playlist in the library.

## Syntax


```JScript
retVal = PlaylistCollection.newPlaylist(
  name
)
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

**String** containing the name of the playlist to be created.

</dd> </dl>

## Return value

This method returns a **Playlist** object.

## Remarks

This method creates an empty playlist in the library. To fill the playlist with media items, use *Playlist*.**appendItem** or *Playlist*.**insertItem**.

Multiple playlists having the same name are permitted in the library. To avoid creating a duplicate playlist name with this method, use **getByName** and *PlaylistArray*.**count** to determine whether a playlist with a particular name already exists.

Leading and trailing spaces are not permitted in playlist names, and are automatically removed from the value specified for the *name* parameter.

To use this method, full access to the library is required. For more information, see [Library Access](library-access.md).

## Examples

The following JScript example creates a new empty playlist called "ThreeList". The **Player** object was created with ID="Player".


```JScript
//Add a new empty playlist, named ThreeList, to the playlist collection.
var NewList = Player.playlistCollection.newPlaylist("ThreeList");

```



## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**MediaCollection.add**](mediacollection-add.md)
</dt> <dt>

[**Playlist.appendItem**](playlist-appenditem.md)
</dt> <dt>

[**Playlist.insertItem**](playlist-insertitem.md)
</dt> <dt>

[**PlaylistArray.count**](playlistarray-count.md)
</dt> <dt>

[**PlaylistCollection Object**](playlistcollection-object.md)
</dt> <dt>

[**PlaylistCollection.getByName**](playlistcollection-getbyname.md)
</dt> <dt>

[**PlaylistCollection.importPlaylist**](playlistcollection-importplaylist.md)
</dt> <dt>

[**PlaylistCollection.remove**](playlistcollection-remove.md)
</dt> <dt>

[**Settings.mediaAccessRights**](settings-mediaaccessrights.md)
</dt> <dt>

[**Settings.requestMediaAccessRights**](settings-requestmediaaccessrights.md)
</dt> </dl>

 

 





