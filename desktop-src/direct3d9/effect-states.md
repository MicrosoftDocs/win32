---
description: Effect states are used to initialize pipeline states in preparation for vertex and pixel processing.
ms.assetid: b62a6ccc-a1ea-455c-9659-544d4bcaf6a2
title: Effect States (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Effect States (Direct3D 9)

Effect states are used to initialize pipeline states in preparation for vertex and pixel processing.


```
effect state [ [index] ] = expression;
```



Where:

-   effect state - Similar to the traditional fixed function pipeline states. A complete list of states is provided below.
-   \[ \[index\] \] - Optional integer index. The index identifies a particular state within an array of effect states. The outer brackets indicate that an index is optional. If an index is used, be sure to use the inner brackets.
-   expression - State assignment expression. See [Expressions (Direct3D 9)](expressions.md).

Each state has a native data type. This is the data type that the state expects values to be in when the effect assigns them. The data types that each state expects are listed below.

Note that the effect interface will attempt to cast values to the appropriate type as early as possible. Literal values can be cast at compile time. Non-literals (i.e. regular variables) need to be cast when the appropriate Set methods are called. For example, the effect interface will cast values set using [**SetBool**](id3dxbaseeffect--setbool.md), [**SetValue**](id3dxbaseeffect--setvalue.md), and other similar functions if necessary. For better performance ensure that the values passed to the effect interface are already the correct type and will not need casting. If the runtime is unable to cast a value, an error is returned.

Effect states can be broken up into the following categories:

-   [Light States](#light-states)
-   [Material States](#material-states)
-   [Render States](#render-states)
    -   [Pixel Pipe Render States](#pixel-pipe-render-states)
    -   [Vertex Pipe Render States](#vertex-pipe-render-states)
-   [Sampler States](#sampler-states)
-   [Sampler Stage States](#sampler-stage-states)
-   [Shader States](#shader-states)
-   [Shader Constant States](#shader-constant-states)
-   [Texture States](#texture-states)
-   [Texture Stage States](#texture-stage-states)
-   [Transform States](#transform-states)

## Light States

To enable the best performance for applying an effect, all components of a light or a material should be specified in the effect file. States that you fail to declare are set to some default value because there is no way for Direct3D to set light states individually.



| Light State            | Type   | Values                                                                                                              |
|------------------------|--------|---------------------------------------------------------------------------------------------------------------------|
| LightAmbient\[n\]      | float4 | See the Ambient member of [**D3DLIGHT9**](d3dlight9.md).                                                           |
| LightAttenuation0\[n\] | float  | See the Attenuation0 member of [**D3DLIGHT9**](d3dlight9.md).                                                      |
| LightAttenuation1\[n\] | float  | See the Attenuation1 member of [**D3DLIGHT9**](d3dlight9.md).                                                      |
| LightAttenuation2\[n\] | float  | See the Attenuation2 member of [**D3DLIGHT9**](d3dlight9.md).                                                      |
| LightDiffuse\[n\]      | float4 | See the Diffuse member of [**D3DLIGHT9**](d3dlight9.md).                                                           |
| LightDirection\[n\]    | float3 | See the Direction member of [**D3DLIGHT9**](d3dlight9.md).                                                         |
| LightEnable\[n\]       | bool   | **TRUE** or **FALSE**. See the bEnable argument in [**LightEnable**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-lightenable).            |
| LightFalloff\[n\]      | float  | [**D3DCOLORVALUE**](d3dcolorvalue.md). See the Falloff member of [**D3DLIGHT9**](d3dlight9.md).                   |
| LightPhi\[n\]          | float  | See the Phi member of [**D3DLIGHT9**](d3dlight9.md).                                                               |
| LightPosition\[n\]     | float3 | See the Position member of [**D3DLIGHT9**](d3dlight9.md).                                                          |
| LightRange\[n\]        | float  | See the Range member of [**D3DLIGHT9**](d3dlight9.md).                                                             |
| LightSpecular\[n\]     | float4 | See the Specular member of [**D3DLIGHT9**](d3dlight9.md).                                                          |
| LightTheta\[n\]        | float  | See the Theta member of [**D3DLIGHT9**](d3dlight9.md).                                                             |
| LightType\[n\]         | dword  | Same value as the array of up to n [**D3DLIGHTTYPE**](./d3dlighttype.md) values without the D3DLIGHT\_ prefix. |



 

Example:


```
LightEnable[0] = TRUE;
LightType[0] = POINT;
LightPosition[0] = float3<10.0f, 1.0f, 23.0f>;
LightAmbient[0] = float4<0.7f, 0.0f, 0.0f, 1.0f>;
```



This will enable lighting, make point lighting the type, set the light position to float3<10.0f, 1.0f, 23.0f>, and set the ambient color to float4<0.7f, 0.0f, 0.0f, 1.0f>.

## Material States

States that you fail to declare are set to some default value because there is no way for Direct3D to set material states individually.



| Material State   | Type   | Values                                         |
|------------------|--------|------------------------------------------------|
| MaterialAmbient  | float4 | Same value as [**Ambient**](d3dmaterial9.md)  |
| MaterialDiffuse  | float4 | Same value as [**Diffuse**](d3dmaterial9.md)  |
| MaterialEmissive | float4 | Same value as [**Emissive**](d3dmaterial9.md) |
| MaterialPower    | float  | Same value as [**Power**](d3dmaterial9.md)    |
| MaterialSpecular | float4 | Same value as [**Specular**](d3dmaterial9.md) |



 

Example:


```
MaterialDiffuse = float4<0.7f, 0.0f, 0.0f, 1.0f>;
MaterialPower = 3.0f;
```



This will set the diffuse color to float4<0.7f, 0.0f, 0.0f, 1.0f> and make the power of the material 3.0f.

## Render States

There are two types of render states:

-   [Pixel Pipe Render States](#pixel-pipe-render-states)
-   [Vertex Pipe Render States](#vertex-pipe-render-states)

### Pixel Pipe Render States

Effect file render states have names similar to the fixed function pipeline states, often with the prefix removed.

| Render State | Type | Values |
|-|-|-|
| AlphaBlendEnable | bool | True or False. Same values as D3DRS_ALPHABLENDENABLE in <a href="/windows/desktop/direct3d9/d3drenderstatetype"><strong>D3DRENDERSTATETYPE</strong></a>. | 
| AlphaFunc | dword | Same values as <a href="/windows/desktop/direct3d9/d3dcmpfunc"><strong>D3DCMPFUNC</strong></a> without the D3DCMP_ prefix. See D3DRS_ALPHAFUNC. | 
| AlphaRef | dword | Same values as D3DRS_ALPHAREF. | 
| AlphaTestEnable | dword | True or False. See D3DRS_ALPHATESTENABLE. | 
| BlendOp | dword | Same values as <a href="/windows/desktop/direct3d9/d3dblendop"><strong>D3DBLENDOP</strong></a> without the D3DBLENDOP_ prefix. | 
| ColorWriteEnable | dword | Bitwise combination of RED|GREEN|BLUE|ALPHA. See D3DRS_COLORWRITEENABLE. | 
| DepthBias | float | Same values as D3DRS_DEPTHBIAS. | 
| DestBlend | dword | Same values as <a href="/windows/desktop/direct3d9/d3dblend"><strong>D3DBLEND</strong></a> without the D3DBLEND_ prefix. | 
| DitherEnable | bool | True or False. Same values as D3DRS_DITHERENABLE. | 
| FillMode | dword | Same values as <a href="/windows/desktop/direct3d9/d3dfillmode"><strong>D3DFILLMODE</strong></a> without the D3DFILL_ prefix. | 
| LastPixel | dword | True or False. See D3DRS_LASTPIXEL. | 
| ShadeMode | dword | Same values as <a href="/windows/desktop/direct3d9/d3dshademode"><strong>D3DSHADEMODE</strong></a> without the D3DSHADE_ prefix. | 
| SlopeScaleDepthBias | float | Same values as D3DRS_SLOPESCALEDEPTHBIAS. | 
| SrcBlend | dword | Same values as <a href="/windows/desktop/direct3d9/d3dblend"><strong>D3DBLEND</strong></a> without the D3DBLEND_ prefix. | 
| SRGBWriteEnable | bool | True or False. Same values as D3DRS_SRGBWRITEENABLE. | 
| StencilEnable | bool | True or False. Same values as D3DRS_STENCILENABLE. | 
| StencilFail | dword | Same values as <a href="d3dstencilcaps.md">D3DSTENCILCAPS</a> without the D3DSTENCILCAP_ prefix. See D3DRS_STENCILFAIL. | 
| StencilFunc | dword | Same values as <a href="/windows/desktop/direct3d9/d3dcmpfunc"><strong>D3DCMPFUNC</strong></a> without the D3DCMP_ prefix. See D3DRS_STENCILFUNC. | 
| StencilMask | dword | Same values as D3DRS_STENCILMASK. | 
| StencilPass | dword | Same values as <a href="d3dstencilcaps.md">D3DSTENCILCAPS</a> without the D3DSTENCILCAP_ prefix. See D3DRS_STENCILPASS. | 
| StencilRef | int | Same values as D3DRS_STENCILREF. | 
| StencilWriteMask | dword | Same values as D3DRS_STENCILWRITEMASK. | 
| StencilZFail | dword | Same values as <a href="d3dstencilcaps.md">D3DSTENCILCAPS</a> without the D3DSTENCILCAP_ prefix. See D3DRS_STENCILZFAIL. | 
| TextureFactor | dword | Same values as <a href="d3dcolor.md"><strong>D3DCOLOR</strong></a>. Same values as D3DRS_TEXTUREFACTOR. | 
| Wrap0 - Wrap15 | dword | Values are the same as the values used by D3DRS_WRAP0. Valid values are:<ul><li>COORD0 (which corresponds to D3DWRAPCOORD_0)</li><li>COORD1 (which corresponds to D3DWRAPCOORD_1)</li><li>COORD2 (which corresponds to D3DWRAPCOORD_2)</li><li>COORD3 (which corresponds to D3DWRAPCOORD_3)</li><li>U (which corresponds to D3DWRAP_U)</li><li>V (which corresponds to D3DWRAP_V)</li><li>W (which corresponds to D3DWRAP_W)</li></ul> | 
| ZEnable | dword | Same values as <a href="/windows/desktop/direct3d9/d3dzbuffertype"><strong>D3DZBUFFERTYPE</strong></a> without the D3DZB_ prefix. | 
| ZFunc | dword | Same values as <a href="/windows/desktop/direct3d9/d3dcmpfunc"><strong>D3DCMPFUNC</strong></a> without the D3DCMP_ prefix. See D3DRS_ZFUNC. | 
| ZWriteEnable | bool | True or False. See D3DRS_ZWRITEENABLE. | 

Example:

```
AlphaBlendEnable = TRUE;
FillMode = WIREFRAME;
```

This will enable alpha blending and make all geometries render in wireframe.

### Vertex Pipe Render States

Effect file render states have names similar to the fixed function pipeline states, often with the prefix removed.



| Render State             | Type   | Values                                                                                                                                        |
|--------------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Ambient                  | float4 | Same values as D3DRS\_AMBIENT.                                                                                                                |
| AmbientMaterialSource    | dword  | Same values as [**D3DMATERIALCOLORSOURCE**](./d3dmaterialcolorsource.md) without the D3DMCS\_ prefix. See D3DRS\_AMBIENTMATERIALSOURCE.  |
| Clipping                 | bool   | True or False. Same values as D3DRS\_CLIPPING.                                                                                                |
| ClipPlaneEnable          | dword  | Bitwise combination of D3DCLIPPLANE0 - D3DCLIPPLANE5 macros. See [**D3DCLIPPLANEn**](d3dclipplanen.md) and D3DRS\_CLIPPLANEENABLE.           |
| ColorVertex              | bool   | True or False. Same values as D3DRS\_COLORVERTEX.                                                                                             |
| CullMode                 | dword  | Same values as [**D3DCULL**](./d3dcull.md) without the D3DCULL\_ prefix.                                                                 |
| DiffuseMaterialSource    | dword  | Same values as [**D3DMATERIALCOLORSOURCE**](./d3dmaterialcolorsource.md) without the D3DMCS\_ prefix. See D3DRS\_DIFFUSEMATERIALSOURCE.  |
| EmissiveMaterialSource   | dword  | Same values as [**D3DMATERIALCOLORSOURCE**](./d3dmaterialcolorsource.md) without the D3DMCS\_ prefix. See D3DRS\_EMISSIVEMATERIALSOURCE. |
| FogColor                 | dword  | Same values as [**D3DCOLOR**](d3dcolor.md). See D3DRS\_FOGCOLOR.                                                                             |
| FogDensity               | float  | Same values as D3DRS\_FOGDENSITY.                                                                                                             |
| FogEnable                | bool   | True or False. Same values as D3DRS\_FOGENABLE.                                                                                               |
| FogEnd                   | float  | Same values as D3DRS\_FOGEND.                                                                                                                 |
| FogStart                 | float  | Same values as D3DRS\_FOGSTART.                                                                                                               |
| FogTableMode             | dword  | Same values as [**D3DFOGMODE**](./d3dfogmode.md). See D3DRS\_FOGTABLEMODE in [**D3DRENDERSTATETYPE**](./d3drenderstatetype.md).     |
| FogVertexMode            | dword  | Same values as [**D3DFOGMODE**](./d3dfogmode.md) without the D3DFOG\_ prefix.                                                            |
| IndexedVertexBlendEnable | bool   | True or False. Same values as D3DRS\_INDEXEDVERTEXBLENDENABLE.                                                                                |
| Lighting                 | bool   | True or False. Same values as D3DRS\_LIGHTING.                                                                                                |
| LocalViewer              | bool   | True or False. Same values as D3DRS\_LOCALVIEWER.                                                                                             |
| MultiSampleAntialias     | bool   | Same values as D3DRS\_MULTISAMPLEANTIALIAS.                                                                                                   |
| MultiSampleMask          | dword  | Same values as D3DRS\_MULTISAMPLEMASK.                                                                                                        |
| NormalizeNormals         | bool   | True or False. Same values as D3DRS\_NORMALIZENORMALS.                                                                                        |
| PatchSegments            | float  | Same values as nSegments in [**SetNPatchMode**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setnpatchmode).                                                         |
| PointScale\_A            | float  | Same values as D3DRS\_POINTSCALE\_A.                                                                                                          |
| PointScale\_B            | float  | Same values as D3DRS\_POINTSCALE\_B.                                                                                                          |
| PointScale\_C            | float  | Same values as D3DRS\_POINTSCALE\_C.                                                                                                          |
| PointScaleEnable         | bool   | Same values as D3DRS\_POINTSCALEENABLE.                                                                                                       |
| PointSize                | float  | Same values as D3DRS\_POINTSIZE.                                                                                                              |
| PointSize\_Min           | float  | Same values as D3DRS\_POINTSIZE\_MIN.                                                                                                         |
| PointSize\_Max           | float  | Same values as D3DRS\_POINTSIZE\_MAX without the D3DRS\_ prefix.                                                                              |
| PointSpriteEnable        | bool   | True or False. Same values as D3DRS\_POINTSPRITEENABLE.                                                                                       |
| RangeFogEnable           | bool   | True or False. Same values as D3DRS\_RANGEFOGENABLE.                                                                                          |
| SpecularEnable           | bool   | True or False. Same values as D3DRS\_SPECULARENABLE.                                                                                          |
| SpecularMaterialSource   | dword  | Same values as [**D3DMATERIALCOLORSOURCE**](./d3dmaterialcolorsource.md) without the D3DMCS\_ prefix. See D3DRS\_SPECULARMATERIALSOURCE. |
| TweenFactor              | float  | Same values as D3DRS\_TWEENFACTOR.                                                                                                            |
| VertexBlend              | dword  | Same values as [**D3DVERTEXBLENDFLAGS**](./d3dvertexblendflags.md) without the D3DVBF\_ prefix. See D3DRS\_VERTEXBLEND.                  |



 

Example:


```
Ambient = float4<0.7f, 0.0f, 0.0f, 1.0f>;
CullMode = CCW;
FogColor = 0xff0000;
```



This will make the ambient color float4<0.7f, 0.0f, 0.0f, 1.0f>, set the backface culling mode to counter-clockwise, and set the fog color to red.

## Sampler States

A sampler state represents a sampler object.



| State   | Type    | Values                              |
|---------|---------|-------------------------------------|
| Sampler | sampler | **NULL**, or a sampler state block. |



 

## Sampler Stage States

Sampler stage states are used to sample textures. Sampler state determines filtering types and texture addressing modes.



| Sampler State       | Type                         | Values                                                                                                                            |
|---------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| AddressU\[16\]      | dword                        | Same values as [**D3DTEXTUREADDRESS**](./d3dtextureaddress.md) without the D3DTADDRESS\_ prefix. See D3DSAMP\_ADDRESSU.      |
| AddressV\[16\]      | dword                        | Same values as [**D3DTEXTUREADDRESS**](./d3dtextureaddress.md) without the D3DTADDRESS\_ prefix. See D3DSAMP\_ADDRESSV.      |
| AddressW\[16\]      | dword                        | Same values as [**D3DTEXTUREADDRESS**](./d3dtextureaddress.md) without the D3DTADDRESS\_ prefix. See D3DSAMP\_ADDRESSW.      |
| BorderColor\[16\]   | [**D3DCOLOR**](d3dcolor.md) | Same values as [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md) without the D3DTEXF\_ prefix. See D3DSAMP\_BORDERCOLOR. |
| MagFilter\[16\]     | dword                        | Same values as [**D3DTEXTUREFILTERTYPE**](./d3dtexturefiltertype.md) without the D3DTEXF\_ prefix. See D3DSAMP\_MAGFILTER.   |
| MaxAnisotropy\[16\] | dword                        | Same values as D3DSAMP\_MAXANISOTROPY without the D3DSAMP\_ prefix.                                                               |
| MaxMipLevel\[16\]   | int                          | Same values as D3DSAMP\_MAXMIPLEVEL without the D3DSAMP\_ prefix.                                                                 |
| MinFilter\[16\]     | dword                        | Same values as D3DSAMP\_MINFILTER without the D3DSAMP\_ prefix.                                                                   |
| MipFilter\[16\]     | dword                        | Same values as D3DSAMP\_MIPFILTER without the D3DSAMP\_ prefix.                                                                   |
| MipMapLodBias\[16\] | float                        | Same values as D3DSAMP\_MIPMAPLODBIAS without the D3DSAMP\_ prefix.                                                               |
| SRGBTexture         | bool                         | Same value as D3DSAMP\_SRGBTEXTURE without the D3DSAMP\_ prefix.                                                                   |



 

Example:


```
AddressU[0] = CLAMP;
AddressV[0] = CLAMP;
AddressW[0] = CLAMP;
```



This clamps UVW values to be in between 0 and 1.

## Shader States

There are only two effect shader states: one associated with a vertex shader object and the other associated with a pixel shader object.



| Shader State | Type         | Values                                                                      |
|--------------|--------------|-----------------------------------------------------------------------------|
| PixelShader  | pixelshader  | **NULL**, an assembly block, a compile target, or a pixel shader parameter. |
| VertexShader | vertexshader | **NULL**, an assembly block, a compile target, or a pixel shader parameter. |



 

Example:


```
VertexShader = compile vs_1_1 VSTexture();
PixelShader  = NULL;
```



This will compile VSTexture, a vertex shader defined earlier in the .fx file, to the vertex shader version 1.1, and then set that compiled shader as the vertex shader. The pixel shader is assigned to **NULL**.

## Shader Constant States

Shader constant states are used to access shader constant parameters.



| Shader Constant State | Type            | Values                                       |
|-----------------------|-----------------|----------------------------------------------|
| PixelShaderConstant   | float\[m\[n\]\] | m x n array of floats; m and n are optional. |
| PixelShaderConstant1  | float4          | One 4D float.                                |
| PixelShaderConstant2  | float4x2        | Two 4D floats.                               |
| PixelShaderConstant3  | float4x3        | Three 4D floats.                             |
| PixelShaderConstant4  | float4x4        | Four 4D floats.                              |
| PixelShaderConstantB  | bool\[m\[n\]\]  | m x n array of bools; m and n are optional.  |
| PixelShaderConstantI  | int\[m\[n\]\]   | m x n array of ints. m and n are optional.   |
| PixelShaderConstantF  | float\[m\[n\]\] | m x n array of floats. m and n are optional. |
| VertexShaderConstant  | float\[m\[n\]\] | m x n array of floats. m and n are optional. |
| VertexShaderConstant1 | float4          | One 4D float.                                |
| VertexShaderConstant2 | float4x2        | Two 4D floats.                               |
| VertexShaderConstant3 | float4x3        | Three 4D floats.                             |
| VertexShaderConstant4 | float4x4        | Four 4D floats.                              |
| VertexShaderConstantB | bool\[m\[n\]\]  | m x n array of bools. m and n are optional.  |
| VertexShaderConstantI | int\[m\[n\]\]   | m x n array of ints. m and n are optional.   |
| VertexShaderConstantF | float\[m\[n\]\] | m x n array of floats. m and n are optional. |



 

## Texture States

Texture states initialize textures used by the multitexture blender.



| Texture State | Type    | Values                            |
|---------------|---------|-----------------------------------|
| Texture\[8\]  | texture | **NULL**, or a texture parameter. |



 

## Texture Stage States

Texture stage states set up textures and the texture stages in the multitexture blender.



| Texture Stage State        | Type  | Values                                                                                                                                                    |
|----------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| AlphaOp\[8\]               | dword | Same as [**D3DTEXTUREOP**](./d3dtextureop.md) without the D3DTOP\_ prefix. See D3DTSS\_ALPHAOP.                                                      |
| AlphaArg0\[8\]             | dword | Same as [D3DTA](d3dta.md) without the D3DTA\_ prefix. See D3DTSS\_ALPHAARG0.                                                                             |
| AlphaArg1\[8\]             | dword | Same as [D3DTA](d3dta.md) without the D3DTA\_ prefix. See D3DTSS\_ALPHAARG1.                                                                             |
| AlphaArg2\[8\]             | dword | Same as [D3DTA](d3dta.md) without the D3DTA\_ prefix. See D3DTSS\_ALPHAARG2.                                                                             |
| ColorArg0\[8\]             | dword | Same as [D3DTA](d3dta.md) without the D3DTA\_ prefix. See D3DTSS\_COLORARG0.                                                                             |
| ColorArg1\[8\]             | dword | Same as [D3DTA](d3dta.md) without the D3DTA\_ prefix. See D3DTSS\_COLORARG1.                                                                             |
| ColorArg2\[8\]             | dword | Same as [D3DTA](d3dta.md) without the D3DTA\_ prefix. See D3DTSS\_COLORARG2.                                                                             |
| ColorOp\[8\]               | dword | Same as [**D3DTEXTUREOP**](./d3dtextureop.md) without the D3DTOP\_ prefix. See D3DTSS\_COLOROP.                                                      |
| BumpEnvLScale\[8\]         | float | Same values as D3DTSS\_BUMPENVLSCALE without the D3DTSS\_TCI prefix.                                                                                      |
| BumpEnvLOffset\[8\]        | float | Same values as D3DTSS\_BUMPENVLOFFSET without the D3DTSS\_TCI prefix.                                                                                     |
| BumpEnvMat00\[8\]          | float | Same values as D3DTSS\_BUMPENVMAT00.                                                                                                                      |
| BumpEnvMat01\[8\]          | float | Same values as D3DTSS\_BUMPENVMAT01.                                                                                                                      |
| BumpEnvMat10\[8\]          | float | Same values as D3DTSS\_BUMPENVMAT10.                                                                                                                      |
| BumpEnvMat11\[8\]          | float | Same values as D3DTSS\_BUMPENVMAT11.                                                                                                                      |
| ResultArg\[8\]             | dword | Same as [D3DTA](d3dta.md) without the D3DTA\_ prefix. See D3DTSS\_RESULTARG.                                                                             |
| TexCoordIndex\[8\]         | dword | Same values as D3DTSS\_TEXCOORDINDEX without the D3DTSS\_TCI prefix.                                                                                      |
| TextureTransformFlags\[8\] | dword | Same values as [**D3DTEXTURETRANSFORMFLAGS**](./d3dtexturetransformflags.md) values without the D3DTTFF\_ prefix. See D3DTSS\_TEXTURETRANSFORMFLAGS. |



 

## Transform States

Set transform states to initialize transformation matrices. Effects use transposed matrices for efficiency. You can provide transposed matrices to an effect, or an effect will automatically transpose the matrices before using them.



| Transform State       | Type     | Values                                                                                                                          |
|-----------------------|----------|---------------------------------------------------------------------------------------------------------------------------------|
| ProjectionTransform   | float4x4 | A 4x4 matrix of floats. Same values as D3DTS\_PROJECTION without the D3DTS\_ prefix.                                            |
| TextureTransform\[8\] | float4x4 | A 4x4 matrix of floats. Same values as [**D3DTRANSFORMSTATETYPE**](./d3dtransformstatetype.md) without the D3DTS\_ prefix. |
| ViewTransform         | float4x4 | A 4x4 matrix of floats. Same values as D3DTS\_VIEW without the D3DTS\_ prefix.                                                  |
| WorldTransform        | float4x4 | A 4x4 matrix of floats.                                                                                                         |



 

## Related topics

<dl> <dt>

[Effect Format](dx9-graphics-reference-effects-file-format.md)
</dt> </dl>
