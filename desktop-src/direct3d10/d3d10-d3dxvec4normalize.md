---
description: Returns the normalized version of a 4D vector.
ms.assetid: ed3c48cf-4985-4ef3-b733-f8532e3ff6b5
title: D3DXVec4Normalize function (D3DX10Math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXVec4Normalize
api_type: 
- HeaderDef
api_location: 
- D3DX10Math.h
---

# D3DXVec4Normalize function (D3DX10Math.h)

Returns the normalized version of a 4D vector.

## Syntax


```C++
D3DXVECTOR4* D3DXVec4Normalize(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_    const D3DXVECTOR4 *pV
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to the [**D3DXVECTOR4**](d3d10-d3dxvector4.md) that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to the source D3DXVECTOR4 structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](../direct3d9/d3dxvector4.md)\***

Pointer to a D3DXVECTOR4 structure that is the normalized version of the vector.

## Remarks

The return value for this function is the same value returned in the pOut parameter. In this way, the D3DXVec4Normalize function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Math.h</dt> </dl> |



## See also

<dl> <dt>

[Math Functions](d3d10-graphics-reference-d3dx10-functions-math.md)
</dt> </dl>

 

 
