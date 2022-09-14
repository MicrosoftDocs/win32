---
title: WM/Year Attribute
description: The WM/Year attribute is the year the content was published.
ms.assetid: b64e37f1-6f12-43a6-8a66-7d61b470853c
keywords:
- WM/Year Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/Year
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/Year Attribute

The **WM/Year** attribute is the year the content was published.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored only in the digital media file.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

This attribute should not be used as part of a query condition. It is derived from another attribute and cannot be directly queried against in a media collection.

The Windows Media Format SDK constant for this attribute is g\_wszWMYear.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series Windows Media Player 10 or later does not support this attribute<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





