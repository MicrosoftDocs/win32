---
description: ID3DX10SkinInfo allows you to optimize, process, and manually set the relationship between bones and vertices in your meshes (see Skeletal Animation on Wikipedia).
ms.assetid: bea0fe71-c201-45c6-8036-d0d76d5851fd
title: ID3DX10SkinInfo interface (D3DX10.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DX10SkinInfo
api_type: 
- COM
api_location: 
- D3DX10.lib
- D3DX10.dll
---

# ID3DX10SkinInfo interface

ID3DX10SkinInfo allows you to optimize, process, and manually set the relationship between bones and vertices in your meshes (see [Skeletal Animation on Wikipedia](https://en.wikipedia.org/wiki/Skeletal_animation)). It is most useful for making .x files exported by DCC Apps (such as 3DS Max and Maya) more hardware-friendly, and for improving the render speed of your skinned meshes in software render mode.

## Members

The **ID3DX10SkinInfo** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DX10SkinInfo** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DX10SkinInfo** interface has these methods.



| Method                                                                   | Description                                                                                                                        |
|:-------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**AddBoneInfluences**](id3dx10skininfo-addboneinfluences.md)           | Enable an existing bone to influence a group of vertices and define how much influence the bone has on each vertex.<br/>     |
| [**AddBones**](id3dx10skininfo-addbones.md)                             | Allocate space for more bones.<br/>                                                                                          |
| [**AddVertices**](id3dx10skininfo-addvertices.md)                       | Allocate space for additional vertices.<br/>                                                                                 |
| [**ClearBoneInfluences**](id3dx10skininfo-clearboneinfluences.md)       | Clear a bone's list of vertices that it influences.<br/>                                                                     |
| [**Compact**](id3dx10skininfo-compact.md)                               | Limit the number of bones that can influence a vertex and/or limit the amount of influence a bone can have on a vertex.<br/> |
| [**DoSoftwareSkinning**](id3dx10skininfo-dosoftwareskinning.md)         | Do software skinning on an array of vertices.<br/>                                                                           |
| [**FindBoneInfluenceIndex**](id3dx10skininfo-findboneinfluenceindex.md) | Find the index that indicates where a given vertex is in a given bone's list of influenced vertices.<br/>                    |
| [**GetBoneInfluence**](id3dx10skininfo-getboneinfluence.md)             | Get the amount of influence a given bone has over a given vertex.<br/>                                                       |
| [**GetBoneInfluenceCount**](id3dx10skininfo-getboneinfluencecount.md)   | Get the number of vertices that a given bone influences.<br/>                                                                |
| [**GetBoneInfluences**](id3dx10skininfo-getboneinfluences.md)           | Get a list of vertices that a given bone influences and a list of the amount of influence that bone has on each vertex.<br/> |
| [**GetMaxBoneInfluences**](id3dx10skininfo-getmaxboneinfluences.md)     | Get the number of vertices a bone can maximally influence.<br/>                                                              |
| [**GetNumBones**](id3dx10skininfo-getnumbones.md)                       | Get the number of bones in ID3DX10SkinInfo.<br/>                                                                             |
| [**GetNumVertices**](id3dx10skininfo-getnumvertices.md)                 | Get the number of vertices in ID3DX10SkinInfo.<br/>                                                                          |
| [**RemapBones**](id3dx10skininfo-remapbones.md)                         | Change which bones influence which vertices.<br/>                                                                            |
| [**RemapVertices**](id3dx10skininfo-remapvertices.md)                   | Change which vertices are influenced by which bones.<br/>                                                                    |
| [**RemoveBone**](id3dx10skininfo-removebone.md)                         | Remove a bone.<br/>                                                                                                          |
| [**SetBoneInfluence**](id3dx10skininfo-setboneinfluence.md)             | Set the amount of influence a given bone has over a given vertex.<br/>                                                       |



 

## Remarks

Create a ID3DX10SkinInfo interface with [**D3DX10CreateSkinInfo**](d3d10-d3dx10createskininfo.md), **D3DX10CreateSkinInfoFromBlendedMesh**, or **D3DX10CreateSkinInfoFVF**.

The LPD3DX10SKININFO type is defined as a pointer to the **ID3DX10SkinInfo** interface.


```
typedef struct ID3DX10SkinInfo *LPD3DX10SKININFO;
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX10.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3DX10.lib</dt> </dl> |



## See also

<dl> <dt>

[D3DX Interfaces](d3d10-graphics-reference-d3dx10-interfaces.md)
</dt> </dl>

 

 
