---
description: D3DXQuaternionBaryCentric function (D3DX10Math.h) - Returns a quaternion in barycentric coordinates.
ms.assetid: 0a8d8d5a-f486-4457-86e9-27e76eaf1bc4
title: D3DXQuaternionBaryCentric function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXQuaternionBaryCentric
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXQuaternionBaryCentric function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Returns a quaternion in barycentric coordinates.

## Syntax


```C++
D3DXQUATERNION* D3DXQuaternionBaryCentric(
  _Inout_       D3DXQUATERNION *pOut,
  _In_    const D3DXQUATERNION *pQ1,
  _In_    const D3DXQUATERNION *pQ2,
  _In_    const D3DXQUATERNION *pQ3,
  _In_          FLOAT          f,
  _In_          FLOAT          g
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to the [**D3DXQUATERNION**](d3d10-d3dxquaternion.md) that is the result of the operation.

</dd> <dt>

*pQ1* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to a source D3DXQUATERNION structure.

</dd> <dt>

*pQ2* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to a source D3DXQUATERNION structure.

</dd> <dt>

*pQ3* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to a source D3DXQUATERNION structure.

</dd> <dt>

*f* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Weighting factor. See Remarks.

</dd> <dt>

*g* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Weighting factor. See Remarks.

</dd> </dl>

## Return value

Type: **[**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to a D3DXQUATERNION structure in Barycentric coordinates.

## Remarks

To compute the barycentric coordinates, the D3DXQuaternionBaryCentric function implements the following series of spherical linear interpolation operations:


```
Slerp(Slerp(Q1, Q2, f+g), Slerp(Q1, Q3, f+g), g/(f+g))
```



The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXQuaternionBaryCentric function can be used as a parameter for another function.

Use [**D3DXQuaternionNormalize**](d3d10-d3dxquaternionnormalize.md) for any quaternion input that is not already normalized.

Barycentric coordinates define a point inside a triangle in terms of the triangle's vertices. For a more in-depth description of barycentric coordinates, see [Mathworld's Barycentric Coordinates Description](https://mathworld.wolfram.com/BarycentricCoordinates.html).

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
