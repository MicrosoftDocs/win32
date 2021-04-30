---
description: Defines settings used for mesh tangent frame computations.
ms.assetid: b525b4cc-9a2d-4569-bae8-7cc7f7832cbc
title: D3DXTANGENT enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXTANGENT
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXTANGENT enumeration

Defines settings used for mesh tangent frame computations.

## Syntax


```C++
typedef enum D3DXTANGENT { 
  D3DXTANGENT_WRAP_U                   = 0x01,
  D3DXTANGENT_WRAP_V                   = 0x02,
  D3DXTANGENT_WRAP_UV                  = 0x03,
  D3DXTANGENT_DONT_NORMALIZE_PARTIALS  = 0x04,
  D3DXTANGENT_DONT_ORTHOGONALIZE       = 0x08,
  D3DXTANGENT_ORTHOGONALIZE_FROM_V     = 0x010,
  D3DXTANGENT_ORTHOGONALIZE_FROM_U     = 0x020,
  D3DXTANGENT_WEIGHT_BY_AREA           = 0x040,
  D3DXTANGENT_WEIGHT_EQUAL             = 0x080,
  D3DXTANGENT_WIND_CW                  = 0x0100,
  D3DXTANGENT_CALCULATE_NORMALS        = 0x0200,
  D3DXTANGENT_GENERATE_IN_PLACE        = 0x0400
} D3DXTANGENT, *LPD3DXTANGENT;
```



## Constants

<dl> <dt>

<span id="D3DXTANGENT_WRAP_U"></span><span id="d3dxtangent_wrap_u"></span>**D3DXTANGENT\_WRAP\_U**
</dt> <dd>

Texture coordinate values in the u direction are between 0 and 1. In this case a texture coordinate set will be chosen that minimizes the perimeter of the triangle. See [Texture Wrapping (Direct3D 9)](texture-wrapping.md).

</dd> <dt>

<span id="D3DXTANGENT_WRAP_V"></span><span id="d3dxtangent_wrap_v"></span>**D3DXTANGENT\_WRAP\_V**
</dt> <dd>

Texture coordinate values in the v direction are between 0 and 1. In this case a texture coordinate set will be chosen that minimizes the perimeter of the triangle. See [Texture Wrapping (Direct3D 9)](texture-wrapping.md).

</dd> <dt>

<span id="D3DXTANGENT_WRAP_UV"></span><span id="d3dxtangent_wrap_uv"></span>**D3DXTANGENT\_WRAP\_UV**
</dt> <dd>

Texture coordinate values in both u and v directions are between 0 and 1. In this case a texture coordinate set will be chosen that minimizes the perimeter of the triangle. See [Texture Wrapping (Direct3D 9)](texture-wrapping.md).

</dd> <dt>

<span id="D3DXTANGENT_DONT_NORMALIZE_PARTIALS"></span><span id="d3dxtangent_dont_normalize_partials"></span>**D3DXTANGENT\_DONT\_NORMALIZE\_PARTIALS**
</dt> <dd>

Do not normalize partial derivatives with respect to texture coordinates. If not normalized, the scale of the partial derivatives is proportional to the scale of the 3D model divided by the scale of the triangle in (u, v) space. This scale value provides a measure of how much the texture is stretched in a given direction. The resulting vector length is a weighted sum of the lengths of the partial derivatives.

</dd> <dt>

<span id="D3DXTANGENT_DONT_ORTHOGONALIZE"></span><span id="d3dxtangent_dont_orthogonalize"></span>**D3DXTANGENT\_DONT\_ORTHOGONALIZE**
</dt> <dd>

Do not transform texture coordinates to orthogonal Cartesian coordinates. Mutually exclusive with D3DXTANGENT\_ORTHOGONALIZE\_FROM\_U and D3DXTANGENT\_ORTHOGONALIZE\_FROM\_V.

</dd> <dt>

<span id="D3DXTANGENT_ORTHOGONALIZE_FROM_V"></span><span id="d3dxtangent_orthogonalize_from_v"></span>**D3DXTANGENT\_ORTHOGONALIZE\_FROM\_V**
</dt> <dd>

Compute the partial derivative with respect to texture coordinate v independently for each vertex, and then compute the partial derivative with respect to u as the cross product of the partial derivative with respect to v and the normal vector. Mutually exclusive with D3DXTANGENT\_DONT\_ORTHOGONALIZE and D3DXTANGENT\_ORTHOGONALIZE\_FROM\_U.

</dd> <dt>

<span id="D3DXTANGENT_ORTHOGONALIZE_FROM_U"></span><span id="d3dxtangent_orthogonalize_from_u"></span>**D3DXTANGENT\_ORTHOGONALIZE\_FROM\_U**
</dt> <dd>

Compute the partial derivative with respect to texture coordinate u independently for each vertex, and then compute the partial derivative with respect to v as the cross product of the normal vector and the partial derivative with respect to u. Mutually exclusive with D3DXTANGENT\_DONT\_ORTHOGONALIZE and D3DXTANGENT\_ORTHOGONALIZE\_FROM\_V.

</dd> <dt>

<span id="D3DXTANGENT_WEIGHT_BY_AREA"></span><span id="d3dxtangent_weight_by_area"></span>**D3DXTANGENT\_WEIGHT\_BY\_AREA**
</dt> <dd>

Weight the direction of the computed per-vertex normal or partial derivative vector according to the areas of triangles attached to that vertex. Mutually exclusive with D3DXTANGENT\_WEIGHT\_EQUAL.

</dd> <dt>

<span id="D3DXTANGENT_WEIGHT_EQUAL"></span><span id="d3dxtangent_weight_equal"></span>**D3DXTANGENT\_WEIGHT\_EQUAL**
</dt> <dd>

Compute a unit-length normal vector for each triangle of the input mesh. Mutually exclusive with D3DXTANGENT\_WEIGHT\_BY\_AREA.

</dd> <dt>

<span id="D3DXTANGENT_WIND_CW"></span><span id="d3dxtangent_wind_cw"></span>**D3DXTANGENT\_WIND\_CW**
</dt> <dd>

Vertices are ordered in a clockwise direction around each triangle. The computed normal vector direction is therefore inverted 180 degrees from the direction computed using counterclockwise vertex ordering.

</dd> <dt>

<span id="D3DXTANGENT_CALCULATE_NORMALS"></span><span id="d3dxtangent_calculate_normals"></span>**D3DXTANGENT\_CALCULATE\_NORMALS**
</dt> <dd>

Compute the per-vertex normal vector for each triangle of the input mesh, and ignore any normal vectors already in the input mesh.

</dd> <dt>

<span id="D3DXTANGENT_GENERATE_IN_PLACE"></span><span id="d3dxtangent_generate_in_place"></span>**D3DXTANGENT\_GENERATE\_IN\_PLACE**
</dt> <dd>

The results are stored in the original input mesh, and the output mesh is not used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> <dt>

[**D3DXComputeTangentFrameEx**](d3dxcomputetangentframeex.md)
</dt> </dl>

 

 




