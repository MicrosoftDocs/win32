---
Description: 'Specifies the rectangle used to enclose glyphs on a monochrome surface.'
ms.assetid: 'ce5d492f-38d1-4e7b-a9c2-68c791c84d0c'
title: D3DCOMPOSERECTDESC structure
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

Type: **[**USHORT**](winprog.windows_data_types)**

</dd> <dd>

Left coordinate to begin copy at.

</dd> <dt>

**Y**
</dt> <dd>

Type: **[**USHORT**](winprog.windows_data_types)**

</dd> <dd>

Top coordinate to begin copy at.

</dd> <dt>

**Width**
</dt> <dd>

Type: **[**USHORT**](winprog.windows_data_types)**

</dd> <dd>

Number of texels from left coordinate.

</dd> <dt>

**Height**
</dt> <dd>

Type: **[**USHORT**](winprog.windows_data_types)**

</dd> <dd>

Number of texels from the top coordinate.

</dd> </dl>

## Remarks

This structure is used in calls to [**ComposeRects**](idirect3ddevice9ex-composerect.md) to enclose glyphs on the source surface. A vertex buffer (see [**IDirect3DVertexBuffer9**](idirect3dvertexbuffer9.md)) filled with these structures are created to contain the glyph locations. USHORT members are used to reduce the memory footprint as much as possible.

## Requirements



|                   |                                                                                        |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3d9types.h</dt> </dl> |



## See also

<dl> <dt>

[Direct3D Structures](dx9-graphics-reference-d3d-structures.md)
</dt> </dl>

 

 




