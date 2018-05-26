---
Description: .
ms.assetid: a4508a1e-d68b-4c55-bce4-c8b462134fa1
title: Creating DXVA-HD Video Surfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating DXVA-HD Video Surfaces

The application must create one or more Direct3D surfaces to use for the input frames. These must be allocated in the memory pool specified by the **InputPool** member of the [**DXVAHD\_VPDEVCAPS**](/windows/win32/dxvahd/ns-dxvahd-_dxvahd_vpdevcaps?branch=master) structure. The following surface types can be used:

-   A video surface created by calling [**IDXVAHD\_Device::CreateVideoSurface**](/windows/win32/dxvahd/nf-dxvahd-idxvahd_device-createvideosurface?branch=master) and specifying the **DXVAHD\_SURFACE\_TYPE\_VIDEO\_INPUT** or **DXVAHD\_SURFACE\_TYPE\_VIDEO\_INPUT\_PRIVATE** surface type. This surface type is equivalent to an off-screen plain surface.
-   A decoder render-target surface, created by calling [**IDirectXVideoAccelerationService::CreateSurface**](/windows/win32/dxva2api/nf-dxva2api-idirectxvideoaccelerationservice-createsurface?branch=master) and specifying the **DXVA2\_VideoDecoderRenderTarget** surface type. This surface type is used for DXVA decoding.
-   An off-screen plain surface.

The following code shows how to allocate a video surface, using [**CreateVideoSurface**](/windows/win32/dxvahd/nf-dxvahd-idxvahd_device-createvideosurface?branch=master):


```C++
    // Create the video surface for the primary video stream.
    hr = pDXVAHD->CreateVideoSurface(
        VIDEO_WIDTH,
        VIDEO_HEIGHT,
        VIDEO_FORMAT,
        caps.InputPool,
        0,  // Usage
        DXVAHD_SURFACE_TYPE_VIDEO_INPUT,
        1,      // Number of surfaces to create
        &amp;pSurf, // Array of surface pointers
        NULL
        );
```



## Related topics

<dl> <dt>

[DXVA-HD](dxva-hd.md)
</dt> </dl>

 

 



