---
title: Volume Tiled Resources
description: Volume (3D) textures can be used as tiled resources, noting that tile resolution is three-dimensional.
ms.assetid: 'B6BF22A2-EDA3-4765-B545-BF825043D4C4'
---

# Volume Tiled Resources

Volume (3D) textures can be used as tiled resources, noting that tile resolution is three-dimensional.

-   [Overview](#overview)
-   [D3D11.3 Tiled Resource APIs](#d3d113-tiled-resource-apis)
-   [Related topics](#related-topics)

## Overview

Tiled resources decouple a D3D Resource object from its backing memory (resources in the past had a 1:1 relationship with their backing memory). This allows for a variety of interesting scenarios such as streaming in texture data and reusing or reducing memory usage

2D texture tiled resources are supported in D3D11.2. D3D12 and D3D11.3 add support for 3D tiled textures.

The typical resource dimensions used in tiling are 4 x 4 tiles for 2D textures, and 4 x 4 x 4 tiles for 3D textures.



|                             |                                     |
|-----------------------------|-------------------------------------|
| Bits/pixel (1 sample/pixel) | Tile dimensions (pixels, w x h x d) |
| 8                           | 64x32x32                            |
| 16                          | 32x32x32                            |
| 32                          | 32x32x16                            |
| 64                          | 32x16x16                            |
| 128                         | 16x16x16                            |
| BC 1,4                      | 128x64x16                           |
| BC 2,3,5,6,7                | 64x64x16                            |



 

Note the following formats are not supported with tiled resources: 96bpp formats, video formats, R1\_UNORM, R8G8\_B8G8\_UNORM, R8R8\_G8B8\_UNORM.

In the diagrams below dark gray represents NULL tiles.

-   [Texture 3D Tiled Resource default mapping (most detailed mip)](#texture-3d-tiled-resource-default-mapping-most-detailed-mip)
-   [Texture 3D Tiled Resource default mapping (second most detailed mip)](#texture-3d-tiled-resource-default-mapping-second-most-detailed-mip)
-   [Texture 3D Tiled Resource (most detailed mip)](#texture-3d-tiled-resource-most-detailed-mip)
-   [Texture 3D Tiled Resource (second most detailed mip)](#texture-3d-tiled-resource-second-most-detailed-mip)
-   [Texture 3D Tiled Resource (Single Tile)](#texture-3d-tiled-resource-single-tile)
-   [Texture 3D Tiled Resource (Uniform Box)](#texture-3d-tiled-resource-uniform-box)

### Texture 3D Tiled Resource default mapping (most detailed mip)

![default mapping of the most detailed mip](images/vtr-tex3d-default-1.png)

### Texture 3D Tiled Resource default mapping (second most detailed mip)

![default mapping of the second most detailed mip](images/vtr-tex3d-default-2.png)

### Texture 3D Tiled Resource (most detailed mip)

The following code sets up a 3D tiled resource at the most detailed mip.

``` syntax
D3D11_TILED_RESOURCE_COORDINATE trCoord;
trCoord.X = 1;
trCoord.Y = 0;
trCoord.Z = 0;
trCoord.Subresource = 0;

D3D11_TILE_REGION_SIZE trSize;
trSize.bUseBox = false;
trSize.NumTiles = 63;
```

![most detailed mapping of a 3d tiled resource](images/vtr-tex3d-default-1b.png)

### Texture 3D Tiled Resource (second most detailed mip)

The following code sets up a 3D tiled resource, and the second most detailed mip:

``` syntax
D3D11_TILED_RESOURCE_COORDINATE trCoord;
trCoord.X = 1;
trCoord.Y = 0;
trCoord.Z = 0;
trCoord.Subresource = 1;

D3D11_TILE_REGION_SIZE trSize;
trSize.bUseBox = false;
trSize.NumTiles = 6;
```

![second most detailed mapping of a 3d tiled resource](images/vtr-tex3d-default-2b.png)

### Texture 3D Tiled Resource (Single Tile)

The following code sets up a Single Tile resource:

``` syntax
D3D11_TILED_RESOURCE_COORDINATE trCoord;
trCoord.X = 1;
trCoord.Y = 1;
trCoord.Z = 1;
trCoord.Subresource = 0;

D3D11_TILE_REGION_SIZE trSize;
trSize.bUseBox = true;
trSize.NumTiles = 27;
trSize.Width = 3;
trSize.Height = 3;
trSize.Depth = 3;
```

![a single tile](images/vtr-tex3d-single.png)

### Texture 3D Tiled Resource (Uniform Box)

The following code sets up a Uniform Box tiled resource (note the statement `trSize.bUseBox = true;) :`

``` syntax
D3D11_TILED_RESOURCE_COORDINATE trCoord;
trCoord.X = 0;
trCoord.Y = 1;
trCoord.Z = 0;
trCoord.Subresource = 0;

D3D11_TILE_REGION_SIZE trSize;
trSize.bUseBox = true;
trSize.NumTiles = 27;
trSize.Width = 3;
trSize.Height = 3;
trSize.Depth = 3;
```

![a uniform box](images/vtr-tex3d-uniform.png)

## D3D11.3 Tiled Resource APIs

The same API calls are used for both 2D and 3D tiled resources:

Enums

-   [**D3D11\_TILED\_RESOURCES\_TIER**](d3d11-tiled-resources-tier.md) : determines the level of tiled resource support.
-   [**D3D11\_FORMAT\_SUPPORT2**](d3d11-format-support2.md) : used to test for tiled resource support.
-   [**D3D11\_CHECK\_MULTISAMPLE\_QUALITY\_LEVELS\_FLAG**](d3d11-check-multisample-quality-levels-flags.md) : determines tiled resource support in a multi-sampling resource.
-   [**D3D11\_TILE\_COPY\_FLAGS**](d3d11-tile-copy-flags.md) : holds flags for copying to and from swizzled tiled resources and linear buffers.

Structures

-   [**D3D11\_TILED\_RESOURCE\_COORDINATE**](d3d11-tiled-resource-coordinate.md) : holds the x, y, and z co-ordinate, and subresource reference. Note there is a helper class: CD3D11\_TILED\_RESOURCE\_COORDINATE.
-   [**D3D11\_TILE\_REGION\_SIZE**](d3d11-tile-region-size.md) : specifies the size, and number of tiles, of the tiled region.
-   [**D3D11\_TILE\_SHAPE**](d3d11-tile-shape.md) : the tile shape as a width, height and depth in texels.
-   [**D3D11\_FEATURE\_DATA\_D3D11\_OPTIONS1**](d3d11-feature-data-d3d11-options1.md): holds the supported tile resource tier level.

Methods

-   [**ID3D11Device::CheckFeatureSupport**](id3d11device-checkfeaturesupport.md) : used to determine what features, and at what tier, are supported by the current hardware.
-   [**ID3D11DeviceContext2::CopyTiles**](id3d11devicecontext2-copytiles.md) : copies tiles from buffer to tiled resource or vice versa.
-   [**ID3D11DeviceContext2::UpdateTileMappings**](id3d11devicecontext2-updatetilemappings.md) : updates mappings of tile locations in tiled resources to memory locations in a tile pool.
-   [**ID3D11DeviceContext2::CopyTileMappings**](id3d11devicecontext2-copytilemappings.md) : copies mappings from a source tiled resource to a destination tiled resource.
-   [**ID3D11DeviceContext2::GetResourceTiling**](id3d11device2-getresourcetiling.md) : gets info about how a tiled resource is broken into tiles.

## Related topics

<dl> <dt>

[Direct3D 11.3 Features](direct3d-11-3-features.md)
</dt> </dl>

 

 




