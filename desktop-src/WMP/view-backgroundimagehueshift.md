---
title: VIEW.backgroundImageHueShift
description: The backgroundImageHueShift attribute specifies or retrieves the amount by which the hue of the background image is shifted.
ms.assetid: 13cedc87-f43a-4d33-9339-f317ea7b8d3b
keywords:
- VIEW.backgroundImageHueShift Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.backgroundImageHueShift
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VIEW.backgroundImageHueShift

The **backgroundImageHueShift** attribute specifies or retrieves the amount by which the hue of the background image is shifted.

``` syntax
        elementID.backgroundImageHueShift
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value ranging from 0.0 to 360.0 with a default value of 0.0.

## Remarks

This attribute changes the hue value of the images specified by the **backgroundImage** attribute if it has been specified and it refers to an 8-bit BMP image.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**VIEW.backgroundImage**](view-backgroundimage.md)
</dt> <dt>

[**VIEW.backgroundImageSaturation**](view-backgroundimagesaturation.md)
</dt> </dl>

 

 





