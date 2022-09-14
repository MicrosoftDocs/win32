---
title: CUSTOMSLIDER.transparencyColor
description: The transparencyColor attribute specifies or retrieves the transparency color of the custom slider images.
ms.assetid: 39bdac82-7c84-4c79-b3f0-ec4828263ccd
keywords:
- CUSTOMSLIDER.transparencyColor Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.transparencyColor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CUSTOMSLIDER.transparencyColor

The **transparencyColor** attribute specifies or retrieves the transparency color of the custom slider images.

``` syntax
        elementID.transparencyColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. It has no default value.

## Remarks

Any part of the custom slider images containing the **transparencyColor** will allow the background to show through.

Because JPGs are lossy and therefore subject to unexpected color change, they are not recommended when **transparencyColor** is used.

## Examples

See the [positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **CUSTOMSLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> </dl>

 

 





