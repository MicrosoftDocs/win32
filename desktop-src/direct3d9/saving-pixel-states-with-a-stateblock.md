---
description: A state block can be used to capture only pixel state (see State Blocks Save and Restore State (Direct3D 9)).
ms.assetid: 30624c0a-e30f-4383-bc0c-b43f42403e72
title: Saving Pixel State With a StateBlock (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Saving Pixel State With a StateBlock (Direct3D 9)

A state block can be used to capture only pixel state (see [State Blocks Save and Restore State (Direct3D 9)](state-blocks-save-and-restore-state.md)). The following state is pixel state:

-   Pixel render state (see [Pixel Pipeline: Render State](#pixel-pipeline-render-state)).
-   Pixel texture state (see [Pixel Pipeline: Texture State](#pixel-pipeline-texture-state)).
-   Pixel sampler state (see [Pixel Pipeline: Sampler State](#pixel-pipeline-sampler-state)).
-   The current pixel shader and each of the pixel shader constants.

To capture pixel state with a state block, specify D3DSBT\_PIXELSTATE when calling [**IDirect3DDevice9::CreateStateBlock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createstateblock).

## Pixel Pipeline: Render State

Device render states affect the behavior of almost every part of the pipeline. Render states are set by calling [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate).

The following table includes all render states that set-up pixel state:



| Render States                              | Default Value      |
|--------------------------------------------|--------------------|
| D3DRS\_ZENABLE                             | D3DZB\_FALSE       |
| D3DRS\_SPECULARENABLE                      | **FALSE**          |
| [**D3DFILLMODE**](./d3dfillmode.md)   | D3DFILL\_SOLID     |
| [**D3DSHADEMODE**](./d3dshademode.md) | D3DSHADE\_GOURAUD  |
| D3DRS\_ZWRITEENABLE                        | **TRUE**           |
| D3DRS\_ALPHATESTENABLE                     | **FALSE**          |
| D3DRS\_LASTPIXEL                           | **TRUE**           |
| D3DRS\_SRCBLEND                            | D3DBLEND\_ONE      |
| D3DRS\_DESTBLEND                           | D3DBLEND\_ZERO     |
| D3DRS\_ZFUNC                               | D3DCMP\_LESSEQUAL  |
| D3DRS\_ALPHAREF                            | 0                  |
| D3DRS\_ALPHAFUNC                           | D3DCMP\_ALWAYS     |
| D3DRS\_DITHERENABLE                        | **FALSE**          |
| D3DRS\_FOGSTART                            | 0                  |
| D3DRS\_FOGEND                              | 1                  |
| D3DRS\_FOGDENSITY                          | 1                  |
| D3DRS\_ALPHABLENDENABLE                    | **FALSE**          |
| D3DRS\_DEPTHBIAS                           | 0                  |
| D3DRS\_STENCILENABLE                       | **FALSE**          |
| D3DRS\_STENCILFAIL                         | D3DSTENCILOP\_KEEP |
| D3DRS\_STENCILZFAIL                        | D3DSTENCILOP\_KEEP |
| D3DRS\_STENCILPASS                         | D3DSTENCILOP\_KEEP |
| D3DRS\_STENCILFUNC                         | D3DCMP\_ALWAYS     |
| D3DRS\_STENCILREF                          | 0                  |
| D3DRS\_STENCILMASK                         | 0xffffffff         |
| D3DRS\_STENCILWRITEMASK                    | 0xffffffff         |
| D3DRS\_TEXTUREFACTOR                       | 0xffffffff         |
| D3DRS\_WRAP0                               | 0                  |
| D3DRS\_WRAP1                               | 0                  |
| D3DRS\_WRAP2                               | 0                  |
| D3DRS\_WRAP3                               | 0                  |
| D3DRS\_WRAP4                               | 0                  |
| D3DRS\_WRAP5                               | 0                  |
| D3DRS\_WRAP6                               | 0                  |
| D3DRS\_WRAP7                               | 0                  |
| D3DRS\_WRAP8                               | 0                  |
| D3DRS\_WRAP9                               | 0                  |
| D3DRS\_WRAP10                              | 0                  |
| D3DRS\_WRAP11                              | 0                  |
| D3DRS\_WRAP12                              | 0                  |
| D3DRS\_WRAP13                              | 0                  |
| D3DRS\_WRAP14                              | 0                  |
| D3DRS\_WRAP15                              | 0                  |
| D3DRS\_LOCALVIEWER                         | **TRUE**           |
| D3DRS\_EMISSIVEMATERIALSOURCE              | D3DMCS\_MATERIAL   |
| D3DRS\_AMBIENTMATERIALSOURCE               | D3DMCS\_MATERIAL   |
| D3DRS\_DIFFUSEMATERIALSOURCE               | D3DMCS\_COLOR1     |
| D3DRS\_SPECULARMATERIALSOURCE              | D3DMCS\_COLOR2     |
| D3DRS\_COLORWRITEENABLE                    | 0x0000000f         |
| [**D3DBLENDOP**](./d3dblendop.md)     | D3DBLENDOP\_ADD    |
| D3DRS\_SCISSORTESTENABLE                   | **FALSE**          |
| D3DRS\_SLOPESCALEDEPTHBIAS                 | 0                  |
| D3DRS\_ANTIALIASEDLINEENABLE               | **FALSE**          |
| D3DRS\_TWOSIDEDSTENCILMODE                 | **FALSE**          |
| D3DRS\_CCW\_STENCILFAIL                    | D3DSTENCILOP\_KEEP |
| D3DRS\_CCW\_STENCILZFAIL                   | D3DSTENCILOP\_KEEP |
| D3DRS\_CCW\_STENCILPASS                    | D3DSTENCILOP\_KEEP |
| D3DRS\_CCW\_STENCILFUNC                    | D3DCMP\_ALWAYS     |
| D3DRS\_COLORWRITEENABLE1                   | 0x0000000f         |
| D3DRS\_COLORWRITEENABLE2                   | 0x0000000f         |
| D3DRS\_COLORWRITEENABLE3                   | 0x0000000f         |
| D3DRS\_BLENDFACTOR                         | 0xffffffff         |
| D3DRS\_SRGBWRITEENABLE                     | 0                  |
| D3DRS\_SEPARATEALPHABLENDENABLE            | **FALSE**          |
| D3DRS\_SRCBLENDALPHA                       | D3DBLEND\_ONE      |
| D3DRS\_DESTBLENDALPHA                      | D3DBLEND\_ZERO     |
| D3DRS\_BLENDOPALPHA                        | D3DBLENDOP\_ADD    |



 

## Pixel Pipeline: Sampler State

Sampler states control sampling related topics such as filtering, tiling, and texture coordinate address modes. Use [**IDirect3DDevice9::SetSamplerState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setsamplerstate) to set up the sampler state (including the one used in the tessellator unit to sample displacement maps). The sampler states have been renamed with a "D3DSAMP\_" prefix to enable compile time error detection when porting from DirectX 8.

The following table includes all sampler states that set-up pixel state:



| Sampler States         | Default Value     |
|------------------------|-------------------|
| D3DSAMP\_ADDRESSU      | D3DTADDRESS\_WRAP |
| D3DSAMP\_ADDRESSV      | D3DTADDRESS\_WRAP |
| D3DSAMP\_ADDRESSW      | D3DTADDRESS\_WRAP |
| D3DSAMP\_BORDERCOLOR   | 0x00000000        |
| D3DSAMP\_MAGFILTER     | D3DTEXF\_POINT    |
| D3DSAMP\_MINFILTER     | D3DTEXF\_POINT    |
| D3DSAMP\_MIPFILTER     | D3DTEXF\_NONE     |
| D3DSAMP\_MIPMAPLODBIAS | 0                 |
| D3DSAMP\_MAXMIPLEVEL   | 0                 |
| D3DSAMP\_MAXANISOTROPY | 1                 |
| D3DSAMP\_SRGBTEXTURE   | 0                 |
| D3DSAMP\_ELEMENTINDEX  | 0                 |



 

## Pixel Pipeline: Texture State

Texture states control texture blending operations of the multi-texture blender. Use [**IDirect3DDevice9::SetTextureStageState**](/windows/desktop/api) to set-up texture stage states. Use [**IDirect3DDevice9::SetTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture) to associate a texture with a sampler stage.

The following table includes all the texture states that set-up pixel state:



| Texture States                | Default Value    |
|-------------------------------|------------------|
| D3DTSS\_COLOROP               | D3DTOP\_DISABLE  |
| D3DTSS\_COLORARG1             | D3DTA\_TEXTURE   |
| D3DTSS\_COLORARG2             | D3DTA\_CURRENT   |
| D3DTSS\_ALPHAOP               | D3DTOP\_DISABLE  |
| D3DTSS\_ALPHAARG1             | D3DTA\_TEXTURE   |
| D3DTSS\_ALPHAARG2             | D3DTA\_CURRENT   |
| D3DTSS\_BUMPENVMAT00          | 0                |
| D3DTSS\_BUMPENVMAT01          | 0                |
| D3DTSS\_BUMPENVMAT10          | 0                |
| D3DTSS\_BUMPENVMAT11          | 0                |
| D3DTSS\_TEXCOORDINDEX         | 0                |
| D3DTSS\_BUMPENVLSCALE         | 0                |
| D3DTSS\_BUMPENVLOFFSET        | 0                |
| D3DTSS\_TEXTURETRANSFORMFLAGS | D3DTTFF\_DISABLE |
| D3DTSS\_COLORARG0             | D3DTA\_CURRENT   |
| D3DTSS\_ALPHAARG0             | D3DTA\_CURRENT   |
| D3DTSS\_RESULTARG             | D3DTA\_CURRENT   |



 

## Related topics

<dl> <dt>

[State Blocks Save and Restore State](state-blocks-save-and-restore-state.md)
</dt> </dl>

 

 
