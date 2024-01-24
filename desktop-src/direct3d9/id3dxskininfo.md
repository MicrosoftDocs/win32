---
description: Applications use the methods of the ID3DXSkinInfo interface to manipulate bone matrices, which are used to skin vertex data for animation. This interface is no longer strictly tied to ID3DXMesh and can be used to skin any set of vertex data.
ms.assetid: 4ccf88b0-2cc7-4e91-a0f2-fb8eea66a3ce
title: ID3DXSkinInfo interface (D3DX9Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXSkinInfo
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXSkinInfo interface

Applications use the methods of the ID3DXSkinInfo interface to manipulate bone matrices, which are used to skin vertex data for animation. This interface is no longer strictly tied to [**ID3DXMesh**](id3dxmesh.md) and can be used to skin any set of vertex data.

## Members

The **ID3DXSkinInfo** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXSkinInfo** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXSkinInfo** interface has these methods.



| Method                                                                              | Description                                                                                                                                                                                    |
|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Clone**](id3dxskininfo--clone.md)                                               | Clones a skin info object.<br/>                                                                                                                                                          |
| [**ConvertToBlendedMesh**](id3dxskininfo--converttoblendedmesh.md)                 | Takes a mesh and returns a new mesh with per-vertex blend weights and a bone combination table. The table describes which bones affect which subsets of the mesh.<br/>                   |
| [**ConvertToIndexedBlendedMesh**](id3dxskininfo--converttoindexedblendedmesh.md)   | Takes a mesh and returns a new mesh with per-vertex blend weights, indices, and a bone combination table. The table describes which bone palettes affect which subsets of the mesh.<br/> |
| [**FindBoneVertexInfluenceIndex**](id3dxskininfo--findbonevertexinfluenceindex.md) | Retrieves the index of the bone influence affecting a single vertex.<br/>                                                                                                                |
| [**GetBoneInfluence**](id3dxskininfo--getboneinfluence.md)                         | Gets the vertices and weights that a bone influences.<br/>                                                                                                                               |
| [**GetBoneName**](id3dxskininfo--getbonename.md)                                   | Gets the bone name, from the bone index.<br/>                                                                                                                                            |
| [**GetBoneOffsetMatrix**](id3dxskininfo--getboneoffsetmatrix.md)                   | Gets the bone offset matrix.<br/>                                                                                                                                                        |
| [**GetBoneVertexInfluence**](id3dxskininfo--getbonevertexinfluence.md)             | Retrieves the blend factor and vertex affected by a specified bone influence.<br/>                                                                                                       |
| [**GetDeclaration**](id3dxskininfo--getdeclaration.md)                             | Gets the vertex declaration.<br/>                                                                                                                                                        |
| [**GetFVF**](id3dxskininfo--getfvf.md)                                             | Gets the fixed function vertex value.<br/>                                                                                                                                               |
| [**GetMaxFaceInfluences**](id3dxskininfo--getmaxfaceinfluences.md)                 | Gets the maximum face influences in a triangle mesh with the specified index buffer.<br/>                                                                                                |
| [**GetMaxVertexInfluences**](id3dxskininfo--getmaxvertexinfluences.md)             | Gets the maximum number of influences for any vertex in the mesh.<br/>                                                                                                                   |
| [**GetMinBoneInfluence**](id3dxskininfo--getminboneinfluence.md)                   | Gets the minimum bone influence. Influence values smaller than this are ignored.<br/>                                                                                                    |
| [**GetNumBoneInfluences**](id3dxskininfo--getnumboneinfluences.md)                 | Gets the number of influences for a bone.<br/>                                                                                                                                           |
| [**GetNumBones**](id3dxskininfo--getnumbones.md)                                   | Gets the number of bones.<br/>                                                                                                                                                           |
| [**Remap**](id3dxskininfo--remap.md)                                               | Updates bone influence information to match vertices after they are reordered. This method should be called if the target vertex buffer has been reordered externally.<br/>              |
| [**SetBoneInfluence**](id3dxskininfo--setboneinfluence.md)                         | Sets the influence value for a bone.<br/>                                                                                                                                                |
| [**SetBoneName**](id3dxskininfo--setbonename.md)                                   | Sets the bone name.<br/>                                                                                                                                                                 |
| [**SetBoneOffsetMatrix**](id3dxskininfo--setboneoffsetmatrix.md)                   | Sets the bone offset matrix.<br/>                                                                                                                                                        |
| [**SetBoneVertexInfluence**](id3dxskininfo--setbonevertexinfluence.md)             | Sets an influence value of a bone on a single vertex.<br/>                                                                                                                               |
| [**SetDeclaration**](id3dxskininfo--setdeclaration.md)                             | Sets the vertex declaration.<br/>                                                                                                                                                        |
| [**SetFVF**](id3dxskininfo--setfvf.md)                                             | Sets the flexible vertex format (FVF) type.<br/>                                                                                                                                         |
| [**SetMinBoneInfluence**](id3dxskininfo--setminboneinfluence.md)                   | Sets the minimum bone influence. Influence values smaller than this are ignored.<br/>                                                                                                    |
| [**UpdateSkinnedMesh**](id3dxskininfo--updateskinnedmesh.md)                       | Applies software skinning to the target vertices based on the current matrices.<br/>                                                                                                     |



 

## Remarks

Create a **ID3DXSkinInfo** interface with [**D3DXCreateSkinInfo**](d3dxcreateskininfo.md), [**D3DXCreateSkinInfoFromBlendedMesh**](d3dxcreateskininfofromblendedmesh.md), or [**D3DXCreateSkinInfoFVF**](d3dxcreateskininfofvf.md).

The LPD3DXSKININFO type is defined as a pointer to the **ID3DXSkinInfo** interface.


```
typedef struct ID3DXSkinInfo *LPD3DXSKININFO;
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

 

 
