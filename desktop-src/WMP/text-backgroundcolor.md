---
title: TEXT.backgroundColor
description: The backgroundColor attribute specifies or retrieves the background color for the Text control.
ms.assetid: 0c16318f-bf57-4c5f-85c1-46641124d431
keywords:
- TEXT.backgroundColor Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.backgroundColor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# TEXT.backgroundColor

The **backgroundColor** attribute specifies or retrieves the background color for the Text control.

``` syntax
        elementID.backgroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value or the value "none". It has a default value of "none", which means the background is transparent.

## Remarks

The background color is set for the height and width of the control. If height and width are not set, the background color is set to the height and width of the text.

When you use **alphaBlend** or **alphaBlendTo** with a **TEXT** element that does not have the **backgroundColor** specified, a background color of black will be used. If the foreground color is also black (which is the default value for the **foregroundColor** attribute), your text may become unreadable. To prevent this, always specify the **backgroundColor** attribute, or set **foregroundColor** to a color other than black.

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**AmbientAttributes.alphaBlend**](ambientattributes-alphablend.md)
</dt> <dt>

[**AmbientAttributes.alphaBlendTo**](ambientattributes-alphablendto.md)
</dt> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**TEXT Element**](text-element.md)
</dt> <dt>

[**TEXT.foregroundColor**](text-foregroundcolor.md)
</dt> </dl>

 

 





