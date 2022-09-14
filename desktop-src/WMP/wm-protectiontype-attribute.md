---
title: WM/ProtectionType Attribute
description: The WM/ProtectionType attribute is the type of protection used on the content.
ms.assetid: aab36b57-5b4e-4a3f-80cf-872ec8369c49
keywords:
- WM/ProtectionType Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/ProtectionType
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/ProtectionType Attribute

The **WM/ProtectionType** attribute is the type of protection used on the content.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Video Items](video-item-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

**ProtectionType** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMProtectionType.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





