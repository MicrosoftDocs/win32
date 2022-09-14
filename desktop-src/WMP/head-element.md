---
title: head Element
description: The head element contains metadata that applies to the entire playlist.
ms.assetid: 9554c84a-34af-4492-964a-4b262cd7c4a4
keywords:
- head Element Windows Media Player
topic_type:
- apiref
api_name:
- head Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# head Element

The **head** element contains metadata that applies to the entire playlist.

``` syntax
<head>
</head>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy | Elements                                                  |
|-----------|-----------------------------------------------------------|
| Parent    | [smil](smil-element.md)                                  |
| Child     | [title](title-element--wpl.md), [meta](meta-element.md) |



 

## Remarks

Typically the **head** element contains a **title** element and one or more **meta** elements that define global characteristics of the playlist.

## Examples


```
<head>
    <title>Party Playlist</title>
    <meta name = "Author" CONTENT = "Frank Lee"/>
    <meta name = "Category" CONTENT = "Party Music"/>
    <meta name = "Genre" CONTENT = "Pop"/>
    <meta name = "UserName1" CONTENT = "Frank001"/>
    <meta name = "UserRating1" CONTENT = "82"/>
</head>
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**meta Element**](meta-element.md)
</dt> <dt>

[**title Element (WPL)**](title-element--wpl.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





