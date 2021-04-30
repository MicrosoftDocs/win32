---
description: This section contains information about the internal organization of compressed texture formats.
ms.assetid: a916d635-2be4-48be-ba70-a743b2969553
title: Compressed Texture Formats (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Compressed Texture Formats (Direct3D 9)

This section contains information about the internal organization of compressed texture formats. You do not need these details to use compressed textures, because you can use D3DX functions for conversion to and from compressed formats. However, this information is useful if you want to operate on compressed surface data directly.

Direct3D uses a compression format that divides texture maps into 4x4 texel blocks. If the texture contains no transparency - is opaque - or if the transparency is specified by a 1-bit alpha, an 8-byte block represents the texture map block. If the texture map does contain transparent texels, using an alpha channel, a 16-byte block represents it.

-   [Opaque and 1-Bit Alpha Textures (Direct3D 9)](opaque-and-1-bit-alpha-textures.md)
-   [Textures with Alpha Channels (Direct3D 9)](textures-with-alpha-channels.md)

Any single texture must specify that its data is stored as 64 or 128 bits per group of 16 texels. If 64-bit blocks - that is, format DXT1 - are used for the texture, it is possible to mix the opaque and 1-bit alpha formats on a per-block basis within the same texture. In other words, the comparison of the unsigned integer magnitude of color\_0 and color\_1 is performed uniquely for each block of 16 texels.

When 128-bit blocks are used, the alpha channel must be specified in either explicit (format DXT2 or DXT3) or interpolated mode (format DXT4 or DXT5) for the entire texture. As with color, when interpolated mode is selected, either eight interpolated alphas or six interpolated alphas mode can be used on a block-by-block basis. Again the magnitude comparison of alpha\_0 and alpha\_1 is done uniquely on a block-by-block basis.

The pitch for DXTn formats is different from what was returned in DirectX 7.0. Pitch is now measured in bytes (not blocks). For example, if you have a width of 16, then you will have a pitch of four blocks (4\*8 for DXT1, 4\*16 for DXT2-5).

## Related topics

<dl> <dt>

[Compressed Texture Resources](compressed-texture-resources.md)
</dt> </dl>

 

 



