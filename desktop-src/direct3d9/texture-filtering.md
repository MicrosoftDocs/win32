---
description: When Direct3D renders a primitive, it maps the 3D primitive onto a 2D screen.
ms.assetid: 'vs|directx_sdk|~\texture_filtering.htm'
title: Texture Filtering (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Texture Filtering (Direct3D 9)

When Direct3D renders a primitive, it maps the 3D primitive onto a 2D screen. If the primitive has a texture, Direct3D must use that texture to produce a color for each pixel in the primitive's 2D rendered image. For every pixel in the primitive's on-screen image, it must obtain a color value from the texture. This process is called texture filtering.

When a texture filter operation is performed, the texture being used is typically also being magnified or minified. In other words, it is being mapped into a primitive image that is larger or smaller than itself. Magnification of a texture can result in many pixels being mapped to one texel. The result can be a chunky appearance. Minification of a texture often means that a single pixel is mapped to many texels. The resulting image can be blurry or aliased. To resolve these problems, some blending of the texel colors must be performed to arrive at a color for the pixel.

Direct3D simplifies the complex process of texture filtering. It provides you with three types of texture filtering - linear filtering, anisotropic filtering, and mipmap filtering. If you select no texture filtering, Direct3D uses a technique called nearest-point sampling.

Each type of texture filtering has advantages and disadvantages. For instance, linear texture filtering can produce jagged edges or a chunky appearance in the final image. However, it is a computationally low-overhead method of texture filtering. Filtering with mipmaps usually produces the best results, especially when combined with anisotropic filtering. However, it requires the most memory of the techniques that Direct3D supports.

Applications that use texture interface pointers should set the current texture filtering method by calling the [**IDirect3DDevice9::SetSamplerState**](/windows/desktop/api) method. Set the value of the first parameter to the integer index number (0-7) of the texture for which you are selecting a texture filtering method. Pass D3DSAMP\_MAGFILTER, D3DSAMP\_MINFILTER, or D3DSAMP\_MIPFILTER for the second parameter to set the magnification, minification, or mipmapping filter. Pass a member of the [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md) enumerated type as the value in the third parameter.

This section presents the texture filtering methods that Direct3D supports. It is organized into the following topics.

-   [Nearest-Point Sampling (Direct3D 9)](nearest-point-sampling.md)
-   [Linear Texture Filtering (Direct3D 9)](linear-texture-filtering.md)
-   [Bilinear Texture Filtering (Direct3D 9)](bilinear-texture-filtering.md)
-   [Anisotropic Texture Filtering (Direct3D 9)](anisotropic-texture-filtering.md)
-   [Texture Filtering with Mipmaps (Direct3D 9)](texture-filtering-with-mipmaps.md)

> [!Note]  
> Although the texture-filtering render states present in the [**D3DRENDERSTATETYPE**](./d3drenderstatetype.md) enumerated type are superseded by texture stage states, the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate), as opposed to the IDirect3DDevice2 version, does not fail if you attempt to use them. Rather, the system maps the effects of these render states to the first stage in the multitexture cascade, stage 0. Applications should not mix the legacy render states with their corresponding texture stage states, as unpredictable results can occur.

 

## Related topics

<dl> <dt>

[Direct3D Textures](direct3d-textures.md)
</dt> </dl>

 

 
