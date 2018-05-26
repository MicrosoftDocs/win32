---
Description: Builds a matrix that rotates around the y-axis.
ms.assetid: b58def9b-29dc-4c7d-89a3-188ef9b9f94f
title: D3DXMatrixRotationY function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXMatrixRotationY function

Builds a matrix that rotates around the y-axis.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixRotationY(
  _Inout_ D3DXMATRIX *pOut,
  _In_    FLOAT      Angle
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to the [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*Angle* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Angle of rotation in radians. Angles are measured clockwise when looking along the rotation axis toward the origin.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](direct3d9.d3dxmatrix)\***

Pointer to a D3DXMATRIX structure rotated around the y-axis.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixRotationY function can be used as a parameter for another function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




