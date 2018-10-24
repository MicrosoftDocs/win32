---
Description: Transforms an array (x, y, z, 1) by a given matrix.
ms.assetid: f64c55df-ea93-4c93-be89-eee650e6ecf0
title: D3DXVec3TransformArray function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXVec3TransformArray
api_type: 
- HeaderDef
api_location: 
- D3DX10Math.h
---

# D3DXVec3TransformArray function

Transforms an array (x, y, z, 1) by a given matrix.

## Syntax


```C++
D3DXVECTOR4* D3DXVec3TransformArray(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_          UINT        OutStride,
  _In_    const D3DXVECTOR3 *pV,
  _In_          UINT        VStride,
  _In_    const D3DXMATRIX  *pM,
  _In_          UINT        n
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](https://msdn.microsoft.com/en-us/library/Bb205548(v=VS.85).aspx)\***

Pointer to the [**D3DXVECTOR4**](d3d10-d3dxvector4.md) array that is the result of the operation.

</dd> <dt>

*OutStride* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Stride between vectors in the output data stream.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/en-us/library/Bb205546(v=VS.85).aspx)\***

Pointer to the source [**D3DXVECTOR3**](d3d10-d3dxvector3.md) array.

</dd> <dt>

*VStride* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Stride between vectors in the input data stream.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](https://msdn.microsoft.com/en-us/library/Bb172912(v=VS.85).aspx)\***

Pointer to the source [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure.

</dd> <dt>

*n* \[in\]
</dt> <dd>

Type: **[**UINT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Number of elements in the array.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](https://msdn.microsoft.com/en-us/library/Bb205548(v=VS.85).aspx)\***

Pointer to a [**D3DXVECTOR4**](d3d10-d3dxvector4.md) transformed array.

## Remarks

This function transforms the array pV (x, y, z, 1) by the matrix pM.

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXVec3TransformArray function can be used as a parameter for another function.

## Requirements



|                   |                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




