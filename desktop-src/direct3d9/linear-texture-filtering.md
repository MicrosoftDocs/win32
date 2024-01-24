---
description: Direct3D uses a form of linear texture filtering called bilinear filtering.
ms.assetid: 'vs|directx_sdk|~\linear_texture_filtering.htm'
title: Linear Texture Filtering (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Linear Texture Filtering (Direct3D 9)

Direct3D uses a form of linear texture filtering called bilinear filtering. Like [Nearest-Point Sampling (Direct3D 9)](nearest-point-sampling.md), bilinear texture filtering first computes a texel address, which is usually not an integer address. Bilinear filtering then finds the texel whose integer address is closest to the computed address. In addition, the Direct3D rendering module computes a weighted average of the texels that are immediately above, below, to the left of, and to the right of the nearest sample point.

Select bilinear texture filtering by invoking the [**IDirect3DDevice9::SetSamplerState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setsamplerstate) method. Set the value of the first parameter to the integer index number (0-7) of the texture for which you are selecting a texture filtering method. Pass D3DSAMP\_MAGFILTER, D3DSAMP\_MINFILTER, or D3DSAMP\_MIPFILTER for the second parameter to set the magnification, minification, or mipmapping filter. Pass D3DTEXF\_LINEAR in the third parameter.

## Related topics

<dl> <dt>

[Texture Filtering](texture-filtering.md)
</dt> </dl>

 

 
