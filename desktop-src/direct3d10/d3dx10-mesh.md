---
description: D3DX10_MESH enumeration - Flags used to specify creation options for a mesh.
ms.assetid: 1a5a6b3f-34f4-4338-9ffe-8f95f6f0c385
title: D3DX10_MESH enumeration (D3DX10Mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DX10_MESH
api_type: 
- HeaderDef
api_location: 
- D3DX10Mesh.h
---

# D3DX10\_MESH enumeration

Flags used to specify creation options for a mesh.

## Syntax


```C++
typedef enum D3DX10_MESH { 
  D3DX10_MESH_32_BIT        = 0x001,
  D3DX10_MESH_GS_ADJACENCY  = 0x004
} D3DX10_MESH, *LPD3DX10_MESH;
```



## Constants

<dl> <dt>

<span id="D3DX10_MESH_32_BIT"></span><span id="d3dx10_mesh_32_bit"></span>**D3DX10\_MESH\_32\_BIT**
</dt> <dd>

The mesh has 32-bit indices instead of 16-bit indices. See Remarks.

</dd> <dt>

<span id="D3DX10_MESH_GS_ADJACENCY"></span><span id="d3dx10_mesh_gs_adjacency"></span>**D3DX10\_MESH\_GS\_ADJACENCY**
</dt> <dd>

Signals that the mesh contains geometry shader adjacency data.

</dd> </dl>

## Remarks

A 32-bit mesh (D3DXMESH\_32BIT) can theoretically support (2³²)-1 faces and vertices. However, allocating memory for a mesh that large on a 32-bit operating system is not practical.

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3DX10Mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](d3d10-graphics-reference-d3dx10-enums.md)
</dt> </dl>

 

 




