---
description: Media Property Bag
ms.assetid: 06678d57-c00b-4575-84e7-3d09f65f19ba
title: Media Property Bag
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Media Property Bag

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Media Property Bag object sets or retrieves INFO and DISP chunks in AVI files. Create this object by calling **CoCreateInstance**.



| Label | Value |
|------------------|------------------------------------------------|
| Class Identifier | CLSID\_MediaPropertyBag                        |
| Interfaces       | [**IMediaPropertyBag**](/windows/desktop/api/Strmif/nn-strmif-imediapropertybag) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[**IPersistMediaPropertyBag Interface**](/windows/desktop/api/Strmif/nn-strmif-ipersistmediapropertybag)
</dt> </dl>

 

 



