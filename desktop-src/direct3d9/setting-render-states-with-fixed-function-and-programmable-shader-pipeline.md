---
title: Set device state on fixed-function, shader pipelines
description: This section provides the key differences between setting device state with the fixed-function and programmable shader pipeline.
ms.assetid: FF0F2A97-F75A-4AF0-8F5A-EA687523E753
ms.topic: article
ms.date: 05/31/2018
---

# Set device state on fixed-function, shader pipelines

This section provides the key differences between setting device state with the fixed-function and programmable shader pipeline.

Here are the device states that you can set for just a fixed-function pipeline:

-   Fixed-function transform and lighting: [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) with D3DRS\_SHADEMODE, D3DRS\_SPECULARENABLE, D3DRS\_LIGHTING, D3DRS\_AMBIENT, D3DRS\_COLORVERTEX, D3DRS\_LOCALVIEWER, D3DRS\_NORMALIZENORMALS, D3DRS\_DIFFUSEMATERIALSOURCE, D3DRS\_SPECULARMATERIALSOURCE, D3DRS\_AMBIENTMATERIALSOURCE, D3DRS\_EMISSIVEMATERIALSOURCE, D3DRS\_VERTEXBLEND, D3DRS\_INDEXEDVERTEXBLENDENABLE, D3DRS\_TWEENFACTOR, [**IDirect3DDevice9::LightEnable**](/windows/desktop/api), [**IDirect3DDevice9::MultiplyTransform**](/windows/desktop/api), [**IDirect3DDevice9::SetFVF**](/windows/desktop/api), [**IDirect3DDevice9::SetLight**](/windows/desktop/api), [**IDirect3DDevice9::SetMaterial**](/windows/desktop/api), [**IDirect3DDevice9::SetTransform**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settransform)
-   Fixed-function pixel shader: [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) with D3DRS\_TEXTUREFACTOR, [**IDirect3DDevice9::SetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexturestagestate)
-   Fog: [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) with D3DRS\_FOGENABLE, D3DRS\_FOGCOLOR, D3DRS\_FOGTABLEMODE, D3DRS\_FOGSTART, D3DRS\_FOGEND, D3DRS\_FOGDENSITY, D3DRS\_RANGEFOGENABLE, D3DRS\_FOGVERTEXMODE

Here are the device render states that you can set with [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) for both fixed-function and programmable shader pipelines:

-   Render Target state: D3DRS\_COLORWRITEENABLE, D3DRS\_COLORWRITEENABLE1, D3DRS\_COLORWRITEENABLE2, D3DRS\_COLORWRITEENABLE3, D3DRS\_SRGBWRITEENABLE
-   Depth state: D3DRS\_ZENABLE, D3DRS\_ZWRITEENABLE, D3DRS\_ZFUNC, D3DRS\_SLOPESCALEDEPTHBIAS, D3DRS\_DEPTHBIAS
-   Stencil state: D3DRS\_STENCILENABLE, D3DRS\_STENCILFAIL, D3DRS\_STENCILZFAIL, D3DRS\_STENCILPASS, D3DRS\_STENCILFUNC, D3DRS\_STENCILREF, D3DRS\_STENCILMASK, D3DRS\_STENCILWRITEMASK, D3DRS\_TWOSIDEDSTENCILMODE, D3DRS\_CCW\_STENCILFAIL, D3DRS\_CCW\_STENCILZFAIL, D3DRS\_CCW\_STENCILPASS, D3DRS\_CCW\_STENCILFUNC
-   Alpha Blending: D3DRS\_SRCBLEND, D3DRS\_DESTBLEND, D3DRS\_BLENDOP, D3DRS\_BLENDFACTOR, D3DRS\_SEPARATEALPHABLENDENABLE, D3DRS\_SRCBLENDALPHA, D3DRS\_DESTBLENDALPHA, D3DRS\_BLENDOPALPHA
-   Alpha Test: D3DRS\_ALPHATESTENABLE, D3DRS\_ALPHAREF, D3DRS\_ALPHAFUNC
-   Rasterizer state: D3DRS\_FILLMODE, D3DRS\_LASTPIXEL, D3DRS\_DITHERENABLE (16-bit surfaces)
-   Culling: D3DRS\_CULLMODE
-   Clipping: D3DRS\_CLIPPING, D3DRS\_CLIPPLANEENABLE
-   Scissors: D3DRS\_SCISSORTESTENABLE
-   Texture samplers: D3DRS\_WRAP0, D3DRS\_WRAP1, D3DRS\_WRAP2, D3DRS\_WRAP3, D3DRS\_WRAP4, D3DRS\_WRAP5, D3DRS\_WRAP6, D3DRS\_WRAP7, D3DRS\_WRAP8, D3DRS\_WRAP9, D3DRS\_WRAP10, D3DRS\_WRAP11, D3DRS\_WRAP12, D3DRS\_WRAP13, D3DRS\_WRAP14, D3DRS\_WRAP15
-   Anti-aliasing: D3DRS\_MULTISAMPLEANTIALIAS, D3DRS\_MULTISAMPLEMASK, D3DRS\_ANTIALIASEDLINEENABLE
-   Point sprites : D3DRS\_POINTSIZE, D3DRS\_POINTSIZE\_MIN, D3DRS\_POINTSPRITEENABLE, D3DRS\_POINTSIZE\_MAXD3DRS\_POINTSCALEENABLE, D3DRS\_POINTSCALE\_A, D3DRS\_POINTSCALE\_B, D3DRS\_POINTSCALE\_C
-   N-patches: D3DRS\_PATCHEDGESTYLE, D3DRS\_POSITIONDEGREE, D3DRS\_NORMALDEGREE, D3DRS\_MINTESSELLATIONLEVEL, D3DRS\_MAXTESSELLATIONLEVEL, D3DRS\_ADAPTIVETESS\_X, D3DRS\_ADAPTIVETESS\_Y, D3DRS\_ADAPTIVETESS\_Z, D3DRS\_ADAPTIVETESS\_W, D3DRS\_ENABLEADAPTIVETESSELLATION

## Related topics

<dl> <dt>

[Advanced Topics](advanced-topics.md)
</dt> </dl>

 

 
