---
title: CUSTOMSLIDER.downImage
description: The downImage attribute specifies or retrieves the down state image of the custom slider.
ms.assetid: e1efe703-df0a-4ef9-92a9-c9cfb991ee37
keywords:
- CUSTOMSLIDER.downImage Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.downImage
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CUSTOMSLIDER.downImage

The **downImage** attribute specifies or retrieves the down state image of the custom slider.

``` syntax
        elementID.downImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

This attribute is optional. If it not specified, the file specified in the **image** attribute will be used.

The **downImage** represents the down state of the **CUSTOMSLIDER** control. It can be a single image or a series of images representing the various states of the slider. If multiple images are used, they are arranged in the same way as the **image** file.

The supported image file types are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**CUSTOMSLIDER Element**](customslider-element.md)
</dt> <dt>

[**CUSTOMSLIDER.image**](customslider-image.md)
</dt> </dl>

 

 





