---
title: Pushed Image Source
description: Pushed Image Source
ms.assetid: 6cc290d8-2c15-4789-970d-9a3663a64d08
keywords:
- Windows Media Player Mobile skins,button image source
- skins,button image source
- reference for skins,buttons
- buttons in skins,image source
- image source for skins,buttons
ms.topic: article
ms.date: 05/31/2018
---

# Pushed Image Source

You must define the source of the image you want to display when the user pushes a button. The image comes from the file you defined as Pushed in the Bitmaps section. You must enter the image type followed by a space and the @ symbol and another space. You must then enter two positive integers that define the top and left coordinates (in pixels) of the image you want to use inside the Pushed image file. The location at which the image will be displayed comes from the coordinates defined for the button relative to the Background image; but the location it comes from is defined by the two numbers following "Pushed @" and is relative to the Pushed image you are reading the image from.

For example, to use an image from the Pushed image that is in the Pushed file whose top-left location is 50,60 you would use the following code:


```C++
Pushed @ 50,60

```



If you do not want to display a different image, you can define the Background bitmap as your Pushed bitmap. To do this, specify the Background file as your pushed file and specify the offset to the top-left corner of the button:


```C++
Pushed @ 50,60

```



If you do this, none of your buttons can display a Pushed image. We recommend that you display a Pushed image for all buttons to give your user a visual indication, because it is not always clear whether a tap produces a result, especially when music is playing or the tapping sound is turned off.

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




