---
description: Scales a 4D vector.
ms.assetid: b185a9b9-f768-4b50-aa6c-667c71eac39a
title: D3DXVec4Scale function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXVec4Scale
api_type: 
- LibDef
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec4Scale function

Scales a 4D vector.

## Syntax


```C++
D3DXVECTOR4* D3DXVec4Scale(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_    const D3DXVECTOR4 *pV,
  _In_          FLOAT       s
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to the [**D3DXVECTOR4**](d3dxvector4.md) structure that is the result of the operation.

</dd> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to the source [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> <dt>

*s* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Scaling value.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to the [**D3DXVECTOR4**](d3dxvector4.md) structure that is the scaled vector.

## Remarks

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXVec4Scale** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXVec4Add**](d3dxvec4add.md)
</dt> <dt>

[**D3DXVec4Subtract**](d3dxvec4subtract.md)
</dt> </dl>

 

 
