---
Description: DirectX Surface Buffer
ms.assetid: 2c82c023-4436-4f8a-b896-7f4765f989b3
title: DirectX Surface Buffer
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DirectX Surface Buffer

The DirectX surface buffer object is a media buffer that manages a Direct3D surface. To create an instance of this object, call [**MFCreateDXSurfaceBuffer**](/windows/win32/mfapi/nf-mfapi-mfcreatedxsurfacebuffer?branch=master) and pass in a pointer to the DirectX surface. The DirectX surface buffer exposes the following interfaces:

-   [**IMFMediaBuffer**](/windows/win32/mfobjects/nn-mfobjects-imfmediabuffer?branch=master)
-   [**IMF2DBuffer**](/windows/win32/mfobjects/nn-mfobjects-imf2dbuffer?branch=master)
-   [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master)

There are several ways to access the surface memory from the buffer object:

-   Recommended: Call [**IMFGetService::GetService**](/windows/win32/mfidl/nf-mfidl-imfgetservice-getservice?branch=master) on the buffer. Use the service identifier **MR\_BUFFER\_SERVICE**. The method returns a pointer to the underlying Direct3D surface.
-   Call [**IMF2DBuffer::Lock2D**](/windows/win32/mfobjects/nf-mfobjects-imf2dbuffer-lock2d?branch=master). This method calls **IDirect3DSurface9::LockRect** directly on the surface. The [**IMF2DBuffer::Unlock2D**](/windows/win32/mfobjects/nf-mfobjects-imf2dbuffer-unlock2d?branch=master) method calls **UnlockRect** on the surface.
-   Call [**IMFMediaBuffer::Lock**](/windows/win32/mfobjects/nf-mfobjects-imfmediabuffer-lock?branch=master). Generally this is not recommended, because it forces the object to copy memory from the Direct3D surface and then back again. The [**Lock2D**](/windows/win32/mfobjects/nf-mfobjects-imf2dbuffer-lock2d?branch=master) method is more efficient.

Both [**Lock**](/windows/win32/mfobjects/nf-mfobjects-imfmediabuffer-lock?branch=master) and [**Lock2D**](/windows/win32/mfobjects/nf-mfobjects-imf2dbuffer-lock2d?branch=master) can fail if the underlying surface is not lockable. The DirectX surface buffer implements these two methods primarily for components that are not designed to work with Direct3D surfaces.

The enhanced video renderer (EVR) creates DirectX surface buffers when the decoder is not configured for DirectX Video Acceleration (DXVA). For more information, see [**IMFVideoSampleAllocator**](/windows/win32/mfidl/nn-mfidl-imfvideosampleallocator?branch=master).

### Obtaining the Direct3D Surface

To get a Direct3D surface from a video sample, do the following:

1.  Call [**IMFSample::GetBufferByIndex**](/windows/win32/mfobjects/nf-mfobjects-imfsample-getbufferbyindex?branch=master) with an index value of zero.
2.  Call [**MFGetService**](/windows/win32/mfidl/nf-mfidl-mfgetservice?branch=master) and specify the **MR\_BUFFER\_SERVICE** service identifier.

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

 

 



