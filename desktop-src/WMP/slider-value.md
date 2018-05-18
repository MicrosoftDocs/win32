---
title: SLIDER.value
description: The value attribute specifies or retrieves the current position of the slider.
ms.assetid: '29e17f48-1848-458d-9da4-316013b21980'
keywords: ["SLIDER.value Windows Media Player"]
topic_type:
- apiref
api_name:
- SLIDER.value
api_type:
- NA
---

# SLIDER.value

The **value** attribute specifies or retrieves the current position of the slider.

``` syntax
        elementID.value
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value of **min**.

## Remarks

The **value** should always be greater than or equal to **min** and less than or equal to **max**. If you specify a value outside this range, **value** and the position of the slider are not changed.

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
</dt> </dl>

 

 





