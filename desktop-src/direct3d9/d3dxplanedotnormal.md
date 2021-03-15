---
description: Computes the dot product of a plane and a 3D vector. The w parameter of the vector is assumed to be 0.
ms.assetid: 7aba1e94-6531-4c07-83b0-6100805e8bbd
title: D3DXPlaneDotNormal function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPlaneDotNormal
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXPlaneDotNormal function

Computes the dot product of a plane and a 3D vector. The w parameter of the vector is assumed to be 0.

## Syntax


```C++
FLOAT D3DXPlaneDotNormal(
  _In_ const D3DXPLANE   *pP,
  _In_ const D3DXVECTOR3 *pV
);
```



## Parameters

<dl> <dt>

*pP* \[in\]
</dt> <dd>

Type: **const [**D3DXPLANE**](d3dxplane.md)\***

Pointer to a source [**D3DXPLANE**](d3dxplane.md) structure.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a source [**D3DXVECTOR3**](d3dxvector3.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The dot product of the plane and 3D vector.

## Remarks

Given a plane (a, b, c, d) and a 3D vector (x, y, z) the return value of this function is a\*x + b\*y + c\*z + d\*0. The **D3DXPlaneDotNormal** function is useful for calculating the angle between the normal of the plane, and another normal.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXPlaneDot**](d3dxplanedot.md)
</dt> <dt>

[**D3DXPlaneDotCoord**](d3dxplanedotcoord.md)
</dt> </dl>

 

 
