---
title: FileSize Attribute
description: The FileSize attribute is the size of the file in bytes.
ms.assetid: e845cc82-6975-4fd9-800f-a66f59a5fb39
keywords:
- FileSize Attribute Windows Media Player
topic_type:
- apiref
api_name:
- FileSize
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# FileSize Attribute

The **FileSize** attribute is the size of the file in bytes.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media Files](commonly-used-windows-media-file-attributes.md)
-   [Other Items](other-item-attributes.md)
-   [Photo Items](photo-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

**Size** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMFileSize.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later (The photo item is supported only in Windows Media Player 10 or later)<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





