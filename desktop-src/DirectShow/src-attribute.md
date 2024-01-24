---
description: The src attribute specifies the path name of a media file. The file can be any type supported by DirectShow, or a still image. The supported formats for still images are bitmap, device-independent bitmap, GIF, and JPEG.
ms.assetid: 45476826-bde5-43b7-8102-30c94260740f
title: src Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# src Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `src` attribute specifies the path name of a media file. The file can be any type supported by DirectShow, or a still image. The supported formats for still images are bitmap, device-independent bitmap, GIF, and JPEG.

## Possible Values

Must be a string that specifies a path name.

## Applies To

[**clip**](clip-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineSrc::SetMediaName**](iamtimelinesrc-setmedianame.md)
</dt> </dl>

 

 



