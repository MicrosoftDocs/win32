---
description: Specifies how many buffers the video-sample allocator creates for each video sample.
ms.assetid: A782BF8A-822A-407D-A30A-F2045BBB0BC0
title: MF_SA_BUFFERS_PER_SAMPLE attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SA\_BUFFERS\_PER\_SAMPLE attribute

Specifies how many buffers the video-sample allocator creates for each video sample.

## Data type

**UINT32**

## Remarks

If you use the [**IMFVideoSampleAllocatorEx**](/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatorex) interface to allocate video samples, you can use this attribute to create video samples that contain multiple buffers. For example, if the attribute value is 2, the allocator creates two video buffers for each video sample. Set the attribute in the *pAttributes* parameter of the [**IMFVideoSampleAllocatorEx::InitializeSampleAllocatorEx**](/windows/desktop/api/mfidl/nf-mfidl-imfvideosampleallocatorex-initializesampleallocatorex) method.

The default value is 1. If the attribute is not set, the allocator creates video samples that contain a single buffer per sample.

This attribute is primarily intended for Media Foundation transforms (MFTs) that support stereo 3D output, in the following situation:

-   The MFT supports Microsoft DirectX Graphics Infrastructure (DXGI).
-   The MFT allocates its own output samples.
-   The MFT uses the [**IMFVideoSampleAllocatorEx**](/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatorex) interface to allocate the output samples.
-   The 3D video format uses a separate buffer for each view.

If all of these criteria are true, the MFT should set the attribute value to 2 (one buffer per view).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 




