---
title: BUTTON.disabledImage
description: The disabledImage attribute specifies or retrieves the image that displays when the BUTTON is disabled.
ms.assetid: b5654323-589a-45da-9534-6fa67c3a4c4b
keywords:
- BUTTON.disabledImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.disabledImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTON.disabledImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **disabledImage** attribute specifies or retrieves the image that displays when the **BUTTON** is disabled.

``` syntax
        elementID.disabledImage
```

## Possible Values

This attribute is a read/write **String** containing the image file name.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF.

This image will be displayed whenever the **disabled** attribute of the control is set to true. If the disabled image is larger than the defined region, the disabled image will be cropped.

If the image cannot be retrieved, a default image (the red-x image) is displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> </dl>

 

 





