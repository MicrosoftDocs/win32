---
title: PlaylistCollection Object
description: The PlaylistCollection object provides a way to organize your playlists.
ms.assetid: 9ea61954-d185-4a77-9016-4d58340a96fc
keywords:
- PlaylistCollection Object Windows Media Player
topic_type:
- apiref
api_name:
- PlaylistCollection Object
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PlaylistCollection Object

The **PlaylistCollection** object provides a way to organize your playlists.

The **PlaylistCollection** object supports the following methods.



| Method                                                  | Description                                                                                                              |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [getAll](playlistcollection-getall.md)                 | Retrieves a [PlaylistArray](playlistarray-object.md) object containing all the playlists in the library.                |
| [getByName](playlistcollection-getbyname.md)           | Retrieves a [PlaylistArray](playlistarray-object.md) object containing playlists with the specified name, if any exist. |
| [importPlaylist](playlistcollection-importplaylist.md) | Adds a static playlist to the library.                                                                                   |
| [isDeleted](playlistcollection-isdeleted.md)           | Retrieves a value indicating whether the specified playlist is in the deleted items folder.                              |
| [newPlaylist](playlistcollection-newplaylist.md)       | Creates a new playlist in the library.                                                                                   |
| [remove](playlistcollection-remove.md)                 | Removes a playlist from the library.                                                                                     |
| [setDeleted](playlistcollection-setdeleted.md)         | Moves a playlist to the deleted items folder.                                                                            |



 

The **PlaylistCollection** object is accessed through the following property.



| Object                      | Property                                            |
|-----------------------------|-----------------------------------------------------|
| [Player](player-object.md) | [playlistCollection](player-playlistcollection.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




