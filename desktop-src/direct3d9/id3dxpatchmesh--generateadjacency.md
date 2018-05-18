---
Description: 'Generate a list of mesh edges and the patches that share each edge.'
ms.assetid: '024528c0-2c0d-4448-9b38-05cf8d6ffc63'
title: 'ID3DXPatchMesh::GenerateAdjacency method'
---

# ID3DXPatchMesh::GenerateAdjacency method

Generate a list of mesh edges and the patches that share each edge.

## Syntax


```C++
HRESULT GenerateAdjacency(
  [in] FLOAT fTolerance
);
```



## Parameters

<dl> <dt>

*fTolerance* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Specifies that vertices that differ in position by less than the tolerance should be treated as coincident.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is D3D\_OK. If the method fails, the return value can be one of the following: D3DERR\_INVALIDCALL, E\_OUTOFMEMORY.

## Remarks

After an application generates adjacency information for a mesh, the mesh data can be optimized for better drawing performance. This method determines which patches are adjacent (within the provided tolerance). This information is used internally to optimize tessellation.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[ID3DXPatchMesh](id3dxpatchmesh.md)
</dt> <dt>

[**ID3DXPatchMesh::Optimize**](id3dxpatchmesh--optimize.md)
</dt> </dl>

 

 




