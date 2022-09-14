---
title: WM/AlbumArtist Attribute
description: The WM/AlbumArtist attribute is the name of the primary artist for the album.
ms.assetid: 9da02a85-d0cf-41e3-ad5b-08b908315993
keywords:
- WM/AlbumArtist Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/AlbumArtist
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/AlbumArtist Attribute

The **WM/AlbumArtist** attribute is the name of the primary artist for the album.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**AlbumArtist** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMAlbumArtist.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





