---
description: Subtracts two 4D vectors.
ms.assetid: 3bc55b38-818e-40eb-859e-495ee28fc4ae
title: D3DXVec4Subtract function (D3dx9math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXVec4Subtract
api_type:
- LibDef
api_location:
- d3dx9.lib
- d3dx9.dll
---

# D3DXVec4Subtract function

> [!Note]
> The D3DX utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Subtracts two 4D vectors.

## Syntax


```C++
D3DXVECTOR4* D3DXVec4Subtract(
  _Inout_       D3DXVECTOR4 *pOut,
  _In_    const D3DXVECTOR4 *pV1,
  _In_    const D3DXVECTOR4 *pV2
);
```



## Parameters

<dl> <dt>

*pOut* \[in, out\]
</dt> <dd>

Type: **[**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to the [**D3DXVECTOR4**](d3dxvector4.md) structure that is the result of the operation.

</dd> <dt>

*pV1* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a source [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> <dt>

*pV2* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a source [**D3DXVECTOR4**](d3dxvector4.md) structure.

</dd> </dl>

## Return value

Type: **[**D3DXVECTOR4**](d3dxvector4.md)\***

Pointer to a [**D3DXVECTOR4**](d3dxvector4.md) structure that is the difference of two vectors.

## Remarks

The return value for this function is the same value returned in the *pOut* parameter. In this way, the **D3DXVec4Subtract** function can be used as a parameter for another function.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[Math Functions](dx9-graphics-reference-d3dx-functions-math.md)
</dt> <dt>

[**D3DXVec3Add**](d3dxvec3add.md)
</dt> <dt>

[**D3DXVec3Scale**](d3dxvec3scale.md)
</dt> </dl>

 

 
