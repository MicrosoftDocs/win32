---
title: WM/Language Attribute
description: The WM/Language attribute is the language of the item.
ms.assetid: aebfb518-61ca-4b75-875a-ce2127a74b67
keywords:
- WM/Language Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/Language
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/Language Attribute

The **WM/Language** attribute is the language of the item.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Radio Items](radio-item-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

This attribute may have multiple values. To retrieve all of the values for a multi-valued attribute, you must use the **Media.getItemInfoByType** method, not the **Media.getItemInfo** method.

**Language** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMLanguage.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later (The radio item is supported only in Windows Media Player 9 Series)<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> <dt>

[**Media.getItemInfoByType**](media-getiteminfobytype.md)
</dt> </dl>

 

 





