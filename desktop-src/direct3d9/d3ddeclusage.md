---
description: Identifies the intended use of vertex data.
ms.assetid: ee9b46c2-b779-480c-9b5c-6d189d2af014
title: D3DDECLUSAGE enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DDECLUSAGE
api_type: 
- HeaderDef
api_location: 
- D3D9Types.h
---

# D3DDECLUSAGE enumeration

Identifies the intended use of vertex data.

## Syntax


```C++
typedef enum D3DDECLUSAGE { 
  D3DDECLUSAGE_POSITION      = 0,
  D3DDECLUSAGE_BLENDWEIGHT   = 1,
  D3DDECLUSAGE_BLENDINDICES  = 2,
  D3DDECLUSAGE_NORMAL        = 3,
  D3DDECLUSAGE_PSIZE         = 4,
  D3DDECLUSAGE_TEXCOORD      = 5,
  D3DDECLUSAGE_TANGENT       = 6,
  D3DDECLUSAGE_BINORMAL      = 7,
  D3DDECLUSAGE_TESSFACTOR    = 8,
  D3DDECLUSAGE_POSITIONT     = 9,
  D3DDECLUSAGE_COLOR         = 10,
  D3DDECLUSAGE_FOG           = 11,
  D3DDECLUSAGE_DEPTH         = 12,
  D3DDECLUSAGE_SAMPLE        = 13
} D3DDECLUSAGE, *LPD3DDECLUSAGE;
```



## Constants

<dl> <dt>

<span id="D3DDECLUSAGE_POSITION"></span><span id="d3ddeclusage_position"></span>**D3DDECLUSAGE\_POSITION**
</dt> <dd>

Position data ranging from (-1,-1) to (1,1). Use D3DDECLUSAGE\_POSITION with a usage index of 0 to specify untransformed position for fixed function vertex processing and the n-patch tessellator. Use D3DDECLUSAGE\_POSITION with a usage index of 1 to specify untransformed position in the fixed function vertex shader for vertex tweening.

</dd> <dt>

<span id="D3DDECLUSAGE_BLENDWEIGHT"></span><span id="d3ddeclusage_blendweight"></span>**D3DDECLUSAGE\_BLENDWEIGHT**
</dt> <dd>

Blending weight data. Use D3DDECLUSAGE\_BLENDWEIGHT with a usage index of 0 to specify the blend weights used in indexed and nonindexed vertex blending.

</dd> <dt>

<span id="D3DDECLUSAGE_BLENDINDICES"></span><span id="d3ddeclusage_blendindices"></span>**D3DDECLUSAGE\_BLENDINDICES**
</dt> <dd>

Blending indices data. Use D3DDECLUSAGE\_BLENDINDICES with a usage index of 0 to specify matrix indices for indexed paletted skinning.

</dd> <dt>

<span id="D3DDECLUSAGE_NORMAL"></span><span id="d3ddeclusage_normal"></span>**D3DDECLUSAGE\_NORMAL**
</dt> <dd>

Vertex normal data. Use D3DDECLUSAGE\_NORMAL with a usage index of 0 to specify vertex normals for fixed function vertex processing and the n-patch tessellator. Use D3DDECLUSAGE\_NORMAL with a usage index of 1 to specify vertex normals for fixed function vertex processing for vertex tweening.

</dd> <dt>

<span id="D3DDECLUSAGE_PSIZE"></span><span id="d3ddeclusage_psize"></span>**D3DDECLUSAGE\_PSIZE**
</dt> <dd>

Point size data. Use D3DDECLUSAGE\_PSIZE with a usage index of 0 to specify the point-size attribute used by the setup engine of the rasterizer to expand a point into a quad for the point-sprite functionality.

</dd> <dt>

<span id="D3DDECLUSAGE_TEXCOORD"></span><span id="d3ddeclusage_texcoord"></span>**D3DDECLUSAGE\_TEXCOORD**
</dt> <dd>

Texture coordinate data. Use D3DDECLUSAGE\_TEXCOORD, n to specify texture coordinates in fixed function vertex processing and in pixel shaders prior to ps\_3\_0. These can be used to pass user defined data.

</dd> <dt>

<span id="D3DDECLUSAGE_TANGENT"></span><span id="d3ddeclusage_tangent"></span>**D3DDECLUSAGE\_TANGENT**
</dt> <dd>

Vertex tangent data.

</dd> <dt>

<span id="D3DDECLUSAGE_BINORMAL"></span><span id="d3ddeclusage_binormal"></span>**D3DDECLUSAGE\_BINORMAL**
</dt> <dd>

Vertex binormal data.

</dd> <dt>

<span id="D3DDECLUSAGE_TESSFACTOR"></span><span id="d3ddeclusage_tessfactor"></span>**D3DDECLUSAGE\_TESSFACTOR**
</dt> <dd>

Single positive floating point value. Use D3DDECLUSAGE\_TESSFACTOR with a usage index of 0 to specify a tessellation factor used in the tessellation unit to control the rate of tessellation. For more information about the data type, see D3DDECLTYPE\_FLOAT1.

</dd> <dt>

<span id="D3DDECLUSAGE_POSITIONT"></span><span id="d3ddeclusage_positiont"></span>**D3DDECLUSAGE\_POSITIONT**
</dt> <dd>

Vertex data contains transformed position data ranging from (0,0) to (viewport width, viewport height). Use D3DDECLUSAGE\_POSITIONT with a usage index of 0 to specify transformed position. When a declaration containing this is set, the pipeline does not perform vertex processing.

</dd> <dt>

<span id="D3DDECLUSAGE_COLOR"></span><span id="d3ddeclusage_color"></span>**D3DDECLUSAGE\_COLOR**
</dt> <dd>

Vertex data contains diffuse or specular color. Use D3DDECLUSAGE\_COLOR with a usage index of 0 to specify the diffuse color in the fixed function vertex shader and pixel shaders prior to ps\_3\_0. Use D3DDECLUSAGE\_COLOR with a usage index of 1 to specify the specular color in the fixed function vertex shader and pixel shaders prior to ps\_3\_0.

</dd> <dt>

<span id="D3DDECLUSAGE_FOG"></span><span id="d3ddeclusage_fog"></span>**D3DDECLUSAGE\_FOG**
</dt> <dd>

Vertex data contains fog data. Use D3DDECLUSAGE\_FOG with a usage index of 0 to specify a fog blend value used after pixel shading finishes. This applies to pixel shaders prior to version ps\_3\_0.

</dd> <dt>

<span id="D3DDECLUSAGE_DEPTH"></span><span id="d3ddeclusage_depth"></span>**D3DDECLUSAGE\_DEPTH**
</dt> <dd>

Vertex data contains depth data.

</dd> <dt>

<span id="D3DDECLUSAGE_SAMPLE"></span><span id="d3ddeclusage_sample"></span>**D3DDECLUSAGE\_SAMPLE**
</dt> <dd>

Vertex data contains sampler data. Use D3DDECLUSAGE\_SAMPLE with a usage index of 0 to specify the displacement value to look up. It can be used only with D3DDECLUSAGE\_LOOKUPPRESAMPLED or D3DDECLUSAGE\_LOOKUP.

</dd> </dl>

## Remarks

Vertex data is declared with an array of [**D3DVERTEXELEMENT9**](d3dvertexelement9.md) structures. Each element in the array contains a usage type.

For more information about vertex declarations, see [Vertex Declaration (Direct3D 9)](vertex-declaration.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)
</dt> <dt>

[Vertex Declaration (Direct3D 9)](vertex-declaration.md)
</dt> </dl>

 

 




