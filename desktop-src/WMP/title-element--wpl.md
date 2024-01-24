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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# title Element (WPL)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





