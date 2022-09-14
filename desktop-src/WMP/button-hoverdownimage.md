---
title: BUTTON.hoverDownImage
description: The hoverDownImage attribute specifies or retrieves the image displayed when the BUTTON is in the down state and the user hovers over it with the mouse pointer.
ms.assetid: 06645307-50f1-400d-aa73-c48d0fba3ee1
keywords:
- BUTTON.hoverDownImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.hoverDownImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTON.hoverDownImage

The **hoverDownImage** attribute specifies or retrieves the image displayed when the **BUTTON** is in the down state and the user hovers over it with the mouse pointer.

``` syntax
        elementID.hoverDownImage
```

## Possible Values

This attribute is a read/write **String** containing the image file name.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF.

The default image is the one specified in the **downImage** attribute, or its default.

If the hover-down image is larger than the defined region in the ambient attribute, the hover-down image will be cropped.

If the image cannot be retrieved, a default image (the red-x image) is displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> <dt>

[**BUTTON.downImage**](button-downimage.md)
</dt> </dl>

 

 





