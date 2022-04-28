---
description: D3DXComputeBoundingBox function (D3DX10math.h) - Computes a coordinate-axis oriented bounding box.
ms.assetid: 1b8f328c-2fe1-462e-b464-c8dd9dc03e67
title: D3DXComputeBoundingBox function (D3DX10math.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DXComputeBoundingBox
api_type:
- LibDef
api_location:
- D3DX10.lib
- D3DX10.dll
---

# D3DXComputeBoundingBox function (D3DX10math.h)

> [!Note]
> The D3DX10 utility library is deprecated. We recommend that you use [DirectXMath](../dxmath/pg-xnamath-migration-d3dx.md) instead.

Computes a coordinate-axis oriented bounding box.

## Syntax


```C++
HRESULT D3DXComputeBoundingBox(
  _In_  const D3DXVECTOR3 *pFirstPosition,
  _In_        DWORD       NumVertices,
  _In_        DWORD       dwStride,
  _Out_       D3DXVECTOR3 *pMin,
  _Out_       D3DXVECTOR3 *pMax
);
```



## Parameters

<dl> <dt>

*pFirstPosition* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to the first position.

</dd> <dt>

*NumVertices* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Number of vertices.

</dd> <dt>

*dwStride* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Count or number of bytes between vertices.

</dd> <dt>

*pMin* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, describing the returned lower-left corner of the bounding box.

</dd> <dt>

*pMax* \[out\]
</dt> <dd>

Type: **[**D3DXVECTOR3**](../direct3d9/d3dxvector3.md)\***

Pointer to a [**D3DXVECTOR3**](d3d10-d3dxvector3.md) structure, describing the returned upper-right corner of the bounding box.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the function succeeds, the return value is D3D\_OK. If the function fails, the return value can be one of the following: D3DERR\_INVALIDCALL.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10math.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl>   |



## See also

<dl> <dt>

[Mesh Functions](d3d10-graphics-reference-d3dx10-functions-mesh.md)
</dt> </dl>

 

 
