---
title: SLIDER.transparencyColor
description: The transparencyColor attribute specifies or retrieves the transparent color of the slider control background and foreground images.
ms.assetid: 39bdac82-7c84-4c79-b3f0-ec4828263ccd
keywords:
- SLIDER.transparencyColor Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.transparencyColor
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SLIDER.transparencyColor

The **transparencyColor** attribute specifies or retrieves the transparent color of the slider control background and foreground images.

``` syntax
        elementID.transparencyColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value. It has no default value.

## Remarks

Any part of the image containing the **transparencyColor** will allow the background to show through.

Because JPGs are lossy and therefore subject to unexpected color change, they are not recommended when **transparencyColor** is used.

## Requirements



|                    |                                                      |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**Color Reference**](color-reference.md)
</dt> </dl>

 

 





