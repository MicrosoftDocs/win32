---
title: CUSTOMSLIDER.hoverImage
description: The hoverImage attribute specifies or retrieves the image that appears when the mouse is over the custom slider.
ms.assetid: b5d10289-280c-4578-83e8-6259249ff448
keywords:
- CUSTOMSLIDER.hoverImage Windows Media Player
topic_type:
- apiref
api_name:
- CUSTOMSLIDER.hoverImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.hoverImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **hoverImage** attribute specifies or retrieves the image that appears when the mouse is over the custom slider.

``` syntax
        elementID.hoverImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file.

## Remarks

This attribute is optional. If it not specified, the file specified in the **image** attribute will be used.

The **hoverImage** represents the hover state of the CUSTOMSLIDER control; that is, the state that is shown when the mouse cursor hovers over it. It can be a single image or a series of images representing the various states of the slider. If multiple images are used, they are arranged in the same way as the **image** file

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

 

 





