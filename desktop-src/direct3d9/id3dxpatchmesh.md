---
description: This interface encapsulates patch mesh functionality.
ms.assetid: c70c0fe0-b695-4ad9-b0c6-7854cf8f7593
title: ID3DXPatchMesh interface (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXPatchMesh
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXPatchMesh interface

This interface encapsulates patch mesh functionality.

## Members

The **ID3DXPatchMesh** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXPatchMesh** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXPatchMesh** interface has these methods.



| Method                                                                           | Description                                                                                     |
|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**CloneMesh**](id3dxpatchmesh--clonemesh.md)                                   | Creates a new patch mesh with the specified vertex declaration.<br/>                      |
| [**GenerateAdjacency**](id3dxpatchmesh--generateadjacency.md)                   | Generate a list of mesh edges and the patches that share each edge.<br/>                  |
| [**GetControlVerticesPerPatch**](id3dxpatchmesh--getcontrolverticesperpatch.md) | Gets the number of control vertices per patch.<br/>                                       |
| [**GetDeclaration**](id3dxpatchmesh--getdeclaration.md)                         | Gets the vertex declaration.<br/>                                                         |
| [**GetDevice**](id3dxpatchmesh--getdevice.md)                                   | Gets the device that created the mesh.<br/>                                               |
| [**GetDisplaceParam**](id3dxpatchmesh--getdisplaceparam.md)                     | Gets mesh geometry displacement parameters.<br/>                                          |
| [**GetIndexBuffer**](id3dxpatchmesh--getindexbuffer.md)                         | Gets the mesh index buffer.<br/>                                                          |
| [**GetNumPatches**](id3dxpatchmesh--getnumpatches.md)                           | Gets the number of patches in the mesh.<br/>                                              |
| [**GetNumVertices**](id3dxpatchmesh--getnumvertices.md)                         | Gets the number of vertices in the mesh.<br/>                                             |
| [**GetOptions**](id3dxpatchmesh--getoptions.md)                                 | Gets the type of patch.<br/>                                                              |
| [**GetPatchInfo**](id3dxpatchmesh--getpatchinfo.md)                             | Gets the attributes of the patch.<br/>                                                    |
| [**GetTessSize**](id3dxpatchmesh--gettesssize.md)                               | Gets the size of the tessellated mesh, given a tessellation level.<br/>                   |
| [**GetVertexBuffer**](id3dxpatchmesh--getvertexbuffer.md)                       | Gets the mesh vertex buffer.<br/>                                                         |
| [**LockAttributeBuffer**](id3dxpatchmesh--lockattributebuffer.md)               | Locks the attribute buffer.<br/>                                                          |
| [**LockIndexBuffer**](id3dxpatchmesh--lockindexbuffer.md)                       | Lock the index buffer.<br/>                                                               |
| [**LockVertexBuffer**](id3dxpatchmesh--lockvertexbuffer.md)                     | Lock the vertex buffer.<br/>                                                              |
| [**Optimize**](id3dxpatchmesh--optimize.md)                                     | Optimizes the patch mesh for efficient tessellation.<br/>                                 |
| [**SetDisplaceParam**](id3dxpatchmesh--setdisplaceparam.md)                     | Sets mesh geometry displacement parameters.<br/>                                          |
| [**Tessellate**](id3dxpatchmesh--tessellate.md)                                 | Performs uniform tessellation based on the tessellation level.<br/>                       |
| [**TessellateAdaptive**](id3dxpatchmesh--tessellateadaptive.md)                 | Performs adaptive tessellation based on the z-based adaptive tessellation criterion.<br/> |
| [**UnlockAttributeBuffer**](id3dxpatchmesh--unlockattributebuffer.md)           | Unlock the attribute buffer.<br/>                                                         |
| [**UnlockIndexBuffer**](id3dxpatchmesh--unlockindexbuffer.md)                   | Unlock the index buffer.<br/>                                                             |
| [**UnlockVertexBuffer**](id3dxpatchmesh--unlockvertexbuffer.md)                 | Unlock the vertex buffer.<br/>                                                            |



 

## Remarks

A patch mesh is a mesh that consists of a series of patches.

To obtain the **ID3DXPatchMesh** interface, call the [**D3DXCreatePatchMesh**](d3dxcreatepatchmesh.md) function.

The LPD3DXPATCHMESH type is defined as a pointer to the **ID3DXPatchMesh** interface, as follows:


```
typedef struct ID3DXPatchMesh *LPD3DXPATCHMESH;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 
