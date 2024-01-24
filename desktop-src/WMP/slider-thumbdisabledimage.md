---
title: SLIDER.thumbDisabledImage
description: The thumbDisabledImage attribute specifies or retrieves the thumb image of the slider control that is used when the control is disabled.
ms.assetid: 56b7d373-bf97-4a13-bd00-9cbee1e40762
keywords:
- SLIDER.thumbDisabledImage Windows Media Player
topic_type:
- apiref
api_name:
- SLIDER.thumbDisabledImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SLIDER.thumbDisabledImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **thumbDisabledImage** attribute specifies or retrieves the thumb image of the slider control that is used when the control is disabled.

``` syntax
        elementID.thumbDisabledImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

The **thumbDisabledImage** is optional. If it is not specified, **thumbImage** is used instead.

The supported formats are BMP, JPG, PNG, and GIF (not including animated GIFs).

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**SLIDER Element**](slider-element.md)
</dt> <dt>

[**AmbientAttributes.enabled**](ambientattributes-enabled.md)
</dt> <dt>

[**SLIDER.thumbImage**](slider-thumbimage.md)
</dt> </dl>

 

 





