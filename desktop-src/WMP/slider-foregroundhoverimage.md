---
title: SLIDER.foregroundHoverImage
description: The foregroundHoverImage attribute specifies or retrieves the foreground image of the slider that appears when hovering over it with the mouse.
ms.assetid: c9098852-4d44-4165-a58e-d0b02d46398f
keywords:
- SLIDER.foregroundHoverImage Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.foregroundHoverImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.foregroundHoverImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **foregroundHoverImage** attribute specifies or retrieves the foreground image of the slider that appears when hovering over it with the mouse.

``` syntax
        elementID.foregroundHoverImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

The **foregroundHoverImage** is optional. If it is not provided, the **backgroundImage** is used.

The supported formats are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> </dl>

 

 





