---
description: Performs adaptive tessellation based on the z-based adaptive tessellation criterion.
ms.assetid: 9f8f5c18-e866-4893-ba07-2a3c0d26c028
title: ID3DXPatchMesh::TessellateAdaptive method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPatchMesh.TessellateAdaptive
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPatchMesh::TessellateAdaptive method

Performs adaptive tessellation based on the z-based adaptive tessellation criterion.

## Syntax


```C++
HRESULT TessellateAdaptive(
  [in] const D3DXVECTOR4 *pTrans,
  [in]       DWORD       dwMaxTessLevel,
  [in]       DWORD       dwMinTessLevel,
  [in]       LPD3DXMESH  pMesh
);
```



## Parameters

<dl> <dt>

*pTrans* \[in\]
</dt> <dd>

Type: **const [**D3DXVECTOR4**](d3dxvector4.md)\***

Specifies a 4D vector that is dotted with the vertices to get the per-vertex adaptive tessellation amount. Each edge is tessellated to the average value of the tessellation levels for the two vertices it connects.

</dd> <dt>

*dwMaxTessLevel* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Maximum limit for adaptive tessellation. This is the number of vertices introduced between existing vertices. This integer value can range from 1 to 32, inclusive.

</dd> <dt>

*dwMinTessLevel* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Minimum limit for adaptive tessellation. This is the number of vertices introduced between existing vertices. This integer value can range from 1 to 32, inclusive.

</dd> <dt>

*pMesh* \[in\]
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

Resulting tessellated mesh. See [**ID3DXMesh**](id3dxmesh.md).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

This function will perform more efficiently if the patch mesh has been optimized using [**ID3DXPatchMesh::Optimize**](id3dxpatchmesh--optimize.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> </dl>

 

 
