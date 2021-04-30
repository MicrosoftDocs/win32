---
description: Using the DirectShow EVR Filter
ms.assetid: 4d85aed0-4b11-4c5f-bfc0-cad0a7d2f490
title: Using the DirectShow EVR Filter
ms.topic: article
ms.date: 05/31/2018
---

# Using the DirectShow EVR Filter

To create the enhanced video renderer (EVR) filter, call **CoCreateInstance**. The CLSID is CLSID\_EnhancedVideoRenderer, defined in uuids.h. You do not have to call [**MFStartup**](/windows/desktop/api/mfapi/nf-mfapi-mfstartup) or [**MFShutdown**](/windows/desktop/api/mfapi/nf-mfapi-mfshutdown) to use the EVR filter.

For more information about using the EVR filter in a DirectShow application, see [Audio/Video Playback in DirectShow](../directshow/audio-video-playback-in-directshow.md).

The EVR filter starts with one input pin, which corresponds to the reference stream. To add pins for substreams, query the filter for the [**IEVRFilterConfig**](/windows/desktop/api/evr/nn-evr-ievrfilterconfig) interface and call [**IEVRFilterConfig::SetNumberOfStreams**](/windows/desktop/api/evr/nf-evr-ievrfilterconfig-setnumberofstreams). Call this method before connecting any input pins. Pin 0 is always the reference stream. Connect this pin before any other pins, because the format of the reference stream might limit which substream formats are available.

Before starting the graph, set the video clipping window and the destination rectangle. For more information, see [Using the Video Display Controls](using-the-video-display-controls.md).

Unlike the Video Mixing Renderer (VMR), the EVR does not have operational modes (windowed, windowless, and so forth). In particular:

-   The EVR does not support windowed mode. The application must provide the clipping window.
-   The EVR does not have a renderless mode. To replace the default presenter, call [**IMFVideoRenderer::InitializeRenderer**](/windows/desktop/api/evr/nf-evr-imfvideorenderer-initializerenderer).
-   The EVR does not have a mixing mode. The EVR always creates the mixer. If you have one input stream, it is not necessary to call [**SetNumberOfStreams**](/windows/desktop/api/evr/nf-evr-ievrfilterconfig-setnumberofstreams) to force the EVR to use the mixer.

## Filter Interfaces

The EVR filter exposes the following interfaces. Some of these interfaces are documented in the DirectShow SDK. Use **QueryInterface** to retrieve pointers to these interfaces:

-   [**IAMCertifiedOutputProtection**](/windows/win32/api/strmif/nn-strmif-iamcertifiedoutputprotection) (DirectShow)
-   [**IAMFilterMiscFlags**](/windows/win32/api/strmif/nn-strmif-iamfiltermiscflags) (DirectShow)
-   [**IBaseFilter**](/windows/win32/api/strmif/nn-strmif-ibasefilter) (DirectShow)
-   [**IEVRFilterConfig**](/windows/desktop/api/evr/nn-evr-ievrfilterconfig)
-   [**IKsPropertySet**](../directshow/ikspropertyset.md) (DirectShow)
-   [**IMediaEventSink**](/windows/win32/api/strmif/nn-strmif-imediaeventsink) (DirectShow)
-   [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)
-   [**IMFVideoPositionMapper**](/windows/desktop/api/evr/nn-evr-imfvideopositionmapper)
-   [**IMFVideoRenderer**](/windows/desktop/api/evr/nn-evr-imfvideorenderer)
-   **IPersistStream**
-   [**IQualityControl**](/windows/win32/api/strmif/nn-strmif-iqualitycontrol) (DirectShow)
-   [**IQualProp**](/previous-versions/windows/desktop/api/amvideo/nn-amvideo-iqualprop) (DirectShow)
-   **ISpecifyPropertyPages**

## Input Pin Interfaces

The input pins on the EVR filter expose the following interfaces. Use **QueryInterface** to retrieve pointers to these interfaces:

-   [**IEVRVideoStreamControl**](/windows/desktop/api/evr9/nn-evr9-ievrvideostreamcontrol)
-   [**IMemInputPin**](/windows/win32/api/strmif/nn-strmif-imeminputpin) (DirectShow)
-   [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)
-   [**IPin**](/windows/win32/api/strmif/nn-strmif-ipin) (DirectShow)
-   [**IQualityControl**](/windows/win32/api/strmif/nn-strmif-iqualitycontrol) (DirectShow)

In addition, you can use the [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) interface to retrieve the following interface:

-   [**IDirectXVideoMemoryConfiguration**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideomemoryconfiguration)

## Related topics

<dl> <dt>

[Audio/Video Playback in DirectShow](../directshow/audio-video-playback-in-directshow.md)
</dt> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 
