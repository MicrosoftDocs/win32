---
description: Constructs a plane from a point and a normal.
ms.assetid: 93c644d2-ab8c-47a1-9a3b-8b9c6a13178b
title: D3DXPlaneFromPointNormal function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPlaneFromPointNormal
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXPlaneFromPointNormal function (D3DX10Math.h)

Constructs a plane from a point and a normal.

## Syntax


```C++
D3DXPLANE* D3DXPlaneFromPointNormal(
  _Inout_       D3DXPLANE   *pOut,
  _In_    const D3DXVECTOR3 *pPoint,
  _In_    const D3DXVECTOR3 *pNormal
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXPLANE**](../direct3d9/d3dxplane.md)\***

Pointer to the [**D3DXPLANE**](d3d10-d3dxplane.md) that is the result of the operation.

</dd> <dt>

*pPoint* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md), defining the point used to construct the plane.

</dd> <dt>

*pNormal* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a D3DXVECTOR3 structure, defining the normal used to construct the plane.

</dd> </dl>

## Return value

Type: **[**D3DXPLANE**](../direct3d9/d3dxplane.md)\***

Pointer to the D3DXPLANE structure constructed from the point and the normal.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXPlaneFromPointNormal function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
