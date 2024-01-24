---
description: Computes the dot product of a plane and a 4D vector.
ms.assetid: e6232ca8-52cc-472d-8bdb-4f8dfc520d4f
title: D3DXPlaneDot function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXPlaneDot
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXPlaneDot function

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Computes the dot product of a plane and a 4D vector.

## Syntax


```C++
FLOAT D3DXPlaneDot(
  _In_ const D3DXPLANE   *pP,
  _In_ const D3DXVECTOR4 *pV
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

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The dot product of the plane and 4D vector.

## Remarks

Given a plane (a, b, c, d) and a 4D vector (x, y, z, w) the return value of this function is a\*x + b\*y + c\*z + d\*w. The **D3DXPlaneDot** function is useful for determining the plane's relationship with a homogeneous coordinate. For example, this function could be used to determine if a particular coordinate is on a particular plane, or on which side of a particular plane a particular coordinate lies.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXPlaneDotCoord**](d3dxplanedotcoord.md)
</dt> <dt>

[**D3DXPlaneDotNormal**](d3dxplanedotnormal.md)
</dt> </dl>

 

 
