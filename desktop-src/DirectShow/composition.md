---
description: Composition
ms.assetid: b5f607b2-9cca-4eef-9c63-d2015bd10469
title: Composition
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Composition

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The composition object is a container for tracks. It can also hold other compositions (for nesting of tracks), effects, and transitions. To create this object, call the [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) method.

The composition object exposes the following interfaces:

-   [**IAMTimelineComp**](iamtimelinecomp.md)
-   [**IAMTimelineEffectable**](iamtimelineeffectable.md)
-   [**IAMTimelineObj**](iamtimelineobj.md)
-   [**IAMTimelineTransable**](iamtimelinetransable.md)
-   [**IAMTimelineVirtualTrack**](iamtimelinevirtualtrack.md)

## Related topics

<dl> <dt>

[The Timeline Model](the-timeline-model.md)
</dt> <dt>

[Constructing a Timeline](constructing-a-timeline.md)
</dt> </dl>

 

 



