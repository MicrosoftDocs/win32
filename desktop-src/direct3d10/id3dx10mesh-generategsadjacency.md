---
Description: Adds adjacency data to the meshs index buffer. When the mesh is to be sent to a geometry shader that takes adjacency data, it is neccessary for the meshs index buffer to contain adjacency data.
ms.assetid: 8e587620-a4b6-4415-8fe7-9ec22f253b16
title: ID3DX10MeshGenerateGSAdjacency method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID3DX10Mesh::GenerateGSAdjacency method

Adds adjacency data to the mesh's index buffer. When the mesh is to be sent to a geometry shader that takes adjacency data, it is neccessary for the mesh's index buffer to contain adjacency data.

## Syntax


```C++
HRESULT GenerateGSAdjacency();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

The return value is one of the values listed in [Direct3D 10 Return Codes](d3d10-graphics-reference-returnvalues.md).

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

 

 




