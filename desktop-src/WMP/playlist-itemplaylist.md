---
title: PLAYLIST.itemPlaylist
description: The itemPlaylist attribute retrieves the playlist for the media item that is displayed at the given index in the PLAYLIST element.
ms.assetid: 094bcb5d-8a59-4531-96b8-0e993ca00be6
keywords:
- PLAYLIST.itemPlaylist Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.itemPlaylist
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PLAYLIST.itemPlaylist

The **itemPlaylist** attribute retrieves the playlist for the media item that is displayed at the given index in the **PLAYLIST** element.

``` syntax
        elementID.itemPlaylist(index)
```

## Possible Values

This attribute is a read-only **Playlist** object.

## Parameters

<dl> <dt>

<span id="index"></span><span id="INDEX"></span>*index*
</dt> <dd>

**Number**(**long**) containing the index of a playlist item.

</dd> </dl>

## Remarks

The **itemPlaylist** property will return the playlist object that is expanded in the **PLAYLIST** element. For example, if there are two nested playlists that are not expanded in the **PLAYLIST** element, and that contain three media clips each, **itemPlaylist**(1) will return the parent playlist that contains the two nested playlists. If the second playlist is expanded, **itemPlaylist**(1) will return the second playlist. If both playlists are expanded, **itemPlaylist**(1) will return the first playlist.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**Playlist Object**](playlist-object.md)
</dt> </dl>

 

 





