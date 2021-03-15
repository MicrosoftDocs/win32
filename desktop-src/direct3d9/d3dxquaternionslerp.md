---
description: Interpolates between two quaternions, using spherical linear interpolation.
ms.assetid: 94a989c8-fa6b-4852-9aa3-e55ad814ffd7
title: D3DXQuaternionSlerp function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXQuaternionSlerp
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXQuaternionSlerp function (D3dx9math.h)

Interpolates between two quaternions, using spherical linear interpolation.

## Syntax


```C++
D3DXQUATERNION* D3DXQuaternionSlerp(
  _Inout_       D3DXQUATERNION *pOut,
  _In_    const D3DXQUATERNION *pQ1,
  _In_    const D3DXQUATERNION *pQ2,
  _In_          FLOAT          t
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to the [**D3DXQUATERNION**](d3dxquaternion.md) structure that is the result of the operation.

</dd> <dt>

*pQ1* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> <dt>

*pQ2* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> <dt>

*t* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Parameter that indicates how far to interpolate between the quaternions.

</dd> </dl>

## Return value

Type: **[**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to a [**D3DXQUATERNION**](d3dxquaternion.md) structure that is the result of the interpolation.

## Remarks

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXQuaternionSlerp** function can be used as a parameter for another function.

Use [**D3DXQuaternionNormalize**](d3dxquaternionnormalize.md) for any quaternion input that is not already normalized.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 
