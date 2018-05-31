---
title: Stream Buffer Engine Interfaces
description: Stream Buffer Engine Interfaces
ms.assetid: b3e8703a-2b69-4262-9aaa-ff9ac8ca2f28
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stream Buffer Engine Interfaces

Applications use the following interfaces for building Stream Buffer Engine graphs in addition to the base filter interfaces.



| Interface                                                                    | Description                                                                                                                                                                                                         |
|------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEnumStreamBufferRecordingAttrib**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-ienumstreambufferrecordingattrib) | Enumerates a collection of attributes on a stream buffer file.                                                                                                                                                      |
| [**ISBE2Crossbar**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2crossbar)                                       | Implements crossbars (managers that handle enumerations and profiles for mapping streams to output pins) for a Stream Buffer Engine, version 2 (SBE2) [Stream Buffer Source](stream-buffer-sink-filter.md) filter. |
| [**ISBE2EnumStream**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2enumstream)                                   | Enumerates streams mapped to output pins on an SBE2 [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                 |
| [**ISBE2FileScan**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2filescan)                                       | Repairs a corrupted WTV file.                                                                                                                                                                                       |
| [**ISBE2GlobalEvent**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2globalevent)                                 | Gets global events and their data from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                            |
| [**ISBE2GlobalEvent2**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2globalevent2)                               | Extend the [**ISBE2GlobalEvent**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2globalevent) interface.                                                                                                                                                  |
| [**ISBE2MediaTypeProfile**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2mediatypeprofile)                       | Implements a media type profile, which describes a set of streams and their media types, for a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                      |
| [**ISBE2StreamMap**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2streammap)                                     | Handles mapping between output pins and streams from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                              |
| [**ISBE2SpanningEvent**](/previous-versions/windows/desktop/api/sbe/nn-sbe-isbe2spanningevent)                             | Gets spanning events and their data from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                          |
| [**IStreamBufferConfigure**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferconfigure)                     | Configures the location, number, and size of the backing files used by the various stream buffer objects.                                                                                                           |
| [**IStreamBufferConfigure2**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferconfigure2)                   | Extends the [**IStreamBufferConfigure**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferconfigure) interface.                                                                                                                                     |
| [**IStreamBufferConfigure3**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferconfigure3)                   | Extends the [**IStreamBufferConfigure2**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferconfigure2) interface.                                                                                                                                   |
| [**IStreamBufferDataCounters**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferdatacounters)               | Returns performance statistics.                                                                                                                                                                                     |
| [**IStreamBufferInitialize**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferinitialize)                   | Configures the stream buffer filters.                                                                                                                                                                               |
| [**IStreamBufferMediaSeeking**](/previous-versions/windows/desktop/api/Sbe/)               | Controls seeking in a stream buffer source graph.                                                                                                                                                                   |
| [**IStreamBufferMediaSeeking2**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffermediaseeking2)             | Controls the frame rate during fast-forward play ("trick mode").                                                                                                                                                    |
| [**IStreamBufferRecComp**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferreccomp)                         | Creates new content recordings by concatenating existing recordings.                                                                                                                                                |
| [**IStreamBufferRecordControl**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferrecordcontrol)             | Controls [Recording](recording-object.md) objects                                                                                                                                                                  |
| [**IStreamBufferRecordingAttribute**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambufferrecordingattribute)   | Sets and retrieves attributes on a stream buffer recording.                                                                                                                                                         |
| [**IStreamBufferSink**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersink)                               | Controls the [Stream Buffer Sink](stream-buffer-sink-filter.md) filter.                                                                                                                                            |
| [**IStreamBufferSink2**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersink2)                             | Extends the [**IStreamBufferSink**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersink) interface.                                                                                                                                               |
| [**IStreamBufferSink3**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersink3)                             | Extends the [**IStreamBufferSink2**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersink2) interface.                                                                                                                                             |
| [**IStreamBufferSource**](/previous-versions/windows/desktop/api/Sbe/nn-sbe-istreambuffersource)                           | Controls the [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Stream Buffer Engine Reference](stream-buffer-engine-reference.md)
</dt> </dl>

 

 




