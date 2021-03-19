---
title: Copyright Attribute (Msfeeds.h)
description: The Copyright attribute is the copyright message for the item.
ms.assetid: 617272cb-883f-46d6-b0a9-29ac32c63148
keywords:
- Copyright Attribute Windows Media Player
topic_type:
- apiref
api_name:
- Copyright
api_location:
- msfeeds.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Copyright Attribute

The **Copyright** attribute is the copyright message for the item.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media Files](commonly-used-windows-media-file-attributes.md)
-   [DVDs](dvd-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

The Windows Media Format SDK constant for this attribute is g\_wszWMCopyright.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/>                                    |
| Header<br/>  | <dl> <dt>Msfeeds.h</dt> </dl> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





