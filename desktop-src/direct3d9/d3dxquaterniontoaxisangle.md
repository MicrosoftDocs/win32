---
Description: Computes a quaternions axis and angle of rotation.
ms.assetid: 6efd0a68-7641-403e-8ae2-c715b705b36e
title: D3DXQuaternionToAxisAngle function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# D3DXQuaternionToAxisAngle function

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

Type: **const [**D3DXQUATERNION**](d3dxquaternion.md)\***

Pointer to the source [**D3DXQUATERNION**](d3dxquaternion.md) structure.

</dd> <dt>

*pAxis* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](d3dxvector3.md)\***

This function returns a pointer to a [**D3DXVECTOR3**](d3dxvector3.md) structure that identifies the quaternion's axis of rotation.

</dd> <dt>

*pAngle* \[in, out\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)\***

This function returns a pointer to a FLOAT value that identifies the quaternion's angle of rotation in radians.

</dd> </dl>

## Return value

No return value.

## Remarks

Use [**D3DXQuaternionNormalize**](d3dxquaternionnormalize.md) for any quaternion input that is not already normalized.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 




