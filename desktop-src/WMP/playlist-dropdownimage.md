---
title: PLAYLIST.dropDownImage
description: The dropDownImage attribute specifies or retrieves the name of the image used for the drop-down list button that is displayed at the right edge of the drop-down list.
ms.assetid: 92454a8a-1688-4b5d-887d-6847f4232d87
keywords:
- PLAYLIST.dropDownImage Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.dropDownImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# PLAYLIST.dropDownImage

The **dropDownImage** attribute specifies or retrieves the name of the image used for the drop-down list button that is displayed at the right edge of the drop-down list.

``` syntax
        elementID.dropDownImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file. It has no default value.

## Remarks

This attribute supports PNG, JPG, BMP, and GIF files. If the image is an 8-bit BMP file, its hue and saturation values can be changed dynamically using the **hueShift** and **saturation** attributes.

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

[**PLAYLIST.hueShift**](playlist-hueshift.md)
</dt> <dt>

[**PLAYLIST.saturation**](playlist-saturation.md)
</dt> </dl>

 

 





