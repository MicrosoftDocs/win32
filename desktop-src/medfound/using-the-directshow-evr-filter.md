---
Description: Using the DirectShow EVR Filter
ms.assetid: 4d85aed0-4b11-4c5f-bfc0-cad0a7d2f490
title: Using the DirectShow EVR Filter
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the DirectShow EVR Filter

To create the enhanced video renderer (EVR) filter, call **CoCreateInstance**. The CLSID is CLSID\_EnhancedVideoRenderer, defined in uuids.h. You do not have to call [**MFStartup**](/windows/win32/mfapi/nf-mfapi-mfstartup?branch=master) or [**MFShutdown**](/windows/win32/mfapi/nf-mfapi-mfshutdown?branch=master) to use the EVR filter.

For more information about using the EVR filter in a DirectShow application, see [Audio/Video Playback in DirectShow](dshow.audio_video_playback_in_directshow).

The EVR filter starts with one input pin, which corresponds to the reference stream. To add pins for substreams, query the filter for the [**IEVRFilterConfig**](/windows/win32/evr/nn-evr-ievrfilterconfig?branch=master) interface and call [**IEVRFilterConfig::SetNumberOfStreams**](/windows/win32/evr/nf-evr-ievrfilterconfig-setnumberofstreams?branch=master). Call this method before connecting any input pins. Pin 0 is always the reference stream. Connect this pin before any other pins, because the format of the reference stream might limit which substream formats are available.

Before starting the graph, set the video clipping window and the destination rectangle. For more information, see [Using the Video Display Controls](using-the-video-display-controls.md).

Unlike the Video Mixing Renderer (VMR), the EVR does not have operational modes (windowed, windowless, and so forth). In particular:

-   The EVR does not support windowed mode. The application must provide the clipping window.
-   The EVR does not have a renderless mode. To replace the default presenter, call [**IMFVideoRenderer::InitializeRenderer**](/windows/win32/evr/nf-evr-imfvideorenderer-initializerenderer?branch=master).
-   The EVR does not have a mixing mode. The EVR always creates the mixer. If you have one input stream, it is not necessary to call [**SetNumberOfStreams**](/windows/win32/evr/nf-evr-ievrfilterconfig-setnumberofstreams?branch=master) to force the EVR to use the mixer.

## Filter Interfaces

The EVR filter exposes the following interfaces. Some of these interfaces are documented in the DirectShow SDK. Use **QueryInterface** to retrieve pointers to these interfaces:

-   [**IAMCertifiedOutputProtection**](dshow.iamcertifiedoutputprotection) (DirectShow)
-   [**IAMFilterMiscFlags**](dshow.iamfiltermiscflags) (DirectShow)
-   [**IBaseFilter**](dshow.ibasefilter) (DirectShow)
-   [**IEVRFilterConfig**](/windows/win32/evr/nn-evr-ievrfilterconfig?branch=master)
-   [**IKsPropertySet**](dshow.ikspropertyset) (DirectShow)
-   [**IMediaEventSink**](dshow.imediaeventsink) (DirectShow)
-   [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master)
-   [**IMFVideoPositionMapper**](/windows/win32/evr/nn-evr-imfvideopositionmapper?branch=master)
-   [**IMFVideoRenderer**](/windows/win32/evr/nn-evr-imfvideorenderer?branch=master)
-   **IPersistStream**
-   [**IQualityControl**](dshow.iqualitycontrol) (DirectShow)
-   [**IQualProp**](dshow.iqualprop) (DirectShow)
-   **ISpecifyPropertyPages**

## Input Pin Interfaces

The input pins on the EVR filter expose the following interfaces. Use **QueryInterface** to retrieve pointers to these interfaces:

-   [**IEVRVideoStreamControl**](/windows/win32/evr9/nn-evr9-ievrvideostreamcontrol?branch=master)
-   [**IMemInputPin**](dshow.imeminputpin) (DirectShow)
-   [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master)
-   [**IPin**](dshow.ipin) (DirectShow)
-   [**IQualityControl**](dshow.iqualitycontrol) (DirectShow)

In addition, you can use the [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master) interface to retrieve the following interface:

-   [**IDirectXVideoMemoryConfiguration**](/windows/win32/dxva2api/nn-dxva2api-idirectxvideomemoryconfiguration?branch=master)

## Related topics

<dl> <dt>

[Audio/Video Playback in DirectShow](dshow.audio_video_playback_in_directshow)
</dt> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 



