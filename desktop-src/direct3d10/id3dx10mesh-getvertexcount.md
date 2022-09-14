---
description: Get the number of vertices in the mesh.
ms.assetid: fea8a3b5-ca10-4066-b2ca-6579829d31b6
title: ID3DX10Mesh::GetVertexCount method (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh.GetVertexCount
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Mesh::GetVertexCount method

Get the number of vertices in the mesh. A mesh may contain multiple vertex buffers (i.e. one vertex buffer may contain all position data, another may contains all texture coordinate data, etc.), however each vertex buffer will contain the same number of elements.

## Syntax


```C++
UINT GetVertexCount();
```



## Parameters

This method has no parameters.

## Return value

Type: **[**UINT**](../winprog/windows-data-types.md)**

The number of vertices in the mesh.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[ID3DX10Mesh](id3dx10mesh.md)
</dt> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
