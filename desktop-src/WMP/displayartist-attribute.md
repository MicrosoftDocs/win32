---
title: DisplayArtist Attribute
description: The DisplayArtist attribute is the name of the artist that is displayed for an item.
ms.assetid: 8cf5a4e6-ce96-4fd4-b01a-6cd4264a5c09
keywords:
- DisplayArtist Attribute Windows Media Player
topic_type:
- apiref
api_name:
- DisplayArtist
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DisplayArtist Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **DisplayArtist** attribute is the name of the artist that is displayed for an item.

## Applies To

-   [Audio Items](audio-item-attributes.md)

## Remarks

Generally, **DisplayArtist** will have the same value as the **WM/AlbumArtist** attribute when that attribute is set. Otherwise, the value will be the name of the artist that is associated with the first track on the album.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> <dt>

[**WM/AlbumArtist Attribute**](wm-albumartist-attribute.md)
</dt> </dl>

 

 





