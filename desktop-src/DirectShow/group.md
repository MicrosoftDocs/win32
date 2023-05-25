---
description: Group
ms.assetid: d1391664-df1d-4b2f-9625-d3be09cc1110
title: Group (DirectShow)
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Group (DirectShow)

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The group object represents a top-level composition. Each group defines one video or audio stream in the final project. To create this object, call the [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) method.

The group object exposes the following interfaces:

-   [**IAMTimelineComp**](iamtimelinecomp.md)
-   [**IAMTimelineGroup**](iamtimelinegroup.md)
-   [**IAMTimelineObj**](iamtimelineobj.md)

## Related topics

<dl> <dt>

[The Timeline Model](the-timeline-model.md)
</dt> <dt>

[Constructing a Timeline](constructing-a-timeline.md)
</dt> </dl>

 

 



