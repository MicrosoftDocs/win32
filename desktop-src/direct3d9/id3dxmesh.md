---
description: Applications use the methods of the ID3DXMesh interface to manipulate mesh objects.
ms.assetid: f571fe0b-3f0c-43c9-809c-d1e14f85b720
title: ID3DXMesh interface (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXMesh
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXMesh interface

Applications use the methods of the ID3DXMesh interface to manipulate mesh objects.

## Members

The **ID3DXMesh** interface inherits from [**ID3DXBaseMesh**](id3dxbasemesh.md). **ID3DXMesh** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXMesh** interface has these methods.



| Method                                                            | Description                                                                                                                            |
|:------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**LockAttributeBuffer**](id3dxmesh--lockattributebuffer.md)     | Locks the mesh buffer that contains the mesh attribute data, and returns a pointer to it.<br/>                                   |
| [**Optimize**](id3dxmesh--optimize.md)                           | Generates a new mesh with reordered faces and vertices to optimize drawing performance.<br/>                                     |
| [**OptimizeInplace**](id3dxmesh--optimizeinplace.md)             | Generates a mesh with reordered faces and vertices to optimize drawing performance. This method reorders the existing mesh.<br/> |
| [**SetAttributeTable**](id3dxmesh--setattributetable.md)         | Sets the attribute table for a mesh and the number of entries stored in the table.<br/>                                          |
| [**UnlockAttributeBuffer**](id3dxmesh--unlockattributebuffer.md) | Unlocks an attribute buffer.<br/>                                                                                                |



 

## Remarks

To obtain the **ID3DXMesh** interface, call either the [**D3DXCreateMesh**](d3dxcreatemesh.md) or [**D3DXCreateMeshFVF**](d3dxcreatemeshfvf.md) function.

This interface inherits additional functionality from the [**ID3DXBaseMesh**](id3dxbasemesh.md) interface.

The LPD3DXMESH type is defined as a pointer to the **ID3DXMesh** interface.


```
typedef struct ID3DXMesh *LPD3DXMESH;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Mesh.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[**ID3DXBaseMesh**](id3dxbasemesh.md)
</dt> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> <dt>

[Mesh Functions](dx9-graphics-reference-d3dx-functions-mesh.md)
</dt> </dl>

 

 




