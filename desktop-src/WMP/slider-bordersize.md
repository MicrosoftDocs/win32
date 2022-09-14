---
title: SLIDER.borderSize
description: The borderSize attribute specifies or retrieves the border width in pixels.
ms.assetid: ca766b45-1be3-4207-8cd0-ad50c33d52be
keywords:
- SLIDER.borderSize Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.borderSize
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.borderSize

The **borderSize** attribute specifies or retrieves the border width in pixels.

``` syntax
        elementID.borderSize
```

## Possible Values

This attribute is a read/write **Number** (**long**) representing the border width in pixels. The default value is zero.

## Remarks

This attribute defines an offset from the beginning and end of the slider control that is, from the left and right if the **direction** attribute is set to "horizontal", and from the top and bottom if it is set to "vertical". These offset positions dictate the minimum and maximum positions of the slider thumb, beyond which the foreground color or image will not be applied.

If a background image is used with the **tiled** attribute set to true, the offset is applied to the image, dictating the amount of the image (either from the left and right or from the top and bottom) to be used for the beginning and end borders of the slider control, with the central portion of the image being tiled throughout the remainder. In this way, a small background image can be used to cover the full length of a larger slider control.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.foregroundColor**](slider-foregroundcolor.md)
</dt> <dt>

[**SLIDER.foregroundImage**](slider-foregroundimage.md)
</dt> <dt>

[**SLIDER.thumbImage**](slider-thumbimage.md)
</dt> <dt>

[**SLIDER.tiled**](slider-tiled.md)
</dt> </dl>

 

 





