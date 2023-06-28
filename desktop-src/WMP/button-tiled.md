---
title: BUTTON.tiled
description: The tiled attribute specifies or retrieves a value indicating whether the BUTTON image will be tiled.
ms.assetid: 5526477d-a235-4960-adef-5cf0ef9c46be
keywords:
- BUTTON.tiled Windows Media Player
topic_type:
- apiref
api_name:
- BUTTON.tiled
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTON.tiled

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **tiled** attribute specifies or retrieves a value indicating whether the **BUTTON** image will be tiled.

``` syntax
        elementID.tiled
```

## Possible Values

This attribute is a read/write **Boolean**.



| Value | Description                       |
|-------|-----------------------------------|
| true  | Image will be tiled.              |
| false | Default. Image will not be tiled. |



 

## Remarks

If the image is smaller than the actual region of the control, then tiling the image will repeat it until it fills the entire region. If an image is not specified or cannot be retrieved, **tiled** will be set to false.

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

 

 





