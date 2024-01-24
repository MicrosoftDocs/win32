---
description: Effect
ms.assetid: '5674901e-6646-4243-8ef9-5784ceae4bdb'
title: Effect
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Effect

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The effect object produces a video or audio effect. To create this object, call the [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) method.

The effect object exposes the following interfaces:

-   [**IAMTimelineEffect**](iamtimelineeffect.md)
-   [**IAMTimelineObj**](iamtimelineobj.md)
-   [**IAMTimelineSplittable**](iamtimelinesplittable.md)
-   **IPropertyPage**

## Related topics

<dl> <dt>

[The Timeline Model](the-timeline-model.md)
</dt> <dt>

[Working with Effects and Transitions](working-with-effects-and-transitions.md)
</dt> </dl>

 

 



