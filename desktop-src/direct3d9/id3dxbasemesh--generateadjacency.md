---
Description: Generate a list of mesh edges, as well as a list of faces that share each edge.
ms.assetid: 9d52290f-1c9e-43a7-b239-35cd54e36466
title: ID3DXBaseMesh::GenerateAdjacency method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ID3DXBaseMesh::GenerateAdjacency method

Generate a list of mesh edges, as well as a list of faces that share each edge.

## Syntax


```C++
HRESULT GenerateAdjacency(
  [in] FLOAT Epsilon,
  [in] DWORD *pAdjacency
);
```



## Parameters

<dl> <dt>

*Epsilon* \[in\]
</dt> <dd>

Type: **[**FLOAT**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)**

Specifies that vertices that differ in position by less than epsilon should be treated as coincident.

</dd> <dt>

*pAdjacency* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/4553cafc-450e-4493-a4d4-cb6e2f274d46)\***

Pointer to an array of three DWORDs per face to be filled with the indices of adjacent faces. The number of bytes in this array must be at least 3 \* [**ID3DXBaseMesh::GetNumFaces**](id3dxbasemesh--getnumfaces.md) \* sizeof(DWORD).

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

After an application generates adjacency information for a mesh, the mesh data can be optimized for better drawing performance.

The order of the entries in the adjacency buffer is determined by the order of the vertex indices in the index buffer. The adjacent triangle 0 always corresponds to the edge between the indices of the corners 0 and 1. The adjacent triangle 1 always corresponds to the edge between the indices of the corners 1 and 2 while the adjacent triangle 2 corresponds to the edge between the indices of the corners 2 and 0.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXBaseMesh](id3dxbasemesh.md)
</dt> <dt>

[**ID3DXMesh::Optimize**](id3dxmesh--optimize.md)
</dt> <dt>

[**ID3DXMesh::OptimizeInplace**](id3dxmesh--optimizeinplace.md)
</dt> </dl>

 

 




