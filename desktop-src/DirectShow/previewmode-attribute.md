---
description: The previewmode attribute specifies the preview mode for the group. If the value is TRUE, frames might be dropped during preview. Otherwise, no frames are dropped during preview. The default value is TRUE.
ms.assetid: 5e4f4407-b43e-4b31-8676-1e12b6b70034
title: previewmode Attribute
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# previewmode Attribute

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `previewmode` attribute specifies the preview mode for the group. If the value is **TRUE**, frames might be dropped during preview. Otherwise, no frames are dropped during preview. The default value is **TRUE**.

## Possible Values

The following values are defined as TRUE: y, Y, t, T, 1. The following values are defined as FALSE: n, N, f, F, 0 (zero).

## Applies To

[**group**](group-element.md)

## Remarks

Under the default setting, frames are dropped while previewing slow effects or transitions, to keep the video synchronized with the audio. The video might look choppy as a result. Setting this attribute to **FALSE** forces every frame to render during preview, possibly resulting in the video becoming out of sync with the audio. Frames are never dropped when writing to a file.

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineGroup::SetPreviewMode**](iamtimelinegroup-setpreviewmode.md)
</dt> </dl>

 

 



