---
title: WM/ContentDistributorType Attribute
description: The WM/ContentDistributorType attribute is the type of the distributor of the item.
ms.assetid: 3be711a2-51b0-4b61-8009-f97394207b1c
keywords:
- WM/ContentDistributorType Attribute Windows Media Player
topic_type:
- apiref
api_name:
- WM/ContentDistributorType
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# WM/ContentDistributorType Attribute

The **WM/ContentDistributorType** attribute is the type of the distributor of the item.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media File Attributes](commonly-used-windows-media-file-attributes.md)
-   [Playlists](playlist-attributes-ref.md)
-   [Video Items](video-item-attributes.md)

## Remarks

The value of this attribute will be set to either "List" or "Radio". This attribute is stored in both the library and the digital media file.

**ContentDistributorType** is an alias for this attribute.

The Windows Media Format SDK constant for this attribute is g\_wszWMContentDistributorType.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





