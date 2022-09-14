---
title: Tier 2
description: This section describes tier 2 support.
ms.assetid: 4A4AEF13-2F0F-482E-9262-256C257ED85A
ms.topic: article
ms.date: 05/31/2018
---

# Tier 2

This section describes tier 2 support.

-   Hardware at Feature Level 11.1 minimum.
-   All features of the previous tier (without [Tier 1](tier-1.md) specific limitations) plus the additions in these following items:
-   Shader instructions for clamping LOD and mapped status feedback are available. For more info, see [HLSL tiled resources exposure](hlsl-tiled-resources-exposure.md).
-   Reads from non-mapped tiles return 0 in all non-missing components of the format, and the default for missing components.
-   Writes to non-mapped tiles are stopped from going to memory but might end up in caches that subsequent reads to the same address might or might not pick up.
-   Texture filtering with a footprint that straddles **NULL** and non-**NULL** tiles contributes 0 (with defaults for missing format components) for texels on **NULL** tiles into the overall filter operation. Some early hardware don't meet this requirement and returns 0 (with defaults for missing format components) for the full filter result if any texels (with nonzero weight) fall on a **NULL** tile. No other hardware will be allowed to miss the requirement to include all (nonzero weighted) texels in the filter operation.
-   **NULL** texel accesses cause the [**CheckAccessFullyMapped**](/windows/desktop/direct3dhlsl/checkaccessfullymapped) operation on the status feedback for a texture read to return false. This is regardless of how the texture access result might get write masked in the shader and how many components are in the texture format (the combination of which might make it appear that the texture does not need to be accessed).
-   Alignment constraints for standard tile shapes: Mipmaps that fill at least one standard tile in all dimensions are guaranteed to use the standard tiling, with the remainder considered packed as a **unit** into N tiles (N reported to the application). The application can map the N tiles into arbitrarily disjoint locations in a tile pool, but must either map all or none of the packed tiles. The mip packing is a unique set of packed tiles per array slice.
-   Min/Max reduction filtering is supported. For info about Min/Max reduction filtering, see [Tiled resources texture sampling features](tiled-resources-texture-sampling-features.md).
-   Tiled resources with any mipmaps less than standard tile size in any dimension are not allowed to have an array size larger than 1.
-   Limitations on how tiles can be accessed when there are duplicate mappings, described in [Tile access limitations with duplicate mappings](tile-access-limitations-with-duplicate-mappings-.md), continue to apply.

## Related topics

<dl> <dt>

[Tiled resources features tiers](tiled-resources-features-tiers.md)
</dt> </dl>

 

 