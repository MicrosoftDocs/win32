---
title: Normal Secondary Image Source
description: Normal Secondary Image Source
ms.assetid: fe5c0da2-0c40-456f-ab56-ac61ed69ff2d
keywords:
- Windows Media Player Mobile skins,button image source
- skins,button image source
- reference for skins,buttons
- buttons in skins,image source
- image source for skins,buttons
ms.topic: article
ms.date: 05/31/2018
---

# Normal Secondary Image Source

Depending on the button function, you may need to define the location of the normal image for the secondary state of the button. This will be the image users see when they push a PlayPause function button the first time.

To define this image, you must enter the image type followed by a space and the @ symbol and another space. You must then enter two positive integers that define the top-left coordinates (in pixels) of the image you want to use inside the bitmap type you are drawing from.

For example, to define the normal image for a secondary image source, if your image is inside the Pushed bitmap, type:


```C++
Pushed @ 210,0

```



Secondary states cannot have a Disabled image. Secondary images are assumed to be the same width and height as the primary image.

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




