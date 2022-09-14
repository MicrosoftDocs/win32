---
title: AlbumID Attribute
description: The AlbumID attribute is a unique identifier for the album.
ms.assetid: 0412d91a-11a7-434c-8717-a71d85655679
keywords:
- AlbumID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- AlbumID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AlbumID Attribute

The **AlbumID** attribute is a unique identifier for the album.

## Applies To

-   [Audio Items](audio-item-attributes.md)

## Remarks

This attribute is stored only in the library.

The unique identifier is a combination of the album title and the album artist name. In this attribute, the album title comes first. When you use the [MediaCollection.getAttributeStringCollection](mediacollection-getattributestringcollection.md) method to get a **StringCollection** object using this attribute, the values are sorted by album title.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**AlbumIDAlbumArtist Attribute**](albumidalbumartist-attribute.md)
</dt> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





