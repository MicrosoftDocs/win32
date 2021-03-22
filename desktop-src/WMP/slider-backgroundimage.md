---
title: SLIDER.backgroundImage
description: The backgroundImage attribute specifies or retrieves the background image of the slider.
ms.assetid: 73757635-4d1c-4ed0-8721-0608cd85859c
keywords:
- SLIDER.backgroundImage Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.backgroundImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.backgroundImage

The **backgroundImage** attribute specifies or retrieves the background image of the slider.

``` syntax
        elementID.backgroundImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

This attribute is optional. When using images to construct a slider, the **backgroundImage** is used for the main slider image. The **thumbImage** represents the actual slider and can be moved using the mouse. At the **thumbImage** slider there is an invisible line where the background image is displayed on one side of the line, and the foreground image is displayed on the other side.

When the **thumbImage** slider is moved with the mouse, if **slide** is set to true, the foreground image slides along as if being pulled by the slider to cover the background image. If **slide** is set to false, the foreground image does not move, but is revealed in place, as if the slider is moving the background image off the foreground image.

If the **tiled** attribute is set to true and the background image is smaller than the slider control, the image will be tiled either horizontally or vertically depending on the **direction** attribute. If the **borderSize** attribute is set to a value greater than zero, the number specified will be the number of pixels from the left and right or top and bottom of the image (again, depending on the **direction** attribute) that will be reserved for the borders of the slider control. In this case, only the central portion of the image is used for tiling the remainder of the control.

The supported formats are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.foregroundImage**](slider-foregroundimage.md)
</dt> <dt>

[**SLIDER.slide**](slider-slide.md)
</dt> <dt>

[**SLIDER.thumbImage**](slider-thumbimage.md)
</dt> </dl>

 

 





