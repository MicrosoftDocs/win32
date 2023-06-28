---
title: Playlist Object
description: The Playlist object provides a way to organize media items in a list for easy manipulation by using the following properties and methods.
ms.assetid: c2d2f265-b207-4b82-bb76-aee467f00659
keywords:
- Playlist Object Windows Media Player
topic_type:
- apiref
api_name:
- Playlist Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# Playlist Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **Playlist** object provides a way to organize media items in a list for easy manipulation by using the following properties and methods.

The **Playlist** object supports the following properties.



| Property                                      | Description                                                      |
|-----------------------------------------------|------------------------------------------------------------------|
| [attributeCount](playlist-attributecount.md) | Retrieves the number of attributes associated with the playlist. |
| [attributeName](playlist-attributename.md)   | Retrieves the name of an attribute specified by an index.        |
| [count](playlist-count.md)                   | Retrieves the number of items in the playlist.                   |
| [name](playlist-name.md)                     | Specifies or retrieves the name of the playlist.                 |



 

The **Playlist** object supports the following methods.



| Method                                  | Description                                                                                            |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------|
| [appendItem](playlist-appenditem.md)   | Adds a media item to the end of the playlist.                                                          |
| **clear**                               | Reserved for future use.                                                                               |
| [getItemInfo](playlist-getiteminfo.md) | Retrieves the value of a playlist attribute.                                                           |
| [insertItem](playlist-insertitem.md)   | Inserts a media item into the playlist at the specified location.                                      |
| [isIdentical](playlist-isidentical.md) | Retrieves a value indicating whether the supplied **Playlist** object is identical to the current one. |
| [item](playlist-item.md)               | Retrieves the media item at the specified index.                                                       |
| [moveItem](playlist-moveitem.md)       | Changes the location of an item in the playlist.                                                       |
| [removeItem](playlist-removeitem.md)   | Removes the specified item from the playlist.                                                          |
| [setItemInfo](playlist-setiteminfo.md) | Specifies the value of a playlist attribute.                                                           |



 

The **Playlist** object is accessed through the following properties and methods.



| Object                                              | Property or method                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Cdrom](cdrom-object.md)                           | [playlist](cdrom-playlist.md)                                                                                                                                                                                                                                                     |
| [MediaCollection](mediacollection-object.md)       | [getAll](mediacollection-getall.md), [getByAlbum](mediacollection-getbyalbum.md), [getByAttribute](mediacollection-getbyattribute.md), [getByAuthor](mediacollection-getbyauthor.md), [getByGenre](mediacollection-getbygenre.md), [getByName](mediacollection-getbyname.md) |
| [Player](player-object.md)                         | [currentPlaylist](player-currentplaylist.md), [newPlaylist](player-newplaylist.md)                                                                                                                                                                                               |
| [PlaylistArray](playlistarray-object.md)           | [item](playlistarray-item.md)                                                                                                                                                                                                                                                     |
| [PlaylistCollection](playlistcollection-object.md) | [newPlaylist](playlistcollection-newplaylist.md)                                                                                                                                                                                                                                  |



 

Because it is the most common means of access, *player*.**currentPlaylist** is used for purposes of illustration in the reference syntax sections.

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




