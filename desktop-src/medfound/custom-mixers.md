---
Description: Custom Mixers
ms.assetid: a0af318d-9ac2-43f9-8934-f28c472256a6
title: Custom Mixers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Custom Mixers

This topic describes how to write a custom mixer for the enhanced video renderer (EVR). You can use a custom mixer with either the Media Foundation EVR media sink, or the DirectShow EVR filter. For more information about mixers and presenters, see [Enhanced Video Renderer](enhanced-video-renderer.md).

The mixer is a Media Foundation transform (MFT) with one or more inputs (the reference stream plus the substreams) and one output. The input stream receives samples from upstream. The output stream delivers samples to the presenter. The EVR is responsible for calling [**IMFTransform::ProcessInput**](/windows/win32/mftransform/nf-mftransform-imftransform-processinput?branch=master) on the mixer, and the presenter is responsible for calling [**IMFTransform::ProcessOutput**](/windows/win32/mftransform/nf-mftransform-imftransform-processoutput?branch=master).

At a minimum, an EVR mixer must implement the following interfaces:



| Interface                                                                | Description                                                                                      |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**IMFTransform**](/windows/win32/mftransform/nn-mftransform-imftransform?branch=master)                                     | Provides base MFT functionality.                                                                 |
| [**IMFTopologyServiceLookupClient**](/windows/win32/evr/nn-evr-imftopologyservicelookupclient?branch=master) | Enables the mixer to get interfaces from the EVR.                                                |
| [**IMFVideoDeviceID**](/windows/win32/evr/nn-evr-imfvideodeviceid?branch=master)                             | Enables the mixer to get interfaces from the EVR.                                                |
| [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master)                                   | Used to expose the [**MF\_SA\_D3D\_AWARE**](mf-sa-d3d-aware-attribute.md) attribute to the EVR. |



 

Optionally, an MFT can implement any of the following interfaces:



| Interface                                                | Description                                                                                                                                          |
|----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IEVRTrustedVideoPlugin**](/windows/win32/evr/nn-evr-ievrtrustedvideoplugin?branch=master) | Required to play protected content.                                                                                                                  |
| [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master)                   | Exposes interfaces such as [**IMFVideoMixerBitmap**](/windows/win32/evr9/nn-evr9-imfvideomixerbitmap?branch=master) and [**IMFVideoProcessor**](/windows/win32/evr9/nn-evr9-imfvideoprocessor?branch=master) to the application. |
| [**IMFQualityAdvise**](/windows/win32/mfidl/nn-mfidl-imfqualityadvise?branch=master)             | Enables the quality manager to adjust the video quality.                                                                                             |
| [**IMFVideoMixerBitmap**](/windows/win32/evr9/nn-evr9-imfvideomixerbitmap?branch=master)       | Enables the application to mix a static bitmap onto the video.                                                                                       |
| [**IMFVideoPositionMapper**](/windows/win32/evr/nn-evr-imfvideopositionmapper?branch=master) | Maps coordinates on the output video frame to coordinates on the input video frame.                                                                  |
| [**IMFVideoProcessor**](/windows/win32/evr9/nn-evr9-imfvideoprocessor?branch=master)           | Exposes some DXVA video processing features to the application.                                                                                      |



 

Format negotiation with the mixer works as follows:

1.  The EVR sets the media type on the reference stream.
2.  The EVR calls [**IMFVideoPresenter::ProcessMessage**](/windows/win32/evr/nf-evr-imfvideopresenter-processmessage?branch=master) on the presenter with the **MFVP\_MESSAGE\_INVALIDATEMEDIATYPE** message.

3.  The presenter sets the media type on the mixer's output stream.
4.  The EVR sets the media type on the substreams.

If the media type on the reference stream changes, the mixer's other media types are no longer valid. The mixer's [**IMFTransform::ProcessOutput**](/windows/win32/mftransform/nf-mftransform-imftransform-processoutput?branch=master) method will then fail and return **MF\_E\_TRANSFORM\_STREAM\_CHANGE**. The presenter should not do anything at this point. The EVR will initiate the format negotiation process again.

When any input stream reaches the end of the stream, the EVR calls [**IMFTransform::ProcessMessage**](/windows/win32/mftransform/nf-mftransform-imftransform-processmessage?branch=master) on the mixer with [**MFT\_MESSAGE\_NOTIFY\_END\_OF\_STREAM**](mft-message-notify-end-of-stream.md).

The mixer sends the following events to the EVR, using the EVR's [**IMediaEventSink**](dshow.imediaeventsink) interface. This interface is documented in the DirectShow SDK documentation.



