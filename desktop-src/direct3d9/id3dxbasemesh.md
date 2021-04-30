---
description: Applications use the methods of the ID3DXBaseMesh interface to manipulate and query mesh and progressive mesh objects.
ms.assetid: ec4ccd77-e370-470c-9325-3d794a8f7f16
title: ID3DXBaseMesh interface (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXBaseMesh
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXBaseMesh interface

Applications use the methods of the **ID3DXBaseMesh** interface to manipulate and query mesh and progressive mesh objects.

## Members

The **ID3DXBaseMesh** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXBaseMesh** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXBaseMesh** interface has these methods.



| Method                                                                            | Description                                                                                                                                                                                                           |
|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CloneMesh**](id3dxbasemesh--clonemesh.md)                                     | Clones a mesh using a declarator.<br/>                                                                                                                                                                          |
| [**CloneMeshFVF**](id3dxbasemesh--clonemeshfvf.md)                               | Clones a mesh using a flexible vertex format (FVF) code.<br/>                                                                                                                                                   |
| [**ConvertAdjacencyToPointReps**](id3dxbasemesh--convertadjacencytopointreps.md) | Converts mesh adjacency information to an array of point representatives.<br/>                                                                                                                                  |
| [**ConvertPointRepsToAdjacency**](id3dxbasemesh--convertpointrepstoadjacency.md) | Converts point representative data to mesh adjacency information.<br/>                                                                                                                                          |
| [**DrawSubset**](id3dxbasemesh--drawsubset.md)                                   | Draws a subset of a mesh.<br/>                                                                                                                                                                                  |
| [**GenerateAdjacency**](id3dxbasemesh--generateadjacency.md)                     | Generate a list of mesh edges, as well as a list of faces that share each edge.<br/>                                                                                                                            |
| [**GetAttributeTable**](id3dxbasemesh--getattributetable.md)                     | Retrieves either an attribute table for a mesh, or the number of entries stored in an attribute table for a mesh.<br/>                                                                                          |
| [**GetDeclaration**](id3dxbasemesh--getdeclaration.md)                           | Retrieves a declaration describing the vertices in the mesh.<br/>                                                                                                                                               |
| [**GetDevice**](id3dxbasemesh--getdevice.md)                                     | Retrieves the device associated with the mesh.<br/>                                                                                                                                                             |
| [**GetFVF**](id3dxbasemesh--getfvf.md)                                           | Gets the fixed function vertex value.<br/>                                                                                                                                                                      |
| [**GetIndexBuffer**](id3dxbasemesh--getindexbuffer.md)                           | Retrieves the data in an index buffer.<br/>                                                                                                                                                                     |
| [**GetNumBytesPerVertex**](id3dxbasemesh--getnumbytespervertex.md)               | Gets the number of bytes per vertex.<br/>                                                                                                                                                                       |
| [**GetNumFaces**](id3dxbasemesh--getnumfaces.md)                                 | Retrieves the number of faces in the mesh.<br/>                                                                                                                                                                 |
| [**GetNumVertices**](id3dxbasemesh--getnumvertices.md)                           | Retrieves the number of vertices in the mesh.<br/>                                                                                                                                                              |
| [**GetOptions**](id3dxbasemesh--getoptions.md)                                   | Retrieves the mesh options enabled for this mesh at creation time.<br/>                                                                                                                                         |
| [**GetVertexBuffer**](id3dxbasemesh--getvertexbuffer.md)                         | Retrieves the vertex buffer associated with the mesh.<br/>                                                                                                                                                      |
| [**LockIndexBuffer**](id3dxbasemesh--lockindexbuffer.md)                         | Locks an index buffer and obtains a pointer to the index buffer memory.<br/>                                                                                                                                    |
| [**LockVertexBuffer**](id3dxbasemesh--lockvertexbuffer.md)                       | Locks a vertex buffer and obtains a pointer to the vertex buffer memory.<br/>                                                                                                                                   |
| [**UnlockIndexBuffer**](id3dxbasemesh--unlockindexbuffer.md)                     | Unlocks an index buffer.<br/>                                                                                                                                                                                   |
| [**UnlockVertexBuffer**](id3dxbasemesh--unlockvertexbuffer.md)                   | Unlocks a vertex buffer.<br/>                                                                                                                                                                                   |
| [**UpdateSemantics**](id3dxbasemesh--updatesemantics.md)                         | This method allows the user to change the mesh declaration without changing the data layout of the vertex buffer. The call is valid only if the old and new declaration formats have the same vertex size.<br/> |



 

## Remarks

A mesh is an object made up of a set of polygonal faces. A mesh defines a set of vertices and a set of faces (the faces are defined in terms of the vertices and normals of the mesh).

The LPD3DXBASEMESH type is defined as a pointer to the **ID3DXBaseMesh** interface.


```
typedef struct ID3DXBaseMesh *LPD3DXBASEMESH;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 
