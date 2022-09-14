---
description: Returns a 3D vector that is made up of the smallest components of two 3D vectors.
ms.assetid: f38164a5-d016-4a8a-a7fe-d7eb0a681107
title: D3DXVec3Minimize function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec3Minimize
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec3Minimize function

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Returns a 3D vector that is made up of the smallest components of two 3D vectors.

## Syntax


```C++
D3DXVECTOR3* D3DXVec3Minimize(
  _Inout_       D3DXVECTOR3 *pOut,
  _In_    const D3DXVECTOR3 *pV1,
  _In_    const D3DXVECTOR3 *pV2
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to the [**D3DXVECTOR3**](d3dxvector3.md) structure that is the result of the operation.

</dd> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a source [**D3DXVECTOR3**](d3dxvector3.md) structure.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a source [**D3DXVECTOR3**](d3dxvector3.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR3**](d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure that is made up of the smallest components of the two vectors.

## Remarks

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXVec3Minimize** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXVec3Maximize**](d3dxvec3maximize.md)
</dt> </dl>

 

 
