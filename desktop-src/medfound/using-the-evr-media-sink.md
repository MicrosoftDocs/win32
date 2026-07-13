---
description: Using the EVR Media Sink
ms.assetid: cd98266a-bc62-43da-b4d7-3561447d634f
title: Using the EVR Media Sink
ms.topic: concept-article
ms.date: 05/31/2018
---

# Using the EVR Media Sink

[The component described on this page, [Enhanced Video Renderer](/windows/win32/medfound/enhanced-video-renderer), is a legacy feature. It has been superseded by the Simple Video Renderer (SVR) exposed through the [MediaPlayer](/uwp/api/windows.media.playback.mediaplayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine) components. To play video content you should send data into one of these components and allow them to instantiate the new video renderer.  These components have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** or the lower level **IMFMediaEngine** APIs to play video media in Windows instead of the EVR, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.]


The enhanced video renderer (EVR) media sink can be used as a stand-alone component. More often, however, an application will create the EVR media sink inside a topology, and then use the Media Session to control playback.

There are two ways to create the EVR media sink:

-   The [**MFCreateVideoRenderer**](/windows/desktop/api/evr/nc-evr-mfcreatevideorenderer) function creates the media sink.

-   The [**MFCreateVideoRendererActivate**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatevideorendereractivate) function creates an activation object for the media sink.

The EVR media sink initially has one stream sink, which corresponds to the reference stream. To add new stream sinks, call [**IMFMediaSink::AddStreamSink**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasink-addstreamsink).

## Related topics

<dl> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> <dt>

[Media Sinks](media-sinks.md)
</dt> </dl>

 

 



