---
title: SLIDER.thumbHoverImage
description: The thumbHoverImage attribute specifies or retrieves the image of the thumb that appears when hovering over it with the mouse.
ms.assetid: 128ed8c3-fb06-4f05-a639-12333f989e3f
keywords:
- SLIDER.thumbHoverImage Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.thumbHoverImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.thumbHoverImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **thumbHoverImage** attribute specifies or retrieves the image of the thumb that appears when hovering over it with the mouse.

``` syntax
        elementID.thumbHoverImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

The **thumbHoverImage** is optional. If it is not provided, the slider control will not change appearance when the mouse hovers over it.

The supported formats are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> </dl>

 

 





