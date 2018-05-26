---
Description: Calculates the inverse of a matrix.
ms.assetid: 928a201b-814d-41cc-bfab-d2f8a12addeb
title: D3DXMatrixInverse function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXMatrixInverse function

Calculates the inverse of a matrix.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixInverse(
  _Inout_       D3DXMATRIX *pOut,
  _Inout_       FLOAT      *pDeterminant,
  _In_    const D3DXMATRIX *pM
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to the [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pDeterminant* \[in, out\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

Pointer to a FLOAT value containing the determinant of the matrix. If the determinant is not needed, set this parameter to **NULL**.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to the source D3DXMATRIX structure.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to a D3DXMATRIX structure that is the inverse of the matrix. If matrix inversion fails, **NULL** is returned.

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixInverse function can be used as a parameter for another function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




