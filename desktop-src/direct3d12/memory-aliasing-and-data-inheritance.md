---
title: Memory Aliasing and Data Inheritance
description: Placed and reserved resource may alias physical memory within a heap. Placed resources enable more data inheritance scenarios than reserved resources when the heap has the shared flag set or when the aliased resources have fully defined memory layouts.
ms.assetid: 53C5804B-0F81-41AF-83D2-A96DCDFDC94A
ms.topic: article
ms.date: 05/31/2018
---

# Memory Aliasing and Data Inheritance

Placed and reserved resource may alias physical memory within a heap. Placed resources enable more data inheritance scenarios than reserved resources when the heap has the shared flag set or when the aliased resources have fully defined memory layouts.

-   [Aliasing](#memory-aliasing-and-data-inheritance)
-   [Data Inheritance](#data-inheritance)
-   [Related topics](#related-topics)

## Aliasing

An aliasing barrier must be issued between the usage of two resources that share the same physical memory, even if data inheritance is not desired. Simple usage models must denote, at least, the destination resource involved in such an operation. See [**CreatePlacedResource**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-createplacedresource) for more details and advanced usage models.

After a resource is accessed, any resources which share physical memory with that resource become invalidated, unless data inheritance is allowed to occur. Reads of invalidated resources result in undefined resource contents. Writes to invalidated resources also result in undefined resource contents, unless two conditions occur:

-   The resource does not have either the D3D12\_RESOURCE\_FLAG\_ALLOW\_RENDER\_TARGET or D3D12\_RESOURCE\_FLAG\_ALLOW\_DEPTH\_STENCIL.
-   The write is a copy or clear operation to an entire subresource or tile. Tile-initialization is only available for resources with 64KB\_TILE\_UNDEFINED\_SWIZZLE and 64KB\_TILE\_STANDARD\_SWIZZLE.

Overlapping invalidations are scoped to smaller granularities, when layouts provide information on the location on the location of texel data and when resources are in certain transition barrier states. But, invalidations cannot go any smaller than resource alignment granularities.

A buffer alignment granularity is 64KB, and larger alignment granularity takes precedence. This is important when considering 4KB textures, as multiple 4KB textures can reside in a 64KB region without overlapping each other. But, a buffer aliasing the same 64KB region cannot be used in conjunction with any of those 4KB textures. The application cannot reliably keep the access to the buffer from intersecting the 4KB textures, as GPUs are allowed to swizzle 4KB texture data within the 64KB region in an undefined pattern.

64KB\_TILE\_UNDEFINED\_SWIZZLE, 64KB\_TILE\_STANDARD\_SWIZZLE, and ROW\_MAJOR texture layouts inform the application which overlapping alignment granularities have become invalid. For example: An application can create a 2D render target texture array with 2 array slices, a single mip level, and the 64KB\_TILE\_UNDEFINED\_SWIZZLE layout. Assume the application understands each array slice occupies 100 64KB tiles. The application can forgo using array slice 0, and re-use that memory for either a ~6MB buffer, a ~6MB texture with undefined layout, etc. Going further, assume the application no longer required the first tile of array slice 1. Then, the application could also locate a 64KB buffer there until rendering would again require the first tile of array slice 1. The application would have to do a full tile clear or copy in order to re-use the first tile with the texture array again.

However, even textures with defined layouts still have problematic cases. Texture resource sizes can significantly differ from what the application can calculate itself, because some adapter architectures allocate extra memory for textures to reduce the effective bandwidth during common rendering scenarios. Any invalidations into that extra memory region cause the entire resource to become invalidated. See [**GetResourceAllocationInfo**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-getresourceallocationinfo) for more details.

## Data Inheritance

Placed resources enable the most data inheritance for textures, even with undefined memory layouts. Applications can mimic the data inheritance capabilities that shared committed resources enable by locating two textures with identical resource properties at the same offset in a shared heap. The entire resource description must be identical, including the optimized clear value and type of resource creation method (placed or reserved). But, both resources may have had different initial transition barrier states.

Reserved resources enable per-tile data inheritance; but restrictions commonly exist for resource transition barrier states.

To inherit data, both resources must be in a compatible resource transition barrier state:

-   For buffers, simultaneous access textures, and cross-adapter textures, the resource transition state is not important and all states are “compatible”.
-   For reserved textures without the previous properties or other per-tile data inheritance through 64KB\_TILE\_UNDEFINED\_SWIZZLE or 64KB\_TILE\_STANDARD\_SWIZZLE, the resource transition barrier state including the tile must be in the common state.
-   For all other textures, where the resource descriptions match exactly, the resource transition barrier state for each corresponding pair of subresources must:
    -   Be in the common state.
    -   Be equal when the state has the same GPU-write flag in them.

When the GPU supports standard swizzle, buffers and standard swizzle textures may be aliased to the same memory and inherit data between them. The application can manipulate texels from the buffer representation, because the standard swizzle pattern describes how texels are laid out in memory. The CPU-visible swizzle pattern is equivalent to the GPU-visible swizzle pattern seen in buffers.

## Related topics

<dl> <dt>

[Suballocation Within Heaps](suballocation-within-heaps.md)
</dt> </dl>

 

 




