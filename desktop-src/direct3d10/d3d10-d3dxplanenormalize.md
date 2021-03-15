---
description: Normalizes the plane coefficients so that the plane normal has unit length.
ms.assetid: 52ae36a7-e37b-457a-9832-e62900a85bde
title: D3DXPlaneNormalize function (D3DX10Math.h)
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
- D3DX10.lib
- D3DX10.dll
---

# D3DXPlaneNormalize function (D3DX10Math.h)

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

Type: **[**D3DXPLANE**](../direct3d9/d3dxplane.md)\***

Pointer to the [**D3DXPLANE**](d3d10-d3dxplane.md) that is the result of the operation.

</dd> <dt>

*pP* \[in\]
</dt> <dd>

Type: **const [**D3DXPLANE**](../direct3d9/d3dxplane.md)\***

Pointer to the source D3DXPLANE structure.

</dd> </dl>

## Return value

Type: **[**D3DXPLANE**](../direct3d9/d3dxplane.md)\***

Pointer to a D3DXPLANE structure that represents the normal of the plane.

## Remarks

This function normalizes a plane so that \|a,b,c\| == 1.

The return value for this function is the same value returned in the pOut parameter. In this way, this function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
