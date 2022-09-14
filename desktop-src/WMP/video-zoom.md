---
title: VIDEO.zoom
description: The zoom attribute specifies the percentage by which to scale the video.
ms.assetid: 71c0e5a6-f7c4-46cf-a180-083d2926ba20
keywords:
- VIDEO.zoom Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.zoom
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VIDEO.zoom

The **zoom** attribute specifies the percentage by which to scale the video.

``` syntax
        elementID.zoom
```

## Possible Values

This attribute is a read/write **Number** (**long**) ranging from 1 to the maximum size accommodated by the width and height of the Video control. It has a default value of 100.

## Remarks

This attribute cannot be used in conjunction with the **fullScreen** attribute.

If **width** and **height** are specified, and the resulting video window is larger than the video being played, the video can be enlarged by scaling up to the maximum size accommodated by the window. If **width** and **height** are not specified, **zoom** is limited to values of 100 or less.

If the **shrinkToFit** property is false, the video will change proportion upon zooming, to fit itself to the available space. If **shrinkToFit** is true, the video will shrink to fit within the most restrictive dimension, while retaining its original proportions.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**VIDEO Element**](video-element.md)
</dt> <dt>

[**VIDEO.fullScreen**](video-fullscreen.md)
</dt> <dt>

[**VIDEO.shrinkToFit**](video-shrinktofit.md)
</dt> </dl>

 

 





