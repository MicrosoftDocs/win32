---
description: DirectShow Objects
ms.assetid: 4b5068b5-4af9-40cb-b5a2-c9761ef13c55
title: DirectShow Objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DirectShow Objects

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This topic contains reference entries for the core COM objects included with DirectShow, other than filters. For a list of filters included with DirectShow, see [DirectShow Filters](directshow-filters.md).



| Object                                                   | Description                                                      |
|----------------------------------------------------------|------------------------------------------------------------------|
| [Capture Graph Builder](capture-graph-builder.md)       | Builds video capture graphs.                                     |
| [DVD Graph Builder](dvd-graph-builder.md)               | Builds DVD playback graphs.                                      |
| [Filter Graph Manager](filter-graph-manager.md)         | Builds and controls filter graphs.                               |
| [Filter Mapper](filter-mapper.md)                       | Searches the registry for registered filters.                    |
| [Media Property Bag](media-property-bag.md)             | Sets or retrieves INFO and DISP chunks in AVI files.             |
| [Memory Allocator](memory-allocator.md)                 | Allocates buffers for media samples.                             |
| [System Reference Clock](system-reference-clock.md)     | Implements a reference clock.                                    |
| [System Device Enumerator](system-device-enumerator.md) | Enumerates filters and hardware devices installed on the system. |



 

## Related topics

<dl> <dt>

[DirectShow Reference](directshow-reference.md)
</dt> </dl>

 

 



