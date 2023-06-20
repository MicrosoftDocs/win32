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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# smil Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





