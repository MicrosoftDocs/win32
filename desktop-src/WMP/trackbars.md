---
title: Trackbars
description: Trackbars
ms.assetid: b9676697-c3ab-465c-8b50-eb784f53bb11
keywords:
- Windows Media Player Mobile skins,trackbars
- skins,trackbars
- reference for skins,trackbars
- trackbars in skins,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Trackbars

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A trackbar displays an image that changes in small increments. Trackbars are used for volume controls and playback position controls. You can use trackbars to display information about the current media item or to allow the user to change settings or playback position. For example, you can use a trackbar to enable the user to adjust the volume, and another trackbar that can show the user the current playback position. Trackbars have a thumb image that defines the current setting of the trackbar value.

The Trackbars section of the skin definition file must begin with this line:


```C++
[ Trackbars ]

```



You then must add one or more lines that contain information about each of the trackbars in your skin.


```C++
    Seek        5,25,226,17    Disabled @ 4,1      SeekThumb.bmp      18,17
    Volume      32,220,172,23  Disabled @ 32,27    VolumeThumb.bmp    23,22

```



You can use the following template for the Trackbars section of your skin definition file:


```C++
//  <Type> <Location>     <Dis Image Src> <Thumb Image Src> <Thumb Size>
//  ------ ----------     --------------- ----------------- ------------

```



You must use the following order for trackbar information for each line in the Trackbars section (each part of the line is required):

1.  [Trackbar Type](trackbar-type.md)
2.  [Trackbar Location](trackbar-location.md)
3.  [Image Source for Disabled Trackbar](image-source-for-disabled-trackbar.md)
4.  [Thumb Image Source](thumb-image-source.md)
5.  [Thumb Size](thumb-size.md)

For an example of Trackbars code, see [Sample Trackbars Section](sample-trackbars-section.md).

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




