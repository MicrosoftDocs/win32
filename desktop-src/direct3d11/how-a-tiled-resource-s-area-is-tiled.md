---
title: How a tiled resource's area is tiled
description: When you create a tiled resource, the dimensions, format element size, and number of mipmaps and/or array slices (if applicable) determine the number of tiles that are required to back the entire surface area.
ms.assetid: 834E317F-CFFD-460C-9F89-793081BA1853
ms.topic: article
ms.date: 05/31/2018
---

# How a tiled resource's area is tiled

When you create a tiled resource, the dimensions, format element size, and number of mipmaps and/or array slices (if applicable) determine the number of tiles that are required to back the entire surface area. The pixel/byte layout within tiles is determined by the implementation. The number of pixels that fit in a tile, depending on the format element size, is fixed and identical whether you use a standard swizzle or not.

The number of tiles that will be used by a given surface size and format element width is well defined and predictable based on the tables in the following sections. For resources that contain mipmaps or cases where surface dimensions don't fill a tile, some constraints exist and are discussed in [Mipmap packing](mipmap-packing.md).

Different tiled resources can point to identical memory with different formats as long as applications don't rely on the results of writing to the memory with one format and reading with another. But, in constrained circumstances, applications can rely on the results of writing to the memory with one format and reading with another if the formats are in the same format family (that is, they have the same typeless parent format). For example, DXGI\_FORMAT\_R8G8B8A8\_UNORM and DXGI\_FORMAT\_R8G8B8A8\_UINT are compatible with each other but not with DXGI\_FORMAT\_R16G16\_UNORM. An application must conservatively match all resource properties in order to reinterpret data between two textures since tile patterns are very conservatively undefined. Obviously, though, the format is more lax. The formats need only be compatible as illustrated above. An exception is where bleeding data from one format aliasing to another is well defined: if a tile completely contains 0 for all its bits, that tile can be used with any format that interprets those memory contents as 0 (regardless of memory layout). So, a tile could be cleared to 0x00 with the format DXGI\_FORMAT\_R8\_UNORM and then used with a format like DXGI\_FORMAT\_R32G32\_FLOAT and it would appear the contents are still (0.0f,0.0f).

The layout of data within a tile may be depend on resource properties, the subresource in which it resides, and the tile location within the subresource. The major exceptions are illustrated above: compatible formats with other resource properties being equal and when all texels are the same pattern.

## In this section



| Topic                                                                                                             | Description                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Texture2D and Texture2DArray subresource tiling](texture2d-and-texture2darray-subresource-tiling.md)<br/> | These tables show how [**Texture2D**](/windows/desktop/direct3dhlsl/sm5-object-texture2d) and [**Texture2DArray**](/windows/desktop/direct3dhlsl/sm5-object-texture2darray) subresources are tiled. <br/>                                                                                                          |
| [Texture3D subresource tiling](texture3d-subresource-tiling.md)<br/>                                       | This table shows how [**Texture3D**](/windows/desktop/direct3dhlsl/sm5-object-texture3d) subresources are tiled. <br/>                                                                                                                                                                            |
| [Buffer tiling](buffer-tiling.md)<br/>                                                                     | A [Buffer](overviews-direct3d-11-resources-buffers.md) resource is divided into 64KB tiles, with some empty space in the last tile if the size is not a multiple of 64KB.<br/>                                                                                                  |
| [Mipmap packing](mipmap-packing.md)<br/>                                                                   | Depending on the [tier](tiled-resources-features-tiers.md) of tiled resources support, mipmaps with certain dimensions don't follow the standard tile shapes and are considered to all be packed together with one another in a manner that is opaque to the application. <br/> |



 

## Related topics

<dl> <dt>

[Creating tiled resources](creating-tiled-resources.md)
</dt> </dl>

 

