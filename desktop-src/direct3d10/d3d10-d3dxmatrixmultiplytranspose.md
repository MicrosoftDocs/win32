---
description: Calculates the transposed product of two matrices.
ms.assetid: 3db4138c-407c-47b5-b8b9-04af8771e98e
title: D3DXMatrixMultiplyTranspose function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMatrixMultiplyTranspose
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXMatrixMultiplyTranspose function (D3DX10Math.h)

Calculates the transposed product of two matrices.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixMultiplyTranspose(
  _Inout_       D3DXMATRIX *pOut,
  _In_    const D3DXMATRIX *pM1,
  _In_    const D3DXMATRIX *pM2
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pM1* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a source D3DXMATRIX structure (left hand side).

</dd> <dt>

*pM2* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a source D3DXMATRIX structure (right hand side).

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to a D3DXMATRIX structure that is the product of two matrices.

## Remarks

The result is the transposed of the product of two transformation matrices, Out = T(M1\*M2).

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixMultiplyTranspose function can be used as a parameter for another function.

This function is useful to set matrices as constants for vertex and pixel shaders.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
