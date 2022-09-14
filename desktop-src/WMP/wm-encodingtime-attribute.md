---
title: WM/EncodingTime Attribute
description: The WM/EncodingTime attribute is the date and time at which the content was encoded.
ms.assetid: 264f379a-0bec-4143-bc23-ab45fb725af6
keywords:
- WM/EncodingTime Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/EncodingTime
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/EncodingTime Attribute

The **WM/EncodingTime** attribute is the date and time at which the content was encoded.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

**CreationDate** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMEncodingTime.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





