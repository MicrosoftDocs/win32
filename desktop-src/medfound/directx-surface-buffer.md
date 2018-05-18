---
Description: DirectX Surface Buffer
ms.assetid: '2c82c023-4436-4f8a-b896-7f4765f989b3'
title: DirectX Surface Buffer
---

# DirectX Surface Buffer

The DirectX surface buffer object is a media buffer that manages a Direct3D surface. To create an instance of this object, call [**MFCreateDXSurfaceBuffer**](mfcreatedxsurfacebuffer.md) and pass in a pointer to the DirectX surface. The DirectX surface buffer exposes the following interfaces:

-   [**IMFMediaBuffer**](imfmediabuffer.md)
-   [**IMF2DBuffer**](imf2dbuffer.md)
-   [**IMFGetService**](imfgetservice.md)

There are several ways to access the surface memory from the buffer object:

-   Recommended: Call [**IMFGetService::GetService**](imfgetservice-getservice.md) on the buffer. Use the service identifier **MR\_BUFFER\_SERVICE**. The method returns a pointer to the underlying Direct3D surface.
-   Call [**IMF2DBuffer::Lock2D**](imf2dbuffer-lock2d.md). This method calls **IDirect3DSurface9::LockRect** directly on the surface. The [**IMF2DBuffer::Unlock2D**](imf2dbuffer-unlock2d.md) method calls **UnlockRect** on the surface.
-   Call [**IMFMediaBuffer::Lock**](imfmediabuffer-lock.md). Generally this is not recommended, because it forces the object to copy memory from the Direct3D surface and then back again. The [**Lock2D**](imf2dbuffer-lock2d.md) method is more efficient.

Both [**Lock**](imfmediabuffer-lock.md) and [**Lock2D**](imf2dbuffer-lock2d.md) can fail if the underlying surface is not lockable. The DirectX surface buffer implements these two methods primarily for components that are not designed to work with Direct3D surfaces.

The enhanced video renderer (EVR) creates DirectX surface buffers when the decoder is not configured for DirectX Video Acceleration (DXVA). For more information, see [**IMFVideoSampleAllocator**](imfvideosampleallocator.md).

### Obtaining the Direct3D Surface

To get a Direct3D surface from a video sample, do the following:

1.  Call [**IMFSample::GetBufferByIndex**](imfsample-getbufferbyindex.md) with an index value of zero.
2.  Call [**MFGetService**](mfgetservice.md) and specify the **MR\_BUFFER\_SERVICE** service identifier.

The following code shows these steps:


```C++
HRESULT GetD3DSurfaceFromSample(IMFSample *pSample, IDirect3DSurface9 **ppSurface)
{
    *ppSurface = NULL;

    IMFMediaBuffer *pBuffer = NULL;

    HRESULT hr = pSample->GetBufferByIndex(0, &amp;pBuffer);
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

 

 



