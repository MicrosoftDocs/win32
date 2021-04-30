---
description: Custom Mixers
ms.assetid: a0af318d-9ac2-43f9-8934-f28c472256a6
title: Custom Mixers
ms.topic: article
ms.date: 05/31/2018
---

# Custom Mixers

This topic describes how to write a custom mixer for the enhanced video renderer (EVR). You can use a custom mixer with either the Media Foundation EVR media sink, or the DirectShow EVR filter. For more information about mixers and presenters, see [Enhanced Video Renderer](enhanced-video-renderer.md).

The mixer is a Media Foundation transform (MFT) with one or more inputs (the reference stream plus the substreams) and one output. The input stream receives samples from upstream. The output stream delivers samples to the presenter. The EVR is responsible for calling [**IMFTransform::ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) on the mixer, and the presenter is responsible for calling [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput).

At a minimum, an EVR mixer must implement the following interfaces:



| Interface                                                                | Description                                                                                      |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**IMFTransform**](/windows/desktop/api/mftransform/nn-mftransform-imftransform)                                     | Provides base MFT functionality.                                                                 |
| [**IMFTopologyServiceLookupClient**](/windows/desktop/api/evr/nn-evr-imftopologyservicelookupclient) | Enables the mixer to get interfaces from the EVR.                                                |
| [**IMFVideoDeviceID**](/windows/desktop/api/evr/nn-evr-imfvideodeviceid)                             | Enables the mixer to get interfaces from the EVR.                                                |
| [**IMFAttributes**](/windows/desktop/api/mfobjects/nn-mfobjects-imfattributes)                                   | Used to expose the [**MF\_SA\_D3D\_AWARE**](mf-sa-d3d-aware-attribute.md) attribute to the EVR. |



 

Optionally, an MFT can implement any of the following interfaces:



| Interface                                                | Description                                                                                                                                          |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEVRTrustedVideoPlugin**](/windows/desktop/api/evr/nn-evr-ievrtrustedvideoplugin) | Required to play protected content.                                                                                                                  |
| [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)                   | Exposes interfaces such as [**IMFVideoMixerBitmap**](/windows/desktop/api/evr9/nn-evr9-imfvideomixerbitmap) and [**IMFVideoProcessor**](/windows/desktop/api/evr9/nn-evr9-imfvideoprocessor) to the application. |
| [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise)             | Enables the quality manager to adjust the video quality.                                                                                             |
| [**IMFVideoMixerBitmap**](/windows/desktop/api/evr9/nn-evr9-imfvideomixerbitmap)       | Enables the application to mix a static bitmap onto the video.                                                                                       |
| [**IMFVideoPositionMapper**](/windows/desktop/api/evr/nn-evr-imfvideopositionmapper) | Maps coordinates on the output video frame to coordinates on the input video frame.                                                                  |
| [**IMFVideoProcessor**](/windows/desktop/api/evr9/nn-evr9-imfvideoprocessor)           | Exposes some DXVA video processing features to the application.                                                                                      |



 

Format negotiation with the mixer works as follows:

1.  The EVR sets the media type on the reference stream.
2.  The EVR calls [**IMFVideoPresenter::ProcessMessage**](/windows/desktop/api/evr/nf-evr-imfvideopresenter-processmessage) on the presenter with the **MFVP\_MESSAGE\_INVALIDATEMEDIATYPE** message.

3.  The presenter sets the media type on the mixer's output stream.
4.  The EVR sets the media type on the substreams.

