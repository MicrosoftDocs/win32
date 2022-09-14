---
description: Applications use the methods of the ID3DX10Mesh interface to manipulate mesh objects.
ms.assetid: 1734b8fd-e1a6-4aa4-96a0-8693019a9dac
title: ID3DX10Mesh interface (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10Mesh
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10Mesh interface

Applications use the methods of the ID3DX10Mesh interface to manipulate mesh objects.

## Members

The **ID3DX10Mesh** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX10Mesh** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX10Mesh** interface has these methods.



| Method                                                                                   | Description                                                                                                                                                                                                                                                                                                                          |
|:-----------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CloneMesh**](id3dx10mesh-clonemesh.md)                                               | Creates a new mesh and fills it with the data of a previously loaded mesh.<br/>                                                                                                                                                                                                                                                |
| [**CommitToDevice**](id3dx10mesh-committodevice.md)                                     | Commit any changes made to a mesh to the device so that the changes can be rendered. This should be called after a mesh's data is altered and before it is rendered. A mesh cannot be rendered unless it is committed to the device. See remarks.<br/>                                                                         |
| [**Discard**](id3dx10mesh-discard.md)                                                   | Removes mesh data from the device that has been committed to the device (with [**ID3DX10Mesh::CommitToDevice**](id3dx10mesh-committodevice.md)).<br/>                                                                                                                                                                         |
| [**DrawSubset**](id3dx10mesh-drawsubset.md)                                             | Draws a subset of a mesh.<br/>                                                                                                                                                                                                                                                                                                 |
| [**DrawSubsetInstanced**](id3dx10mesh-drawsubsetinstanced.md)                           | Draw several instances of the same subset of a mesh.<br/>                                                                                                                                                                                                                                                                      |
| [**GenerateAdjacencyAndPointReps**](id3dx10mesh-generateadjacencyandpointreps.md)       | Generate a list of mesh edges, as well as a list of faces that share each edge.<br/>                                                                                                                                                                                                                                           |
| [**GenerateAttributeBufferFromTable**](id3dx10mesh-generateattributebufferfromtable.md) | Generate an attribute buffer from the data in the mesh's attribute table. An attribute buffer is another format for storing the data in the attribute table. Both the attribute buffer and the attribute table are internal data structures in the mesh.<br/>                                                                  |
| [**GenerateGSAdjacency**](id3dx10mesh-generategsadjacency.md)                           | Adds adjacency data to the mesh's index buffer. When the mesh is to be sent to a geometry shader that takes adjacency data, it is neccessary for the mesh's index buffer to contain adjacency data.<br/>                                                                                                                       |
| [**GetAdjacencyBuffer**](id3dx10mesh-getadjacencybuffer.md)                             | Access the mesh's adjacency buffer.<br/>                                                                                                                                                                                                                                                                                       |
| [**GetAttributeBuffer**](id3dx10mesh-getattributebuffer.md)                             | Access the mesh's attribute buffer.<br/>                                                                                                                                                                                                                                                                                       |
| [**GetAttributeTable**](id3dx10mesh-getattributetable.md)                               | Retrieves either an attribute table for a mesh, or the number of entries stored in an attribute table for a mesh.<br/>                                                                                                                                                                                                         |
| [**GetDeviceIndexBuffer**](id3dx10mesh-getdeviceindexbuffer.md)                         | Access the mesh's index buffer after it has been committed to the device with [**ID3DX10Mesh::CommitToDevice**](id3dx10mesh-committodevice.md). This is different from [**ID3DX10Mesh::GetIndexBuffer**](id3dx10mesh-getindexbuffer.md), which returns the index buffer before it has been committed to the device.<br/>     |
| [**GetDeviceVertexBuffer**](id3dx10mesh-getdevicevertexbuffer.md)                       | Access the mesh's vertex buffer after it has been committed to the device with [**ID3DX10Mesh::CommitToDevice**](id3dx10mesh-committodevice.md). This is different from [**ID3DX10Mesh::GetVertexBuffer**](id3dx10mesh-getvertexbuffer.md), which returns the vertex buffer before it has been committed to the device.<br/> |
| [**GetFaceCount**](id3dx10mesh-getfacecount.md)                                         | Retrieves the number of faces in the mesh.<br/>                                                                                                                                                                                                                                                                                |
| [**GetFlags**](id3dx10mesh-getflags.md)                                                 | Access the mesh's creation flags.<br/>                                                                                                                                                                                                                                                                                         |
| [**GetIndexBuffer**](id3dx10mesh-getindexbuffer.md)                                     | Retrieves the data in an index buffer.<br/>                                                                                                                                                                                                                                                                                    |
| [**GetPointRepBuffer**](id3dx10mesh-getpointrepbuffer.md)                               | Get the mesh's point rep buffer.<br/>                                                                                                                                                                                                                                                                                          |
| [**GetVertexBuffer**](id3dx10mesh-getvertexbuffer.md)                                   | Retrieves the vertex buffer associated with the mesh.<br/>                                                                                                                                                                                                                                                                     |
| [**GetVertexBufferCount**](id3dx10mesh-getvertexbuffercount.md)                         | Get the number of vertex buffers in the mesh.<br/>                                                                                                                                                                                                                                                                             |
| [**GetVertexCount**](id3dx10mesh-getvertexcount.md)                                     | Get the number of vertices in the mesh. A mesh may contain multiple vertex buffers (i.e. one vertex buffer may contain all position data, another may contains all texture coordinate data, etc.), however each vertex buffer will contain the same number of elements.<br/>                                                   |
| [**GetVertexDescription**](id3dx10mesh-getvertexdescription.md)                         | Access the vertex description passed into [**D3DX10CreateMesh**](d3d10-d3dx10createmesh.md). The vertex description describes the layout of the mesh's vertex buffers.<br/>                                                                                                                                                   |
| [**Intersect**](id3dx10mesh-intersect.md)                                               | Determines if a ray intersects with this mesh.<br/>                                                                                                                                                                                                                                                                            |
| [**IntersectSubset**](id3dx10mesh-intersectsubset.md)                                   | Determines if a ray intersects with a subset of this mesh.<br/>                                                                                                                                                                                                                                                                |
| [**Optimize**](id3dx10mesh-optimize.md)                                                 | Generates a new mesh with reordered faces and vertices to optimize drawing performance.<br/>                                                                                                                                                                                                                                   |
| [**SetAdjacencyData**](id3dx10mesh-setadjacencydata.md)                                 | Set the mesh's adjacency data.<br/>                                                                                                                                                                                                                                                                                            |
| [**SetAttributeData**](id3dx10mesh-setattributedata.md)                                 | Set the mesh's attribute data.<br/>                                                                                                                                                                                                                                                                                            |
| [**SetAttributeTable**](id3dx10mesh-setattributetable.md)                               | Sets the attribute table for a mesh and the number of entries stored in the table.<br/>                                                                                                                                                                                                                                        |
| [**SetIndexData**](id3dx10mesh-setindexdata.md)                                         | Set the mesh's index data.<br/>                                                                                                                                                                                                                                                                                                |
| [**SetPointRepData**](id3dx10mesh-setpointrepdata.md)                                   | Set the point rep data for the mesh.<br/>                                                                                                                                                                                                                                                                                      |
| [**SetVertexData**](id3dx10mesh-setvertexdata.md)                                       | Set vertex data into one of the mesh's vertex buffers.<br/>                                                                                                                                                                                                                                                                    |



 

## Remarks

To obtain the ID3DX10Mesh interface, call [**D3DX10CreateMesh**](d3d10-d3dx10createmesh.md).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
