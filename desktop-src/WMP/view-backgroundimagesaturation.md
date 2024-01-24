---
title: VIEW.backgroundImageSaturation
description: The backgroundImageSaturation attribute specifies or retrieves the saturation value of the background image.
ms.assetid: 9e1f205b-6366-4816-9430-1153f57d686c
keywords:
- VIEW.backgroundImageSaturation Windows Media Player
topic_type:
- apiref
api_name:
- VIEW.backgroundImageSaturation
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VIEW.backgroundImageSaturation

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **backgroundImageSaturation** attribute specifies or retrieves the saturation value of the background image.

``` syntax
        elementID.backgroundImageSaturation
```

## Possible Values

This attribute is a read/write **Number** (**float**) with a value ranging from 0.0 to 2.0 with a default value of 1.0.

## Remarks

This attribute changes the saturation value of the images specified by the **backgroundImage** attribute if it has been specified and it refers to an 8-bit BMP image.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**VIEW Element**](view-element.md)
</dt> <dt>

[**VIEW.backgroundImage**](view-backgroundimage.md)
</dt> <dt>

[**VIEW.backgroundImageHueShift**](view-backgroundimagehueshift.md)
</dt> </dl>

 

 





