---
title: Tile access limitations with duplicate mappings
description: This section describes tile access limitations with duplicate mappings.
ms.assetid: 7A498E0D-9151-4A89-B7C3-C4F476457D17
ms.topic: article
ms.date: 05/31/2018
---

# Tile access limitations with duplicate mappings

This section describes tile access limitations with duplicate mappings.

## Copying tiled resources with overlapping source and destination

If tiles in the source and destination area of a Copy\* operation have duplicated mappings in the copy area that would have overlapped even if both resources were not tiled resources and the Copy\* operation supports overlapping copies, the Copy\* operation will behave fine (as if the source is copied to a temporary location before going to the destination). But if the overlap is not obvious (like the source and destination resources are different but share mappings or mappings are duplicated over a given surface), results of the copy operation on the tiles that are shared are undefined.

## Copying to tiled resource with duplicated tiles in destination area

Copying to a tiled resource with duplicated tiles in the destination area produces undefined results in these tiles unless the data itself is identical; different tiles might write the tiles in different orders.

## UAV accesses to duplicate tiles mappings

Suppose an unordered access view (UAV) on a tiled resource has duplicate tile mappings in its area or with other resources bound to the pipeline. Ordering of accesses to these duplicated tiles is undefined if performed by different threads, just as any ordering of memory access to UAVs in general is unordered.

## Rendering after tile mapping changes or content updates from outside mappings

If a tiled resource's tile mappings have changed or content in mapped tiled pool tiles have changed via another tiled resource's mappings, and the tiled resource is going to be rendered via render target view or depth stencil view, the application must Clear (using the fixed function Clear APIs) or fully copy over using Copy\*/Update\* APIs the tiles that have changed within the area being rendered (mapped or not). Failure of an application to clear or copy in these cases results in hardware optimization structures for the given render target view or depth stencil view being stale and will result in garbage rendering results on some hardware and inconsistency across different hardware. These hidden optimization data structures used by hardware might be local to individual mappings and not visible to other mappings to the same memory.

The [**ID3D11DeviceContext1::ClearView**](/windows/desktop/api/D3D11_1/nf-d3d11_1-id3d11devicecontext1-clearview) operation supports clearing render target views with rectangles. For hardware that supports tiled resources, **ClearView** must also support clearing of depth stencil views with rectangles, for depth only surfaces (without stencil). This operation allows applications to clear only the necessary area of a surface.

If an application needs to preserve existing memory contents of areas in a tiled resource where mappings have changed, that application must work around the clear requirement. The application can accomplish this work-around by first saving the contents where tile mappings have changed (by copying them to a temporary surface, for example, by using [**ID3D11DeviceContext2::CopyTiles**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-copytiles)), issuing the required clear command and then copying the contents back. While this would accomplish the task of preserving surface contents for incremental rendering, the downside is that subsequent rendering performance on the surface might suffer because rendering optimizations might be lost.

If a tile is mapped into multiple tiled resources at the same time and tile contents are manipulated by any means (render, copy, and so on) via one of the tiled resources, if the same tile is to be rendered via any other tiled resource, the tile must be cleared first as previously described.

## Rendering to tiles shared outside render area

Suppose an area in a tiled resource is being rendered to and the tile pool tiles referenced by the render area are also mapped to from outside the render area (including via other tiled resources, at the same time or not). Data rendered to these tiles isn't guaranteed to appear correctly when viewed through the other mappings, even though the underlying memory layout is compatible. This fact is due to optimization data structures some hardware use that can be local to individual mappings for renderable surfaces and not visible to other mappings to the same memory location. You can work around this restriction by copying from the rendered mapping to all the other mappings to the same memory that might be accessed (or clearing that memory or copying other data to it if the old contents are no longer needed). While this work-around seems redundant, it makes all other mappings to the same memory correctly understand how to access its contents, and at least the memory savings of having only a single physical memory backing remains intact. Also, when you switch between using different tiled resources that share mappings (unless only reading), you must call the [**ID3D11DeviceContext2::TiledResourceBarrier**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-tiledresourcebarrier) API in between the switches.

## Rendering to tiles shared within render area

If an area in a tiled resource is being rendered to and within the render area multiple tiles are mapped to the same tile pool location, rendering results are undefined on those tiles.

## Data compatibility across tiled resources sharing tiles

Suppose multiple tiled resources have mappings to the same tile pool locations and each resource is used to access the same data. This scenario is only valid if the other rules about avoiding problems with hardware optimization structures are avoided, appropriate calls to [**ID3D11DeviceContext2::TiledResourceBarrier**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-tiledresourcebarrier) are made, and the tiled resources are compatible with each other. The latter is described here in terms of what it means for tiled resources sharing tiles to be incompatible. The incompatibility conditions of accessing the same data across duplicate tile mappings are the use of different surface dimensions or format, or differences in the presence of render target or depth stencil bind flags on the resources. Writing to the memory with one type of mapping produces undefined results if you subsequently read or render via a mapping from an incompatible resource. If the other resource sharing mappings are first initialized with new data (recycling the memory for a different purpose), the subsequent read or render operation is fine since data isn't bleeding across incompatible interpretations. But, you must call the **TiledResourceBarrier** API when you switch between accessing incompatible mappings like this.

If the render target or depth stencil bind flag isn't set on any of the resources sharing mappings with each other, there are far fewer restrictions. As long as the format and surface types (for example, Texture2D) are the same, tiles can be shared. Different formats being compatible are cases such as BC\* surfaces and the equivalent sized uncompressed 32 bit or 16 bit per component format, like BC6H and R32G32B32A32. Many 32 bit per element formats can be aliased with R32\_\* as well (R10G10B10A2\_\*, R8G8B8A8\_\*, B8G8R8A8\_\*,B8G8R8X8\_\*,R16G16\_\*); this operation has always been allowed for non-tiled resources.

Sharing between packed and non-packed tiles is fine if the formats are compatible and the tiles are filled with solid color.

Finally, if nothing is common about the resources sharing tile mappings except that none have render target or depth stencil bind flags, only memory filled with 0 can be shared safely; the mapping will appear as whatever 0 decodes to for the definition of the given resource format (typically just 0).

## Related topics

<dl> <dt>

[Pipeline access to tiled resources](pipeline-access-to-tiled-resources.md)
</dt> </dl>

 

 




