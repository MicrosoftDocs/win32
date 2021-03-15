---
description: Returns material information saved in Direct3D (.x) files.
ms.assetid: dfa021ba-61d8-4f99-9bbb-0cfbe11b787d
title: D3DXMATERIAL structure (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXMATERIAL
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXMATERIAL structure

Returns material information saved in Direct3D (.x) files.

## Syntax


```C++
typedef struct D3DXMATERIAL {
  D3DMATERIAL9 MatD3D;
  LPSTR        pTextureFilename;
} D3DXMATERIAL, *LPD3DXMATERIAL;
```



## Members

<dl> <dt>

**MatD3D**
</dt> <dd>

Type: **[**D3DMATERIAL9**](d3dmaterial9.md)**

</dd> <dd>

[**D3DMATERIAL9**](d3dmaterial9.md) structure that describes the material properties.

</dd> <dt>

**pTextureFilename**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Pointer to a string that specifies the file name of the texture.

</dd> </dl>

## Remarks

The [**D3DXLoadMeshFromX**](d3dxloadmeshfromx.md) and [**D3DXLoadMeshFromXof**](d3dxloadmeshfromxof.md) functions return an array of **D3DXMATERIAL** structures that specify the material color and name of the texture for each material in the mesh. The application is then required to load the texture.

The LPD3DXMATERIAL type is defined as a pointer to the **D3DXMATERIAL** structure.


```
typedef struct D3DXMATERIAL* LPD3DXMATERIAL;
```



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**D3DXLoadMeshFromX**](d3dxloadmeshfromx.md)
</dt> <dt>

[**D3DXLoadMeshFromXof**](d3dxloadmeshfromxof.md)
</dt> </dl>

 

 




