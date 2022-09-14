---
title: title Element (WPL)
description: The title element specifies a title for the playlist.
ms.assetid: 8a214b96-d507-4dbf-b5f2-8fdfc4409fb0
keywords:
- title Element (WPL) Windows Media Player
topic_type:
- apiref
api_name:
- title Element (WPL)
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# title Element (WPL)

The **title** element specifies a title for the playlist.

``` syntax
<head>
    <title>Dance Songs That I Haven't Played Recently</title>
</head>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy | Elements                 |
|-----------|--------------------------|
| Parent    | [head](head-element.md) |
| Child     | None                     |



 

## Remarks

When choosing a title for a Windows Media Playlist (WPL), consider that the content of the playlist can be dynamic. A good approach is to base the title on the logic in the **argument** elements because this is what defines the content of the playlist. Examples of this are "My Favorite Rock Songs from 1966" or "Dance Songs That I Haven't Played Recently".

## Examples


```
<head>
    <title>Dance Songs That I Haven't Played Recently</title>
</head>
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**argument Element**](argument-element.md)
</dt> <dt>

[**head Element**](head-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





