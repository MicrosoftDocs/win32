---
title: BUTTONGROUP.disabledImage
description: The disabledImage attribute specifies or retrieves the name of the image representing the disabled state of the buttons in the BUTTONGROUP.
ms.assetid: 34d4e6a9-de73-4dfa-9c23-4f17b55298f6
keywords:
- BUTTONGROUP.disabledImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.disabledImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONGROUP.disabledImage

The **disabledImage** attribute specifies or retrieves the name of the image representing the disabled state of the buttons in the **BUTTONGROUP**.

``` syntax
        elementID.disabledImage
```

## Possible Values

This attribute is a read/write **String**.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF. If the image is an 8-bit BMP file, its hue and saturation values can be changed dynamically using the **hueShift** and **saturation** attributes.

When the **disabled** attribute of a **BUTTONELEMENT** element is set to true, the corresponding region of the **disabledImage** for the **BUTTONGROUP** is displayed. If the disabled image is larger than the defined region, the disabled image will be cropped.

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

 

 





