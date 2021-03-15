---
description: Texture stage states define multi-blender texture operations.
ms.assetid: 87a5a1bb-e748-4c72-8320-ea82250dcc0e
title: D3DTEXTURESTAGESTATETYPE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DTEXTURESTAGESTATETYPE
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DTEXTURESTAGESTATETYPE enumeration

Texture stage states define multi-blender texture operations. Some sampler states set up vertex processing, and some set up pixel processing. Texture stage states can be saved and restored using stateblocks (see [State Blocks Save and Restore State (Direct3D 9)](state-blocks-save-and-restore-state.md)).

## Syntax


```C++
typedef enum D3DTEXTURESTAGESTATETYPE { 
  D3DTSS_COLOROP                = 1,
  D3DTSS_COLORARG1              = 2,
  D3DTSS_COLORARG2              = 3,
  D3DTSS_ALPHAOP                = 4,
  D3DTSS_ALPHAARG1              = 5,
  D3DTSS_ALPHAARG2              = 6,
  D3DTSS_BUMPENVMAT00           = 7,
  D3DTSS_BUMPENVMAT01           = 8,
  D3DTSS_BUMPENVMAT10           = 9,
  D3DTSS_BUMPENVMAT11           = 10,
  D3DTSS_TEXCOORDINDEX          = 11,
  D3DTSS_BUMPENVLSCALE          = 22,
  D3DTSS_BUMPENVLOFFSET         = 23,
  D3DTSS_TEXTURETRANSFORMFLAGS  = 24,
  D3DTSS_COLORARG0              = 26,
  D3DTSS_ALPHAARG0              = 27,
  D3DTSS_RESULTARG              = 28,
  D3DTSS_CONSTANT               = 32,
  D3DTSS_FORCE_DWORD            = 0x7fffffff
} D3DTEXTURESTAGESTATETYPE, *LPD3DTEXTURESTAGESTATETYPE;
```



## Constants

<dl> <dt>

<span id="D3DTSS_COLOROP"></span><span id="d3dtss_colorop"></span>**D3DTSS\_COLOROP**
</dt> <dd>

Texture-stage state is a texture color blending operation identified by one member of the [**D3DTEXTUREOP**](./d3dtextureop.md) enumerated type. The default value for the first texture stage (stage 0) is D3DTOP\_MODULATE; for all other stages the default is D3DTOP\_DISABLE.

</dd> <dt>

<span id="D3DTSS_COLORARG1"></span><span id="d3dtss_colorarg1"></span>**D3DTSS\_COLORARG1**
</dt> <dd>

Texture-stage state is the first color argument for the stage, identified by one of the [D3DTA](d3dta.md). The default argument is D3DTA\_TEXTURE.

Specify D3DTA\_TEMP to select a temporary register color for read or write. D3DTA\_TEMP is supported if the D3DPMISCCAPS\_TSSARGTEMP device capability is present. The default value for the register is (0.0, 0.0, 0.0, 0.0).

</dd> <dt>

<span id="D3DTSS_COLORARG2"></span><span id="d3dtss_colorarg2"></span>**D3DTSS\_COLORARG2**
</dt> <dd>

Texture-stage state is the second color argument for the stage, identified by [D3DTA](d3dta.md). The default argument is D3DTA\_CURRENT. Specify D3DTA\_TEMP to select a temporary register color for read or write. D3DTA\_TEMP is supported if the D3DPMISCCAPS\_TSSARGTEMP device capability is present. The default value for the register is (0.0, 0.0, 0.0, 0.0)

</dd> <dt>

<span id="D3DTSS_ALPHAOP"></span><span id="d3dtss_alphaop"></span>**D3DTSS\_ALPHAOP**
</dt> <dd>

Texture-stage state is a texture alpha blending operation identified by one member of the [**D3DTEXTUREOP**](./d3dtextureop.md) enumerated type. The default value for the first texture stage (stage 0) is D3DTOP\_SELECTARG1, and for all other stages the default is D3DTOP\_DISABLE.

</dd> <dt>

