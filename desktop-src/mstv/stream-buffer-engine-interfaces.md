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
| [**IEnumStreamBufferRecordingAttrib**](ienumstreambufferrecordingattrib.md) | Enumerates a collection of attributes on a stream buffer file.                                                                                                                                                      |
| [**ISBE2Crossbar**](isbe2crossbar.md)                                       | Implements crossbars (managers that handle enumerations and profiles for mapping streams to output pins) for a Stream Buffer Engine, version 2 (SBE2) [Stream Buffer Source](stream-buffer-sink-filter.md) filter. |
| [**ISBE2EnumStream**](isbe2enumstream.md)                                   | Enumerates streams mapped to output pins on an SBE2 [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                 |
| [**ISBE2FileScan**](isbe2filescan.md)                                       | Repairs a corrupted WTV file.                                                                                                                                                                                       |
| [**ISBE2GlobalEvent**](isbe2globalevent.md)                                 | Gets global events and their data from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                            |
| [**ISBE2GlobalEvent2**](isbe2globalevent2.md)                               | Extend the [**ISBE2GlobalEvent**](isbe2globalevent.md) interface.                                                                                                                                                  |
| [**ISBE2MediaTypeProfile**](isbe2mediatypeprofile.md)                       | Implements a media type profile, which describes a set of streams and their media types, for a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                      |
| [**ISBE2StreamMap**](isbe2streammap.md)                                     | Handles mapping between output pins and streams from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                              |
| [**ISBE2SpanningEvent**](isbe2spanningevent.md)                             | Gets spanning events and their data from a [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                          |
| [**IStreamBufferConfigure**](istreambufferconfigure.md)                     | Configures the location, number, and size of the backing files used by the various stream buffer objects.                                                                                                           |
| [**IStreamBufferConfigure2**](istreambufferconfigure2.md)                   | Extends the [**IStreamBufferConfigure**](istreambufferconfigure.md) interface.                                                                                                                                     |
| [**IStreamBufferConfigure3**](istreambufferconfigure3.md)                   | Extends the [**IStreamBufferConfigure2**](istreambufferconfigure2.md) interface.                                                                                                                                   |
| [**IStreamBufferDataCounters**](istreambufferdatacounters.md)               | Returns performance statistics.                                                                                                                                                                                     |
| [**IStreamBufferInitialize**](istreambufferinitialize.md)                   | Configures the stream buffer filters.                                                                                                                                                                               |
| [**IStreamBufferMediaSeeking**](istreambuffermediaseeking.md)               | Controls seeking in a stream buffer source graph.                                                                                                                                                                   |
| [**IStreamBufferMediaSeeking2**](istreambuffermediaseeking2.md)             | Controls the frame rate during fast-forward play ("trick mode").                                                                                                                                                    |
| [**IStreamBufferRecComp**](istreambufferreccomp.md)                         | Creates new content recordings by concatenating existing recordings.                                                                                                                                                |
| [**IStreamBufferRecordControl**](istreambufferrecordcontrol.md)             | Controls [Recording](recording-object.md) objects                                                                                                                                                                  |
| [**IStreamBufferRecordingAttribute**](istreambufferrecordingattribute.md)   | Sets and retrieves attributes on a stream buffer recording.                                                                                                                                                         |
| [**IStreamBufferSink**](istreambuffersink.md)                               | Controls the [Stream Buffer Sink](stream-buffer-sink-filter.md) filter.                                                                                                                                            |
| [**IStreamBufferSink2**](istreambuffersink2.md)                             | Extends the [**IStreamBufferSink**](istreambuffersink.md) interface.                                                                                                                                               |
| [**IStreamBufferSink3**](istreambuffersink3.md)                             | Extends the [**IStreamBufferSink2**](istreambuffersink2.md) interface.                                                                                                                                             |
| [**IStreamBufferSource**](istreambuffersource.md)                           | Controls the [Stream Buffer Source](stream-buffer-source-filter.md) filter.                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Stream Buffer Engine Reference](stream-buffer-engine-reference.md)
</dt> </dl>

 

 




