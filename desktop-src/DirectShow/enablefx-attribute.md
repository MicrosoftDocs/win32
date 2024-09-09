---
description: The enablefx attribute specifies whether effects are enabled. If the value is TRUE, the rendering engine renders effects. Otherwise, it does not. The default value is TRUE.
ms.assetid: 7ea09742-8dd3-431b-b07f-cf317fe11690
title: enablefx Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# enablefx Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `enablefx` attribute specifies whether effects are enabled. If the value is **TRUE**, the rendering engine renders effects. Otherwise, it does not. The default value is **TRUE**.

## Possible Values

The following values are defined as TRUE: y, Y, t, T, 1. The following values are defined as FALSE: n, N, f, F, 0 (zero).

## Applies To

[**timeline**](timeline-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimeline::EnableEffects**](iamtimeline-enableeffects.md)
</dt> </dl>

 

 



