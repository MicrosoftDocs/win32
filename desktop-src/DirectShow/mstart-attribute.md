---
description: The mstart attribute specifies the start time of a clip, relative to the original media file.
ms.assetid: ed63f448-8ca3-4733-afc0-2d743f82bebe
title: mstart Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# mstart Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `mstart` attribute specifies the start time of a clip, relative to the original media file.

## Applies To

[**clip**](clip-element.md)

## Possible Values

Must be a string with the format *hh:mm:ss.ff* format, where *hh* = hours, *mm* = minutes, *ss* = seconds, and *ff* = fractions of seconds. Example: 1:04:30.512. Leading units can be omitted. For example, 3:00 (three minutes) and 45 (45 seconds) are both valid.

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineSrc::SetMediaTimes**](iamtimelinesrc-setmediatimes.md)
</dt> </dl>

 

 



