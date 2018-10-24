---
Description: Builds a matrix that rotates around an arbitrary axis.
ms.assetid: dc4b8b3f-e1d2-475f-9dcb-622ada9fae6b
title: D3DXMatrixRotationAxis function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMatrixRotationAxis
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXMatrixRotationAxis function

Builds a matrix that rotates around an arbitrary axis.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixRotationAxis(
  _Inout_       D3DXMATRIX  *pOut,
  _In_    const D3DXVECTOR3 *pV,
  _In_          FLOAT       Angle
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](https://msdn.microsoft.com/en-us/library/Bb172912(v=VS.85).aspx)\***

Pointer to the [**D3DXMATRIX**](d3d10-d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](https://msdn.microsoft.com/en-us/library/Bb205546(v=VS.85).aspx)\***

Pointer to the arbitrary axis. See [**D3DXVECTOR3**](d3d10-d3dxvector3.md).

</dd> <dt>

*Angle* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Angle of rotation in radians. Angles are measured clockwise when looking along the rotation axis toward the origin.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](https://msdn.microsoft.com/en-us/library/Bb172912(v=VS.85).aspx)\***

Pointer to a D3DXMATRIX structure rotated around the specified axis.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXMatrixRotationAxis function can be used as a parameter for another function.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 




