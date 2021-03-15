---
description: Transforms an array (x, y, 0, 1) by a given matrix, and projects the result back into w = 1.
ms.assetid: 23c88bed-344b-4b3a-bb92-e50cbe96daf9
title: D3DXVec2TransformCoordArray function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXVec2TransformCoordArray
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec2TransformCoordArray function (D3dx9math.h)

Transforms an array (x, y, 0, 1) by a given matrix, and projects the result back into w = 1.

## Syntax


```C++
D3DXVECTOR2* D3DXVec2TransformCoordArray(
  _Inout_       D3DXVECTOR2 *pOut,
  _In_          UINT        OutStride,
  _In_    const D3DXVECTOR2 *pV,
  _In_          UINT        VStride,
  _In_    const D3DXMATRIX  *pM,
  _In_          UINT        n
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to the [**D3DXVECTOR2**](d3dxvector2.md) structure that is the result of the operation.

</dd> <dt>

*OutStride* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Stride between vectors in the output data stream.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to the source [**D3DXVECTOR2**](d3dxvector2.md) array.

</dd> <dt>

*VStride* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Stride between vectors in the input data stream.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the source [**D3DXMATRIX**](d3dxmatrix.md) structure.

</dd> <dt>

*n* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

Number of elements in the array.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR4**](d3dxvector4.md) transformed array.

## Remarks

This function transforms the array *pV* (x, y, 0, 1) by the matrix *pM*, projecting the result back into w = 1.

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXVec2TransformCoordArray** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 
