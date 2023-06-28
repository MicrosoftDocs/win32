---
title: Sample Trackbars Section
description: Sample Trackbars Section
ms.assetid: b336a034-12ad-480e-8ec8-9c6d2bd9196f
keywords:
- Windows Media Player Mobile skins,trackbars
- skins,trackbars
- reference for skins,trackbars
- trackbars in skins,Trackbars section
- skin definition files,Trackbars section
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Sample Trackbars Section

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following lines show a typical Trackbars section of a skin definition file:


```C++
[ Trackbars ]

//  <Type>      <Location>     <Dis Image Src>  <Thumb Image Src>  <Thumb Size>
//  ----------  ----------     ---------------  -----------------  ------------
    Seek      32,220,172,23  Disabled @ 32,27    SeekThumb.bmp    23,22

```



The preceding example defines a trackbar that allows the user to seek through a media item by tapping and dragging the SeekThumb image.

## Related topics

<dl> <dt>

[**Trackbars**](trackbars.md)
</dt> </dl>

 

 




