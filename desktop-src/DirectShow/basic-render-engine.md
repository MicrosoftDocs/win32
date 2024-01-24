---
description: Basic Render Engine
ms.assetid: 0a4fcf2a-dbad-4211-9a85-7741c8dfc95e
title: Basic Render Engine
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Basic Render Engine

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Basic Render Engine object renders uncompressed output from a timeline. To create this object, call **CoCreateInstance**. For compressed output, use the Smart Render Engine. The class identifier is CLSID\_RenderEngine.

The Basic Render Engine exposes the following interfaces:

-   [**IAMSetErrorLog**](iamseterrorlog.md)
-   IObjectWithSite
-   [**IRenderEngine**](irenderengine.md)
-   [**IRenderEngine2**](irenderengine2.md)

## Related topics

<dl> <dt>

[Rendering a Project](rendering-a-project.md)
</dt> <dt>

[Smart Render Engine](smart-render-engine.md)
</dt> </dl>

 

 



