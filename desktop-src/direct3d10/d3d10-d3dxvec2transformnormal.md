---
Description: Transforms the 2D vector normal by the given matrix.
ms.assetid: fc238bb1-155f-4018-9c92-16352726920d
title: D3DXVec2TransformNormal function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXVec2TransformNormal function

Transforms the 2D vector normal by the given matrix.

## Syntax


```C++
D3DXVECTOR2* D3DXVec2TransformNormal(
  _Inout_       D3DXVECTOR2 *pOut,
  _In_    const D3DXVECTOR2 *pV,
  _In_    const D3DXMATRIX  *pM
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR2**](direct3d9.d3dxvector2)\***

Pointer to the [**D3DXVECTOR2**](d3d10-d3dxvector2.md) that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](direct3d9.d3dxvector2)\***

Pointer to the source D3DXVECTOR2 structure.

</dd> <dt>

*pM* \[in\]
</dt> <dd>

Type: **const [**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to the source [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR2**](direct3d9.d3dxvector2)\***

Pointer to a D3DXVECTOR2 structure that is the transformed vector.

## Remarks

This function transforms the vector (pV-&gt;x, pV-&gt;y, 0, 0) by the matrix pointed to by pM.

If you want to transform a normal, the matrix you pass to this function should be the transpose of the inverse of the matrix you would use to transform a point.

The return value for this function is the same value returned in the pOut parameter. In this way, the **D3DXVec2TransformNormal** function can be used as a parameter for another function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




