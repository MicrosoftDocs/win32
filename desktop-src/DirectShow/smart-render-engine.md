---
description: Smart Render Engine
ms.assetid: 279be879-9728-4fa1-bdf7-6b48485fc75f
title: Smart Render Engine
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Smart Render Engine

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Smart Render Engine object renders compressed output from a timeline. To create this object, call **CoCreateInstance**. For uncompressed output, use the Basic Render Engine. The class identifier is CLSID\_SmartRenderEngine.

The Smart Render Engine exposes the following interfaces:

-   [**IAMSetErrorLog**](iamseterrorlog.md)
-   **IObjectWithSite**
-   [**IRenderEngine**](irenderengine.md)
-   [**IRenderEngine2**](irenderengine2.md)
-   [**ISmartRenderEngine**](ismartrenderengine.md)

## Related topics

<dl> <dt>

[Rendering a Project](rendering-a-project.md)
</dt> <dt>

[Basic Render Engine](basic-render-engine.md)
</dt> </dl>

 

 



