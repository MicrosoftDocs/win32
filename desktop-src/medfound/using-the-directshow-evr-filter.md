---
Description: Using the DirectShow EVR Filter
ms.assetid: '4d85aed0-4b11-4c5f-bfc0-cad0a7d2f490'
title: Using the DirectShow EVR Filter
---

# Using the DirectShow EVR Filter

To create the enhanced video renderer (EVR) filter, call **CoCreateInstance**. The CLSID is CLSID\_EnhancedVideoRenderer, defined in uuids.h. You do not have to call [**MFStartup**](mfstartup.md) or [**MFShutdown**](mfshutdown.md) to use the EVR filter.

For more information about using the EVR filter in a DirectShow application, see [Audio/Video Playback in DirectShow](dshow.audio_video_playback_in_directshow).

The EVR filter starts with one input pin, which corresponds to the reference stream. To add pins for substreams, query the filter for the [**IEVRFilterConfig**](ievrfilterconfig.md) interface and call [**IEVRFilterConfig::SetNumberOfStreams**](ievrfilterconfig-setnumberofstreams.md). Call this method before connecting any input pins. Pin 0 is always the reference stream. Connect this pin before any other pins, because the format of the reference stream might limit which substream formats are available.

Before starting the graph, set the video clipping window and the destination rectangle. For more information, see [Using the Video Display Controls](using-the-video-display-controls.md).

Unlike the Video Mixing Renderer (VMR), the EVR does not have operational modes (windowed, windowless, and so forth). In particular:

-   The EVR does not support windowed mode. The application must provide the clipping window.
-   The EVR does not have a renderless mode. To replace the default presenter, call [**IMFVideoRenderer::InitializeRenderer**](imfvideorenderer-initializerenderer.md).
-   The EVR does not have a mixing mode. The EVR always creates the mixer. If you have one input stream, it is not necessary to call [**SetNumberOfStreams**](ievrfilterconfig-setnumberofstreams.md) to force the EVR to use the mixer.

## Filter Interfaces

The EVR filter exposes the following interfaces. Some of these interfaces are documented in the DirectShow SDK. Use **QueryInterface** to retrieve pointers to these interfaces:

-   [**IAMCertifiedOutputProtection**](dshow.iamcertifiedoutputprotection) (DirectShow)
-   [**IAMFilterMiscFlags**](dshow.iamfiltermiscflags) (DirectShow)
-   [**IBaseFilter**](dshow.ibasefilter) (DirectShow)
-   [**IEVRFilterConfig**](ievrfilterconfig.md)
-   [**IKsPropertySet**](dshow.ikspropertyset) (DirectShow)
-   [**IMediaEventSink**](dshow.imediaeventsink) (DirectShow)
-   [**IMFGetService**](imfgetservice.md)
-   [**IMFVideoPositionMapper**](imfvideopositionmapper.md)
-   [**IMFVideoRenderer**](imfvideorenderer.md)
-   **IPersistStream**
-   [**IQualityControl**](dshow.iqualitycontrol) (DirectShow)
-   [**IQualProp**](dshow.iqualprop) (DirectShow)
-   **ISpecifyPropertyPages**

## Input Pin Interfaces

The input pins on the EVR filter expose the following interfaces. Use **QueryInterface** to retrieve pointers to these interfaces:

-   [**IEVRVideoStreamControl**](ievrvideostreamcontrol.md)
-   [**IMemInputPin**](dshow.imeminputpin) (DirectShow)
-   [**IMFGetService**](imfgetservice.md)
-   [**IPin**](dshow.ipin) (DirectShow)
-   [**IQualityControl**](dshow.iqualitycontrol) (DirectShow)

In addition, you can use the [**IMFGetService**](imfgetservice.md) interface to retrieve the following interface:

-   [**IDirectXVideoMemoryConfiguration**](idirectxvideomemoryconfiguration.md)

## Related topics

<dl> <dt>

[Audio/Video Playback in DirectShow](dshow.audio_video_playback_in_directshow)
</dt> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 



