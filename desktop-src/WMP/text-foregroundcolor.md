---
title: TEXT.foregroundColor
description: The foregroundColor attribute specifies or retrieves the text color for the Text control.
ms.assetid: 1ddbad93-fbff-4be6-9797-6594b5f09a1e
keywords:
- TEXT.foregroundColor Windows Media Player
topic_type:
- apiref
api_name:
- TEXT.foregroundColor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# TEXT.foregroundColor

The **foregroundColor** attribute specifies or retrieves the text color for the Text control.

``` syntax
        elementID.foregroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. The default value is "black".

See the [value](text-value.md) attribute for a sample illustrating how the attributes of the **TEXT** element are used.

When you use **alphaBlend** or **alphaBlendTo** with a **TEXT** element that does not have the **backgroundColor** specified, a background color of black will be used. If the foreground color is also black (which is the default value for the **foregroundColor** attribute), your text may become unreadable. To prevent this, always specify the **backgroundColor** attribute, or set **foregroundColor** to a color other than black.

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

[**TEXT.backgroundColor**](text-backgroundcolor.md)
</dt> </dl>

 

 





