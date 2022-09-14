---
title: WM/Composer Attribute
description: The WM/Composer attribute is the name of the composer of the music.
ms.assetid: 48459027-ed80-46a2-ad5c-ace602144150
keywords:
- WM/Composer Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/Composer
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/Composer Attribute

The **WM/Composer** attribute is the name of the composer of the music.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Playlists](cd-playlist-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

This attribute may have multiple values. To retrieve all of the values for a multi-valued attribute, you must use the **Media.getItemInfoByType** method, not the **Media.getItemInfo** method.

**Composer** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMComposer.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> <dt>

[**Media.getItemInfoByType**](media-getiteminfobytype.md)
</dt> </dl>

 

 





