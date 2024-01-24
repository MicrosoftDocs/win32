---
title: Video Size
description: Video Size
ms.assetid: 6ea16cd3-946d-4959-ab43-ddfe96467d1b
keywords:
- Windows Media Player Mobile skins,video
- skins,video
- reference for skins,video
- video in skins,size
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Video Size

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You can specify the size of the video display area up to the maximum size of the device display. However, such a large display area would cover all the controls your skin exposes, making them useless while video is playing. If the video display area is larger than the dimensions of the video that is playing, the video will be displayed at actual size and the unused portions of the video display will appear as a black border around the video image. If the video display area is smaller than the dimensions of the video that is playing, the video will still be displayed at actual size, but will appear centered and cropped within the available display area.

The following table shows recommended standard video display sizes.



| DPI | Width in pixels | Height in pixels |
|-----|-----------------|------------------|
| 96  | 208             | 160              |
| 192 | 516             | 320              |



 

The following table shows recommended minimum video display sizes.



| DPI | Width in pixels | Height in pixels |
|-----|-----------------|------------------|
| 96  | 160             | 120              |
| 192 | 320             | 240              |



 

## Related topics

<dl> <dt>

[**Video**](video.md)
</dt> </dl>

 

 




