---
Description: 'Indicates to the video sample allocator to create textures as shareable using keyed-mutex.'
ms.assetid: '798CA474-3B1A-4795-81B7-563749197104'
title: 'MF\_SA\_D3D11\_SHARED attribute'
---

# MF\_SA\_D3D11\_SHARED attribute

Indicates to the video sample allocator to create textures as shareable using keyed-mutex.

## Data type

**UINT32**

## Remarks

### Sample Allocator

This attribute can be set on the video sample allocator, in the [**IMFVideoSampleAllocatorEx::InitializeSampleAllocatorEx**](imfvideosampleallocatorex-initializesampleallocatorex.md) method.

## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                              |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFVideoSampleAllocatorEx::InitializeSampleAllocatorEx**](imfvideosampleallocatorex-initializesampleallocatorex.md)
</dt> <dt>

[MF\_SA\_D3D11\_SHARED\_WITHOUT\_MUTEX](mf-sa-d3d11-shared-without-mutex.md)
</dt> </dl>

 

 




