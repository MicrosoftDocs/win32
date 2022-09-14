---
description: Describes a render surface.
ms.assetid: cffa1555-1fa2-427d-8bcb-da0e61d82152
title: D3DXRTS_DESC structure (D3dx9core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- D3DXRTS_DESC
api_type: 
- HeaderDef
api_location: 
- d3dx9core.h
---

# D3DXRTS\_DESC structure

Describes a render surface.

## Syntax


```C++
typedef struct D3DXRTS_DESC {
  UINT      Width;
  UINT      Height;
  D3DFORMAT Format;
  BOOL      DepthStencil;
  D3DFORMAT DepthStencilFormat;
} D3DXRTS_DESC, *LPD3DXRTS_DESC;
```



## Members

<dl> <dt>

**Width**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Width of the render surface, in pixels.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**UINT**](../winprog/windows-data-types.md)**

</dd> <dd>

Height of the render surface, in pixels.

</dd> <dt>

**Format**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

Member of the [D3DFORMAT](d3dformat.md) enumerated type, describing the pixel format of the render surface.

</dd> <dt>

**DepthStencil**
</dt> <dd>

Type: **[**BOOL**](../winprog/windows-data-types.md)**

</dd> <dd>

If **TRUE**, the render surface supports a depth-stencil surface; otherwise this member is set to **FALSE**.

</dd> <dt>

**DepthStencilFormat**
</dt> <dd>

Type: **[D3DFORMAT](d3dformat.md)**

</dd> <dd>

If DepthStencil is set to **TRUE**, this parameter is a member of the [D3DFORMAT](d3dformat.md) enumerated type, describing the depth-stencil format of the render surface.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3dx9core.h</dt> </dl> |



## See also

<dl> <dt>

[D3DX Structures](dx9-graphics-reference-d3dx-structures.md)
</dt> <dt>

[**ID3DXRenderToSurface::GetDesc**](id3dxrendertosurface--getdesc.md)
</dt> </dl>

 

 
