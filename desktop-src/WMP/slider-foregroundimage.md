---
title: SLIDER.foregroundImage
description: The foregroundImage attribute specifies or retrieves the foreground image of the slider.
ms.assetid: f713fba8-e965-4fed-b323-8a513d1f13e6
keywords:
- SLIDER.foregroundImage Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.foregroundImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.foregroundImage

The **foregroundImage** attribute specifies or retrieves the foreground image of the slider.

``` syntax
        elementID.foregroundImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

This attribute is optional. When using images to construct a slider control, the **backgroundImage** is used for the main slider image. The **thumbImage** represents the actual slider and can be moved using the mouse. At the **thumbImage** slider there is an invisible line where the background image is displayed on one side of the line, and the foreground image is displayed on the other side.

When the **thumbImage** slider is moved with the mouse, if **slide** is set to true, the foreground image slides along as if being pulled by the slider to cover the background image. If **slide** is set to false, the foreground image does not move, but is revealed in place, as if the slider is moving the background image off the foreground image.

If the **tiled** attribute is set to true and the foreground image is smaller than the foreground area of the slider control, the image will be tiled either horizontally or vertically, depending on the **direction** attribute, to fill the available space.

The supported formats are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.backgroundImage**](slider-backgroundimage.md)
</dt> <dt>

[**SLIDER.slide**](slider-slide.md)
</dt> <dt>

[**SLIDER.thumbImage**](slider-thumbimage.md)
</dt> <dt>

[**SLIDER.value**](slider-value.md)
</dt> </dl>

 

 





