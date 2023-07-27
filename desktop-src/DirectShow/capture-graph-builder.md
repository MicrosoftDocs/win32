---
description: Capture Graph Builder
ms.assetid: 'df59afcf-6e11-463f-80ac-8b1fcc496d5b'
title: Capture Graph Builder
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Capture Graph Builder

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Capture Graph Builder is a helper object for building video and audio capture graphs. Capture and editing applications can use this component to construct filter graphs. Create this object by calling **CoCreateInstance**.



| Label | Value |
|------------------|--------------------------------------------------------|
| Class Identifier | CLSID\_CaptureGraphBuilder2                            |
| Interfaces       | [**ICaptureGraphBuilder2**](/windows/desktop/api/Strmif/nn-strmif-icapturegraphbuilder2) |



 

## Related topics

<dl> <dt>

[Audio Capture](audio-capture.md)
</dt> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[Video Capture](video-capture.md)
</dt> </dl>

 

 



