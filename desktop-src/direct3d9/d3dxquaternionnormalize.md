---
description: D3DXQuaternionNormalize function (D3dx9math.h) - Computes a unit length quaternion.
ms.assetid: 31f56c2b-96b0-4110-a5b9-ce09983779b6
title: D3DXQuaternionNormalize function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXQuaternionNormalize
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXQuaternionNormalize function (D3dx9math.h)

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Computes a unit length quaternion.

## Syntax


```C++
D3DXQUATERNION* D3DXQuaternionNormalize(
  _Inout_       D3DXQUATERNION *pOut,
  _In_    const D3DXQUATERNION *pQ
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to the [**D3DXQUATERNION**](d3dxquaternion.md) structure that is the result of the operation.

</dd> <dt>

*pQ* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to the source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a [**D3DXQUATERNION**](d3dxquaternion.md) structure that is the normal of the quaternion.

## Remarks

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXQuaternionNormalize** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXQuaternionInverse**](d3dxquaternioninverse.md)
</dt> </dl>

 

 
