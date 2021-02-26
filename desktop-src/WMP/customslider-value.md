---
title: CUSTOMSLIDER.value
description: The value attribute specifies or retrieves the current position of the slider. | CUSTOMSLIDER.value
ms.assetid: 29e17f48-1848-458d-9da4-316013b21980
keywords:
- CUSTOMSLIDER.value Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.value
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CUSTOMSLIDER.value

The **value** attribute specifies or retrieves the current position of the slider.

``` syntax
        elementID.value
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a default value equal to the **min** attribute.

## Remarks

The **value** must be greater than or equal to **min** and less than or equal to **max**. If the value falls outside the range, a warning is issued, and the value does not change.

## Examples

See the [positionImage](customslider-positionimage.md) attribute for a sample illustrating how the attributes of the **CUSTOMSLIDER** element are used.

## Requirements



|                    |                                                      |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> </dl>

 

 





