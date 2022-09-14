---
description: Specifies simplification options for a mesh.
ms.assetid: f03170bd-7d2a-4839-9aec-c29426b95437
title: D3DXMESHSIMP enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- _D3DXMESHSIMP
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXMESHSIMP enumeration

Specifies simplification options for a mesh.

## Syntax


```C++
enum _D3DXMESHSIMP {
  D3DXMESHSIMP_VERTEX  = 1, 
  D3DXMESHSIMP_FACE    = 2 

};
```



## Constants

<dl> <dt>

<span id="D3DXMESHSIMP_VERTEX"></span><span id="d3dxmeshsimp_vertex"></span>**D3DXMESHSIMP\_VERTEX**
</dt> <dd>

The mesh will be simplified by the number of vertices specified in the MinValue parameter.

</dd> <dt>

<span id="D3DXMESHSIMP_FACE"></span><span id="d3dxmeshsimp_face"></span>**D3DXMESHSIMP\_FACE**
</dt> <dd>

The mesh will be simplified by the number of faces specified in the MinValue parameter.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> <dt>

[**D3DXSimplifyMesh**](d3dxsimplifymesh.md)
</dt> </dl>

 

 




