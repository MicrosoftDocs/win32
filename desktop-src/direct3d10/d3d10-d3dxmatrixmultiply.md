---
description: D3DXMatrixMultiply function (D3DX10Math.h) - Determines the product of two matrices.
ms.assetid: d15cd680-0e19-4353-9eee-73933663960e
title: D3DXMatrixMultiply function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXMatrixMultiply
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXMatrixMultiply function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

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

The result represents the transformation M1 followed by the transformation M2 (Out = M1 \* M2).

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixMultiply function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