If the media type on the reference stream changes, the mixer's other media types are no longer valid. The mixer's [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method will then fail and return **MF\_E\_TRANSFORM\_STREAM\_CHANGE**. The presenter should not do anything at this point. The EVR will initiate the format negotiation process again.

When any input stream reaches the end of the stream, the EVR calls [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) on the mixer with [**MFT\_MESSAGE\_NOTIFY\_END\_OF\_STREAM**](mft-message-notify-end-of-stream.md).

The mixer sends the following events to the EVR, using the EVR's [**IMediaEventSink**](/windows/win32/api/strmif/nn-strmif-imediaeventsink) interface. This interface is documented in the DirectShow SDK documentation.



| Event                                            | Description                            |
|--------------------------------------------------|----------------------------------------|
| [**EC\_SAMPLE\_NEEDED**](../directshow/ec-sample-needed.md) | The mixer requires a new input sample. |



 

The EVR might call [**ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) on the mixer before streaming starts. The mixer should not fail these calls. Instead, it should fill the output surface with black pixels. The mixer should continue to color-fill output samples until it receives an [**MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING**](mft-message-notify-begin-streaming.md) message or the [**ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput) method is called. If the mixer receives an [**MFT\_MESSAGE\_NOTIFY\_END\_STREAMING**](mft-message-notify-end-streaming.md) message, it should switch back to color-fill mode.

## Implementing IMFVideoDeviceID

The [**IMFVideoDeviceID**](/windows/desktop/api/evr/nn-evr-imfvideodeviceid) interface contains one method, [**GetDeviceID**](/windows/desktop/api/evr/nf-evr-imfvideodeviceid-getdeviceid), which returns a device GUID. The device GUID ensures that the presenter and the mixer use compatible technologies. If the device GUIDs do not match, the EVR fails to initialize.

The standard mixer and presenter both use Direct3D 9, with the device GUID equal to IID\_IDirect3DDevice9. If you intend to use your custom presenter with the standard mixer, the presenter's device GUID must be IID\_IDirect3DDevice9. If you replace both components, you could define a new device GUID.

## Implementing IMFTopologyServiceLookupClient

The mixer must implement the [**IMFTopologyServiceLookupClient**](/windows/desktop/api/evr/nn-evr-imftopologyservicelookupclient) interface. Before streaming begins, the EVR calls [**IMFTopologyServiceLookupClient::InitServicePointers**](/windows/desktop/api/evr/nf-evr-imftopologyservicelookupclient-initservicepointers) and passes in a pointer to the EVR's [**IMFTopologyServiceLookup**](/windows/desktop/api/evr/nn-evr-imftopologyservicelookup) interface. The mixer uses this pointer to get interface pointers from the EVR.

At a minimum, the mixer must query for the following interface:

-   [**IMediaEventSink**](/windows/win32/api/strmif/nn-strmif-imediaeventsink)

When the EVR calls [**IMFTopologyServiceLookupClient::ReleaseServicePointers**](/windows/desktop/api/evr/nf-evr-imftopologyservicelookupclient-releaseservicepointers), the mixer must release any pointers obtained from the call to [**InitServicePointers**](/windows/desktop/api/evr/nf-evr-imftopologyservicelookupclient-initservicepointers).

## Mixer Attributes

A mixer should support the following attributes.



| Attribute                                                                        | Description                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_SA\_D3D\_AWARE**](mf-sa-d3d-aware-attribute.md)                          | Specifies whether the mixer supports DirectX Video Acceleration (DXVA).                                                                                                                                                                               |
| [**MF\_SA\_REQUIRED\_SAMPLE\_COUNT**](mf-sa-required-sample-count-attribute.md) | The number of video samples the EVR should allocate for each mixer stream. This attribute applies to individual streams; use the attribute store returned by [**IMFTransform::GetInputStreamAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getinputstreamattributes). |



 

## Setting the Mixer on the EVR

To set a custom mixer on the EVR, call [**IMFVideoRenderer::InitializeRenderer**](/windows/desktop/api/evr/nf-evr-imfvideorenderer-initializerenderer). Both the DirectShow EVR filter and the EVR media sink implement this method.

**EVR Activation Object**. If you are using the EVR activation object, you can provide a custom mixer by setting one of the following attributes on the EVR activation object:



| Attribute                                                                                                 | Description                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_ACTIVATE**](mf-activate-custom-video-mixer-activate-attribute.md) | Pointer to an activation object for the mixer. The activation object must implement the [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) interface. |
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID**](mf-activate-custom-video-mixer-clsid-attribute.md)       | CLSID of the mixer.                                                                                                                   |



 

## Related topics

<dl> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 
