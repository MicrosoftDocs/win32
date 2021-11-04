---
title: seq Element
description: The seq element contains elements that define a static playlist or elements that define a smart playlist.
ms.assetid: 849f7b38-25f2-4708-a83c-e651812a1a72
keywords:
- seq Element Windows Media Player
topic_type:
- apiref
api_name:
- seq Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# seq Element

The **seq** element contains elements that define a static playlist or elements that define a smart playlist.

``` syntax
<seq>
</seq>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy | Elements                                                               |
|-----------|------------------------------------------------------------------------|
| Parent    | [body](body-element.md)                                               |
| Child     | [media](media-element.md), [smartPlaylist](smartplaylist-element.md) |



 

## Remarks

When a **seq** element only contains **media** elements that reference specific media items, the playlist is considered to be static. When a **seq** element contains a **smartPlaylist** element, it is considered to be a dynamic "smart" playlist.

## Examples


```
<seq>
    <media></media>
    <media></media>
</seq>

<seq>
    <smartPlaylist></smartPlaylist>
</seq>
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**body Element**](body-element.md)
</dt> <dt>

[**media Element**](media-element.md)
</dt> <dt>

[**smartPlaylist Element**](smartplaylist-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





