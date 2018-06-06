---
Description: Determines if a ray intersects with a mesh.
ms.assetid: 325f5b40-80ba-4400-a143-bae41146ab07
title: D3DXIntersect function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# D3DXIntersect function

Determines if a ray intersects with a mesh.

## Syntax


```C++
HRESULT D3DXIntersect(
  _In_        LPD3DXBASEMESH pMesh,
  _In_  const D3DXVECTOR3    *pRayPos,
  _In_  const D3DXVECTOR3    *pRayDir,
  _Out_       BOOL           *pHit,
  _Out_       DWORD          *pFaceIndex,
  _Out_       FLOAT          *pU,
  _Out_       FLOAT          *pV,
  _Out_       FLOAT          *pDist,
  _Out_       LPD3DXBUFFER   *ppAllHits,
  _Out_       DWORD          *pCountOfHits
);
```



## Parameters

<dl> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXBASEMESH**](id3dxbasemesh.md)**

Pointer to an [**ID3DXBaseMesh**](id3dxbasemesh.md) interface, representing the mesh to be tested.

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

*pHit* \[out\]
</dt> <dd>

Type: **[**BOOL**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to a BOOL. If the ray intersects a triangular face on the mesh, this value will be set to **TRUE**. Otherwise, this value is set to **FALSE**.

</dd> <dt>

*pFaceIndex* \[out\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to an index value of the face closest to the ray origin, if pHit is **TRUE**.

</dd> <dt>

*pU* \[out\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to a barycentric hit coordinate, U.

</dd> <dt>

*pV* \[out\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to a barycentric hit coordinate, V.

</dd> <dt>

*pDist* \[out\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to a ray intersection parameter distance.

</dd> <dt>

*ppAllHits* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Pointer to an [**ID3DXBuffer**](id3dxbuffer.md) object, containing an array of [**D3DXINTERSECTINFO**](d3dxintersectinfo.md) structures.

</dd> <dt>

*pCountOfHits* \[out\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to a DWORD that contains the number of entries in the ppAllHits array.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be: E\_OUTOFMEMORY.

## Remarks

The **D3DXIntersect** function provides a way to understand points in and around a triangle, independent of where the triangle is actually located. This function returns the resulting point by using the following equation: V1 + U(V2 - V1) + V(V3 - V1).

Any point in the plane V1V2V3 can be represented by the barycentric coordinate (U,V). The parameter U controls how much V2 gets weighted into the result, and the parameter V controls how much V3 gets weighted into the result. Lastly, the value of \[1 - (U + V)\] controls how much V1 gets weighted into the result.

Barycentric coordinates are a form of general coordinates. In this context, using barycentric coordinates represents a change in coordinate systems. What holds true for Cartesian coordinates holds true for barycentric coordinates.

Barycentric coordinates define a point inside a triangle in terms of the triangle's vertices. For a more in-depth description of barycentric coordinates, see [Mathworld's Barycentric Coordinates Description](http://go.microsoft.com/?linkid=9742311).

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




