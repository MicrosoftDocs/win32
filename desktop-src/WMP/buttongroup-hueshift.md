---
title: BUTTONGROUP.hueShift
description: The hueShift attribute specifies or retrieves the amount by which the hue of the BUTTONGROUP images is shifted.
ms.assetid: 156256ef-ec24-40c4-ad23-064e38c79e69
keywords:
- BUTTONGROUP.hueShift Windows Media Player
topic_type:
- apiref
api_name:
- BUTTONGROUP.hueShift
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BUTTONGROUP.hueShift

The **hueShift** attribute specifies or retrieves the amount by which the hue of the **BUTTONGROUP** images is shifted.

``` syntax
        elementID.hueShift
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value ranging from 0.0 to 360.0 with a default value of 0.0.

## Remarks

This attribute changes the hue value of the images specified by the **disabledImage**, **downImage**, **hoverDownImage**, **hoverImage**, and **image** attributes if they have been specified and they refer to 8-bit BMP images.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**BUTTONGROUP Element**](buttongroup-element.md)
</dt> <dt>

[**BUTTONGROUP.disabledImage**](buttongroup-disabledimage.md)
</dt> <dt>

[**BUTTONGROUP.downImage**](buttongroup-downimage.md)
</dt> <dt>

[**BUTTONGROUP.hoverDownImage**](buttongroup-hoverdownimage.md)
</dt> <dt>

[**BUTTONGROUP.hoverImage**](buttongroup-hoverimage.md)
</dt> <dt>

[**BUTTONGROUP.image**](buttongroup-image.md)
</dt> <dt>

[**BUTTONGROUP.saturation**](buttongroup-saturation.md)
</dt> </dl>

 

 





