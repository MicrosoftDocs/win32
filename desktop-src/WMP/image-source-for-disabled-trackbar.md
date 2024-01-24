---
title: Image Source for Disabled Trackbar
description: Image Source for Disabled Trackbar
ms.assetid: ecbe1670-2914-4b66-92bd-d854e6c1e897
keywords:
- Windows Media Player Mobile skins,trackbars
- skins,trackbars
- reference for skins,trackbars
- trackbars in skins,image source
- image source for skins,trackbars
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Image Source for Disabled Trackbar

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must define the source of the image you want to display when a trackbar is disabled, using the bitmap type you want to draw the image from. The image you display will usually be inside the Super file or if you are creating a skin for Windows Media Player 10 Mobile, the image would be inside the SeekThumb file. You must enter the image type followed by a space and the @ symbol and another space. You must then enter two positive integers that define the top-left coordinates (in pixels) of the image you want to use inside the bitmap type you are drawing from.

For example, to use an image from the SeekThumb bitmap that has a top and left position of 50,60 pixels, type:


```C++
Disabled @ 50,60

```



You must define an image location for a disabled trackbar image. If you do not want to display a new image, you can define the Background image as your Disabled image with an offset of 0,0:


```C++
Disabled @ 50,60

```



In the preceding example, 50,60 represents the location of the button you are working with in the SeekThumb file (in this case, the same location as the button on the Background bitmap). However, it is highly recommended that you display a Disabled image for all trackbars to give your user a visual indication, because trackbars will not be useable under certain conditions. For example, Seek trackbars may be disabled when the current playlist is empty.

## Related topics

<dl> <dt>

[**Trackbars**](trackbars.md)
</dt> </dl>

 

 




