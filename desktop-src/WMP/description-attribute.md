---
title: Description Attribute (WMP SDK)
description: The Description attribute is a description of the content.
ms.assetid: 8bf76bf5-2bba-4ceb-bc98-f8b8ab2c8b6f
keywords:
- Description Attribute Windows Media Player
topic_type:
- apiref
api_name:
- Description
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# Description Attribute

The **Description** attribute is a description of the content.

## Applies To

-   [Music Files](music-file-attributes.md)

## Remarks

This attribute is stored in music files, not in the library.

This attribute may have multiple values. To retrieve all of the values for a multi-valued attribute, you must use the *Media*.**getItemInfoByType** method, not the *Media*.getItemInfo method.

The Windows Media Format SDK constant for this attribute is g\_wszWMDescription.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> </dl>

 

 





