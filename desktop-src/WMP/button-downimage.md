---
title: BUTTON.downImage
description: The downImage attribute specifies or retrieves the image representing the down state of the BUTTON.
ms.assetid: 18149668-5be6-4b64-8adf-8904585ff0be
keywords:
- BUTTON.downImage Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.downImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTON.downImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **downImage** attribute specifies or retrieves the image representing the down state of the **BUTTON**.

``` syntax
        elementID.downImage
```

## Possible Values

This attribute is a read/write **String** containing the image file name.

## Remarks

The supported image formats are BMP, JPG, PNG, and GIF.

The default image is the one specified in the **image** attribute, or its default.

If the down image is larger than the defined region in the ambient attribute, the down image will be cropped.

If the image cannot be retrieved, a default image (the red-x image) is displayed.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later<br/> |



## See also

<dl> <dt>

[**BUTTON Element**](button-element.md)
</dt> <dt>

[**BUTTON.down**](button-down.md)
</dt> <dt>

[**BUTTON.image**](button-image.md)
</dt> </dl>

 

 





