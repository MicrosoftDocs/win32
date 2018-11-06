---
title: Normal Tertiary Image Source
description: Normal Tertiary Image Source
ms.assetid: ce0b009a-b008-4e8b-875b-b2ff3c1c0b81
keywords:
- Windows Media Player Mobile skins,button image source
- skins,button image source
- reference for skins,buttons
- buttons in skins,image source
- image source for skins,buttons
ms.topic: article
ms.date: 05/31/2018
---

# Normal Tertiary Image Source

The PlayPauseStop button function requires that you define the location of the normal image for the tertiary state of the button. This will be the image users see after they have pushed the PlayPauseStop button to begin streaming a live broadcast.

To define this image, you must enter the image type followed by a space and the @ symbol and another space. You must then enter two positive integers that define the top-left coordinates (in pixels) of the image you want to use inside the bitmap type you are drawing from.

For example, to define the normal image for a tertiary image source, if your image is inside the Pushed bitmap, type:


```C++
Pushed @ 286,0

```



Tertiary states cannot have a Disabled image. Tertiary images are assumed to be the same width and height as the primary and secondary images.

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




