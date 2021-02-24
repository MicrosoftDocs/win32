---
description: Supporting DXVA 2.0 in Media Foundation
ms.assetid: d7330370-adb3-4c6a-962a-7b46c344500c
title: Supporting DXVA 2.0 in Media Foundation
ms.topic: article
ms.date: 05/31/2018
---

# Supporting DXVA 2.0 in Media Foundation

This topic describes how to support DirectX Video Acceleration (DXVA) 2.0 in a Media Foundation transform (MFT) using Microsoft Direct3D 9 Specifically, it describes the communication between the decoder and the video renderer, which is mediated by the topology loader. This topic does not describe how to implement DXVA decoding.

In the remainder of this topic, the term *decoder* refers to the decoder MFT, which receives compressed video and outputs uncompressed video. The term *decoder device* refers to a hardware video accelerator implemented by the graphics driver.

> [!TIP]
> For info on Microsoft Direct3D 11 video decoding see, [Supporting Direct3D 11 Video Decoding in Media Foundation](supporting-direct3d-11-video-decoding-in-media-foundation.md).

 

> [!Note]  
> Windows Store apps must use Direct3D 11.

 

Here are the basic steps that a decoder must perform to support DXVA 2.0 in Media Foundation:

1.  Open a handle to the Direct3D 9 device.
2.  Find a DXVA decoder configuration.
3.  Allocate uncompressed Buffers.
4.  Decode frames.

These steps are described in more detail in the remainder of this topic.

## Opening a Direct3D Device Handle

The MFT uses the Microsoft Direct3D device manager to get a handle to the Direct3D 9 device. To open the device handle, perform the following steps:

1.  Expose the [MF\_SA\_D3D\_AWARE](mf-sa-d3d-aware-attribute.md) attribute with the value **TRUE**. The topology loader queries this attribute by calling [**IMFTransform::GetAttributes**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getattributes). Setting the attribute to **TRUE** notifies the topology loader that the MFT supports DXVA.
2.  When format negotiation begins, the topology loader calls [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) with the [**MFT\_MESSAGE\_SET\_D3D\_MANAGER**](mft-message-set-d3d-manager.md) message. The *ulParam* parameter is an **IUnknown** pointer to the video renderer's Direct3D device manager. Query this pointer for the [**IDirect3DDeviceManager9**](/windows/desktop/api/dxva2api/nn-dxva2api-idirect3ddevicemanager9) interface.
3.  Call [**IDirect3DDeviceManager9::OpenDeviceHandle**](/windows/desktop/api/dxva2api/nf-dxva2api-idirect3ddevicemanager9-opendevicehandle) to get a handle to the renderer's Direct3D device.
4.  Call [**IDirect3DDeviceManager9::GetVideoService**](/windows/desktop/api/dxva2api/nf-dxva2api-idirect3ddevicemanager9-getvideoservice) and pass in the device handle. This method returns a pointer to the [**IDirectXVideoDecoderService**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideodecoderservice) interface.
5.  Cache the pointers and the device handle.

## Finding a Decoder Configuration

The MFT must find a compatible configuration for the DXVA decoder device. Perform the following steps inside the [**IMFTransform::SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) method, after validating the input type:

1.  Call [**IDirectXVideoDecoderService::GetDecoderDeviceGuids**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoderservice-getdecoderdeviceguids). This method returns an array of decoder device GUIDs.
2.  Loop through the array of decoder GUIDs to find the ones that the decoder supports. For example, for an MPEG-2 decoder, you would look for **DXVA2\_ModeMPEG2\_MOCOMP**, **DXVA2\_ModeMPEG2\_IDCT**, or **DXVA2\_ModeMPEG2\_VLD**.

3.  When you find a candidate decoder device GUID, pass the GUID to the [**IDirectXVideoDecoderService::GetDecoderRenderTargets**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoderservice-getdecoderrendertargets) method. This method returns an array of render target formats, specified as **D3DFORMAT** values.
4.  Loop through the render target formats and look for a format supported by the decoder.
5.  Call [**IDirectXVideoDecoderService::GetDecoderConfigurations**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoderservice-getdecoderconfigurations). Pass in the same decoder device GUID, along with a [**DXVA2\_VideoDesc**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_videodesc) structure that describes the proposed output format. The method returns an array of [**DXVA2\_ConfigPictureDecode**](/windows/desktop/api/dxva2api/ns-dxva2api-dxva2_configpicturedecode) structures. Each structure describes one possible configuration for the decoder device. Look for a configuration that the decoder supports.
6.  Store the render target format and configuration.

In the [**IMFTransform::GetOutputAvailableType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputavailabletype) method, return an uncompressed video format, based on the proposed render target format.

In the [**IMFTransform::SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) method, check the media type against the render target format.

### Fallback to Software Decoding

