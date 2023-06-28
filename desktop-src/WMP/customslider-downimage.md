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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# CUSTOMSLIDER.downImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 





