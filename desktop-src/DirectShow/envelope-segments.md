---
description: Envelope Segments
ms.assetid: 1b59cd1c-7c37-4c70-a36c-2ee1f42b42c5
title: Envelope Segments
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Envelope Segments

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A parameter curve consists of one or more envelope segments, defined using the [**MP\_ENVELOPE\_SEGMENT**](/previous-versions/windows/desktop/api/Medparam/ns-medparam-mp_envelope_segment) structure. This structure contains the following information:

-   The start and end times.
-   The starting and ending values.
-   The curve type (linear, square, and so forth).
-   Optional flags, described shortly.

The client adds envelope segments to a parameter by calling the [**IMediaParams::AddEnvelope**](/previous-versions/windows/desktop/api/Medparam/nf-medparam-imediaparams-addenvelope) method and passing in an array of **MP\_ENVELOPE\_SEGMENT** structures. The client should sort the segments into ascending time order before calling the method. As the DMO processes data, you can imagine the parameter traveling over each envelope segment, like a car driving over a series of hills. The [**IMediaParams::GetParam**](/previous-versions/windows/desktop/api/Medparam/nf-medparam-imediaparams-getparam) method returns the most recent value.

Two adjacent segments can have a gap between them. During gaps, the parameter retains its previous value, as follows:

-   Before the first segment, the value is the neutral value.
-   Between segments, the value is the ending value of the previous segment.
-   After the last segment, the value remains at the ending value of that segment.
-   If the client flushes the DMO, the value reverts to the neutral value.

You can alter a segment by setting either of the following flags:

-   MPF\_ENVLP\_BEGIN\_CURRENTVAL. The DMO uses the most recent value of the parameter as the starting value for the segment. This might be the neutral value, or the ending value from the previous segment. The DMO ignores the **valStart** member of the **MP\_ENVELOPE\_SEGMENT** structure.
-   MPF\_ENVLP\_BEGIN\_NEUTRALVAL. The DMO uses the neutral value of the parameter as the starting value for the segment. It ignores **valStart**.

You can think of these flags as grabbing the starting point of the segment and moving it up or down, while the ending value remains fixed. The segment will "stretch" accordingly.

## Related topics

<dl> <dt>

[Media Parameters](media-parameters.md)
</dt> </dl>

 

 



