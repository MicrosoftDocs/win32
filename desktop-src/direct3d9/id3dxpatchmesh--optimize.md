---
description: Optimizes the patch mesh for efficient tessellation.
ms.assetid: 0049e649-5fe5-45b4-9b09-14b7f99b4988
title: ID3DXPatchMesh::Optimize method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPatchMesh.Optimize
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPatchMesh::Optimize method

Optimizes the patch mesh for efficient tessellation.

## Syntax


```C++
HRESULT Optimize(
  [in] DWORD Flags
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Currently unused.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_CANNOTATTRSORT.

## Remarks

After an application generates adjacency information for a mesh, the mesh data can be optimized (reordered) for better drawing performance. This method determines which patches are adjacent (within the provided tolerance).

Adjacency information is also used to optimize tessellation. Generate adjacency information once and tessellate repeatedly by calling [**ID3DXPatchMesh::Tessellate**](id3dxpatchmesh--tessellate.md). The optimization performed is independent of the actual tessellation level used. However, if the mesh vertices are changed, you must regenerate the adjacency information.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> <dt>

[**ID3DXPatchMesh::GenerateAdjacency**](id3dxpatchmesh--generateadjacency.md)
</dt> </dl>

 

 
