---
description: Mesh patch types.
ms.assetid: 229d01b2-781c-48a8-93f2-9dd9dbd67f3e
title: D3DXPATCHMESHTYPE enumeration (D3dx9mesh.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXPATCHMESHTYPE
api_type: 
- HeaderDef
api_location: 
- d3dx9mesh.h
---

# D3DXPATCHMESHTYPE enumeration

Mesh patch types.

## Syntax


```C++
typedef enum D3DXPATCHMESHTYPE { 
  D3DXPATCHMESH_RECT         = 0x001,
  D3DXPATCHMESH_TRI          = 0x002,
  D3DXPATCHMESH_NPATCH       = 0x003,
  D3DXPATCHMESH_FORCE_DWORD  = 0x7fffffff
} D3DXPATCHMESHTYPE, *LPD3DXPATCHMESHTYPE;
```



## Constants

<dl> <dt>

<span id="D3DXPATCHMESH_RECT"></span><span id="d3dxpatchmesh_rect"></span>**D3DXPATCHMESH\_RECT**
</dt> <dd>

Rectangle patch mesh type.

</dd> <dt>

<span id="D3DXPATCHMESH_TRI"></span><span id="d3dxpatchmesh_tri"></span>**D3DXPATCHMESH\_TRI**
</dt> <dd>

Triangle patch mesh type.

</dd> <dt>

<span id="D3DXPATCHMESH_NPATCH"></span><span id="d3dxpatchmesh_npatch"></span>**D3DXPATCHMESH\_NPATCH**
</dt> <dd>

N-patch mesh type.

</dd> <dt>

<span id="D3DXPATCHMESH_FORCE_DWORD"></span><span id="d3dxpatchmesh_force_dword"></span>**D3DXPATCHMESH\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

Triangle patches have three sides and are described in [**D3DTRIPATCH\_INFO**](d3dtripatch-info.md). Rectangle patches are four-sided and are described in [**D3DRECTPATCH\_INFO**](d3drectpatch-info.md).

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9mesh.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Enumerations](dx9-graphics-reference-d3dx-enums.md)
</dt> <dt>

[Using Higher-Order Primitives (Direct3D 9)](using-higher-order-primitives.md)
</dt> </dl>

 

 




