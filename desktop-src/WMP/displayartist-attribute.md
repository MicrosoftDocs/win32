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
ms.date: 05/31/2018
---

# DisplayArtist Attribute

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

 

 





