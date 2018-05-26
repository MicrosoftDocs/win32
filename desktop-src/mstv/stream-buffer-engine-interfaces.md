---
title: Stream Buffer Engine Interfaces
description: Stream Buffer Engine Interfaces
ms.assetid: b3e8703a-2b69-4262-9aaa-ff9ac8ca2f28
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Stream Buffer Engine Interfaces

Applications use the following interfaces for building Stream Buffer Engine graphs in addition to the base filter interfaces.



| Interface                                                                    | Description                                                                                                                                                                                                         |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumStreamBufferRecordingAttrib**](/windows/previous-versions/Sbe/nn-sbe-ienumstreambufferrecordingattrib?branch=master) | Enumerates a collection of attributes on a stream buffer file.                                                                                                                                                      |
| [**ISBE2Crossbar**](/windows/previous-versions/sbe/nn-sbe-isbe2crossbar?branch=master)                                       | Implements crossbars (managers that handle enumerations and profiles for mapping streams to output pins) for a Stream Buffer Engine, version 2 (SBE2) [Stream Buffer Source](stream-buffer-sink-filter.md) filter. |
| [**ISBE2EnumStream**](/windows/previous-versions/sbe/nn-sbe-isbe2enumstream?branch=master)                                   | Enumerates streams mapped to output pins on an SBE2 [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                 |
| [**ISBE2FileScan**](/windows/previous-versions/sbe/nn-sbe-isbe2filescan?branch=master)                                       | Repairs a corrupted WTV file.                                                                                                                                                                                       |
| [**ISBE2GlobalEvent**](/windows/previous-versions/sbe/nn-sbe-isbe2globalevent?branch=master)                                 | Gets global events and their data from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                            |
| [**ISBE2GlobalEvent2**](/windows/previous-versions/sbe/nn-sbe-isbe2globalevent2?branch=master)                               | Extend the [**ISBE2GlobalEvent**](/windows/previous-versions/sbe/nn-sbe-isbe2globalevent?branch=master) interface.                                                                                                                                                  |
| [**ISBE2MediaTypeProfile**](/windows/previous-versions/sbe/nn-sbe-isbe2mediatypeprofile?branch=master)                       | Implements a media type profile, which describes a set of streams and their media types, for a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                      |
| [**ISBE2StreamMap**](/windows/previous-versions/sbe/nn-sbe-isbe2streammap?branch=master)                                     | Handles mapping between output pins and streams from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                              |
| [**ISBE2SpanningEvent**](/windows/previous-versions/sbe/nn-sbe-isbe2spanningevent?branch=master)                             | Gets spanning events and their data from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                          |
| [**IStreamBufferConfigure**](/windows/previous-versions/Sbe/nn-sbe-istreambufferconfigure?branch=master)                     | Configures the location, number, and size of the backing files used by the various stream buffer objects.                                                                                                           |
| [**IStreamBufferConfigure2**](/windows/previous-versions/Sbe/nn-sbe-istreambufferconfigure2?branch=master)                   | Extends the [**IStreamBufferConfigure**](/windows/previous-versions/Sbe/nn-sbe-istreambufferconfigure?branch=master) interface.                                                                                                                                     |
| [**IStreamBufferConfigure3**](/windows/previous-versions/Sbe/nn-sbe-istreambufferconfigure3?branch=master)                   | Extends the [**IStreamBufferConfigure2**](/windows/previous-versions/Sbe/nn-sbe-istreambufferconfigure2?branch=master) interface.                                                                                                                                   |
| [**IStreamBufferDataCounters**](/windows/previous-versions/Sbe/nn-sbe-istreambufferdatacounters?branch=master)               | Returns performance statistics.                                                                                                                                                                                     |
| [**IStreamBufferInitialize**](/windows/previous-versions/Sbe/nn-sbe-istreambufferinitialize?branch=master)                   | Configures the stream buffer filters.                                                                                                                                                                               |
| [**IStreamBufferMediaSeeking**](/windows/previous-versions/Sbe/?branch=master)               | Controls seeking in a stream buffer source graph.                                                                                                                                                                   |
| [**IStreamBufferMediaSeeking2**](/windows/previous-versions/Sbe/nn-sbe-istreambuffermediaseeking2?branch=master)             | Controls the frame rate during fast-forward play ("trick mode").                                                                                                                                                    |
| [**IStreamBufferRecComp**](/windows/previous-versions/Sbe/nn-sbe-istreambufferreccomp?branch=master)                         | Creates new content recordings by concatenating existing recordings.                                                                                                                                                |
| [**IStreamBufferRecordControl**](/windows/previous-versions/Sbe/nn-sbe-istreambufferrecordcontrol?branch=master)             | Controls [Recording](recording-object.md) objects                                                                                                                                                                  |
| [**IStreamBufferRecordingAttribute**](/windows/previous-versions/Sbe/nn-sbe-istreambufferrecordingattribute?branch=master)   | Sets and retrieves attributes on a stream buffer recording.                                                                                                                                                         |
| [**IStreamBufferSink**](/windows/previous-versions/Sbe/nn-sbe-istreambuffersink?branch=master)                               | Controls the [Stream Buffer Sink](stream-buffer-sink-filter.md) filter.                                                                                                                                            |
| [**IStreamBufferSink2**](/windows/previous-versions/Sbe/nn-sbe-istreambuffersink2?branch=master)                             | Extends the [**IStreamBufferSink**](/windows/previous-versions/Sbe/nn-sbe-istreambuffersink?branch=master) interface.                                                                                                                                               |
| [**IStreamBufferSink3**](/windows/previous-versions/Sbe/nn-sbe-istreambuffersink3?branch=master)                             | Extends the [**IStreamBufferSink2**](/windows/previous-versions/Sbe/nn-sbe-istreambuffersink2?branch=master) interface.                                                                                                                                             |
| [**IStreamBufferSource**](/windows/previous-versions/Sbe/nn-sbe-istreambuffersource?branch=master)                           | Controls the [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Stream Buffer Engine Reference](stream-buffer-engine-reference.md)
</dt> </dl>

 

 




