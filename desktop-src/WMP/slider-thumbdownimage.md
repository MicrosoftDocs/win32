---
title: SLIDER.thumbDownImage
description: The thumbDownImage attribute specifies or retrieves the image representing the down state of the thumb.
ms.assetid: 6e7c694a-b651-4327-9550-8e05d0c42f02
keywords:
- SLIDER.thumbDownImage Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.thumbDownImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.thumbDownImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **thumbDownImage** attribute specifies or retrieves the image representing the down state of the thumb.

``` syntax
        elementID.thumbDownImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

The **thumbDownImage** is optional and is the image used to represent the down state of the **thumbImage**. If a **thumbDownImage** is not provided, the slider will use the **thumbImage**.

The supported formats are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**SLIDER.thumbImage**](slider-thumbimage.md)
</dt> </dl>

 

 





