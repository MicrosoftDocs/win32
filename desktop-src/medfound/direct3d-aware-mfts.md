---
Description: 'This topic describes how to implement a Direct3D-aware Media Foundation transform (MFT) for video.'
ms.assetid: '8ec7e678-8477-41fa-9726-54df5ed187cd'
title: 'Direct3D-Aware MFTs'
---

# Direct3D-Aware MFTs

This topic describes how to implement a *Direct3D-aware* Media Foundation transform (MFT) for video.

An video MFT is considered *Direct3D-aware* if it can process samples that contain Direct3D surfaces. The typical reason for supporting Direct3D in a video MFT is to enable hardware-accelerated decoding, using DirectX Video Acceleration (DXVA).

This topic describes the steps that are required to make your MFT Direct3D-aware. This topic does not cover the mechanics of DXVA decoding. For information about DXVA, see [DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md).

> \[!Important\]  
> Beginning in Windows 8, [**IMFDXGIDeviceManager**](imfdxgidevicemanager.md) can be used instead of the [**IDirect3DDeviceManager9**](idirect3ddevicemanager9.md). For Windows Store apps, you must use **IMFDXGIDeviceManager** and Microsoft Direct3D 11. For more info, see the [Direct3D 11 Video APIs](direct3d-11-video-apis.md).

 

1.  Implement the [**IMFTransform::GetAttributes**](imftransform-getattributes.md) method. This method returns a pointer to an attribute store.
2.  The MFT must set the value of the [**MF\_SA\_D3D\_AWARE**](mf-sa-d3d-aware-attribute.md) attribute to **TRUE** on its own attribute store. Beginning in Windows 8, if using Direct3D 11 use [MF\_SA\_D3D11\_AWARE](mf-sa-d3d11-aware.md).
3.  During format negotiation, if the [**MF\_SA\_D3D\_AWARE**](mf-sa-d3d-aware-attribute.md) (or [MF\_SA\_D3D11\_AWARE](mf-sa-d3d11-aware.md) if using Direct3D 11) attribute is **TRUE**, the client may send the [**MFT\_MESSAGE\_SET\_D3D\_MANAGER**](mft-message-set-d3d-manager.md) message to the MFT. The *ulParam* event parameter is a pointer to the [**IDirect3DDeviceManager9**](idirect3ddevicemanager9.md) interface. Beginning in Windows 8, you can use [**IMFDXGIDeviceManager**](imfdxgidevicemanager.md) instead of **IDirect3DDeviceManager9**. The client is not required to send this message.
4.  The MFT calls [**IDirect3DDeviceManager9::GetVideoService**](idirect3ddevicemanager9-getvideoservice.md) to query for the DXVA service it needs. Beginning in Windows 8, if [**IMFDXGIDeviceManager**](imfdxgidevicemanager.md) was used the MFT calls [**IMFDXGIDeviceManager::GetVideoService**](imfdxgidevicemanager-getvideoservice.md). Typically a decoder would query for [**IDirectXVideoDecoderService**](idirectxvideodecoderservice.md), and a video processor would query for [**IDirectXVideoProcessorService**](idirectxvideoprocessorservice.md).
5.  Assuming the previous step is successful, the [**IMFTransform::GetInputAvailableType**](imftransform-getinputavailabletype.md) and [**IMFTransform::GetOutputAvailableType**](imftransform-getoutputavailabletype.md) methods must return DXVA-compatible formats.
6.  The client configures the media types on the MFT. If a media type is not compatible with DXVA, the MFT must return the error code **MF\_E\_UNSUPPORTED\_D3D\_TYPE**.
7.  At this point, there are two options, depending on whether the client finds a suitable DXVA format.
    -   If the client successfully configures a DXVA format, it may begin processing. At this point, the MFT can use DXVA for processing, or fall back to software processing.
    -   Alternatively, if the client does not find an acceptable DXVA format, the client may send another [**MFT\_MESSAGE\_SET\_D3D\_MANAGER**](mft-message-set-d3d-manager.md) message, this time setting *ulParam* to **NULL**. The MFT must release the [**IDirect3DDeviceManager9**](idirect3ddevicemanager9.md) pointer (the [**IMFDXGIDeviceManager**](imfdxgidevicemanager.md) pointer, if **IMFDXGIDeviceManager** was used) and any other DXVA interfaces, and revert to software processing. At this point, the MFT must not use DXVA processing.

A Direct3D-aware MFT must be prepared to handle samples that contain a Direct3D surface. The sample will contain exactly one media buffer. To get the Direct3D surface from the buffer, call the [**MFGetService**](mfgetservice.md) function and specify the **MR\_BUFFER\_SERVICE** service. For more information, see [DirectX Surface Buffer](directx-surface-buffer.md).

An MFT that uses DXVA must allocate its own output samples, as follows:

1.  In the [**IMFTransform::GetOutputStreamInfo**](imftransform-getoutputstreaminfo.md) method, set the **MFT\_OUTPUT\_STREAM\_PROVIDES\_SAMPLES** flag.
2.  Create a pool of DXVA surfaces, as described in the DXVA specification.
3.  Create media samples by calling [**MFCreateVideoSampleFromSurface**](mfcreatevideosamplefromsurface.md).

The MFT should always support software processing as a fallback, because DXVA processing might not available, for several reasons:

-   The GPU might not support DXVA.
-   The client might not use Direct3D.
-   DXVA profiles are not defined for every video format.

A Direct3D-aware MFT must have a single output stream. It cannot have multiple outputs.

## Related topics

<dl> <dt>

[Writing a Custom MFT](writing-a-custom-mft.md)
</dt> </dl>

 

 



