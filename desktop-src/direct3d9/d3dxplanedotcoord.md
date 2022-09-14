---
description: Computes the dot product of a plane and a 3D vector. The w parameter of the vector is assumed to be 1.
ms.assetid: 634de6bc-b631-493d-a7a6-292a3c3253d6
title: D3DXPlaneDotCoord function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXPlaneDotCoord
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXPlaneDotCoord function

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Computes the dot product of a plane and a 3D vector. The w parameter of the vector is assumed to be 1.

## Syntax


```C++
FLOAT D3DXPlaneDotCoord(
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

Given a plane (a, b, c, d) and a 3D vector (x, y, z) the return value of this function is a\*x + b\*y + c\*z + d\*1. The **D3DXPlaneDotCoord** function is useful for determining the plane's relationship with a coordinate in 3D space.

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

[**D3DXPlaneDotNormal**](d3dxplanedotnormal.md)
</dt> </dl>

 

 