<span id="D3DTSS_ALPHAARG1"></span><span id="d3dtss_alphaarg1"></span>**D3DTSS\_ALPHAARG1**
</dt> <dd>

Texture-stage state is the first alpha argument for the stage, identified by by [D3DTA](d3dta.md). The default argument is D3DTA\_TEXTURE. If no texture is set for this stage, the default argument is D3DTA\_DIFFUSE. Specify D3DTA\_TEMP to select a temporary register color for read or write. D3DTA\_TEMP is supported if the D3DPMISCCAPS\_TSSARGTEMP device capability is present. The default value for the register is (0.0, 0.0, 0.0, 0.0).

</dd> <dt>

<span id="D3DTSS_ALPHAARG2"></span><span id="d3dtss_alphaarg2"></span>**D3DTSS\_ALPHAARG2**
</dt> <dd>

Texture-stage state is the second alpha argument for the stage, identified by by [D3DTA](d3dta.md). The default argument is D3DTA\_CURRENT. Specify D3DTA\_TEMP to select a temporary register color for read or write. D3DTA\_TEMP is supported if the D3DPMISCCAPS\_TSSARGTEMP device capability is present. The default value for the register is (0.0, 0.0, 0.0, 0.0).

</dd> <dt>

<span id="D3DTSS_BUMPENVMAT00"></span><span id="d3dtss_bumpenvmat00"></span>**D3DTSS\_BUMPENVMAT00**
</dt> <dd>

Texture-stage state is a floating-point value for the \[0\]\[0\] coefficient in a bump-mapping matrix. The default value is 0.0.

</dd> <dt>

<span id="D3DTSS_BUMPENVMAT01"></span><span id="d3dtss_bumpenvmat01"></span>**D3DTSS\_BUMPENVMAT01**
</dt> <dd>

Texture-stage state is a floating-point value for the \[0\]\[1\] coefficient in a bump-mapping matrix. The default value is 0.0.

</dd> <dt>

<span id="D3DTSS_BUMPENVMAT10"></span><span id="d3dtss_bumpenvmat10"></span>**D3DTSS\_BUMPENVMAT10**
</dt> <dd>

Texture-stage state is a floating-point value for the \[1\]\[0\] coefficient in a bump-mapping matrix. The default value is 0.0.

</dd> <dt>

<span id="D3DTSS_BUMPENVMAT11"></span><span id="d3dtss_bumpenvmat11"></span>**D3DTSS\_BUMPENVMAT11**
</dt> <dd>

Texture-stage state is a floating-point value for the \[1\]\[1\] coefficient in a bump-mapping matrix. The default value is 0.0.

</dd> <dt>

<span id="D3DTSS_TEXCOORDINDEX"></span><span id="d3dtss_texcoordindex"></span>**D3DTSS\_TEXCOORDINDEX**
</dt> <dd>

Index of the texture coordinate set to use with this texture stage. You can specify up to eight sets of texture coordinates per vertex. If a vertex does not include a set of texture coordinates at the specified index, the system defaults to the u and v coordinates (0,0).

When rendering using vertex shaders, each stage's texture coordinate index must be set to its default value. The default index for each stage is equal to the stage index. Set this state to the zero-based index of the coordinate set for each vertex that this texture stage uses.

Additionally, applications can include, as logical OR with the index being set, one of the constants to request that Direct3D automatically generate the input texture coordinates for a texture transformation. For a list of all the constants, see [D3DTSS\_TCI](d3dtss-tci.md).

With the exception of D3DTSS\_TCI\_PASSTHRU, which resolves to zero, if any of the following values is included with the index being set, the system uses the index strictly to determine texture wrapping mode. These flags are most useful when performing environment mapping.

</dd> <dt>

<span id="D3DTSS_BUMPENVLSCALE"></span><span id="d3dtss_bumpenvlscale"></span>**D3DTSS\_BUMPENVLSCALE**
</dt> <dd>

Floating-point scale value for bump-map luminance. The default value is 0.0.

</dd> <dt>

<span id="D3DTSS_BUMPENVLOFFSET"></span><span id="d3dtss_bumpenvloffset"></span>**D3DTSS\_BUMPENVLOFFSET**
</dt> <dd>

