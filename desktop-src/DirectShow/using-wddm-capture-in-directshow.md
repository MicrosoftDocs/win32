---
description: Using WDDM Capture in DirectShow
ms.assetid: 57ee86b0-50bc-4992-94d4-f290f83d2afc
title: Using WDDM Capture in DirectShow
ms.topic: article
ms.date: 05/31/2018
---

# Using WDDM Capture in DirectShow

This topic applies to Windows Vista and later.

Some video cards have integrated video capture functionality. On these cards, captured video frames are placed in video memory (VRAM). Prior to Windows Vista, there was no standard mechanism for processing the frames while they remained in VRAM. Instead, the data had to be copied into system memory, processed, and then copied back to VRAM for display. In Windows Vista, DirectShow now supports a mechanism for keeping the video frames in VRAM throughout the processing pipeline, from capture to display.

The KsProxy filter determines if the driver supports VRAM surface capture by querying the driver for the KSPROPERTY\_PREFERRED\_CAPTURE\_SURFACE property. (This property is documented in the Windows Driver Kit documentation.) If the driver supports VRAM surface capture, KsProxy allocates a special kind of media sample that holds a pointer to a Direct3D surface.

Next, KsProxy determines whether the downstream filter supports DirectX Video Acceleration (DXVA) 2.0, as follows:

1.  KsProxy queries the downstream input pin for the **IMFGetService** interface.
2.  If the pin exposes **IMFGetService**, KsProxy calls **IMFGetService::GetService** for the **IDirect3DDeviceManager** interface. The service identier is MR\_VIDEO\_ACCELERATION\_SERVICE.

Both of these interfaces are documented in the Media Foundation SDK documentation.

If the downstream filter does not support DXVA 2.0, KsProxy allocates an additional system memory buffer. It uses this buffer to copy the video frames from VRAM to system memory. The media sample's [**IMediaSample::GetPointer**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getpointer) method returns a pointer to this system memory buffer.

However, if the downstream filter does support DXVA 2.0, then KsProxy does not allocate a system memory buffer. In that case, the **GetPointer** method returns E\_NOTIMPL. Instead, the downstream filter is expected to access the sample's Direct3D surface directly. There are two ways for the downstream filter to get a pointer to the surface, both of them equivalent:

-   Query the sample for the **IMFGetService** interface and call **GetService** for the **IDirect3DSurface9** interface. The service identifier is MR\_BUFFER\_SERVICE.
-   Query the sample for the [**IMediaSample2Config**](/windows/desktop/api/Strmif/nn-strmif-imediasample2config) interface and call [**IMediaSample2Config::GetSurface**](/windows/desktop/api/Strmif/nf-strmif-imediasample2config-getsurface).

## Related topics

<dl> <dt>

[Advanced Capture Topics](advanced-capture-topics.md)
</dt> </dl>

 

 



