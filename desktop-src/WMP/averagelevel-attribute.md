---
title: AverageLevel Attribute
description: The AverageLevel attribute is a 16-bit amplitude value indicating the average volume level.
ms.assetid: 04ff19f1-a9a5-4e47-86a6-50c6f08b0d7d
keywords:
- AverageLevel Attribute Windows Media Player
topic_type:
- apiref
api_name:
- AverageLevel
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AverageLevel Attribute

The **AverageLevel** attribute is a 16-bit amplitude value indicating the average volume level.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Commonly Used Windows Media Files](commonly-used-windows-media-file-attributes.md)

## Remarks

This attribute is stored in both the library and the digital media file.

Windows Media Player sets this value in either of the following instances:

-   After it has ripped a file.
-   After it has played a file (when the Auto Volume Leveling enhancement is enabled).

The Windows Media Format SDK constant for this attribute is g\_wszAverageLevel.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