If the MFT cannot find a DXVA configuration (for example, if the graphics driver does not have the right capabilities), it should return the error code **MF\_E\_UNSUPPORTED\_D3D\_TYPE** from the [**SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype) and [**SetOutputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setoutputtype) methods. The topology loader will respond by sending the [**MFT\_MESSAGE\_SET\_D3D\_MANAGER**](mft-message-set-d3d-manager.md) message with the value **NULL** for the *ulParam* parameter. The MFT should release its pointer to the [**IDirect3DDeviceManager9**](/windows/desktop/api/dxva2api/nn-dxva2api-idirect3ddevicemanager9) interface. The topology loader will then renegotiate the media type, and the MFT can use software decoding.

## Allocating Uncompressed Buffers

In DXVA 2.0, the decoder is responsible for allocating Direct3D surfaces to use as uncompressed video buffers. The decoder should allocate 3 surfaces for the EVR to use for deinterlacing. This number is fixed, because Media Foundation does not provide a way for the EVR to specify how many surfaces the graphics driver requires for deinterlacing. Three surfaces should be sufficient for any driver.

In the [**IMFTransform::GetOutputStreamInfo**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-getoutputstreaminfo) method, set the **MFT\_OUTPUT\_STREAM\_PROVIDES\_SAMPLES** flag in the [**MFT\_OUTPUT\_STREAM\_INFO**](/windows/desktop/api/mftransform/ns-mftransform-mft_output_stream_info) structure. This flag notifies the Media Session that the MFT allocates its own output samples.

To create the surfaces, call [**IDirectXVideoAccelerationService::CreateSurface**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideoaccelerationservice-createsurface). (The [**IDirectXVideoDecoderService**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideodecoderservice) interface inherits this method from [**IDirectXVideoAccelerationService**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideoaccelerationservice).) You can do this in [**SetInputType**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-setinputtype), after finding the render target format.

For each surface, call [**MFCreateVideoSampleFromSurface**](/windows/desktop/api/evr/nc-evr-mfcreatevideosamplefromsurface) to create a media sample to hold the surface. The method returns a pointer to the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface.

## Decoding

To create the decoder device, call [**IDirectXVideoDecoderService::CreateVideoDecoder**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoderservice-createvideodecoder). The method returns a pointer to the [**IDirectXVideoDecoder**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideodecoder) interface of the decoder device.

Decoding should occur inside the [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method. On each frame, call [**IDirect3DDeviceManager9::TestDevice**](/windows/desktop/api/dxva2api/nf-dxva2api-idirect3ddevicemanager9-testdevice) to test the device handle. If the device has changed, the method returns **DXVA2\_E\_NEW\_VIDEO\_DEVICE**. If this occurs, do the following:

1.  Close the device handle by calling [**IDirect3DDeviceManager9::CloseDeviceHandle**](/windows/desktop/api/dxva2api/nf-dxva2api-idirect3ddevicemanager9-closedevicehandle).
2.  Release the [**IDirectXVideoDecoderService**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideodecoderservice) and [**IDirectXVideoDecoder**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideodecoder) pointers.
3.  Open a new device handle.
4.  Negotiate a new decoder configuration, as described in "Finding a Decoder Configuration" earlier on this page.
5.  Create a new decoder device.

Assuming that the device handle is valid, the decoding process works as follows:

1.  Get an available surface that is not currently in use. (Initially all of the surfaces are available.)
2.  Query the media sample for the [**IMFTrackedSample**](/windows/win32/api/mfidl/nn-mfidl-imftrackedsample) interface.
3.  Call [**IMFTrackedSample::SetAllocator**](/windows/win32/api/mfidl/nf-mfidl-imftrackedsample-setallocator) and provide a pointer to the [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) interface, implemented by the decoder. When the video renderer releases the sample, the decoder's callback will be invoked.
4.  Call [**IDirectXVideoDecoder::BeginFrame**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoder-beginframe).
5.  Do the following one or more times:
    1.  Call [**IDirectXVideoDecoder::GetBuffer**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoder-getbuffer) to get a DXVA decoder buffer.
    2.  Fill the buffer.
    3.  Call [**IDirectXVideoDecoder::ReleaseBuffer**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoder-releasebuffer).
    4.  Call [**IDirectXVideoDecoder::Execute**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoder-execute) to perform the decoding operations on the frame.

DXVA 2.0 uses the same data structures as DXVA 1.0 for decoding operations. For the original set of DXVA profiles (for H.261, H.263, and MPEG-2), these data structures are described in the [DXVA 1.0 specification](/windows-hardware/drivers/display/directx-video-acceleration).

Within each pair of [**BeginFrame**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoder-beginframe)/[**Execute**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoder-execute) calls, you may call [**GetBuffer**](/windows/desktop/api/dxva2api/nf-dxva2api-idirectxvideodecoder-getbuffer) multiple times, but only once for each type of DXVA buffer. If you call it twice with the same buffer type, you will overwrite the data.

Use the callback from the [**SetAllocator**](/windows/win32/api/mfidl/nf-mfidl-imftrackedsample-setallocator) method (step 3) to keep track of which samples are currently available and which are in use.

## Related topics

<dl> <dt>

[DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md)
</dt> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> </dl>

 

 
