---
title: VIDEO.backgroundColor
description: The backgroundColor attribute specifies or retrieves the background color of the Video control.
ms.assetid: 7acf7dc8-80c3-4620-ad89-4c8de20d17ee
keywords:
- VIDEO.backgroundColor Windows Media Player
topic_type:
- apiref
api_name:
- VIDEO.backgroundColor
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# VIDEO.backgroundColor

The **backgroundColor** attribute specifies or retrieves the background color of the Video control.

``` syntax
        elementID.backgroundColor
```

## Possible Values

This attribute is a read/write **String** containing any Microsoft Internet Explorer color value or the value "none". It has a default value of "none", which means that if there is no video associated with the video control, the Video control is transparent and the background shows through.

## Remarks

When the video is smaller than the window and **stretchToFit** is false, the background color appears around the video.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**Color Reference**](color-reference.md)
</dt> <dt>

[**VIDEO Element**](video-element.md)
</dt> <dt>

[**VIDEO.stretchToFit**](video-stretchtofit.md)
</dt> </dl>

 

 





