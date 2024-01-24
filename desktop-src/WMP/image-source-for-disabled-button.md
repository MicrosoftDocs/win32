---
title: Image Source for Disabled Button
description: Image Source for Disabled Button
ms.assetid: 6c50e0bd-c174-4335-8d34-ae25feec9ec6
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

# Image Source for Disabled Button

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must define the source of the image you want to display when a button is disabled or has a state that corresponds to off. The image comes from the file you defined as Disabled in the Bitmaps section. You must enter the image type followed by a space and the @ symbol and another space. You must then enter two positive integers that define the top-left coordinates (in pixels) of the image you want to use inside the bitmap file. The location at which the image will be displayed comes from the coordinates defined for the button relative to the Background image, but the location it comes from is defined by the two numbers following "Disabled @" and is relative to the Disabled bitmap you are reading the image from.

For example, to use an image from the Disabled bitmap that is in the Disabled file at a top and left location of 50,60 pixels, use the following code:


```C++
Disabled @ 50,60

```



You must define a Disabled bitmap. If you do not want to display a different image, you can define the Background bitmap as your Disabled bitmap with an offset of 0,0:


```C++
Disabled @ 50,60

```



In the preceding example, 50,60 is the location of the button you are working with in the Disabled file (in this case, the same location as the button on the Background bitmap). However, it is highly recommended that you display a Disabled image for all buttons to give your users a visual indication, because many buttons will not be useable under certain conditions, such as an empty playlist. If users know a button is disabled, they will not keep trying to click on it or think your skin is not functioning as designed.

## Related topics

<dl> <dt>

[**Buttons**](buttons.md)
</dt> </dl>

 

 




