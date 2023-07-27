---
description: Media Locator
ms.assetid: 165d5f94-d3f1-45f4-9ceb-0adcd1e03da5
title: Media Locator
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media Locator

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Media Locator object locates the files associated with source objects. Use this object to validate sources in the timeline. To create this object, call **CoCreateInstance**. The class identifier is CLSID\_MediaLocator.

The Media Locator object exposes the following interface:

-   [**IMediaLocator**](imedialocator.md)

## Related topics

<dl> <dt>

[Working with Sources](working-with-sources.md)
</dt> </dl>

 

 



