---
title: Default Texture Mapping
description: The use of default texture mapping reduces copying and memory usage while sharing image data between the GPU and the CPU.
ms.assetid: '77AF4BFA-09B5-4181-9408-002764F2A923'
---

# Default Texture Mapping

The use of default texture mapping reduces copying and memory usage while sharing image data between the GPU and the CPU. However, it should only be used in specific situations. The standard swizzle layout avoids copying or swizzling data in multiple layouts.

-   [Overview](#overview)
-   [D3D11.3 APIs](#d3d113-apis)
-   [Related topics](#related-topics)

## Overview

Mapping default textures should not be the first choice for developers. Developers should code in a discrete-GPU friendly way first (that is, do not have any CPU access for the majority of textures and upload with [**CopySubresourceRegion1**](id3d11devicecontext1-copysubresourceregion1.md)). But, for certain cases, the CPU and GPU may interact so frequently on the same data, that mapping default textures becomes helpful to save power, or to speed up a particular design on particular adapters or architectures. Applications should detect these cases and optimize out the unnecessary copies.

In D3D11.3, textures created with D3D11\_TEXTURE\_LAYOUT\_UNDEFINED (one member of the [**D3D11\_TEXTURE\_LAYOUT**](d3d11-texture-layout.md) enum) and no CPU access are the most efficient for frequent GPU rendering and sampling. When performance testing, those textures should be compared against D3D11\_TEXTURE\_LAYOUT\_UNDEFINED with CPU access, and D3D11\_TEXTURE\_LAYOUT\_64K\_STANDARD\_SWIZZLE with CPU access, and D3D11\_TEXTURE\_LAYOUT\_ROW\_MAJOR for cross-adapter support.

Using D3D11\_TEXTURE\_LAYOUT\_UNDEFINED with CPU access enables the methods [**WriteToSubresource**](id3d11device3-writetosubresource.md), [**ReadFromSubresource**](id3d11device3-readfromsubresource.md), [**Map**](id3d11devicecontext-map.md) (precluding application access to pointer), and [**Unmap**](id3d11devicecontext-unmap.md); but can sacrifice efficiency of GPU access. Using D3D11\_TEXTURE\_LAYOUT\_64K\_STANDARD\_SWIZZLE with CPU access enables **WriteToSubresource**, **ReadFromSubresource**, **Map** (which returns a valid pointer to application), and **Unmap**. It can also sacrifice efficiency of GPU access more than D3D11\_TEXTURE\_LAYOUT\_UNDEFINED with CPU access.

In general, applications should create the majority of textures as GPU-only-accessible, and with D3D11\_TEXTURE\_LAYOUT\_UNDEFINED.

Previous to the mapping default textures feature, there was only one standardized layout for multi-dimensional data: "linear", also known as "row-major". Applications should avoid USAGE\_STAGING and USAGE\_DYNAMIC textures when map default is available. The USAGE\_STAGING and USAGE\_DYNAMIC textures use the linear layout.

D3D11.3 (and D3D12) introduce a standard multi-dimensional data layout. This is done to enable multiple processing units to operate on the same data without copying the data or swizzling the data between multiple layouts. A standardized layout enables efficiency gains through network effects and allows algorithms to make short-cuts assuming a particular pattern.

Note though that this standard swizzle is a hardware feature, and may not be supported by all GPUs.

## D3D11.3 APIs

Unlike D3D12, D3D11.3 does not supports texture mapping by default, so you need to query [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS2**](d3d11-feature-data-d3d11-options2.md). Standard swizzle will also need to be queried for with a call to [**ID3D11Device::CheckFeatureSupport**](id3d11device-checkfeaturesupport.md) and checking the `StandardSwizzle64KBSupported` field of **D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS2**.

The following APIs reference texture mapping:

Enums

-   [**D3D11\_TEXTURE\_LAYOUT**](d3d11-texture-layout.md) : controls the swizzle pattern of default textures and enable map support on default textures.
-   [**D3D11\_FEATURE**](d3d11-feature.md) : references [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS2**](d3d11-feature-data-d3d11-options2.md).
-   [**D3D11\_TILE\_COPY\_FLAG**](d3d11-tile-copy-flags.md) : contains flags to copy swizzled tiled resources to and from linear buffers.

Structures

-   [**D3D11\_TEXTURE2D\_DESC1**](d3d11-texture2d-desc1.md) : describes a 2D texture. Note the CD3D11\_TEXTURE2D\_DESC1 helper structure.
-   [**D3D11\_TEXTURE3D\_DESC1**](d3d11-texture3d-desc1.md) : describes a 3D texture. Note the CD3D11\_TEXTURE3D\_DESC1 helper structure.

Methods

-   [**ID3D11Device3::CreateTexture2D1**](id3d11device3-createtexture2d1.md) : creates an array of 2D textures.
-   [**ID3D11Device3::CreateTexture3D1**](id3d11device3-createtexture3d1.md) : creates a single 3D texture.
-   [**ID3D11Device3::WriteToSubresource**](id3d11device3-writetosubresource.md) : copies data into a D3D11\_USAGE\_DEFAULT texture which was mapped using [**Map**](id3d11devicecontext-map.md).
-   [**ID3D11Device3::ReadFromSubresource**](id3d11device3-readfromsubresource.md) : copies data from a D3D11\_USAGE\_DEFAULT texture which was mapped using [**Map**](id3d11devicecontext-map.md).
-   [**ID3D11DeviceContext::Map**](id3d11devicecontext-map.md) : gets a pointer to the data contained in a subresource, and denies the GPU access to that subresource.
-   [**ID3D11DeviceContext::Unmap**](id3d11devicecontext-unmap.md) : invalidates the pointer to a resource and reenables the GPU's access to that resource.
-   [**ID3D11Texture2D1::GetDesc1**](id3d11texture2d1-getdesc1.md) : gets the properties of a 2D texture resource.
-   [**ID3D11Texture3D1::GetDesc1**](id3d11texture3d1-getdesc1.md) : gets the properties of a 3D texture resource.

## Related topics

<dl> <dt>

[Direct3D 11.3 Features](direct3d-11-3-features.md)
</dt> </dl>

 

 




