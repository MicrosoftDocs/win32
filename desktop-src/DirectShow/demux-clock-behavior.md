---
description: Demux Clock Behavior
ms.assetid: c8a067f7-4e4c-4f25-b26c-f6bb048060b0
title: Demux Clock Behavior
ms.topic: article
ms.date: 05/31/2018
---

# Demux Clock Behavior

In push mode, the MPEG-2 Demultiplexer (demux) exposes the [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock) interface. It acts as a live source, so it will be chosen as the graph reference clock by default; see [Live Sources](live-sources.md) for more information.

-   For transport streams, the demux synchronizes its clock to the PCR stream that corresponds to the audio or video stream most recently mapped by the application. Internally, the demux tracks the PAT and PMT tables. When the application maps an elementary stream PID to an output pin, the demux looks up the PCR stream for that PID and uses that PCR stream. (Currently, there is not way for the application to specify the PCR PID directly.)
-   For program streams, the demux synchronizes its clock to the SCR stream.

Synchronizing the filter clock to the PCR or SCR stream prevents data overflow or underflow, which could result if the graph clock varied from the stream clock. The demux also translates PES PTS values into DirectShow reference times, and uses these values to time stamp the media samples. The time stamps apply to the next frame boundary; there is no guarantee that the frame boundary will align with the start of the media sample.

The demux guarantees that the time stamps increase monotonically. This means, for example, that if a transport stream includes a segment such as a commercial that was created with a different clock than the main program, the demux will adjust the presentation time stamps to hide the time discontinuity from downstream filters.

## Related topics

<dl> <dt>

[Using the MPEG-2 Demultiplexer](using-the-mpeg-2-demultiplexer.md)
</dt> </dl>

 

 



