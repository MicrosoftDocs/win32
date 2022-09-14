---
title: BUTTONGROUP.downImage
description: The downImage attribute specifies or retrieves the name of the image representing the down state of the BUTTONGROUP.
ms.assetid: 022e77e7-d3c0-41b5-984a-84d016a5a25a
keywords:
- BUTTONGROUP.downImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.downImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONGROUP.downImage

The **downImage** attribute specifies or retrieves the name of the image representing the down state of the **BUTTONGROUP**.

``` syntax
        elementID.downImage
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF. If the image is an 8-bit BMP file, its hue and saturation values can be changed dynamically using the **hueShift** and **saturation** attributes.

The default image is the one specified in the **image** attribute.

If the down image is larger than the defined region, the down image will be cropped.

If the image cannot be retrieved, a default image (the red-x image) is displayed.

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

 

 





