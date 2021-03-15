---
description: Builds a right-handed, look-at matrix.
ms.assetid: 10198bb9-a77e-4482-be6e-cc5f76eff30b
title: D3DXMatrixLookAtRH function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMatrixLookAtRH
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXMatrixLookAtRH function (D3dx9math.h)

Builds a right-handed, look-at matrix.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixLookAtRH(
  _Inout_       D3DXMATRIX  *pOut,
  _In_    const D3DXVECTOR3 *pEye,
  _In_    const D3DXVECTOR3 *pAt,
  _In_    const D3DXVECTOR3 *pUp
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pEye* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to the [**D3DXVECTOR3**](d3dxvector3.md) structure that defines the eye point. This value is used in translation.

</dd> <dt>

*pAt* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to the [**D3DXVECTOR3**](d3dxvector3.md) structure that defines the camera look-at target.

</dd> <dt>

*pUp* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to the [**D3DXVECTOR3**](d3dxvector3.md) structure that defines the current world's up, usually \[0, 1, 0\].

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) structure that is a right-handed, look-at matrix.

## Remarks

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXMatrixLookAtRH** function can be used as a parameter for another function.

This function uses the following formula to compute the returned matrix.


```
zaxis = normal(Eye - At)
xaxis = normal(cross(Up, zaxis))
yaxis = cross(zaxis, xaxis)
    
 xaxis.x           yaxis.x           zaxis.x          0
 xaxis.y           yaxis.y           zaxis.y          0
 xaxis.z           yaxis.z           zaxis.z          0
 dot(xaxis, eye)   dot(yaxis, eye)   dot(zaxis, eye)  1
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXMatrixLookAtLH**](d3dxmatrixlookatlh.md)
</dt> </dl>

 

 




