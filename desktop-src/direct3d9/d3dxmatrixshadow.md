---
description: D3DXMatrixShadow function (D3dx9math.h) - Builds a matrix that flattens geometry into a plane.
ms.assetid: 8f283ff9-c879-476c-8057-f4fe77a7a9e7
title: D3DXMatrixShadow function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMatrixShadow
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXMatrixShadow function (D3dx9math.h)

Builds a matrix that flattens geometry into a plane.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixShadow(
  _Inout_       D3DXMATRIX  *pOut,
  _In_    const D3DXVECTOR4 *pLight,
  _In_    const D3DXPLANE   *pPlane
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pLight* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a [**D3DXVECTOR4**](d3dxvector4.md) structure describing the light's position.

</dd> <dt>

*pPlane* \[in\]
</dt> <dd>

Type: **const [**D3DXPLANE**](d3dxplane.md)\***

Pointer to the source [**D3DXPLANE**](d3dxplane.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) structure that flattens geometry into a plane.

## Remarks

The **D3DXMatrixShadow** function flattens geometry into a plane, as if casting a shadow from a light.

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXMatrixShadow** function can be used as a parameter for another function.

This function uses the following formula to compute the returned matrix.


```
P = normalize(Plane);
L = Light;
d = -dot(P, L)
    
P.a * L.x + d  P.a * L.y      P.a * L.z      P.a * L.w  
P.b * L.x      P.b * L.y + d  P.b * L.z      P.b * L.w  
P.c * L.x      P.c * L.y      P.c * L.z + d  P.c * L.w  
P.d * L.x      P.d * L.y      P.d * L.z      P.d * L.w + d
```



If the light's w-component is 0, the ray from the origin to the light represents a directional light. If it is 1, the light is a point light.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 




