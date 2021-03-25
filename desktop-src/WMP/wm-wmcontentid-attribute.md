---
title: WM/WMContentID Attribute
description: The WM/WMContentID attribute is a GUID identifying the content of the item.
ms.assetid: 1e741286-cdd8-4c2f-8fef-5d91d81d6387
keywords:
- WM/WMContentID Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/WMContentID
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/WMContentID Attribute

The **WM/WMContentID** attribute is a GUID identifying the content of the item.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [CD Tracks](cd-track-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library (or cache) and the digital media file.

**WMContentID** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMContentID.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





