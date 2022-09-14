---
title: Creating tiled resources
description: Tiled resources are created by specifying the D3D11\_RESOURCE\_MISC\_TILED flag when you create a resource.
ms.assetid: DED2B70C-1E95-4A85-A818-FD32165FBF6C
ms.topic: article
ms.date: 05/31/2018
---

# Creating tiled resources

Tiled resources are created by specifying the [**D3D11\_RESOURCE\_MISC\_TILED**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag) flag when you create a resource.

Restrictions on when you can use [**D3D11\_RESOURCE\_MISC\_TILED**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag) to create a resource are described in [Tiled resource creation parameters](tiled-resource-creation-parameters.md).

A non-tiled resource's storage is allocated in the graphics system when the resource is created. For example, when you call [**ID3D11Device::CreateTexture2D**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createtexture2d) to create an array of 2D textures, the graphics system allocates storage for those 2D textures. When a tiled resource is created, the graphics system doesn't allocate the storage for the resource contents. Instead, when an application creates a tiled resource, the graphics system makes an address space reservation for the tiled surface's area only, and then allows the mapping of the tiles to be controlled by the application. The "mapping" of a tile is simply the physical location in memory that a logical tile in a resource points to (or **NULL** for an unmapped tile). Don't confuse this concept with the notion of mapping a Direct3D resource for CPU access, which despite using the same name is completely independent. You will be able to define and change the mapping of each tile individually as needed, knowing that all tiles for a surface don't need to be mapped at a time, thereby making effective use of the amount of memory available.

This section provides more info about how to create tiled resources.

## In this section



| Topic                                                                                                             | Description                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Mappings are into a tile pool](mappings-are-into-a-tile-pool.md)<br/>                                     | When a resource is created with the [**D3D11\_RESOURCE\_MISC\_TILED**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag) flag, the tiles that make up the resource come from pointing at locations in a tile pool. A tile pool is a pool of memory (backed by one or more allocations behind the scenes - unseen by the application). <br/> |
| [Tiled resource creation parameters](tiled-resource-creation-parameters.md)<br/>                           | There are some constraints on the type of Direct3D resources that you can create with the [**D3D11\_RESOURCE\_MISC\_TILED**](/windows/desktop/api/D3D11/ne-d3d11-d3d11_resource_misc_flag) flag. This section provides the valid parameters for creating tiled resources.<br/>                                                |
| [Address space available for tiled resources](address-space-available-for-tiled-resources.md)<br/>         | This section specifies the virtual address space that is available for tiled resources. <br/>                                                                                                                                                                                                                           |
| [Tile pool creation parameters](tile-pool-creation-parameters.md)<br/>                                     | Use the parameters in this section to define tile pools via the [**ID3D11Device::CreateBuffer**](/windows/desktop/api/D3D11/nf-d3d11-id3d11device-createbuffer) API. <br/>                                                                                                                                                                              |
| [Tiled resource cross process and device sharing](tiled-resource-cross-process-and-device-sharing.md)<br/> | Tile pools can be shared with other processes just like traditional resources. Tiled resources that reference tile pools can't be shared across devices and processes. But separate processes can create their own tiled resources that map to tile pools that are shared between those tiled resources. <br/>          |
| [Operations available on tiled resources](operations-available-on-tiled-resources.md)<br/>                 | This section lists operations that you can perform on tiled resources.<br/>                                                                                                                                                                                                                                             |
| [Operations available on tile pools](operations-available-on-tile-pools.md)<br/>                           | This section lists operations that you can perform on tile pools.<br/>                                                                                                                                                                                                                                                  |
| [How a tiled resource's area is tiled](how-a-tiled-resource-s-area-is-tiled.md)<br/>                       | When you create a tiled resource, the dimensions, format element size, and number of mipmaps and/or array slices (if applicable) determine the number of tiles that are required to back the entire surface area. <br/>                                                                                                 |



 

## Related topics

<dl> <dt>

[Tiled resources](tiled-resources.md)
</dt> </dl>

 

 





