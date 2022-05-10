---
description: Scales a 2D vector.
ms.assetid: 1887bc48-3766-42d7-840b-1e29d78db4ce
title: D3DXVec2Scale function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec2Scale
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec2Scale function

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Scales a 2D vector.

## Syntax


```C++
D3DXVECTOR2* D3DXVec2Scale(
  _Inout_       D3DXVECTOR2 *pOut,
  _In_    const D3DXVECTOR2 *pV,
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

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to the source [**D3DXVECTOR2**](d3dxvector2.md) structure.

</dd> <dt>

*s* \[in\]
</dt> <dd>

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

Scaling value.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR2**](d3dxvector2.md)\***

Pointer to a [**D3DXVECTOR2**](d3dxvector2.md) structure that is the scaled vector.

## Remarks

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXVec2Scale** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXVec2Add**](d3dxvec2add.md)
</dt> <dt>

[**D3DXVec2Subtract**](d3dxvec2subtract.md)
</dt> </dl>

 

 
