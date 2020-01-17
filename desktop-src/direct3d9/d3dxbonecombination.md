---
Description: Describes a subset of the mesh that has the same attribute and bone combination.
ms.assetid: e6a4b3bb-d28d-44c2-a6df-f60f0412a70e
title: D3DXBONECOMBINATION structure (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXBONECOMBINATION
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXBONECOMBINATION structure

Describes a subset of the mesh that has the same attribute and bone combination.

## Syntax


```C++
typedef struct D3DXBONECOMBINATION {
  DWORD AttribId;
  DWORD FaceStart;
  DWORD FaceCount;
  DWORD VertexStart;
  DWORD VertexCount;
  DWORD *BoneId;
} D3DXBONECOMBINATION, *LPD3DXBONECOMBINATION;
```



## Members

<dl> <dt>

**AttribId**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Attribute table identifier.

</dd> <dt>

**FaceStart**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Starting face.

</dd> <dt>

**FaceCount**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Face count.

</dd> <dt>

**VertexStart**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Starting vertex.

</dd> <dt>

**VertexCount**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)**

</dd> <dd>

Vertex count.

</dd> <dt>

**BoneId**
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/library/Aa383751(v=VS.85).aspx)\***

</dd> <dd>

Pointer to an array of values that identify each of the bones that can be drawn in a single drawing call. Note that the array can be of variable length to accommodate variable length bone combinations of [**ConvertToIndexedBlendedMesh**](id3dxskininfo--converttoindexedblendedmesh.md).

The size of the array varies based on the type of mesh generated. A non-indexed mesh array size is equal to the number of weights per vertex (pMaxVertexInfl in [**ConvertToBlendedMesh**](id3dxskininfo--converttoblendedmesh.md)). An indexed mesh array size is equal to the number of bone matrix palette entries (paletteSize in [**ConvertToIndexedBlendedMesh**](id3dxskininfo--converttoindexedblendedmesh.md)).

</dd> </dl>

## Remarks

The subset of the mesh described by **D3DXBONECOMBINATION** can be rendered in a single drawing call.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 




