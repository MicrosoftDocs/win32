---
description: The cutsonly attribute specifies whether a transition is rendered as a cut. If the value is TRUE, the transition is an instantaneous cut. Otherwise, the transition is rendered normally. The default value is FALSE.
ms.assetid: 810921fb-952b-42df-abda-7ef9a273a02d
title: cutsonly Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# cutsonly Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `cutsonly` attribute specifies whether a transition is rendered as a cut. If the value is **TRUE**, the transition is an instantaneous cut. Otherwise, the transition is rendered normally. The default value is **FALSE**.

## Possible Values

The following values are defined as TRUE: y, Y, t, T, 1. The following values are defined as FALSE: n, N, f, F, 0 (zero).

## Applies To

[**transition**](transition-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineTrans::SetCutPoint**](iamtimelinetrans-setcutpoint.md)
</dt> </dl>

 

 



