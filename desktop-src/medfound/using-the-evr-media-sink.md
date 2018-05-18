---
Description: Using the EVR Media Sink
ms.assetid: 'cd98266a-bc62-43da-b4d7-3561447d634f'
title: Using the EVR Media Sink
---

# Using the EVR Media Sink

The enhanced video renderer (EVR) media sink can be used as a stand-alone component. More often, however, an application will create the EVR media sink inside a topology, and then use the Media Session to control playback.

There are two ways to create the EVR media sink:

-   The [**MFCreateVideoRenderer**](mfcreatevideorenderer.md) function creates the media sink.

-   The [**MFCreateVideoRendererActivate**](mfcreatevideorendereractivate.md) function creates an activation object for the media sink.

The EVR media sink initially has one stream sink, which corresponds to the reference stream. To add new stream sinks, call [**IMFMediaSink::AddStreamSink**](imfmediasink-addstreamsink.md).

## Related topics

<dl> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> <dt>

[Media Sinks](media-sinks.md)
</dt> </dl>

 

 



