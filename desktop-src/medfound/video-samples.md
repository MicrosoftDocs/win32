---
Description: Video Samples
ms.assetid: 1ee2ad6f-5e84-45ba-9849-cd3bd8e7eb29
title: Video Samples
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Video Samples

The video sample object is a specialized implementation of the [**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master) interface for use with the [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR). To create an instance of this object, call the [**MFCreateVideoSampleFromSurface**](/windows/win32/evr/nc-evr-mfcreatevideosamplefromsurface?branch=master) function. The function takes a pointer to a Direct3D surface and returns a pointer to the **IMFSample** interface. The following types of objects should allocate samples using this function:

-   Custom EVR presenters. A presenter allocates video samples and sends them to the mixer's [**IMFTransform::ProcessOutput**](/windows/win32/mftransform/nf-mftransform-imftransform-processoutput?branch=master) method. For more information, see [How to Write an EVR Presenter](how-to-write-an-evr-presenter.md).

-   Video decoders that support video acceleration. For more information, see [Supporting DXVA 2.0 in Media Foundation](supporting-dxva-2-0-in-media-foundation.md).

The video sample object implements the following interfaces:

-   [**IMFSample**](/windows/win32/mfobjects/nn-mfobjects-imfsample?branch=master)

-   [**IMFDesiredSample**](/windows/win32/evr/nn-evr-imfdesiredsample?branch=master)

-   [**IMFTrackedSample**](/windows/win32/evr/nn-mfidl-imftrackedsample?branch=master)

If the *pUnkSurface* parameter of [**MFCreateVideoSampleFromSurface**](/windows/win32/evr/nc-evr-mfcreatevideosamplefromsurface?branch=master) is non-**NULL**, the resulting video sample contains a single media buffer that encapsulates the Direct3D surface. This buffer object has limited functionality:

-   The buffer's [**IMFMediaBuffer::Lock**](/windows/win32/mfobjects/nf-mfobjects-imfmediabuffer-lock?branch=master) method returns E\_NOTIMPL.

-   The buffer does not implement the [**IMF2DBuffer**](/windows/win32/mfobjects/nn-mfobjects-imf2dbuffer?branch=master) interface.

The only way to access the surface from the buffer is to call [**IMFGetService::GetService**](/windows/win32/mfidl/nf-mfidl-imfgetservice-getservice?branch=master), using the service identifier MR\_BUFFER\_SERVICE.

If the *pUnkSurface* parameter is **NULL**, the video sample is created with zero media buffers. To add a buffer the sample, do the following:

1.  Create a Direct3D surface.

2.  Create a surface buffer by calling [**MFCreateDXSurfaceBuffer**](/windows/win32/mfapi/nf-mfapi-mfcreatedxsurfacebuffer?branch=master). For more information, see [DirectX Surface Buffer](directx-surface-buffer.md).

3.  Add the buffer to the sample by calling [**IMFSample::AddBuffer**](/windows/win32/mfobjects/nf-mfobjects-imfsample-addbuffer?branch=master).

Use this approach if you need the surface memory to be accessible through the [**IMF2DBuffer**](/windows/win32/mfobjects/nn-mfobjects-imf2dbuffer?branch=master) interface.

## Related topics

<dl> <dt>

[Media Buffers](media-buffers.md)
</dt> <dt>

[Media Samples](media-samples.md)
</dt> </dl>

 

 



