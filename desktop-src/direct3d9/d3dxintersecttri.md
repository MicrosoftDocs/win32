---
description: D3DXIntersectTri function (D3DX9Mesh.h) - Computes the intersection of a ray and a triangle.
ms.assetid: f335a71d-7203-4ea1-a6bf-407b28c712e6
title: D3DXIntersectTri function (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXIntersectTri
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXIntersectTri function (D3DX9Mesh.h)

Computes the intersection of a ray and a triangle.

## Syntax


```C++
BOOL D3DXIntersectTri(
  _In_  const D3DXVECTOR3 *p0,
  _In_  const D3DXVECTOR3 *p1,
  _In_  const D3DXVECTOR3 *p2,
  _In_  const D3DXVECTOR3 *pRayPos,
  _In_  const D3DXVECTOR3 *pRayDir,
  _Out_       FLOAT       *pU,
  _Out_       FLOAT       *pV,
  _Out_       FLOAT       *pDist
);
```



## Parameters

<dl> <dt>

*p0* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure, describing the first triangle vertex position.

</dd> <dt>

*p1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure, describing the second triangle vertex position.

</dd> <dt>

*p2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure, describing the third triangle vertex position.

</dd> <dt>

*pRayPos* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure, specifying the point where the ray begins.

</dd> <dt>

*pRayDir* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure, specifying the direction of the ray.

</dd> <dt>

*pU* \[out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Barycentric hit coordinates, U.

</dd> <dt>

*pV* \[out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Barycentric hit coordinates, V.

</dd> <dt>

*pDist* \[out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

Ray-intersection parameter distance.

</dd> </dl>

## Return value

Type: **[**BOOL**](../winprog/windows-data-types.md)**

Returns **TRUE** if the ray intersects the area of the triangle. Otherwise, returns **FALSE**.

## Remarks

The [**D3DXIntersect**](d3dxintersect.md) function provides a way to understand points in and around a triangle, independent of where the triangle is actually located. This function returns the resulting point by using the following equation: V1 + U(V2 - V1) + V(V3 - V1).

Any point in the plane V1V2V3 can be represented by the barycentric coordinate (U,V). The parameter U controls how much V2 gets weighted into the result, and the parameter V controls how much V3 gets weighted into the result. Lastly, the value of \[1 - (U + V)\] controls how much V1 gets weighted into the result.

Barycentric coordinates are a form of general coordinates. In this context, using barycentric coordinates represents a change in coordinate systems. What holds true for Cartesian coordinates holds true for barycentric coordinates.

Barycentric coordinates define a point inside a triangle in terms of the triangle's vertices. For a more in-depth description of barycentric coordinates, see [Mathworld's Barycentric Coordinates Description](https://mathworld.wolfram.com/BarycentricCoordinates.html).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