| Event                                            | Description                            |
|--------------------------------------------------|----------------------------------------|
| [**EC\_SAMPLE\_NEEDED**](dshow.ec_sample_needed) | The mixer requires a new input sample. |



 

The EVR might call [**ProcessOutput**](/windows/win32/mftransform/nf-mftransform-imftransform-processoutput?branch=master) on the mixer before streaming starts. The mixer should not fail these calls. Instead, it should fill the output surface with black pixels. The mixer should continue to color-fill output samples until it receives an [**MFT\_MESSAGE\_NOTIFY\_BEGIN\_STREAMING**](mft-message-notify-begin-streaming.md) message or the [**ProcessInput**](/windows/win32/mftransform/nf-mftransform-imftransform-processinput?branch=master) method is called. If the mixer receives an [**MFT\_MESSAGE\_NOTIFY\_END\_STREAMING**](mft-message-notify-end-streaming.md) message, it should switch back to color-fill mode.

## Implementing IMFVideoDeviceID

The [**IMFVideoDeviceID**](/windows/win32/evr/nn-evr-imfvideodeviceid?branch=master) interface contains one method, [**GetDeviceID**](/windows/win32/evr/nf-evr-imfvideodeviceid-getdeviceid?branch=master), which returns a device GUID. The device GUID ensures that the presenter and the mixer use compatible technologies. If the device GUIDs do not match, the EVR fails to initialize.

The standard mixer and presenter both use Direct3D 9, with the device GUID equal to IID\_IDirect3DDevice9. If you intend to use your custom presenter with the standard mixer, the presenter's device GUID must be IID\_IDirect3DDevice9. If you replace both components, you could define a new device GUID.

## Implementing IMFTopologyServiceLookupClient

The mixer must implement the [**IMFTopologyServiceLookupClient**](/windows/win32/evr/nn-evr-imftopologyservicelookupclient?branch=master) interface. Before streaming begins, the EVR calls [**IMFTopologyServiceLookupClient::InitServicePointers**](/windows/win32/evr/nf-evr-imftopologyservicelookupclient-initservicepointers?branch=master) and passes in a pointer to the EVR's [**IMFTopologyServiceLookup**](/windows/win32/evr/nn-evr-imftopologyservicelookup?branch=master) interface. The mixer uses this pointer to get interface pointers from the EVR.

At a minimum, the mixer must query for the following interface:

-   [**IMediaEventSink**](dshow.imediaeventsink)

When the EVR calls [**IMFTopologyServiceLookupClient::ReleaseServicePointers**](/windows/win32/evr/nf-evr-imftopologyservicelookupclient-releaseservicepointers?branch=master), the mixer must release any pointers obtained from the call to [**InitServicePointers**](/windows/win32/evr/nf-evr-imftopologyservicelookupclient-initservicepointers?branch=master).

## Mixer Attributes

A mixer should support the following attributes.



| Attribute                                                                        | Description                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_SA\_D3D\_AWARE**](mf-sa-d3d-aware-attribute.md)                          | Specifies whether the mixer supports DirectX Video Acceleration (DXVA).                                                                                                                                                                               |
| [**MF\_SA\_REQUIRED\_SAMPLE\_COUNT**](mf-sa-required-sample-count-attribute.md) | The number of video samples the EVR should allocate for each mixer stream. This attribute applies to individual streams; use the attribute store returned by [**IMFTransform::GetInputStreamAttributes**](/windows/win32/mftransform/nf-mftransform-imftransform-getinputstreamattributes?branch=master). |



 

## Setting the Mixer on the EVR

To set a custom mixer on the EVR, call [**IMFVideoRenderer::InitializeRenderer**](/windows/win32/evr/nf-evr-imfvideorenderer-initializerenderer?branch=master). Both the DirectShow EVR filter and the EVR media sink implement this method.

**EVR Activation Object**. If you are using the EVR activation object, you can provide a custom mixer by setting one of the following attributes on the EVR activation object:



| Attribute                                                                                                 | Description                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_ACTIVATE**](mf-activate-custom-video-mixer-activate-attribute.md) | Pointer to an activation object for the mixer. The activation object must implement the [**IMFActivate**](/windows/win32/mfobjects/nn-mfobjects-imfactivate?branch=master) interface. |
| [**MF\_ACTIVATE\_CUSTOM\_VIDEO\_MIXER\_CLSID**](mf-activate-custom-video-mixer-clsid-attribute.md)       | CLSID of the mixer.                                                                                                                   |



 

## Related topics

<dl> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> </dl>

 

 



