---
description: Mesh data structure.
ms.assetid: 9164b956-95b7-4bc0-bf7e-feed2e3b4a2b
title: D3DXMESHDATA structure (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMESHDATA
api_type: 
- HeaderDef
api_location: 
- D3dx9anim.h
---

# D3DXMESHDATA structure

Mesh data structure.

## Syntax


```C++
typedef struct D3DXMESHDATA {
  D3DXMESHDATATYPE Type;
  union {
    LPD3DXMESH      pMesh;
    LPD3DXPATCHMESH pPatchMesh;
  };
} D3DXMESHDATA, *LPD3DXMESHDATA;
```



## Members

<dl> <dt>

**Type**
</dt> <dd>

Type: **[**D3DXMESHDATATYPE**](./d3dxmeshdatatype.md)**

</dd> <dd>

Defines the mesh data type. See [**D3DXMESHDATATYPE**](./d3dxmeshdatatype.md).

</dd> <dt>

**pMesh**
</dt> <dd>

Type: **[**LPD3DXMESH**](id3dxmesh.md)**

</dd> <dd>

Pointer to a mesh. See [**ID3DXMesh**](id3dxmesh.md).

</dd> <dt>

**pPatchMesh**
</dt> <dd>

Type: **LPD3DXPATCHMESH**

</dd> <dd>

Pointer to a patch mesh. See [**ID3DXPatchMesh**](id3dxpatchmesh.md).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9anim.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DXMESHCONTAINER**](d3dxmeshcontainer.md)
</dt> </dl>

 

 
