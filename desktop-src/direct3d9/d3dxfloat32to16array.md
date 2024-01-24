---
description: D3DXFloat32To16Array function (D3dx9math.h) - Converts an array of 32-bit floats to 16-bit floats.
ms.assetid: 00f7ae77-d2b5-4244-8fe9-6fea475700b7
title: D3DXFloat32To16Array function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXFloat32To16Array
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXFloat32To16Array function (D3dx9math.h)

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Converts an array of 32-bit floats to 16-bit floats.

## Syntax


```C++
D3DXFLOAT16* D3DXFloat32To16Array(
  _Inout_       D3DXFLOAT16 *pOut,
  _In_    const FLOAT       *pIn,
  _In_          UINT        n
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXFLOAT16**](d3dxfloat16.md)\***

Pointer to the array of 16-bit floats.

</dd> <dt>

*pIn* \[in\]
</dt> <dd>

Type: **const [**FLOAT**](../winprog/windows-data-types.md)\***

Pointer to an array of 32-bit floats.

</dd> <dt>

*n* \[in\]
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of elements in the array.

</dd> </dl>

## Return value

Type: **[**D3DXFLOAT16**](d3dxfloat16.md)\***

Pointer to an array of 16-bit floats.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> </dl>

 

 
