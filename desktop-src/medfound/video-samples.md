---
description: Video Samples
ms.assetid: 1ee2ad6f-5e84-45ba-9849-cd3bd8e7eb29
title: Video Samples
ms.topic: article
ms.date: 05/31/2018
---

# Video Samples

The video sample object is a specialized implementation of the [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample) interface for use with the [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR). To create an instance of this object, call the [**MFCreateVideoSampleFromSurface**](/windows/desktop/api/evr/nc-evr-mfcreatevideosamplefromsurface) function. The function takes a pointer to a Direct3D surface and returns a pointer to the **IMFSample** interface. The following types of objects should allocate samples using this function:

-   Custom EVR presenters. A presenter allocates video samples and sends them to the mixer's [**IMFTransform::ProcessOutput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processoutput) method. For more information, see [How to Write an EVR Presenter](how-to-write-an-evr-presenter.md).

-   Video decoders that support video acceleration. For more information, see [Supporting DXVA 2.0 in Media Foundation](supporting-dxva-2-0-in-media-foundation.md).

The video sample object implements the following interfaces:

-   [**IMFSample**](/windows/desktop/api/mfobjects/nn-mfobjects-imfsample)

-   [**IMFDesiredSample**](/windows/desktop/api/evr/nn-evr-imfdesiredsample)

-   [**IMFTrackedSample**](/windows/win32/api/mfidl/nn-mfidl-imftrackedsample)

If the *pUnkSurface* parameter of [**MFCreateVideoSampleFromSurface**](/windows/desktop/api/evr/nc-evr-mfcreatevideosamplefromsurface) is non-**NULL**, the resulting video sample contains a single media buffer that encapsulates the Direct3D surface. This buffer object has limited functionality:

-   The buffer's [**IMFMediaBuffer::Lock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-lock) method returns E\_NOTIMPL.

-   The buffer does not implement the [**IMF2DBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imf2dbuffer) interface.

The only way to access the surface from the buffer is to call [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice), using the service identifier MR\_BUFFER\_SERVICE.

If the *pUnkSurface* parameter is **NULL**, the video sample is created with zero media buffers. To add a buffer the sample, do the following:

1.  Create a Direct3D surface.

2.  Create a surface buffer by calling [**MFCreateDXSurfaceBuffer**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatedxsurfacebuffer). For more information, see [DirectX Surface Buffer](directx-surface-buffer.md).

3.  Add the buffer to the sample by calling [**IMFSample::AddBuffer**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-addbuffer).

Use this approach if you need the surface memory to be accessible through the [**IMF2DBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imf2dbuffer) interface.

## Related topics

<dl> <dt>

[Media Buffers](media-buffers.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 
