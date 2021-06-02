---
description: Specifies the rectangle used to enclose glyphs on a monochrome surface.
ms.assetid: ce5d492f-38d1-4e7b-a9c2-68c791c84d0c
title: D3DCOMPOSERECTDESC structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DCOMPOSERECTDESC
api_type:
- HeaderDef
api_location:
- d3d9types.h
---

# D3DCOMPOSERECTDESC structure

Specifies the rectangle used to enclose glyphs on a monochrome surface.

## Syntax


```C++
typedef struct _D3DCOMPOSERECTDESC {
  USHORT X;
  USHORT Y;
  USHORT Width;
  USHORT Height;
} D3DCOMPOSERECTDESC;
```



## Members

<dl> <dt>

**X**
</dt> <dd>

Type: **[**USHORT**](../winprog/windows-data-types.md)**

</dd> <dd>

Left coordinate to begin copy at.

</dd> <dt>

**Y**
</dt> <dd>

Type: **[**USHORT**](../winprog/windows-data-types.md)**

</dd> <dd>

Top coordinate to begin copy at.

</dd> <dt>

**Width**
</dt> <dd>

Type: **[**USHORT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of texels from left coordinate.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**USHORT**](../winprog/windows-data-types.md)**

</dd> <dd>

Number of texels from the top coordinate.

</dd> </dl>

## Remarks

This structure is used in calls to [**ComposeRects**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9ex-composerects) to enclose glyphs on the source surface. A vertex buffer (see [**IDirect3DVertexBuffer9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dvertexbuffer9)) filled with these structures are created to contain the glyph locations. USHORT members are used to reduce the memory footprint as much as possible.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 
