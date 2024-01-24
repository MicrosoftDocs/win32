---
title: AlbumIDAlbumArtist Attribute
description: The AlbumIDAlbumArtist attribute is a unique identifier for the album.
ms.assetid: beaa8d01-1722-4545-8705-6b3d130113b1
keywords:
- AlbumIDAlbumArtist Attribute Windows Media Player
topic_type:
- apiref
api_name:
- AlbumIDAlbumArtist
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AlbumIDAlbumArtist Attribute

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **AlbumIDAlbumArtist** attribute is a unique identifier for the album.

## Applies To

-   [Audio Items](audio-item-attributes.md)

## Remarks

This attribute is stored only in the library.

The unique identifier is a combination of the album title and the album artist name. In this attribute, the album artist name comes first. When you use the [MediaCollection.getAttributeStringCollection](mediacollection-getattributestringcollection.md) method to get a **StringCollection** object using this attribute, the values are sorted by album artist name.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**AlbumID Attribute**](albumid-attribute.md)
</dt> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





