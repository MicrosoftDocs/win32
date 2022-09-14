---
title: PLAYLIST.saturation
description: The saturation attribute specifies or retrieves the saturation value of the drop-down images.
ms.assetid: 4c5dd3d9-828a-45c9-896a-9a702d354544
keywords:
- PLAYLIST.saturation Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.saturation
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PLAYLIST.saturation

The **saturation** attribute specifies or retrieves the saturation value of the drop-down images.

``` syntax
        elementID.saturation
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value ranging from 0.0 to 2.0 with a default value of 1.0.

## Remarks

This attribute changes the saturation value of the images specified by the **dropDownBackgroundImage** and **dropDownImage** attributes if they have been specified and they refer to 8-bit BMP images.

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

[**PLAYLIST.hueShift**](playlist-hueshift.md)
</dt> </dl>

 

 





