---
description: D3DXQuaternionExp function (D3DX10Math.h) - Calculates the exponential.
ms.assetid: bd70c432-ac61-4c38-b10b-3b103e49ead8
title: D3DXQuaternionExp function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXQuaternionExp
api_type: 
- LibDef
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# D3DXQuaternionExp function (D3DX10Math.h)

Calculates the exponential.

## Syntax


```C++
D3DXQUATERNION* D3DXQuaternionExp(
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

Pointer to a D3DXQUATERNION structure that is the exponential.

## Remarks

This method converts a pure quaternion to a unit quaternion. D3DXQuaternionExp expects a pure quaternion, where w is ignored in the calculation (w == 0).


```
Given a pure quaternion defined by:
q = (0, theta * v); 
    
This method calculates the exponential result.
exp(Q) = (cos(theta), sin(theta) * v)
```



where v is the vector portion of a quaternion.

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXQuaternionExp function can be used as a parameter for another function.

The [**D3DXQuaternionSquadSetup**](d3d10-d3dxquaternionsquadsetup.md) method can also be used to set up the control points of a quaternion.

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

 

 
