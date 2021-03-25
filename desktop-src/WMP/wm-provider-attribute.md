---
title: WM/Provider Attribute
description: The WM/Provider attribute is the name of the provider of the attribute values.
ms.assetid: 358651d3-5bcd-4a03-a9aa-a33745d0323a
keywords:
- WM/Provider Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/Provider
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/Provider Attribute

The **WM/Provider** attribute is the name of the provider of the attribute values.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Radio Items](radio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**MetadataSource** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMProvider.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later (The photo item is supported only in Windows Media Player 10 or later)<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





