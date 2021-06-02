---
title: SLIDER.thumbImage
description: The thumbImage attribute specifies or retrieves the image that will be used to represent the current position of the slider.
ms.assetid: 3aa69188-3443-483c-81a9-bf22832509d8
keywords:
- SLIDER.thumbImage Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.thumbImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.thumbImage

The **thumbImage** attribute specifies or retrieves the image that will be used to represent the current position of the slider.

``` syntax
        elementID.thumbImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

The **thumbImage** specifies the image that will be used to represent current position, as well as indicate that the user can take action with the control. If no thumb image is specified, the slider is non-interactive.

The thumb image is centered in the narrow dimension of the slider control. If the thumb image is narrower than the control, the image appears in the middle of the background. If the thumb image is larger than the control, the ends of the image are cut off.

The position of the slider is specified by the center of the thumb image. If **borderSize** is zero, only half the thumb image will be visible at the beginning and end slider positions. To prevent this, set **borderSize** to a value greater than or equal to half the width of the thumb image (or half the height if **direction** is set to "vertical").

The supported formats are BMP, JPG, PNG, and GIF (not including animated GIFs).

See the **CUSTOMSLIDER**.[positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **SLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.borderSize**](slider-bordersize.md)
</dt> <dt>

[**SLIDER.direction**](slider-direction.md)
</dt> </dl>

 

 





