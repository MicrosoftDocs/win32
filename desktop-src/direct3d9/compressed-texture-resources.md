---
description: Texture maps are digitized images drawn on three-dimensional shapes to add visual detail.
ms.assetid: 0ea5cb07-a21a-4e2c-93e2-54966153bb8a
title: Compressed Texture Resources (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Compressed Texture Resources (Direct3D 9)

Texture maps are digitized images drawn on three-dimensional shapes to add visual detail. They are mapped into these shapes during rasterization, and the process can consume large amounts of both the system bus and memory. To reduce the amount of memory consumed by textures, Direct3D supports the compression of texture surfaces. Some Direct3D devices support compressed texture surfaces natively. On such devices, when you have created a compressed surface and loaded the data into it, the surface can be used in Direct3D like any other texture surface. Direct3D handles decompression when the texture is mapped to a 3D object.

## Storage Efficiency and Texture Compression

All texture compression formats are powers of two. While this does not mean that a texture is necessarily square, it does mean that both x and y are powers of two. For example, if a texture is originally 512 by 128 bytes, the next mipmapping would be 256 by 64 and so on, with each level decreasing by a power of two. At lower levels, where the texture is filtered to 16 by 2 and 8 by 1, there will be wasted bits because the compression block is always a 4 by 4 block of texels. Unused portions of the block are padded. Although there are wasted bits at the lowest levels, the overall gain is still significant. The worst case is, in theory, a 2K by 1 texture (2⁰ power). Here, only a single row of pixels is encoded per block, while the rest of the block is unused.

## Mixing Formats Within a Single Texture

It is important to note that any single texture must specify that its data is stored as 64 or 128 bits per group of 16 texels. If 64-bit blocks - that is, format DXT1 - are used for the texture, it is possible to mix the opaque and 1-bit alpha formats on a per-block basis within the same texture. In other words, the comparison of the unsigned integer magnitude of color\_0 and color\_1 is performed uniquely for each block of 16 texels.

Once the 128-bit blocks are used, the alpha channel must be specified in either explicit (format DXT2 and DXT3) or interpolated mode (format DXT4 and DXT5) for the entire texture. As with color, when interpolated mode (format DXT4 and DXT5) is selected, then either eight interpolated alphas or six interpolated alphas mode can be used on a block-by-block basis. Again the magnitude comparison of alpha\_0 and alpha\_1 is done uniquely on a block-by-block basis.

Direct3D provides services to compress surfaces that are used for texturing 3D models. This section provides information about creating and manipulating the data in a compressed texture surface.

Information is contained in the following topics.

-   [Opaque and 1-Bit Alpha Textures (Direct3D 9)](opaque-and-1-bit-alpha-textures.md)
-   [Textures with Alpha Channels (Direct3D 9)](textures-with-alpha-channels.md)
-   [Compressed Texture Formats (Direct3D 9)](compressed-texture-formats.md)
-   [Using Compressed Textures (Direct3D 9)](using-compressed-textures.md)

## Related topics

<dl> <dt>

[Direct3D Textures](direct3d-textures.md)
</dt> </dl>

 

 



