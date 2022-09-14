---
title: MediaType Attribute
description: The MediaType attribute is the type of content in the item.
ms.assetid: 0d8a6937-32d8-4a4a-87e5-0002f077fefe
keywords:
- MediaType Attribute Windows Media Player
topic_type:
- apiref
api_name:
- MediaType
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# MediaType Attribute

The **MediaType** attribute is the type of content in the item.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Photo Items](photo-item-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Radio Items](radio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored only in the library.

This attribute has one of the following values: "audio", "other", "photo", "playlist", "radio", or "video". Use this attribute with the *MediaCollection*.**getByAttribute** method to retrieve a playlist containing all of the items of a particular type.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> <dt>

[**MediaCollection.getByAttribute**](mediacollection-getbyattribute.md)
</dt> </dl>

 

 





