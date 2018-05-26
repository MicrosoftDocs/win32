---
Description: Transforms a 2D vector by a given matrix.
ms.assetid: 4b57eb7f-fae9-48ac-a806-510da75d25a6
title: D3DXVec2Transform function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXVec2Transform function

Transforms a 2D vector by a given matrix.

## Syntax


```C++
D3DXVECTOR4* D3DXVec2Transform(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_    const D3DXVECTOR2 *pV,
  _In_    const D3DXMATRIX  *pM
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](direct3d9.d3dxvector4)\***

Pointer to the [**D3DXVECTOR4**](d3d10-d3dxvector4.md) structure that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](direct3d9.d3dxvector2)\***

Pointer to the source [**D3DXVECTOR2**](d3d10-d3dxvector2.md).

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to the source [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](direct3d9.d3dxvector4)\***

Pointer to a D3DXVECTOR4 structure that is the transformed vector.

## Remarks

This function transforms the vector pV (x, y, 0, 1) by the matrix pM.

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXVec2Transform function can be used as a parameter for another function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




