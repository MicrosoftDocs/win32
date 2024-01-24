---
description: A mesh buffer is a buffer that contains data about a mesh.
ms.assetid: a9fdfa22-531d-4da0-89f0-8766c2635e20
title: ID3DX10MeshBuffer interface (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10MeshBuffer
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10MeshBuffer interface

A mesh buffer is a buffer that contains data about a mesh. It can contain one of five different types of data: vertex data, index data, adjacency data, attribute data, or point rep data. The structure is used to access these five pieces of data through the following five APIs: [**ID3DX10Mesh::GetVertexBuffer**](id3dx10mesh-getvertexbuffer.md), [**ID3DX10Mesh::GetIndexBuffer**](id3dx10mesh-getindexbuffer.md), [**ID3DX10Mesh::GetAdjacencyBuffer**](id3dx10mesh-getadjacencybuffer.md), [**ID3DX10Mesh::GetAttributeBuffer**](id3dx10mesh-getattributebuffer.md), or [**ID3DX10Mesh::GetPointRepBuffer**](id3dx10mesh-getpointrepbuffer.md).

## Members

The **ID3DX10MeshBuffer** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX10MeshBuffer** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX10MeshBuffer** interface has these methods.



| Method                                       | Description                                                                |
|:---------------------------------------------|:---------------------------------------------------------------------------|
| [**GetSize**](id3dx10meshbuffer-getsize.md) | Get the size of the mesh buffer, in bytes.<br/>                      |
| [**Map**](id3dx10meshbuffer-map.md)         | Get a pointer to the mesh buffer memory to modify its contents.<br/> |
| [**Unmap**](id3dx10meshbuffer-unmap.md)     | Unmap a buffer.<br/>                                                 |



 

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
