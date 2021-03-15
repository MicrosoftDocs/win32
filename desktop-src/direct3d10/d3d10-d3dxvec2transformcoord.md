---
description: Transforms a 2D vector by a given matrix, projecting the result back into w = 1.
ms.assetid: bb24204f-0c8e-4dc5-bcae-12e3033d1a39
title: D3DXVec2TransformCoord function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXVec2TransformCoord
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXVec2TransformCoord function (D3DX10Math.h)

Transforms a 2D vector by a given matrix, projecting the result back into w = 1.

## Syntax


```C++
D3DXVECTOR2* D3DXVec2TransformCoord(
  _Inout_       D3DXVECTOR2 *pOut,
  _In_    const D3DXVECTOR2 *pV,
  _In_    const D3DXMATRIX  *pM
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR2**](../direct3d9/d3dxvector2.md)\***

Pointer to the [**D3DXVECTOR2**](d3d10-d3dxvector2.md) that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](../direct3d9/d3dxvector2.md)\***

Pointer to the source D3DXVECTOR2 structure.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the source [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR2**](../direct3d9/d3dxvector2.md)\***

Pointer to a D3DXVECTOR2 structure that is the transformed vector.

## Remarks

This function transforms the vector, pV (x, y, 0, 1), by the matrix, pM, projecting the result back into w=1.

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXVec2TransformCoord function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
