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
ms.date: 05/31/2018
---

# PLAYLIST.backgroundImage

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

 

 





