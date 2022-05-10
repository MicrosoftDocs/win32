---
description: D3DXMatrixRotationQuaternion function (D3dx9math.h) - Builds a rotation matrix from a quaternion.
ms.assetid: e590058c-772b-4eef-aab0-a12bb04c299a
title: D3DXMatrixRotationQuaternion function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXMatrixRotationQuaternion
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXMatrixRotationQuaternion function (D3dx9math.h)

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Builds a rotation matrix from a quaternion.

## Syntax


```C++
D3DXMATRIX* D3DXMatrixRotationQuaternion(
  _Inout_       D3DXMATRIX     *pOut,
  _In_    const D3DXQUATERNION *pQ
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to the [**D3DXMATRIX**](d3dxmatrix.md) structure that is the result of the operation.

</dd> <dt>

*pQ* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to the source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXMATRIX**](d3dxmatrix.md)\***

Pointer to a [**D3DXMATRIX**](d3dxmatrix.md) structure built from the source quaternion.

## Remarks

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXMatrixRotationQuaternion** function can be used as a parameter for another function.

For information about how to calculate quaternion values from a direction vector ( x, y, z ) and an angle of rotation, see [**D3DXQUATERNION**](d3dxquaternion.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXMatrixRotationAxis**](d3dxmatrixrotationaxis.md)
</dt> <dt>

[**D3DXMatrixRotationX**](d3dxmatrixrotationx.md)
</dt> <dt>

[**D3DXMatrixRotationY**](d3dxmatrixrotationy.md)
</dt> <dt>

[**D3DXMatrixRotationYawPitchRoll**](d3dxmatrixrotationyawpitchroll.md)
</dt> <dt>

[**D3DXMatrixRotationZ**](d3dxmatrixrotationz.md)
</dt> </dl>

 

 
