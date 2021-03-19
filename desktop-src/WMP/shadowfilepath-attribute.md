---
title: ShadowFilePath Attribute
description: The ShadowFilePath attribute is the fully qualified path to a shadow file.
ms.assetid: dd00d53c-8a95-450c-a65b-1763e9112941
keywords:
- ShadowFilePath Attribute Windows Media Player
topic_type:
- apiref
api_name:
- ShadowFilePath
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ShadowFilePath Attribute

The **ShadowFilePath** attribute is the fully qualified path to a shadow file.

## Applies To

-   [Audio Items](audio-item-attributes.md)

## Remarks

A *shadow file* is created as part of a file format conversion. It is the copy of a file that the Player uses when the user syncs content from the computer to a device that requires the content to be in the original file format. This attribute is set for the converted file to point to the location of the shadow file.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**About the Conversion Process**](about-the-conversion-process.md)
</dt> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





