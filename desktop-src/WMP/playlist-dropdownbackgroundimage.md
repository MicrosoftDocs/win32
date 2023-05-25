---
title: PLAYLIST.dropDownBackgroundImage
description: The dropDownBackgroundImage attribute specifies or retrieves the name of the image that displays in the background of the drop-down list.
ms.assetid: 40253d82-7178-4f6c-805b-7c1e92ea0636
keywords:
- PLAYLIST.dropDownBackgroundImage Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.dropDownBackgroundImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.dropDownBackgroundImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **dropDownBackgroundImage** attribute specifies or retrieves the name of the image that displays in the background of the drop-down list.

``` syntax
        elementID.dropDownBackgroundImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file. It has no default value.

## Remarks

This attribute supports PNG, JPG, BMP, and GIF files. If the image is an 8-bit BMP file, its hue and saturation values can be changed dynamically using the **hueShift** and **saturation** attributes.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------|
| Version<br/> | Windows Media Player 9 Series or later<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> <dt>

[**PLAYLIST.dropDownImage**](playlist-dropdownimage.md)
</dt> <dt>

[**PLAYLIST.hueShift**](playlist-hueshift.md)
</dt> <dt>

[**PLAYLIST.saturation**](playlist-saturation.md)
</dt> </dl>

 

 





