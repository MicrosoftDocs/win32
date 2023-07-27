---
description: Per-Pixel Alpha Blending
ms.assetid: 68661dc5-1423-47b2-a0df-858e5eb7f02b
title: Per-Pixel Alpha Blending
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Per-Pixel Alpha Blending

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Four media subtypes have been defined for per-pixel alpha blending. These subtypes are only supported when the VMR is in mixing mode. The VMR will reject the connection if it is not in mixing mode when an upstream filter attempts to connect using one of these subtypes. These subtypes are defined in uuids.h:

-   MEDIASUBTYPE\_ARGB1555
-   MEDIASUBTYPE\_ARGB4444
-   MEDIASUBTYPE\_ARGB32
-   MEDIASUBTYPE\_AYUV

For more information, see [Uncompressed RGB Video Subtypes](uncompressed-rgb-video-subtypes.md) and [**YUV Video Subtypes**](yuv-video-subtypes.md).

 

 



