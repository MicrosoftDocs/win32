---
title: AmbientAttributes.clippingColor
description: The clippingColor attribute specifies or retrieves the color to clip out from the clippingImage bitmap.
ms.assetid: d6ea43d3-c118-43d3-bfdc-29ddd6ea4978
keywords:
- AmbientAttributes.clippingColor Windows Media Player
topic_type:
- apiref
api_name:
- AmbientAttributes.clippingColor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# AmbientAttributes.clippingColor

The **clippingColor** attribute specifies or retrieves the color to clip out from the **clippingImage** bitmap.

``` syntax
        elementID.clippingColor
```

## Possible Values

This attribute is a read/write **String**.



| Value                                       | Description                                       |
|---------------------------------------------|---------------------------------------------------|
| Auto                                        | Default. The color at pixel location 0,0 is used. |
| any Microsoft Internet Explorer color value | The specified Internet Explorer color is used.    |



 

## Remarks

The clipping color indicates the regions of the **clippingImage** (or **backgroundImage** for **VIEW** or **SUBVIEW**) that correspond to transparent, non-clickable portions of the control. The clipping color can indicate multiple regions to be clipped out. A warning is issued if the **clippingImage** is a JPG to warn of loss of color in JPGs.

The **clippingColor** attribute is not supported by the **PLAYLIST** element.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Ambient Attributes**](ambient-attributes.md)
</dt> <dt>

[**AmbientAttributes.clippingImage**](ambientattributes-clippingimage.md)
</dt> <dt>

[**Color Reference**](color-reference.md)
</dt> </dl>

 

 





