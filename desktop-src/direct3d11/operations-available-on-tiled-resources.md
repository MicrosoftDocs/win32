---
title: Operations available on tiled resources
description: This section lists operations that you can perform on tiled resources.
ms.assetid: '1CF42A18-B6EA-4BA9-BEDE-9A8CC083CBAF'
---

# Operations available on tiled resources

This section lists operations that you can perform on tiled resources.

-   void [**ID3D11DeviceContext2::UpdateTileMappings**](id3d11devicecontext2-updatetilemappings.md) and [**ID3D11DeviceContext2::CopyTileMappings**](id3d11devicecontext2-copytilemappings.md) operations - These operations point tile locations in a tiled resource to locations in tile pools, or to NULL, or to both. These operations can update a disjoint subset of the tile pointers.
-   Copy\*() and Update\*() operations - All the APIs that can copy data to and from a default pool surface (for example, [**ID3D11DeviceContext1::CopySubresourceRegion1**](id3d11devicecontext1-copysubresourceregion1.md) and [**ID3D11DeviceContext1::UpdateSubresource1**](id3d11devicecontext1-updatesubresource1.md)) work for tiled resources. Reading from unmapped tiles produces 0 and writes to unmapped tiles are dropped.
-   [**ID3D11DeviceContext2::CopyTiles**](id3d11devicecontext2-copytiles.md) and [**ID3D11DeviceContext2::UpdateTiles**](id3d11devicecontext2-updatetiles.md) operations - These operations exist for copying tiles at 64KB granularity to and from any tiled resource and a buffer resource in a canonical memory layout. The display driver and hardware perform any memory "swizzling" necessary for the tiled resource.
-   Direct3D pipeline bindings and view creations / bindings that would work on non-tiled resources work on tiled resources as well.

Tile controls are available on immediate or deferred contexts (just like updates to typical resources) and upon execution impact subsequent accesses to the tiles (not previously submitted operations).

## Related topics

<dl> <dt>

[Creating tiled resources](creating-tiled-resources.md)
</dt> </dl>

 

 




