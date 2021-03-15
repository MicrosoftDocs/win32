---
description: Determines if a ray intersects the volume of a sphere's bounding box.
ms.assetid: 5984a1a6-d36c-4a05-8c74-0ece7443356c
title: D3DXSphereBoundProbe function (D3DX10math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXSphereBoundProbe
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXSphereBoundProbe function (D3DX10math.h)

Determines if a ray intersects the volume of a sphere's bounding box.

## Syntax


```C++
BOOL D3DXSphereBoundProbe(
  _In_ const D3DXVECTOR3 *pCenter,
  _In_       FLOAT       Radius,
  _In_ const D3DXVECTOR3 *pRayPosition,
  _In_ const D3DXVECTOR3 *pRayDirection
);
```



## Parameters

<dl> <dt>

*pCenter* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, specifying the center coordinate of the sphere.

</dd> <dt>

*Radius* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Radius of the sphere.

</dd> <dt>

*pRayPosition* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, specifying the origin coordinate of the ray.

</dd> <dt>

*pRayDirection* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, specifying the direction of the ray. This vector should not be (0,0,0) but does not need to be normalized.

</dd> </dl>

## Return value

Type: **[**BOOL**](../winprog/windows-data-types.md)**

Returns **TRUE** if the ray intersects the volume of the sphere's bounding box. Otherwise, returns **FALSE**.

## Remarks

**D3DXSphereBoundProbe** determines if the ray intersects the volume of the sphere's bounding box, not just the surface of the sphere.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](d3d10-graphics-reference-d3dx10-functions-mesh.md)
</dt> </dl>

 

 
