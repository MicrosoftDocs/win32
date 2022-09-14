---
title: SLIDER.tiled
description: The tiled attribute specifies or retrieves a value indicating whether the slider image will be tiled.
ms.assetid: 159a2972-a0eb-4e43-a083-e124e56782f5
keywords:
- SLIDER.tiled Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.tiled
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.tiled

The **tiled** attribute specifies or retrieves a value indicating whether the slider image will be tiled.

``` syntax
        elementID.tiled
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                                                                 |
|-------|---------------------------------------------------------------------------------------------|
| true  | Default. The image bitmap will be repeated until it fills the entire region of the control. |
| false | The image will not be tiled.                                                                |



 

## Remarks

This attribute applies only if you are using foreground and background images to define a slider control. If the images are smaller than the defined area of the slider, and the **tiled** attribute is set to true, the images will be repeated until they fill the entire length of the control.

You may wish to use this attribute in conjunction with the **borderSize** attribute. The **borderSize** attribute allows you to define a border that is not repeated during tiling.

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

[**SLIDER.borderSize**](slider-bordersize.md)
</dt> <dt>

[**SLIDER.foregroundImage**](slider-foregroundimage.md)
</dt> </dl>

 

 





