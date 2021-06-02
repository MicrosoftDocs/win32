---
description: The distortion visible in the texels of a 3D object whose surface is oriented at an angle with respect to the plane of the screen is called anisotropy.
ms.assetid: f6c8a9e2-aab0-4f06-956e-bb86557c72e7
title: Anisotropic Texture Filtering (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Anisotropic Texture Filtering (Direct3D 9)

The distortion visible in the texels of a 3D object whose surface is oriented at an angle with respect to the plane of the screen is called anisotropy. When a pixel from an anisotropic primitive is mapped to texels, its shape is distorted. Direct3D measures the anisotropy of a pixel as the elongation - that is, length divided by width - of a screen pixel that is inverse-mapped into texture space.

You can use anisotropic texture filtering in conjunction with linear texture filtering or mipmap texture filtering to improve rendering results. Your application enables anisotropic texture filtering by calling the [**IDirect3DDevice9::SetSamplerState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setsamplerstate) method. Set the value of the first parameter to the integer index number (0-7) of the texture for which you are selecting a texture filtering method. Pass D3DSAMP\_MAGFILTER, D3DSAMP\_MINFILTER, or D3DSAMP\_MIPFILTER for the second parameter to set the magnification, minification, or mipmapping filter. Set the third parameter to D3DTEXF\_ANISOTROPIC.

Your application must also set the degree of anisotropy to a value greater than one. Do this by calling the [**IDirect3DDevice9::SetSamplerState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setsamplerstate) method. Set the value of the first parameter to the integer index number (0-7) of the texture for which you are setting the degree of isotropy. Pass D3DSAMP\_MAXANISOTROPY as the value of the second parameter. The final parameter should be the degree of isotropy.

You can disable isotropic filtering by setting the degree of isotropy to one; any value larger than one enables it. Check the MaxAnisotropy flag in the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure to determine the possible range of values for the degree of anisotropy.

## Related topics

<dl> <dt>

[Texture Filtering](texture-filtering.md)
</dt> </dl>

 

 
