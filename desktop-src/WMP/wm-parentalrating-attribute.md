---
title: WM/ParentalRating Attribute
description: The WM/ParentalRating attribute is the parental rating of the content.
ms.assetid: 9cbe5ae7-96b9-41f2-bdfd-8043f4cbd82d
keywords:
- WM/ParentalRating Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/ParentalRating
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/ParentalRating Attribute

The **WM/ParentalRating** attribute is the parental rating of the content.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [DVDs](dvd-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

The Windows Media Format SDK constant for this attribute is g\_wszWMParentalRating.

**MPAARating** is an alias for this attribute.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





