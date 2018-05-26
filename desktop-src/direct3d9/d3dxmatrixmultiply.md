---
Description: Determines the product of two matrices.
ms.assetid: 160c801a-6589-4a0d-8e90-7e7a99fbd5f7
title: D3DXMatrixMultiply function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXMatrixMultiply function

Determines the product of two matrices.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixMultiply(
  _Inout_       D3DXMATRIX *pOut,
  _In_    const D3DXMATRIX *pM1,
  _In_    const D3DXMATRIX *pM2
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pM1* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a source [**D3DXMATRIX**](d3dxmatrix.md) structure.

</dd> <dt>

*pM2* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a source [**D3DXMATRIX**](d3dxmatrix.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) structure that is the product of two matrices.

## Remarks

The result represents the transformation M1 followed by the transformation M2 (Out = M1 \* M2).

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXMatrixMultiply** function can be used as a parameter for another function.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXQuaternionMultiply**](d3dxquaternionmultiply.md)
</dt> </dl>

 

 




