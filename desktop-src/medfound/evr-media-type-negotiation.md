---
description: EVR Media Type Negotiation
ms.assetid: 3a12b80d-7aac-437d-b515-aab37c1e81b2
title: EVR Media Type Negotiation
ms.topic: reference
ms.date: 05/31/2018
---

# EVR Media Type Negotiation

[The component described on this page, [Enhanced Video Renderer](/windows/win32/medfound/enhanced-video-renderer), is a legacy feature. It has been superseded by the Simple Video Renderer (SVR) exposed through the [MediaPlayer](/uwp/api/windows.media.playback.mediaplayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine) components. To play video content you should send data into one of these components and allow them to instantiate the new video renderer.  These components have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** or the lower level **IMFMediaEngine** APIs to play video media in Windows instead of the EVR, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.]


This topic describes how the enhanced video renderer (EVR) validates media types.

-   For the DirectShow EVR filter, type negotiation occurs when the filter's pins are connected.

-   For the EVR media sink, the media types are set through the [**IMFMediaTypeHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfmediatypehandler) interface on the stream sinks. Typically the topology loader negotiates the media types, although the application can also set the media types directly.

The EVR does not report any preferred media types. The client must test media types until it finds an acceptable type. The media type for the reference stream must be set before the types can be set on any of the substreams.

For the reference stream, the EVR mixer gets a list of compatible DirectX Video Acceleration (DXVA) render target formats. The EVR presenter uses this list to select the format for the Direct3D swap chain. If no compatible render target format can be found, the EVR rejects the media type.

For the substreams, the EVR mixer queries whether the DXVA device supports that substream format in combination with the render target format that was selected for the reference stream. As a result, the available substream formats might change depending on the reference stream.

Here is the process in more detail. These details are not important for most applications, but might be helpful if you are writing a custom mixer or presenter.

For the reference stream, negotiation happens as follows:

1.  The EVR calls [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) on the mixer.

2.  The mixer converts the media type to a DXVA 2.0 description, using the [**DXVA2\_VideoDesc**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_videodesc) structure.

3.  The mixer calls [**IDirectXVideoProcessorService::GetVideoProcessorDeviceGuids**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideoprocessorservice-getvideoprocessordeviceguids) to get a list of video processor GUIDs.

4.  For each video processor GUID, the mixer calls [**IDirectXVideoProcessorService::GetVideoProcessorRenderTargets**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideoprocessorservice-getvideoprocessorrendertargets) to get the supported render target formats.

5.  The EVR calls [**IMFVideoPresenter::ProcessMessage**](/windows/desktop/api/evr/nf-evr-imfvideopresenter-processmessage) on the presenter with the MFVP\_MESSAGE\_INVALIDATEMEDIATYPE message. This message causes the presenter to select a new format.

6.  The presenter calls [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) to get a list of available output formats from the mixer. The mixer generates this list from the formats obtained in step 4.

7.  The presenter selects a format and calls [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) on the mixer.

For substreams, the process is simpler:

1.  The EVR calls [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) on the mixer.

2.  The mixer calls [**IDirectXVideoProcessorService::GetVideoProcessorSubStreamFormats**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideoprocessorservice-getvideoprocessorsubstreamformats) to get a list of available substream formats.

3.  If the proposed format is contained in this list, the EVR accepts the input type.

## Related topics

<dl> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 



