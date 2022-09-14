---
title: BUTTONGROUP.image
description: The image attribute specifies or retrieves the name of the image representing the buttons of a BUTTONGROUP.
ms.assetid: dad50a1e-d147-4e0f-b5d6-8cbfeef32438
keywords:
- BUTTONGROUP.image Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.image
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONGROUP.image

The **image** attribute specifies or retrieves the name of the image representing the buttons of a **BUTTONGROUP**.

``` syntax
        elementID.image
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF. If the image is an 8-bit BMP file, its hue and saturation values can be changed dynamically using the **hueShift** and **saturation** attributes.

If the image of the control is larger than the defined region, the image will be cropped.

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

[**BUTTONGROUP.saturation**](buttongroup-saturation.md)
</dt> </dl>

 

 





