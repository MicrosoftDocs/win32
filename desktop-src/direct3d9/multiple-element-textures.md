---
description: Traditional textures are considered to be single-element textures.
ms.assetid: 8fe8da80-0879-413a-a7db-617d2f558b28
title: Multiple-element Textures (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Multiple-element Textures (Direct3D 9)

Traditional textures are considered to be single-element textures. Multiple-element textures enable applications to write simultaneously to multiple elements of a texture from the pixel shader. The result in the next rendering pass is that an application can use one or more of the elements as a single-element texture - that is, as inputs to the pixel shader. These additional elements can be thought of as a temporary store for intermediate results that will be used in a later pass by the application.

The first generation of hardware that exposes this feature has the following restrictions:

-   All multiple-element texture surfaces will be allocated automatically. This limitation is addressed by treating this as a new type of surface format with multiple RGBA channels interleaved.
-   All elements of the multiple element texture can have the same bit depth. This limitation is expressed by the name of the new surface formats.
-   A multiple-element texture cannot be the primary/displayable. In other words, it must be off-screen only. This limitation is expressed by the surface-format enumeration.
-   No dithering, alpha test, fogging, blending, raster-op, or masking is allowed. No post-pixel shader processing is done, except the z-test and stencil test.
-   The texture cannot be a mipmap. Creation of the mip chain will fail.
-   The same element cannot be set as a texture at the same time it is a render target. However, different elements of the same multiple-element texture surface can simultaneously be textures and render targets.
-   No antialiasing is supported.
-   Multiple-element texture surfaces, when used as a texture, cannot be filtered. This limitation can be verified using [**CheckDeviceFormat**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-checkdeviceformat).
-   Multiple-element texture surfaces cannot be locked.
-   More than one multiple-element texture surface can be used simultaneously by assigning each to various stages, just as with normal textures.
-   Multiple-element texture surfaces support conversion of gamma from 2.2 to 1.0 conversion on a read operation, just as with other texture formats.
-   Some of the implementations do not apply the output write mask (D3DRS\_COLORWRITEENABLE). Those that can have independent color write masks. This is expressed using a new capability bit. The number of independent color write masks available will be equal to the maximum number of elements of which the device is capable.
-   [**Clear**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-clear) clears all elements of the multiple-element texture which is set as the render target.

The usage of multiple-element textures follows these steps:

1.  Applications discover support for this feature by checking for the availability of multiple-element texture formats.
2.  The application creates these surfaces by calling [**CreateTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createtexture).
3.  The application sets the surface as a render target using the [**SetRenderTarget**](/windows/desktop/api) call. The pixel shader provides output to the surfaces using the [mov - ps](../direct3dhlsl/mov---ps.md) instruction.
4.  [**SetTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture) is called to set a multiple-element texture surface to a particular stage. As with other textures, the same surface is allowed to be set to multiple stages at once.
5.  [**SetSamplerState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setsamplerstate) is called to set D3DSAMP\_ELEMENTINDEX to the appropriate element number in the multiple-element texture from which the sampler samples. Default value for this state is 0, which means non-multiple-element textures will work. Setting this state to an inappropriate number results in an undefined behavior - if the multiple-element texture is only two elements wide but the sampler is asked to sample from the fourth element, for example.

## API Support

The following is a summary of the API elements that support multiple-element textures:

-   The [D3DFMT\_MULTI2\_ARGB8](d3dformat.md) surface format expresses the interleaved nature of the format.
-   The D3DSAMP\_ELEMENTINDEX sampler state indicates which element index to use.
-   The following render states support multiple-element textures:

    -   D3DRS\_COLORWRITEENABLE1
    -   D3DRS\_COLORWRITEENABLE2
    -   D3DRS\_COLORWRITEENABLE3

    D3DRS\_COLORWRITEENABLE applies to render target (or element) zero.

-   The [D3DPMISCCAPS\_INDEPENDENTWRITEMASKS](d3dpmisccaps.md) flag indicates that the device supports independent write masks for multiple element textures or multiple render targets.

## Related topics

<dl> <dt>

[Pixel Pipeline](pixel-pipeline.md)
</dt> </dl>

 

 
