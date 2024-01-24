---
description: Specifies the source glyph and location in a monochrome surface to copy glyphs into.
ms.assetid: eda6fc82-6a06-4a59-a3ab-9f7e5c5bb5a1
title: D3DCOMPOSERECTDESTINATION structure (D3d9types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DCOMPOSERECTDESTINATION
api_type:
- HeaderDef
api_location:
- d3d9types.h
---

# D3DCOMPOSERECTDESTINATION structure

Specifies the source glyph and location in a monochrome surface to copy glyphs into.

## Syntax


```C++
typedef struct _D3DCOMPOSERECTDESTINATION {
  USHORT SrcRectIndex;
  USHORT Reserved;
  USHORT X;
  USHORT Y;
} D3DCOMPOSERECTDESTINATION;
```



## Members

<dl> <dt>

**SrcRectIndex**
</dt> <dd>

Type: **[**USHORT**](../winprog/windows-data-types.md)**

</dd> <dd>

Index particular glyph from vertex buffer containing [**D3DCOMPOSERECTDESC**](d3dcomposerectdesc.md) structures.

</dd> <dt>

**Reserved**
</dt> <dd>

Type: **[**USHORT**](../winprog/windows-data-types.md)**

</dd> <dd>

Reserved for alignment purposes.

</dd> <dt>

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

</dd> </dl>

## Remarks

This structure is used in calls to [**ComposeRects**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9ex-composerects) to indicate the location glyphs should be copied to and which particular glyph should be copied. A vertex buffer (see [**IDirect3DVertexBuffer9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dvertexbuffer9)) filled with these structures are created to contain the glyph locations. USHORT members are used to reduce the memory footprint as much as possible.

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 
