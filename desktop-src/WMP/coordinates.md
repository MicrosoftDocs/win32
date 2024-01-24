---
title: Coordinates
description: Coordinates
ms.assetid: 248af2ea-534e-4d33-82fe-2d46732efed5
keywords:
- Windows Media Player Mobile skins,bitmaps
- skins,bitmaps
- reference for skins,bitmaps
- bitmaps in skins,coordinates
- coordinates in bitmaps in skins
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Coordinates

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This defines the x- and y-coordinates of the image relative to the background file. Two positive integers are required, separated by a comma. There are two types of coordinates you must use, depending on the type of image you are defining. The following table shows the permitted coordinate values for bitmap types.



| Bitmap type               | Coordinate values                                                             |
|---------------------------|-------------------------------------------------------------------------------|
| Background or Super       | 0,0                                                                           |
| Disabled, Push, or Region | The top-left corner of the image relative to the background image, in pixels. |



 

## Related topics

<dl> <dt>

[**Bitmaps**](bitmaps.md)
</dt> </dl>

 

 




