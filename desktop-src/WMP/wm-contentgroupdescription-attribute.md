---
title: WM/ContentGroupDescription Attribute
description: The WM/ContentGroupDescription attribute is the description of the content group, which is a collection of media items such as a CD boxed set.
ms.assetid: b2615f78-2d45-45f0-89f7-f1e8e083be9b
keywords:
- WM/ContentGroupDescription Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/ContentGroupDescription
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/ContentGroupDescription Attribute

The **WM/ContentGroupDescription** attribute is the description of the content group, which is a collection of media items such as a CD boxed set.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

**ContentGroupDescription** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMContentGroupDistribution.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





