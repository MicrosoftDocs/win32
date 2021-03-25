---
title: SLIDER.foregroundColor
description: The foregroundColor attribute specifies or retrieves the foreground color of the slider control.
ms.assetid: 8c8de4a9-0021-41ed-aeb8-75653855b6f1
keywords:
- SLIDER.foregroundColor Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.foregroundColor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# SLIDER.foregroundColor

The **foregroundColor** attribute specifies or retrieves the foreground color of the slider control.

``` syntax
        elementID.foregroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. The default value is "white".

## Remarks

A basic slider control can be constructed by specifying one of two pairs of attributes: the **backgroundColor** and **foregroundColor**, or the **backgroundImage** and **foregroundImage**.

When you construct a slider control using the color attributes, the dimensions of the slider control define the area filled by the background color. The foreground color covers the background color as the slider position increases.

To make a gradient fill in the area occupied by the background or foreground color, specify the **backgroundEndColor** or **foregroundEndColor** attributes.

See the *CUSTOMSLIDER*.[positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **SLIDER** element are used.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.backgroundColor**](slider-backgroundcolor.md)
</dt> <dt>

[**SLIDER.backgroundEndColor**](slider-backgroundendcolor.md)
</dt> <dt>

[**SLIDER.foregroundEndColor**](slider-foregroundendcolor.md)
</dt> <dt>

[**SLIDER.foregroundImage**](slider-foregroundimage.md)
</dt> </dl>

 

 





