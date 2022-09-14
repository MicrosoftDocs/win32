---
title: body Element
description: The body element contains the elements that define the contents of a playlist.
ms.assetid: 96d09635-c360-4a36-a56e-6cecbbd4ff30
keywords:
- body Element Windows Media Player
topic_type:
- apiref
api_name:
- body Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# body Element

The **body** element contains the elements that define the contents of a playlist.

``` syntax
<body>
</body>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy | Elements                 |
|-----------|--------------------------|
| Parent    | [smil](smil-element.md) |
| Child     | [seq](seq-element.md)   |



 

## Remarks

The contents of a playlist are organized within a **seq** element that is contained within the **body** element. Typically there is either one **seq** element that defines a static set of media items and contains **media** elements, or there is one that defines a dynamic set of media items and contains a **smartPlaylist** element.

## Examples


```XML
<body>
    <seq>
        <media></media>
        <media></media>
        <media></media>
    </seq>
</body>

<body>
    <seq>
        <smartPlaylist></smartPlaylist>
    </seq>
</body>
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**media Element**](media-element.md)
</dt> <dt>

[**seq Element**](seq-element.md)
</dt> <dt>

[**smartPlaylist Element**](smartplaylist-element.md)
</dt> <dt>

[**smil Element**](smil-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





