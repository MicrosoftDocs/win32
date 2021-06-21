---
description: D3DXQuaternionToAxisAngle function (D3DX10Math.h) - Computes a quaternion's axis and angle of rotation.
ms.assetid: 1e81b88b-071d-46f1-b640-c70d063a14d1
title: D3DXQuaternionToAxisAngle function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXQuaternionToAxisAngle
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXQuaternionToAxisAngle function (D3DX10Math.h)

Computes a quaternion's axis and angle of rotation.

## Syntax


```C++
void D3DXQuaternionToAxisAngle(
  _In_    const D3DXQUATERNION *pQ,
  _Inout_       D3DXVECTOR3    *pAxis,
  _Inout_       FLOAT          *pAngle
);
```



## Parameters

<dl> <dt>

*pQ* \[in\]
</dt> <dd>

Type: **const [**D3DXQUATERNION**](../direct3d9/d3dxquaternion.md)\***

Pointer to the source [**D3DXQUATERNION**](d3d10-d3dxquaternion.md).

</dd> <dt>

*pAxis* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

This function returns a pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) that identifies the quaternion's axis of rotation.

</dd> <dt>

*pAngle* \[in, out\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)\***

This function returns a pointer to a FLOAT value that identifies the quaternion's angle of rotation in radians.

</dd> </dl>

## Return value

No return value.

## Remarks

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

 

 
