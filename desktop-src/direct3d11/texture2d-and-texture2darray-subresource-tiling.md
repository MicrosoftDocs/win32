---
title: Texture2D and Texture2DArray subresource tiling
description: These tables show how Texture2D and Texture2DArray subresources are tiled.
ms.assetid: 3CFA384D-2C49-4BB2-9A92-FC45B1A499B5
ms.topic: article
ms.date: 05/31/2018
---

# Texture2D and Texture2DArray subresource tiling

These tables show how [**Texture2D**](/windows/desktop/direct3dhlsl/sm5-object-texture2d) and [**Texture2DArray**](/windows/desktop/direct3dhlsl/sm5-object-texture2darray) subresources are tiled. The values in these tables don't count tail mip packing.

This table shows how [**Texture2D**](/windows/desktop/direct3dhlsl/sm5-object-texture2d) and [**Texture2DArray**](/windows/desktop/direct3dhlsl/sm5-object-texture2darray) subresources with multisample counts of 1 are tiled.



| Bits/Pixel (1 sample/pixel) | Tile Dimensions (Pixels, WxH) |
|-----------------------------|-------------------------------|
| 8                           | 256x256                       |
| 16                          | 256x128                       |
| 32                          | 128x128                       |
| 64                          | 128x64                        |
| 128                         | 64x64                         |
| BC1,4                       | 512x256                       |
| BC2,3,5,6,7                 | 256x256                       |



 

Format bit counts not supported with tiled resources are 96 bpp formats, video formats, DXGI\_FORMAT\_R1\_UNORM, DXGI\_FORMAT\_R8G8\_B8G8\_UNORM, and DXGI\_FORMAT\_R8R8\_G8B8\_UNORM.

This table shows how [**Texture2D**](/windows/desktop/direct3dhlsl/sm5-object-texture2d) and [**Texture2DArray**](/windows/desktop/direct3dhlsl/sm5-object-texture2darray) subresources with various multisample counts are tiled.



| Multisample Count           | Divide Tile Dimensions Above by (WxH) |
|-----------------------------|-------------------------------|
| 1                           | 1x1                           |
| 2                           | 2x1                           |
| 4                           | 2x2                           |
| 8                           | 4x2                           |
| 16                          | 4x4                           |



 

Only sample counts 1 and 4 are required (and allowed) to be supported with tiled resources. Tiled resources don't currently support 2, 8, and 16 even though they are shown.

Implementations can choose to support 2, 8, and/or 16 sample multisample antialiasing (MSAA) mode for non-tiled resources even though tiled resource don't support them.

Tiled resources with sample counts larger than 1 can't use 128 bpp formats.

## Related topics

<dl> <dt>

[How a tiled resource's area is tiled](how-a-tiled-resource-s-area-is-tiled.md)
</dt> </dl>

 

 