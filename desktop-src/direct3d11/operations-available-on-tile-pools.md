---
title: Operations available on tile pools
description: This section lists operations that you can perform on tile pools.
ms.assetid: '69CF182B-9161-43B7-89A5-0468E1BBD6B7'
---

# Operations available on tile pools

This section lists operations that you can perform on tile pools.

-   The lifetime of tile pools works like any other Direct3D Resource, backed by reference counting, including in this case tracking of mappings from tiled resources. When the application no longer references a tile pool and any tile mappings to the memory are gone and graphics processing unit (GPU) accesses completed, the operating system will deallocate the tile pool.
-   APIs related to surface sharing and synchronization work for tile pools (but not directly on tiled resources). Similar to the behavior for offered tile pools, Direct3D commands that access tiled resources that point to a tile pool are dropped if the tile pool has been shared and is currently acquired by another device and process.
-   [**ID3D11DeviceContext2::ResizeTilePool**](id3d11devicecontext2-resizetilepool.md) operation
-   [**IDXGIDevice2::OfferResources**](https://msdn.microsoft.com/library/windows/desktop/hh404549) and [**ReclaimResources**](https://msdn.microsoft.com/library/windows/desktop/hh404551) operations - These APIs for yielding memory temporarily to the system operate on the entire tile pool (and aren't available for individual tiled resources). If a tiled resource points to a tile in an offered tile pool, the tiled resource behaves as if it is offered (for example, the runtime drops commands that reference it).

Data can't be copied to and from tile pool memory directly. Accesses to the memory are always done through tiled resources.

## Related topics

<dl> <dt>

[Creating tiled resources](creating-tiled-resources.md)
</dt> </dl>

 

 




