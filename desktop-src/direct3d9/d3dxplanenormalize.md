---
description: Normalizes the plane coefficients so that the plane normal has unit length.
ms.assetid: 9c595986-e1f8-4153-ba23-1fa6e583a050
title: D3DXPlaneNormalize function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPlaneNormalize
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXPlaneNormalize function (D3dx9math.h)

Normalizes the plane coefficients so that the plane normal has unit length.

## Syntax


```C++
D3DXPLANE* D3DXPlaneNormalize(
  _Inout_       D3DXPLANE *pOut,
  _In_    const D3DXPLANE *pP
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXPLANE**](d3dxplane.md)\***

Pointer to the [**D3DXPLANE**](d3dxplane.md) structure that is the result of the operation.

</dd> <dt>

*pP* \[in\]
</dt> <dd>

Type: **const [**D3DXPLANE**](d3dxplane.md)\***

Pointer to the source [**D3DXPLANE**](d3dxplane.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXPLANE**](d3dxplane.md)\***

Pointer to a [**D3DXPLANE**](d3dxplane.md) structure that represents the normal of the plane.

## Remarks

This function normalizes a plane so that \|a,b,c\| == 1.

The return value for this function is the same value returned in the *pOut* parameter. In this way, this function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 




