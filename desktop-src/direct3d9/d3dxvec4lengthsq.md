---
description: Returns the square of the length of a 4D vector.
ms.assetid: 73091179-4acb-408b-8c91-766052999f26
title: D3DXVec4LengthSq function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec4LengthSq
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec4LengthSq function

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Returns the square of the length of a 4D vector.

## Syntax


```C++
FLOAT D3DXVec4LengthSq(
  _In_ const D3DXVECTOR4 *pV
);
```



## Parameters

<dl> <dt>

*pV* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to the source [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> </dl>

## Return value

Type: **[**FLOAT**](../winprog/windows-data-types.md)**

The vector's squared length.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXVec4Length**](d3dxvec4length.md)
</dt> </dl>

 

 
