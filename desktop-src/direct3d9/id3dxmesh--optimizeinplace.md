---
description: Generates a mesh with reordered faces and vertices to optimize drawing performance. This method reorders the existing mesh.
ms.assetid: 2cdaf627-d1d3-44f0-a5ae-9023d4b0de45
title: ID3DXMesh::OptimizeInplace method (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXMesh.OptimizeInplace
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMesh::OptimizeInplace method

Generates a mesh with reordered faces and vertices to optimize drawing performance. This method reorders the existing mesh.

## Syntax


```C++
HRESULT OptimizeInplace(
  [in]        DWORD        Flags,
  [in]  const DWORD        *pAdjacencyIn,
  [out]       DWORD        *pAdjacencyOut,
  [out]       DWORD        *pFaceRemap,
  [out]       LPD3DXBUFFER *ppVertexRemap
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Combination of one or more [**D3DXMESHOPT**](./d3dxmeshopt.md) flags, specifying the type of optimization to perform.

</dd> <dt>

*pAdjacencyIn* \[in\]
</dt> <dd>

Type: **const [**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specifies the three neighbors for each face in the source mesh. If the edge has no adjacent faces, the value is 0xffffffff.

</dd> <dt>

*pAdjacencyOut* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

Pointer to an array of three DWORDs per face that specifies the three neighbors for each face in the optimized mesh. If the edge has no adjacent faces, the value is 0xffffffff. If the value supplied for this argument is **NULL**, adjacency data is not returned.

</dd> <dt>

*pFaceRemap* \[out\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

An array of DWORDs, one per face, that identifies the original mesh face that corresponds to each face in the optimized mesh. If the value supplied for this argument is **NULL**, face remap data is not returned.

</dd> <dt>

*ppVertexRemap* \[out\]
</dt> <dd>

Type: **[**LPD3DXBUFFER**](id3dxbuffer.md)\***

Address of a pointer to an [**ID3DXBuffer**](id3dxbuffer.md) interface, which contains a DWORD for each vertex that specifies how the new vertices map to the old vertices. This remap is useful if you need to alter external data based on the new vertex mapping. If the value supplied for this argument is **NULL**, vertex remap data is not returned.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, D3DXERR\_CANNOTATTRSORT, E\_OUTOFMEMORY.

## Remarks

Before running **ID3DXMesh::OptimizeInplace**, an application must generate an adjacency buffer by calling [**ID3DXBaseMesh::GenerateAdjacency**](id3dxbasemesh--generateadjacency.md). The adjacency buffer contains adjacency data, such as a list of edges and the faces that are adjacent to each other.

> [!Note]  
> This method will fail if the mesh is sharing its vertex buffer with another mesh, unless the D3DXMESHOPT\_IGNOREVERTS is set in Flags.

 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXMesh](id3dxmesh.md)
</dt> <dt>

[**ID3DXMesh::Optimize**](id3dxmesh--optimize.md)
</dt> </dl>

 

 
