---
title: Thumb Image Source
description: Thumb Image Source
ms.assetid: dca1f54d-ee79-4fd4-9c4e-8226f65c9515
keywords:
- Windows Media Player Mobile skins,trackbars
- skins,trackbars
- reference for skins,trackbars
- trackbars in skins,image source
- trackbars in skins,thumb image source
- image source for skins,trackbars
- thumb,image source
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Thumb Image Source

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must define the name of the file that contains the thumb image. This must be a valid file name with the extension .bmp, .gif, .jpg, or .png. The file must contain three side-by-side images of identical size. They must be adjacent to each other with no space between. The top-left position of the left image must be at the top-left corner of the file. The image on the left side is the normal image for the thumb image, and the image in the middle depicts the pushed state and the image on the right depicts the disabled state.


```C++
SeekThumb.bmp

```



You may want to make certain areas of the thumb image transparent. This will allow you to create thumb images in shapes other than rectangular. Any region of the thumb image that you fill with the color specified by the RGB value 255, 0, 255 will appear transparent in your skin.

## Related topics

<dl> <dt>

[**Trackbars**](trackbars.md)
</dt> </dl>

 

 




