---
title: Tile pool resizing
description: Use the ID3D11DeviceContext2 ResizeTilePool API to grow a tile pool if the application needs more working set for the tiled resources mapping into it or to shrink if less space is needed.
ms.assetid: 529E874E-650B-4BFD-97F6-E66E743564A9
ms.topic: article
ms.date: 05/31/2018
---

# Tile pool resizing

Use the [**ID3D11DeviceContext2::ResizeTilePool**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-resizetilepool) API to grow a tile pool if the application needs more working set for the tiled resources mapping into it or to shrink if less space is needed. Another option for applications is to allocate additional tile pools for new tiled resources. But if any single tiled resource needs more space than initially available in its tile pool, growing the tile pool is a good option. A tiled resource can't have mappings into multiple tile pools at the same time.

When a tile pool is grown, additional tiles are added to the end via one or more new allocations by the display driver. This breakdown into allocations isn't visible to the application. Existing memory in the tile pool is left untouched, and existing tiled resource mappings into that memory remain intact.

When a tile pool is shrunk, tiles are removed from the end. Tiles are removed even below the initial allocation size, down to 0, which means new mappings can't be made past the new size. But, existing mappings past the end of the new size remain intact and useable. The display driver will keep the memory around as long as mappings to any part of the allocations that the driver uses for the tile pool memory remains. If after shrinking some memory has been kept alive because tile mappings are pointing to it and then the tile pool is regrown again (by any amount), the existing memory is reused first before any additional allocations occur to service the size of the grow operation.

To be able to save memory, an application has to not only shrink a tile pool but also remove/remap existing mappings past the end of the new smaller tile pool size.

The act of shrinking (and removing mappings) doesn't necessarily produce immediate memory savings. Freeing of memory depends on how granular the display driver's underlying allocations for the tile pool are. When shrinking happens to be enough to make a display driver allocation unused, the display driver can free it. If a tile pool was grown, shrinking to previous sizes (and removing/remapping tile mappings correspondingly) is most likely to yield memory savings, though not guaranteed in the case that the sizes don't exactly align with the underlying allocation sizes chosen by the display driver.

## Related topics

<dl> <dt>

[Mappings are into a tile pool](mappings-are-into-a-tile-pool.md)
</dt> </dl>

 

 




