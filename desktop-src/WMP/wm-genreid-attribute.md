---
title: WM/GenreID Attribute
description: The WM/GenreID attribute is a genre identifier compliant with the TCON tag in ID3v2.
ms.assetid: 9b68f9be-1f02-4b14-b052-90657b8800e3
keywords:
- WM/GenreID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/GenreID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/GenreID Attribute

The **WM/GenreID** attribute is a genre identifier compliant with the TCON tag in ID3v2.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored only in the digital media file.

ID3 version 2 is a tagging convention that was originally designed for MP3. For more information, see the [ID3 organization's website](https://id3.org/).

The Windows Media Format SDK constant for this attribute is g\_wszGenreID.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series Windows Media Player 10 or later does not support this attribute<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





