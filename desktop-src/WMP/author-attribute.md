---
title: Author Attribute
description: The Author attribute is the name of a media artist or actor associated with the content.
ms.assetid: 6621a955-dd6b-4725-9690-0cc96e73d94f
keywords:
- Author Attribute Windows Media Player
topic_type:
- apiref
api_name:
- Author
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Author Attribute

The **Author** attribute is the name of a media artist or actor associated with the content.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media Files](commonly-used-windows-media-file-attributes.md)
-   [DVDs](dvd-attributes.md)
-   [Media.getItemInfoByType](media-getiteminfobytype.md)
-   [Photo Items](photo-item-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Radio Items](radio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the media file.

This attribute may have multiple values. To retrieve all of the values for a multi-valued attribute, you must use the *Media*.**getItemInfoByType** method, not the *Media*.**getItemInfo** method.

The Windows Media Format SDK constant for this attribute is g\_wszWMAuthor.

**Actor** and **Artist** are aliases for this attribute.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





