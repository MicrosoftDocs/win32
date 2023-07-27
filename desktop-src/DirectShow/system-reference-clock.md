---
description: System Reference Clock
ms.assetid: 0247dcb9-64ee-4562-944a-44bcfae80f2d
title: System Reference Clock
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# System Reference Clock

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The System Reference Clock object implements a reference clock that returns the system time. If none of the filters in the graph provides a reference clock, the filter graph manager uses this component to synchronize the graph. Create this object by calling **CoCreateInstance**.



| Label | Value |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Class Identifier | CLSID\_SystemClock                                                                                                                                       |
| Interfaces       | [**IAMClockAdjust**](/windows/desktop/api/Strmif/nn-strmif-iamclockadjust), [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock), [**IReferenceClockTimerControl**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclocktimercontrol) |



 

## Related topics

<dl> <dt>

[DirectShow Objects](directshow-objects.md)
</dt> <dt>

[Reference Clocks](reference-clocks.md)
</dt> <dt>

[Time and Clocks in DirectShow](time-and-clocks-in-directshow.md)
</dt> </dl>

 

 



