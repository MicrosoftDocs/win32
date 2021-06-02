---
description: The lighting engine combines material color, vertex color, and lighting information to generate a per-vertex color.
ms.assetid: 1e7c31cb-dc63-4f4a-9ddc-d1d1d0b69085
title: Alpha Texture Blending (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Alpha Texture Blending (Direct3D 9)

The lighting engine combines material color, vertex color, and lighting information to generate a per-vertex color. Once interpolated, this generates a per-pixel color that is written to the frame buffer. If an application enables texture blending, the pixel color will become a combination of the current pixel in the frame buffer and a texture color.

This formula determines the final blended pixel color:


```
Color = TexelColor x SourceBlend + CurrentPixelColor x DestBlend
```



Where:

-   Color is the output pixel color.
-   TexelColor is the input color after texture filtering.
-   SourceBlend is the percentage of the final pixel color that is made up of the source texel color.
-   CurrentPixelColor is the color of the current pixel.
-   DestBlend is the percentage of the final pixel color that is made up of the current pixel color.

The final blending equation is set by calling [**IDirect3DDevice9::SetRenderState**](/windows/desktop/api) and specifying the blend render state (D3DRS\_BLENDXXX) with a corresponding blending factor ([**D3DBLEND**](./d3dblend.md)). The values of SourceBlend and DestBlend range from 0.0 (transparent) to 1.0 (opaque) inclusive. In addition, an application can control the transparency of a pixel by setting the alpha value in a texture. In this case, use the following:


```
SourceBlend = D3DBLEND_ZERO 
DestBlend = D3DBLEND_ONE
```



The blending equation will cause the rendered pixel to be transparent. The default values are:


```
SourceBlend = D3DBLEND_SRCALPHA 
DestBlend = D3DBLEND_INVSRCALPHA
```



## Related topics

<dl> <dt>

[Texture Blending](texture-blending.md)
</dt> <dt>

[Texture Filtering (Direct3D 9)](texture-filtering.md)
</dt> <dt>

[**D3DRENDERSTATETYPE**](./d3drenderstatetype.md)
</dt> </dl>

 

 
