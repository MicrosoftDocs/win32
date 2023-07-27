---
description: Memory Allocator
ms.assetid: 2dc055a2-b77a-443d-b602-d9636cbe4db3
title: Memory Allocator
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Memory Allocator

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Memory Allocator object allocates buffers for media samples. Filters can use this object to allocate shared memory buffers; however, a filter with special requirements can also implement its own memory allocator object. Create this object by calling **CoCreateInstance**.



| Label | Value |
|------------------|----------------------------------------|
| Class Identifier | CLSID\_MemoryAllocator                 |
| Interfaces       | [**IMemAllocator**](/windows/desktop/api/Strmif/nn-strmif-imemallocator) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> </dl>

 

 



