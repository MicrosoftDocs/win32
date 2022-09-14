---
description: Indicates to the video sample allocator to create textures as shareable using the legacy mechanism.
ms.assetid: A9F4D4AF-BB47-48E2-B40A-D0245FD61FAF
title: MF_SA_D3D11_SHARED_WITHOUT_MUTEX attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_SA\_D3D11\_SHARED\_WITHOUT\_MUTEX attribute

Indicates to the video sample allocator to create textures as shareable using the legacy mechanism.

## Data type

**UINT32**

## Remarks

### Sample Allocator

This attribute can be set on the video sample allocator, in the [**IMFVideoSampleAllocatorEx::InitializeSampleAllocatorEx**](/windows/desktop/api/mfidl/nf-mfidl-imfvideosampleallocatorex-initializesampleallocatorex) method.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFVideoSampleAllocatorEx::InitializeSampleAllocatorEx**](/windows/desktop/api/mfidl/nf-mfidl-imfvideosampleallocatorex-initializesampleallocatorex)
</dt> <dt>

[MF\_SA\_D3D11\_SHARED](mf-sa-d3d11-shared.md)
</dt> </dl>

 

 




