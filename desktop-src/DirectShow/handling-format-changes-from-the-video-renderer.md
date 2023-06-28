---
description: Handling Format Changes from the Video Renderer
ms.assetid: ac7d7b1c-3c9a-4693-87ea-0a10a8ab915c
title: Handling Format Changes from the Video Renderer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Handling Format Changes from the Video Renderer

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section describes how a decoder filter or transform filter should handle format changes from the video renderer.

**Video Renderer Filter**

When the old [Video Renderer](video-renderer-filter.md) filter connects, it requires an RGB format that matches the display format of the primary monitor. This enables it to use GDI for rendering if DirectDraw is not available. When playback starts, the Video Renderer may switch to a DirectDraw-compatible format. To verfify whether the upstream filter can support the new format, the Video Renderer calls [**IPin::QueryAccept**](/windows/desktop/api/Strmif/nf-strmif-ipin-queryaccept) on the upstream filter's output pin. If the upstream filter accepts the new format, the **QueryAccept** method returns S\_OK. The Video Renderer switches formats by attaching a media type with the new format to the next media sample returned by its allocator. The upstream filter should check for format changes by calling [**IMediaSample::GetMediaType**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getmediatype) on each sample. The Video Renderer may switch back and forth between the original format and new format at any time during streaming. It does not call **QueryAccept** after the first format change. Once the upstream filter has accepted the new format, it must be able to switch back and forth.

The upstream filter can reject the format change by returning S\_FALSE from **QueryAccept**. In that case, the Video Renderer continues to use GDI with the original format.

**Video Mixing Renderer Filter**

The Video Mixing Renderer filter (VMR-7 and VMR-9) will connect with any format that is supported by the graphics hardware on the system. The VMR-7 always uses DirectDraw for rendering, and allocates the underlying DirectDraw surfaces when the upstream filter connects. The VMR-9 always uses Direct3D for rendering, and allocates the underlying Direct3D surfaces when the upstream filter connects.

The graphics hardware may require a larger surface stride than the image width. In that case, the VMR requests a new format by calling **QueryAccept**. It reports the surface stride in the **biWidth** member of the [**BITMAPINFOHEADER**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfoheader) in the video format. If the upstream filter does not return S\_OK from **QueryAccept**, the VMR rejects the format and tries to connect using the next format advertised by the upstream filter. The VMR attaches the media type with the new format to the first media sample. After the first sample, the format remains constant; the VMR will not switch formats while the graph is running.

**Enhanced Video Render (EVR)**

The EVR always uses Direct3D for rendering. If a larger surface stride is needed, the EVR uses the same **QueryAccept** mechanism as the VMR.

## Related topics

<dl> <dt>

[QueryAccept (Upstream)](queryaccept--upstream.md)
</dt> </dl>

 

 



