---
description: The following flags are used to specify which channels in a texture to operate on.
ms.assetid: 0317b857-2512-4ad7-b6e3-82afdda7ea10
title: D3DX_FILTER
ms.topic: article
ms.date: 05/31/2018
---

# D3DX\_FILTER

The following flags are used to specify which channels in a texture to operate on.



| \#define                | Description                                                                                                                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DX\_FILTER\_NONE      | No scaling or filtering will take place. Pixels outside the bounds of the source image are assumed to be transparent black.                                                                                 |
| D3DX\_FILTER\_POINT     | Each destination pixel is computed by sampling the nearest pixel from the source image.                                                                                                                     |
| D3DX\_FILTER\_LINEAR    | Each destination pixel is computed by sampling the four nearest pixels from the source image. This filter works best when the scale on both axes is less than two.                                          |
| D3DX\_FILTER\_TRIANGLE  | Every pixel in the source image contributes equally to the destination image. This is the slowest of the filters.                                                                                           |
| D3DX\_FILTER\_BOX       | Each pixel is computed by averaging a 2x2(x2) box of pixels from the source image. This filter works only when the dimensions of the destination are half those of the source, as is the case with mipmaps. |
| D3DX\_FILTER\_MIRROR\_U | Pixels off the edge of the texture on the u-axis should be mirrored, not wrapped.                                                                                                                           |
| D3DX\_FILTER\_MIRROR\_V | Pixels off the edge of the texture on the v-axis should be mirrored, not wrapped.                                                                                                                           |
| D3DX\_FILTER\_MIRROR\_W | Pixels off the edge of the texture on the w-axis should be mirrored, not wrapped.                                                                                                                           |
| D3DX\_FILTER\_MIRROR    | Specifying this flag is the same as specifying the D3DX\_FILTER\_MIRROR\_U, D3DX\_FILTER\_MIRROR\_V, and D3DX\_FILTER\_MIRROR\_W flags.                                                                     |
| D3DX\_FILTER\_DITHER    | The resulting image must be dithered using a 4x4 ordered dither algorithm.                                                                                                                                  |
| D3DX\_FILTER\_SRGB\_IN  | Input data is in sRGB (gamma 2.2) color space.                                                                                                                                                              |
| D3DX\_FILTER\_SRGB\_OUT | The output data is in sRGB (gamma 2.2) color space.                                                                                                                                                         |
| D3DX\_FILTER\_SRGB      | Same as specifying D3DX\_FILTER\_SRGB\_IN \| D3DX\_FILTER\_SRGB\_OUT.                                                                                                                                       |



 

Each valid filter must contain exactly one of the following flags: D3DX\_FILTER\_NONE, D3DX\_FILTER\_POINT, D3DX\_FILTER\_LINEAR, D3DX\_FILTER\_TRIANGLE, or D3DX\_FILTER\_BOX. In addition, you can use the OR operator to specify zero or more of the following optional flags with a valid filter: D3DX\_FILTER\_MIRROR\_U, D3DX\_FILTER\_MIRROR\_V, D3DX\_FILTER\_MIRROR\_W, D3DX\_FILTER\_MIRROR, D3DX\_FILTER\_DITHER, D3DX\_FILTER\_SRGB\_IN, D3DX\_FILTER\_SRGB\_OUT or D3DX\_FILTER\_SRGB.

Specifying D3DX\_DEFAULT for this parameter is usually the equivalent of specifying D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER. However, D3DX\_DEFAULT can have different meanings, depending on which method uses the filter. For example:

-   When using [**D3DXCreateTextureFromFileEx**](d3dxcreatetexturefromfileex.md), D3DX\_DEFAULT maps to D3DX\_FILTER\_TRIANGLE \| D3DX\_FILTER\_DITHER.
-   When using [**D3DXFilterTexture**](d3dxfiltertexture.md), D3DX\_DEFAULT maps to D3DX\_FILTER\_BOX if the texture size is a power of two, and D3DX\_FILTER\_BOX \| D3DX\_FILTER\_DITHER otherwise.

Reference each method to check for information about how D3DX\_DEFAULT filter is mapped.

## Constant Information



|                          |            |
|--------------------------|------------|
| Header                   | d3dx9tex.h |
| Minimum operating system | Windows 98 |



 

## Related topics

<dl> <dt>

[D3DX Constants](dx9-graphics-reference-d3dx-constants.md)
</dt> </dl>

 

 



