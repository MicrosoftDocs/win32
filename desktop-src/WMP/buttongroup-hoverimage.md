---
title: BUTTONGROUP.hoverImage
description: The hoverImage attribute specifies or retrieves the name of the image representing the hover state of a button in the BUTTONGROUP. The hover state occurs when the button is in the up state and the user hovers over it with the mouse.
ms.assetid: 319b8770-8c4a-441a-ad03-9ff895958cf2
keywords:
- BUTTONGROUP.hoverImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.hoverImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONGROUP.hoverImage

The **hoverImage** attribute specifies or retrieves the name of the image representing the hover state of a button in the **BUTTONGROUP**. The hover state occurs when the button is in the up state and the user hovers over it with the mouse.

``` syntax
        elementID.hoverImage
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF. If the image is an 8-bit BMP file, its hue and saturation values can be changed dynamically using the **hueShift** and **saturation** attributes.

The default image is the one specified in the **image** attribute, or its default.

If the hover image is larger than the defined region, the hover image will be cropped.

If the image cannot be retrieved, a default image (the red-x image) is displayed.

## Examples

See the *BUTTONELEMENT*.[mappingColor](buttonelement-mappingcolor.md) attribute for a sample illustrating the use of this attribute.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> <dt>

[**BUTTONGROUP.hueShift**](buttongroup-hueshift.md)
</dt> <dt>

[**BUTTONGROUP.image**](buttongroup-image.md)
</dt> <dt>

[**BUTTONGROUP.saturation**](buttongroup-saturation.md)
</dt> </dl>

 

 





