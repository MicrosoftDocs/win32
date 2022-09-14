---
description: DirectX Surface Buffer
ms.assetid: 2c82c023-4436-4f8a-b896-7f4765f989b3
title: DirectX Surface Buffer
ms.topic: article
ms.date: 05/31/2018
---

# DirectX Surface Buffer

The DirectX surface buffer object is a media buffer that manages a Direct3D surface. To create an instance of this object, call [**MFCreateDXSurfaceBuffer**](/windows/desktop/api/mfapi/nf-mfapi-mfcreatedxsurfacebuffer) and pass in a pointer to the DirectX surface. The DirectX surface buffer exposes the following interfaces:

-   [**IMFMediaBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediabuffer)
-   [**IMF2DBuffer**](/windows/desktop/api/mfobjects/nn-mfobjects-imf2dbuffer)
-   [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)

There are several ways to access the surface memory from the buffer object:

-   Recommended: Call [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) on the buffer. Use the service identifier **MR\_BUFFER\_SERVICE**. The method returns a pointer to the underlying Direct3D surface.
-   Call [**IMF2DBuffer::Lock2D**](/windows/desktop/api/mfobjects/nf-mfobjects-imf2dbuffer-lock2d). This method calls **IDirect3DSurface9::LockRect** directly on the surface. The [**IMF2DBuffer::Unlock2D**](/windows/desktop/api/mfobjects/nf-mfobjects-imf2dbuffer-unlock2d) method calls **UnlockRect** on the surface.
-   Call [**IMFMediaBuffer::Lock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-lock). Generally this is not recommended, because it forces the object to copy memory from the Direct3D surface and then back again. The [**Lock2D**](/windows/desktop/api/mfobjects/nf-mfobjects-imf2dbuffer-lock2d) method is more efficient.

Both [**Lock**](/windows/desktop/api/mfobjects/nf-mfobjects-imfmediabuffer-lock) and [**Lock2D**](/windows/desktop/api/mfobjects/nf-mfobjects-imf2dbuffer-lock2d) can fail if the underlying surface is not lockable. The DirectX surface buffer implements these two methods primarily for components that are not designed to work with Direct3D surfaces.

The enhanced video renderer (EVR) creates DirectX surface buffers when the decoder is not configured for DirectX Video Acceleration (DXVA). For more information, see [**IMFVideoSampleAllocator**](/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocator).

### Obtaining the Direct3D Surface

To get a Direct3D surface from a video sample, do the following:

1.  Call [**IMFSample::GetBufferByIndex**](/windows/desktop/api/mfobjects/nf-mfobjects-imfsample-getbufferbyindex) with an index value of zero.
2.  Call [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) and specify the **MR\_BUFFER\_SERVICE** service identifier.

The following code shows these steps:


```C++
HRESULT GetD3DSurfaceFromSample(IMFSample *pSample, IDirect3DSurface9 **ppSurface)
{
    *ppSurface = NULL;

    IMFMediaBuffer *pBuffer = NULL;

    HRESULT hr = pSample->GetBufferByIndex(0, &pBuffer);
    if (SUCCEEDED(hr))
    {
        hr = MFGetService(pBuffer, MR_BUFFER_SERVICE, IID_PPV_ARGS(ppSurface));
        pBuffer->Release();
    }

    return hr;
}
```



## Related topics

<dl> <dt>

[Media Buffers](media-buffers.md)
</dt> <dt>

[Video Samples](video-samples.md)
</dt> </dl>

 

 



