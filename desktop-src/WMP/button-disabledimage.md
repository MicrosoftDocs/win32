---
title: BUTTON.disabledImage
description: The disabledImage attribute specifies or retrieves the image that displays when the BUTTON is disabled.
ms.assetid: b5654323-589a-45da-9534-6fa67c3a4c4b
keywords:
- BUTTON.disabledImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.disabledImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTON.disabledImage

The **disabledImage** attribute specifies or retrieves the image that displays when the **BUTTON** is disabled.

``` syntax
        elementID.disabledImage
```

## Possible Values

This attribute is a read/write **String** containing the image file name.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF.

This image will be displayed whenever the **disabled** attribute of the control is set to true. If the disabled image is larger than the defined region, the disabled image will be cropped.

If the image cannot be retrieved, a default image (the red-x image) is displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> </dl>

 

 





