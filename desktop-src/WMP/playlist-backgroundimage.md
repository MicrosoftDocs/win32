---
title: PLAYLIST.backgroundImage
description: The backgroundImage attribute specifies or retrieves the background image.
ms.assetid: d4efa774-d42e-4415-a487-1e858d984075
keywords:
- PLAYLIST.backgroundImage Windows Media Player
topic_type:
- apiref
api_name:
- PLAYLIST.backgroundImage
api_type:
- NA
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST.backgroundImage

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **backgroundImage** attribute specifies or retrieves the background image.

``` syntax
        elementID.backgroundImage
```

## Possible Values

This attribute is a read/write **String** containing the name of an image file. It has no default value.

## Remarks

If the image height and width are smaller than the height and width of the **PLAYLIST** element, the image is tiled. The supported formats are BMP, JPG, GIF and PNG.

Specifying a value of "gradient" for the background image causes the background of the playlist to display as a color gradient. This means the background color gradually transitions between the [PLAYLIST.backgroundColor](playlist-backgroundcolor.md) (at the top of the background) and [PLAYLIST.statusColor](playlist-statuscolor.md) values.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later, Windows Media Player 10 for the gradient feature<br/> |



## See also

<dl> <dt>

[**PLAYLIST Element**](playlist-element.md)
</dt> </dl>

 

 





