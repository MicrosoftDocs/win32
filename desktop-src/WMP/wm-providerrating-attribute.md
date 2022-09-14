---
title: WM/ProviderRating Attribute
description: The WM/ProviderRating attribute is the rating of the item assigned by the provider of the attribute values.
ms.assetid: a1a76560-a8d9-486a-badc-56d7bf488c10
keywords:
- WM/ProviderRating Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/ProviderRating
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/ProviderRating Attribute

The **WM/ProviderRating** attribute is the rating of the item assigned by the provider of the attribute values.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [DVDs](dvd-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**Rating** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMProviderRating.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





