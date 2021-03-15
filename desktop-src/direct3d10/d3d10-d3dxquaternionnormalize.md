---
description: Computes a unit length quaternion.
ms.assetid: 6735a632-64d7-4bc1-b63e-d0cd27f5a29b
title: D3DXQuaternionNormalize function (D3DX10Math.h)
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
- D3DX10.lib
- D3DX10.dll
---

# D3DXQuaternionNormalize function (D3DX10Math.h)

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

Pointer to a D3DXQUATERNION structure that is the normal of the quaternion.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXQuaternionNormalize function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10Math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
