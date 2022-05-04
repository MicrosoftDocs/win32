---
description: D3DXVec4BaryCentric function (D3dx9math.h) - Returns a point in Barycentric coordinates, using the specified 4D vectors.
ms.assetid: 80d73232-76bf-4f40-add2-dd1bdcc5cd98
title: D3DXVec4BaryCentric function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec4BaryCentric
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec4BaryCentric function (D3dx9math.h)

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Returns a point in Barycentric coordinates, using the specified 4D vectors.

## Syntax


```C++
D3DXVECTOR4* D3DXVec4BaryCentric(
  _Out_       D3DXVECTOR4 *pOut,
  _In_  const D3DXVECTOR4 *pV1,
  _In_  const D3DXVECTOR4 *pV2,
  _In_  const D3DXVECTOR4 *pV3,
  _In_        FLOAT       f,
  _In_        FLOAT       g
);
```



## Parameters

<dl> <dt>

*pOut* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to the [**D3DXVECTOR4**](d3dxvector4.md) structure that is the result of the operation.

</dd> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a source [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a source [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> <dt>

*pV3* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a source [**D3DXVECTOR4**](d3dxvector4.md) structure.

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

Type: **[**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a [**D3DXVECTOR4**](d3dxvector4.md) structure in Barycentric coordinates.

## Remarks

The **D3DXVec4BaryCentric** function provides a way to understand points in and around a triangle, independent of where the triangle is actually located. This function returns the resulting point by using the following equation: V1 + f(V2-V1) + g(V3-V1).

Any point in the plane V1V2V3 can be represented by the Barycentric coordinate (f,g).The parameter *f* controls how much V2 gets weighted into the result and the parameter *g* controls how much V3 gets weighted into the result. Lastly, 1-f-g controls how much V1 gets weighted into the result.

Note the following relations.

-   If (f>=0 &, & g>=0 &, & 1-f-g>=0), the point is inside the triangle V1V2V3.
-   If (f==0 &, & g>=0 &, & 1-f-g>=0), the point is on the line V1V3.
-   If (f>=0 &, & g==0 &, & 1-f-g>=0), the point is on the line V1V2.
-   If (f>=0 &, & g>=0 &, & 1-f-g==0), the point is on the line V2V3.

Barycentric coordinates are a form of general coordinates. In this context, using Barycentric coordinates represents a change in coordinate systems. What holds true for Cartesian coordinates holds true for Barycentric coordinates.

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXVec4BaryCentric** function can be used as a parameter for another function.

Barycentric coordinates define a point inside a triangle in terms of the triangle's vertices. For a more in-depth description of barycentric coordinates, see [Mathworld's Barycentric Coordinates Description](https://mathworld.wolfram.com/BarycentricCoordinates.html).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 
