---
title: WM/MCDI Attribute
description: The WM/MCDI attribute is the music CD identifier of the CD from which the file or track was copied.
ms.assetid: f0bec14d-416c-477f-98df-dece0bf85ea4
keywords:
- WM/MCDI Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/MCDI
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/MCDI Attribute

The **WM/MCDI** attribute is the music CD identifier of the CD from which the file or track was copied.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**TOC** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMMCDI.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





