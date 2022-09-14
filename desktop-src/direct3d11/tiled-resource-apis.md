---
title: Tiled Resource APIs
description: The APIs described in this section work with tiled resources and tile pool.
ms.assetid: 02DCF9BA-F9EA-4176-AD6F-AA620CE968BA
ms.topic: article
ms.date: 05/31/2018
---

# Tiled Resource APIs

The APIs described in this section work with tiled resources and tile pool.

-   [Assigning tiles from a tile pool to a resource](#assigning-tiles-from-a-tile-pool-to-a-resource)
-   [Querying resource tiling and support](#querying-resource-tiling-and-support)
-   [Copying tiled data](#copying-tiled-data)
-   [Resizing tile pool](#resizing-tile-pool)
-   [Tiled resource barrier](#tiled-resource-barrier)
-   [Related topics](#related-topics)

## Assigning tiles from a tile pool to a resource

The [**ID3D11DeviceContext2::UpdateTileMappings**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-updatetilemappings) and [**ID3D11DeviceContext2::CopyTileMappings**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-copytilemappings) APIs manipulate and query tile mappings. Update calls only affect the tiles identified in the call, and others are left as defined previously.

Any given tile from a tile pool can be mapped to multiple locations in a resource and even multiple resources. This mapping includes tiles in a resource that have an implementation-chosen layout ([Mipmap packing](mipmap-packing.md)) where multiple mipmaps are packed together into a single tile. The catch is that if data is written to the tile via one mapping, but read via a differently configured mapping, the results are undefined. Careful use of this flexibility can still be useful for an application though, like sharing a tile between resources that will not be used simultaneously, where the contents of the tile are always initialized through the same resource mapping as they will be subsequently read from. Similarly, a tile mapped to hold the packed mipmaps of multiple different resources with the same surface dimensions will work fine - the data will appear the same in both mappings.

Changes to tile assignments for a resource can be made at any time in an immediate or deferred context.

## Querying resource tiling and support

To query resource tiling, use [**ID3D11Device2::GetResourceTiling**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11device2-getresourcetiling).

For other resource tiling support, use [**ID3D11Device2::CheckMultisampleQualityLevels1**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11device2-checkmultisamplequalitylevels1).

## Copying tiled data

Any methods in Direct3D for moving data around work with tiled resources just as if they are not tiled, except that writes to unmapped areas are dropped and reads from unmapped areas produce 0. If a copy operation involves writing to the same memory location multiple times because multiple locations in the destination resource are mapped to the same tile memory, the resulting writes to multi-mapped tiles are non-deterministic and non-repeatable. That is, accesses happen in whatever order the hardware happens to execute the copy.

Direct3D 11.2 introduces methods for these additional ways to copy:

-   Copy between tiles in a tiled resource (at 64KB tile granularity) and (to/from) a buffer in graphics processing unit (GPU) memory (or staging resource) - [**ID3D11DeviceContext2::CopyTiles**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-copytiles)
-   Copy from application-provided memory to tiles in a tiled resource - [**ID3D11DeviceContext2::UpdateTiles**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-updatetiles)

These methods swizzle/deswizzle as needed, and allow a D3D11\_TILE\_COPY\_NO\_OVERWRITE flag when the caller promises the destination memory is not referenced by GPU work that is in flight.

The tiles involved in the copy can't include tiles that contain packed mipmaps or that have results that are undefined. To transfer data to/from mipmaps that the hardware packs into one tile, you must use the standard (non-tile specific) Copy/Update APIs or [**ID3D11DeviceContext::GenerateMips**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-generatemips) for the whole mip chain.

**Note on [**GenerateMips**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-generatemips):** Using [**ID3D11DeviceContext::GenerateMips**](/windows/desktop/api/D3D11/nf-d3d11-id3d11devicecontext-generatemips) on a resource with partially mapped tiles will produce results that simply follow the rules for reading and writing **NULL** applied to whatever algorithm the hardware and display driver happen to use to **GenerateMips**. So, it is not particularly useful for an application to bother doing this unless somehow the areas with **NULL** mappings (and their effect on other mips during the generation phase) will have no consequence on the parts of the surface the application does care about.

Copying tile data from a staging surface or from application memory would be the way to upload tiles that may have been streamed off disk, for example. A variation when streaming off disk is uploading some sort of compressed data to GPU memory and then decoding on the GPU. The decode target could be a buffer resource in GPU memory, from which [**CopyTiles**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-copytiles) then copies to the actual tiled resource. This copy step allows the GPU to swizzle when the swizzle pattern is not known. Swizzling is not needed if the tiled resource itself is a buffer resource (for example, as opposed to a Texture).

The memory layout of the tiles in the non-tiled buffer resource side of the copy is simply linear in memory within 64KB tiles, which the hardware and display driver would swizzle/deswizzle per tile as appropriate when transferring to/from a tiled resource. For multisample antialiasing (MSAA) surfaces, each pixel's samples are traversed in sample-index order before moving to the next pixel. For tiles that are partially filled on the right side (for a surface that has a width not a multiple of tile width in pixels), the pitch/stride to move down a row is the full size in bytes of the number pixels that would fit across the tile if the tile was full. So, there can be a gap between each row of pixels in memory. For specification simplicity, mipmaps smaller than a tile are not packed together in the linear layout. This seems to be a waste of memory space, but as mentioned copying to mips that the hardware packs together is not allowed via [**CopyTiles**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-copytiles) or [**UpdateTiles**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-updatetiles). The application can just use generic UpdateSubresource\*() or CopySubresource\*() APIs to copy small mips individually, though in the case of CopySubresource\*() that means the linear memory has to be the same dimension as the tiled resource - CopySubresource\*() can't copy from a buffer resource to a Texture2D for instance.

If a hardware standard swizzle is defined, flags could be added to indicate that the data in the buffer is to be interpreted in that format (no swizzle necessary on transfer), though alternative approaches to uploading data may also make sense in that case such as allowing applications direct access to tile pool memory.

Copying operations can be done on an immediate or deferred context.

## Resizing tile pool

To resize a tile pool, use [**ID3D11DeviceContext2::ResizeTilePool**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-resizetilepool).

## Tiled resource barrier

To specify a data access ordering constraint between multiple tiled resources, use [**ID3D11DeviceContext2::TiledResourceBarrier**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-tiledresourcebarrier).

## Related topics

<dl> <dt>

[Tiled resources](tiled-resources.md)
</dt> </dl>

 

 




