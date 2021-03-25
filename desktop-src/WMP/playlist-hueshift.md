---
title: PLAYLIST.hueShift
description: The hueShift attribute specifies or retrieves the amount by which the hue of the drop-down images is shifted.
ms.assetid: 9d4d8b73-527e-43f3-a921-0576b8897918
keywords:
- PLAYLIST.hueShift Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.hueShift
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PLAYLIST.hueShift

The **hueShift** attribute specifies or retrieves the amount by which the hue of the drop-down images is shifted.

``` syntax
        elementID.hueShift
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value ranging from 0.0 to 360.0 with a default value of 0.0.

## Remarks

This attribute changes the hue value of the images specified by the **dropDownBackgroundImage** and **dropDownImage** attributes if they have been specified and they refer to 8-bit BMP images.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.dropDownBackgroundImage**](playlist-dropdownbackgroundimage.md)
</dt> <dt>

[**PLAYLIST.dropDownImage**](playlist-dropdownimage.md)
</dt> <dt>

[**PLAYLIST.saturation**](playlist-saturation.md)
</dt> </dl>

 

 





