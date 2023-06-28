---
title: MediaCollection Object
description: The MediaCollection object provides a way to organize a large collection of media items. It can be queried to generate playlists automatically.
ms.assetid: afcb2c51-3ecb-4529-8f3e-56aa6d0ec2b4
keywords:
- MediaCollection Object Windows Media Player
topic_type:
- apiref
api_name:
- MediaCollection Object
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# MediaCollection Object

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **MediaCollection** object provides a way to organize a large collection of media items. It can be queried to generate playlists automatically.

The **MediaCollection** object supports the following methods.



| Method                                                                           | Description                                                                                                                                                    |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [add](mediacollection-add.md)                                                   | Adds a new media item or playlist to the library.                                                                                                              |
| [createQuery](mediacollection-createquery.md)                                   | Creates a new [Query](query-object.md) object.                                                                                                                |
| [getAll](mediacollection-getall.md)                                             | Retrieves a [Playlist](playlist-object.md) object containing all media items in the library.                                                                  |
| [getAttributeStringCollection](mediacollection-getattributestringcollection.md) | Retrieves a [StringCollection](stringcollection-object.md) object representing the set of all values for a specified attribute within a specified media type. |
| [getByAlbum](mediacollection-getbyalbum.md)                                     | Retrieves a [Playlist](playlist-object.md) object containing media items from the specified album.                                                            |
| [getByAttribute](mediacollection-getbyattribute.md)                             | Retrieves a [Playlist](playlist-object.md) object containing media items with the specified attribute having the specified value.                             |
| [getByAttributeAndMediaType](mediacollection-getbyattributeandmediatype.md)     | Retrieves a [Playlist](playlist-object.md) object containing [Media](media-object.md) objects having the specified attribute and media type.                 |
| [getByAuthor](mediacollection-getbyauthor.md)                                   | Retrieves a [Playlist](playlist-object.md) object containing media items by the specified author.                                                             |
| [getByGenre](mediacollection-getbygenre.md)                                     | Retrieves a [Playlist](playlist-object.md) object containing media items with the specified genre.                                                            |
| [getByName](mediacollection-getbyname.md)                                       | Retrieves a [Playlist](playlist-object.md) object containing media items with the specified name.                                                             |
| [getMediaAtom](mediacollection-getmediaatom.md)                                 | Retrieves the index at which a specified property resides within the set of available properties.                                                              |
| [getPlaylistByQuery](mediacollection-getplaylistbyquery.md)                     | Retrieves a [Playlist](playlist-object.md) object containing [Media](media-object.md) objects that match the query conditions.                               |
| [getStringCollectionByQuery](mediacollection-getstringcollectionbyquery.md)     | Retrieves a [StringCollection](stringcollection-object.md) object containing strings that match the query conditions.                                         |
| [isDeleted](mediacollection-isdeleted.md)                                       | Retrieves a value indicating whether the specified media item is in the deleted items folder.                                                                  |
| [remove](mediacollection-remove.md)                                             | Removes an item from the media collection.                                                                                                                     |
| [setDeleted](mediacollection-setdeleted.md)                                     | Moves the specified media item to the deleted items folder.                                                                                                    |



 

The **MediaCollection** object is accessed through the following property.



| Object                      | Property                                      |
|-----------------------------|-----------------------------------------------|
| [Player](player-object.md) | [mediaCollection](player-mediacollection.md) |



 

## See also

<dl> <dt>

[**Object Model Reference for Scripting**](object-model-reference-for-scripting.md)
</dt> </dl>

 

 




