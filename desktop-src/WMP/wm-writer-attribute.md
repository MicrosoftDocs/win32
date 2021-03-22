---
title: WM/Writer Attribute
description: The WM/Writer attribute is the name of the writer who wrote the words of the content.
ms.assetid: e2035cf7-29f4-4642-9388-4cd7cb08149e
keywords:
- WM/Writer Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/Writer
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/Writer Attribute

The **WM/Writer** attribute is the name of the writer who wrote the words of the content.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

This attribute may have multiple values. To retrieve all of the values for a multi-valued attribute, you must use the **Media.getItemInfoByType** method, not the **Media.getItemInfo** method.

**Writer** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMWriter.

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

 

 





