---
description: New Segments
ms.assetid: 6c470b38-481f-4e52-93b8-eb6b343dcefc
title: New Segments
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# New Segments

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A *segment* is a group of media samples that share a common start time, stop time, and playback rate. The [**IPin::NewSegment**](/windows/desktop/api/Strmif/nf-strmif-ipin-newsegment) method signals the start of a new segment. It provides a way for a source filter to inform downstream filters that the time and rate information has changed. For example, if the source filter seeks to a new point in the stream, it calls **NewSegment** with the new start time.

Some downstream filters use the segment information when they process samples. For example, in a format that uses interframe compression, if the stop time falls on a delta frame, the source filter may need to send additional samples after the stop time. This enables the decoder to decode the final delta frame. To determine the correct final frame, the decoder refers to the segment stop time. As another example, audio renderers use the segment rate along with the audio sampling rate to generate the correct audio output.

In the push model, the source filter initiates the **NewSegment** call. In the pull model, this is done by the parser filter. In either case, the filter calls **NewSegment** on the downstream input pin, which propagates the call to the next filter, until the call reaches the renderer. Filters must serialize **NewSegment** calls with other streaming calls, such as [**IMemInputPin::Receive**](/windows/desktop/api/Strmif/nf-strmif-imeminputpin-receive).

Stream time resets to zero after each new segment. Time stamps on samples delivered after the segment start from zero.

 

 



