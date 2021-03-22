---
title: BUTTON.image
description: The image attribute specifies or retrieves the default image of the BUTTON.
ms.assetid: d0d97f14-2c4d-4769-b45c-c6cde7282bea
keywords:
- BUTTON.image Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.image
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTON.image

The **image** attribute specifies or retrieves the default image of the **BUTTON**.

``` syntax
        elementID.image
```

## Possible Values

This attribute is a read/write **String** containing the image file name.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF (including animated GIFs).

If the **BUTTON** image is larger than the region defined by the **width** and **height** attributes, the image will be cropped.

If the image is not specified but the **height** and **width** are, then the image directly behind this control is displayed. This can facilitate drawing the image on the **VIEW** itself, reducing the number of separate image files needed.

If the image cannot be retrieved, a default image (the red-x image) is displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> </dl>

 

 





