---
description: D3DXQuaternionLn function (D3DX10Math.h) - Calculates the natural logarithm.
ms.assetid: 576cf676-bb42-45ec-8e45-4612a7cdb167
title: D3DXQuaternionLn function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXQuaternionLn
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXQuaternionLn function (D3DX10Math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Calculates the natural logarithm.

## Syntax


```C++
D3DXQUATERNION* D3DXQuaternionLn(
  _Inout_       D3DXQUATERNION *pOut,
  _In_    const D3DXQUATERNION *pQ
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to the [**D3DXQUATERNION**](d3d10-d3dxquaternion.md) that is the result of the operation.

</dd> <dt>

*pQ* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to the source D3DXQUATERNION structure.

</dd> </dl>

## Return value

Type: **[**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to a D3DXQUATERNION structure that is the natural logarithm.

## Remarks

The D3DXQuaternionLn function works only for unit quaternions.


```
A unit quaternion, is defined by:
Q == (cos(theta), sin(theta) * v) where |v| = 1
The natural logarithm of Q is, ln(Q) = (0, theta * v)
```



The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXQuaternionLn function can be used as a parameter for another function.

Use [**D3DXQuaternionNormalize**](d3d10-d3dxquaternionnormalize.md) for any quaternion input that is not already normalized.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
