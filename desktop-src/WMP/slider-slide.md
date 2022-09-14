---
title: SLIDER.slide
description: The slide attribute specifies or retrieves a value indicating whether the foreground image slides over the background image or is gradually revealed in a static position over the background image.
ms.assetid: dc68c2a0-d3fe-4984-9607-12703a27edbd
keywords:
- SLIDER.slide Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.slide
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.slide

The **slide** attribute specifies or retrieves a value indicating whether the foreground image slides over the background image or is gradually revealed in a static position over the background image.

``` syntax
        elementID.slide
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                                                          |
|-------|----------------------------------------------------------------------|
| true  | Default. The foreground image slides over the background image.      |
| false | The foreground image is revealed in place over the background image. |



 

## Remarks

When the **thumbImage** slider is moved with the mouse, if **slide** is set to true, the foreground image slides along as if being pulled by the slider to cover the background image. If **slide** is set to false, the foreground image does not move, but is revealed in place, as if the slider is moving the background image off the foreground image.

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

[**SLIDER.foregroundImage**](slider-foregroundimage.md)
</dt> </dl>

 

 





