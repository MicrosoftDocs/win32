---
description: Access to DirectDraw Surfaces
ms.assetid: 21002c9f-8b8b-49f3-9ea3-3703780e3412
title: Access to DirectDraw Surfaces
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Access to DirectDraw Surfaces

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Media Sample objects provided by the VMR to upstream filters support the [**IVMRSurface**](/windows/desktop/api/Strmif/nn-strmif-ivmrsurface) interface. To obtain the interface, call QueryInterface on the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface and specify IID\_IVMRSurface. Upstream filters can then use the IVMRSurface methods to access and manipulate the surface that has been created by the VMR.

## Related topics

<dl> <dt>

[Using the VMR for DirectShow Filter Developers](using-the-vmr-for-directshow-filter-developers.md)
</dt> </dl>

 

 



