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
ms.date: 05/31/2018
---

# Pushed Tertiary Image Source

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

 

 




