---
title: ContentDistributorDuration Attribute
description: The ContentDistributorDuration attribute is the playing duration of the item, in seconds.
ms.assetid: c64cb4ca-b0bc-4beb-b2ae-ddd0c5fcd35c
keywords:
- ContentDistributorDuration Attribute Windows Media Player
topic_type:
- apiref
api_name:
- ContentDistributorDuration
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ContentDistributorDuration Attribute

The **ContentDistributorDuration** attribute is the playing duration of the item, in seconds.

## Applies To

-   [Audio Items](audio-item-attributes.md)
-   [Other Items](other-item-attributes.md)

## Remarks

If the regular **Duration** attribute is either not set (Null) or 0, then the value of this attribute will be returned instead.

To determine whether you can change the value of this attribute, use the [Media.isReadOnlyItem](media-isreadonlyitem.md) method.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------|
| Version<br/> | Windows Media Player 11<br/> |



## See also

<dl> <dt>

[**Attribute Reference**](attribute-reference.md)
</dt> <dt>

[**Duration Attribute**](duration-attribute.md)
</dt> </dl>

 

 





