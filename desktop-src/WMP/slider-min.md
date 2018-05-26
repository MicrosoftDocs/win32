---
title: SLIDER.min
description: The min attribute specifies or retrieves the minimum value of the range defined by the slider control.
ms.assetid: a152cf9f-7383-47da-a9b2-dedd13749964
keywords:
- SLIDER.min Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.min
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SLIDER.min

The **min** attribute specifies or retrieves the minimum value of the range defined by the slider control.

``` syntax
        elementID.min
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value of zero.

## Remarks

The value specified for **min** must be less than the one for **max**.

See the **CUSTOMSLIDER**.[positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **SLIDER** element are used.

## Requirements



|                    |                                                      |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.max**](slider-max.md)
</dt> <dt>

[**SLIDER.value**](slider-value.md)
</dt> </dl>

 

 





