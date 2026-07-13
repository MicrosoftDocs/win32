---
description: The samplingrate attribute specifies the sampling rate of the output audio, in Hz.
ms.assetid: d053285c-bf94-465a-99d3-bed7c2d09b1a
title: samplingrate Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# samplingrate Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `samplingrate` attribute specifies the sampling rate of the output audio, in Hz.

## Possible Values

The value must be 8000, 11025, 22050, 32000, 44100, or 48000. The default value is 44100.

## Applies To

[**group**](group-element.md)

## Remarks

Set this attribute only if the **type** attribute is `audio`.

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> </dl>

 

 



