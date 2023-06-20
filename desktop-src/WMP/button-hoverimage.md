---
title: BUTTON.hoverImage
description: The hoverImage attribute specifies or retrieves the image displayed when the BUTTON is in the up state and the user hovers over it with the mouse pointer.
ms.assetid: 6704e63d-1def-4e8e-808f-131c3cc1c0de
keywords:
- BUTTON.hoverImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.hoverImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTON.hoverImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **hoverImage** attribute specifies or retrieves the image displayed when the **BUTTON** is in the up state and the user hovers over it with the mouse pointer.

``` syntax
        elementID.hoverImage
```

## Possible Values

This attribute is a read/write **String** containing the image file name.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF.

The default image is the one specified in the **image** attribute, or its default.

If the hover image is larger than the defined region in the ambient attribute, the hover image will be cropped.

If the image cannot be retrieved, a default image (the red-x image) is displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> <dt>

[**BUTTON.image**](button-image.md)
</dt> </dl>

 

 





