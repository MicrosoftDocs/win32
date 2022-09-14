---
description: A state block can be used to capture only vertex state (see State Blocks Save and Restore State (Direct3D 9)).
ms.assetid: cb898228-dc45-4a2a-a82e-8d64523e9b85
title: Saving Vertex States With a StateBlock (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Saving Vertex States With a StateBlock (Direct3D 9)

A state block can be used to capture only vertex state (see [State Blocks Save and Restore State (Direct3D 9)](state-blocks-save-and-restore-state.md)). The following state is vertex state:

-   Vertex render state (see [Vertex Pipeline: Render State](#vertex-pipeline-render-state)).
-   Vertex sampler state (see [Vertex Pipeline: Sampler State](#vertex-pipeline-sampler-state)).
-   Vertex texture state (see [Vertex Pipeline: Texture State](#vertex-pipeline-texture-state)).
-   The NPatch mode segments from [**IDirect3DDevice9::SetNPatchMode**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setnpatchmode).
-   Each light from [**IDirect3DDevice9::SetLight**](/windows/desktop/api), as well as whether or not the light is enabled with [**IDirect3DDevice9::LightEnable**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-lightenable).
-   The current vertex shader and each of the vertex shader constants.
-   For each vertex stream, store the divider value from [**IDirect3DDevice9::SetStreamSourceFreq**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setstreamsourcefreq).
-   The current vertex declaration.

To capture vertex state with a state block, specify D3DSBT\_VERTEXSTATE when calling [**IDirect3DDevice9::CreateStateBlock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createstateblock).

## Vertex Pipeline: Render State

Device render states affect the behavior of almost every part of the pipeline. Render states are set by calling [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate).

The following table includes all render states that set-up vertex state:



| Render States                           | Default Value          |
|-----------------------------------------|------------------------|
| D3DRS\_CULLMODE                         | D3DCULL\_CCW           |
| D3DRS\_FOGCOLOR                         | 0                      |
| D3DRS\_FOGTABLEMODE                     | D3DFOG\_NONE           |
| D3DRS\_FOGSTART                         | 0                      |
| D3DRS\_FOGEND                           | 1                      |
| D3DRS\_FOGDENSITY                       | 1                      |
| D3DRS\_RANGEFOGENABLE                   | **FALSE**              |
| D3DRS\_AMBIENT                          | 0                      |
| D3DRS\_COLORVERTEX                      | **TRUE**               |
| D3DRS\_FOGVERTEXMODE                    | D3DFOG\_NONE           |
| D3DRS\_CLIPPING                         | **TRUE**               |
| D3DRS\_LIGHTING                         | **TRUE**               |
| D3DRS\_LOCALVIEWER                      | **TRUE**               |
| D3DRS\_EMISSIVEMATERIALSOURCE           | D3DMCS\_MATERIAL       |
| D3DRS\_AMBIENTMATERIALSOURCE            | D3DMCS\_MATERIAL       |
| D3DRS\_DIFFUSEMATERIALSOURCE            | D3DMCS\_COLOR1         |
| D3DRS\_SPECULARMATERIALSOURCE           | D3DMCS\_COLOR2         |
| D3DRS\_VERTEXBLEND                      | D3DVBF\_DISABLE        |
| D3DRS\_CLIPPLANEENABLE                  | 0                      |
| D3DRS\_POINTSIZE                        | Driver dependent       |
| D3DRS\_POINTSIZE\_MIN                   | 1                      |
| D3DRS\_POINTSPRITEENABLE                | **FALSE**              |
| D3DRS\_POINTSCALEENABLE                 | **FALSE**              |
| D3DRS\_POINTSCALE\_A                    | 1                      |
| D3DRS\_POINTSCALE\_B                    | 0                      |
| D3DRS\_POINTSCALE\_C                    | 0                      |
| D3DRS\_MULTISAMPLEANTIALIAS             | **TRUE**               |
| D3DRS\_MULTISAMPLEMASK                  | 0xffffffff             |
| D3DRS\_PATCHEDGESTYLE                   | D3DPATCHEDGE\_DISCRETE |
| D3DRS\_POINTSIZE\_MAX                   | 1                      |
| D3DRS\_INDEXEDVERTEXBLENDENABLE         | **FALSE**              |
| D3DRS\_TWEENFACTOR                      | 0                      |
| D3DRS\_POSITIONDEGREE                   | D3DDEGREE\_CUBIC       |
| D3DRS\_NORMALDEGREE                     | D3DDEGREE\_LINEAR      |
| D3DRS\_MINTESSELLATIONLEVEL             | 1                      |
| D3DRS\_MAXTESSELLATIONLEVEL             | 1                      |
| D3DRS\_ADAPTIVETESS\_X                  | 0                      |
| D3DRS\_ADAPTIVETESS\_Y                  | 0                      |
| D3DRS\_ADAPTIVETESS\_Z                  | 1                      |
| D3DRS\_ADAPTIVETESS\_W                  | 0                      |
| D3DRS\_ENABLEADAPTIVETESSELLATION"/> | **FALSE**              |



 

## Vertex Pipeline: Sampler State

Sampler states control sampling related topics such as filtering, tiling, and texture coordinate address modes. Use [**IDirect3DDevice9::SetSamplerState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setsamplerstate) to set up the sampler state (including the one used in the tessellator unit to sample displacement maps). The sampler states have been renamed with a "D3DSAMP\_" prefix to enable compile time error detection when porting from DirectX 8.

The following table includes all sampler states that set-up vertex state:



| Sampler States      | Default Value |
|---------------------|---------------|
| D3DSAMP\_DMAPOFFSET | 256           |



 

## Vertex Pipeline: Texture State

Texture states control texture blending operations of the multi-texture blender. Use [**IDirect3DDevice9::SetTextureStageState**](/windows/desktop/api) to set-up texture states. Use [**IDirect3DDevice9::SetTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexture) to associate a texture with a sampler stage.

The following table includes all the texture states that set-up vertex state:



| Texture States                | Default Value    |
|-------------------------------|------------------|
| D3DTSS\_TEXCOORDINDEX         | 0                |
| D3DTSS\_TEXTURETRANSFORMFLAGS | D3DTTFF\_DISABLE |



 

D3DTSS\_TEXCOORDINDEX is a fixed function vertex processing state. If a programmable vertex shader is used, this state is ignored.

## Related topics

<dl> <dt>

[State Blocks Save and Restore State](state-blocks-save-and-restore-state.md)
</dt> </dl>

 

 
