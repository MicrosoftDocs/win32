---
description: Transforms an array (x, y, z, w) by a given matrix.
ms.assetid: afd5cccb-e22f-4726-a84e-9eac1c1c277f
title: D3DXVec4TransformArray function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec4TransformArray
api_type:
- HeaderDef
api_location:
- D3DX10Math.h
---

# D3DXVec4TransformArray function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Transforms an array (x, y, z, w) by a given matrix.

## Syntax


```C++
D3DXVECTOR4* D3DXVec4TransformArray(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_          UINT        OutStride,
  _In_    const D3DXVECTOR4 *pV,
  _In_          UINT        VStride,
  _In_    const D3DXMATRIX  *pM,
  _In_          UINT        n
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to the [**D3DXVECTOR4**](d3d10-d3dxvector4.md) array that is the result of the operation.

</dd> <dt>

*OutStride* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Stride between vectors in the output data stream.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to the source D3DXVECTOR4 array.

</dd> <dt>

*VStride* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Stride between vectors in the input data stream.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](../direct3d9/d3dxmatrix.md)\***

Pointer to the source [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure.

</dd> <dt>

*n* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of elements in the array.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to a [**D3DXVECTOR4**](d3d10-d3dxvector4.md) structure that is the transformed array.

## Remarks

This function transforms the array pV (x, y, z, w) by the matrix pM.

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXVec4TransformArray** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