Floating-point offset value for bump-map luminance. The default value is 0.0.

</dd> <dt>

<span id="D3DTSS_TEXTURETRANSFORMFLAGS"></span><span id="d3dtss_texturetransformflags"></span>**D3DTSS\_TEXTURETRANSFORMFLAGS**
</dt> <dd>

Member of the [**D3DTEXTURETRANSFORMFLAGS**](./d3dtexturetransformflags.md) enumerated type that controls the transformation of texture coordinates for this texture stage. The default value is D3DTTFF\_DISABLE.

</dd> <dt>

<span id="D3DTSS_COLORARG0"></span><span id="d3dtss_colorarg0"></span>**D3DTSS\_COLORARG0**
</dt> <dd>

Settings for the third color operand for triadic operations (multiply, add, and linearly interpolate), identified by [D3DTA](d3dta.md). This setting is supported if the D3DTEXOPCAPS\_MULTIPLYADD or D3DTEXOPCAPS\_LERP device capabilities are present. The default argument is D3DTA\_CURRENT. Specify D3DTA\_TEMP to select a temporary register color for read or write. D3DTA\_TEMP is supported if the D3DPMISCCAPS\_TSSARGTEMP device capability is present. The default value for the register is (0.0, 0.0, 0.0, 0.0).

</dd> <dt>

<span id="D3DTSS_ALPHAARG0"></span><span id="d3dtss_alphaarg0"></span>**D3DTSS\_ALPHAARG0**
</dt> <dd>

Settings for the alpha channel selector operand for triadic operations (multiply, add, and linearly interpolate), identified by [D3DTA](d3dta.md). This setting is supported if the D3DTEXOPCAPS\_MULTIPLYADD or D3DTEXOPCAPS\_LERP device capabilities are present. The default argument is D3DTA\_CURRENT. Specify D3DTA\_TEMP to select a temporary register color for read or write. D3DTA\_TEMP is supported if the D3DPMISCCAPS\_TSSARGTEMP device capability is present. The default argument is (0.0, 0.0, 0.0, 0.0).

</dd> <dt>

<span id="D3DTSS_RESULTARG"></span><span id="d3dtss_resultarg"></span>**D3DTSS\_RESULTARG**
</dt> <dd>

Setting to select destination register for the result of this stage, identified by [D3DTA](d3dta.md). This value can be set to D3DTA\_CURRENT (the default value) or to D3DTA\_TEMP, which is a single temporary register that can be read into subsequent stages as an input argument. The final color passed to the fog blender and frame buffer is taken from D3DTA\_CURRENT, so the last active texture stage state must be set to write to current. This setting is supported if the D3DPMISCCAPS\_TSSARGTEMP device capability is present.

</dd> <dt>

<span id="D3DTSS_CONSTANT"></span><span id="d3dtss_constant"></span>**D3DTSS\_CONSTANT**
</dt> <dd>

Per-stage constant color. To see if a device supports a per-stage constant color, see the D3DPMISCCAPS\_PERSTAGECONSTANT constant in [D3DPMISCCAPS](d3dpmisccaps.md). D3DTSS\_CONSTANT is used by D3DTA\_CONSTANT. See [D3DTA](d3dta.md).

</dd> <dt>

<span id="D3DTSS_FORCE_DWORD"></span><span id="d3dtss_force_dword"></span>**D3DTSS\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Members of this enumerated type are used with the [**IDirect3DDevice9::GetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-gettexturestagestate) and [**IDirect3DDevice9::SetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexturestagestate) methods to retrieve and set texture state values.

The valid range of values for the D3DTSS\_BUMPENVMAT00, D3DTSS\_BUMPENVMAT01, D3DTSS\_BUMPENVMAT10, and D3DTSS\_BUMPENVMAT11 bump-mapping matrix coefficients is greater than or equal to -8.0 and less than 8.0. This range, expressed in mathematical notation is (-8.0,8.0).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[**IDirect3DDevice9::GetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-gettexturestagestate)
</dt> <dt>

[**IDirect3DDevice9::SetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-settexturestagestate)
</dt> </dl>

 

 
