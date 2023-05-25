---
title: Video (Windows Media Player SDK)
description: Video
ms.assetid: '3c654494-19b5-401e-bed8-02f7cc7d7f4e'
keywords:
- Windows Media Player Mobile skins,video
- skins,video
- reference for skins,video
- video in skins,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video (Windows Media Player SDK)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A video display allows the user to view digital video files. The video display area is only visible when video is playing or paused. When you design your skin, you will want to reserve space in the Background image to contain the video display. If you don't, the video display may superimpose itself over any visible art, such as the Background file, buttons, and trackbars, which will keep the user from operating the controls on your skin.

The Video section of the skin definition file must begin with this line:


```C++
[ Video ]

```



You then must add a line that specifies the location and size of the video display area in your skin.


```C++
0,38,240,172

```



You can use the following template for the Video section of your skin definition file:


```C++
//  <Location>
//  ----------

```



The following sections provide further details.

-   [Video Location](video-location.md)
-   [Video Image Source](video-image-source.md)
-   [Video Size](video-size.md)
-   [Sample Video Section](sample-video-section.md)

## Related topics

<dl> <dt>

[**Skin Reference**](skin-reference.md)
</dt> </dl>

 

 




