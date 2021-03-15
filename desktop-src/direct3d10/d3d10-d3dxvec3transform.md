---
description: Transforms vector (x, y, z, 1) by a given matrix.
ms.assetid: 88b26d94-2550-4126-bf91-b06391ec5c75
title: D3DXVec3Transform function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXVec3Transform
api_type: 
- HeaderDef
api_location: 
- D3DX10Math.h
---

# D3DXVec3Transform function (D3DX10Math.h)

Transforms vector (x, y, z, 1) by a given matrix.

## Syntax


```C++
D3DXVECTOR4* D3DXVec3Transform(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_    const D3DXVECTOR3 *pV,
  _In_    const D3DXMATRIX  *pM
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to the [**D3DXVECTOR4**](d3d10-d3dxvector4.md) structure that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to the source [**D3DXVECTOR3**](d3d10-d3dxvector3.md).

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the source [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to a D3DXVECTOR4 structure that is the transformed vector.

## Remarks

This function transforms the vector, pV (x, y, z, 1), by the matrix pM.

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXVec3Transform function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
