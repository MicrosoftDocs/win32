---
title: SLIDER.max
description: The max attribute specifies or retrieves the maximum value of the range defined by the slider control.
ms.assetid: 2b788b13-d9a8-4cf6-9397-a2fc8d5d19e1
keywords:
- SLIDER.max Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.max
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SLIDER.max

The **max** attribute specifies or retrieves the maximum value of the range defined by the slider control.

``` syntax
        elementID.max
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value of 100.

## Remarks

The value specified for **max** must be greater than the one for **min**.

See the **CUSTOMSLIDER**.[positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **SLIDER** element are used.

## Requirements



|                    |                                                      |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.min**](slider-min.md)
</dt> <dt>

[**SLIDER.value**](slider-value.md)
</dt> </dl>

 

 





