---
title: smil Element
description: The smil element is always the top level element in a Windows Media Playlist (WPL) file. It specifies that the file uses SMIL (Synchronized Multimedia Integration Language) syntax and grammar.
ms.assetid: bb14f1b8-53d0-47ff-9fd3-4620a1467985
keywords:
- smil Element Windows Media Player
topic_type:
- apiref
api_name:
- smil Element
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# smil Element

The **smil** element is always the top level element in a Windows Media Playlist (WPL) file. It specifies that the file uses SMIL (Synchronized Multimedia Integration Language) syntax and grammar.

``` syntax
<smil>
</smil>
```

## Attributes

This element has no attributes.

## Parent/Child Elements



| Hierarchy | Elements                                           |
|-----------|----------------------------------------------------|
| Parent    | None                                               |
| Child     | [head](head-element.md), [body](body-element.md) |



 

## Remarks

Every Windows Media Playlist must have the **smil** element at its root.

## Examples


```
<?wpl version = "1.0"?>
<smil>
    <head>
        <entity type="hellip"/>
    </head>

    <body>
        <entity type="hellip"/>
    </body>
</smil>
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later.<br/> |



## See also

<dl> <dt>

[**body Element**](body-element.md)
</dt> <dt>

[**head Element**](head-element.md)
</dt> <dt>

[**Windows Media Playlist Elements Reference**](windows-media-playlist-elements-reference.md)
</dt> </dl>

 

 





