---
description: The timeline element defines the timeline. This element is the root node in the XML file.
ms.assetid: db1da09f-d9b2-43fa-8dec-e3dc11cbfafa
title: timeline Element (Windows.ui.xaml.media.animation.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- timeline
api_type: 
- HeaderDef
api_location: 
- windows.ui.xaml.media.animation.h
ms.custom: UpdateFrequency5
---

# timeline Element

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `timeline` element defines the timeline. This element is the root node in the XML file.

## Attributes

[**defaultfx**](defaultfx-attribute.md), [**defaulttrans**](defaulttrans-attribute.md), [**enablefx**](enablefx-attribute.md), [**enabletrans**](enabletrans-attribute.md), [**framerate**](framerate-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|-------------------------------------------------------|
| Parent   | None. This element must be the root node in the file. |
| Children | [**group**](group-element.md)                        |



 

## Examples


```XML
<timeline> </timeline>
```



## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Windows.ui.xaml.media.animation.h</dt> </dl> |



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 




