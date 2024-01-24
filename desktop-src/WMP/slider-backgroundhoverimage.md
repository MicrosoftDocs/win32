---
title: SLIDER.backgroundHoverImage
description: The backgroundHoverImage attribute specifies or retrieves the background image of the slider that appears when hovering over it with the mouse.
ms.assetid: 292af0c4-d720-4f29-9778-6ae83539da70
keywords:
- SLIDER.backgroundHoverImage Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.backgroundHoverImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.backgroundHoverImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **backgroundHoverImage** attribute specifies or retrieves the background image of the slider that appears when hovering over it with the mouse.

``` syntax
        elementID.backgroundHoverImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

This attribute is optional. If it is not specified, the **backgroundImage** will be used.

The supported formats are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> </dl>

 

 





