---
title: Pushed Tertiary Image Source
description: Pushed Tertiary Image Source
ms.assetid: e2d41729-87c5-4cec-931c-8702585930f2
keywords:
- Windows Media Player Mobile skins,button image source
- skins,button image source
- reference for skins,buttons
- buttons in skins,image source
- image source for skins,buttons
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Pushed Tertiary Image Source

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The PlayPauseStop button function requires that you define the location of the pushed image for the tertiary state of the button. This will be the image users see when they push the PlayPauseStop button while streaming a live broadcast.

To define this image, you must enter the image type followed by a space and the @ symbol and another space. You must then enter two positive integers that define the top-left coordinates (in pixels) of the image you want to use inside the bitmap type you are drawing from.

For example, to define the pushed image for a tertiary image source, if your image is inside the Pushed bitmap, type:


```C++
Pushed @ 324,0

```



Tertiary states cannot have a Disabled image. Tertiary images are assumed to be the same width and height as the primary and secondary images.

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




