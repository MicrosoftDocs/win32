---
Description: Generate a list of mesh edges, as well as a list of faces that share each edge.
ms.assetid: 3932e2b1-031d-4962-ad90-6e9da8cf2e0e
title: ID3DX10MeshGenerateAdjacencyAndPointReps method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX10Mesh::GenerateAdjacencyAndPointReps method

Generate a list of mesh edges, as well as a list of faces that share each edge.

## Syntax


```C++
HRESULT GenerateAdjacencyAndPointReps(
  [in] FLOAT Epsilon
);
```



## Parameters

<dl> <dt>

*Epsilon* \[in\]
</dt> <dd>

Type: **[**FLOAT**](winprog.windows_data_types)**

Specifies that vertices that differ in position by less than epsilon should be treated as coincident.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

## Remarks

After an application generates adjacency information for a mesh, the mesh data can be optimized for better drawing performance.

The order of the entries in the adjacency buffer is determined by the order of the vertex indices in the index buffer. The adjacent triangle 0 always corresponds to the edge between the indices of the corners 0 and 1. The adjacent triangle 1 always corresponds to the edge between the indices of the corners 1 and 2 while the adjacent triangle 2 corresponds to the edge between the indices of the corners 2 and 0.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Mesh](id3dx10mesh.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 




