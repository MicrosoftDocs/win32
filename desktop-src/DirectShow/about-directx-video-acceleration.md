---
description: About DirectX Video Acceleration
ms.assetid: 50f402e5-7e85-4e80-ad72-9c3887efcd10
title: About DirectX Video Acceleration
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About DirectX Video Acceleration

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectX VA describes an Application Programming Interface (API) and a corresponding Device Driver Interface (DDI) for hardware acceleration of digital video decoding processing, with support of alpha blending for such purposes as DVD subpicture support. It provides an interface definition focused on support of MPEG-2 "main profile" video (formally ITU-T H.262 \| ISO/IEC 13818-2), but is also intended to support other key video codecs (for example, ITU-T Recommendations H.263 and H.261, and MPEG-1 and MPEG-4). DirectX VA also specifies how device drivers can implement de-interlacing and frame rate conversion operations.

> [!Note]  
> The DirectX VA specification is now located in the Microsoft Platform DDK. Developers of software decoders as well as device drivers should refer to that specification.

 

## Related topics

<dl> <dt>

[Decoder Interfaces and Specifications](decoder-interfaces-and-specifications.md)
</dt> </dl>

 

 



