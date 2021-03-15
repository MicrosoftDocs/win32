---
description: Performs a linear interpolation between two 2D vectors.
ms.assetid: f8e9e6be-9696-4a4a-a6c8-c021985decaa
title: D3DXVec2Lerp function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXVec2Lerp
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec2Lerp function

Performs a linear interpolation between two 2D vectors.

## Syntax


```C++
D3DXVECTOR2* D3DXVec2Lerp(
  _Inout_       D3DXVECTOR2 *pOut,
  _In_    const D3DXVECTOR2 *pV1,
  _In_    const D3DXVECTOR2 *pV2,
  _In_          FLOAT       s
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to the [**D3DXVECTOR2**](d3dxvector2.md) structure that is the result of the operation.

</dd> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a source [**D3DXVECTOR2**](d3dxvector2.md) structure.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a source [**D3DXVECTOR2**](d3dxvector2.md) structure.

</dd> <dt>

*s* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Parameter that linearly interpolates between the vectors.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure that is the result of the linear interpolation.

## Remarks

This function performs the linear interpolation based on the following formula: V1 + s(V2-V1).

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXVec2Lerp** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 
