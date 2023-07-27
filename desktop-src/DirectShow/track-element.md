---
description: The track element defines a track object.
ms.assetid: 5cc11f26-80b2-4548-af33-2fdf883e3189
title: track Element
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# track Element

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `track` element defines a track object.

## Attributes

[**lock**](lock-attribute.md), [**mute**](mute-attribute.md), [**userdata**](userdata-attribute.md), [**userid**](userid-attribute.md), [**username**](username-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|----------------------------------------------------------------------------------------------------------|
| Parent   | [**composite**](composite-element.md), [**group**](group-element.md)                                   |
| Children | [**clip**](clip-element.md), [**effect**](effect-element.md), [**transition**](transition-element.md) |



 

## Examples


```XML
<track> </track>
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



