---
description: Encapsulates a mesh object in a transformation frame hierarchy.
ms.assetid: 50e98230-7dc3-468a-92c4-8165e8fe242b
title: D3DXMESHCONTAINER structure (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMESHCONTAINER
api_type: 
- HeaderDef
api_location: 
- d3dx9anim.h
---

# D3DXMESHCONTAINER structure

Encapsulates a mesh object in a transformation frame hierarchy.

## Syntax


```C++
typedef struct D3DXMESHCONTAINER {
  LPSTR                Name;
  D3DXMESHDATA         MeshData;
  LPD3DXMATERIAL       pMaterials;
  LPD3DXEFFECTINSTANCE pEffects;
  DWORD                NumMaterials;
  DWORD                *pAdjacency;
  LPD3DXSKININFO       pSkinInfo;
  D3DXMESHCONTAINER    *pNextMeshContainer;
} D3DXMESHCONTAINER, *LPD3DXMESHCONTAINER;
```



## Members

<dl> <dt>

**Name**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Mesh name.

</dd> <dt>

**MeshData**
</dt> <dd>

Type: **[**D3DXMESHDATA**](d3dxmeshdata.md)**

</dd> <dd>

Type of data in the mesh. See [**D3DXMESHDATA**](d3dxmeshdata.md).

</dd> <dt>

**pMaterials**
</dt> <dd>

Type: **[**LPD3DXMATERIAL**](d3dxmaterial.md)**

</dd> <dd>

Array of mesh materials. See [**D3DXMATERIAL**](d3dxmaterial.md).

</dd> <dt>

**pEffects**
</dt> <dd>

Type: **[**LPD3DXEFFECTINSTANCE**](d3dxeffectinstance.md)**

</dd> <dd>

Pointer to a set of default effect parameters. See [**D3DXEFFECTINSTANCE**](d3dxeffectinstance.md).

</dd> <dt>

**NumMaterials**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of materials in the mesh.

</dd> <dt>

**pAdjacency**
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)\***

</dd> <dd>

Pointer to an array of three DWORDs per triangle of the mesh that contains adjacency information.

</dd> <dt>

**pSkinInfo**
</dt> <dd>

Type: **[**LPD3DXSKININFO**](id3dxskininfo.md)**

</dd> <dd>

Pointer to the skin information interface. See [**ID3DXSkinInfo**](id3dxskininfo.md).

</dd> <dt>

**pNextMeshContainer**
</dt> <dd>

Type: ****D3DXMESHCONTAINER**\***

</dd> <dd>

Pointer to the next mesh container.

</dd> </dl>

## Remarks

An application can derive from this structure to add other data.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> </dl>

 

 
