---
title: Tier 1
description: This section describes tier 1 support.
ms.assetid: 8E2907D2-EFCB-4F97-9B40-6835A65D3DE5
ms.topic: article
ms.date: 05/31/2018
---

# Tier 1

This section describes tier 1 support.

-   Hardware at feature level 11.0 minimum.
-   No quilting support.
-   No Texture1D or Texture3D support.
-   No 2, 8 or 16 sample multisample antialiasing (MSAA) support. Only 4x is required, except no 128 bpp formats.
-   No standard swizzle pattern (layout within 64KB tiles and tail mip packing is up to the hardware vendor).
-   Limitations on how tiles can be accessed when there are duplicate mappings, described in [Tile access limitations with duplicate mappings](tile-access-limitations-with-duplicate-mappings-.md).

### Limitations affecting tier 1 only

-   Tiled resources can have **NULL** mappings but reading from them or writing to them produces undefined results, including device removed. Applications can get around this by mapping a single dummy page to all the empty areas. Take care if you write and render to a page that is mapped to multiple render target locations because the order of writes will be undefined.
-   Shader instructions for clamping LOD and mapped status feedback are not available. For more info, see [HLSL tiled resources exposure](hlsl-tiled-resources-exposure.md).
-   Alignment constraints for standard tile shapes: It is only guaranteed that mips (starting from the finest) whose dimensions are all multiples of the standard tile size support the standard tile shapes and can have individual tiles arbitrarily mapped/unmapped. The first mipmap in a tiled resource that has any dimension not a multiple of standard tile size, along with all coarser mipmaps, can have a non-standard tiling shape, fitting into N 64KB tiles for this set of mips at once (N reported to the application). These N tiles are considered packed as one unit, which must be either fully mapped or fully unmapped by the application at any given time, though the mappings of each of the N tiles can be at arbitrarily disjoint locations in a tile pool.
-   Tiled resources with any mipmaps not a multiple of standard tile size in all dimensions are not allowed to have an array size larger than 1.
-   In order to switch between referencing tiles in a tile pool via a [Buffer](overviews-direct3d-11-resources-buffers.md) resource to referencing the same tiles via a [Texture](overviews-direct3d-11-resources-textures.md) resource, or vice-versa, the most recent call to [**UpdateTileMappings**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-updatetilemappings) or [**CopyTileMappings**](/windows/desktop/api/D3D11_2/nf-d3d11_2-id3d11devicecontext2-copytilemappings) that defines mappings to those tile pool tiles must be for the same resource dimension (Buffer versus Texture\*) as the resource dimension that will be used to access the tiles. Otherwise, behavior is undefined including the chance of device reset. So, for example, calling **UpdateTileMappings** to define tile mappings for a Buffer, then **UpdateTileMappings** to the same tiles in the tile pool via a [**Texture2D**](/windows/desktop/direct3dhlsl/sm5-object-texture2d) resource, then accessing the tiles via the Buffer is invalid. Work-around operations are to either redefine tile mappings for a resource when switching between Buffer and Texture (or vice versa) sharing tiles or just never sharing tiles in a tile pool between Buffer resources and Texture resources.
-   Min/Max reduction filtering is not supported. For info about Min/Max reduction filtering, see [Tiled resources texture sampling features](tiled-resources-texture-sampling-features.md).

## Related topics

<dl> <dt>

[Tiled resources features tiers](tiled-resources-features-tiers.md)
</dt> </dl>

 

 